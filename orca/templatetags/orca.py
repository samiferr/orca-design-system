"""ORCA template tags. Load with ``{% load orca %}``.

Tags
    {% orca_head %}                     stylesheets, brand tokens, theme restore, favicon, script
    {% orca_html_attrs %}               lang/data-theme attributes for the <html> element
    {% icon "search" %}                 inline 16px icon (decorative)
    {% icon "close" label="Close" %}    icon that is the only carrier of meaning
    {% status_icon "negative" %}        coloured status glyph (success, warning, error, info)
    {% orca_logo %}                     brand logo or wordmark
    {% orca_illustration "empty" %}     empty / search illustration
    {% orca_timezone_options "Europe/Paris" %}
    {% orca_brand "name" %}             a brand value from settings.ORCA["BRAND"]

Filters
    {{ minutes|orca_duration }}         90 -> "1 h 30 min" (int minutes or timedelta)
    {{ user.get_full_name|orca_initials }}  "Ada Lovelace" -> "AL"
"""

from __future__ import annotations

import datetime as dt
import re
from html import escape
from zoneinfo import available_timezones

from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from .. import icons
from ..conf import brand_style, compute_brand, theme

register = template.Library()

_THEME_RESTORE = (
    "(function(){try{var t=localStorage.getItem('orca-theme');"
    "if(t==='light'||t==='dark'||t==='paper')document.documentElement.setAttribute('data-theme',t);}catch(e){}})();"
)


def _nonce(context) -> str:
    request = context.get("request")
    nonce = getattr(request, "csp_nonce", "") if request is not None else ""
    return f' nonce="{escape(str(nonce))}"' if nonce else ""


@register.simple_tag(takes_context=True)
def orca_head(context, script: bool = True, theme_restore: bool = True):
    """Everything ORCA needs in <head>. Place it before your own stylesheets."""
    brand = compute_brand()
    nonce = _nonce(context)
    parts = [
        f'<link rel="stylesheet" href="{static("orca/css/tokens.css")}">',
        f'<link rel="stylesheet" href="{static("orca/css/orca.css")}">',
        f'<link rel="stylesheet" href="{static("orca/css/components.css")}">',
        f'<link rel="stylesheet" href="{static("orca/css/patterns.css")}">',
        f"<style{nonce}>{brand_style(brand)}</style>",
        f'<meta name="theme-color" content="{brand.css["light"]["--orca-brand-strong"]}">',
    ]
    if brand.values.get("favicon"):
        href = static(brand.values["favicon"])
        kind = "image/svg+xml" if href.endswith(".svg") else "image/png"
        parts.append(f'<link rel="icon" href="{escape(href)}" type="{kind}">')
    if theme_restore and theme() == "auto":
        parts.append(f"<script{nonce}>{_THEME_RESTORE}</script>")
    if script:
        parts.append(f'<script src="{static("orca/js/orca.js")}" defer></script>')
        # Status glyphs for toasts the script creates (ORCA.toast)
        for glyph in ("success", "error", "warning", "info"):
            parts.append(f'<template data-orca-icon="{glyph}">{icons.svg(glyph)}</template>')
    return mark_safe("\n".join(parts))


@register.simple_tag
def orca_html_attrs(lang: str = "en"):
    """Attributes for <html>: language and, when settings fix one, the theme."""
    attrs = f'lang="{escape(lang)}"'
    if theme() != "auto":
        attrs += f' data-theme="{theme()}"'
    return mark_safe(attrs)


@register.simple_tag(name="icon")
def icon_tag(name: str, size: str = "s", label: str = "", **kwargs):
    return mark_safe(icons.svg(name, size=size, label=label, css_class=kwargs.get("class", "")))


@register.simple_tag
def status_icon(tone: str, label: str = "", size: str = "s"):
    """The status glyph for a tone (positive, caution, negative, info, neutral), in its colour."""
    glyph = icons.STATUS_GLYPHS.get(tone, "info")
    return mark_safe(icons.svg(glyph, size=size, label=label, css_class=f"orca-status-icon--{tone}"))


@register.simple_tag
def orca_brand(key: str):
    return compute_brand().values.get(key, "")


@register.simple_tag
def orca_logo(href: str = "/", size: str = ""):
    values = compute_brand().values
    name = escape(values["name"])
    cls = "orca-logo" + (" orca-logo--lg" if size == "lg" else "")
    if values.get("logo"):
        inner = f'<img class="orca-logo__img" src="{escape(static(values["logo"]))}" alt="{name}">'
    else:
        inner = f'<span class="orca-logo__mark" aria-hidden="true"></span><span>{name}</span>'
    if href:
        return mark_safe(f'<a class="{cls}" href="{escape(href)}">{inner}</a>')
    return mark_safe(f'<span class="{cls}">{inner}</span>')


