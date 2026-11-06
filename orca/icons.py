"""The ORCA icon set: 16px, single ink, ``currentColor``.

* 106 filled glyphs from Vanilla framework 4.59 (LGPL-3.0, via Tangerine): ``data/icons_vanilla.json``.
* ORCA glyphs for ideas Vanilla has no icon for (home, edit, calendar, clock...), drawn on the same
  16px grid with a 1.5px line so they sit beside Vanilla's filled outlines without looking foreign.
* Aliases map the names used in the ORCA guide to a glyph (``bell`` → ``notifications``).
"""

from __future__ import annotations

import itertools
import json
from functools import lru_cache
from html import escape
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data" / "icons_vanilla.json"

_LINE = {"fill": "none", "stroke": "currentColor", "strokeWidth": "1.5"}


def _p(d: str) -> list:
    return ["path", dict(_LINE, d=d)]


def _dot(cx: float, cy: float, r: float = 1.25) -> list:
    return ["circle", {"cx": str(cx), "cy": str(cy), "r": str(r), "fill": "currentColor"}]


_CAL = "M2.75 3.75h10.5v9.5H2.75z M2.75 6.75h10.5 M5.25 1.75v3 M10.75 1.75v3"

ORCA_GLYPHS: dict[str, list] = {
    "home": [_p("M1.75 7.75 8 2.25l6.25 5.5 M3.75 6.5v7.25h3v-4h2.5v4h3V6.5")],
    "edit": [_p("M10.75 2.25l3 3-8.5 8.5h-3v-3z M9.25 3.75l3 3")],
    "filter": [_p("M1.75 2.75h12.5l-4.75 5.5v4.5l-3 1.75v-6.25z")],
    "star": [_p("M8 1.75l1.85 3.9 4.25.55-3.1 2.95.8 4.25L8 11.3l-3.8 2.1.8-4.25L1.9 6.2l4.25-.55z")],
    "more": [_dot(3, 8), _dot(8, 8), _dot(13, 8)],
    "sort": [_p("M4.75 13.75v-11.5 M2.25 4.75l2.5-2.5 2.5 2.5 M11.25 2.25v11.5 M8.75 11.25l2.5 2.5 2.5-2.5")],
    "grid": [_p("M2.75 2.75h4v4h-4z M9.25 2.75h4v4h-4z M2.75 9.25h4v4h-4z M9.25 9.25h4v4h-4z")],
    "list": [_p("M5.5 3.75h8.75 M5.5 8h8.75 M5.5 12.25h8.75"), _dot(2.5, 3.75, 1), _dot(2.5, 8, 1), _dot(2.5, 12.25, 1)],
    "chat": [_p("M2.25 2.75h11.5v8h-6.5l-3.25 2.75v-2.75h-1.75z")],
    "sliders": [_p("M1.75 4.5h12.5 M1.75 11.5h12.5 M5.25 2.25v4.5 M10.75 9.25v4.5")],
    "unlock": [_p("M2.75 7.25h10.5v6.5H2.75z M5.25 7.25V4.75a2.75 2.75 0 0 1 5.3-1 M8 9.75v1.5")],
    "lock": [_p("M2.75 7.25h10.5v6.5H2.75z M5.25 7.25V4.75a2.75 2.75 0 0 1 5.5 0v2.5 M8 9.75v1.5")],
    "settings": [_p("M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 1 0 0-5z M8 1.25v2.25 M8 12.5v2.25 M1.25 8h2.25 M12.5 8h2.25 "
                    "M3.2 3.2l1.6 1.6 M11.2 11.2l1.6 1.6 M3.2 12.8l1.6-1.6 M11.2 4.8l1.6-1.6")],
    "calendar": [_p(_CAL)],
    "calendar-plus": [_p(_CAL + " M8 8.5v3.25 M6.375 10.125h3.25")],
    "today": [_p(_CAL), ["path", {"d": "M5 8.75h3v3H5z", "fill": "currentColor"}]],
    "clock": [_p("M8 1.75a6.25 6.25 0 1 0 0 12.5 6.25 6.25 0 1 0 0-12.5z M8 4.5V8l2.5 1.75")],
    "alarm": [_p("M8 3.75a5.25 5.25 0 1 0 0 10.5 5.25 5.25 0 1 0 0-10.5z M8 6.25V9l1.75 1.25 M1.75 4.25 4 2 M14.25 4.25 12 2")],
    "timer": [_p("M8 3.75a5.25 5.25 0 1 0 0 10.5 5.25 5.25 0 1 0 0-10.5z M6 1.25h4 M8 1.25v2.5 M8 9l2-2 M12.25 4.5l1.25-1.25")],
    "hourglass": [_p("M3.25 1.75h9.5 M3.25 14.25h9.5 M4.5 1.75c0 3.5 3.5 4.25 3.5 6.25S4.5 10.75 4.5 14.25 "
                     "M11.5 1.75c0 3.5-3.5 4.25-3.5 6.25s3.5 2.75 3.5 6.25")],
    "flag": [_p("M3.25 14.75V1.75 M3.25 2.5h9.75L11 5.75l2 3.25H3.25")],
    "pin": [_p("M5.5 1.75h5 M6.5 1.75v4.5L4 9.5h8L9.5 6.25v-4.5 M8 9.5v5")],
    "repeat": [_p("M2.75 7.5V5.25h9.75 M10.5 3l2.25 2.25-2.25 2.25 M13.25 8.5v2.25H3.5 M5.5 13l-2.25-2.25 2.25-2.25")],
    "mail": [_p("M1.75 3.25h12.5v9.5H1.75z M1.75 3.75 8 8.75l6.25-5")],
    "sun": [_p("M8 5a3 3 0 1 0 0 6 3 3 0 1 0 0-6z M8 .75v2 M8 13.25v2 M.75 8h2 M13.25 8h2 M2.9 2.9l1.4 1.4 "
               "M11.7 11.7l1.4 1.4 M2.9 13.1l1.4-1.4 M11.7 4.3l1.4-1.4")],
    "moon": [_p("M13.25 9.75A5.75 5.75 0 1 1 6.25 2.75a4.5 4.5 0 0 0 7 7z")],
    "check": [_p("M2.5 8.5l3.5 3.5 7.5-8")],
    "barcode": [_p("M2 3v10 M4.5 3v10 M6 3v10 M8.5 3v10 M11 3v10 M12.5 3v10 M14 3v10")],
    "qr-code": [_p("M2.75 2.75h4v4h-4z M9.25 2.75h4v4h-4z M2.75 9.25h4v4h-4z M9.25 9.25h1.5v1.5 M12 12h1.25v1.25 M9.25 13.25h1.5")],
    "camera": [_p("M1.75 4.75h3l1.25-2h4l1.25 2h3v8.5H1.75z M8 6.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 1 0 0-5z")],
}

