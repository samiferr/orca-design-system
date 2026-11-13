# Status marks and labels

Small marks that show a condition or categorise an item. Status pairs colour with a word and, where it matters, a shape.

## Status dot

`id: status-dot` · level: primitive · source: Tangerine

A 12px round mark before a word that shows live state.

### General description

A small coloured circle next to a word showing the current state of something, such as online, offline or stopped.

#### Use cases

- Showing online or offline in a list.
- Showing running or stopped services.
- Showing enabled or disabled items.

#### When not to use it

- Statuses that need more emphasis: use a badge.
- Alerts and messages: use an alert.

#### Best practices

- Always pair the dot with a word.
- Keep the number of colours small.
- Use the same colour for the same meaning everywhere.
- Use motion only for live states, and stop it for reduced motion.

### When to use

- Online/offline, running/stopped, enabled/disabled in tables and lists.

### When not to use

- The dot alone.
- More than five distinct dot colours on one screen.

### How to use

- `<span class="orca-status"><span class="orca-dot orca-dot--positive"></span>Online</span>`.
- Tones: info, positive, caution, negative, neutral (default), purple, brand. Small: `.orca-dot--sm`.
- Live (recording, streaming): add `.orca-dot--pulse` to a negative dot; it stops for reduced motion.

#### Example: Dots

```django
<div class="orca-stack">
  <span class="orca-status"><span class="orca-dot orca-dot--positive"></span>Online</span>
  <span class="orca-status"><span class="orca-dot orca-dot--negative orca-dot--pulse"></span>Recording</span>
  <span class="orca-status"><span class="orca-dot"></span>Disabled</span>
</div>
```

**Classes:** `.orca-status`, `.orca-dot`, `.orca-dot--positive`, `.orca-dot--negative`, `.orca-dot--caution`, `.orca-dot--info`, `.orca-dot--pulse`

**Tokens:** `--orca-positive`, `--orca-caution`, `--orca-negative`, `--orca-info`, `--orca-neutral`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Miller's law: chunk information so working memory is not overloaded

**Related:** `badge`

**ORCA guide items covered:** Status dot

---

## Badge

`id: badge` · level: primitive · source: Tangerine

A compact square label with a status or category word, solid or subtle.

### General description

A small label with a short word that shows a status or category, such as Approved, Draft or New.

#### Use cases

- Showing a record's status in a table.
- Marking items as new or beta.
- Showing a plan or role.

#### When not to use it

- Filter choices people can click: use tags.
- Showing a number: use a count badge.
- Long text: use a normal label.

#### Best practices

- Use one or two words.
- Do not rely on colour alone.
- Keep colours consistent in meaning.
- Check text contrast on the background.

### When to use

- Status of a record (Approved, Failed, Draft) in tables, cards and headers.
- Category labels (Beta, New).

### When not to use

- Long text (more than three words).
- Interactive filters: use tags.
- Several solid badges in one row: use `--subtle`.

### How to use

- `<span class="orca-badge orca-badge--positive">Approved</span>`.
- Tones: `--info` (informative, action), `--positive`, `--caution`, `--negative`, default neutral grey fill, `--grey` (light neutral), `--purple` (tertiary), `--accent`, `--brand`.
- Subtle tint with dark text: add `--subtle` (info, positive, caution, negative); add a status icon inside.
- Write sentence case; badges are not uppercased and use the 12px label style.

### Accessibility

- Text in solid badges holds 4.5:1 (caution uses black text).

#### Example: Solid

```django
<div class="orca-row">
  <span class="orca-badge orca-badge--info">Informative</span>
  <span class="orca-badge orca-badge--positive">Approved</span>
  <span class="orca-badge orca-badge--caution">Pending</span>
  <span class="orca-badge orca-badge--negative">Failed</span>
  <span class="orca-badge">Draft</span>
  <span class="orca-badge orca-badge--grey">Archived</span>
  <span class="orca-badge orca-badge--purple">Beta</span>
  <span class="orca-badge orca-badge--accent">New</span>
  <span class="orca-badge orca-badge--brand">Pro</span>
</div>
```

#### Example: Subtle with icon

```django
<div class="orca-row">
  <span class="orca-badge orca-badge--subtle orca-badge--positive">
    {% icon "success" %}
    Online
  </span>
  <span class="orca-badge orca-badge--subtle orca-badge--caution">
    {% icon "warning" %}
    Degraded
  </span>
  <span class="orca-badge orca-badge--subtle orca-badge--negative">
    {% icon "error" %}
    Offline
  </span>
  <span class="orca-badge orca-badge--subtle orca-badge--info">
    {% icon "info" %}
    Updating
  </span>
</div>
```

**Classes:** `.orca-badge`, `.orca-badge--info`, `.orca-badge--positive`, `.orca-badge--caution`, `.orca-badge--negative`, `.orca-badge--grey`, `.orca-badge--purple`, `.orca-badge--accent`, `.orca-badge--brand`, `.orca-badge--subtle`

**Tokens:** `--orca-info-fill`, `--orca-positive-fill`, `--orca-caution-fill`, `--orca-negative-fill`, `--orca-neutral-fill`, `--orca-on-fill`, `--orca-on-caution`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI C03: Communicate meaning beyond colour; Practical UI C04: Reserve status colours for their meanings

**Related:** `status-dot`, `tag`, `count-badge`

**ORCA guide items covered:** Badge (information, positive, negative, caution); Badge (neutral, grey); Badge (accent, brand); Badge (action, informative); Badge (tertiary, purple)

---

## Alert icon

`id: alert-icon` · level: primitive · source: Tangerine