_ILLUSTRATIONS = {
    "empty": (
        '<svg class="orca-illustration" viewBox="0 0 128 96" aria-hidden="true" focusable="false">'
        '<rect class="ill-panel" x="16" y="12" width="96" height="72"/>'
        '<rect class="ill-accent" x="16" y="12" width="96" height="3"/>'
        '<rect class="ill-bar" x="28" y="30" width="56" height="6"/><rect class="ill-bar" x="28" y="44" width="72" height="6"/>'
        '<rect class="ill-bar" x="28" y="58" width="40" height="6"/></svg>'
    ),
    "search": (
        '<svg class="orca-illustration" viewBox="0 0 128 96" aria-hidden="true" focusable="false">'
        '<rect class="ill-panel" x="12" y="12" width="80" height="64"/>'
        '<rect class="ill-bar" x="24" y="28" width="44" height="6"/><rect class="ill-bar" x="24" y="42" width="56" height="6"/>'
        '<circle class="ill-lens" cx="86" cy="58" r="16"/><path class="ill-line" d="M98 70l14 14"/></svg>'
    ),
    "error": (
        '<svg class="orca-illustration" viewBox="0 0 128 96" aria-hidden="true" focusable="false">'
        '<rect class="ill-panel" x="16" y="12" width="96" height="72"/>'
        '<path class="ill-line" d="M52 36l24 24M76 36L52 60"/></svg>'
    ),
}


@register.simple_tag
def orca_illustration(kind: str = "empty"):
    return mark_safe(_ILLUSTRATIONS.get(kind, _ILLUSTRATIONS["empty"]))


@register.simple_tag
def orca_timezone_options(selected: str = ""):
    """<option> elements for every IANA timezone, grouped by region, the selected one marked."""
    zones = sorted(z for z in available_timezones() if "/" in z and not z.startswith(("Etc/", "SystemV/")))
    groups: dict[str, list[str]] = {}
    for zone in zones:
        groups.setdefault(zone.split("/", 1)[0], []).append(zone)
    out = ['<option value="UTC"' + (" selected" if selected == "UTC" else "") + ">UTC</option>"]
    for region, items in groups.items():
        out.append(f'<optgroup label="{escape(region)}">')
        for zone in items:
            label = zone.split("/", 1)[1].replace("_", " ").replace("/", " / ")
            sel = " selected" if zone == selected else ""
            out.append(f'<option value="{escape(zone)}"{sel}>{escape(label)}</option>')
        out.append("</optgroup>")
    return mark_safe("".join(out))


_TICKS = re.compile(r"`([^`]+)`")


@register.filter
def orca_inline_code(value):
    """Escape text and turn `backticked` parts into <code> (used by the catalogue pages)."""
    return mark_safe(_TICKS.sub(lambda m: f'<code class="orca-code">{m.group(1)}</code>', escape(str(value))))


