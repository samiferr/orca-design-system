# Base styles

Tokens every other element is built from: colour, type, space, shape, elevation, layers, size and motion. Use these names, never raw values. Only brand tokens may be changed by a project.

## Colour palette

`id: color-palette` · level: primitive · source: ORCA

Raw colours: a 13-step gray scale and eleven hues with nine numbered steps each.

### When to use

- Charts, zones, calendars and illustrations that need several distinguishable categories.
- Defining a new semantic token inside ORCA itself.

### When not to use

- Text, controls, grounds and status: use semantic tokens (`semantic-colors`) instead.
- Telling two series apart by hue alone: change lightness or add a shape, label or pattern.

### How to use

- Gray: `--orca-gray-0` (white) to `--orca-gray-1000` (black), ORCA's values.
- Hues: `--orca-{red|orange|amber|yellow|green|teal|cyan|blue|indigo|purple|pink}-{100..900}`; 100 is lightest.
- For data series prefer `--orca-chart-1`…`--orca-chart-8`, which already pick contrasting steps per theme.
- Text on a hue step: steps 100–400 take `--orca-text` in light themes; 600–900 take white.

#### Example: Gray and one hue

```django
<div class="orca-row">
  <span class="orca-swatch" style="--orca-swatch: var(--orca-gray-200)"></span>
  <span class="orca-swatch" style="--orca-swatch: var(--orca-gray-500)"></span>
  <span class="orca-swatch" style="--orca-swatch: var(--orca-gray-900)"></span>
  <span class="orca-swatch" style="--orca-swatch: var(--orca-teal-200)"></span>
  <span class="orca-swatch" style="--orca-swatch: var(--orca-teal-500)"></span>
  <span class="orca-swatch" style="--orca-swatch: var(--orca-teal-800)"></span>
</div>
```

**Tokens:** `--orca-gray-500`, `--orca-blue-600`, `--orca-chart-1`, `--orca-heat-3`

**Principles applied:** Practical UI C18: Name raw colours separately from their uses; Practical UI C03: Communicate meaning beyond colour; Aesthetic–usability effect: consistent, careful visuals earn trust

**Related:** `semantic-colors`, `swatch`

**ORCA guide items covered:** Colour palette; Neutral scale (gray); Hue scales (eleven hues, numbered steps)

---

## Semantic colour tokens

`id: semantic-colors` · level: primitive · source: Tangerine

Colours named by their job: text, grounds, lines, interaction, status, actions, planning, data.

### When to use

- Every colour in every element and page.

### When not to use

- Choosing a token for how it looks rather than what it is for (a muted heading is still `--orca-text`).
- Using `--orca-border` (decorative, 1.6:1) on a control: controls need `--orca-border-strong` (3:1).

### How to use

- Text: `text` (body, labels, headings), `text-muted` (help, meta), `text-inactive` (unselected nav).
- Grounds: `bg` page, `bg-alt` set-apart region, `bg-input` fields, `bg-hover`, `bg-active` (pressed, selected), `bg-elevated` floating.
- Lines: `border` decorative, `border-strong` controls, `border-weak` row separators.
- Status families `info`, `positive`, `caution`, `negative`, `neutral`: the bare name for marks and text, `-bg` for tints, `-fill` for solid badges.
- Actions: `primary*` (main action, green), `danger*` (confirmed destruction), `brand-strong*` (brand fill).
- Pair every status colour with an icon and a word.

### Accessibility

- `text` and `text-muted` hold 4.5:1 on `bg`, `bg-alt` and `bg-input` in every theme.
- Known exception kept from Vanilla: `caution` as text is 3.0:1 in light; never set caution text alone.

#### Example: Roles in use

