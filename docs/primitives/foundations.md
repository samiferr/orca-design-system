# Base styles

The tokens all other elements are built from: colour, type, space, shape, elevation, layers, size and motion. Use the names, never raw values. Projects may change only brand tokens.

## Colour palette

`id: color-palette` · level: primitive · source: ORCA

Raw colours: a 13-step gray scale and eleven hues with nine numbered steps each.

### General description

A color palette is the fixed set of raw colors a product draws from, usually a gray scale plus a few hues in graded shades.

#### Use cases

- Choosing colors for charts and illustrations that need several distinct categories.
- Defining the colors that interface roles such as text or errors point to.
- Keeping brand and data colors consistent across pages.

#### When not to use it

- Coloring text, buttons or status directly from raw swatches; name colors by their job instead.
- Telling chart series apart by hue alone; add labels, shapes or patterns.

#### Best practices

- Keep the palette small and name every shade.
- Make neighboring shades differ enough to tell apart.
- Check text contrast against every background it sits on.
- Give each hue the same range of light to dark steps.

### When to use

- Charts, zones, calendars and illustrations that need several distinct categories.
- Defining a new semantic token inside ORCA itself.

### When not to use

- Text, controls, backgrounds and status: use `semantic-colors`.
- Separating series by hue alone: also vary lightness or add a shape, label or pattern.

### How to use

- Gray: `--orca-gray-0` (white) to `--orca-gray-1000` (black).
- Hues: `--orca-{red|orange|amber|yellow|green|teal|cyan|blue|indigo|purple|pink}-{100..900}`; 100 is lightest.
- For data series use `--orca-chart-1`…`--orca-chart-8`, which pick contrasting steps for each theme.
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

Colours named by their job: text, backgrounds, lines, interaction, status, actions, planning and data.

### General description

Semantic colors are named by their purpose, such as text, border, error or success, rather than by how they look. They let one design work in many themes.

#### Use cases

- Coloring text, backgrounds and borders consistently across a product.
- Showing status such as success, warning and error.
- Switching between light and dark themes without changing components.

#### When not to use it

- Picking a color for its look instead of its meaning; choose the role it plays.
- Using color alone to show status; add an icon and a word.

#### Best practices

- Name colors by job, not by hue.
- Test each role for readable contrast in every theme.
- Pair every status color with an icon and text.
- Use one color per meaning, everywhere.

### When to use

- Every colour in every element and page.

### When not to use

- Picking a token for its look instead of its job (a muted heading is still `--orca-text`).
- `--orca-border` (decorative, 1.6:1) on a control: controls need `--orca-border-strong` (3:1).

### How to use

- Text: `text` (body, labels, headings), `text-muted` (help, meta), `text-inactive` (unselected nav).
- Backgrounds: `bg` page, `bg-alt` separate region, `bg-input` fields, `bg-hover`, `bg-active` (pressed, selected), `bg-elevated` floating.
- Lines: `border` decorative, `border-strong` controls, `border-weak` row separators.
- Status families `info`, `positive`, `caution`, `negative`, `neutral`: the bare name for marks and text, `-bg` for tints, `-fill` for solid badges.
- Actions: `primary*` (main action, green), `danger*` (confirmed destruction), `brand-strong*` (brand fill).
- Pair every status colour with an icon and a word.

### Accessibility

- `text` and `text-muted` hold 4.5:1 on `bg`, `bg-alt` and `bg-input` in every theme.
- Known exception from Vanilla: `caution` text is 3.0:1 in light themes, so never use it alone.

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

### General description

The brand color is the one signature color that identifies a product. It marks a few key moments, such as the logo, top bar or a main button.

#### Use cases

- Coloring the logo, header bar or a single main call to action.
- Re-skinning a product for a new brand.
- Adding a small highlight rule or accent mark.

#### When not to use it

- Showing success, warning or error; use status colors instead.
- Filling many elements on one screen; repeated emphasis stops standing out.

#### Best practices

