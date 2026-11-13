# ORCA for AI coding agents

You are building a Django UI with ORCA. Follow these rules exactly. When unsure, look the element up; do not invent.

## 1. Look up before you write

- `python -m orca search <words>` finds the element; `python -m orca show <id>` prints its **when, when not, how,
  accessibility notes, classes, tokens and a working example**. Copy the example, then adapt the content.
- The same text is in `docs/primitives/<category>.md`, `docs/components/<category>.md`, `docs/patterns/<category>.md`, `docs/templates/<category>.md` and `docs/catalogue.json`.
- When an element needs Python (views, forms, mixins, URLs, settings), `python -m orca show <id>` ends with its
  **Server code**: copy it too. Generic pages use `orca.mixins.OrcaPageMixin`; charts and calendars take plain data.
- **Prefer a pattern over assembling components, and a component over assembling primitives.** Each element's
  "Built from" list names what it is made of.
- Charts, calendars and emails come from tags; never hand-draw SVG or write a Chart.js configuration yourself (the tags draw charts with Chart.js in token colours): `{% orca_chart kind data %}`,
  `{% orca_month_calendar events %}`, `{% orca_week_view events days=7|3|1 %}`, `{% orca_agenda events %}`,
  `{% orca_year_view year events=events %}`, and emails extend `orca/email/base.html`.
- With Django forms, render every field with `{% orca_field form.x %}` (and `switch=True` for settings that apply at once);
  put `{% orca_form_errors form %}` above the fields and `{% orca_messages %}` at the top of the page;
  paginate with `{% orca_pagination page_obj noun="…" %}`.
- Run `python manage.py orca_lint <templates dir>` before you finish. Fix every finding.

## 2. Hard rules

1. **Tokens only.** Never hard-code a colour, size, radius, shadow, z-index or duration. Use `var(--orca-*)`.
2. **Brand tokens only can change**, and only in `settings.ORCA["BRAND"]` (name, logo, favicon, color, on_color,
   accent, accent_dark, font_sans, font_mono). Never redefine another `--orca-*` token.
   For a tighter interface use the density mode (`ORCA["DENSITY"] = "dense"`, or `data-density="dense"` on a region),
   never smaller sizes of your own.
3. **Only classes that exist.** If `python -m orca search` has no element for what you need, compose existing
   primitives with the utilities `.orca-stack` and `.orca-row`; do not invent `orca-*` class names.
4. **One primary action per screen** (`orca-button--primary`). Secondary actions use the default button; rare ones
   `--ghost` or `--link`. A destructive first step is never red; confirm it in a dialog with `--danger`.
5. **Every control has a visible label** (`<label class="orca-label" for>`). Placeholders are not labels.
   Help text goes **between label and field** with `aria-describedby`. Errors go above the field with
   `aria-invalid="true"`, an error icon and a sentence that says how to fix it.
6. **Status is never colour alone**: a word plus an icon or shape (`badge`, `status-dot`, `status-icon`).
7. **Icons**: `{% icon "name" %}` from the ORCA set only; icon-only buttons need `aria-label`. Never mix another set.
8. **Every `<button>` has `type`**; every `<img>` has `alt` (`alt=""` if decorative).
9. **Native controls first**: `<input type="date">`, `<select>`, `<dialog>`, `<details>`, `<progress>`.
10. **Page filters live in a right drawer.** A page's filters never sit in a row above the results or in a side
    column: a `Filters` button (filter icon, count of applied filters) in the page actions (`{% block page_actions %}`,
    `.orca-page-head__actions`) opens the `filter-drawer` pattern (`<dialog class="orca-drawer">`, right side).
    Applied filters show above the results as removable tags with `Clear all` (`filter-bar`).
11. **Grounds as in wise_people_analyzer**: the body is `--orca-bg-page` (set by ORCA); panels, cards and the
    sidebar are `--orca-bg-panel`; stat cards are `--orca-bg-stat` with `--orca-border-stat`; the top bar is
    `--orca-brand-bar` with `--orca-brand-bar-on` text. Patterns already apply them.
12. **Write like ORCA**: sentence case, verbs on buttons ("Save image", never "OK"/"Submit"), no exclamation marks,
    numbers as digits with separators, errors say what happened and what to do.

## 3. Choosing between similar elements

| Need | Use | Not |
|---|---|---|
| On/off saved with the form | `checkbox` | `switch` |
| On/off applied immediately | `switch` | `checkbox` |
| One of ≤ 7 options | `radio` | `select` |
| One of many known options | `select` / `timezone-select` | radios |
| Small number change | `number-input` (stepper) | select |
| Category / keyword | `tag` | `badge` |
| Record status | `badge` or `status-dot` | `tag` |
| Waiting < 1 s | nothing or `spinner` in the button | progress bar |
| Waiting, known progress | `progress-bar` with text | spinner |
| Region loading later | `skeleton` | spinner |
| Date for people | `date-label` (`6 November 2026`) | `06/11/2026` |
| A form field | `form-field` via `{% orca_field %}` | hand-written label + input |
| Event result that stays | `alert` | toast |
| Quick confirmation, maybe Undo | `toast` (`ORCA.toast(…)`) | alert |
| Guidance that belongs to the page | `callout` | alert |
| Irreversible action | `confirm-dialog` (`data-orca-confirm`) | a red first button |
| Several secondary actions | `dropdown-menu` / `record-actions` | a row of equal buttons |
| One of many known options, typed | `combobox` | long select |
| Several items from a long list | `multi-picker` | listbox |
| Views of one object | `tab-bar` | buttons |
| Cards vs table, period, granularity | `view-toggle`, `period-selector`, `granularity-selector` (segmented) | tabs |

## 4. Page skeleton

Do not write the document skeleton yourself: extend a layout.

```django
{% extends "orca/layouts/app.html" %}{% load orca %}
{% block page_actions %}<a class="orca-button orca-button--primary" href="{% url 'image-create' %}">Add image</a>{% endblock %}
{% block content %}<div class="orca-vstack">…patterns…</div>{% endblock %}
```

Context: `title`, `subtitle`, `breadcrumbs` [(label, url)], `nav` (sidebar sections). Other layouts: `auth`, `error`,
`marketing`, `docs`, `dashboard`, `calendar`, `scheduler`, `board`, `timeline`, `booking`, `event_editor`,
`simple_data`; CRUD: `orca/generic/list|detail|form|confirm_delete|confirm_action.html` and the parent-child set.
`python -m orca show app-shell` lists every block and context variable.

## 5. Levels and scope of this release

Each ORCA level is a group of the level before it, never skipping one (a pattern uses components, not primitives):

| Level | Is a group of | Examples |
|---|---|---|
| Primitive | – (smallest piece) | button, input, icon, text style, status mark |
| Component | primitives | form field, search bar, date picker, stat card |
| Pattern | components | page head with page actions, filter drawer, data table |
| Template | patterns | app shell, list page, detail page |
| Page | a template with real content | the empty, overdue, right-to-left and dark variations |

Released: **primitives**, **components**, **patterns** and **templates**. Pages from the ORCA guide come next.
Start every page from a template: extend `orca/layouts/app.html` (or a page-type layout) and fill its blocks;
for CRUD use `orca/generic/*.html` with `orca.mixins.OrcaPageMixin`. Never copy a layout's markup into a page.
