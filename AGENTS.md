# ORCA for AI coding agents

You are building a Django UI with ORCA. Follow these rules exactly. When unsure, look the element up; do not invent.

## 1. Look up before you write

- `python -m orca search <words>` finds the element; `python -m orca show <id>` prints its **why, when, when not, how,
  accessibility notes, classes, tokens and a working example**. Copy the example, then adapt the content.
- The same text is in `docs/primitives/<category>.md` and `docs/catalogue.json`.
- Run `python manage.py orca_lint <templates dir>` before you finish. Fix every finding.

## 2. Hard rules

1. **Tokens only.** Never hard-code a colour, size, radius, shadow, z-index or duration. Use `var(--orca-*)`.
2. **Brand tokens only can change**, and only in `settings.ORCA["BRAND"]` (name, logo, favicon, color, on_color,
   accent, accent_dark, font_sans, font_mono). Never redefine another `--orca-*` token.
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
10. **Write like ORCA**: sentence case, verbs on buttons ("Save camera", never "OK"/"Submit"), no exclamation marks,
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

## 4. Page skeleton

```django
{% load orca %}<!doctype html>
<html {% orca_html_attrs %}>
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">{% orca_head %}</head>
<body>
  <a class="orca-skip-link" href="#main">Skip to main content</a>
  <main id="main" tabindex="-1">…</main>
</body>
</html>
```

## 5. Scope of this release

Phase 1 ships **primitives** only. Components, patterns, templates and pages from the ORCA guide come next; until
then, build them from primitives, following each primitive's "how" rules.
