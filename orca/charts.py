"""Chart data for ORCA's chart patterns, drawn by Chart.js.

The server parses the data, writes the legend, the summary for screen readers and the data table, and hands a
small JSON spec to the canvas. ``orca.js`` loads the vendored Chart.js only on pages with charts and draws the
spec in token colours (``--orca-chart-1`` to ``-8``), redrawing when the theme changes. Without JavaScript the
legend and the data table still carry every value. Data is a dict or a compact string:

    {"labels": ["Mon", "Tue"], "series": [{"name": "Entrance A", "values": [120, 180]}]}
    "labels=Mon,Tue | Entrance A=120,180 | Entrance B=90,110"
    scatter / bubble values are points: "Weekdays=12:340,14:410" or "Sites=12:340:6" (x:y[:size])
"""

from __future__ import annotations

import json

from django.utils import formats

KINDS = ("bar", "line", "area", "pie", "doughnut", "scatter", "bubble", "radar", "polar")


def _num(v) -> float:
    return float(str(v).strip())


def parse(data) -> dict:
    if isinstance(data, dict):
        out = {"labels": [str(x) for x in data.get("labels", [])], "series": []}
        for s in data.get("series", []):
            out["series"].append({"name": str(s.get("name", "")), "values": list(s.get("values", []))})
        return out
    labels, series = [], []
    for part in str(data or "").split("|"):
        if "=" not in part:
            continue
        key, values = part.split("=", 1)
        items = [v.strip() for v in values.split(",") if v.strip()]
        if key.strip() == "labels":
            labels = items
        else:
            parsed = [tuple(_num(x) for x in v.split(":")) if ":" in v else _num(v) for v in items]
            series.append({"name": key.strip(), "values": parsed})
    return {"labels": labels, "series": series}


def fmt(v: float) -> str:
    return formats.number_format(int(v) if float(v).is_integer() else round(v, 1), force_grouping=True)


def _color(i: int) -> str:
    return f"--c: var(--orca-chart-{i % 8 + 1})"


def _summary(kind, d, unit) -> str:
    if kind in ("pie", "doughnut", "polar"):
        vals = d["series"][0]["values"] if d["series"] else []
        total = sum(vals) or 1
        return "; ".join(f"{lab} {fmt(v)}{unit} ({round(v / total * 100)}%)" for lab, v in zip(d["labels"], vals))
    if kind in ("scatter", "bubble"):
        return "; ".join(f"{s['name']}: {len(s['values'])} points" for s in d["series"])
    parts = []
    for s in d["series"]:
        vals = s["values"]
        if vals:
            hi = max(range(len(vals)), key=lambda i: vals[i])
            lo = min(range(len(vals)), key=lambda i: vals[i])
            parts.append(f"{s['name']}: highest {fmt(vals[hi])}{unit} at {d['labels'][hi]}, lowest {fmt(vals[lo])}{unit} at {d['labels'][lo]}")
    return "; ".join(parts)


def chart_context(kind: str, data, title="", subtitle="", caption="", unit="", stacked=False, horizontal=False) -> dict:
    if kind not in KINDS:
        raise ValueError(f"Unknown chart kind {kind!r}. Use one of: {', '.join(KINDS)}.")
    d = parse(data)
    spec = {"kind": kind, "labels": d["labels"], "unit": unit, "stacked": bool(stacked), "horizontal": bool(horizontal),
            "series": [{"name": s_["name"], "values": [list(v) if isinstance(v, tuple) else v for v in s_["values"]]} for s_ in d["series"]]}
    round_chart = kind in ("pie", "doughnut", "polar")
    if round_chart:
        vals = d["series"][0]["values"] if d["series"] else []
        total = sum(vals) or 1
        legend = [{"name": lab, "style": _color(i), "value": f"{fmt(v)}{unit} · {round(v / total * 100)}%"}
                  for i, (lab, v) in enumerate(zip(d["labels"], vals))]
    else:
        legend = [{"name": s["name"], "style": _color(i), "value": ""} for i, s in enumerate(d["series"])]
    point = kind in ("scatter", "bubble")
    if point:
        head = ["Series", "x", "y"] + (["Size"] if kind == "bubble" else [])
        rows = [[s["name"]] + [fmt(v) for v in p] for s in d["series"] for p in s["values"]]
    else:
        head = [""] + [s["name"] for s in d["series"]]
        rows = [[lab] + [fmt(s["values"][i]) + unit for s in d["series"]] for i, lab in enumerate(d["labels"])]
    return {"kind": kind, "spec": json.dumps(spec, ensure_ascii=False), "summary": _summary(kind, d, unit), "title": title, "subtitle": subtitle, "caption": caption, "legend": legend,
            "show_legend": round_chart or len(d["series"]) > 1 or point, "head": head, "rows": rows, "round": round_chart}