- Use the brand color sparingly so it keeps its impact.
- Check that text on brand fills has enough contrast.
- Pair it with neutral grays for most of the page.
- Do not rely on it alone to show state.

### When to use

- One brand moment per page: the top bar, brand button, logo mark or a highlight rule.
- Re-branding: set `ORCA['BRAND']['color']` and nothing else.

### When not to use

- More than one brand-filled element per screen (Von Restorff: emphasis loses power when repeated).
- Showing status: brand never means success, warning or error.
- Links and checked controls: use the accent colour.

### How to use

- `--orca-brand`: the colour as given, for decorative marks and 3px bars (needs only 3:1).
- `--orca-brand-strong`: fills that carry text, darkened until `--orca-brand-on` reads at 4.5:1.
- `--orca-brand-strong-hover` / `-active`: derived hover and pressed fills.
- Surfaces: page `--orca-bg`, set-apart regions `--orca-bg-alt`, floating `--orca-bg-elevated`.
- Set it in settings; any adjustment ORCA makes is reported as a system-check warning (`orca.W001`).

### Accessibility

- Never show state by brand colour alone; selection uses the accent and a shape.

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

### General description

The accent color is the single color that signals something is interactive or selected, such as links, checked boxes and active controls.

#### Use cases

- Coloring links so people see what they can click.
- Showing checked, on or selected states.
- Filling progress indicators and highlighting selected dates.

#### When not to use it

- Coloring static headings or decorative icons; this makes people think they are clickable.
- Large fills behind long text; they are hard to read.

#### Best practices

- Use one action color across the whole product.
- Make sure link text reaches readable contrast on every background.
- Do not depend on color alone; add underlines or shapes.
- Reserve the color for things people can act on.

### When to use

- Links, checked ticks, radios and switches, progress fills, selected calendar days, accent outlines and badges.

### When not to use

- Static headings or decorative icons: action colour on non-interactive things misleads (C07).
- Large fills behind long text.

### How to use

- Use `var(--orca-accent)`; hover is `var(--orca-accent-hover)`.
- Set `ORCA['BRAND']['accent']` (light and paper) and optionally `accent_dark`; ORCA adjusts it to 4.5:1.
- Text on an accent fill is `var(--orca-bg)`.

### Accessibility

- Holds 4.5:1 on `bg` and `bg-alt` in every theme, so it works for link text.

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

### General description

A theme is a complete set of colors for the same interface, such as light or dark. People choose one, or the system picks it for them.

#### Use cases

- Offering a dark mode for low light or light sensitivity.
- Following the person's operating system setting automatically.
- Offering a low-glare paper-like reading mode.

#### When not to use it

- Writing separate styles for each theme in every component; define shared color names once.
- Using pure black backgrounds; very dark grays are easier on the eyes.

#### Best practices

- Respect the system theme by default and remember a manual choice.
- Keep contrast readable in every theme.
- Define colors by role so components need no theme-specific code.
- Test every screen in all themes.

### When to use

- Always: every page gets all three themes for free.
- Set `ORCA['THEME']` to `light`, `dark` or `paper` to force one. `auto` (default) follows the OS and the user's saved choice.

### When not to use

- Theme-specific CSS: if you need it, a token is missing, so report it.
- Pure black backgrounds: dark uses #262626 and #202020.

### How to use

- Put `{% orca_html_attrs %}` on `<html>` and `{% orca_head %}` in `<head>`.
- A theme toggle is a button with `data-orca-theme-toggle`; it cycles light → dark → paper and remembers the choice.
- Appearance: ORCA only (square corners, 1.5px borders, filled fields with a bottom border, inside focus ring).

### Accessibility

- Contrast holds in every theme; dark lifts floating surfaces one step so elevation shows without shadows.

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

### General description

Typography is the choice and arrangement of fonts, sizes and weights so text is easy to read and its importance is clear.

#### Use cases

- Setting headings, body text, labels and captions.
- Showing code in a monospaced font.
- Building a clear visual hierarchy on a page.

#### When not to use it

- Inventing new sizes and weights for each page; use a fixed scale.
- Setting long text in all capitals; use it only for short labels.

