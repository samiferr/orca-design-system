# Actions

Button groups, menus, and the action sets on records and rows.

## Button group

`id: button-group` · level: component · source: ORCA

Related buttons joined into one control, or spaced as a set.

Built from: `button`

### General description

A button group is a set of related buttons placed together. Joined buttons act on the same thing, and spaced ones are separate actions.

#### Use cases

- Offering alternatives on one object, such as zoom in and out.
- Grouping related actions like Export and Print.
- Keeping toolbars tidy.

#### When not to use it

- Choosing one mode among several: use a segmented control or toggle buttons.
- Many actions: use a menu.

#### Best practices

- Keep a consistent style in a group.
- Label the group for screen readers.
- Keep destructive actions apart.
- Keep a group to a few buttons.

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
  <div class="orca-button-group" role="group" aria-label="Zoom">
    <button class="orca-button orca-button--dense" type="button" aria-label="Zoom out">
      {% icon "minus" %}
    </button>
    <button class="orca-button orca-button--dense" type="button">100%</button>
    <button class="orca-button orca-button--dense" type="button" aria-label="Zoom in">
      {% icon "plus" %}
    </button>
  </div>
  <div class="orca-button-group orca-button-group--spaced" role="group" aria-label="Report">
    <button class="orca-button" type="button">Export CSV</button>
    <button class="orca-button" type="button">Schedule</button>
  </div>
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

### General description

A dropdown menu is a button that opens a list of actions. It hides less common actions to keep the screen simple.

#### Use cases

- Grouping secondary actions on a record.
- Account or user menus.
- An 'Add' button with several kinds.

#### When not to use it

- Choosing a value for a field: use a select.
- The main action: show it as a visible button.

#### Best practices

- Make the menu work with the keyboard.
- Put destructive items last.
- Use short verb labels.
- Close on Escape and return focus.

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
  <button class="orca-button" type="button" aria-haspopup="menu" aria-expanded="false" aria-controls="dm-1" data-orca-menu>
    Actions
    {% icon "chevron-down" %}
  </button>
  <ul class="orca-popover" role="menu" id="dm-1" hidden>
    <li role="none">
      <button class="orca-menu__item" role="menuitem" type="button">
        {% icon "edit" %}
        Rename
      </button>
    </li>
    <li role="none">
      <button class="orca-menu__item" role="menuitem" type="button">
        {% icon "copy" %}
        Duplicate
      </button>
    </li>
    <li role="none">
      <a class="orca-menu__item" role="menuitem" href="#">
        {% icon "external-link" %}
        Open stream
      </a>
    </li>
    <li role="separator" class="orca-menu__separator"></li>
    <li role="none">
      <button class="orca-menu__item orca-menu__item--danger" role="menuitem" type="button">
        {% icon "delete" %}
        Delete
      </button>
    </li>
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

### General description

A dropdown item is one action in a menu, shown as a row with a label and often an icon, description or shortcut.

#### Use cases

- Listing actions in a menu.
- Showing a shortcut next to an action.
- Explaining why an action is unavailable.

#### When not to use it

- Navigation between main sections: use navigation links.
- Setting options: use a checkbox or radio menu item.

#### Best practices

- Start labels with a verb.
- Use icons the same way on every row.
- Mark destructive items clearly.
- Say why an item is disabled.

### When to use

- Every row of a dropdown menu.

### How to use

- `<li role="none"><button class="orca-menu__item" role="menuitem" type="button">` or an `<a>` for navigation.
- Description: wrap text in `.orca-menu__text` with `.orca-menu__desc`. Shortcut: a `.orca-kbd` at the end.
- `--danger` for destructive items (confirm them); `aria-disabled="true"` with the reason in the description.

#### Example: Items

