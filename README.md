# ORCA design system

ORCA is a Django design system built so that developers and AI coding agents can produce consistent, accessible
interfaces without guessing. **Every element documents its why, when (and when not), and how**, the tokens and classes
it uses, the UX principles it applies, and a copy-ready template example.

- **Structure:** the ORCA Design System Guide (Atomic Design with ORCA names):
  Primitives → Components → Patterns → Templates → Pages.
- **Rules:** *Practical UI* (Dannaway, 2024) and *Laws of UX* (Yablonski, 2024). Each element cites the rules it applies.
- **Base:** the Tangerine system from `wise_people_analyzer` (Vanilla framework 4.59 values): square corners,
  1.5px borders, filled fields, an 8px grid, light / dark / paper themes. ORCA has one appearance: Tangerine.
- **Phase 1: Primitives.** 141 elements covering all 214 primitive items of the guide, including the planning
  primitives (date, time, calendar marks) the guide marks as not built yet.
- **Phase 2: Components.** 145 elements covering all 154 component items of the guide: form fields,
  pickers, menus, tabs, dialogs, toasts, cards, calendar and schedule parts, plan items. Each lists the primitives it is
  built from, and template tags render the fiddly ones straight from Django objects.
- **Phase 3 (this release): Patterns.** 97 elements covering all 98 pattern items of the guide: page frame (header,
  sidebar, drawer, settings panel), data tables and filtering, forms and editors, media, record management, eight
  chart types, marketing and docs sections, email frame, calendar views, scheduler, event editing and planning boards.
  Charts and calendars render on the server as SVG and HTML from plain Python data: no JavaScript library.

## Install

```bash
pip install git+https://github.com/samiferr/orca-design-system.git
```

```python
# settings.py
INSTALLED_APPS = [..., "django.contrib.staticfiles", "orca"]

ORCA = {
    "BRAND": {                # the only values a project may change
        "name": "Acme",
        "color": "#0f95a1",   # brand colour
        "accent": "#0066cc",  # interactive colour (links, ticks, switches)
        "logo": "brand/logo.svg",
        "favicon": "brand/favicon.svg",
    },
    "THEME": "auto",          # auto | light | dark | paper
    "DENSITY": "comfortable", # comfortable | dense (tighter type, controls and spacing)
}
```

```django
{# base.html #}
{% load orca %}<!doctype html>
<html {% orca_html_attrs %}>
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  {% orca_head %}
</head>
<body>
  <a class="orca-skip-link" href="#main">Skip to main content</a>
  <main id="main" tabindex="-1">
    <h1 class="orca-page-title">Cameras</h1>
    <button class="orca-button orca-button--primary" type="button">{% icon "plus" %}Add camera</button>
  </main>
</body>
</html>
```

## Documentation website

The documentation website is generated from the package itself: an overview, nine guide pages (installation, usage,
brand and themes, AI agents, principles, accessibility, localization, tooling, roadmap), one page per element with
live examples, and the token and icon references.

```python
# serve it inside your project, with your brand
path("orca/", include("orca.urls")),
```

```bash
# or export it as static HTML (one file per page, relative links)
python demo/manage.py orca_site site/
```

`.github/workflows/docs.yml` tests, exports and deploys it to GitHub Pages on every push to `main`
(enable it once: repository Settings, Pages, Source: GitHub Actions).

## Components from Django objects

```django
{% load orca %}
{% orca_messages %}                                  {# django.contrib.messages as alerts #}
<form method="post">{% csrf_token %}
  {% orca_form_errors form %}                        {# non-field errors + linked summary #}
  <div class="orca-fields">
    {% orca_field form.name %}                       {# label, (optional), help, error, control, ARIA #}
    {% orca_field form.port width="w8" %}
    {% orca_field form.enabled switch=True %}
  </div>
  <div class="orca-form-actions"><button class="orca-button orca-button--primary" type="submit">Save camera</button></div>
</form>
{% orca_pagination page_obj noun="cameras" %}        {# keeps filters in the links #}
{% orca_mini_calendar month selected=day url="/day/{date}/" nav_url="?month={month}" %}
{% orca_sparkline values "Visitors per hour" %}  {% orca_donut segments total_label="Visitors" %}
```

## Patterns from your data

```django
{% orca_chart "bar" data title="Visitors per day" subtitle="This week" %}    {# data: {"labels": [...], "series": [{"name", "values"}]} #}
{% orca_month_calendar events month="2026-11" today=today day_url="?day={date}" %}
{% orca_week_view events start=monday days=7 today=today now=now %}          {# days=1 day view, days=3 multi-day #}
{% orca_agenda events start=today days=7 %}  {% orca_year_view year=2026 events=events %}
{% extends "orca/email/base.html" %}                                         {# brand-coloured transactional email #}
```

