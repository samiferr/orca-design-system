"""Server-rendered SVG charts for ORCA's chart patterns.

No JavaScript and no chart library: the server draws an accessible SVG in token colours, and every chart
comes with its data as a table. Data is a dict or a compact string:

    {"labels": ["Mon", "Tue"], "series": [{"name": "Entrance A", "values": [120, 180]}]}
    "labels=Mon,Tue | Entrance A=120,180 | Entrance B=90,110"
    scatter / bubble values are points: "Weekdays=12:340,14:410" or "Sites=12:340:6" (x:y[:size])
"""

from __future__ import annotations

import math
from html import escape

from django.utils import formats

W, H = 480, 240
PAD_L, PAD_R, PAD_T, PAD_B = 44, 12, 12, 28
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


def nice_ticks(lo: float, hi: float, count: int = 5) -> list[float]:
    if hi <= lo:
        hi = lo + 1
    raw = (hi - lo) / count
    mag = 10 ** math.floor(math.log10(raw))
    step = next(m * mag for m in (1, 2, 2.5, 5, 10) if m * mag >= raw)
    start = math.floor(lo / step) * step
    ticks = []
    v = start
    while v <= hi + step * 0.001:
        ticks.append(round(v, 10))
        v += step
    if ticks[-1] < hi:
        ticks.append(ticks[-1] + step)
    return ticks


def _color(i: int) -> str:
    return f"--c: var(--orca-chart-{i % 8 + 1})"


def _t(x, y, text, cls="orca-chart__label", anchor="middle", extra="") -> str:
    return f'<text class="{cls}" x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}"{extra}>{escape(str(text))}</text>'


def _axes_y(ticks, y_of, x0=PAD_L, x1=W - PAD_R, unit="") -> list[str]:
    out = []
    for t in ticks:
        y = y_of(t)
        out.append(f'<line class="orca-chart__grid" x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}"/>')
        out.append(_t(x0 - 6, y + 4, fmt(t) + unit, anchor="end"))
    return out


def _svg(body: list[str], label: str, w: int = W, h: int = H) -> str:
    return (f'<svg class="orca-chart" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}" preserveAspectRatio="xMidYMid meet">'
            + "".join(body) + "</svg>")


def bar_svg(d, stacked=False, horizontal=False, unit="") -> str:
    labels, series = d["labels"], d["series"]
    n, m = len(labels), max(len(series), 1)
    totals = [sum(s["values"][i] for s in series) for i in range(n)] if stacked else []
    hi = max(totals or [v for s in series for v in s["values"]] or [1])
    ticks = nice_ticks(0, hi)
    top = ticks[-1]
    body = []
    if horizontal:
        x0, x1 = PAD_L + 44, W - PAD_R
        band = (H - PAD_T - PAD_B) / max(n, 1)
        x_of = lambda v: x0 + v / top * (x1 - x0)  # noqa: E731
        for t in ticks:
            x = x_of(t)
            body.append(f'<line class="orca-chart__grid" x1="{x:.1f}" x2="{x:.1f}" y1="{PAD_T}" y2="{H - PAD_B}"/>')
            body.append(_t(x, H - PAD_B + 16, fmt(t) + unit))
        for i, lab in enumerate(labels):
            y = PAD_T + i * band
            body.append(_t(x0 - 6, y + band / 2 + 4, lab, anchor="end"))
            acc = 0.0
            for j, s in enumerate(series):
                v = s["values"][i]
                bh = band * 0.7 / (1 if stacked else m)
                by = y + band * 0.15 + (0 if stacked else j * bh)
                bx = x_of(acc) if stacked else x0
                bw = x_of(acc + v) - bx if stacked else x_of(v) - x0
                body.append(f'<rect class="orca-chart__bar" style="{_color(j)}" x="{bx:.1f}" y="{by:.1f}" width="{max(bw, 0):.1f}" height="{bh:.1f}"><title>{escape(s["name"])}, {escape(lab)}: {fmt(v)}{unit}</title></rect>')
                if stacked:
                    acc += v
        return _svg(body, _summary("bar", d, unit))
    y_of = lambda v: H - PAD_B - v / top * (H - PAD_T - PAD_B)  # noqa: E731
    body += _axes_y(ticks, y_of, unit=unit)
    band = (W - PAD_L - PAD_R) / max(n, 1)
    for i, lab in enumerate(labels):
        x = PAD_L + i * band
        body.append(_t(x + band / 2, H - PAD_B + 16, lab))
        acc = 0.0
        for j, s in enumerate(series):
            v = s["values"][i]
            bw = band * 0.7 / (1 if stacked else m)
            bx = x + band * 0.15 + (0 if stacked else j * bw)
            y_top = y_of(acc + v) if stacked else y_of(v)
            y_bot = y_of(acc) if stacked else y_of(0)
            body.append(f'<rect class="orca-chart__bar" style="{_color(j)}" x="{bx:.1f}" y="{y_top:.1f}" width="{bw:.1f}" height="{max(y_bot - y_top, 0):.1f}"><title>{escape(s["name"])}, {escape(lab)}: {fmt(v)}{unit}</title></rect>')
            if stacked:
                acc += v
    body.append(f'<line class="orca-chart__axis" x1="{PAD_L}" x2="{W - PAD_R}" y1="{y_of(0):.1f}" y2="{y_of(0):.1f}"/>')
    return _svg(body, _summary("bar", d, unit))