#### Best practices

- Use one readable font family with few weights.
- Size text in relative units so it follows the user's settings.
- Limit line length to about 70 characters.
- Use tabular figures for numbers in tables.

### When to use

- Every piece of text; pick the style by role: heading, title, body, detail, label or code.

### When not to use

- New sizes or weights in page CSS.
- Weights other than 400 and 550 for interface text (thin 180/275 only for the large h2/h4 styles).
- All caps for anything longer than a short label (W07).

### How to use

- Heading: `--orca-type-h1`…`h6`, `--orca-type-page-title`, `--orca-type-display`.
- Title: `--orca-type-title` (panel and card titles, 18/24 550).
- Body: `--orca-type-body` (16/24) and `--orca-type-body-strong` (550). Bold is 550, not 700.
- Detail: `--orca-type-detail` (14/20) for help, meta and timestamps; `--orca-type-label` (12/16 550) for table headers, badges, kickers and stat card labels.
- Figure: `--orca-type-figure` (28/36 550) for a stat card's number.
- Code: `--orca-type-code` with `--orca-font-mono` (JetBrains Mono, self-hosted; it keeps 0/O and 1/l/I distinct). Code blocks use the `--orca-code-*` tokens.
- Numbers in tables and stats get `font-variant-numeric: tabular-nums` (`.orca-num`).
- Apply as `font: var(--orca-type-body)`. Brand tokens `font_sans` / `font_mono` swap the families.

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

### General description

Spacing is the empty room around and between elements. A fixed scale of steps makes layouts consistent and shows which things belong together.

#### Use cases

- Setting padding, margins and gaps between elements.
- Grouping related items closer than unrelated ones.
- Separating sections without lines or boxes.

#### When not to use it

- Picking one-off values such as 10px or 18px; use the scale.
- Using the same gap at every level; it hides the grouping.

#### Best practices

- Base all spacing on one unit, such as 8px.
- Work from the inside out: the smallest gap sits closest to the content.
- Use space before adding borders.
- Keep gaps larger between groups than within them.

### When to use

- Every margin, padding and gap.

### When not to use

- Values off the scale (6px, 10px, 18px).
- Using the same gap at every nesting level: it flattens grouping.

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

### General description

Borders are lines drawn around or between elements to outline them and separate content. A few set line weights keep them consistent.

#### Use cases

- Outlining buttons, cards, alerts and fields.
- Separating rows in tables and lists.
- Marking the selected tab or a highlight.

#### When not to use it

- Boxing every group; use spacing first and keep borders for real separation.
- Using faint decorative lines as the edge of a control; controls need stronger contrast.

#### Best practices

- Use only a few line weights and give each a meaning.
- Give control outlines enough contrast to see.
- Keep thick lines for emphasis only.
- Pick line color by purpose, decorative or functional.

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

### General description

Corner radii set how rounded the corners of elements are. A consistent corner style gives a product a recognizable look.

#### Use cases

- Setting square or rounded corners on buttons, cards and fields.
- Making circles for avatars, status dots and radio buttons.
- Giving pills and progress tracks their rounded ends.

#### When not to use it

- Mixing many corner styles in one screen; choose a small set.
- Rounding checkboxes like radio buttons; shape tells people which is which.

#### Best practices

- Define radii as named values, even for zero.
- Use round shapes only for round things.
- Apply the same radius to the same kind of element.
- Keep nested corners visually consistent.

### When to use

- `--orca-radius-none` for every box: buttons, fields, cards, menus, dialogs, badges, tags.
- `--orca-radius-round` for radios, status dots, avatars, step markers, the switch handle.
- `--orca-radius-pill` for the switch track and count badges; `--orca-radius-bar` for progress tracks.

### When not to use

- Rounding a checkbox: square means pick many, round means pick one (Practical UI R07).

### How to use

- Use the tokens even for 0, so a later rounding change only edits a token.

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

### General description

Shadows suggest depth by making an element look lifted above the page. They help show what floats, such as menus, or what can be moved.

#### Use cases

