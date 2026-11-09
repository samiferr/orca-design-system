# Structural layouts

Layout classes that arrange sections inside a page: stacks, grids and splits. They hold patterns and never style them.

## Vertical stack

`id: vertical-stack` · level: template · source: ORCA

Sections one under another with one spacing step between them; tight and loose variants.

Built from: `panel`

### Why

Equal gaps between sections show they are siblings, and larger gaps than inside a section show where one ends (Practical UI L09).

### When to use

- The main column of almost every page; the sections of a side panel.

### How to use

- `<div class="orca-vstack">` around the sections; `--tight` (12px) inside panels, `--loose` (40px) between page regions.
- Do not add margins to the children: the stack owns the spacing.

#### Example: Stack

```django
<div class="orca-vstack"><section class="orca-panel" aria-label="Section one"><p class="orca-panel-title">Section one</p><div class="orca-skeleton orca-skeleton--text"></div></section><section class="orca-panel" aria-label="Section two"><p class="orca-panel-title">Section two</p><div class="orca-skeleton orca-skeleton--text"></div></section></div>
```

**Classes:** `.orca-vstack`, `.orca-vstack--tight`, `.orca-vstack--loose`

**Principles applied:** Practical UI L09: Set spacing by relationship; Practical UI L08: Define a limited spacing scale

**ORCA guide items covered:** Vertical stack

---

## Stat grid

`id: stat-grid` · level: template · source: ORCA

Stat cards in equal columns that wrap, each at least 12rem wide.

Built from: `kpi-grid`

### Why