def line_svg(d, area=False, unit="") -> str:
    labels, series = d["labels"], d["series"]
    vals = [v for s in series for v in s["values"]] or [0]
    ticks = nice_ticks(min(0, min(vals)), max(vals))
    lo, top = ticks[0], ticks[-1]
    y_of = lambda v: H - PAD_B - (v - lo) / (top - lo) * (H - PAD_T - PAD_B)  # noqa: E731
    n = len(labels)
    x_of = lambda i: PAD_L + (i / max(n - 1, 1)) * (W - PAD_L - PAD_R)  # noqa: E731
    body = _axes_y(ticks, y_of, unit=unit)
    step = max(1, math.ceil(n / 8))
    for i, lab in enumerate(labels):
        if i % step == 0:
            body.append(_t(x_of(i), H - PAD_B + 16, lab))
    for j, s in enumerate(series):
        pts = [(x_of(i), y_of(v)) for i, v in enumerate(s["values"])]
        line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        if area:
            body.append(f'<polygon class="orca-chart__area" style="{_color(j)}" points="{pts[0][0]:.1f},{y_of(lo):.1f} {line} {pts[-1][0]:.1f},{y_of(lo):.1f}"/>')
        dash = ' stroke-dasharray="6 4"' if j % 3 == 1 else (' stroke-dasharray="2 3"' if j % 3 == 2 else "")
        body.append(f'<polyline class="orca-chart__line" style="{_color(j)}" points="{line}"{dash}/>')
        for (x, y), v, lab in zip(pts, s["values"], labels):
            body.append(f'<circle class="orca-chart__point" style="{_color(j)}" cx="{x:.1f}" cy="{y:.1f}" r="3"><title>{escape(s["name"])}, {escape(lab)}: {fmt(v)}{unit}</title></circle>')
    return _svg(body, _summary("line", d, unit))


