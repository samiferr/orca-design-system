# Actions

Things people press. One primary action per screen; everything else is quieter.

## Button

`id: button` · level: primitive · source: Tangerine

A command. Variants show importance: primary, secondary (default), ghost, link, plus brand, danger, neutral, elevated and outlines.

### General description

A control that triggers an action when pressed, such as saving a form or opening a dialog. Its style shows how important the action is.

#### Use cases

- Submitting forms and saving changes.
- Opening dialogs and starting actions.
- Confirming or cancelling a decision.

#### When not to use it

- Moving to another page: use a link.
- Several equally strong buttons on one screen: pick one primary action.

#### Best practices

- Start labels with a verb and name the result, such as 'Save image'.
- Use one primary button per screen.
- Make buttons at least 44 pixels tall on touch screens.
- Show a busy state during slow actions.
- Show disabled state with a clear reason.

### When to use

- `orca-button--primary`: the one main action of a screen or form (Save, Add image).
- default (no modifier): secondary actions and equal alternatives (Cancel, Export).
- `--ghost`: low-priority or repeated actions in toolbars and rows.
- `--danger`: only to confirm a destructive action inside a confirm dialog.
- `--brand`: the single brand moment on a marketing or onboarding screen.
- `--neutral`: filled grey for toggles and filter chips in toolbars.
- `--elevated`: a button floating over media or maps.
- `--outline-accent` / `--outline-danger`: a secondary action that needs a colour cue (a quiet first step of a delete).

### When not to use

- Navigation: use a link.
- Two primary buttons on one screen.
- A red button as the first step of a delete (B13): use the default or `--outline-danger`, confirm with `--danger`.
- 'OK', 'Submit', 'Yes': name the action.

### How to use

- `<button class="orca-button orca-button--primary" type="submit">Save image</button>`. Always set `type`.
- Label: verb + object, 1 to 3 words, sentence case (B10).
- Order: most important first, left to right; stack full width on phones (B08).
- Icon + label: put `{% icon %}` before the text; the icon is decorative.
- Busy: set `aria-busy="true"`, disable, and prepend `<span class="orca-spinner orca-spinner--sm"></span>`.
- Old aliases still work: positive = primary, negative = danger, base = ghost, secondary = default.

### Accessibility

- The focus ring is drawn inside the button; on filled variants it uses the on-fill colour so it stays visible.
- Disabled buttons cannot be focused: explain why nearby or keep the button enabled and validate on press (B06, B07).

#### Example: Weights

```django
<div class="orca-row">
  <button class="orca-button orca-button--primary" type="button">Save image</button>
  <button class="orca-button" type="button">Cancel</button>
  <button class="orca-button orca-button--ghost" type="button">
    {% icon "copy" %}
    Duplicate
  </button>
</div>
```

#### Example: Other variants

```django
<div class="orca-row">
  <button class="orca-button orca-button--brand" type="button">Start free trial</button>
  <button class="orca-button orca-button--danger" type="button">Delete image</button>
  <button class="orca-button orca-button--neutral" type="button">Neutral</button>
  <button class="orca-button orca-button--elevated" type="button">Elevated</button>
  <button class="orca-button orca-button--outline-accent" type="button">Outline accent</button>
  <button class="orca-button orca-button--outline-danger" type="button">Delete</button>
</div>
```

#### Example: Busy and disabled

```django
<div class="orca-row">
  <button class="orca-button orca-button--primary" type="button" aria-busy="true" disabled><span class="orca-spinner orca-spinner--sm" style="color: inherit"></span>Saving</button>
  <button class="orca-button" type="button" disabled>Export</button>
  <span class="orca-small orca-muted">Export is available once the run has finished.</span>
</div>
```

**Classes:** `.orca-button`, `.orca-button--primary`, `.orca-button--brand`, `.orca-button--danger`, `.orca-button--neutral`, `.orca-button--ghost`, `.orca-button--elevated`, `.orca-button--outline-accent`, `.orca-button--outline-danger`

**Tokens:** `--orca-primary`, `--orca-primary-hover`, `--orca-danger`, `--orca-brand-strong`, `--orca-border-strong`, `--orca-control-md`

**Principles applied:** Practical UI B01: Three distinguishable action weights; Practical UI B03: One primary action; Practical UI B10: Name the action clearly; Practical UI B13: Scale friction to the consequence; Hick's law: fewer, clearer choices mean faster decisions; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Fitts's law: big, close, well-spaced targets are faster and safer

