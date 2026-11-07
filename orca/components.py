"""Server-side helpers behind ORCA's component template tags.

The tags move the fiddly, easy-to-get-wrong parts into the system (Tesler's law): ids and
``aria-describedby`` wiring for form fields, page windows with gaps, month grids that respect the locale's
first weekday, and chart geometry.
"""

from __future__ import annotations

import calendar
import copy
import datetime as dt
from urllib.parse import urlencode

from django import forms
from django.utils import formats, timezone

TONES = {"success": "positive", "error": "negative", "warning": "caution", "info": "info", "debug": "info"}
STATUS_TITLES = {"positive": "Done", "negative": "Something went wrong", "caution": "Check this", "info": "Note"}


# ---------------------------------------------------------------------------------------------- form fields

def _kind(widget) -> str:
    if isinstance(widget, forms.CheckboxSelectMultiple):
        return "checkboxes"
    if isinstance(widget, forms.RadioSelect):
        return "radios"
    if isinstance(widget, forms.CheckboxInput):
        return "checkbox"
    if isinstance(widget, forms.SelectMultiple):
        return "listbox"
    if isinstance(widget, forms.Select):
        return "select"
    if isinstance(widget, forms.Textarea):
        return "textarea"
    if isinstance(widget, forms.FileInput):
        return "file"
    if isinstance(widget, forms.HiddenInput):
        return "hidden"
    return "input"


_NATIVE_TYPES = {forms.DateTimeInput: ("datetime-local", "%Y-%m-%dT%H:%M"), forms.DateInput: ("date", "%Y-%m-%d"),
                 forms.TimeInput: ("time", "%H:%M")}


def field_context(bf, switch: bool = False, width: str = "", label: str | None = None, help_text: str | None = None,
                  hide_label: bool = False, horizontal: bool = False) -> dict:
    """Everything the orca/components/field.html template needs for one bound field."""
    widget = bf.field.widget
    kind = _kind(widget)
    fid = bf.id_for_label or bf.auto_id or bf.html_name
    help_id, error_id = f"{fid}-help", f"{fid}-error"
    help_text = bf.help_text if help_text is None else help_text
    errors = list(bf.errors)
    described = " ".join(i for i, on in ((error_id, errors), (help_id, help_text)) if on)
    attrs = {}
    if described:
        attrs["aria-describedby"] = described
    if errors:
        attrs["aria-invalid"] = "true"

    control = ""
    native = widget
    for cls, (input_type, fmt) in _NATIVE_TYPES.items():
        if isinstance(widget, cls) and getattr(widget, "input_type", "") == "text":
            native = copy.copy(widget)
            native.input_type, native.format = input_type, fmt
            break
    if kind in ("input", "textarea", "select", "listbox", "file"):
        css = {"input": "orca-input", "textarea": "orca-textarea", "select": "orca-select",
               "listbox": "orca-select orca-listbox", "file": "orca-file"}[kind]
        if width and kind == "input":
            css += f" orca-input--{width}"
        attrs["class"] = (widget.attrs.get("class", "") + " " + css).strip()
        control = bf.as_widget(widget=native, attrs=attrs)
    elif kind == "checkbox":
        if switch:
            attrs["role"] = "switch"
        control = bf.as_widget(attrs=attrs)
    elif kind == "hidden":
        control = bf.as_widget()

    options = []
    if kind in ("radios", "checkboxes"):
        for sub in bf.subwidgets:
            options.append({"tag": sub.tag(), "label": sub.choice_label, "id": sub.id_for_label})
    return {
        "bf": bf, "kind": kind, "control": control, "options": options, "switch": switch,
        "label": bf.label if label is None else label, "hide_label": hide_label, "required": bf.field.required,
        "help_text": help_text, "help_id": help_id, "errors": errors, "error_id": error_id, "id": fid,
        "described": described, "horizontal": horizontal,
    }


def form_errors_context(form) -> dict:
    field_errors = [(form[name].id_for_label or form[name].auto_id, form[name].label, err)
                    for name, errs in form.errors.items() if name != forms.forms.NON_FIELD_ERRORS and name in form.fields
                    for err in errs[:1]]
    return {"non_field": list(form.non_field_errors()), "field_errors": field_errors, "count": len(field_errors)}