```django
<div style="background: var(--orca-bg-alt); padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border)">
  <p class="orca-p">Body text uses <code class="orca-code">--orca-text</code>.</p>
  <p class="orca-p orca-muted">Secondary text uses <code class="orca-code">--orca-text-muted</code>.</p>
  <span class="orca-badge orca-badge--subtle orca-badge--positive">
    {% icon "success" %}
    Approved
  </span>
</div>
```

**Tokens:** `--orca-text`, `--orca-text-muted`, `--orca-bg`, `--orca-bg-alt`, `--orca-border-strong`, `--orca-positive`, `--orca-negative-bg`, `--orca-primary`

**Principles applied:** Practical UI C09: Give each palette token a role; Practical UI C18: Name raw colours separately from their uses; Practical UI C01: Check contrast for meaningful content; Practical UI C04: Reserve status colours for their meanings

**Related:** `color-palette`, `themes`

**ORCA guide items covered:** Semantic colour tokens

---

## Brand colour and surfaces

`id: brand-color` · level: primitive · source: ORCA

The one brand colour, the fills derived from it, and the page surfaces it sits on.

### When to use

- The one brand moment on a page: the top bar, the brand button, the logo mark, a highlight rule.
- Re-branding a deployment: set `ORCA['BRAND']['color']` and nothing else.

### When not to use

- More than one brand-filled element per screen (Von Restorff: emphasis loses power when repeated).
- Status meaning: brand is never success, warning or error.
- Links and checked controls: those use the accent colour.

### How to use

- `--orca-brand`: the colour as given, for decorative marks and 3px bars (needs only 3:1).
- `--orca-brand-strong`: fills that carry text; darkened by ORCA until `--orca-brand-on` reads at 4.5:1.
- `--orca-brand-strong-hover` / `-active`: hover and pressed fills, derived.
- Surfaces: page `--orca-bg`, set-apart regions `--orca-bg-alt`, floating `--orca-bg-elevated`.
- Set it in settings; ORCA reports any adjustment it made as a system-check warning (`orca.W001`).

### Accessibility

- Never rely on brand colour alone to show state; selection uses the accent and a shape.

#### Example: Brand moments

```django
<div class="orca-stack">
  <span class="orca-row">
    {% orca_logo href="" %}
  </span>
  <hr class="orca-divider orca-divider--brand">
  <button class="orca-button orca-button--brand" type="button">Start free trial</button>
</div>
```

**Tokens:** `--orca-brand`, `--orca-brand-strong`, `--orca-brand-strong-hover`, `--orca-brand-on`, `--orca-bg`, `--orca-bg-alt`, `--orca-bg-elevated`

**Principles applied:** Practical UI C07: Prefer one purposeful action colour; Practical UI C08: Choose and adapt the brand colour deliberately; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Tesler's law: move unavoidable complexity from the user to the system

**Related:** `accent-color`, `button`, `logo`

**ORCA guide items covered:** Brand colour and surfaces

---

## Accent colour

`id: accent-color` · level: primitive · source: ORCA

The single interactive colour: links, checked ticks, radios, switches, progress, selected days.

### When to use

- Text links, the checked state of ticks, radios and switches, progress fills, selected calendar days, accent outlines and accent badges.

### When not to use

- Static headings or decorative icons: action colour on non-interactive things misleads (C07).
- Large fills behind long text.

### How to use

- Use `var(--orca-accent)`; hover is `var(--orca-accent-hover)`.
- Brand token: `ORCA['BRAND']['accent']` (light and paper) and optional `accent_dark`; ORCA darkens or lightens it to 4.5:1.
- Text on an accent fill is `var(--orca-bg)`.

### Accessibility

- Holds 4.5:1 on `bg` and `bg-alt` in every theme, so it can be used for link text.

#### Example: Accent in use

```django
<p class="orca-p">Read the <a class="orca-link" href="#">retention policy</a>.</p>
<label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Email me a daily report</label>
```

**Tokens:** `--orca-accent`, `--orca-accent-hover`

**Principles applied:** Practical UI C07: Prefer one purposeful action colour; Jakob's law: work the way products people already know work