**Related:** `button-size`, `icon-button`, `link-action`

**ORCA guide items covered:** Button (base, positive, negative, brand); Button (primary, brand, secondary, neutral, ghost, elevated, danger); Button outlines (accent, neutral, danger); Disabled button

---

## Button sizes

`id: button-size` · level: primitive · source: Tangerine

Size modifiers: sm, dense, default, lg, xl, plus block (full width) and icon-only.

### General description

Different heights and widths for buttons, such as small, regular and large, chosen to fit the place and the device where they appear.

#### Use cases

- Using compact buttons in tables and toolbars.
- Using large buttons for touch screens and main phone actions.
- Making a full-width button at the bottom of a form.

#### When not to use it

- Showing importance: change the button style, not its size.
- Mixing many sizes in one row: choose one size for the group.

#### Best practices

- Keep the same size for buttons in a row.
- Make touch targets at least 44 pixels.
- Match button height to nearby fields.
- Add an accessible name to icon-only buttons.

### When to use

- `--sm` in table rows; `--dense` in top bars and filter bars; default elsewhere; `--lg`/`--xl` for touch-first and phone primary actions.
- `--block` for the primary action at the bottom of a phone form.
- `--icon-only` for a square button with only an icon (prefer `icon-button`).

### When not to use

- Using size to signal importance: use the variant.
- Mixing sizes in one row.

### How to use

- Add one size modifier to `.orca-button`. On coarse pointers every size grows to 44px automatically.
- Icon-only buttons need `aria-label`.

#### Example: Sizes

```django
<div class="orca-row">
  <button class="orca-button orca-button--sm" type="button">Small</button>
  <button class="orca-button orca-button--dense" type="button">Dense</button>
  <button class="orca-button" type="button">Default</button>
  <button class="orca-button orca-button--lg" type="button">Large</button>
  <button class="orca-button orca-button--icon-only" type="button" aria-label="Refresh">
    {% icon "restart" %}
  </button>
</div>
<div style="max-width: 20rem; margin-top: var(--orca-space-16)">
  <button class="orca-button orca-button--primary orca-button--block orca-button--xl" type="button">Save image</button>
</div>
```

**Classes:** `.orca-button--sm`, `.orca-button--dense`, `.orca-button--lg`, `.orca-button--xl`, `.orca-button--block`, `.orca-button--icon-only`

**Tokens:** `--orca-control-sm`, `--orca-control-dense`, `--orca-control-md`, `--orca-control-lg`, `--orca-control-xl`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI B11: Make targets large and separated

**Related:** `button`, `control-heights`

**ORCA guide items covered:** Button sizes (small, dense, block, icon-only); Button sizes (sm, lg, xl)

---

## Link (tertiary action)

`id: link-action` · level: primitive · source: Tangerine

A text-styled button or link for the least important actions.

### General description

A button or link drawn as plain text for low-priority actions, such as 'Clear filters' or 'Show more', that should not compete with main buttons.

#### Use cases

- Clearing filters or resetting a form.
- Showing more or less content.
- Linking to related pages within a sentence.

#### When not to use it

- The main action of a screen: use a primary button.
- Actions that need strong emphasis, such as deleting: use a button with clear styling.

#### Best practices

- Underline or style it so it looks clickable.
- Name the result, never 'click here'.
- Use a real link for navigation and a button for actions.
- Keep the text short.

### When to use

- 'Show more', 'Clear filters', 'Edit' inside a sentence or summary; secondary navigation like 'Back to images'.

### When not to use

- The main action of a screen.

### How to use

- Command: `<button class="orca-button orca-button--link" type="button">Clear filters</button>`.
- Navigation: `<a class="orca-link">`.
- Name the destination or result, never 'Click here'.

#### Example: Tertiary

```django
<p class="orca-p">3 filters applied. <button class="orca-button orca-button--link" type="button">Clear filters</button></p>
```

**Classes:** `.orca-button--link`

**Tokens:** `--orca-accent`

**Principles applied:** Practical UI B01: Three distinguishable action weights; Practical UI B05: Keep low-priority actions quieter; Practical UI W14: Give links meaningful destination names

**Related:** `text-link`, `button`

**ORCA guide items covered:** Link

---

## Pin button

`id: pin-button` · level: primitive · source: Tangerine