Equal tiles in a row are compared at a glance (Miller's law); a minimum width keeps every number readable on any screen (Practical UI L11).

### When to use

- Headline numbers at the top of a dashboard or a parent record.

### How to use

- `<div class="orca-stat-grid">` of stat cards; keep to 3–6 cards.

#### Example: Stats

```django
<div class="orca-stat-grid"><div class="orca-stat-card"><div class="orca-stat-card__head"><p class="orca-stat-label">Metric 1</p><span class="orca-stat-card__icon" aria-hidden="true">{% icon "statistics" %}</span></div><p class="orca-stat-value">1,234</p></div><div class="orca-stat-card"><div class="orca-stat-card__head"><p class="orca-stat-label">Metric 2</p><span class="orca-stat-card__icon" aria-hidden="true">{% icon "statistics" %}</span></div><p class="orca-stat-value">56</p></div><div class="orca-stat-card"><div class="orca-stat-card__head"><p class="orca-stat-label">Metric 3</p><span class="orca-stat-card__icon" aria-hidden="true">{% icon "statistics" %}</span></div><p class="orca-stat-value">98%</p></div></div>
```

**Classes:** `.orca-stat-grid`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI L11: Align the layout with a responsive grid

**ORCA guide items covered:** Stat grid

---

## Card grid

`id: card-grid-layout` · level: template · source: ORCA

Cards in as many equal columns as fit, at least 15rem wide.

Built from: `card-grid`

### Why

A regular grid lets people scan many similar items by position (Practical UI L11); auto-fill adapts from one column on phones to four on wide screens without breakpoints.

### When to use

- Collections browsed by picture or title: videos, products, people, plans.

### When not to use

- Items compared on several attributes: use a table.

### How to use

- `<ul class="orca-card-grid">` of `<li class="orca-card">`; override the minimum with `grid-template-columns` only for a different card type.

#### Example: Cards

```django
<ul class="orca-card-grid"><li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Card 1</h3><p class="orca-card-meta">Meta line</p></div></li><li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Card 2</h3><p class="orca-card-meta">Meta line</p></div></li><li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Card 3</h3><p class="orca-card-meta">Meta line</p></div></li><li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Card 4</h3><p class="orca-card-meta">Meta line</p></div></li></ul>
```

**Classes:** `.orca-card-grid`

**Principles applied:** Practical UI L11: Align the layout with a responsive grid; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Card grid

---

## Two-column grid

`id: two-column-grid` · level: template · source: ORCA

Two equal columns from 1036px, one column below.

Built from: `panel`

### Why

Two equal columns pair related panels (two charts, two lists) for comparison (Practical UI L01) while staying readable; on narrow screens they stack in reading order.

### When to use

- Pairs of charts or panels of the same importance.

### How to use

- `<div class="orca-two-col">` with exactly two children (more wrap into rows of two).

#### Example: Two columns

```django
<div class="orca-two-col"><section class="orca-panel" aria-label="Left"><p class="orca-panel-title">Left</p><div class="orca-skeleton orca-skeleton--text"></div></section><section class="orca-panel" aria-label="Right"><p class="orca-panel-title">Right</p><div class="orca-skeleton orca-skeleton--text"></div></section></div>
```

**Classes:** `.orca-two-col`

**Principles applied:** Practical UI L01: Group related information; Practical UI L11: Align the layout with a responsive grid

**ORCA guide items covered:** Two-column grid

---

## Split (main + aside)

`id: split-layout` · level: template · source: ORCA

A main column and a 20rem aside (end by default, start or wider as variants); the aside drops below on narrow screens.

Built from: `panel`

### Why

Primary content gets the width and secondary context sits beside it, not in the way (Practical UI L03); below 1036px the aside follows the main content so reading order holds.

### When to use

- A form with help or conflicts beside it, a record with related items, a booking with its summary.

### How to use

- `<div class="orca-split">` with the main element first, then `<aside>`; `--aside-start` puts the aside first on wide screens, `--wide-aside` makes it 26rem.

#### Example: Split

```django
<div class="orca-split"><section class="orca-panel" aria-label="Main"><p class="orca-panel-title">Main</p><div class="orca-skeleton orca-skeleton--text"></div></section><aside><section class="orca-panel" aria-label="Aside"><p class="orca-panel-title">Aside</p><div class="orca-skeleton orca-skeleton--text"></div></section></aside></div>
```

**Classes:** `.orca-split`, `.orca-split--aside-start`, `.orca-split--wide-aside`

**Principles applied:** Practical UI L03: Establish an order of importance; Practical UI L01: Group related information

**ORCA guide items covered:** Split (main + aside)

---

## Media split

`id: media-split` · level: template · source: Tangerine

The live picture in two thirds, details and actions in one third; the picture stays in view while the details scroll.

Built from: `recording-player`, `panel`

### Why

When watching and adjusting at the same time (zones, settings), the picture must stay visible next to the controls (Practical UI L14: less travel between related things).

### When to use

- Video, zone and recording pages; any media with its settings.

### How to use

- `<div class="orca-media-split">` with `.orca-media-split__media` (the player or snapshot) and `.orca-media-split__side` (panels).

#### Example: Media split

```django
<div class="orca-media-split"><div class="orca-media-split__media"><div class="orca-skeleton orca-aspect-16x9"></div></div><div class="orca-media-split__side"><section class="orca-panel" aria-label="Status"><p class="orca-panel-title">Status</p><div class="orca-skeleton orca-skeleton--text"></div></section><section class="orca-panel" aria-label="Settings"><p class="orca-panel-title">Settings</p><div class="orca-skeleton orca-skeleton--text"></div></section></div></div>
```

**Classes:** `.orca-media-split`, `.orca-media-split__media`, `.orca-media-split__side`

**Principles applied:** Practical UI L14: Reduce travel between related actions; Practical UI L01: Group related information

**ORCA guide items covered:** Media split

---

## Form grid

`id: form-grid` · level: template · source: ORCA

Short fields side by side in as many 16rem columns as fit; long fields span the full width.

Built from: `form-section`

### Why

Short related fields (host and port, from and to) read as one unit side by side (Practical UI L01); long answers keep the full width. Use only for short, related fields: one column is still the default (R01).

### When to use

- Settings pages with many short fields; address and connection details.

### When not to use

- Ordinary forms: use one column (narrow form).

### How to use

- `<div class="orca-form-grid">` of fields; add `.orca-form-grid__full` to textareas and anything long.

#### Example: Connection

```django
<div class="orca-form-grid"><div class="orca-field"><label class="orca-label" for="fg-h">Host</label><input class="orca-input" id="fg-h"></div><div class="orca-field"><label class="orca-label" for="fg-p">Port</label><input class="orca-input orca-input--w8" id="fg-p" inputmode="numeric"></div><div class="orca-field orca-form-grid__full"><label class="orca-label" for="fg-n">Notes <span class="orca-optional">(optional)</span></label><textarea class="orca-textarea" id="fg-n" rows="2"></textarea></div></div>
```

**Classes:** `.orca-form-grid`, `.orca-form-grid__full`

**Principles applied:** Practical UI L01: Group related information; Practical UI R01: Keep the main form flow in one column; Practical UI R06: Match input width to the expected answer

**ORCA guide items covered:** Form grid

---

## Narrow form

`id: narrow-form` · level: template · source: ORCA

One column of fields at most 36rem wide.

Built from: `form-stack`

### Why

A single, narrow column is read and filled top to bottom without missing fields (Practical UI R01), and short line lengths keep labels and help readable (T09).

### When to use

- Every ordinary form: create, edit, settings, sign-up.

### How to use

- `<div class="orca-narrow-form">` around the form; the generic form templates use it.

#### Example: Form

```django
<div class="orca-narrow-form"><div class="orca-form-stack"><div class="orca-field"><label class="orca-label" for="nf-a">Name</label><input class="orca-input" id="nf-a"></div><div class="orca-field"><label class="orca-label" for="nf-b">Email</label><input class="orca-input" id="nf-b" type="email"></div><div class="orca-form-actions"><button class="orca-button orca-button--primary" type="button">Save</button></div></div></div>
```

**Classes:** `.orca-narrow-form`

**Principles applied:** Practical UI R01: Keep the main form flow in one column; Practical UI T09: Limit reading measure

**ORCA guide items covered:** Narrow form

---
