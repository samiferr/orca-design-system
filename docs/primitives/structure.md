# Structure marks

Marks that organise and connect (rules, separators, focus, markers, backdrops), plus the accessibility helpers every page needs.

## Divider

`id: divider` · level: primitive · source: Tangerine

A horizontal or vertical rule: default, muted, medium and large spacing, labelled, highlight and brand.

### General description

A divider is a thin line that separates groups of content, either across a page or between side-by-side items.

#### Use cases

- Separating groups in menus and panels.
- Splitting groups of toolbar buttons.
- Showing an 'or' between alternative options.

#### When not to use it

- Putting lines between every item; use spacing or row separators.
- Faking a heading with a line; use a real section title.

#### Best practices

- Use dividers sparingly so they keep meaning.
- Try spacing first.
- Hide purely decorative lines from screen readers.
- Mark real separators with the correct role.

### When to use

- Between menu groups, panel sections and (vertical) toolbar groups.
- Labelled: 'or' between alternative sign-in methods.

### When not to use

- Between every item: use spacing or row separators.
- As a fake heading: use a section title.

### How to use

- `<hr class="orca-divider">` (16px above and below). `--md` 24px, `--lg` 48px, `--flush` 0, `--muted` lighter line.
- Vertical: `<span class="orca-divider orca-divider--vertical" role="separator" aria-orientation="vertical"></span>` inside a flex row.
- Labelled: `<div class="orca-divider orca-divider--labeled" role="separator">or</div>`.
- Emphasis: `--highlight` (3px text colour) or `--brand` (3px brand).

#### Example: Dividers

```django
<div style="max-width: 24rem">
  <p class="orca-p">Above</p>
  <hr class="orca-divider">
  <p class="orca-p">Below</p>
  <div class="orca-divider orca-divider--labeled" role="separator">or</div>
  <div class="orca-row">
    <span>Left</span>
    <span class="orca-divider orca-divider--vertical" role="separator" aria-orientation="vertical"></span>
    <span>Right</span>
  </div>
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

### General description

A chevron separator is a small arrow-like mark placed between items in a path, showing that one sits inside the other.

#### Use cases

- Separating levels in breadcrumbs.
- Showing file or folder paths.
- Showing nested categories.

#### When not to use it

- Using it as a button or toggle; use a real control.
- Separating unrelated items; use spacing or a divider.

#### Best practices

- Keep it small and muted.
- Hide it from screen readers, since the list carries the meaning.
- Flip it in right-to-left languages.
- Use the same mark everywhere.

### When to use

- Breadcrumbs, path displays (Library › Album › Image).

### How to use

- `<span class="orca-sep" aria-hidden="true">{% icon "chevron-right" %}</span>` between items.
- In breadcrumbs the list structure carries the meaning; the separator is hidden from screen readers.

#### Example: Path

```django
<nav aria-label="Breadcrumb" class="orca-small">
  <a class="orca-link orca-link--plain" href="#">Library</a>
  <span class="orca-sep" aria-hidden="true">
    {% icon "chevron-right" %}
  </span>
  <a class="orca-link orca-link--plain" href="#">Summer 2026</a>
  <span class="orca-sep" aria-hidden="true">
    {% icon "chevron-right" %}
  </span>
  <span aria-current="page">Harbour at dusk</span>
</nav>
```

**Classes:** `.orca-sep`

**Tokens:** `--orca-text-muted`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Chevron separator

---

## Screen-reader-only text

`id: sr-only` · level: primitive · source: Tangerine

Text that assistive technology reads but the screen does not show.

### General description

Screen-reader-only text is content hidden from the screen but still read aloud by assistive technology. It supplies meaning that is otherwise only visual.

#### Use cases

- Naming icon-only buttons and links.
- Adding context such as 'opens in a new tab'.
- Explaining changes shown only by color or arrows.

#### When not to use it

- Hiding text that sighted keyboard users also need; show it.
- Repeating text that is already announced.

#### Best practices

- Keep hidden text short and clear.
- Write it so it reads naturally in context.
- Show it again when it gets keyboard focus if it is actionable.
- Test with a screen reader.

### When to use

- Completing a visual cue: '(opens in a new tab)', 'compared with last week', or the name of an icon-only control.

### When not to use

- Hiding text sighted keyboard users also need.
- Repeating text that is already read.

### How to use

- `<span class="orca-sr-only">compared with last week</span>`.
- `.orca-sr-only-focusable` shows the element when it gets focus.

#### Example: Hidden context

```django
<span class="orca-delta orca-delta--up">
  {% icon "arrow-up" size="xs" %}
  +8%
  <span class="orca-sr-only"> compared with last week</span>
