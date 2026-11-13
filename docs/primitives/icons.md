# Icons

One icon set, 16px, single ink in currentColor. Icons support words and never replace them.

## Icon

`id: icon` · level: primitive · source: Tangerine

An inline SVG glyph from the ORCA set, sized by token and coloured like its text.

### General description

A small picture that stands for an object or action, such as a magnifier for search. Icons help people recognise things quickly.

#### Use cases

- Adding meaning next to labels in buttons and menus.
- Marking status in messages and lists.
- Saving space in toolbars with well-known symbols.

#### When not to use it

- Ideas without a well-known symbol: use words.
- Decoration that competes with the content.

#### Best practices

- Pair icons with text whenever possible.
- Use one style and line weight throughout.
- Give standalone icons an accessible name.
- Let icons inherit the colour of the text.

### When to use

- Beside a label in buttons, menus, navigation and status messages.
- Alone only in icon buttons with an `aria-label`.

### When not to use

- Icons from another set on the same screen.
- Icons as the only carrier of meaning.
- Decorative icons that compete with content (B12).

### How to use

- `{% icon "search" %}` renders decorative inline SVG (`aria-hidden`).
- `{% icon "close" label="Close" %}` only when the icon stands alone without a labelled control.
- Sizes: `size="xs"` 12px (inside 12–14px text), `s` 16px default (every control), `m` 20px, `l` 24px (heading icons), `xl` 36px (empty states). Aliases: small=xs, default=s, large=l.
- Colour follows `currentColor`: set `color` on the parent, never on the path.
- List all names: `python -m orca icons`.

### Accessibility

- Decorative by default. Interactive icon-only controls put the name on the control, not the svg.

#### Example: Sizes

```django
<div class="orca-row orca-row--16">
  {% icon "statistics" size="xs" %}
  {% icon "statistics" %}
  {% icon "statistics" size="m" %}
  {% icon "statistics" size="l" %}
  {% icon "statistics" size="xl" %}
</div>
```

#### Example: Icon with a word

```django
<span class="orca-with-icon">
  {% icon "location" %}
  North building
</span>
```

**Classes:** `.orca-icon`, `.orca-icon--xs`, `.orca-icon--m`, `.orca-icon--l`, `.orca-icon--xl`, `.orca-with-icon`

**Tokens:** `--orca-icon-xs`, `--orca-icon-s`, `--orca-icon-m`, `--orca-icon-l`, `--orca-icon-xl`, `--orca-icon`

**Principles applied:** Jakob's law: work the way products people already know work; Hick's law: fewer, clearer choices mean faster decisions; Practical UI F09: Keep visual and functional behaviour consistent; Practical UI B12: Balance icons and labels

**Related:** `icon-set`, `icon-button`

**ORCA guide items covered:** Icon (small, default, large); Icon sizes (xs, s, m, l, xl)

---

## Status icon

`id: status-icon` · level: primitive · source: Tangerine

The four status glyphs (success, warning, error, info), each a distinct shape in its status colour.

### General description

A symbol that shows state, such as success, warning, error or information. Each has its own shape and colour so it can be told apart.

#### Use cases

- Showing results in alerts and messages.
- Marking errors next to form fields.
- Showing the state of a job, device or item.

#### When not to use it

- Pure decoration: choose a neutral icon or none.
- Long explanations: use a text message.

#### Best practices

- Use different shapes, not only different colours.
- Always add a word with the icon.
- Use the same icon for the same meaning everywhere.
- Keep colours with enough contrast.

### When to use

- Alerts, field errors, validation summaries, status badges, run results.

### When not to use

- Using a status glyph as decoration or in another colour.

### How to use

- `{% status_icon "positive" %}` · `"caution"` · `"negative"` · `"info"` · `"neutral"`.
- Always add a word: 'Online', 'Needs attention', 'Failed'.

### Accessibility

- Decorative unless `label=` is given; the visible word is better.

#### Example: Four statuses

```django
<div class="orca-stack">
  <span class="orca-with-icon">
    {% status_icon "positive" %}
    Online
  </span>
  <span class="orca-with-icon">
    {% status_icon "caution" %}
    Disk 90% full
  </span>
  <span class="orca-with-icon">
    {% status_icon "negative" %}
    Offline since 08:14
  </span>
  <span class="orca-with-icon">
    {% status_icon "info" %}
    Firmware update available
  </span>
</div>
```

**Classes:** `.orca-status-icon--positive`, `.orca-status-icon--caution`, `.orca-status-icon--negative`, `.orca-status-icon--info`

**Tokens:** `--orca-positive`, `--orca-caution`, `--orca-negative`, `--orca-info`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI C04: Reserve status colours for their meanings; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**Related:** `badge`, `alert-icon`

