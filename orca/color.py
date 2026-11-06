"""Colour maths used by the token build and by brand validation.

Pure Python, no dependencies. All colours are handled as sRGB tuples of floats in 0..1.
"""

from __future__ import annotations

import math
import re

_HEX = re.compile(r"^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")
_RGBA = re.compile(r"^rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*(?:,\s*([\d.]+)\s*)?\)$")

RGB = tuple[float, float, float]


def parse(value: str) -> tuple[RGB, float]:
    """Parse ``#rgb``, ``#rrggbb``, ``rgb()`` or ``rgba()`` into ``(rgb, alpha)``.

    Accepts a missing ``#`` and any letter case (Postel's law: accept liberally).
    Raises ``ValueError`` with a message that says how to fix the value.
    """
    text = value.strip()
    m = _HEX.match(text)
    if m:
        h = m.group(1)
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return (int(h[0:2], 16) / 255, int(h[2:4], 16) / 255, int(h[4:6], 16) / 255), 1.0
    m = _RGBA.match(text)
    if m:
        r, g, b = (float(m.group(i)) / 255 for i in (1, 2, 3))
        a = float(m.group(4)) if m.group(4) is not None else 1.0
        return (r, g, b), a
    raise ValueError(f"{value!r} is not a colour. Use a hex value such as #0f95a1, or rgb(15, 149, 161).")


def to_hex(rgb: RGB) -> str:
    return "#" + "".join(f"{round(max(0.0, min(1.0, c)) * 255):02x}" for c in rgb)


def normalize(value: str) -> str:
    """Return a lowercase ``#rrggbb`` for an opaque colour."""
    rgb, alpha = parse(value)
    if alpha < 1:
        raise ValueError(f"{value!r} is transparent. Brand colours must be opaque.")
    return to_hex(rgb)


def composite(fg: str, bg: str) -> RGB:
    """The opaque colour you see when ``fg`` (possibly rgba) sits on ``bg``."""
    (fr, fg_, fb), a = parse(fg)
    (br, bg_, bb), _ = parse(bg)
    return (fr * a + br * (1 - a), fg_ * a + bg_ * (1 - a), fb * a + bb * (1 - a))


def _lin(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb: RGB) -> float:
    r, g, b = (_lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(fg: str, bg: str) -> float:
    """WCAG 2 contrast ratio of ``fg`` over ``bg`` (``fg`` may be translucent)."""
    bg_rgb = parse(bg)[0]
    l1 = luminance(composite(fg, bg))
    l2 = luminance(bg_rgb)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def mix(a: str, b: str, amount_b: float) -> str:
    """Mix ``amount_b`` (0..1) of colour ``b`` into ``a``."""
    ra, rb = parse(a)[0], parse(b)[0]
    return to_hex(tuple(x * (1 - amount_b) + y * amount_b for x, y in zip(ra, rb)))


def toward(color: str, target: str, bg: str, ratio: float, step: float = 0.02) -> str:
    """Mix ``color`` toward ``target`` (black or white) until it reaches ``ratio`` on ``bg``.

    Returns the colour unchanged when it already passes.
    """
    amount = 0.0
    current = normalize(color)
    while contrast(current, bg) < ratio and amount < 1:
        amount = min(1.0, amount + step)
        current = mix(color, target, amount)
    return current


def best_on(fill: str) -> str:
    """Black or white, whichever reads better on ``fill``."""
    return "#ffffff" if contrast("#ffffff", fill) >= contrast("#000000", fill) else "#000000"


# --- OKLCH, used to generate the hue scales ---------------------------------------------------

def oklch_to_rgb(l: float, c: float, h: float) -> RGB:
    a = c * math.cos(math.radians(h))
    b = c * math.sin(math.radians(h))
    l_ = l + 0.3963377774 * a + 0.2158037573 * b
    m_ = l - 0.1055613458 * a - 0.0638541728 * b
    s_ = l - 0.0894841775 * a - 1.2914855480 * b
    lc, mc, sc = l_**3, m_**3, s_**3
    r = 4.0767416621 * lc - 3.3077115913 * mc + 0.2309699292 * sc
    g = -1.2684380046 * lc + 2.6097574011 * mc - 0.3413193965 * sc
    bl = -0.0041960863 * lc - 0.7034186147 * mc + 1.7076147010 * sc

    def gamma(x: float) -> float:
        x = max(0.0, min(1.0, x))
        return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055

    return gamma(r), gamma(g), gamma(bl)


def oklch_in_gamut(l: float, c: float, h: float) -> str:
    """Reduce chroma until the OKLCH colour fits sRGB, then return hex."""
    while c > 0:
        a = c * math.cos(math.radians(h))
        b = c * math.sin(math.radians(h))
        l_ = l + 0.3963377774 * a + 0.2158037573 * b
        m_ = l - 0.1055613458 * a - 0.0638541728 * b
        s_ = l - 0.0894841775 * a - 1.2914855480 * b
        lc, mc, sc = l_**3, m_**3, s_**3
        lin = (
            4.0767416621 * lc - 3.3077115913 * mc + 0.2309699292 * sc,
            -1.2684380046 * lc + 2.6097574011 * mc - 0.3413193965 * sc,
            -0.0041960863 * lc - 0.7034186147 * mc + 1.7076147010 * sc,
        )
        if all(-0.0005 <= x <= 1.0005 for x in lin):
            break
        c -= 0.002
    return to_hex(oklch_to_rgb(l, max(c, 0), h))
