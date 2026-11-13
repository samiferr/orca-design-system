# Identity and controls

Who is signed in, panel headers, and small controls that personalise the interface.

## User chip

`id: user-chip` · level: component · source: Tangerine

Avatar, name and role of the signed-in person; opens the account menu.

Built from: `avatar`, `dropdown-menu`

### General description

A small element in the top corner showing the signed-in person's avatar, name and role. It usually opens an account menu.

#### Use cases

- Top bars of web applications.
- Opening profile, settings and sign out.
- Showing which account is active.

#### When not to use it

- Public pages with no sign-in; show a Sign in button instead.
- Long lists of people; use a table row or card.

#### Best practices

- Place it at the top right.
- Show the name or give the button an accessible name.
- Include Sign out in the menu.
- Let it shrink to just the avatar on small screens.

### When to use

- The end of the top bar.

### How to use

- `<button class="orca-user-chip" type="button" aria-haspopup="menu" aria-expanded="false" data-orca-menu aria-controls=…>` with a small avatar and `.orca-user-chip__text` (`__name`, `__role`), inside an `.orca-anchor` with the menu.
- Menu: Profile, Settings, separator, Sign out. Below 620px only the avatar shows; the button keeps the name as its accessible name.

#### Example: User chip

```django
<div class="orca-anchor">
  <button class="orca-user-chip" type="button" aria-haspopup="menu" aria-expanded="false" aria-controls="uc-menu" data-orca-menu>
    <span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span>
    <span class="orca-user-chip__text">
      <span class="orca-user-chip__name">Ada Lovelace</span>
      <span class="orca-user-chip__role">Administrator</span>
    </span>
    {% icon "chevron-down" size="xs" %}
  </button>
  <ul class="orca-popover orca-popover--end" role="menu" id="uc-menu" hidden>
    <li role="none">
      <a class="orca-menu__item" role="menuitem" href="#">
        {% icon "user" %}
        Profile
      </a>
    </li>
    <li role="none">
      <a class="orca-menu__item" role="menuitem" href="#">
        {% icon "settings" %}
        Settings
      </a>
    </li>
    <li role="separator" class="orca-menu__separator"></li>
    <li role="none">
      <a class="orca-menu__item" role="menuitem" href="#">
        {% icon "log-out" %}
        Sign out
      </a>
    </li>
  </ul>
</div>
```

**Classes:** `.orca-user-chip`, `.orca-user-chip__text`, `.orca-user-chip__name`, `.orca-user-chip__role`

**Principles applied:** Jakob's law: work the way products people already know work; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** User chip

---

## Panel header

`id: panel-header` · level: component · source: Tangerine

A panel's top: title, short description and actions.

Built from: `panel-title`, `button`

### General description

The top row of a panel or card with its title, a short description and actions. It says what the panel shows and what can be done with it.

#### Use cases

- Dashboard panels and cards.
- Table and chart frames.
- Settings sections in a panel.

#### When not to use it

- Page titles; use a page heading.
- Panels with no title or actions; skip the header.

#### Best practices

- Keep the title short and about one topic.
- Place actions next to the title.
- Limit actions to the most useful few.
- Let actions wrap on narrow screens.

### When to use

- Every panel, table card and chart frame.

### How to use

- `<div class="orca-panel-header">` with `.orca-panel-header__text` (`h2.orca-panel-title` + `.orca-panel-header__desc`) and `.orca-panel-header__actions` (ghost or dense buttons).
- Actions wrap under the title on narrow panels.

#### Example: Panel header

```django
<div class="orca-panel-header" style="max-width: 36rem">
  <div class="orca-panel-header__text">
    <h2 class="orca-panel-title">People inside</h2>
    <p class="orca-panel-header__desc">All entrances, updated every minute</p>
  </div>
  <div class="orca-panel-header__actions">
    <button class="orca-button orca-button--ghost orca-button--dense" type="button">
      {% icon "restart" %}
      Refresh
    </button>
    <a class="orca-button orca-button--dense" href="#">Open report</a>
  </div>
</div>
```

**Classes:** `.orca-panel-header`, `.orca-panel-header__text`, `.orca-panel-header__desc`, `.orca-panel-header__actions`

**Principles applied:** Practical UI L14: Reduce travel between related actions; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Panel header

---

## Pin control