Events are dicts with `title`, `start`, `end`, `all_day`, `color` (1–8 or any CSS colour), `url`, `location` and
`status`. `orca.samples.SAMPLE` holds the realistic data every documentation example uses.

## Brand tokens only

A project changes **brand tokens only**, through `settings.ORCA["BRAND"]`:

| Key | CSS | What it does |
|---|---|---|
| `name` | – | Product name: logo alt text and wordmark |
| `logo`, `favicon` | – | Static paths of the logo and favicon |
| `color` | `--orca-brand`, `--orca-brand-strong*`, | Brand colour; fills that carry text are derived to reach 4.5:1 |
| `on_color` | `--orca-brand-on` | Text on brand fills (auto black/white when empty) |
| `accent`, `accent_dark` | `--orca-accent` | Interactive colour per theme; adjusted to reach 4.5:1 |
| `font_sans`, `font_mono` | `--orca-font-sans`, `--orca-font-mono` | Font stacks |

Input is accepted liberally (`"0F95A1"`, `"#06c"`, `rgb(…)`) and normalised. If a colour would fail contrast, ORCA
adjusts it and reports what it did as the system-check warning `orca.W001`; unknown keys are errors (`orca.E002`).
Every other token is fixed, and `python manage.py orca_lint` flags any override of a non-brand `--orca-*` token.

## Find the right element

```bash
python -m orca list                 # every element by category
python -m orca show button          # why / when / how / example
python -m orca search date          # search names, guide items and classes
python -m orca icons                # icon names and aliases
python -m orca tokens               # token names and usage
python manage.py orca_element switch
python manage.py orca_lint templates/   # check templates and CSS against ORCA's rules
python manage.py orca_site site/        # export the documentation website
```

The same content is in [`docs/primitives/`](docs/primitives/README.md) and [`docs/components/`](docs/components/README.md) and [`docs/patterns/`](docs/patterns/README.md) (Markdown, one file per category) and
[`docs/catalogue.json`](docs/catalogue.json) (machine-readable). AI agents: start with [`AGENTS.md`](AGENTS.md).

## What is in the package

| Path | Content |
|---|---|
| `orca/tokens.py` | Single source of every token (generated into `static/orca/css/tokens.css`) |
| `orca/static/orca/css/orca.css` | All primitives, in cascade layers `orca.base`, `orca.primitives`, `orca.utilities` |
| `orca/static/orca/css/components.css` | All components, in the `orca.components` layer |
| `orca/static/orca/css/patterns.css` | All patterns, in the `orca.patterns` layer |
| `orca/charts.py`, `orca/calendar_views.py` | Server side of the chart and calendar pattern tags |
| `orca/samples.py` | Sample data used by the documentation examples |
| `orca/static/orca/js/orca.js` | Optional progressive enhancement, opt-in by data attribute: menus, listbox, combobox, tabs, dialogs and confirm, toasts, date shortcuts and ranges, repeating rows, carousel, steppers, OTP, theme |
| `orca/components.py` | Server side of the component tags (field wiring, page windows, month grids, charts) |
| `orca/catalogue/` | The element catalogue: why, when, how, a11y, tokens, classes, principles, examples |
| `orca/templatetags/orca.py` | `orca_head`, `orca_html_attrs`, `icon`, `status_icon`, `orca_logo`, `orca_illustration`, `orca_timezone_options`, filters `orca_duration`, `orca_initials` |
| `orca/icons.py`, `orca/data/` | 106 Vanilla glyphs plus ORCA glyphs (home, edit, calendar, clock, …) |
| `orca/checks.py` | Django system checks for `settings.ORCA` |

## Develop

```bash
python -m venv .venv && .venv/bin/pip install -e .
.venv/bin/python -m orca build                       # regenerate tokens.css and docs/
.venv/bin/python -m django test tests --settings=tests.settings
.venv/bin/python demo/manage.py runserver            # catalogue at http://127.0.0.1:8000/orca/
```

The tests check that every guide item is covered, every element has its why/when/how and a rendering example,
documented classes and tokens exist, text and control contrast hold in all three themes, and generated files are current.

## Roadmap

1. **Primitives** (released).
2. **Components** (released).
3. **Patterns** (this release).
4. Templates, 5. Pages: following the ORCA guide.

## Licences

ORCA's code is MIT. Token values, component measurements and 106 icon shapes come from Canonical's Vanilla framework
4.59 (LGPL-3.0) through Tangerine; Ubuntu Sans fonts are under the Ubuntu Font Licence 1.0. ORCA is not affiliated with
Canonical. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
