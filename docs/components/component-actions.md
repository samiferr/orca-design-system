# Actions

Groups of actions: button groups, menus and the action sets that sit on records and rows.

## Button group

`id: button-group` · level: component · source: ORCA

Related buttons joined into one control, or spaced as a set.

Built from: `button`

### Why

Joining buttons shows they act on the same thing (Practical UI L01: common region); spacing keeps dangerous neighbours apart (Fitts's law).

### When to use

- Joined: alternatives on one object (Zoom in, Zoom out, Reset).
- Spaced: a set of independent actions (Export, Print).

### When not to use

- Choosing a mode: use a segmented control or toggle buttons with aria-pressed.

### How to use

- `<div class="orca-button-group" role="group" aria-label=…>` of `.orca-button`; `--spaced` for 8px gaps.
- Keep the same variant within a joined group; never join a destructive button.

#### Example: Joined and spaced

```django
<div class="orca-row orca-row--16">
  <div class="orca-button-group" role="group" aria-label="Zoom"><button class="orca-button orca-button--dense" type="button" aria-label="Zoom out">{% icon "minus" %}</button><button class="orca-button orca-button--dense" type="button">100%</button><button class="orca-button orca-button--dense" type="button" aria-label="Zoom in">{% icon "plus" %}</button></div>
  <div class="orca-button-group orca-button-group--spaced" role="group" aria-label="Report"><button class="orca-button" type="button">Export CSV</button><button class="orca-button" type="button">Schedule</button></div>
</div>
```

**Classes:** `.orca-button-group`, `.orca-button-group--spaced`

**Principles applied:** Practical UI L01: Group related information; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Button group

---

## Dropdown menu

`id: dropdown-menu` · level: component · source: Tangerine

A button that opens a list of actions.

Built from: `button`, `dropdown-item`

### Why

Rare or secondary actions go behind one button so the screen keeps one clear priority (Hick's law, Practical UI S04), while staying one click away.

### When to use

- More than two secondary actions on an object; account menus; 'Add' menus with several kinds.

### When not to use

- Choosing a value: use a select or dropdown select.
- The one main action: show it as a button.

### How to use

- `<div class="orca-anchor">` with `<button class="orca-button" type="button" aria-haspopup="menu" aria-expanded="false" aria-controls="m1" data-orca-menu>` and `<ul class="orca-popover" role="menu" id="m1" hidden>`.
- Items are dropdown items. Group with `.orca-menu__separator` and `.orca-menu__group` labels; put destructive items last.
- `orca-popover--end` aligns it to the button's end edge; `--up` opens upwards near the bottom of the screen.

### Accessibility

- orca.js: Enter/Space/Down open on the first item, Up on the last; arrows move; Escape closes and returns focus.

#### Example: Actions menu

```django
<div class="orca-anchor">
  <button class="orca-button" type="button" aria-haspopup="menu" aria-expanded="false" aria-controls="dm-1" data-orca-menu>Actions{% icon "chevron-down" %}</button>
  <ul class="orca-popover" role="menu" id="dm-1" hidden>
    <li role="none"><button class="orca-menu__item" role="menuitem" type="button">{% icon "edit" %}Rename</button></li>
    <li role="none"><button class="orca-menu__item" role="menuitem" type="button">{% icon "copy" %}Duplicate</button></li>
    <li role="none"><a class="orca-menu__item" role="menuitem" href="#">{% icon "external-link" %}Open stream</a></li>
    <li role="separator" class="orca-menu__separator"></li>
    <li role="none"><button class="orca-menu__item orca-menu__item--danger" role="menuitem" type="button">{% icon "delete" %}Delete</button></li>
  </ul>
</div>
```

**Classes:** `.orca-anchor`, `.orca-popover`, `.orca-popover--end`, `.orca-popover--up`, `.orca-menu__separator`, `.orca-menu__group`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI S04: Reveal secondary information when needed; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Dropdown menu

---

## Dropdown item

`id: dropdown-item` · level: component · source: Tangerine

One action in a menu: icon, label, optional description or shortcut; danger and disabled variants.

Built from: `icon`, `kbd`

### Why

Consistent rows with a leading icon and a verb are scanned fast (Miller's law); a description removes doubt about what an item does (Practical UI W04).

### When to use

- Every row of a dropdown menu.

### How to use

- `<li role="none"><button class="orca-menu__item" role="menuitem" type="button">` or an `<a>` for navigation.
- Description: wrap text in `.orca-menu__text` with `.orca-menu__desc`. Shortcut: a `.orca-kbd` at the end.
- `--danger` for destructive items (confirm them); `aria-disabled="true"` with the reason in the description.

#### Example: Items

```django
<ul class="orca-popover" role="menu" style="position: static; display: block" aria-label="Example items">
  <li role="none"><button class="orca-menu__item" role="menuitem" type="button">{% icon "copy" %}Copy link<kbd class="orca-kbd">Ctrl C</kbd></button></li>
  <li role="none"><button class="orca-menu__item" role="menuitem" type="button">{% icon "upload" %}<span class="orca-menu__text">Export<span class="orca-menu__desc">CSV with one row per hour</span></span></button></li>
  <li role="none"><button class="orca-menu__item" role="menuitem" type="button" aria-disabled="true">{% icon "archive" %}<span class="orca-menu__text">Archive<span class="orca-menu__desc">Stop the run first</span></span></button></li>
  <li role="none"><button class="orca-menu__item orca-menu__item--danger" role="menuitem" type="button">{% icon "delete" %}Delete</button></li>
</ul>
```

**Classes:** `.orca-menu__item`, `.orca-menu__item--danger`, `.orca-menu__text`, `.orca-menu__desc`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI W04: Lead with the information people seek; Practical UI B07: Explain necessary disabled states

**ORCA guide items covered:** Dropdown item

---

## Copy button

`id: copy-button` · level: component · source: ORCA

A value with a Copy button that confirms 'Copied' in place and for screen readers.

Built from: `button`, `code-text`

### Why

Copying exact values (keys, addresses) by hand causes errors; one click with visible confirmation is faster and certain (Doherty threshold, Tesler's law).

### When to use

- IDs, API keys, addresses, links, commands.

### How to use

- `<div class="orca-copy"><code class="orca-copy__value" id="v1">…</code><button class="orca-button" type="button" data-orca-copy="v1">{% icon "copy" %}<span data-orca-copy-label>Copy</span></button></div>`.
- The label changes to 'Copied' for 1.5 s and the change is announced. Where the clipboard is blocked, the value is selected instead.

#### Example: Copy a stream address

```django
<div class="orca-copy"><code class="orca-copy__value" id="cp-1">https://media.example.com/v/4821</code><button class="orca-button" type="button" data-orca-copy="cp-1">{% icon "copy" %}<span data-orca-copy-label>Copy</span></button></div>
```

**Classes:** `.orca-copy`, `.orca-copy__value`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Copy button (copied confirmation)

---

## Record actions

`id: record-actions` · level: component · source: Tangerine

On a record's page: one visible main action and a 'More actions' menu for the rest.

Built from: `icon-button`, `dropdown-menu`

### Why

One visible action keeps the decision simple (Hick's law, Practical UI B03); the overflow menu keeps the rest reachable without crowding the header.

### When to use

- The header of detail pages and cards with several actions.

### How to use

- `<div class="orca-record-actions">` with the main action as a button and an icon button (`aria-label="More actions for Entrance A"`) opening a dropdown menu.
- Destructive actions go last in the menu and ask for confirmation.

#### Example: Record actions

```django
<div class="orca-record-actions orca-anchor">
  <a class="orca-button" href="#">{% icon "edit" %}Edit video</a>
  <button class="orca-icon-button orca-icon-button--outlined" type="button" aria-label="More actions for Entrance A" aria-haspopup="menu" aria-expanded="false" aria-controls="ra-menu" data-orca-menu>{% icon "more" %}</button>
  <ul class="orca-popover orca-popover--end" role="menu" id="ra-menu" hidden>
    <li role="none"><button class="orca-menu__item" role="menuitem" type="button">{% icon "pin" %}Pin to dashboard</button></li>
    <li role="none"><button class="orca-menu__item" role="menuitem" type="button">{% icon "restart" %}Restart stream</button></li>
    <li role="separator" class="orca-menu__separator"></li>
    <li role="none"><button class="orca-menu__item orca-menu__item--danger" role="menuitem" type="button">{% icon "delete" %}Delete video</button></li>
  </ul>
</div>
```

**Classes:** `.orca-record-actions`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI B03: One primary action; Practical UI B13: Scale friction to the consequence

**ORCA guide items covered:** Record actions (one button + overflow menu)

---

## Row actions

`id: row-actions` · level: component · source: ORCA

Small actions at the end of a table row: one or two ghost buttons and an overflow menu.

Built from: `icon-button`, `dropdown-menu`

### Why

Actions next to the row they affect shorten travel (Practical UI L14); quiet styling keeps many rows from shouting (B05). They are always visible, never hover-only, so touch and keyboard users find them.

### When to use

- The last column of data tables.

### How to use

- `<td><div class="orca-row-actions">` with `orca-button--ghost orca-button--sm` buttons or icon buttons whose `aria-label` names the row ('Edit Entrance A').
- At most two visible actions; the rest in a menu.

#### Example: In a row

```django
<table class="orca-table" style="max-width: 32rem"><tbody><tr><td>Entrance A</td><td><span class="orca-status"><span class="orca-dot orca-dot--positive"></span>Online</span></td>
  <td><div class="orca-row-actions"><a class="orca-button orca-button--ghost orca-button--sm" href="#">Edit</a><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="More actions for Entrance A">{% icon "more" %}</button></div></td></tr></tbody></table>
```

**Classes:** `.orca-row-actions`

**Principles applied:** Practical UI L14: Reduce travel between related actions; Practical UI B05: Keep low-priority actions quieter; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Row actions

---