`id: pin-control` · level: component · source: Tangerine

A pin toggle that shows 'Pinned' in words and announces changes.

Built from: `pin-button`

### General description

A toggle that pins an item so it stays easy to find, for instance at the top of a list or on a dashboard. It shows whether the item is pinned.

#### Use cases

- Pinning favourites to a dashboard.
- Keeping important items at the top of a list.
- Saving shortcuts to frequently used pages.

#### When not to use it

- Marking something as done; use a checkbox.
- Saving to a personal collection; use a bookmark or favourite action.

#### Best practices

- Show the state in words as well as the icon.
- Announce the change to screen readers.
- Save at once and undo if saving fails.
- Name the item being pinned in the label.

### When to use

- Detail pages and cards of items that can be pinned to a dashboard or list top.

### How to use

- `<span class="orca-pin-control">` with a pin button (`id`, `aria-pressed`, `data-orca-toggle`, `data-orca-state-on="Pinned"`, `data-orca-state-off="Not pinned"`) and `<span class="orca-pin-control__state" data-orca-state-for="button-id">`.
- Save on the server (htmx `hx-post`); revert and show an alert if it fails.

#### Example: Pin control

```django
<span class="orca-pin-control">
  <button class="orca-icon-button orca-pin" id="pc-pin" type="button" aria-pressed="true" aria-label="Pin Entrance A to the dashboard" data-orca-toggle data-orca-state-on="Pinned" data-orca-state-off="Not pinned">
    {% icon "pin" %}
  </button>
  <span class="orca-pin-control__state" data-orca-state-for="pc-pin">Pinned</span>
</span>
```

**Classes:** `.orca-pin-control`, `.orca-pin-control__state`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Pin control

---

## Theme toggle

`id: theme-toggle` · level: component · source: Tangerine

A segmented choice of Auto, Light, Dark and Paper themes, remembered per browser.

Built from: `radio`

### General description

A control to switch the look of an interface between themes such as light and dark. It follows the system setting by default and remembers the choice.

#### Use cases

- Settings and account pages.
- Top bar shortcut for switching between light and dark.
- Reading in different lighting.

#### When not to use it

- Basic colour changes with no real need; follow the system setting.
- Sites with a single fixed look.

#### Best practices

- Offer an automatic option that follows the system setting.
- Show all choices at once.
- Remember the choice for the next visit.
- Apply it before the page appears to avoid flashes.

### When to use

- Settings panels and account settings.

### How to use

- `<fieldset class="orca-segmented" data-orca-theme-choice>` with a legend and four radio labels `.orca-segmented__item` (values auto, light, dark, paper).
- orca.js applies and remembers the theme; ORCA's head script restores it before the page paints.
- A compact top-bar alternative is the theme toggle button (`data-orca-theme-toggle`, see Themes).

#### Example: Theme choice

```django
<fieldset class="orca-segmented" data-orca-theme-choice>
  <legend class="orca-label">Theme</legend>
  <label class="orca-segmented__item"><input type="radio" name="tt-theme" value="auto" checked>Auto</label>
  <label class="orca-segmented__item">
    <input type="radio" name="tt-theme" value="light">
    {% icon "sun" %}
    Light
  </label>
  <label class="orca-segmented__item">
    <input type="radio" name="tt-theme" value="dark">
    {% icon "moon" %}
    Dark
  </label>
  <label class="orca-segmented__item"><input type="radio" name="tt-theme" value="paper">Paper</label>
</fieldset>
```

**Classes:** `.orca-segmented`, `.orca-segmented__item`

**Principles applied:** Practical UI R11: Visible choices for small sets; Tesler's law: move unavoidable complexity from the user to the system; Postel's law: accept varied input, output reliable and accessible UI

**Related:** `themes`

**ORCA guide items covered:** Theme toggle

---

## Email button (with fallback link)

`id: email-fallback` · level: component · source: Tangerine

An email button with the address shown and a Copy button, for when no mail app opens.

Built from: `email-button`, `copy-button`

### General description

An email link paired with the visible address and a Copy button. It covers people whose device has no mail app set up.

#### Use cases

- Contact and support pages.
- Sharing a report by email.
- Any link that starts an email.

#### When not to use it

- Long conversations; use a contact form or a chat tool.
- Sensitive details in the link; avoid putting personal data in it.

