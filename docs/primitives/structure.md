# Structure marks

Marks that organise and connect: rules, separators, focus, markers and backdrops. Plus the accessibility helpers every page needs.

## Divider

`id: divider` · level: primitive · source: Tangerine

A horizontal or vertical rule: default, muted, medium and large spacing, labelled, highlight and brand.

### Why

A rule separates groups when space alone is not enough (Practical UI L01); used sparingly it chunks content (Miller's law).

### When to use

- Between groups in a menu, between sections of a panel, between toolbar groups (vertical).
- Labelled: 'or' between alternative sign-in methods.

### When not to use

- Between every item: use spacing or row separators.
- To fake a heading: use a section title.

### How to use

- `<hr class="orca-divider">` (16px above and below). `--md` 24px, `--lg` 48px, `--flush` 0, `--muted` lighter line.
- Vertical: `<span class="orca-divider orca-divider--vertical" role="separator" aria-orientation="vertical"></span>` inside a flex row.
- Labelled: `<div class="orca-divider orca-divider--labeled" role="separator">or</div>`.
- Emphasis: `--highlight` (3px text colour) or `--brand` (3px brand).

#### Example: Dividers

```django
<div style="max-width: 24rem">
  <p class="orca-p">Above</p><hr class="orca-divider"><p class="orca-p">Below</p>
  <div class="orca-divider orca-divider--labeled" role="separator">or</div>
  <div class="orca-row"><span>Left</span><span class="orca-divider orca-divider--vertical" role="separator" aria-orientation="vertical"></span><span>Right</span></div>
  <hr class="orca-divider orca-divider--highlight orca-divider--md">
</div>
```

**Classes:** `.orca-divider`, `.orca-divider--muted`, `.orca-divider--md`, `.orca-divider--lg`, `.orca-divider--vertical`, `.orca-divider--labeled`, `.orca-divider--highlight`, `.orca-divider--brand`

**Tokens:** `--orca-border`, `--orca-border-weak`, `--orca-hairline`, `--orca-bar`

**Principles applied:** Practical UI L01: Group related information; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Divider; Divider (medium, large, vertical, labeled)

---

## Chevron separator

`id: chevron-separator` · level: primitive · source: Tangerine

A small muted chevron between breadcrumb items or path segments.

### Why

The chevron reads as 'inside' by convention (Jakob's law) and is mirrored in right-to-left languages (Postel's law).

### When to use

- Breadcrumbs, path displays (Library › Album › Image).

### How to use

- `<span class="orca-sep" aria-hidden="true">{% icon "chevron-right" %}</span>` between items.
- In breadcrumbs the list structure carries the meaning; the separator is hidden from screen readers.

#### Example: Path

```django
<nav aria-label="Breadcrumb" class="orca-small"><a class="orca-link orca-link--plain" href="#">Library</a><span class="orca-sep" aria-hidden="true">{% icon "chevron-right" %}</span><a class="orca-link orca-link--plain" href="#">Summer 2026</a><span class="orca-sep" aria-hidden="true">{% icon "chevron-right" %}</span><span aria-current="page">Harbour at dusk</span></nav>
```

**Classes:** `.orca-sep`

**Tokens:** `--orca-text-muted`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Chevron separator

---

## Screen-reader-only text

`id: sr-only` · level: primitive · source: Tangerine

Text that is read by assistive technology but not shown.

### Why

Some meaning is visual only (an arrow, a position in a grid); hidden text gives screen-reader users the same information (Postel's law, Practical UI F01).

### When to use

- Completing a visual cue: '(opens in a new tab)', 'compared with last week', the name of an icon-only control in a table.

### When not to use

- Hiding text sighted keyboard users also need.
- Duplicating text that is already read.

### How to use

- `<span class="orca-sr-only">compared with last week</span>`.
- `.orca-sr-only-focusable` shows the element again when it receives focus.

#### Example: Hidden context

```django
<span class="orca-delta orca-delta--up">{% icon "arrow-up" size="xs" %}+8%<span class="orca-sr-only"> compared with last week</span></span>
```

**Classes:** `.orca-sr-only`, `.orca-sr-only-focusable`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Practical UI F01: Design for a diverse audience

**ORCA guide items covered:** Screen-reader-only text

---

## Skip link

`id: skip-link` · level: primitive · source: Tangerine

The first focusable link on every page, jumping past navigation to the main content.

### Why

Keyboard and screen-reader users would otherwise tab through the whole navigation on every page (Fitts's law for the keyboard: shortest path; WCAG 2.4.1).

### When to use

- Every page with navigation before the content.

### How to use

- First element in `<body>`: `<a class="orca-skip-link" href="#main">Skip to main content</a>` and `<main id="main" tabindex="-1">`.
- It is invisible until focused, then appears top-left above everything.

#### Example: Skip link (press Tab inside this example)

```django
<div style="position: relative; height: 3rem; overflow: hidden">
  <a class="orca-skip-link" href="#main">Skip to main content</a>
  <p class="orca-small orca-muted" style="padding: var(--orca-space-8)">Tab into this box to reveal the link.</p>
</div>
```

**Classes:** `.orca-skip-link`

**Tokens:** `--orca-layer-skip`, `--orca-bg-elevated`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI F01: Design for a diverse audience

**ORCA guide items covered:** Skip link

---

## Focus ring

`id: focus-ring` · level: primitive · source: Tangerine

The 3px keyboard focus outline, drawn inside controls (outside for ticks and switches).

### Why

Keyboard users must always see where they are (Von Restorff accessibility, Practical UI F10). ORCA darkens Vanilla's light-theme focus blue so the ring holds 3:1 on every ground.

### When to use

- Automatically on `:focus-visible` for every interactive element. Use `.orca-focus-ring` only for custom widgets that manage focus themselves.

### When not to use

- `outline: none` without a replacement. Never remove it.

### How to use

- Token: `--orca-focus`, width `--orca-focus-width` (3px), offset inside (−3px).
- Filled buttons switch to `--orca-focus-on-fill` or a double ring so it stays visible.
- Custom widget: add `.orca-focus-ring` (inside) or `.orca-focus-ring--outside` while it has focus.

### Accessibility

- Shown for keyboard focus only (`:focus-visible`), never hidden for mouse focus inside text fields.

#### Example: Ring shown

```django
<div class="orca-row orca-row--16">
  <button class="orca-button orca-focus-ring" type="button">Focused button</button>
  <span class="orca-focus-ring--outside orca-focus-ring" style="display: inline-block; width: 1rem; height: 1rem; border: var(--orca-border-width) solid var(--orca-border-strong)"></span>
</div>
```

**Classes:** `.orca-focus-ring`, `.orca-focus-ring--outside`

**Tokens:** `--orca-focus`, `--orca-focus-width`, `--orca-focus-on-fill`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI F10: Specify every interaction state; Practical UI C01: Check contrast for meaningful content

**ORCA guide items covered:** Focus ring

---

## Accordion chevron

`id: chevron` · level: primitive · source: Tangerine

A chevron that points down when its section is open and sideways when closed.

### Why

The rotating chevron is the familiar cue for 'this expands' (Jakob's law, Practical UI F06), and its motion confirms the change.

### When to use

- Disclosure and accordion triggers, collapsible sidebar groups, tree nodes.

### How to use

- Inside a `<summary>` or a button with `aria-expanded`: `<span class="orca-chevron">{% icon "chevron-down" %}</span>`. It rotates automatically when closed.
- Put it at the start of the row (left), in the same place on every row.

### Accessibility

- `<details>`/`<summary>` or `aria-expanded` announces the state; the chevron is decorative.

#### Example: Disclosure

```django
<details class="orca-stack" open>
  <summary class="orca-with-icon" style="cursor: pointer; list-style: none"><span class="orca-chevron">{% icon "chevron-down" %}</span>Advanced settings</summary>
  <p class="orca-p" style="margin-inline-start: var(--orca-space-24)">Frame rate, codec and bitrate.</p>
</details>
```

**Classes:** `.orca-chevron`

**Tokens:** `--orca-duration-fast`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI F06: Prefer established patterns

**ORCA guide items covered:** Accordion chevron

---

## Step marker

`id: step-marker` · level: primitive · source: Tangerine

A round marker for one step of a process: to do, current, done or error.

### Why

Showing where people are in a sequence motivates completion (goal-gradient effect, Peak–end rule) and splits long tasks (Hick's law).

### When to use

- Steps of a multi-step form or setup, timelines of a process.

### How to use

- `<span class="orca-step-marker orca-step-marker--done"></span>` · `--current` · default (to do) · `--error`.
- Always next to the step's name, and the current step has `aria-current="step"` on its item.

### Accessibility

- The state must also be in text for screen readers: 'Step 2 of 4, current'.

#### Example: Markers

```django
<ol class="orca-stack" style="list-style: none; padding: 0; margin: 0">
  <li class="orca-with-icon"><span class="orca-step-marker orca-step-marker--done"></span>Upload video<span class="orca-sr-only">, done</span></li>
  <li class="orca-with-icon" aria-current="step"><span class="orca-step-marker orca-step-marker--current"></span><strong>Choose a thumbnail</strong><span class="orca-sr-only">, current step</span></li>
  <li class="orca-with-icon"><span class="orca-step-marker orca-step-marker--error"></span>Add captions<span class="orca-sr-only">, has errors</span></li>
  <li class="orca-with-icon"><span class="orca-step-marker"></span>Publish</li>
</ol>
```

**Classes:** `.orca-step-marker`, `.orca-step-marker--current`, `.orca-step-marker--done`, `.orca-step-marker--error`

**Tokens:** `--orca-accent`, `--orca-border-strong`, `--orca-negative`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Step marker

---

## Carousel dot

`id: carousel-dot` · level: primitive · source: ORCA

A position marker and button for one slide of a carousel or gallery.

### Why

Dots show how many items there are and which is shown (Practical UI S06: show that more exists). The current dot changes shape, not only colour (C03), and the target is a full 29px/44px button (Fitts's law).

### When to use

- Carousels and image galleries with fewer than about 8 items.

### When not to use

- Many items: show a count ('3 of 24') and thumbnails instead.

### How to use

- `<button class="orca-carousel-dot" type="button" aria-label="Show image 2 of 5" aria-current="true"></button>`; one per slide in a group with `aria-label`.

#### Example: Dots

```django
<div class="orca-row" role="group" aria-label="Choose image" style="gap: 0">
  <button class="orca-carousel-dot" type="button" aria-label="Show image 1 of 4"></button>
  <button class="orca-carousel-dot" type="button" aria-label="Show image 2 of 4" aria-current="true"></button>
  <button class="orca-carousel-dot" type="button" aria-label="Show image 3 of 4"></button>
  <button class="orca-carousel-dot" type="button" aria-label="Show image 4 of 4"></button>
</div>
```

**Classes:** `.orca-carousel-dot`

**Tokens:** `--orca-text`, `--orca-border-strong`

**Principles applied:** Practical UI S06: Make essential content visible or discoverable; Practical UI C03: Communicate meaning beyond colour; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Carousel dot

---

## Pagination gap (ellipsis)

`id: pagination-gap` · level: primitive · source: Tangerine

The ellipsis between page numbers that are not shown.

### Why

It tells people pages exist between the shown numbers without listing them all (Hick's law; S06).

### When to use

- Pagination with more than 7 pages.

### How to use

- `<span class="orca-page-gap" aria-hidden="true">…</span>` between page links. Not focusable.

#### Example: Gap

```django
<div class="orca-row"><a class="orca-button" href="#">1</a><span class="orca-page-gap" aria-hidden="true">…</span><a class="orca-button" href="#" aria-current="page" style="background: var(--orca-bg-active)">7</a><span class="orca-page-gap" aria-hidden="true">…</span><a class="orca-button" href="#">24</a></div>
```

**Classes:** `.orca-page-gap`

**Tokens:** `--orca-text-muted`, `--orca-control-md`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI S06: Make essential content visible or discoverable

**ORCA guide items covered:** Pagination gap (ellipsis)

---

## Dialog backdrop

`id: dialog-backdrop` · level: primitive · source: Tangerine

The dimmed layer behind a modal dialog, plus the dialog surface itself.

### Why

Dimming the page focuses attention on the decision (Von Restorff) and signals that the page is paused; the deliberate pause is useful friction before an irreversible action (Doherty: friction).

### When to use

- Modal confirmations and short focused tasks that must finish before going back.

### When not to use

- Information people need to compare with the page behind: use a drawer or inline panel.

### How to use

- Use the native element: `<dialog class="orca-dialog" aria-labelledby=…>` opened with `showModal()`; `::backdrop` is styled.
- Non-native overlays: `<div class="orca-backdrop"></div>` (`--contained` to stay in a parent).
- Body padding 24px; actions at the bottom; Escape and a Cancel button close it.

### Accessibility

- `showModal()` traps focus and restores it on close; return focus to the opener.

#### Example: Dialog

```django
<button class="orca-button" type="button" onclick="this.nextElementSibling.showModal()">Open dialog</button>
<dialog class="orca-dialog" aria-labelledby="dlg-demo-title">
  <form method="dialog" style="padding: var(--orca-space-24)" class="orca-stack">
    <h2 class="orca-dialog-title" id="dlg-demo-title">Delete Harbour at dusk?</h2>
    <p class="orca-p">It is removed from every album and its share links stop working.</p>
    <div class="orca-row"><button class="orca-button orca-button--danger" type="submit" value="delete">Delete image</button><button class="orca-button" type="submit" value="cancel" autofocus>Cancel</button></div>
  </form>
</dialog>
```

**Classes:** `.orca-dialog`, `.orca-backdrop`

**Tokens:** `--orca-bg-overlay`, `--orca-bg-elevated`, `--orca-shadow-dragged`, `--orca-layer-dialog`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI B13: Scale friction to the consequence

**ORCA guide items covered:** Dialog backdrop

---

## Drawer backdrop

`id: drawer-backdrop` · level: primitive · source: Tangerine

A side drawer on the inline end (right) with its scrim: where page filters live, opened from the page actions.

### Why

Filters change what a page shows without taking the person away from it. A drawer keeps the results in view behind the scrim, keeps the page head free of a row of controls (Hick's law, Practical UI S04: reveal secondary controls when needed), and always opens from the same place, so people know where to look (Jakob's law). The scrim is a large, familiar target to dismiss it (Fitts's law).

### When to use

- Page filters of a list, table, gallery or report: they always go in a right drawer.
- Secondary detail or settings that people compare with the page behind.

### When not to use

- A row of filter controls above the results: put them in the drawer and show the applied ones as tags.
- A decision that must finish before going back: use a dialog.
- Navigation on wide screens: use the sidebar; a navigation drawer is for phones only, on the inline start.

### How to use

- Open button in the page actions: `<button class="orca-button" type="button" data-orca-open="filters" aria-haspopup="dialog" aria-expanded="false">{% icon "filter" %}Filters</button>`. When filters are applied, add their number: `<span class="orca-count orca-count--accent">2</span>` and say it in `aria-label` ('Filters, 2 applied').
- The drawer is a native dialog: `<dialog class="orca-drawer" id="filters" aria-labelledby=…><form method="get">` with `.orca-drawer__head` (dialog title and a Close icon button with `data-orca-close`), `.orca-drawer__body` (one `<fieldset>` per filter) and `.orca-drawer__foot` (primary 'Show results' that submits, then 'Clear filters').
- `orca.js` opens it as a modal (`showModal()`), closes it on Close, Escape or a press on the backdrop, and returns focus to the button.
- Order filters by use; a search field that narrows the list goes first. Above the results, show each applied filter as a removable tag and a 'Clear filters' link button.
- Without a dialog (custom overlays): `<div class="orca-scrim" data-close></div>` before the panel; `--contained` keeps it inside a positioned parent.

### Accessibility

- `showModal()` traps focus and makes the page behind inert; the opener's `aria-expanded` follows the drawer.
- The drawer's title names it ('Filters'); every control inside keeps its visible label.

#### Example: Page filters in a right drawer

```django
<div class="orca-page-head">
  <div class="orca-page-head__text"><h1 class="orca-page-title">Videos</h1><p class="orca-page-subtitle">128 videos in the library.</p></div>
  <div class="orca-page-actions">
    <button class="orca-button" type="button" data-orca-open="drawer-demo" aria-haspopup="dialog" aria-expanded="false" aria-label="Filters, 2 applied">{% icon "filter" %}Filters<span class="orca-count orca-count--accent" aria-hidden="true">2</span></button>
    <button class="orca-button orca-button--primary" type="button">{% icon "plus" %}Add video</button>
  </div>
</div>
<div class="orca-row" style="margin-top: var(--orca-space-16)">
  <span class="orca-tag"><span class="orca-tag__text">Published</span><button class="orca-tag__remove" type="button" aria-label="Remove Published">{% icon "close" %}</button></span>
  <span class="orca-tag"><span class="orca-tag__text">Longer than 10 min</span><button class="orca-tag__remove" type="button" aria-label="Remove Longer than 10 min">{% icon "close" %}</button></span>
  <button class="orca-button orca-button--link" type="button">Clear filters</button>
</div>
<dialog class="orca-drawer" id="drawer-demo" aria-labelledby="drawer-demo-title">
  <form method="dialog">
    <div class="orca-drawer__head">
      <h2 class="orca-dialog-title" id="drawer-demo-title">Filters</h2>
      <button class="orca-icon-button" type="button" data-orca-close aria-label="Close filters">{% icon "close" %}</button>
    </div>
    <div class="orca-drawer__body">
      <div><label class="orca-label" for="drawer-demo-q">Title contains</label>
        <input class="orca-input" type="search" id="drawer-demo-q" name="q"></div>
      <fieldset><legend class="orca-label">Status</legend>
        <label class="orca-check"><input type="checkbox" name="status" value="published" checked><span class="orca-check__box"></span>Published</label>
        <label class="orca-check"><input type="checkbox" name="status" value="draft"><span class="orca-check__box"></span>Draft</label>
      </fieldset>
      <fieldset><legend class="orca-label">Length</legend>
        <label class="orca-radio"><input type="radio" name="length" value="any"><span class="orca-radio__dot"></span>Any length</label>
        <label class="orca-radio"><input type="radio" name="length" value="long" checked><span class="orca-radio__dot"></span>Longer than 10 min</label>
      </fieldset>
    </div>
    <div class="orca-drawer__foot">
      <button class="orca-button orca-button--primary" type="submit">Show 14 videos</button>
      <button class="orca-button" type="reset">Clear filters</button>
    </div>
  </form>
</dialog>
```

**Classes:** `.orca-drawer`, `.orca-drawer__head`, `.orca-drawer__body`, `.orca-drawer__foot`, `.orca-scrim`, `.orca-scrim--contained`

**Tokens:** `--orca-bg-overlay`, `--orca-bg-elevated`, `--orca-shadow-dragged`, `--orca-layer-drawer`, `--orca-duration-brisk`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Jakob's law: work the way products people already know work; Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI S04: Reveal secondary information when needed

**Related:** `page-title`, `tag`, `dialog-backdrop`

**ORCA guide items covered:** Drawer backdrop

---