A toggle that pins an item to the top of a list or the dashboard.

### General description

A toggle button that pins an item so it stays at the top of a list or on a dashboard. Pressing it again removes the pin.

#### Use cases

- Keeping favourite items at the top of a list.
- Adding a report or album to a dashboard.
- Marking items for quick access.

#### When not to use it

- Marking a one-off choice for a bulk action: use a checkbox.
- Rating or liking content: use a star or heart control.

#### Best practices

- Show pinned and unpinned states clearly.
- Name the item in the accessible label, such as 'Pin Entrance A'.
- Save the state on the server.
- Update the label when the state changes.

### When to use

- Lists where a few items are used far more than the rest (albums, reports).

### How to use

- `<button class="orca-icon-button orca-pin" type="button" aria-pressed="false" aria-label="Pin Entrance A" data-orca-toggle data-orca-label-on="Unpin Entrance A" data-orca-label-off="Pin Entrance A">{% icon "pin" %}</button>`.
- Save the state on the server; `data-orca-toggle` only flips the pressed state in the page.

### Accessibility

- `aria-pressed` announces pinned/not pinned; the label names the item.

#### Example: Pin toggle

```django
<button class="orca-icon-button orca-pin" type="button" aria-pressed="true" aria-label="Unpin Entrance A" data-orca-toggle data-orca-label-on="Unpin Entrance A" data-orca-label-off="Pin Entrance A">
  {% icon "pin" %}
</button>
```

**Classes:** `.orca-pin`

**Tokens:** `--orca-accent`, `--orca-bg-active`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI F03: Reduce the total effort of a task

**Related:** `toggle-button`

**ORCA guide items covered:** Pin button

---

## Email button

`id: email-button` · level: primitive · source: Tangerine

A mailto link styled as a button, with the address shown beside it.

### General description

A link that opens the user's email app with the recipient, subject and body filled in, styled as a button.

#### Use cases

- Contacting support or sales.
- Sending a link or report by email.
- Replying to an alert or notice.

#### When not to use it

- Forms that collect detailed messages: use a contact form.
- Users without a mail app: always show the address as well.

#### Best practices

- Show the email address beside the button.
- Set a helpful subject line.
- Encode special characters in the link.
- Label it with what will happen, such as 'Email support'.

### When to use

- Contact support, send a report link, reply to an alert.

### How to use

- `<a class="orca-button" href="mailto:…?subject=…">{% icon "mail" %}Email support</a>` followed by `<span class="orca-email-button__fallback">support@example.com</span>`.
- URL-encode subject and body with `urlencode`.

#### Example: Email with fallback

```django
<div>
  <a class="orca-button" href="mailto:support@example.com?subject=Video%20will%20not%20play">
    {% icon "mail" %}
    Email support
  </a>
  <span class="orca-email-button__fallback">support@example.com</span>
</div>
```

**Classes:** `.orca-email-button__fallback`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Email button

---

## Toggle button (pressed)

`id: toggle-button` · level: primitive · source: Tangerine

A button that stays pressed to show an on state.

### General description

A button that stays pressed to show something is on and pops back when pressed again, used to switch a mode or a display option.

#### Use cases

- Turning toolbar options on or off, such as grid lines or bold.
- Switching a live view or mute on and off.
- Filtering a list with an on-off chip.

#### When not to use it

- Settings that are saved and applied later: use a switch.
- Choosing one option from several: use radio buttons or a segmented control.

#### Best practices

- Keep the label the same in both states.
- Show the pressed state with more than colour.
- Tell assistive tools the pressed state.
- Make the change take effect right away.

### When to use

- Toolbar modes: show grid, bold, live view on/off, mute.

### When not to use

- Settings that are saved: use a switch.
- Choosing one of several views: use a view toggle group (segmented, phase 2).

### How to use

- `<button class="orca-button" type="button" aria-pressed="false" data-orca-toggle>`.
- Keep the label fixed ('Show grid'); the pressed state shows whether it is on.

### Accessibility

- Do not change the label when pressed unless you remove aria-pressed; both together confuse.

#### Example: Toggle

```django
<button class="orca-button orca-button--dense" type="button" aria-pressed="true" data-orca-toggle>
  {% icon "grid" %}
  Show grid
</button>
```

**Classes:** `.orca-button[aria-pressed]`

**Tokens:** `--orca-bg-active`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI C03: Communicate meaning beyond colour; Practical UI R14: Checkbox or switch according to timing