#### Best practices

- Show the address in plain text.
- Add a Copy button and confirm when copied.
- Prefill a clear subject line.
- Keep personal data out of the link.

### When to use

- Contact and support actions, sharing a report by email.

### How to use

- `<div class="orca-stack">` with the mailto button, then a copy button component holding the address.
- Prefill the subject with `?subject=` (URL-encoded); never put personal data in the URL.

#### Example: Email support

```django
<div class="orca-stack" style="align-items: flex-start">
  <a class="orca-button" href="mailto:support@example.com?subject=Video%20offline">
    {% icon "mail" %}
    Email support
  </a>
  <div class="orca-copy">
    <code class="orca-copy__value" id="ef-addr">support@example.com</code>
    <button class="orca-button orca-button--dense" type="button" data-orca-copy="ef-addr">
      {% icon "copy" class="orca-icon--copy" %}
      {% icon "check" class="orca-icon--copied" %}
      <span data-orca-copy-label>Copy address</span>
    </button>
  </div>
</div>
```

**Classes:** `.orca-copy`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Email button (with fallback link)

---

## Logo link

`id: logo-link` · level: component · source: ORCA

The product logo as a link to the home page.

Built from: `logo`

### General description

A logo that links to the home page. It tells people whose site they are on and gives them a quick way back to the start.

#### Use cases

- Header or top bar of a website or app.
- Footer, so people can return home after reading to the end.
- Sign-in pages and emails that carry the brand.

#### When not to use it

- Placing it next to a separate Home link that goes to the same page; keep just one.
- Using the logo as the only way to reach important sections; add real navigation.

#### Best practices

- Put it in the top left, where people look for it.
- Give the link a name that includes the brand name.
- Give the image useful alt text or use the name as text.
- Link to the home page, and skip the link when already on it.

### When to use

- Top bar, site header, footer, sign-in card, error pages and emails.

### When not to use

- A second home link beside it.

### How to use

- `{% orca_logo href="/" %}`: the brand logo (or the name as a wordmark) inside a link named after the product.
- Leave `href` empty where the page is already home, such as sign-in; the logo is then not a link.

### Accessibility

- The link is named after the product, from `settings.ORCA["BRAND"]["name"]`.

#### Example: Logo link

```django
{% orca_logo href="#" %}
```

**Classes:** `.orca-logo`

**Principles applied:** Jakob's law: work the way products people already know work; Fitts's law: big, close, well-spaced targets are faster and safer

**Related:** `top-bar`, `site-header`, `footer`

---

## Collapse toggle

`id: collapse-toggle` · level: component · source: ORCA

An icon button that collapses or expands a region and remembers the choice. Its label says what a press will do.

Built from: `icon-button`

### General description

A button that folds a panel or sidebar away and brings it back. It gives people more room for content without removing the panel.

#### Use cases

- Collapsing a sidebar menu down to icons.
- Hiding a side panel on small screens.
- Giving more width to a table or editor.

#### When not to use it

- Hiding content people need to finish a task; keep it visible instead.
- Showing or hiding a short block of text; use an accordion or disclosure.

#### Best practices

- Say what the button will do, and update the label when the state changes.
- Tell assistive technology whether the region is open with the expanded state.
- Remember the choice for the next visit.
- Keep the button in the same spot in both states.

### When to use

- The foot of a collapsible sidebar; side panels that can shrink to a rail.

### How to use

- `<button class="orca-icon-button orca-sidebar__toggle" type="button" aria-controls=… aria-expanded="true" aria-label="Collapse navigation" data-orca-sidebar-toggle>{% icon "chevron-left" %}</button>`.
- The script flips `aria-expanded`, the label and the chevron, and stores the state.

### Accessibility

- `aria-expanded` and `aria-controls` tell assistive technology what the button changes.

#### Example: Collapse toggle

```django
<button class="orca-icon-button orca-sidebar__toggle" type="button" aria-controls="ct-demo" aria-expanded="true" aria-label="Collapse navigation" data-orca-sidebar-toggle>
  {% icon "chevron-left" %}
</button>
```

**Classes:** `.orca-sidebar__toggle`

**Principles applied:** Practical UI S04: Reveal secondary information when needed; Postel's law: accept varied input, output reliable and accessible UI

**Related:** `sidebar`

---
