# Page frame

The parts every page sits in: headers, top bar, sidebar, footer, page head, messages, drawers and filter panels.

## Header

`id: site-header` · level: pattern · source: ORCA

The public site header: logo, a few section links and one or two actions, sticky at the top.

Built from: `logo`, `primary-navigation`, `button`

### Why

People expect the logo top-left (home) and the main sections beside it on every site (Jakob's law); one primary action keeps the next step obvious (Hick's law).

### When to use

- Public and marketing pages, documentation sites, sign-in pages.

### When not to use

- Inside the application: use the top bar.

### How to use

- `<header class="orca-site-header">` with the logo, `<nav aria-label="Main"><ul class="orca-site-header__nav">` and `.orca-site-header__actions`.
- At most 5 links; the current one gets `aria-current="page"`. On phones the links wrap under the logo.

#### Example: Header

```django
<header class="orca-site-header" style="position: static">
  {% orca_logo href="#" %}
  <nav aria-label="Main"><ul class="orca-site-header__nav"><li><a href="#" aria-current="page">Product</a></li><li><a href="#">Pricing</a></li><li><a href="#">Docs</a></li></ul></nav>
  <div class="orca-site-header__actions"><a class="orca-button orca-button--ghost" href="#">Sign in</a><a class="orca-button orca-button--brand" href="#">Start free trial</a></div>
</header>
```

**Classes:** `.orca-site-header`, `.orca-site-header__nav`, `.orca-site-header__actions`

**Principles applied:** Jakob's law: work the way products people already know work; Hick's law: fewer, clearer choices mean faster decisions; Practical UI B03: One primary action

**ORCA guide items covered:** Header

---

## Top bar

`id: top-bar` · level: pattern · source: Tangerine

The application bar: menu button, logo, main sections, search and the user's tools.

Built from: `logo`, `primary-navigation`, `utility-navigation`, `search-input`, `icon-button`

### Why