</span>
```

**Classes:** `.orca-sr-only`, `.orca-sr-only-focusable`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Practical UI F01: Design for a diverse audience

**ORCA guide items covered:** Screen-reader-only text

---

## Skip link

`id: skip-link` · level: primitive · source: Tangerine

The first focusable link on a page; it jumps past the navigation to the main content.

### General description

A skip link is a link at the very top of a page that lets keyboard and screen reader users jump past repeated navigation to the main content.

#### Use cases

- Letting keyboard users bypass long menus.
- Helping screen reader users reach content quickly.
- Meeting basic accessibility requirements on every page.

#### When not to use it

- Hiding it so it never appears when focused.
- Leaving it out on pages with navigation before the content.

#### Best practices

- Make it the first focusable element on the page.
- Show it clearly when it gets focus.
- Point it to the main content area.
- Use plain wording such as 'Skip to main content'.

### When to use

- Every page with navigation before the content.

### How to use

- First element in `<body>`: `<a class="orca-skip-link" href="#main">Skip to main content</a>` and `<main id="main" tabindex="-1">`.
- Hidden until focused, then shown top-left above everything.

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

### General description

A focus ring is the visible outline around the element that currently has keyboard focus, showing people where they are on the page.

#### Use cases

- Showing the active control during keyboard navigation.
- Marking custom widgets that handle their own focus.
- Helping low-vision users follow the cursor.

#### When not to use it

- Removing the outline without a replacement.
- Hiding it for keyboard users because it looks plain.

#### Best practices

- Show it only for keyboard focus where possible.
- Give it at least 3:1 contrast on every background.
- Keep it thick enough to see.
- Make sure it stays visible on filled controls.

### When to use

- Automatic on `:focus-visible` for every interactive element. Add `.orca-focus-ring` only to custom widgets that manage their own focus.

### When not to use

- `outline: none` without a replacement; never remove the ring.

### How to use

- Token: `--orca-focus`, width `--orca-focus-width` (3px), offset inside (−3px).
- Filled buttons switch to `--orca-focus-on-fill` or a double ring so it stays visible.
- Custom widget: add `.orca-focus-ring` (inside) or `.orca-focus-ring--outside` while it has focus.

### Accessibility

- Shown for keyboard focus only (`:focus-visible`); text fields still show it on mouse focus.

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

### General description

A chevron is a small arrow that points down when a section is open and sideways when closed, hinting that the section can expand or collapse.

#### Use cases

- Showing expandable accordion and disclosure sections.
- Showing opened or closed tree and menu groups.
- Hinting that a row reveals more.

#### When not to use it

- Using it as the only sign that something is clickable; add a label.
- Using it for navigation to a new page; use an arrow or link.

#### Best practices

- Rotate it when the state changes.
- Place it in the same spot on every row.
- Expose the open state to screen readers separately.
- Animate the turn briefly.

### When to use

- Disclosure and accordion triggers, collapsible sidebar groups, tree nodes.

### How to use

- Inside a `<summary>` or a button with `aria-expanded`: `<span class="orca-chevron">{% icon "chevron-down" %}</span>`. It rotates automatically when closed.
- Accordions and trees: at the start of every row. Navigation trees: small, at the row end (see the nav tree).

### Accessibility

- `<details>`/`<summary>` or `aria-expanded` announces the state; the chevron is decorative.

#### Example: Disclosure

```django
<details class="orca-stack" open>
  <summary class="orca-with-icon" style="cursor: pointer; list-style: none">
    <span class="orca-chevron">
      {% icon "chevron-down" %}
    </span>
    Advanced settings
  </summary>
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

### General description

A step marker is a small mark showing one step of a process, with its state such as to do, current, done or error.

#### Use cases

- Showing progress through a multi-step form.
- Listing stages in setup or checkout.
- Showing steps on a timeline.

#### When not to use it

- Using it for a single-page form; it adds noise.
- Showing state by color alone; add text or an icon.

#### Best practices

- Place it beside the step name.
- Say the state in text for screen readers.
- Mark the current step clearly.
- Keep the number of steps small.

### When to use

- Steps of a multi-step form or setup, timelines of a process.

### How to use

- `<span class="orca-step-marker orca-step-marker--done"></span>` · `--current` · default (to do) · `--error`.
- Always beside the step's name; the current step's item has `aria-current="step"`.

### Accessibility

- The state must also be in text for screen readers: 'Step 2 of 4, current'.

#### Example: Markers