The status glyph at the start of an alert, callout or field message, in its left inset.

### General description

The symbol at the start of a message that shows its type, such as an error, warning or success.

#### Use cases

- Leading an alert or banner.
- Marking error and success messages in forms.
- Showing the type of a notification.

#### When not to use it

- Decoration with no meaning: leave it out.
- Showing an item's status in a list: use a status dot or badge.

#### Best practices

- Use the same symbol for the same type everywhere.
- Place it in the same spot on every message.
- Never rely on the icon alone, include text.
- Match the symbol to the colour of the message.

### When to use

- First element of every alert, callout, toast and error summary.

### How to use

- `{% status_icon "negative" %}` with `.orca-alert-icon` when placed in a flex row.
- Match the glyph to the alert tone; never change a glyph's meaning.

#### Example: Leading an alert

```django
<div class="orca-row" style="align-items: flex-start; gap: var(--orca-space-16); max-width: 30rem; padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border); border-inline-start: var(--orca-bar) solid var(--orca-caution)">
  <span class="orca-alert-icon">
    {% status_icon "caution" %}
  </span>
  <div>
    <p class="orca-alert-title">Disk almost full</p>
    <p class="orca-p">Videos older than 20 days will be deleted tonight.</p>
  </div>
</div>
```

**Classes:** `.orca-alert-icon`

**Tokens:** `--orca-negative`, `--orca-caution`, `--orca-positive`, `--orca-info`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI C03: Communicate meaning beyond colour

**Related:** `status-icon`

**ORCA guide items covered:** Alert icon

---

## Count badge

`id: count-badge` · level: primitive · source: ORCA

A small pill with a number: unread items, pending tasks.

### General description

A small circle or pill with a number showing how many items need attention, such as unread messages or open tasks.

#### Use cases

- Unread notifications on a bell icon.
- Pending items on a navigation link.
- Item totals on a tab.

#### When not to use it

- Status words: use a badge.
- Counts that never reach zero: they stop being noticed.

#### Best practices

- Cap large numbers, for example 99+.
- Hide the count when it is zero if that fits.
- Give screen readers the meaning, such as '3 unread'.
- Keep it small and placed on the corner.

### When to use

- On a notifications button, a navigation item or a tab.

### When not to use

- Counts that are always non-zero (people learn to ignore them: banner blindness).

### How to use

- `<span class="orca-count">3</span>`; red by default for 'needs attention'; `--neutral` for plain totals; `--accent`.
- On an icon button: add `.orca-has-count` to the button and put the count inside it.
- Cap at 99+: `{% if n > 99 %}99+{% else %}{{ n }}{% endif %}`.
- Give screen readers the meaning: `aria-label="Notifications, 3 unread"` on the button.

#### Example: Count on a button

```django
<div class="orca-row orca-row--16">
  <button class="orca-icon-button orca-has-count" type="button" aria-label="Notifications, 3 unread">
    {% icon "notifications" %}
    <span class="orca-count" aria-hidden="true">3</span>
  </button>
  <span>Videos <span class="orca-count orca-count--neutral">12</span></span>
</div>
```

**Classes:** `.orca-count`, `.orca-count--neutral`, `.orca-count--accent`, `.orca-has-count`

**Tokens:** `--orca-negative-fill`, `--orca-radius-pill`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Count badge

---

## Tag

`id: tag` · level: primitive · source: Tangerine

A label for a keyword or category; static, selectable (filter) or removable (chosen value).

### General description

A small label for a keyword or category. Tags can be plain, clickable to filter, or removable when they show chosen values.

#### Use cases

- Keywords on a record.
- Active filters that can be removed.
- Chosen values in a multi-select field.

#### When not to use it

- Showing a status: use a badge.
- Navigating between pages: use links or tabs.

#### Best practices

- Keep text short.
- Let people remove a tag with a clearly named button.
- Show the selected state with more than colour.
- Shorten long values and give the full text on hover.

### When to use

- Keywords on a record; filter chips; values chosen in a multi-picker.

### When not to use

- Status (use a badge).
- Tags as navigation.

### How to use

- Static: `<span class="orca-tag">North building</span>`.
- Selectable filter: `<button class="orca-tag" type="button" aria-pressed="false" data-orca-toggle>Weekdays</button>`.
- Removable: `<span class="orca-tag"><span class="orca-tag__text">Entrance A</span><button class="orca-tag__remove" type="button" aria-label="Remove Entrance A">{% icon "close" %}</button></span>`.
- Long values truncate inside the tag; give the full value in `title`.

### Accessibility

- Remove buttons name the value they remove. Selected filter tags use `aria-pressed`.

#### Example: Tags

```django
<div class="orca-row">
  <span class="orca-tag">North building</span>
  <button class="orca-tag" type="button" aria-pressed="true" data-orca-toggle>Weekdays</button>
  <button class="orca-tag" type="button" aria-pressed="false" data-orca-toggle>Weekends</button>
  <span class="orca-tag">
    <span class="orca-tag__text">Entrance A</span>
    <button class="orca-tag__remove" type="button" aria-label="Remove Entrance A">
      {% icon "close" %}
    </button>
  </span>
</div>
```

**Classes:** `.orca-tag`, `.orca-tag--selected`, `.orca-tag__remove`, `.orca-tag__text`

**Tokens:** `--orca-neutral-bg`, `--orca-accent`

**Principles applied:** Practical UI S06: Make essential content visible or discoverable; Postel's law: accept varied input, output reliable and accessible UI; Practical UI C03: Communicate meaning beyond colour

**Related:** `badge`

**ORCA guide items covered:** Tag; Selected tag; Removable tag

---
