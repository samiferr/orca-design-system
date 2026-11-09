# Identity and controls

Who is signed in, what a panel is, and the small controls that personalise the interface.

## User chip

`id: user-chip` · level: component · source: Tangerine

Avatar, name and role of the signed-in person; opens the account menu.

Built from: `avatar`, `dropdown-menu`

### Why

Showing who is signed in, in the familiar top-right place, prevents acting under the wrong account (Jakob's law, Peak–end rule).

### When to use

- The end of the top bar.

### How to use

- `<button class="orca-user-chip" type="button" aria-haspopup="menu" aria-expanded="false" data-orca-menu aria-controls=…>` with a small avatar and `.orca-user-chip__text` (`__name`, `__role`), inside an `.orca-anchor` with the menu.
- Menu items: Profile, Settings, separator, Sign out. Below 620px only the avatar shows; the button keeps the name as its accessible name.

#### Example: User chip

```django
<div class="orca-anchor">
  <button class="orca-user-chip" type="button" aria-haspopup="menu" aria-expanded="false" aria-controls="uc-menu" data-orca-menu><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span class="orca-user-chip__text"><span class="orca-user-chip__name">Ada Lovelace</span><span class="orca-user-chip__role">Administrator</span></span>{% icon "chevron-down" size="xs" %}</button>
  <ul class="orca-popover orca-popover--end" role="menu" id="uc-menu" hidden>
    <li role="none"><a class="orca-menu__item" role="menuitem" href="#">{% icon "user" %}Profile</a></li>
    <li role="none"><a class="orca-menu__item" role="menuitem" href="#">{% icon "settings" %}Settings</a></li>
    <li role="separator" class="orca-menu__separator"></li>
    <li role="none"><a class="orca-menu__item" role="menuitem" href="#">{% icon "log-out" %}Sign out</a></li>
  </ul>
</div>
```

**Classes:** `.orca-user-chip`, `.orca-user-chip__text`, `.orca-user-chip__name`, `.orca-user-chip__role`

**Principles applied:** Jakob's law: work the way products people already know work; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** User chip

---

## Panel header

`id: panel-header` · level: component · source: Tangerine

The top of a panel: title, a short description and the panel's actions.

Built from: `panel-title`, `button`

### Why

Each panel answers one question; naming it and placing its actions beside the name keeps controls next to what they change (Practical UI L14, Miller's law).

### When to use

- Every panel, table card and chart frame.

### How to use

- `<div class="orca-panel-header">` with `.orca-panel-header__text` (`h2.orca-panel-title` + `.orca-panel-header__desc`) and `.orca-panel-header__actions` (ghost or dense buttons).
- Actions wrap under the title on narrow panels.

#### Example: Panel header

```django
<div class="orca-panel-header" style="max-width: 36rem"><div class="orca-panel-header__text"><h2 class="orca-panel-title">People inside</h2><p class="orca-panel-header__desc">All entrances, updated every minute</p></div>
  <div class="orca-panel-header__actions"><button class="orca-button orca-button--ghost orca-button--dense" type="button">{% icon "restart" %}Refresh</button><a class="orca-button orca-button--dense" href="#">Open report</a></div></div>
```

**Classes:** `.orca-panel-header`, `.orca-panel-header__text`, `.orca-panel-header__desc`, `.orca-panel-header__actions`

**Principles applied:** Practical UI L14: Reduce travel between related actions; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Panel header

---

## Pin control

`id: pin-control` · level: component · source: Tangerine

A pin toggle with a visible 'Pinned' state and an announcement when it changes.

Built from: `pin-button`

### Why

Pinning changes where an item appears; saying so in words and announcing it confirms the action for everyone (Doherty threshold, C03).

### When to use

- Detail pages and cards of items that can be pinned to a dashboard or list top.

### How to use

- `<span class="orca-pin-control">` with a pin button (`id`, `aria-pressed`, `data-orca-toggle`, `data-orca-state-on="Pinned"`, `data-orca-state-off="Not pinned"`) and `<span class="orca-pin-control__state" data-orca-state-for="button-id">`.
- Save on the server (htmx `hx-post`); revert and show an alert if it fails.

#### Example: Pin control

```django
<span class="orca-pin-control"><button class="orca-icon-button orca-pin" id="pc-pin" type="button" aria-pressed="true" aria-label="Pin Entrance A to the dashboard" data-orca-toggle data-orca-state-on="Pinned" data-orca-state-off="Not pinned">{% icon "pin" %}</button><span class="orca-pin-control__state" data-orca-state-for="pc-pin">Pinned</span></span>
```

**Classes:** `.orca-pin-control`, `.orca-pin-control__state`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Pin control

---

## Theme toggle

`id: theme-toggle` · level: component · source: Tangerine

A segmented choice of Auto, Light, Dark and Paper themes, remembered per browser.

Built from: `radio`

### Why

People choose a theme for their eyes and surroundings; showing all options at once is clearer than a cycling button (Practical UI R11), and Auto respects the system setting by default (Tesler's law).

### When to use

- Settings panels and account settings.

### How to use

- `<fieldset class="orca-segmented" data-orca-theme-choice>` with a legend and four radio labels `.orca-segmented__item` (values auto, light, dark, paper).
- orca.js applies the theme at once and remembers it; ORCA's head script restores it before the page paints.
- A compact top-bar alternative is the theme toggle button (`data-orca-theme-toggle`, see Themes).

#### Example: Theme choice

```django
<fieldset class="orca-segmented" data-orca-theme-choice><legend class="orca-label">Theme</legend>
  <label class="orca-segmented__item"><input type="radio" name="tt-theme" value="auto" checked>Auto</label>
  <label class="orca-segmented__item"><input type="radio" name="tt-theme" value="light">{% icon "sun" %}Light</label>
  <label class="orca-segmented__item"><input type="radio" name="tt-theme" value="dark">{% icon "moon" %}Dark</label>
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

### Why

mailto links fail silently on many setups; showing the address with a Copy button guarantees a way through (Postel's law, Peak–end rule).

### When to use

- Contact and support actions, sharing a report by email.

### How to use

- `<div class="orca-stack">` with the mailto button, then a copy button component holding the address.
- Prefill the subject with `?subject=` (URL-encoded); never put personal data in the URL.

#### Example: Email support

```django
<div class="orca-stack" style="align-items: flex-start">
  <a class="orca-button" href="mailto:support@example.com?subject=Video%20offline">{% icon "mail" %}Email support</a>
  <div class="orca-copy"><code class="orca-copy__value" id="ef-addr">support@example.com</code><button class="orca-button orca-button--dense" type="button" data-orca-copy="ef-addr">{% icon "copy" class="orca-icon--copy" %}{% icon "check" class="orca-icon--copied" %}<span data-orca-copy-label>Copy address</span></button></div>
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

### Why

People expect the logo to take them home (Jakob's law); one component makes it the same link with the same accessible name in the top bar, the site header, the footer, sign-in and emails.

### When to use

- Top bar, site header, footer, sign-in card, error pages and emails.

### When not to use

- A second home link next to it with the same destination.

### How to use

- `{% orca_logo href="/" %}`: the brand logo (or the name as a wordmark) inside a link named after the product.
- Leave `href` empty where the page is already home, such as the sign-in page; the logo is then not a link.

### Accessibility

- The link's accessible name is the product name from `settings.ORCA["BRAND"]["name"]`.

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

An icon button that collapses or expands a region, says which it will do, and remembers the choice.

Built from: `icon-button`

### Why

A collapsible region gives space back without losing the way back (Practical UI S04); the button's name changes with the state so it never lies about what a press will do (Postel's law).

### When to use

- The foot of a collapsible sidebar; side panels that can shrink to a rail.

### How to use

- `<button class="orca-icon-button orca-sidebar__toggle" type="button" aria-controls=… aria-expanded="true" aria-label="Collapse navigation" data-orca-sidebar-toggle>{% icon "chevron-left" %}</button>`.
- The script flips `aria-expanded`, the label and the chevron, and stores the state.

### Accessibility

- `aria-expanded` and `aria-controls` tell assistive technology what the button changes.

#### Example: Collapse toggle

```django
<button class="orca-icon-button orca-sidebar__toggle" type="button" aria-controls="ct-demo" aria-expanded="true" aria-label="Collapse navigation" data-orca-sidebar-toggle>{% icon "chevron-left" %}</button>
```

**Classes:** `.orca-sidebar__toggle`

**Principles applied:** Practical UI S04: Reveal secondary information when needed; Postel's law: accept varied input, output reliable and accessible UI

**Related:** `sidebar`

---