```django
<ol class="orca-stack" style="list-style: none; padding: 0; margin: 0">
  <li class="orca-with-icon"><span class="orca-step-marker orca-step-marker--done"></span>Upload video<span class="orca-sr-only">, done</span></li>
  <li class="orca-with-icon" aria-current="step">
    <span class="orca-step-marker orca-step-marker--current"></span>
    <strong>Choose a thumbnail</strong>
    <span class="orca-sr-only">, current step</span>
  </li>
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

### General description

A carousel dot is a small clickable marker for one slide in a carousel or gallery. It shows how many slides there are and which one is showing.

#### Use cases

- Jumping to a specific slide.
- Showing the current position in a gallery.
- Letting people browse a short set of images.

#### When not to use it

- Galleries with many items; show a count and thumbnails instead.
- Making dots tiny to tap; keep a large target.

#### Best practices

- Give each dot a label such as 'Show image 2 of 5'.
- Mark the current dot by shape, not only color.
- Keep dots to about eight or fewer.
- Make the tap target at least 44px.

### When to use

- Carousels and image galleries with fewer than about 8 items.

### When not to use

- Many items: show a count ('3 of 24') and thumbnails instead.

### How to use

- `<button class="orca-carousel-dot" type="button" aria-label="Show image 2 of 5" aria-current="true"></button>`; one per slide, grouped with an `aria-label`.

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

### General description

A pagination gap is an ellipsis between page numbers showing that some pages are skipped, so long lists of pages stay short.

#### Use cases

- Shortening page lists with many pages.
- Keeping first, last and nearby pages visible.
- Saving space in narrow layouts.

#### When not to use it

- Using it when there are only a few pages; show them all.
- Making it clickable; use a real page link.

#### Best practices

- Show the first, last and current pages around it.
- Make it non-interactive.
- Hide it from screen readers.
- Keep it visually quiet.

### When to use

- Pagination with more than 7 pages.

### How to use

- `<span class="orca-page-gap" aria-hidden="true">…</span>` between page links. Not focusable.

#### Example: Gap

```django
<div class="orca-row">
  <a class="orca-button" href="#">1</a>
  <span class="orca-page-gap" aria-hidden="true">…</span>
  <a class="orca-button" href="#" aria-current="page" style="background: var(--orca-bg-active)">7</a>
  <span class="orca-page-gap" aria-hidden="true">…</span>
  <a class="orca-button" href="#">24</a>
</div>
```

**Classes:** `.orca-page-gap`

**Tokens:** `--orca-text-muted`, `--orca-control-md`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI S06: Make essential content visible or discoverable

**ORCA guide items covered:** Pagination gap (ellipsis)

---

## Dialog backdrop

`id: dialog-backdrop` · level: primitive · source: Tangerine

The dimmed layer behind a modal dialog, plus the dialog surface itself.

### General description

A dialog backdrop is the dimmed layer behind a modal dialog. It focuses attention on the dialog and blocks the page behind it.

#### Use cases

- Confirming a risky action such as delete.
- Short tasks that must finish before continuing.
- Asking for a decision that cannot wait.

#### When not to use it

- Content people need to compare with the page; use a side panel or inline section.
- Long forms; use a full page instead.

#### Best practices

- Trap focus inside and return it on close.
- Let Escape and a Cancel button close it.
- Put actions at the bottom with the main one clear.
- Dim enough to separate, but not hide the page.

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
    <div class="orca-row">
      <button class="orca-button orca-button--danger" type="submit" value="delete">Delete image</button>
      <button class="orca-button" type="submit" value="cancel" autofocus>Cancel</button>
    </div>
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

The scrim behind a side drawer; pressing it closes the drawer.

### General description

A drawer backdrop is the dimmed layer behind a panel that slides in from the side. Clicking it usually closes the drawer.

#### Use cases

- Showing filters or settings in a side panel.
- Opening navigation on phones.
- Giving a large target to dismiss the drawer.

#### When not to use it

- Panels people must use alongside the page; keep them docked instead.
- Blocking the page without a clear way out.

#### Best practices

- Let clicking the backdrop and Escape close the drawer.
- Offer a visible Close button too.
- Keep focus inside while it is open.
- Return focus to the opener when closed.

### When to use

- Behind the filter drawer (page filters always open in a right drawer) and phone navigation drawers.

### How to use

- With the `drawer` pattern (`<dialog class="orca-drawer" data-orca-light-dismiss>`), the native `::backdrop` is this scrim: nothing more to write.
- Non-native overlays: `<div class="orca-scrim" data-close></div>` before the drawer; `--contained` keeps it inside a positioned parent.
- Clicking the scrim must do what the drawer's Close button does, and so must Escape.

#### Example: Contained scrim

```django
<div style="position: relative; height: 8rem; overflow: hidden; border: var(--orca-border-width) solid var(--orca-border)">
  <p class="orca-p" style="padding: var(--orca-space-16)">Page content</p>
  <div class="orca-scrim orca-scrim--contained"></div>
  <aside class="orca-elevation-2" style="position: absolute; top: 0; bottom: 0; right: 0; width: 60%; padding: var(--orca-space-16); z-index: calc(var(--orca-layer-drawer) + 1)">
    <p class="orca-dialog-title">Filters</p>
  </aside>
</div>
```

**Classes:** `.orca-scrim`, `.orca-scrim--contained`

**Tokens:** `--orca-bg-overlay`, `--orca-layer-drawer`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Drawer backdrop

---