- Lifting menus, dropdowns, popovers and toasts above content.
- Showing a dragged item or a dialog.
- Giving a card a hover lift.

#### When not to use it

- Putting shadows on every card and panel; use a border or background tint.
- Using heavy shadows for decoration; they add noise.

#### Best practices

- Reserve shadows for things that float.
- Use a few fixed levels, not custom blurs.
- In dark themes, lighten the surface as well.
- Keep shadows soft and subtle.

### When to use

- `shadow-card`: the hover lift of an interactive card.
- `shadow-elevated`: menus, dropdown lists, popovers, toasts, drawers.
- `shadow-dragged`: a dragged item, a dialog, a sidebar opened over content.

### When not to use

- Shadows on resting cards, panels or page sections: use a border or `bg-alt`.

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

### General description

Layers define the stacking order of elements that overlap, such as sticky headers, menus, dialogs and notifications.

#### Use cases

- Keeping dropdowns above the content around them.
- Making sure notifications are not hidden behind dialogs.
- Placing sticky headers and sidebars correctly.

#### When not to use it

- Using ever larger random z-index numbers; use named levels.
- Layering many elements at once; reduce overlap where possible.

#### Best practices

- Define a fixed, named stacking order in one place.
- Order levels by how urgent the element is.
- Reference names, not raw numbers.
- Let the skip link and tooltips sit on top.

### When to use

- Any positioned element that must sit above or below another.

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

### General description

Control heights are the standard sizes shared by buttons, fields and selects, so controls line up and are big enough to tap.

#### Use cases

- Aligning buttons and fields in a row or toolbar.
- Making denser controls for tables and filter bars.
- Making larger controls for touch screens.

#### When not to use it

- Mixing heights in one row of controls.
- Small controls on touch screens; make targets at least 44px.

#### Best practices

- Offer a few fixed heights, not custom ones.
- Make touch targets at least 44px high.
- Use the default height unless space is tight.
- Grow controls automatically on touch devices.

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

### General description

Motion is movement and transition in an interface, such as fades and slides, used to give feedback and explain what changed.

#### Use cases

- Giving feedback on hover and press.
- Showing something opening, arriving or closing.
- Showing progress or loading.

#### When not to use it

- Decorative animation that slows people down.
- Long or looping effects, except loading indicators; keep feedback fast.

#### Best practices

- Keep interface animations short, under about 400 milliseconds.
- Use the same timing for the same kind of change.
- Respect the reduced-motion setting and show the end state.
- Use easing that decelerates for things that arrive.

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
- The base layer stops animations for `prefers-reduced-motion: reduce`.

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

### General description

An aspect ratio is the proportion of an element's width to its height. Setting it ahead of time reserves space before the content loads.

#### Use cases

- Reserving room for images and video while they load.
- Keeping thumbnails and cards a consistent shape.
- Framing embedded maps or charts.

#### When not to use it

- Leaving media without set dimensions; the page jumps when it loads.
- Stretching images to fit; crop or letterbox instead.

#### Best practices

- Set the ratio before the media loads.
- Use common ratios such as 16:9, 4:3 and 1:1.
- Crop images to fill the frame without distortion.
- Write alt text for every image.

### When to use

- Any image, video, snapshot or chart whose size is unknown until it loads.

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

### General description

A scrollbar shows that content continues beyond the visible area and lets people move through it. Inner regions can have their own slim scrollbar.

#### Use cases

- Scrolling long panels, menus and sidebars.
- Scrolling code blocks and long lists inside a page.
- Showing that a region holds more content.

#### When not to use it

- Restyling the main page scrollbar; leave the system default.
- Hiding scrollbars completely; people lose the cue that more exists.

#### Best practices

- Keep scrollbars visible and with enough contrast.
- Limit nested scrolling regions where possible.
- Give scroll areas a clear height so the edge is obvious.
- Make sure keyboard users can scroll them.

### When to use

- Scrolling panels, menus, code blocks, sidebars.

### When not to use

- Styling the page's main scrollbar: leave the OS default.

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