A persistent bar in the expected place anchors every page of an application (Jakob's law); dense controls keep it to 56px so content stays in view (Practical UI F03).

### When to use

- Every authenticated page of an application.

### How to use

- `<header class="orca-topbar">` with `.orca-topbar__start` (menu or sidebar toggle, logo, primary navigation) and `.orca-topbar__end` (search, utility navigation).
- `--brand` paints it in the brand colour darkened by 30% with white text (the wise_people_analyzer bar); check the brand colour reads at 4.5:1 there.
- Below 1036px the navigation and search move into the drawer; the menu button opens it.

#### Example: Default and brand

```django
<div class="orca-stack" style="gap: var(--orca-space-16)">
<header class="orca-topbar" style="position: static">
  <div class="orca-topbar__start"><button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Open menu">{% icon "menu" %}</button>{% orca_logo href="#" %}
    <nav aria-label="Main"><ul class="orca-topnav"><li><a href="#" aria-current="page">Dashboard</a></li><li><a href="#">Cameras</a></li><li><a href="#">Reports</a></li></ul></nav></div>
  <div class="orca-topbar__end"><div class="orca-search">{% icon "search" %}<input class="orca-input orca-input--dense" type="search" placeholder="Search" aria-label="Search"></div>
    <a class="orca-icon-button orca-has-count" href="#" aria-label="Notifications, 3 unread">{% icon "notifications" %}<span class="orca-count" aria-hidden="true">3</span></a>
    <button class="orca-user-chip" type="button"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span class="orca-user-chip__text"><span class="orca-user-chip__name">Ada Lovelace</span></span></button></div>
</header>
<header class="orca-topbar orca-topbar--brand" style="position: static">
  <div class="orca-topbar__start"><button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Open menu">{% icon "menu" %}</button>{% orca_logo href="#" %}</div>
  <div class="orca-topbar__end"><a class="orca-icon-button" href="#" aria-label="Help">{% icon "help" %}</a><button class="orca-user-chip" type="button"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span class="orca-user-chip__text"><span class="orca-user-chip__name">Ada Lovelace</span><span class="orca-user-chip__role">Administrator</span></span></button></div>
</header></div>
```

**Classes:** `.orca-topbar`, `.orca-topbar__start`, `.orca-topbar__end`, `.orca-topbar--brand`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI F03: Reduce the total effort of a task; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Top bar

---

## Sidebar

`id: sidebar` · level: pattern · source: Tangerine

The application's side navigation: grouped section links, collapsible to an icon rail, remembered per person.

Built from: `sidebar-link`, `nav-tree`, `icon-button`

### Why

Products with many sections need a persistent, scannable list; groups chunk it (Miller's law) and collapsing gives space back to dense screens (Tesler's law: the person decides).

### When to use

- Applications with more than about 5 sections.

### How to use

- `<div class="orca-app">` holds `<nav class="orca-sidebar" id=… aria-label="Sections">` and `<main class="orca-app__main">`.
- Sections: `.orca-sidebar__section` with an optional `.orca-sidebar__label` and side links; `.orca-sidebar__foot` holds the collapse toggle (`data-orca-sidebar-toggle aria-controls=…`).
- Collapsed (`data-collapsed="true"`): labels become visually hidden but stay readable by screen readers; the rail keeps icons. Give each link a `title` so the rail has tooltips.
- The state is remembered per sidebar in `localStorage` under `orca-sidebar:<id>`, so give the sidebar an `id`.
- Long lists (like this documentation's navigation) nest a nav tree inside a section; hide the tree when collapsed.Below 620px the sidebar hides; put the same links in a drawer opened from the top bar.

#### Example: Sidebar with collapse

```django
<div class="orca-app" style="min-height: 22rem; border: var(--orca-border-width) solid var(--orca-border)">
  <nav class="orca-sidebar" id="sb-demo" aria-label="Sections" data-collapsed="false">
    <div class="orca-sidebar__section"><ul class="orca-side-nav">
      <li><a class="orca-side-link" href="#" aria-current="page">{% icon "home" %}<span class="orca-side-link__label">Dashboard</span></a></li>
      <li><a class="orca-side-link" href="#">{% icon "snapshot" %}<span class="orca-side-link__label">Cameras</span><span class="orca-count orca-count--neutral">12</span></a></li>
      <li><a class="orca-side-link" href="#">{% icon "statistics" %}<span class="orca-side-link__label">Reports</span></a></li></ul></div>
    <div class="orca-sidebar__section"><p class="orca-sidebar__label">Admin</p><ul class="orca-side-nav"><li><a class="orca-side-link" href="#">{% icon "user" %}<span class="orca-side-link__label">Users</span></a></li><li><a class="orca-side-link" href="#">{% icon "settings" %}<span class="orca-side-link__label">Settings</span></a></li></ul></div>
    <div class="orca-sidebar__foot"><button class="orca-icon-button orca-sidebar__toggle" type="button" aria-controls="sb-demo" aria-expanded="true" aria-label="Collapse navigation" data-orca-sidebar-toggle>{% icon "chevron-left" %}</button></div>
  </nav>
  <main class="orca-app__main"><h1 class="orca-page-title">Dashboard</h1></main>
</div>
```

**Classes:** `.orca-app`, `.orca-app__main`, `.orca-sidebar`, `.orca-sidebar__section`, `.orca-sidebar__label`, `.orca-sidebar__foot`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Tesler's law: move unavoidable complexity from the user to the system; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Sidebar

---

## Footer

`id: footer` · level: pattern · source: ORCA

The bottom of public pages: link columns, legal text and version.

Built from: `text-link`, `logo`, `small-text`

### Why

People look at the bottom for legal, contact and help links (Jakob's law); grouping them in titled columns makes them findable (Miller's law).

### When to use

- Public and documentation sites; a slim version (legal and version only) in applications.

### How to use

- `<footer class="orca-footer">` with `.orca-footer__cols` of `<ul class="orca-footer__col">` (first item `.orca-footer__col-title`) and `.orca-footer__legal`.

#### Example: Footer

```django
<footer class="orca-footer">
  {% orca_logo href="" %}
  <div class="orca-footer__cols">
    <ul class="orca-footer__col"><li class="orca-footer__col-title">Product</li><li><a href="#">Features</a></li><li><a href="#">Pricing</a></li></ul>
    <ul class="orca-footer__col"><li class="orca-footer__col-title">Help</li><li><a href="#">Documentation</a></li><li><a href="#">Contact support</a></li></ul>
  </div>
  <p class="orca-footer__legal">© 2026 Acme · <a href="#">Privacy</a> · <a href="#">Terms</a> · Version 0.3.0</p>
</footer>
```

**Classes:** `.orca-footer`, `.orca-footer__cols`, `.orca-footer__col`, `.orca-footer__col-title`, `.orca-footer__legal`

**Principles applied:** Jakob's law: work the way products people already know work; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Footer

---

## Page head

`id: page-head` · level: pattern · source: Tangerine

The top of a page's content: breadcrumbs or back link, title, subtitle, meta and the page's actions.

Built from: `page-title`, `page-subtitle`, `breadcrumbs`, `button`, `create-button`

### Why

One consistent head answers 'where am I, what is this, what can I do here' before anything else (Jakob's law); one primary action keeps the priority clear (Practical UI B03).

### When to use

- The top of every application page.

### How to use

- `<div class="orca-page-head">` with `.orca-page-head__text` (breadcrumbs or back link, `h1.orca-page-title`, `.orca-page-subtitle`, `.orca-page-head__meta`) and `.orca-page-head__actions`.
- Actions: secondary buttons first, the primary (or the create button) last; on phones they stretch full width.

#### Example: Page head

```django
<div class="orca-page-head">
  <div class="orca-page-head__text"><nav class="orca-breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="#">Sites</a></li><li><span aria-current="page">North building</span></li></ol></nav>
    <h1 class="orca-page-title">Cameras</h1><p class="orca-page-subtitle">Every camera counting at North building.</p>
    <p class="orca-page-head__meta"><span class="orca-status"><span class="orca-dot orca-dot--positive"></span>11 online</span><span class="orca-status"><span class="orca-dot orca-dot--negative"></span>1 offline</span></p></div>
  <div class="orca-page-head__actions"><button class="orca-button" type="button">{% icon "upload" %}Export</button><a class="orca-button orca-button--primary orca-create orca-create--static" href="#">{% icon "plus" %}Add camera</a></div>
</div>
```

**Classes:** `.orca-page-head`, `.orca-page-head__text`, `.orca-page-head__meta`, `.orca-page-head__actions`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI B03: One primary action; Practical UI L03: Establish an order of importance

**ORCA guide items covered:** Page head

---

## Messages region

`id: messages-region` · level: pattern · source: Tangerine

The place under the page head where results of the last action appear, announced politely.

Built from: `flash-message`, `alert`

### Why

Results always in the same place are found at once (Jakob's law); a live region announces them to screen-reader users (Postel's law).

### When to use

- Every page, in the base template, between the page head and the content.

### How to use

- `<div class="orca-messages-region" aria-live="polite">{% templatetag openblock %} orca_messages {% templatetag closeblock %}</div>`; errors inside use `role="alert"`.
- Toasts float elsewhere; this region holds messages that must stay until read.

#### Example: Region

```django
<div class="orca-messages-region" aria-live="polite"><div class="orca-messages">
  <div class="orca-alert orca-alert--positive" role="status">{% status_icon "positive" %}<p class="orca-alert__body">Camera “Gate 1” added. Draw its zones next.</p><button class="orca-icon-button orca-icon-button--dense orca-alert__close" type="button" aria-label="Dismiss message" data-orca-dismiss>{% icon "close" %}</button></div>
</div></div>
```

**Classes:** `.orca-messages-region`, `.orca-messages`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Messages region

---

## Drawer

`id: drawer` · level: pattern · source: Tangerine

A panel that slides over the page from one edge, built on the native dialog.

Built from: `drawer-backdrop`, `dialog-title`, `icon-button`, `button`

### Why

A drawer keeps the page in view behind it, for tasks that refer to the page (Practical UI L14); the native dialog traps focus and closes with Escape (Postel's law).

### When to use

- Navigation on phones, filters, details of a selected row, quick settings.

### When not to use

- Long forms: use a page.

### How to use

- `<dialog class="orca-drawer" id=… aria-labelledby=… data-orca-light-dismiss>` with `.orca-drawer__header` (title + close), `.orca-drawer__body`, `.orca-drawer__footer`.
- Open with `data-orca-dialog-open="id"`; `--left` for navigation. A click on the backdrop closes it.

#### Example: Details drawer

```django
<button class="orca-button" type="button" data-orca-dialog-open="dr-demo">Show camera details</button>
<dialog class="orca-drawer" id="dr-demo" aria-labelledby="dr-demo-t" data-orca-light-dismiss>
  <div class="orca-drawer__header"><h2 class="orca-dialog-title" id="dr-demo-t">Entrance A</h2><button class="orca-icon-button" type="button" aria-label="Close" data-orca-dialog-close>{% icon "close" %}</button></div>
  <div class="orca-drawer__body"><dl class="orca-kv orca-kv--stacked"><div><dt>Status</dt><dd>Online</dd></div><div><dt>Today</dt><dd>4,812 visitors</dd></div></dl></div>
  <div class="orca-drawer__footer"><a class="orca-button orca-button--primary" href="#">Open camera</a><button class="orca-button" type="button" data-orca-dialog-close>Close</button></div>
</dialog>
```

**Classes:** `.orca-drawer`, `.orca-drawer--left`, `.orca-drawer__header`, `.orca-drawer__body`, `.orca-drawer__footer`

**Principles applied:** Practical UI L14: Reduce travel between related actions; Postel's law: accept varied input, output reliable and accessible UI; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Drawer

---

## Top actions header

`id: top-actions-header` · level: pattern · source: Tangerine

A thin row above a detail or form page: back link on one side, the page's actions on the other.

Built from: `back-link`, `record-actions`

### Why

Putting the way back and the actions on the same line saves height and keeps them at the top where people look first (Fitts's law, Practical UI B09).

### When to use

- Detail and form pages reached from a list, especially on tablets and phones.

### How to use

- `<div class="orca-top-actions">` with a back link and `.orca-top-actions__end` (record actions).

#### Example: Top actions

```django
<div class="orca-top-actions"><a class="orca-back-link" href="#">{% icon "chevron-left" size="xs" %}Back to cameras</a><div class="orca-top-actions__end"><a class="orca-button orca-button--dense" href="#">{% icon "edit" %}Edit</a><button class="orca-icon-button orca-icon-button--dense orca-icon-button--outlined" type="button" aria-label="More actions">{% icon "more" %}</button></div></div>
```

**Classes:** `.orca-top-actions`, `.orca-top-actions__end`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI B09: Position multi-step navigation carefully

**ORCA guide items covered:** Top actions header (back link + actions)

---

## Settings panel

`id: settings-panel` · level: pattern · source: Tangerine

Display preferences in groups: theme and density, with a live result. ORCA has one appearance (Tangerine) and brand colours set by the project.

Built from: `theme-toggle`, `switch`, `settings-toggle`

### Why

People adapt the interface to their eyes and work (Tesler's law); grouping preferences and applying them at once confirms each choice (Doherty threshold).

### When to use

- A drawer or popover opened by the settings toggle; an account preferences page.

### How to use

- `<div class="orca-settings-panel">` of `<fieldset class="orca-settings-panel__group">`: the theme toggle (Auto, Light, Dark, Paper), and switches for personal preferences such as reduced motion or compact tables.
- Apply immediately and remember per person. Brand colour, accent and rounding are project settings (brand tokens), not personal ones: ORCA keeps one shape language.

#### Example: Panel

```django
<div class="orca-settings-panel" style="max-width: 24rem">
  <fieldset class="orca-segmented orca-settings-panel__group" data-orca-theme-choice style="flex-direction: row"><legend>Theme</legend>
    <label class="orca-segmented__item"><input type="radio" name="sp-theme" value="auto" checked>Auto</label><label class="orca-segmented__item"><input type="radio" name="sp-theme" value="light">Light</label><label class="orca-segmented__item"><input type="radio" name="sp-theme" value="dark">Dark</label><label class="orca-segmented__item"><input type="radio" name="sp-theme" value="paper">Paper</label></fieldset>
  <fieldset class="orca-settings-panel__group"><legend>Tables</legend><label class="orca-switch"><input type="checkbox" role="switch"><span class="orca-switch__track"></span><span>Compact rows</span></label></fieldset>
</div>
```

**Classes:** `.orca-settings-panel`, `.orca-settings-panel__group`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI R14: Checkbox or switch according to timing

**ORCA guide items covered:** Settings panel (appearance, theme, accent, rounding, card shadow)

---

## Filter panel

`id: filter-panel` · level: pattern · source: Tangerine

Filters in labelled groups beside a list, with the number of results and Clear all.

Built from: `choice-group`, `checkbox`, `link-action`, `search-field`

### Why

Seeing all filters and the result count at once lets people narrow a list confidently (Miller's law, Doherty threshold); grouping keeps a long set of filters scannable.

### When to use

- Lists and catalogues on wide screens with several filter dimensions.

### How to use

- `<div class="orca-with-filters">` holding `<form class="orca-filter-panel" method="get" aria-label="Filters">` and the list.
- Head: 'Filters' and a Clear all link; then `<fieldset class="orca-filter-panel__group">` per dimension with checkbox lists; apply on change (htmx or `data-orca-autosubmit`) and announce the count.
- Below 1036px the panel hides; the same form goes in the filter drawer.

#### Example: Panel

```django
<form class="orca-filter-panel" method="get" aria-label="Filters" style="max-width: 15rem" onsubmit="return false">
  <div class="orca-filter-panel__head"><span class="orca-panel-title">Filters</span><button class="orca-button orca-button--link" type="reset">Clear all</button></div>
  <fieldset class="orca-filter-panel__group"><legend>Status</legend><div class="orca-choice-group__items">
    <label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Online <span class="orca-muted">11</span></label>
    <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Offline <span class="orca-muted">1</span></label></div></fieldset>
  <fieldset class="orca-filter-panel__group"><legend>Site</legend><div class="orca-choice-group__items">
    <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>North building</label><label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Warehouse</label></div></fieldset>
  <p class="orca-small orca-muted" role="status">11 cameras match</p>
</form>
```

**Classes:** `.orca-with-filters`, `.orca-filter-panel`, `.orca-filter-panel__head`, `.orca-filter-panel__group`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI S04: Reveal secondary information when needed

**ORCA guide items covered:** Filter panel

---

## Filter drawer

`id: filter-drawer` · level: pattern · source: Tangerine

The filter panel in a drawer, with Apply and Clear, for phones and narrow screens.

Built from: `filter-button`, `drawer-backdrop`, `button`

### Why

On small screens filters must not push the results away; a drawer shows them on demand (Practical UI S04) and an explicit Apply avoids reloading on every tap (Doherty threshold).

### When to use

- Below 1036px, or whenever filters do not fit beside the list.

### How to use

- A filter button (with the active count) opens a `<dialog class="orca-drawer">` containing the filter panel form.
- Footer: 'Show 11 cameras' (primary, the count updates live) and 'Clear all'.

#### Example: Drawer

```django
<button class="orca-button" type="button" data-orca-dialog-open="fd-demo">{% icon "filter" %}Filters<span class="orca-count orca-count--accent" aria-hidden="true">1</span><span class="orca-sr-only">, 1 active</span></button>
<dialog class="orca-drawer" id="fd-demo" aria-labelledby="fd-demo-t" data-orca-light-dismiss><form method="dialog" style="display: contents">
  <div class="orca-drawer__header"><h2 class="orca-dialog-title" id="fd-demo-t">Filters</h2><button class="orca-icon-button" type="button" aria-label="Close" data-orca-dialog-close>{% icon "close" %}</button></div>
  <div class="orca-drawer__body orca-filter-panel"><fieldset class="orca-filter-panel__group"><legend>Status</legend><div class="orca-choice-group__items"><label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Online</label><label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Offline</label></div></fieldset></div>
  <div class="orca-drawer__footer"><button class="orca-button orca-button--primary" type="submit" value="apply">Show 11 cameras</button><button class="orca-button orca-button--ghost" type="reset">Clear all</button></div>
</form></dialog>
```

**Classes:** `.orca-drawer`, `.orca-filter-panel`

**Principles applied:** Practical UI S04: Reveal secondary information when needed; Doherty threshold: respond within 400 ms; show progress for anything slower; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Filter drawer

---