**ORCA guide items covered:** Status icon (four status glyphs); Success; Error

---

## Icon set

`id: icon-set` · level: primitive · source: Tangerine

The named glyphs: 106 from Vanilla (via Tangerine) plus ORCA glyphs for ideas Vanilla lacks.

### General description

The collection of icons a product draws from, all sharing one size grid, line weight and style so the interface looks consistent.

#### Use cases

- Choosing a symbol for a new button or menu item.
- Keeping the look of icons consistent across screens.
- Finding standard names for common concepts.

#### When not to use it

- Mixing icons from several sets on one screen.
- Inventing new symbols for well-known actions: use the familiar one.

#### Best practices

- Pick icons that match the word, such as a bin for delete.
- Keep the same size and weight.
- Do not use one icon for two meanings.
- Add new icons in the same style.

### When to use

- Pick a name from the set; use an alias when the guide's word differs (bell → notifications, refresh → restart, pencil → edit).

### When not to use

- Adding SVGs from other sets (Lucide, Material). If a glyph is missing, use a word and ask for it to be added.

### How to use

- Guide icons: menu, notifications, snapshot, statistics, plus, search, play, arrow-right, chevron-left, chevron-right, chevron-down, close, delete, archive, restart, location, edit, filter, star, more, sort, grid, chat, sliders, home, help, unlock, success, error, settings.
- Full list with previews: the docs site's Icons page or `python -m orca icons`.
- Arrows: arrow-up/down/left/right and diagonals. Chevrons: chevron-up/down/left/right (mirror left/right in RTL).

#### Example: Guide icons

```django
<div class="orca-row orca-row--16" style="max-width: 30rem">
  <span title="menu">
    {% icon "menu" size="m" %}
  </span>
  <span title="notifications">
    {% icon "notifications" size="m" %}
  </span>
  <span title="snapshot">
    {% icon "snapshot" size="m" %}
  </span>
  <span title="statistics">
    {% icon "statistics" size="m" %}
  </span>
  <span title="plus">
    {% icon "plus" size="m" %}
  </span>
  <span title="search">
    {% icon "search" size="m" %}
  </span>
  <span title="play">
    {% icon "play" size="m" %}
  </span>
  <span title="arrow-right">
    {% icon "arrow-right" size="m" %}
  </span>
  <span title="chevron-left">
    {% icon "chevron-left" size="m" %}
  </span>
  <span title="chevron-right">
    {% icon "chevron-right" size="m" %}
  </span>
  <span title="chevron-down">
    {% icon "chevron-down" size="m" %}
  </span>
  <span title="close">
    {% icon "close" size="m" %}
  </span>
  <span title="delete">
    {% icon "delete" size="m" %}
  </span>
  <span title="archive">
    {% icon "archive" size="m" %}
  </span>
  <span title="restart">
    {% icon "restart" size="m" %}
  </span>
  <span title="location">
    {% icon "location" size="m" %}
  </span>
  <span title="edit">
    {% icon "edit" size="m" %}
  </span>
  <span title="filter">
    {% icon "filter" size="m" %}
  </span>
  <span title="star">
    {% icon "star" size="m" %}
  </span>
  <span title="more">
    {% icon "more" size="m" %}
  </span>
  <span title="sort">
    {% icon "sort" size="m" %}
  </span>
  <span title="grid">
    {% icon "grid" size="m" %}
  </span>
  <span title="chat">
    {% icon "chat" size="m" %}
  </span>
  <span title="sliders">
    {% icon "sliders" size="m" %}
  </span>
  <span title="home">
    {% icon "home" size="m" %}
  </span>
  <span title="help">
    {% icon "help" size="m" %}
  </span>
  <span title="unlock">
    {% icon "unlock" size="m" %}
  </span>
  <span title="success">
    {% icon "success" size="m" %}
  </span>
  <span title="error">
    {% icon "error" size="m" %}
  </span>
  <span title="settings">
    {% icon "settings" size="m" %}
  </span>
</div>
```

**Tokens:** `--orca-icon`

**Principles applied:** Practical UI F09: Keep visual and functional behaviour consistent; Aesthetic–usability effect: consistent, careful visuals earn trust; Jakob's law: work the way products people already know work

**Related:** `icon`, `planning-icons`

**ORCA guide items covered:** Menu (hamburger); Notifications; Snapshot; Statistics; Plus; Search (magnifier); Play; Arrows; Chevrons (left, right, down); Close; Delete; Archive; Restart; Location; Lucide icon set; Edit (pencil); Filter; Star; More (ellipsis); Sort; Grid; Chat; Sliders; Home; Help; Unlock; Refresh; Settings

---
