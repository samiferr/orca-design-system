"""Server-side layout for ORCA's calendar view patterns.

Events are plain dicts (or objects with the same attributes)::

    {"title": "Delivery", "start": datetime | date | "2026-11-06T09:00", "end": …, "all_day": False,
     "color": 1..8 (chart colour) or a CSS colour token, "url": "/events/12/", "location": "Loading dock",
     "status": "tentative" | "cancelled" | ""}

The views compute everything a template needs: which days, which events on each, where timed events sit in
the day columns (top, height and side-by-side lanes for overlaps), and the accessible description of each.
"""

from __future__ import annotations

import calendar
import datetime as dt

from django.utils import formats, timezone

from .components import _to_date, mini_calendar_context


def _get(e, key, default=None):
    return e.get(key, default) if isinstance(e, dict) else getattr(e, key, default)


def _to_dt(value) -> dt.datetime | None:
    if value in (None, ""):
        return None
    if isinstance(value, str):
        value = dt.datetime.fromisoformat(value) if "T" in value or " " in value else dt.date.fromisoformat(value)
    if isinstance(value, dt.datetime):
        return timezone.localtime(value).replace(tzinfo=None) if timezone.is_aware(value) else value
    return dt.datetime.combine(value, dt.time())


def _color(c) -> str:
    if c in (None, ""):
        return "var(--orca-chart-1)"
    if isinstance(c, int) or str(c).isdigit():
        return f"var(--orca-chart-{(int(c) - 1) % 8 + 1})"
    return str(c)


def normalize(events) -> list[dict]:
    out = []
    for e in events or []:
        start = _to_dt(_get(e, "start"))
        if start is None:
            continue
        end = _to_dt(_get(e, "end")) or start
        all_day = bool(_get(e, "all_day", False)) or (isinstance(_get(e, "start"), dt.date) and not isinstance(_get(e, "start"), dt.datetime)) \
            or (isinstance(_get(e, "start"), str) and "T" not in _get(e, "start"))
        if all_day and end <= start:
            end = start
        status = _get(e, "status", "") or ""
        title = str(_get(e, "title", ""))
        time_text = "All day" if all_day else f"{formats.time_format(start, 'TIME_FORMAT')}–{formats.time_format(end, 'TIME_FORMAT')}"
        out.append({
            "title": title, "start": start, "end": end, "all_day": all_day, "color": _color(_get(e, "color")),
            "url": _get(e, "url", "") or "", "location": _get(e, "location", "") or "", "status": status,
            "start_time": formats.time_format(start, "TIME_FORMAT"), "time_text": time_text,
            "label": ", ".join(x for x in (title, time_text, _get(e, "location", "") or "", status) if x),
        })
    return sorted(out, key=lambda e: (not e["all_day"], e["start"], e["title"]))


def _on_day(e, day: dt.date) -> bool:
    if e["all_day"]:
        return e["start"].date() <= day <= e["end"].date()
    return e["start"].date() <= day <= (e["end"] - dt.timedelta(seconds=1)).date() if e["end"] > e["start"] else e["start"].date() == day


def _first_weekday() -> int:
    return (int(formats.get_format("FIRST_DAY_OF_WEEK") or 0) - 1) % 7


def month_context(events=(), month=None, today=None, selected=None, day_url="", max_per_day=3, holidays=None) -> dict:
    evs = normalize(events)
    today = _to_date(today) or timezone.localdate()
    first = (_to_date(month) or today).replace(day=1)
    holidays = {_to_date(k): v for k, v in (holidays or {}).items()}
    cal = calendar.Calendar(firstweekday=_first_weekday())
    weeks = []
    for week in cal.monthdatescalendar(first.year, first.month):
        days = []
        for d in week:
            todays = [e for e in evs if _on_day(e, d)]
            label = formats.date_format(d, "l j F")
            days.append({
                "date": d, "iso": d.isoformat(), "day": d.day, "outside": d.month != first.month, "today": d == today,
                "selected": d == _to_date(selected), "weekend": d.weekday() >= 5, "holiday": holidays.get(d, ""),
                "events": todays[:max_per_day], "more": max(len(todays) - max_per_day, 0), "count": len(todays),
                "href": day_url.replace("{date}", d.isoformat()) if day_url else "",
                "label": label + (", today" if d == today else "") + (f", {holidays[d]}" if d in holidays else "")
                + (f", {len(todays)} event{'s' if len(todays) != 1 else ''}" if todays else ""),
            })
        weeks.append({"number": week[0].isocalendar()[1], "days": days})
    weekdays = [{"short": formats.date_format(x["date"], "D"), "long": formats.date_format(x["date"], "l"), "weekend": x["weekend"]}
                for x in weeks[0]["days"]]
    return {"title": formats.date_format(first, "YEAR_MONTH_FORMAT"), "weeks": weeks, "weekdays": weekdays,
            "month_iso": first.strftime("%Y-%m")}