def _arc(cx, cy, r, a0, a1, r_in=0.0) -> str:
    large = 1 if a1 - a0 > math.pi else 0
    x0, y0 = cx + r * math.sin(a0), cy - r * math.cos(a0)
    x1, y1 = cx + r * math.sin(a1), cy - r * math.cos(a1)
    if r_in:
        xi1, yi1 = cx + r_in * math.sin(a1), cy - r_in * math.cos(a1)
        xi0, yi0 = cx + r_in * math.sin(a0), cy - r_in * math.cos(a0)
        return (f"M{x0:.2f},{y0:.2f} A{r},{r} 0 {large} 1 {x1:.2f},{y1:.2f} L{xi1:.2f},{yi1:.2f} "
                f"A{r_in},{r_in} 0 {large} 0 {xi0:.2f},{yi0:.2f} Z")
    return f"M{cx},{cy} L{x0:.2f},{y0:.2f} A{r},{r} 0 {large} 1 {x1:.2f},{y1:.2f} Z"


def pie_svg(d, doughnut=False, unit="") -> str:
    labels = d["labels"]
    values = d["series"][0]["values"] if d["series"] else []
    total = sum(values) or 1
    cx, cy, r = 120, 120, 104
    body, a = [], 0.0
    for i, (lab, v) in enumerate(zip(labels, values)):
        a1 = a + v / total * 2 * math.pi
        if v / total >= 0.9999:
            a1 = a + 2 * math.pi - 1e-4
        body.append(f'<path class="orca-chart__slice" style="{_color(i)}" d="{_arc(cx, cy, r, a, a1, 62 if doughnut else 0)}"><title>{escape(lab)}: {fmt(v)}{unit} ({round(v / total * 100)}%)</title></path>')
        a = a1
    if doughnut:
        body.append(_t(cx, cy + 2, fmt(total), cls="orca-chart__total"))
        body.append(_t(cx, cy + 20, "Total", cls="orca-chart__label"))
    return _svg(body, _summary("pie", d, unit), 240, 240)


def scatter_svg(d, bubble=False, unit="") -> str:
    pts = [p for s in d["series"] for p in s["values"]]
    xs, ys = [p[0] for p in pts] or [0], [p[1] for p in pts] or [0]
    xt, yt = nice_ticks(min(0, min(xs)), max(xs)), nice_ticks(min(0, min(ys)), max(ys))
    x_of = lambda v: PAD_L + (v - xt[0]) / (xt[-1] - xt[0]) * (W - PAD_L - PAD_R)  # noqa: E731
    y_of = lambda v: H - PAD_B - (v - yt[0]) / (yt[-1] - yt[0]) * (H - PAD_T - PAD_B)  # noqa: E731
    body = _axes_y(yt, y_of, unit=unit)
    for t in xt:
        body.append(_t(x_of(t), H - PAD_B + 16, fmt(t)))
    sizes = [p[2] for p in pts if len(p) > 2] or [1]
    smax = max(sizes) or 1
    shapes = ("circle", "rect", "diamond")
    for j, s in enumerate(d["series"]):
        shape = shapes[j % 3]
        for p in s["values"]:
            x, y = x_of(p[0]), y_of(p[1])
            r = 4 + (math.sqrt(p[2] / smax) * 18 if bubble and len(p) > 2 else 0)
            tip = f'<title>{escape(s["name"])}: {fmt(p[0])}, {fmt(p[1])}{unit}{(", size " + fmt(p[2])) if len(p) > 2 else ""}</title>'
            cls = "orca-chart__bubble" if bubble else "orca-chart__point"
            if shape == "circle" or bubble:
                body.append(f'<circle class="{cls}" style="{_color(j)}" cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}">{tip}</circle>')
            elif shape == "rect":
                body.append(f'<rect class="{cls}" style="{_color(j)}" x="{x - r:.1f}" y="{y - r:.1f}" width="{2 * r:.1f}" height="{2 * r:.1f}">{tip}</rect>')
            else:
                body.append(f'<path class="{cls}" style="{_color(j)}" d="M{x:.1f},{y - r - 1:.1f} L{x + r + 1:.1f},{y:.1f} L{x:.1f},{y + r + 1:.1f} L{x - r - 1:.1f},{y:.1f} Z">{tip}</path>')
    return _svg(body, _summary("scatter", d, unit))