ALIASES = {
    "bell": "notifications",
    "reminder": "notifications",
    "magnifier": "search",
    "refresh": "restart",
    "pencil": "edit",
    "ellipsis": "more",
    "hamburger": "menu",
    "trash": "delete",
    "x": "close",
    "info-circle": "info",
    "alert": "warning",
    "date-pin": "pin",
    "calendar-today": "today",
    "dragging": "drag",
}

STATUS_GLYPHS = {"positive": "success", "caution": "warning", "negative": "error", "info": "info", "neutral": "info"}

SIZES = {"xs": "0.75rem", "s": "1rem", "m": "1.25rem", "l": "1.5rem", "xl": "2.25rem",
         "small": "0.75rem", "default": "1rem", "large": "1.5rem"}


_mask_ids = itertools.count(1)


@lru_cache(maxsize=1)
def glyphs() -> dict[str, dict]:
    """name -> {"d": shapes, "r": rotation in degrees (optional), "cut": shapes knocked out (optional)}."""
    out = json.loads(DATA.read_text(encoding="utf-8"))
    out.update({name: {"d": shapes} for name, shapes in ORCA_GLYPHS.items()})
    return out


def names() -> list[str]:
    return sorted(glyphs())


def resolve(name: str) -> str | None:
    name = (name or "").strip().lower()
    if name in glyphs():
        return name
    return ALIASES.get(name)


_ATTR = {"fillRule": "fill-rule", "clipRule": "clip-rule", "strokeWidth": "stroke-width",
         "strokeLinecap": "stroke-linecap", "strokeLinejoin": "stroke-linejoin"}


def _element(tag: str, attrs: dict) -> str:
    parts = " ".join(f'{_ATTR.get(k, k)}="{escape(str(v))}"' for k, v in attrs.items())
    return f"<{tag} {parts}/>"


def svg(name: str, size: str = "s", label: str = "", css_class: str = "") -> str:
    """Return inline SVG markup.

    Decorative by default (``aria-hidden``). Pass ``label`` only when the icon is the sole carrier of
    meaning and has no visible text beside it; then it gets ``role="img"`` and a title.
    """
    key = resolve(name)
    if key is None:
        raise KeyError(f"Unknown ORCA icon {name!r}. Run `python -m orca icons` to list the {len(glyphs())} names.")
    size_cls = f" orca-icon--{size}" if size in SIZES and size not in ("s", "default") else ""
    cls = f"orca-icon{size_cls}" + (f" {css_class}" if css_class else "")
    spec = glyphs()[key]
    group, mask = [], ""
    if spec.get("cut"):  # Vanilla's status glyphs knock their mark out of a filled disc
        mask_id = f"orca-cut-{next(_mask_ids)}"
        cut = "".join(_element(tag, dict(attrs, fill="#000")) for tag, attrs in spec["cut"])
        mask = (f'<mask id="{mask_id}" maskUnits="userSpaceOnUse" x="0" y="0" width="16" height="16">'
                f'<rect width="16" height="16" fill="#fff"/>{cut}</mask>')
        group.append(f'mask="url(#{mask_id})"')
    if spec.get("r"):
        group.append(f'transform="rotate({spec["r"]} 8 8)"')
    shapes = "".join(_element(tag, attrs) for tag, attrs in spec["d"])
    body = mask + (f'<g {" ".join(group)}>{shapes}</g>' if group else shapes)
    if label:
        a11y = f'role="img" aria-label="{escape(label)}"'
    else:
        a11y = 'aria-hidden="true" focusable="false"'
    return f'<svg class="{cls}" viewBox="0 0 16 16" width="16" height="16" {a11y}>{body}</svg>'