```django
<ul class="orca-popover" role="menu" style="position: static; display: block" aria-label="Example items">
  <li role="none">
    <button class="orca-menu__item" role="menuitem" type="button">
      {% icon "copy" %}
      Copy link
      <kbd class="orca-kbd">Ctrl C</kbd>
    </button>
  </li>
  <li role="none">
    <button class="orca-menu__item" role="menuitem" type="button">
      {% icon "upload" %}
      <span class="orca-menu__text">Export<span class="orca-menu__desc">CSV with one row per hour</span></span>
    </button>
  </li>
  <li role="none">
    <button class="orca-menu__item" role="menuitem" type="button" aria-disabled="true">
      {% icon "archive" %}
      <span class="orca-menu__text">Archive<span class="orca-menu__desc">Stop the run first</span></span>
    </button>
  </li>
  <li role="none">
    <button class="orca-menu__item orca-menu__item--danger" role="menuitem" type="button">
      {% icon "delete" %}
      Delete
    </button>
  </li>
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

### General description

A copy button copies a value to the clipboard in one click and confirms that it worked.

#### Use cases

- Copying API keys, links or IDs.
- Copying commands or addresses.
- Avoiding typing mistakes with exact values.

#### When not to use it

- Long documents: offer a download instead.
- Secrets that must not be shown: do not display them.

#### Best practices

- Show the value next to the button.
- Confirm with 'Copied' and announce it to screen readers.
- Give a fallback if the clipboard is blocked.
- Keep the label clear.

### When to use

- IDs, API keys, addresses, links, commands.

### How to use

- `<div class="orca-copy"><code class="orca-copy__value" id="v1">…</code><button class="orca-button" type="button" data-orca-copy="v1">{% icon "copy" class="orca-icon--copy" %}{% icon "check" class="orca-icon--copied" %}<span data-orca-copy-label>Copy</span></button></div>`.
- For 1.5 s the label reads 'Copied', the copy icon becomes a check mark and the change is announced. Where the clipboard is blocked, the value is selected instead.

#### Example: Copy a stream address

```django
<div class="orca-copy">
  <code class="orca-copy__value" id="cp-1">https://media.example.com/v/4821</code>
  <button class="orca-button" type="button" data-orca-copy="cp-1">
    {% icon "copy" class="orca-icon--copy" %}
    {% icon "check" class="orca-icon--copied" %}
    <span data-orca-copy-label>Copy</span>
  </button>
</div>
```

**Classes:** `.orca-copy`, `.orca-copy__value`, `.orca-icon--copy`, `.orca-icon--copied`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Copy button (copied confirmation)

---

## Record actions

`id: record-actions` · level: component · source: Tangerine

On a record's page: one visible main action and a 'More actions' menu for the rest.

Built from: `icon-button`, `dropdown-menu`

### General description

Record actions put the main action of a record in view and tuck the others into a 'More actions' menu.

#### Use cases

- The header of a detail page.
- A card with several actions.
- Keeping a toolbar simple.

#### When not to use it

- Records with one action: show only a button.
- Many equal actions: consider a toolbar.

#### Best practices

- Show one main action.
- Name the record in the menu button's label.
- Put destructive actions last.
- Ask before destructive actions.

### When to use

- The header of detail pages and cards with several actions.

### How to use

- `<div class="orca-record-actions">` with the main action as a button and an icon button (`aria-label="More actions for Entrance A"`) opening a dropdown menu.
- Destructive actions go last in the menu and ask for confirmation.

#### Example: Record actions

```django
<div class="orca-record-actions orca-anchor">
  <a class="orca-button" href="#">
    {% icon "edit" %}
    Edit video
  </a>
  <button class="orca-icon-button orca-icon-button--outlined" type="button" aria-label="More actions for Entrance A" aria-haspopup="menu" aria-expanded="false" aria-controls="ra-menu" data-orca-menu>
    {% icon "more" %}
  </button>
  <ul class="orca-popover orca-popover--end" role="menu" id="ra-menu" hidden>
    <li role="none">
      <button class="orca-menu__item" role="menuitem" type="button">
        {% icon "pin" %}
        Pin to dashboard
      </button>
    </li>
    <li role="none">
      <button class="orca-menu__item" role="menuitem" type="button">
        {% icon "restart" %}
        Restart stream
      </button>
    </li>
    <li role="separator" class="orca-menu__separator"></li>
    <li role="none">
      <button class="orca-menu__item orca-menu__item--danger" role="menuitem" type="button">
        {% icon "delete" %}
        Delete video
      </button>
    </li>
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

### General description

Row actions are small buttons at the end of a table row that act on that row, with extra actions in a menu.

#### Use cases

- Editing or viewing a row.
- Opening a menu of more actions.
- Acting on a row without leaving the table.

#### When not to use it

- Actions for many rows at once: use bulk selection.
- Hover-only actions: they fail on touch screens and keyboards.

#### Best practices

- Show at most two actions.
- Name the row in each button's label.
- Keep actions always visible.
- Use a quiet button style.

### When to use

- The last column of data tables.

### How to use

- `<td><div class="orca-row-actions">` with `orca-button--ghost orca-button--sm` buttons or icon buttons whose `aria-label` names the row ('Edit Entrance A').
- At most two visible actions; the rest in a menu.

#### Example: In a row

```django
<table class="orca-table" style="max-width: 32rem">
  <tbody>
    <tr>
      <td>Entrance A</td>
      <td>
        <span class="orca-status"><span class="orca-dot orca-dot--positive"></span>Online</span>
      </td>
      <td>
        <div class="orca-row-actions">
          <a class="orca-button orca-button--ghost orca-button--sm" href="#">Edit</a>
          <button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="More actions for Entrance A">
            {% icon "more" %}
          </button>
        </div>
      </td>
    </tr>
  </tbody>
</table>
```

**Classes:** `.orca-row-actions`

**Principles applied:** Practical UI L14: Reduce travel between related actions; Practical UI B05: Keep low-priority actions quieter; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Row actions

---