**ORCA guide items covered:** Toggle button (pressed)

---

## Icon button

`id: icon-button` · level: primitive · source: Tangerine

A square button with one 16px icon and an accessible name. Quiet, outlined, accent and neutral-fill variants.

### General description

A button that shows only an icon, used for common actions such as close, search or more options, when space is limited.

#### Use cases

- Closing dialogs and panels.
- Providing toolbar actions such as refresh or edit.
- Opening an overflow menu.

#### When not to use it

- Actions with an unfamiliar icon: use a text button.
- Destructive actions without confirmation: add a confirm step.

#### Best practices

- Give every icon button an accessible name.
- Use widely known icons.
- Make the target at least 44 pixels on touch.
- Add a tooltip when the meaning may be unclear.

### When to use

- Close, more actions, refresh, pin, previous/next and other often-used toolbar actions.

### When not to use

- Actions whose icon is not well known: use a button with a label.
- Destructive actions without confirmation.

### How to use

- `<button class="orca-icon-button" type="button" aria-label="Close">{% icon "close" %}</button>`.
- Variants: default quiet, `--outlined`, `--accent`, `--neutral`. Sizes: `--sm`, `--dense`, `--lg`.
- Add a visible tooltip with the same text when the meaning may be unclear (tooltip: phase 2).

### Accessibility

- `aria-label` is required. The icon is decorative.
- Target grows to 44px on touch.

#### Example: Variants

```django
<div class="orca-row">
  <button class="orca-icon-button" type="button" aria-label="Close">
    {% icon "close" %}
  </button>
  <button class="orca-icon-button orca-icon-button--outlined" type="button" aria-label="More actions">
    {% icon "more" %}
  </button>
  <button class="orca-icon-button orca-icon-button--accent" type="button" aria-label="Refresh">
    {% icon "restart" %}
  </button>
  <button class="orca-icon-button orca-icon-button--neutral" type="button" aria-label="Settings">
    {% icon "settings" %}
  </button>
</div>
```

**Classes:** `.orca-icon-button`, `.orca-icon-button--outlined`, `.orca-icon-button--accent`, `.orca-icon-button--neutral`

**Tokens:** `--orca-icon`, `--orca-bg-hover`, `--orca-control-md`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Hick's law: fewer, clearer choices mean faster decisions; Practical UI B11: Make targets large and separated; Practical UI B12: Balance icons and labels

**Related:** `button`, `icon`

**ORCA guide items covered:** Icon button (quiet, outlined, accent, neutral fill)

---

## Floating action button (FAB)

`id: fab` · level: primitive · source: ORCA

A large floating button for a phone screen's one create action.

### General description

A large round or pill-shaped button that floats above the page, usually at the bottom right of a phone screen, for the main action.

#### Use cases

- Creating a new item on a mobile list screen.
- Starting the main task of a mobile app.
- Keeping the primary action in reach while scrolling.

#### When not to use it

- Desktop screens: put the main action in the page header.
- Screens with several equal actions: use a regular toolbar.

#### Best practices

- Use it for one primary action only.
- Prefer an icon with a text label.
- Leave space so it does not cover content.
- Give icon-only versions an accessible name.

### When to use

- Phone layouts (below 620px) of list pages with one create action.

### When not to use

- Desktop layouts: put the action in the page head.
- More than one FAB, or anything but the primary action.

### How to use

- Icon-only: `<a class="orca-fab" href="…" aria-label="Add image">{% icon "plus" %}</a>`.
- Extended (preferred: icon + label): add `.orca-fab--extended` and visible text.
- Leave 5rem of bottom padding so the FAB never covers the last row.

### Accessibility

- Icon-only FABs need `aria-label`. The FAB is 56px.

#### Example: FAB (shown in place)

```django
<div class="orca-row orca-row--16">
  <a class="orca-fab orca-fab--static" href="#" aria-label="Add image">
    {% icon "plus" %}
  </a>
  <a class="orca-fab orca-fab--static orca-fab--extended" href="#">
    {% icon "plus" %}
    Add image
  </a>
</div>
```

**Classes:** `.orca-fab`, `.orca-fab--extended`, `.orca-fab--static`

**Tokens:** `--orca-primary`, `--orca-shadow-dragged`, `--orca-layer-sticky`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Floating action button (FAB); Extended FAB

---