**Related:** `text-link`, `checkbox`

**ORCA guide items covered:** Accent colour

---

## Themes

`id: themes` · level: primitive · source: Tangerine

Light, dark and paper share every token name. ORCA has one appearance, named ORCA.

### When to use

- Always: every page supports all three themes for free.
- Set `ORCA['THEME']` to `light`, `dark` or `paper` to force one; `auto` (default) follows the OS and the user's stored choice.

### When not to use

- Theme-specific CSS in your own code: if something needs it, the token is missing; report it.
- Pure black grounds: dark uses #262626 and #202020.

### How to use

- Put `{% orca_html_attrs %}` on `<html>` and `{% orca_head %}` in `<head>`.
- A theme toggle is a button with `data-orca-theme-toggle`; it cycles light → dark → paper and remembers the choice.
- Appearance: ORCA only (square corners, 1.5px borders, filled fields with a bottom border, inside focus ring).

### Accessibility

- Contrast promises hold in every theme; dark lifts floating surfaces one step so elevation shows without shadows.

#### Example: Theme toggle

```django
<button class="orca-icon-button orca-icon-button--outlined" type="button" data-orca-theme-toggle aria-label="Change theme">
  {% icon "sun" %}
</button>
```

**Tokens:** `--orca-bg`, `--orca-text`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Practical UI C11: Build dark palettes independently; Practical UI C12: Use elevation consistently

**Related:** `toggle-button`

**ORCA guide items covered:** Themes (light, dark, paper); Appearances (Lumen, Tangerine)

---

## Fonts and type styles

`id: typography` · level: primitive · source: Tangerine

Ubuntu Sans (variable) for everything, JetBrains Mono for code, on a fixed type scale.

### When to use

- Every piece of text. Pick the style by role: heading, title, body, detail, label, code.

### When not to use

- New sizes or weights in page CSS.
- Weights other than 400 and 550 for interface text (thin 180/275 only for the large h2/h4 styles).
- All caps for anything longer than a short label (W07).

### How to use

- Heading: `--orca-type-h1`…`h6`, `--orca-type-page-title`, `--orca-type-display`.
- Title: `--orca-type-title` (panel and card titles, 18/24 550).
- Body: `--orca-type-body` (16/24) and `--orca-type-body-strong` (550). Bold is 550, not 700.
- Detail: `--orca-type-detail` (14/20) for help, meta and timestamps; `--orca-type-label` (12/16 550) for table headers, badges, kickers and stat card labels.
- Figure: `--orca-type-figure` (28/36 550) for the number of a stat card.
- Code: `--orca-type-code` with `--orca-font-mono` (JetBrains Mono, self-hosted; it tells 0/O and 1/l/I apart). Code blocks are coloured with the `--orca-code-*` tokens.
- Numbers in tables and stats get `font-variant-numeric: tabular-nums` (`.orca-num`).
- Use as `font: var(--orca-type-body)`. Brand tokens `font_sans` / `font_mono` swap the families.

### Accessibility

- Sizes are in rem so they follow the user's font-size setting; the root grows to 18px above 1681px.
- Running text is capped at `--orca-measure` (70ch).

#### Example: The scale

```django
<div class="orca-stack">
  <p class="orca-h3">Heading 3 · 24/32 550</p>
  <p class="orca-panel-title">Title · 18/24 550</p>
  <p class="orca-p">Body · 16/24 400</p>
  <p class="orca-small orca-muted">Detail · 14/20 400</p>
  <p class="orca-card-kicker">Label · 12/16 550</p>
  <code class="orca-code">Code · JetBrains Mono</code>
</div>
```

**Tokens:** `--orca-type-h1`, `--orca-type-title`, `--orca-type-body`, `--orca-type-detail`, `--orca-type-label`, `--orca-type-code`, `--orca-font-sans`, `--orca-font-mono`

