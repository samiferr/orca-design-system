# ORCA design system

ORCA is a Django design system that helps developers and AI coding agents build consistent, accessible interfaces
without guessing. **Every element has a general description, then when (and when not) and how to use it in ORCA**,
the tokens and classes it uses, the UX principles it applies, and a copy-ready template example.

- **Structure:** five levels from the ORCA Design System Guide, each built from the level before it:
  **Primitives** → **Components** (groups of primitives) → **Patterns** (groups of components) →
  **Templates** (groups of patterns) → **Pages** (templates with real content).
- **Rules:** *Practical UI* (Dannaway, 2024) and *Laws of UX* (Yablonski, 2024). Each element names the rules it applies.
- **Base:** the Tangerine system from `wise_people_analyzer` (Vanilla framework 4.59 values): square corners,
  1.5px borders, filled fields, an 8px grid, light / dark / paper themes. ORCA has one appearance, named ORCA.
- **Grounds:** the same backgrounds as `wise_people_analyzer`: a grey page (`--orca-bg-page`), white panels and
  sidebar (`--orca-bg-panel`), pale yellow stat cards (`--orca-bg-stat`) and a dark brand top bar (`--orca-brand-bar`).
- **Page filters** always open in a right drawer from a Filters button in the page actions (the `filter-drawer` pattern).
- **Phase 1: Primitives.** 141 elements covering all 214 primitive items of the guide, including the planning
  primitives (date, time, calendar marks) the guide marks as not built yet.
- **Phase 2: Components.** 145 elements covering all 154 component items of the guide: form fields,
  pickers, menus, tabs, dialogs, toasts, cards, calendar and schedule parts, plan items. Each lists the primitives it is
  built from, and template tags render the fiddly ones from Django objects.
- **Phase 3: Patterns.** 97 elements covering all 98 pattern items of the guide: page frame (header,
  sidebar, drawer, settings panel), data tables and filtering, forms and editors, media, record management, eight
  chart types, marketing and docs sections, email frame, calendar views, scheduler, event editing and planning boards.
  Chart.js draws the charts (bundled, and loaded only on pages with charts) and the server renders the calendars, both
  from plain Python data through one template tag.
- **Phase 4 (this release): Templates.** 60 elements covering all 67 template items of the guide: real Django templates
  you extend (app shell, auth, error, email, marketing, blog and docs layouts), generic list / detail / form / confirm and
  parent-child templates that work with class-based views, page-type skeletons (dashboard, calendar, scheduler, board,
  timeline, booking, event editor, simple data page), structural layouts and the named slots (blocks) you fill.

## Install

```bash
pip install orca-design-system
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
    <h1 class="orca-page-title">Images</h1>
    <button class="orca-button orca-button--primary" type="button">{% icon "plus" %}Add image</button>
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
  <div class="orca-form-actions"><button class="orca-button orca-button--primary" type="submit">Save video</button></div>
</form>
{% orca_pagination page_obj noun="videos" %}        {# keeps filters in the links #}
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

## Pages from templates

```python
from django.views.generic import ListView
from orca.mixins import OrcaPageMixin

class VideoList(OrcaPageMixin, ListView):
    model = Video
    paginate_by = 25
    template_name = "orca/generic/list.html"          # title, Add button, search, table → cards on phones, pager
    list_columns = ["name", "site", "status", ("Counted today", "today")]
    detail_url_name, create_url_name = "video-detail", "video-create"
    update_url_name, delete_url_name = "video-update", "video-delete"