def radar_svg(d, unit="") -> str:
    labels, series = d["labels"], d["series"]
    n = len(labels) or 1
    top = nice_ticks(0, max([v for s in series for v in s["values"]] or [1]), 4)[-1]
    cx, cy, r = 150, 128, 96
    pt = lambda i, v: (cx + v / top * r * math.sin(2 * math.pi * i / n), cy - v / top * r * math.cos(2 * math.pi * i / n))  # noqa: E731
    body = []
    for k in (0.25, 0.5, 0.75, 1):
        ring = " ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(i, top * k) for i in range(n)))
        body.append(f'<polygon class="orca-chart__grid" points="{ring}"/>')
    for i, lab in enumerate(labels):
        x, y = pt(i, top)
        body.append(f'<line class="orca-chart__grid" x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}"/>')
        lx, ly = pt(i, top * 1.16)
        anchor = "middle" if abs(lx - cx) < 8 else ("start" if lx > cx else "end")
        body.append(_t(lx, ly + 4, lab, anchor=anchor))
    for j, s in enumerate(series):
        poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(i, v) for i, v in enumerate(s["values"])))
        body.append(f'<polygon class="orca-chart__radar" style="{_color(j)}" points="{poly}"><title>{escape(s["name"])}</title></polygon>')
        for i, v in enumerate(s["values"]):
            x, y = pt(i, v)
            body.append(f'<circle class="orca-chart__point" style="{_color(j)}" cx="{x:.1f}" cy="{y:.1f}" r="3"><title>{escape(s["name"])}, {escape(labels[i])}: {fmt(v)}{unit}</title></circle>')
    return _svg(body, _summary("radar", d, unit), 300, 256)


def polar_svg(d, unit="") -> str:
    labels = d["labels"]
    values = d["series"][0]["values"] if d["series"] else []
    n = len(values) or 1
    top = nice_ticks(0, max(values or [1]), 4)[-1]
    cx, cy, R = 120, 120, 104
    body = []
    for k in (0.25, 0.5, 0.75, 1):
        body.append(f'<circle class="orca-chart__grid" cx="{cx}" cy="{cy}" r="{R * k:.1f}" fill="none"/>')
    for i, (lab, v) in enumerate(zip(labels, values)):
        a0, a1 = 2 * math.pi * i / n, 2 * math.pi * (i + 1) / n
        r = max(math.sqrt(v / top) * R, 1)
        body.append(f'<path class="orca-chart__slice orca-chart__slice--polar" style="{_color(i)}" d="{_arc(cx, cy, r, a0, a1)}"><title>{escape(lab)}: {fmt(v)}{unit}</title></path>')
    return _svg(body, _summary("polar", d, unit), 240, 240)


def _summary(kind, d, unit) -> str:
    if kind in ("pie", "polar"):
        vals = d["series"][0]["values"] if d["series"] else []
        total = sum(vals) or 1
        return "; ".join(f"{lab} {fmt(v)}{unit} ({round(v / total * 100)}%)" for lab, v in zip(d["labels"], vals))
    if kind == "scatter":
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
    if kind == "bar":
        svg = bar_svg(d, stacked=stacked, horizontal=horizontal, unit=unit)
    elif kind in ("line", "area"):
        svg = line_svg(d, area=kind == "area", unit=unit)
    elif kind in ("pie", "doughnut"):
        svg = pie_svg(d, doughnut=kind == "doughnut", unit=unit)
    elif kind in ("scatter", "bubble"):
        svg = scatter_svg(d, bubble=kind == "bubble", unit=unit)
    elif kind == "radar":
        svg = radar_svg(d, unit=unit)
    else:
        svg = polar_svg(d, unit=unit)
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
    return {"kind": kind, "svg": svg, "title": title, "subtitle": subtitle, "caption": caption, "legend": legend,
            "show_legend": round_chart or len(d["series"]) > 1 or point, "head": head, "rows": rows, "round": round_chart}