**Principles applied:** Practical UI T01: One legible sans serif family; Practical UI T04: Limit the working set of weights; Practical UI T05: Build sizes from a type scale; Practical UI T07: Comfortable line spacing; Practical UI T09: Limit reading measure; Aesthetic–usability effect: consistent, careful visuals earn trust

**Related:** `heading`, `paragraph`

**ORCA guide items covered:** Fonts; Type scale; Type styles (heading, title, body, detail); Monospace font

---

## Spacing scale

`id: spacing` · level: primitive · source: Tangerine

Eleven spacing steps on the 8px unit, named by their pixel value.

### When to use

- Every margin, padding and gap.

### When not to use

- Values off the scale (6px, 10px, 18px).
- The same small gap at every nesting level: it flattens grouping.

### How to use

- `--orca-space-4` menu rows · `-8` icon to label, related controls, label to field · `-12` field to help text · `-16` button and input side padding, card padding, between fields · `-24` between sections · `-32` between page regions · `-48` alert text inset.
- Work from the inside out: the innermost gap is smallest.
- Utilities: `.orca-stack` (column, 8px), `.orca-row` (wrapping row, 8px; `.orca-row--16`).

#### Example: Nested spacing

```django
<div style="padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border); display: grid; gap: var(--orca-space-24)">
  <div style="display: grid; gap: var(--orca-space-4)">
    <p class="orca-panel-title">Section one</p>
    <p class="orca-small orca-muted">8px and under inside a group</p>
  </div>
  <div style="display: grid; gap: var(--orca-space-4)">
    <p class="orca-panel-title">Section two</p>
    <p class="orca-small orca-muted">24px between groups</p>
  </div>
</div>
```

**Tokens:** `--orca-space-4`, `--orca-space-8`, `--orca-space-12`, `--orca-space-16`, `--orca-space-24`, `--orca-space-32`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI L08: Define a limited spacing scale; Practical UI L09: Set spacing by relationship; Practical UI L01: Group related information

**Related:** `divider`

**ORCA guide items covered:** Spacing scale (8 px)

---

## Borders

`id: borders` · level: primitive · source: Tangerine

Three line weights: 1px hairline, 1.5px outline, 3px emphasis bar.

### When to use

- Hairline: rules, table header line, row separators.
- 1.5px: outlines of buttons, cards, alerts, tick boxes; the field bottom border.
- 3px: the selected tab, an alert's side bar, the focus ring, a highlight rule.

### When not to use

- Borders that box every group (Practical UI L01): use space first.

### How to use

- Width tokens: `--orca-hairline`, `--orca-border-width`, `--orca-bar`.
- Colour tokens: `--orca-border` (decorative), `--orca-border-strong` (controls, 3:1), `--orca-border-weak` (rows).

#### Example: Three weights

```django
<div class="orca-stack">
  <hr class="orca-divider orca-divider--flush">
  <div style="height: 2rem; border: var(--orca-border-width) solid var(--orca-border-strong)"></div>
  <hr class="orca-divider orca-divider--highlight orca-divider--flush">
</div>
```

**Tokens:** `--orca-hairline`, `--orca-border-width`, `--orca-bar`, `--orca-border`, `--orca-border-strong`, `--orca-border-weak`

**Principles applied:** Practical UI R18: Keep control boundaries visible; Practical UI S02: Remove styles that compete without communicating

**Related:** `divider`

**ORCA guide items covered:** Borders

---

## Corner radii

`id: radii` · level: primitive · source: Tangerine

ORCA is square; only round marks and bar ends are rounded.

### When to use

- `--orca-radius-none` for every box: buttons, fields, cards, menus, dialogs, badges, tags.
- `--orca-radius-round` for radios, status dots, avatars, step markers, the switch handle.
- `--orca-radius-pill` for the switch track and count badges; `--orca-radius-bar` for progress tracks.

### When not to use