```

```django
{% extends "orca/layouts/app.html" %}                   {# or dashboard, calendar, scheduler, board, timeline… #}
{% block page_actions %}<a class="orca-button orca-button--primary" href="…">Add video</a>{% endblock %}
{% block content %}…{% endblock %}
```

Set `nav` (sidebar sections) in a context processor once. Error pages: create `templates/404.html` with
`{% extends "orca/errors/404.html" %}` (same for 403 and 500).

## Brand tokens only

A project changes **brand tokens only**, through `settings.ORCA["BRAND"]`:

| Key | CSS | What it does |
|---|---|---|
| `name` | – | Product name: logo alt text and wordmark |
| `logo`, `favicon` | – | Static paths of the logo and favicon |
| `color` | `--orca-brand`, `--orca-brand-strong*`, `--orca-brand-bar*` | Brand colour; fills that carry text are derived to reach 4.5:1; the top bar is the colour mixed with 30% black |
| `on_color` | `--orca-brand-on` | Text on brand fills (auto black/white when empty) |
| `accent`, `accent_dark` | `--orca-accent` | Interactive colour per theme; adjusted to reach 4.5:1 |
| `font_sans`, `font_mono` | `--orca-font-sans`, `--orca-font-mono` | Font stacks |

Write colours as `"0F95A1"`, `"#06c"` or `rgb(…)`; ORCA normalises them. If a colour fails contrast, ORCA adjusts it
and reports the change as the system-check warning `orca.W001`. Unknown keys are errors (`orca.E002`). Every other
token is fixed, and `python manage.py orca_lint` flags any override of a non-brand `--orca-*` token.

## Find the right element

```bash
python -m orca list                 # every element by category
python -m orca show button          # general description / when / how / example
python -m orca search date          # search names, guide items and classes
python -m orca icons                # icon names and aliases
python -m orca tokens               # token names and usage
python manage.py orca_element switch
python manage.py orca_lint templates/   # check templates and CSS against ORCA's rules
python manage.py orca_site site/        # export the documentation website
```

The same content is in [`docs/primitives/`](docs/primitives/README.md) and [`docs/components/`](docs/components/README.md) and [`docs/patterns/`](docs/patterns/README.md) and [`docs/templates/`](docs/templates/README.md) (Markdown, one file per category) and
[`docs/catalogue.json`](docs/catalogue.json) (machine-readable). AI agents: start with [`AGENTS.md`](AGENTS.md).

## What is in the package

| Path | Content |
|---|---|
| `orca/tokens.py` | Single source of every token (generated into `static/orca/css/tokens.css`) |
| `orca/static/orca/css/orca.css` | All primitives, in cascade layers `orca.base`, `orca.primitives`, `orca.utilities` |
| `orca/static/orca/css/components.css` | All components, in the `orca.components` layer |
| `orca/static/orca/css/patterns.css` | All patterns, in the `orca.patterns` layer |
| `orca/static/orca/css/templates.css` | Structural layouts and page frames, in the `orca.templates` layer |
| `orca/templates/orca/layouts/`, `orca/generic/`, `orca/errors/` | The Django templates you extend |
| `orca/mixins.py` | `OrcaPageMixin` for class-based views |
| `orca/charts.py`, `orca/calendar_views.py` | Server side of the chart and calendar pattern tags |
| `orca/samples.py` | Sample data used by the documentation examples |
| `orca/static/orca/js/orca.js` | Optional progressive enhancement, opt-in by data attribute: menus, listbox, combobox, tabs, dialogs and confirm, toasts, date shortcuts and ranges, repeating rows, carousel, steppers, OTP, theme |
| `orca/components.py` | Server side of the component tags (field wiring, page windows, month grids, charts) |
| `orca/catalogue/` | The element catalogue: when, how, a11y, tokens, classes, principles, examples |
| `orca/data/about/` | The general description of every element (what it is, use cases, when not to use it, best practices) |
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

The tests check that every guide item is covered, every element has a general description, its when/how and a rendering example,
documented classes and tokens exist, text and control contrast hold in all three themes, and generated files are current.

## Roadmap

1. **Primitives** (released): the smallest pieces and the base styles.
2. **Components** (released): groups of primitives (form field, search bar, date picker, pagination, stat card…).
3. **Patterns** (released): groups of components (page head with page actions, filter drawer, sidebar, data table…).
4. **Templates** (this release): groups of patterns (app shell, list page, detail page…).
5. Pages: templates filled with real content.

## Licences

ORCA's code is MIT. Token values, component measurements and 106 icon shapes come from Canonical's Vanilla framework
4.59 (LGPL-3.0) through Tangerine; Ubuntu Sans fonts are under the Ubuntu Font Licence 1.0; the vendored Chart.js 4.4.7 is MIT, highlight.js 11.10 is BSD-3-Clause and JetBrains Mono is under the SIL Open Font Licence 1.1. ORCA is not affiliated with
Canonical. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