# ---------------------------------------------------------------------------------------------- messages

def messages_context(context) -> dict:
    msgs = context.get("messages")
    if msgs is None and context.get("request") is not None:
        from django.contrib.messages import get_messages

        msgs = get_messages(context["request"])
    items = []
    for m in msgs or []:
        level = (getattr(m, "level_tag", "") or "info").split()[0]
        tone = TONES.get(level, "info")
        items.append({"tone": tone, "text": str(m), "role": "alert" if tone == "negative" else "status"})
    return {"messages_list": items}


# ---------------------------------------------------------------------------------------------- pagination

def page_window(current: int, last: int, around: int = 1) -> list[int | None]:
    """Page numbers to show, None where a gap goes: 1 … 6 7 8 … 24. Seven pages or fewer: all of them."""
    if last <= 7:
        return list(range(1, last + 1))
    keep = {1, last} | set(range(max(1, current - around), min(last, current + around) + 1))
    if current <= 3:
        keep |= set(range(1, min(last, 4) + 1))
    if current >= last - 2:
        keep |= set(range(max(1, last - 3), last + 1))
    out: list[int | None] = []
    prev = 0
    for n in sorted(keep):
        if n - prev > 1:
            out.append(None if n - prev > 2 else n - 1)
        out.append(n)
        prev = n
    return out


def pagination_context(context, page_obj, noun: str = "items", param: str = "page") -> dict:
    request = context.get("request")
    query = request.GET.copy() if request is not None else {}

    def href(n: int) -> str:
        q = query.copy() if hasattr(query, "copy") else {}
        q[param] = n
        return "?" + (q.urlencode() if hasattr(q, "urlencode") else urlencode(q))

    paginator = page_obj.paginator
    pages = [{"n": n, "href": href(n) if n else "", "current": n == page_obj.number} for n in
             page_window(page_obj.number, paginator.num_pages)]
    return {
        "page_obj": page_obj, "pages": pages, "noun": noun, "count": paginator.count,
        "start": page_obj.start_index(), "end": page_obj.end_index(),
        "prev_href": href(page_obj.previous_page_number()) if page_obj.has_previous() else "",
        "next_href": href(page_obj.next_page_number()) if page_obj.has_next() else "",
        "single": paginator.num_pages <= 1,
    }


# ---------------------------------------------------------------------------------------------- calendar

def _to_date(value) -> dt.date | None:
    if value in (None, ""):
        return None
    if isinstance(value, dt.datetime):
        return timezone.localtime(value).date() if timezone.is_aware(value) else value.date()
    if isinstance(value, dt.date):
        return value
    text = str(value)
    if len(text) == 7:  # "YYYY-MM" means the first of the month (as in ?month=2026-11)
        text += "-01"
    return dt.date.fromisoformat(text[:10])