@register.filter
def orca_duration(value):
    """Minutes (int) or timedelta → '45 min', '2 h', '1 h 30 min', '3 d 4 h'."""
    if value in (None, ""):
        return ""
    if isinstance(value, dt.timedelta):
        minutes = int(value.total_seconds() // 60)
    else:
        try:
            minutes = int(value)
        except (TypeError, ValueError):
            return value
    days, rest = divmod(abs(minutes), 1440)
    hours, mins = divmod(rest, 60)
    parts = []
    if days:
        parts.append(f"{days} d")
    if hours:
        parts.append(f"{hours} h")
    if mins and not days:
        parts.append(f"{mins} min")
    text = " ".join(parts) or "0 min"
    return ("−" if minutes < 0 else "") + text


@register.filter
def orca_initials(value):
    words = [w for w in str(value or "").replace("-", " ").split() if w[:1].isalpha()]
    if not words:
        return "?"
    if len(words) == 1:
        return words[0][:2].upper()
    return (words[0][0] + words[-1][0]).upper()


# ============================================================================================ component tags
from .. import components as _c  # noqa: E402


@register.inclusion_tag("orca/components/field.html")
def orca_field(bound_field, switch=False, width="", label=None, help_text=None, hide_label=False, horizontal=False):
    """One form field, the ORCA way: label, optional marker, help, error and control, all wired with ARIA.

    {% orca_field form.name %}  {% orca_field form.enabled switch=True %}  {% orca_field form.port width="w8" %}
    """
    return _c.field_context(bound_field, switch=switch, width=width, label=label, help_text=help_text,
                            hide_label=hide_label, horizontal=horizontal)


@register.inclusion_tag("orca/components/form_errors.html")
def orca_form_errors(form):
    """Non-field errors as a callout, and a linked summary when two or more fields are invalid."""
    return _c.form_errors_context(form)


@register.inclusion_tag("orca/components/messages.html", takes_context=True)
def orca_messages(context):
    """django.contrib.messages as dismissible ORCA alerts (errors use role=alert)."""
    return _c.messages_context(context)


@register.inclusion_tag("orca/components/pagination.html", takes_context=True)
def orca_pagination(context, page_obj, noun="items", param="page"):
    """Pagination with gaps and a summary; keeps the other query parameters (filters, sort)."""
    return _c.pagination_context(context, page_obj, noun=noun, param=param)


@register.inclusion_tag("orca/components/mini_calendar.html")
def orca_mini_calendar(month=None, selected=None, today=None, url="", nav_url="", events=(), holidays=None,
                       week_numbers=False):
    """A month grid in the locale's first weekday. url/nav_url patterns use {date} and {month}."""
    return _c.mini_calendar_context(month=month, selected=selected, today=today, url=url, nav_url=nav_url,
                                    events=events, holidays=holidays, week_numbers=week_numbers)


@register.simple_tag
def orca_sparkline(values, label=""):
    """Inline trend line from a list or a comma-separated string of numbers."""
    return mark_safe(_c.sparkline_svg(values, label=label))


@register.inclusion_tag("orca/components/donut.html")
def orca_donut(segments, total_label="Total"):
    """Donut chart with legend from [(label, value), …] or [{"label", "value"}, …]."""
    return _c.donut_context(segments, total_label=total_label)


# ============================================================================================== pattern tags
from .. import calendar_views as _cv  # noqa: E402
from .. import charts as _charts  # noqa: E402


@register.inclusion_tag("orca/patterns/chart.html")
def orca_chart(kind, data, title="", subtitle="", caption="", unit="", stacked=False, horizontal=False):
    """A chart pattern: chart frame, SVG, legend and data table. kind: bar, line, area, pie, doughnut, scatter, bubble, radar, polar."""
    return _charts.chart_context(kind, data, title=title, subtitle=subtitle, caption=caption, unit=unit,
                                 stacked=stacked, horizontal=horizontal)


@register.inclusion_tag("orca/patterns/month_calendar.html")
def orca_month_calendar(events=(), month=None, today=None, selected=None, day_url="", holidays=None, max_per_day=3):
    """Month view: weeks of day cells with up to max_per_day events each and '+N more'."""
    return _cv.month_context(events, month=month, today=today, selected=selected, day_url=day_url,
                             max_per_day=int(max_per_day), holidays=holidays)


@register.inclusion_tag("orca/patterns/time_grid.html")
def orca_week_view(events=(), start=None, days=7, start_hour=7, end_hour=19, today=None, now=None):
    """Week (days=7), multi-day (days=3) or day (days=1) view with positioned events and an all-day row."""
    return _cv.time_grid_context(events, start=start, days=int(days), start_hour=int(start_hour), end_hour=int(end_hour),
                                 today=today, now=now)


@register.inclusion_tag("orca/patterns/agenda.html")
def orca_agenda(events=(), start=None, days=7, today=None):
    """Agenda view: days that have events, each with its list."""
    return _cv.agenda_context(events, start=start, days=int(days), today=today)


@register.inclusion_tag("orca/patterns/year.html")
def orca_year_view(year=None, events=(), today=None, url=""):
    """Year view: twelve mini calendars with event days marked."""
    return _cv.year_context(year=year, events=events, today=today, url=url)


@register.simple_tag
def orca_email_colors():
    """Hex colours and font for HTML emails (email clients cannot read CSS variables)."""
    from ..color import composite, to_hex

    brand = compute_brand()
    light = brand.css["light"]
    return {
        "name": brand.values["name"], "font": "-apple-system, 'Segoe UI', Roboto, Ubuntu, Arial, sans-serif",
        "page": "#f7f7f7", "bg": "#ffffff", "text": "#1a1a1a", "muted": to_hex(composite("rgba(0,0,0,0.6)", "#ffffff")),
        "border": to_hex(composite("rgba(0,0,0,0.2)", "#ffffff")), "brand": light["--orca-brand"],
        "button": light["--orca-brand-strong"], "button_text": light["--orca-brand-on"], "link": light["--orca-accent"],
    }


@register.simple_tag
def orca_email_preview(template="orca/email/base.html", title="", **context):
    """Render an email template into a sandboxed iframe, for documentation and previews."""
    from django.template.loader import render_to_string

    html = render_to_string(template, dict(context, title=title))
    return mark_safe(f'<iframe class="orca-email-preview" sandbox title="Email preview: {escape(title)}" srcdoc="{escape(html)}"></iframe>')