- Rounding a checkbox: the square box versus round radio is how people tell one-of-many from many (Practical UI R07).

### How to use

- Use the tokens even for 0 so a future rounding change is a token change, not a hunt.

#### Example: Shapes

```django
<div class="orca-row orca-row--16">
  <button class="orca-button" type="button">Square button</button>
  <span class="orca-avatar orca-avatar--s">AL</span>
  <span class="orca-dot orca-dot--positive"></span>
  <span class="orca-count">3</span>
</div>
```

**Tokens:** `--orca-radius-none`, `--orca-radius-round`, `--orca-radius-pill`, `--orca-radius-bar`

**Principles applied:** Aesthetic–usability effect: consistent, careful visuals earn trust; Practical UI R07: Keep recognisable control features

**ORCA guide items covered:** Corner radii (rounding)

---

## Shadows and elevation

`id: shadows` · level: primitive · source: Tangerine

Three shadows (card, elevated, dragged) and elevation utilities. Only floating things cast a shadow.

### When to use

- `shadow-card`: the hover lift of an interactive card.
- `shadow-elevated`: menus, dropdown lists, popovers, toasts, drawers.
- `shadow-dragged`: a dragged item, a dialog, a sidebar opened over content.

### When not to use

- Shadows on cards at rest, panels or page sections: use a border or `bg-alt`.

### How to use

- Utilities: `.orca-elevation-0` … `.orca-elevation-3` (2 and 3 also set `--orca-bg-elevated`).
- In dark themes elevation also comes from the lighter `--orca-bg-elevated` surface.

#### Example: Elevation levels

```django
<div class="orca-row orca-row--16">
  <div class="orca-elevation-1" style="padding: var(--orca-space-16)">Card</div>
  <div class="orca-elevation-2" style="padding: var(--orca-space-16)">Elevated</div>
  <div class="orca-elevation-3" style="padding: var(--orca-space-16)">Dragged</div>
</div>
```

**Classes:** `.orca-elevation-0`, `.orca-elevation-1`, `.orca-elevation-2`, `.orca-elevation-3`

**Tokens:** `--orca-shadow-card`, `--orca-shadow-elevated`, `--orca-shadow-dragged`, `--orca-bg-elevated`

**Principles applied:** Practical UI C12: Use elevation consistently; Practical UI L05: Use depth to support navigation and priority

**ORCA guide items covered:** Shadows (card, elevated, dragged); Elevation utilities

---

## Layers (z-index)

`id: layers` · level: primitive · source: ORCA

A fixed stacking order from page content to the skip link.

### When to use

- Anything positioned that must sit above or below something else.

### When not to use

- Raw z-index numbers.

### How to use

- Order: `layer-base` 0 < `raised` 1 < `sticky` 10 < `sidebar` 20 < `dropdown` 100 < `drawer` 150 < `dialog` 200 < `toast` 300 < `tooltip` 400 < `skip` 1000.
- Use `z-index: var(--orca-layer-dropdown)`.

#### Example: Using a layer

```django
<div style="position: relative; height: 4rem; background: var(--orca-bg-alt)">
  <div class="orca-elevation-2" style="position: absolute; z-index: var(--orca-layer-dropdown); top: var(--orca-space-8); left: var(--orca-space-8); padding: var(--orca-space-8)">Dropdown layer</div>
</div>
```

**Tokens:** `--orca-layer-sticky`, `--orca-layer-dropdown`, `--orca-layer-drawer`, `--orca-layer-dialog`, `--orca-layer-toast`, `--orca-layer-tooltip`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Layers

---

## Control heights

`id: control-heights` · level: primitive · source: Tangerine

Five heights shared by buttons, fields, selects and toggles: sm, dense, md, lg, xl.

### When to use

- md (37px) by default; dense (29px) in top bars and filter bars; sm (22.5px) inside table rows; lg (44px) for touch-first screens; xl (48px) for phone primary actions.