def mini_calendar_context(month=None, selected=None, today=None, url: str = "", nav_url: str = "",
                          events=(), holidays=None, week_numbers: bool = False) -> dict:
    """A month grid. ``url`` and ``nav_url`` are patterns with ``{date}`` (YYYY-MM-DD) and ``{month}`` (YYYY-MM)."""
    today = _to_date(today) or timezone.localdate()
    month = _to_date(month) or _to_date(selected) or today
    selected = _to_date(selected)
    first = month.replace(day=1)
    django_first = int(formats.get_format("FIRST_DAY_OF_WEEK") or 0)  # 0 = Sunday in Django
    cal = calendar.Calendar(firstweekday=(django_first - 1) % 7)
    if isinstance(events, str):
        events = [e for e in events.split(",") if e.strip()]
    event_days = {_to_date(e.strip() if isinstance(e, str) else e) for e in events}
    holidays = {(_to_date(k)): v for k, v in (holidays or {}).items()}
    weeks = []
    for week in cal.monthdatescalendar(first.year, first.month):
        days = []
        for d in week:
            label = formats.date_format(d, "l j F Y")
            notes = []
            if d == today:
                notes.append("today")
            if d in holidays:
                notes.append(holidays[d])
            if d in event_days:
                notes.append("has events")
            days.append({
                "date": d, "iso": d.isoformat(), "day": d.day, "outside": d.month != first.month,
                "today": d == today, "selected": d == selected, "weekend": d.weekday() >= 5,
                "holiday": holidays.get(d, ""), "events": d in event_days,
                "href": url.replace("{date}", d.isoformat()) if url else "",
                "label": label + (", " + ", ".join(notes) if notes else ""),
            })
        weeks.append({"number": week[0].isocalendar()[1], "days": days})
    prev_month = (first - dt.timedelta(days=1)).replace(day=1)
    next_month = (first + dt.timedelta(days=32)).replace(day=1)
    weekdays = [{"short": formats.date_format(d, "D"), "long": formats.date_format(d, "l"), "weekend": d.weekday() >= 5}
                for d in (x["date"] for x in weeks[0]["days"])]
    return {
        "title": formats.date_format(first, "YEAR_MONTH_FORMAT"), "month_iso": first.strftime("%Y-%m"),
        "weeks": weeks, "weekdays": weekdays, "week_numbers": week_numbers,
        "prev_href": nav_url.replace("{month}", prev_month.strftime("%Y-%m")) if nav_url else "",
        "next_href": nav_url.replace("{month}", next_month.strftime("%Y-%m")) if nav_url else "",
        "prev_label": formats.date_format(prev_month, "YEAR_MONTH_FORMAT"),
        "next_label": formats.date_format(next_month, "YEAR_MONTH_FORMAT"),
    }


# ---------------------------------------------------------------------------------------------- charts

def _numbers(values) -> list[float]:
    if isinstance(values, str):
        values = [v for v in values.replace(";", ",").split(",") if v.strip()]
    return [float(v) for v in values]


def sparkline_svg(values, label: str = "", width: int = 120, height: int = 32) -> str:
    nums = _numbers(values)
    if len(nums) < 2:
        return ""
    lo, hi = min(nums), max(nums)
    span = (hi - lo) or 1
    step = width / (len(nums) - 1)
    pts = [(round(i * step, 2), round(height - 2 - (v - lo) / span * (height - 4), 2)) for i, v in enumerate(nums)]
    line = " ".join(f"{x},{y}" for x, y in pts)
    area = f"0,{height} " + line + f" {width},{height}"
    end_x, end_y = pts[-1]
    title = label or f"Trend from {nums[0]:g} to {nums[-1]:g}, low {lo:g}, high {hi:g}"
    return (f'<svg class="orca-sparkline" viewBox="0 0 {width} {height}" preserveAspectRatio="none" role="img" aria-label="{title}">'
            f'<polygon class="orca-sparkline__area" points="{area}"/><polyline class="orca-sparkline__line" points="{line}"/>'
            f'<circle class="orca-sparkline__end" cx="{end_x}" cy="{end_y}" r="2.5"/></svg>')


def donut_context(segments, total_label: str = "Total") -> dict:
    if isinstance(segments, str):
        segments = [tuple(part.rsplit(":", 1)) for part in segments.split(",") if ":" in part]
        segments = [(label.strip(), value.strip()) for label, value in segments]
    items = []
    for i, seg in enumerate(segments):
        if isinstance(seg, dict):
            label, value = seg["label"], seg["value"]
        else:
            label, value = seg
        items.append({"label": label, "value": float(value), "color": f"var(--orca-chart-{i % 8 + 1})"})
    total = sum(i["value"] for i in items) or 1
    r = 15.9155
    offset = 0.0
    for item in items:
        share = item["value"] / total * 100
        item.update(pct=round(share), dash=f"{share:.3f} {100 - share:.3f}", offset=f"{-offset:.3f}")
        offset += share
    def fmt(v: float) -> str:
        return formats.number_format(int(v) if v == int(v) else round(v, 1), force_grouping=True)

    for item in items:
        item["display"] = fmt(item["value"])
    shown_total = sum(i["value"] for i in items)
    return {"items": items, "total": fmt(shown_total),
            "total_label": total_label, "r": r,
            "summary": ", ".join(f"{i['label']} {i['pct']}%" for i in items)}
