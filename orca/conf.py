"""Project settings for ORCA and the brand-token computation.

Configure ORCA in ``settings.py``::

    ORCA = {
        "BRAND": {
            "name": "Acme",
            "color": "#7a1fa2",
            "accent": "#0b5cad",
            "logo": "brand/logo.svg",
        },
        "THEME": "auto",        # "auto" (follows the OS), "light", "dark" or "paper"
        "DENSITY": "comfortable",  # or "dense": tighter type, controls and spacing for data-heavy screens
        "DOCS_ENABLED": True,   # serve the element catalogue at the URL you include
    }

Only the keys of ``BRAND`` listed in ``orca.tokens.BRAND_TOKENS`` exist. Unknown keys are reported by
the system check ``orca.E002`` so a typo never silently does nothing.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from . import color
from .tokens import BRAND_KEYS, BRAND_TOKENS, DENSITIES

THEMES = ("auto", "light", "dark", "paper")
_FONT_STACK = re.compile(r'^[\w\s",\-.]+$')

# Grounds the accent must read on (text 4.5:1).
LIGHT_GROUNDS = ("#ffffff", "#f7f7f7")
PAPER_GROUNDS = ("#f3f3f3", "#ebebeb")
DARK_GROUNDS = ("#262626", "#202020", "#2c2c2c")


@dataclass
class Brand:
    values: dict[str, str]
    css: dict[str, dict[str, str]]  # {"light": {...}, "dark": {...}}
    notes: list[str] = field(default_factory=list)  # adjustments made, reported as warnings
    errors: list[str] = field(default_factory=list)


def _defaults() -> dict[str, str]:
    return {t.key: t.default for t in BRAND_TOKENS}


def user_settings() -> dict:
    try:
        from django.conf import settings

        return dict(getattr(settings, "ORCA", {}) or {})
    except Exception:  # Django not configured: use defaults (CLI, build)
        return {}


def theme() -> str:
    value = str(user_settings().get("THEME", "auto")).lower()
    return value if value in THEMES else "auto"


def density() -> str:
    value = str(user_settings().get("DENSITY", "comfortable")).lower()
    return value if value in DENSITIES else "comfortable"


def docs_enabled() -> bool:
    return bool(user_settings().get("DOCS_ENABLED", True))


def _hover(fill: str, on: str) -> tuple[str, str]:
    """Hover and pressed fills: step away from the text colour so contrast only grows."""
    target = "#000000" if on == "#ffffff" else "#ffffff"
    return color.mix(fill, target, 0.12), color.mix(fill, target, 0.2)


def compute_brand(raw: dict | None = None) -> Brand:
    """Validate the BRAND settings and derive every brand CSS value.

    Accepts liberal input (hex without '#', 3-digit hex, rgb()) and normalizes it; colours that
    would fail contrast are adjusted and the adjustment is reported, never silently dropped.
    """
    values = _defaults()
    errors: list[str] = []
    notes: list[str] = []
    raw = dict(raw if raw is not None else user_settings().get("BRAND", {}) or {})

    for key in raw:
        if key not in BRAND_KEYS:
            errors.append(
                f"ORCA['BRAND'] has an unknown key {key!r}. Brand keys are: {', '.join(sorted(BRAND_KEYS))}. "
                "Only brand tokens can be changed; every other token is fixed by the design system."
            )
    for key, value in raw.items():
        if key in BRAND_KEYS and value not in (None, ""):
            values[key] = str(value).strip()

    for key in ("color", "accent", "accent_dark", "on_color"):
        if values.get(key):
            try:
                values[key] = color.normalize(values[key])
            except ValueError as exc:
                errors.append(f"ORCA['BRAND'][{key!r}]: {exc}")
                values[key] = next(t.default for t in BRAND_TOKENS if t.key == key)

    for key in ("font_sans", "font_mono"):
        if not _FONT_STACK.match(values[key]):
            errors.append(
                f"ORCA['BRAND'][{key!r}] must be a CSS font stack such as '\"Inter\", sans-serif' "
                "(letters, digits, spaces, quotes, commas and hyphens only)."
            )
            values[key] = next(t.default for t in BRAND_TOKENS if t.key == key)

    brand = values["color"]
    on = values["on_color"] or color.best_on(brand)
    strong = color.toward(brand, "#000000" if on == "#ffffff" else "#ffffff", on, 4.5)
    if strong != brand:
        notes.append(
            f"Brand fills use {strong} (derived from {brand}) so {on} text on them reads at 4.5:1."
        )
    hover, active = _hover(strong, on)

    accent = values["accent"]
    accent_ok = accent
    for ground in LIGHT_GROUNDS + PAPER_GROUNDS:
        accent_ok = color.toward(accent_ok, "#000000", ground, 4.5)
    if accent_ok != accent:
        notes.append(f"The accent {accent} was darkened to {accent_ok} to read at 4.5:1 on the light and paper grounds.")

    if raw.get("accent_dark"):
        accent_dark = values["accent_dark"]
    elif raw.get("accent"):
        accent_dark = accent
        for ground in DARK_GROUNDS:
            accent_dark = color.toward(accent_dark, "#ffffff", ground, 4.5)
    else:
        accent_dark = values["accent_dark"]
    dark_ok = accent_dark
    for ground in DARK_GROUNDS:
        dark_ok = color.toward(dark_ok, "#ffffff", ground, 4.5)
    if dark_ok != accent_dark and raw.get("accent_dark"):
        notes.append(f"The dark accent {accent_dark} was lightened to {dark_ok} to read at 4.5:1 on the dark grounds.")

    common = {
        "--orca-brand": brand,
        "--orca-brand-strong": strong,
        "--orca-brand-strong-hover": hover,
        "--orca-brand-strong-active": active,
        "--orca-brand-on": on,
        "--orca-font-sans": values["font_sans"],
        "--orca-font-mono": values["font_mono"],
    }
    light = dict(common, **{"--orca-accent": accent_ok, "--orca-accent-hover": color.mix(accent_ok, "#000000", 0.15)})
    dark = dict(common, **{"--orca-accent": dark_ok, "--orca-accent-hover": color.mix(dark_ok, "#ffffff", 0.15)})
    values.update(on_color=on, accent=accent_ok, accent_dark=dark_ok)
    return Brand(values=values, css={"light": light, "dark": dark}, notes=notes, errors=errors)


def brand_style(brand: Brand) -> str:
    """CSS that sets the brand tokens for every theme (dark follows the same selectors as tokens.css)."""

    def block(selector: str, decls: dict[str, str]) -> str:
        body = " ".join(f"{k}: {v};" for k, v in decls.items())
        return f"{selector} {{ {body} }}"

    light_sel = ":root"
    dark_auto = ':root:not([data-theme="light"]):not([data-theme="paper"])'
    return "\n".join(
        [
            block(light_sel, brand.css["light"]),
            "@media (prefers-color-scheme: dark) { " + block(dark_auto, brand.css["dark"]) + " }",
            block(':root[data-theme="dark"]', brand.css["dark"]),
        ]
    )