### When not to use

- Mixing heights in one row of controls.

### How to use

- Modifiers: `--sm`, `--dense`, `--lg`, `--xl` on `.orca-button`, `.orca-input`, `.orca-select`, `.orca-icon-button`.
- On coarse pointers and below 620px every control grows to `--orca-control-lg` (44px) automatically.

#### Example: Heights side by side

```django
<div class="orca-row">
  <button class="orca-button orca-button--sm" type="button">Small</button>
  <button class="orca-button orca-button--dense" type="button">Dense</button>
  <button class="orca-button" type="button">Default</button>
  <button class="orca-button orca-button--lg" type="button">Large</button>
  <button class="orca-button orca-button--xl" type="button">Extra large</button>
</div>
```

**Tokens:** `--orca-control-sm`, `--orca-control-dense`, `--orca-control-md`, `--orca-control-lg`, `--orca-control-xl`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI B11: Make targets large and separated

**ORCA guide items covered:** Control heights (sm, md, lg, xl)

---

## Motion

`id: motion` · level: primitive · source: Tangerine

Four durations and two easings, all under the 400 ms Doherty threshold.

### When to use

- snap 0.1s: hover on buttons, tabs, rows.
- fast 0.165s: field fills, chevrons, card lift.
- brisk 0.333s: ticks, switches, accordions, drawers, progress.

### When not to use

- Animations longer than 0.333s on interface feedback.
- Looping motion except spinners, skeletons and indeterminate progress.

### How to use

- `transition: background-color var(--orca-duration-snap) var(--orca-ease-in)` for hover.
- `var(--orca-ease-out)` for anything arriving.
- ORCA's base layer stops animations for `prefers-reduced-motion: reduce`.

#### Example: Hover speed

```django
<button class="orca-button" type="button">Hover me: 0.1s</button>
```

**Tokens:** `--orca-duration-snap`, `--orca-duration-fast`, `--orca-duration-brisk`, `--orca-ease-out`, `--orca-ease-in`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Animation; Motion

---

## Aspect-ratio utilities

`id: aspect-ratio` · level: primitive · source: ORCA

Reserve the space of images and video before they load.

### When to use

- Any image, video, snapshot or chart whose size is known only after loading.

### How to use

- Wrapper: `.orca-ratio.orca-ratio--16x9` (also 1x1, 4x3, 3x2, 21x9, 3x4) with the media inside.
- Single element: `.orca-aspect-16x9` etc. Custom ratio: `style="--orca-ratio: 5 / 4"` on `.orca-ratio`.

#### Example: 16:9 frame

```django
<div class="orca-ratio orca-ratio--16x9" style="max-width: 20rem">
  <img src="{% static "orca/img/sample-street.svg" %}" alt="City street at dusk" loading="lazy">
</div>
```

**Classes:** `.orca-ratio`, `.orca-ratio--16x9`, `.orca-aspect-16x9`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Aspect-ratio utilities

---

## Scrollbar style

`id: scrollbar` · level: primitive · source: ORCA

A thin, token-coloured scrollbar for inner scrolling regions.

### When to use

- Scrolling panels, menus, code blocks, sidebars.

### When not to use

- Styling the page's main scrollbar; leave the OS default.

### How to use

- Add `.orca-scroll` to the element that scrolls; it sets `overflow: auto`.

#### Example: Scrolling region

```django
<div class="orca-scroll" style="max-height: 6rem; border: var(--orca-border-width) solid var(--orca-border); padding: var(--orca-space-8)">
  {% for i in "123456789" %}
    <p class="orca-p">Row {{ i }}</p>
  {% endfor %}
</div>
```

**Classes:** `.orca-scroll`

**Tokens:** `--orca-border-strong`

**Principles applied:** Practical UI S06: Make essential content visible or discoverable

**ORCA guide items covered:** Scrollbar style

---