def time_grid_context(events=(), start=None, days=7, start_hour=7, end_hour=19, today=None, now=None) -> dict:
    """Day, multi-day and week views: columns of days with positioned events."""
    evs = normalize(events)
    today = _to_date(today) or timezone.localdate()
    start = _to_date(start) or today
    if days == 7 and start.weekday() != _first_weekday():
        start -= dt.timedelta(days=(start.weekday() - _first_weekday()) % 7)
    span_min = (end_hour - start_hour) * 60
    dates = [start + dt.timedelta(days=i) for i in range(days)]
    columns, allday = [], []
    for col, d in enumerate(dates):
        timed = sorted((e for e in evs if not e["all_day"] and e["start"].date() == d), key=lambda e: (e["start"], -e["end"].timestamp()))
        # Split the day into clusters of events that overlap each other; only a cluster shares its width.
        clusters: list[list[dt.datetime | list]] = []
        for e in timed:
            if clusters and e["start"] < clusters[-1][0]:
                clusters[-1][0] = max(clusters[-1][0], e["end"])
                clusters[-1][1].append(e)
            else:
                clusters.append([e["end"], [e]])
        placed = []
        for _, members in clusters:
            lanes: list[dt.datetime] = []
            group = []
            for e in members:
                lane = next((i for i, end in enumerate(lanes) if end <= e["start"]), None)
                if lane is None:
                    lanes.append(e["end"])
                    lane = len(lanes) - 1
                else:
                    lanes[lane] = e["end"]
                group.append((e, lane))
            placed += [(e, lane, 100 / len(lanes)) for e, lane in group]
        items = []
        for e, lane, width in placed:
            s_min = (e["start"].hour - start_hour) * 60 + e["start"].minute
            e_min = (e["end"].hour - start_hour) * 60 + e["end"].minute if e["end"].date() == d else span_min
            s_min, e_min = max(s_min, 0), min(max(e_min, s_min + 15), span_min)
            items.append(dict(e, top=round(s_min / span_min * 100, 3), height=round((e_min - s_min) / span_min * 100, 3),
                              left=round(lane * width, 3), width=round(width, 3), short=(e_min - s_min) < 45))
        columns.append({"date": d, "iso": d.isoformat(), "today": d == today, "weekend": d.weekday() >= 5, "events": items,
                        "weekday": formats.date_format(d, "D"), "day": d.day,
                        "label": formats.date_format(d, "l j F") + (", today" if d == today else "")})
    for e in evs:
        if not e["all_day"]:
            continue
        s, en = e["start"].date(), e["end"].date()
        if en < dates[0] or s > dates[-1]:
            continue
        c0 = max((s - dates[0]).days, 0)
        c1 = min((en - dates[0]).days, days - 1)
        allday.append(dict(e, col=c0 + 1, span=c1 - c0 + 1, before=s < dates[0], after=en > dates[-1]))
    if now:
        now_dt = _to_dt(now)
    else:
        current = timezone.now()
        now_dt = timezone.localtime(current).replace(tzinfo=None) if timezone.is_aware(current) else current
    now_pos = None
    if now_dt and now_dt.date() in dates:
        m = (now_dt.hour - start_hour) * 60 + now_dt.minute
        if 0 <= m <= span_min:
            now_pos = {"col": dates.index(now_dt.date()), "top": round(m / span_min * 100, 3)}
    hours = [{"hour": h, "label": formats.time_format(dt.time(h, 0), "TIME_FORMAT")} for h in range(start_hour, end_hour)]
    first, last = dates[0], dates[-1]
    title = formats.date_format(first, "l j F Y") if days == 1 else (
        f"{first.day}–{formats.date_format(last, 'j F Y')}" if first.month == last.month
        else f"{formats.date_format(first, 'j F')} – {formats.date_format(last, 'j F Y')}")
    return {"columns": columns, "allday": allday, "hours": hours, "days": days, "now": now_pos, "title": title,
            "rows": len(hours) * 2, "week": first.isocalendar()[1]}


def agenda_context(events=(), start=None, days=7, today=None) -> dict:
    evs = normalize(events)
    today = _to_date(today) or timezone.localdate()
    start = _to_date(start) or today
    out = []
    for i in range(days):
        d = start + dt.timedelta(days=i)
        todays = [e for e in evs if _on_day(e, d)]
        if todays:
            out.append({"date": d, "iso": d.isoformat(), "today": d == today, "events": todays,
                        "month": formats.date_format(d, "M"), "weekday": formats.date_format(d, "D"), "day": d.day,
                        "label": formats.date_format(d, "l j F") + (", today" if d == today else "")})
    return {"days": out}


def year_context(year=None, events=(), today=None, url="") -> dict:
    today = _to_date(today) or timezone.localdate()
    year = int(year or today.year)
    evs = normalize(events)
    event_days = sorted({e["start"].date() for e in evs})
    months = [mini_calendar_context(month=dt.date(year, m, 1), today=today, url=url, events=event_days) for m in range(1, 13)]
    return {"year": year, "months": months}
