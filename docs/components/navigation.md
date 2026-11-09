# Navigation

How people move between places and pages. The current location is always marked with aria-current and a shape, not only colour.

## Primary navigation

`id: primary-navigation` · level: component · source: ORCA

The top-bar links to the main sections of the product.

Built from: `text-link`

### Why

A short, always-visible set of sections in the familiar top position lets people know where they are and where they can go (Jakob's law); the 3px bar marks the current section without colour alone (C03).

### When to use

- Products with 2 to about 6 top-level sections, in the top bar.

### When not to use

- More sections: use the sidebar.

### How to use

- `<nav aria-label="Main"><ul class="orca-topnav">` with links; the current section's link gets `aria-current="page"` (or `"true"` for a section).
- Labels are nouns people use: 'Cameras', 'Reports'. Icons optional, never alone.
- Below 1036px move the links into the sidebar drawer (pattern level).

#### Example: Top-bar links

```django
<nav aria-label="Main"><ul class="orca-topnav" style="min-height: var(--orca-nav-height)">
  <li><a href="#" aria-current="page">Dashboard</a></li><li><a href="#">Cameras</a></li><li><a href="#">Reports</a></li><li><a href="#">Alerts</a></li>
</ul></nav>
```

**Classes:** `.orca-topnav`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI C03: Communicate meaning beyond colour; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Primary navigation

---

## Utility navigation

`id: utility-navigation` · level: component · source: ORCA

Help, notifications and the user chip at the end of the top bar.

Built from: `icon-button`, `count-badge`, `avatar`

### Why

Account and help live in the top-right corner of almost every product (Jakob's law); grouping them separates personal tools from sections (Miller's law).

### When to use

- The end of the top bar, in every authenticated page.

### How to use

- `<ul class="orca-utility-nav">` with icon buttons (each with `aria-label`; the notifications one with a count) and the user chip.
- Use dense icon buttons on desktop; they grow to 44px on touch.

#### Example: Utility links

```django
<ul class="orca-utility-nav">
  <li><a class="orca-icon-button" href="#" aria-label="Help">{% icon "help" %}</a></li>
  <li><a class="orca-icon-button orca-has-count" href="#" aria-label="Notifications, 3 unread">{% icon "notifications" %}<span class="orca-count" aria-hidden="true">3</span></a></li>
  <li><button class="orca-user-chip" type="button" aria-haspopup="menu" aria-expanded="false"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span class="orca-user-chip__text"><span class="orca-user-chip__name">Ada Lovelace</span><span class="orca-user-chip__role">Administrator</span></span></button></li>
</ul>
```

**Classes:** `.orca-utility-nav`

**Principles applied:** Jakob's law: work the way products people already know work; Miller's law: chunk information so working memory is not overloaded

**Related:** `user-chip`

**ORCA guide items covered:** Utility navigation

---

## Sidebar link

`id: sidebar-link` · level: component · source: Tangerine

One destination in the side navigation: icon, label and an optional count.

Built from: `icon`, `count-badge`

### Why

A consistent row (icon, label, count) is scanned quickly and its full width is the target (Fitts's law); the current page gets a fill and a 3px bar.

### When to use

- Every item of the sidebar.

### How to use

- `<a class="orca-side-link" href=…>{% icon … %}<span class="orca-side-link__label">Cameras</span><span class="orca-count orca-count--neutral">12</span></a>` inside `<ul class="orca-side-nav">`.
- `aria-current="page"` on the current link; `--l2` for a nested link.
- Labels never wrap; a long one is cut with an ellipsis and has a `title`.

#### Example: Side links

```django
<nav aria-label="Sections" style="max-width: 15rem; background: var(--orca-bg-alt)"><ul class="orca-side-nav">
  <li><a class="orca-side-link" href="#">{% icon "home" %}<span class="orca-side-link__label">Dashboard</span></a></li>
  <li><a class="orca-side-link" href="#" aria-current="page">{% icon "snapshot" %}<span class="orca-side-link__label">Cameras</span><span class="orca-count orca-count--neutral">12</span></a></li>
  <li><a class="orca-side-link orca-side-link--l2" href="#"><span class="orca-side-link__label">Recorders</span></a></li>
  <li><a class="orca-side-link" href="#">{% icon "notifications" %}<span class="orca-side-link__label">Alerts</span><span class="orca-count">3</span></a></li>
</ul></nav>
```

**Classes:** `.orca-side-nav`, `.orca-side-link`, `.orca-side-link__label`, `.orca-side-link--l2`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI C03: Communicate meaning beyond colour; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Sidebar link

---

## Breadcrumbs

`id: breadcrumbs` · level: component · source: ORCA

The path from the top of the hierarchy to the current page.

Built from: `text-link`, `chevron-separator`

### Why

Breadcrumbs show where a page sits and offer one-click routes upward (Jakob's law); the list structure is announced as 'list, 3 items'.

### When to use

- Pages two or more levels deep in a hierarchy (Site › Building › Camera).

### When not to use

- Flat products, or as a substitute for a back link on a linear flow.

### How to use

- `<nav class="orca-breadcrumbs" aria-label="Breadcrumb"><ol>` with links, the last item a `<span aria-current="page">`.
- Separators come from CSS and mirror in right-to-left languages.
- On phones, show only the parent as a back link if space is short.

#### Example: Breadcrumbs

```django
<nav class="orca-breadcrumbs" aria-label="Breadcrumb"><ol>
  <li><a href="#">Sites</a></li><li><a href="#">North building</a></li><li><span aria-current="page">Entrance A</span></li>
</ol></nav>
```

**Classes:** `.orca-breadcrumbs`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Breadcrumbs

---

## Pagination

`id: pagination` · level: component · source: ORCA

Previous, page numbers with gaps, next, and a summary of what is shown.

Built from: `pagination-gap`, `icon`

### Why

Numbered pages tell people how much there is and let them jump (Miller's law); gaps keep the control short (Hick's law); big targets avoid mis-taps (Fitts's law).

### When to use

- Lists and tables with more than one page of results.

### When not to use

- Feeds people read continuously: use 'Load more'.

### How to use

- Django: `{% orca_pagination page_obj noun="cameras" %}` keeps the other query parameters (filters, sort).
- Markup: `<nav class="orca-pagination" aria-label="Pages"><ul>` of `.orca-page-link` links; current with `aria-current="page"`; disabled ends with `aria-disabled="true"`; gaps are `.orca-page-gap`.
- Each link is a page-link: number links carry `aria-label="Page 7"`.

#### Example: Pagination

```django
<nav class="orca-pagination" aria-label="Pages"><ul>
  <li><a class="orca-page-link" href="#" rel="prev">{% icon "chevron-left" %}<span>Previous</span></a></li>
  <li><a class="orca-page-link" href="#" aria-label="Page 1">1</a></li><li><span class="orca-page-gap" aria-hidden="true">…</span></li>
  <li><a class="orca-page-link" href="#" aria-label="Page 6">6</a></li><li><a class="orca-page-link" href="#" aria-current="page" aria-label="Page 7, current">7</a></li><li><a class="orca-page-link" href="#" aria-label="Page 8">8</a></li>
  <li><span class="orca-page-gap" aria-hidden="true">…</span></li><li><a class="orca-page-link" href="#" aria-label="Page 16">16</a></li>
  <li><a class="orca-page-link" href="#" rel="next"><span>Next</span>{% icon "chevron-right" %}</a></li>
</ul></nav>
```

**Classes:** `.orca-pagination`, `.orca-page-link`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Hick's law: fewer, clearer choices mean faster decisions; Fitts's law: big, close, well-spaced targets are faster and safer

**Related:** `pagination-summary`, `table-pager`

**ORCA guide items covered:** Pagination; Pagination link

---

## Pagination summary

`id: pagination-summary` · level: component · source: ORCA

'Showing 121–140 of 312 cameras': what part of the list is on screen.

Built from: `tabular-number`

### Why

A count anchors people in a long list and confirms filters worked (Miller's law, Peak–end rule).

### When to use

- Under or above any paginated list, and alone when there is a single page.

### How to use

- `<p class="orca-pagination-summary">Showing 121–140 of 312 cameras</p>`, with an en dash and grouping separators.
- Zero results: 'No cameras match these filters' and an empty state below.

#### Example: Summary

```django
<p class="orca-pagination-summary">Showing 121–140 of 312 cameras</p>
```

**Classes:** `.orca-pagination-summary`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Pagination summary

---

## Table pager

`id: table-pager` · level: component · source: ORCA

A compact pager under a table: rows per page, the range shown, previous and next.

Built from: `select`, `icon-button`, `pagination-summary`

### Why

Dense data screens need paging in a small space near the rows (Practical UI L14) and a choice of page size for different tasks (Tesler's law).

### When to use

- The footer of data tables and table cards.

### How to use

- `<div class="orca-table-pager">`: a label with a dense select of sizes (20, 50, 100), the range summary, and `.orca-table-pager__nav` with two icon buttons.
- Disable previous on the first page and next on the last; keep sizes small to keep pages fast.

#### Example: Pager

```django
<div class="orca-table-pager" style="border: var(--orca-border-width) solid var(--orca-border)">
  <label>Rows per page <select class="orca-select orca-select--dense"><option>20</option><option selected>50</option><option>100</option></select></label>
  <span class="orca-num">51–100 of 312</span>
  <span class="orca-table-pager__nav"><a class="orca-icon-button orca-icon-button--dense" href="#" aria-label="Previous page">{% icon "chevron-left" %}</a><a class="orca-icon-button orca-icon-button--dense" href="#" aria-label="Next page">{% icon "chevron-right" %}</a></span>
</div>
```

**Classes:** `.orca-table-pager`, `.orca-table-pager__nav`

**Principles applied:** Practical UI L14: Reduce travel between related actions; Tesler's law: move unavoidable complexity from the user to the system; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Table pager

---

## Tab bar

`id: tab-bar` · level: component · source: Tangerine

Tabs that switch between views of the same object, in place or by page.

Built from: `focus-ring`, `count-badge`, `text-link`

### Why

Tabs split related content into chunks people can switch between without losing context (Miller's law); the convention is universal (Jakob's law).

### When to use

- Two to about seven views of one thing: Overview, Zones, Recordings.

### When not to use

- Steps of a process: use steps.
- Unrelated destinations: use navigation.

### How to use

- In-page: `<div class="orca-tabs"><div class="orca-tabs__list" role="tablist" data-orca-tabs aria-label=…>` of `<button class="orca-tab" role="tab" aria-selected aria-controls>`; panels `role="tabpanel"` with `hidden`.
- By page (server-rendered): `<nav class="orca-tabs__list">` of `<a class="orca-tab" aria-current="page">` links.
- orca.js adds arrow keys, Home and End. On narrow screens the list scrolls sideways.

#### Example: In-page tabs

```django
<div class="orca-tabs">
  <div class="orca-tabs__list" role="tablist" aria-label="Camera" data-orca-tabs>
    <button class="orca-tab" role="tab" type="button" id="tb-1" aria-controls="tp-1" aria-selected="true">Overview</button>
    <button class="orca-tab" role="tab" type="button" id="tb-2" aria-controls="tp-2" aria-selected="false">Zones</button>
    <button class="orca-tab" role="tab" type="button" id="tb-3" aria-controls="tp-3" aria-selected="false">Recordings</button>
  </div>
  <div class="orca-tabs__panel" role="tabpanel" id="tp-1" aria-labelledby="tb-1" tabindex="0"><p class="orca-p">Counting since 3 March. 12,480 people this week.</p></div>
  <div class="orca-tabs__panel" role="tabpanel" id="tp-2" aria-labelledby="tb-2" tabindex="0" hidden><p class="orca-p">2 zones: Door line, Staff area.</p></div>
  <div class="orca-tabs__panel" role="tabpanel" id="tp-3" aria-labelledby="tb-3" tabindex="0" hidden><p class="orca-p">No recordings in the last 24 hours.</p></div>
</div>
```

**Classes:** `.orca-tabs`, `.orca-tabs__list`, `.orca-tab`, `.orca-tabs__panel`, `.orca-tabs--brand`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Jakob's law: work the way products people already know work

**Related:** `child-tabs`

**ORCA guide items covered:** Tab bar

---

## Child tabs (with counts)

`id: child-tabs` · level: component · source: ORCA

Page tabs on a parent record, one per kind of child, each showing how many there are.

Built from: `count-badge`

### Why

Counts tell people where the content is before they click (Practical UI S06) and turn empty tabs into information instead of a surprise.

### When to use

- A parent record's detail page with lists of children (a site's cameras, zones, users).

### How to use

- `<nav class="orca-tabs__list" aria-label=…>` of `<a class="orca-tab">Cameras <span class="orca-count orca-count--neutral">12</span></a>`; current tab `aria-current="page"`.
- Keep the parent summary above the tabs so context stays visible.

#### Example: Child tabs

```django
<nav class="orca-tabs__list" aria-label="North building">
  <a class="orca-tab" href="#">Overview</a>
  <a class="orca-tab" href="#" aria-current="page">Cameras <span class="orca-count orca-count--neutral">12</span></a>
  <a class="orca-tab" href="#">Zones <span class="orca-count orca-count--neutral">5</span></a>
  <a class="orca-tab" href="#">Users <span class="orca-count orca-count--neutral">0</span></a>
</nav>
```

**Classes:** `.orca-tabs__list`, `.orca-tab`

**Principles applied:** Practical UI S06: Make essential content visible or discoverable; Miller's law: chunk information so working memory is not overloaded

**Related:** `tab-bar`

**ORCA guide items covered:** Child tabs (with counts)

---

## Bottom navigation bar

`id: bottom-navigation` · level: component · source: ORCA

Three to five main sections as icon-and-label buttons fixed at the bottom of phone screens.

Built from: `icon`, `count-badge`

### Why

The bottom of a phone is in thumb reach (Fitts's law) and the pattern is familiar from mobile platforms (Jakob's law); labels keep icons unambiguous (Hick's law).

### When to use

- Phone layouts of products with 3 to 5 main sections used often.

### When not to use

- Desktop, or more than five sections.

### How to use

- `<nav class="orca-bottom-nav" aria-label="Main">` with links containing an icon and a short label; current link `aria-current="page"`.
- Add bottom padding to the page so content is not hidden behind it (it includes the safe area).
- Show it below 620px only; on wider screens use the sidebar or top bar.

#### Example: Bottom bar (shown in place)

```django
<nav class="orca-bottom-nav orca-bottom-nav--static" aria-label="Main" style="max-width: 24rem">
  <a href="#" aria-current="page">{% icon "home" %}Home</a><a href="#">{% icon "snapshot" %}Cameras</a><a href="#">{% icon "notifications" %}Alerts<span class="orca-count" aria-label="3 new">3</span></a><a href="#">{% icon "user" %}Profile</a>
</nav>
```

**Classes:** `.orca-bottom-nav`, `.orca-bottom-nav--static`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Jakob's law: work the way products people already know work; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Bottom navigation bar

---

## Nav tree

`id: nav-tree` · level: component · source: ORCA

Collapsible sections of navigation links (tree leaves) for large hierarchies.

Built from: `chevron`, `count-badge`

### Why

Grouping many destinations into named sections keeps a long navigation scannable (Miller's law) and shows only what is relevant (Practical UI S04).

### When to use

- Sidebars and documentation with more than about 12 destinations in groups.

### How to use

- `<nav aria-label=…><ul class="orca-nav-tree">` with `<details>` sections: `<summary>` (chevron, name, optional count) and a `<ul>` of leaf links.
- Open the section that contains the current page; leaves use `aria-current="page"`.
- Nest a second level of details for sub-sections; avoid a third.

#### Example: Tree

```django
<nav aria-label="Settings" style="max-width: 16rem"><ul class="orca-nav-tree">
  <li><details open><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>Organisation<span class="orca-count orca-count--neutral">3</span></summary>
    <ul><li><a href="#">Profile</a></li><li><a href="#" aria-current="page">Users</a></li><li><a href="#">Billing</a></li></ul></details></li>
  <li><details><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>Devices<span class="orca-count orca-count--neutral">2</span></summary>
    <ul><li><a href="#">Cameras</a></li><li><a href="#">Recorders</a></li></ul></details></li>
</ul></nav>
```

**Classes:** `.orca-nav-tree`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI S04: Reveal secondary information when needed

**ORCA guide items covered:** Nav tree (collapsible sections); Tree leaf

---

## Back link

`id: back-link` · level: component · source: ORCA

A link to the previous level, above the page title.

Built from: `text-link`, `icon`

### Why

A visible way back near the top keeps people oriented, especially on phones where breadcrumbs do not fit (Jakob's law, Practical UI B09).

### When to use

- Detail and form pages reached from a list; steps of a flow.

### How to use

- `<a class="orca-back-link" href=…>{% icon "chevron-left" %}Back to cameras</a>` above the title.
- Name the destination ('Back to cameras'), never just 'Back'. Link to the real parent, not `history.back()`, so it works from a shared link.

#### Example: Back link

```django
<a class="orca-back-link" href="#">{% icon "chevron-left" size="xs" %}Back to cameras</a>
```

**Classes:** `.orca-back-link`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI B09: Position multi-step navigation carefully; Practical UI W14: Give links meaningful destination names

**ORCA guide items covered:** Back link

---

## View toggle (cards, table)

`id: view-toggle` · level: component · source: ORCA

A segmented control switching a collection between cards and a table.

Built from: `button`, `icon`

### Why

Cards suit browsing with images; tables suit comparing values. Letting people choose moves the decision to them (Tesler's law), and the segmented shape shows both options at once (Practical UI R11).

### When to use

- Collections where both browsing and comparing are common.

### How to use

- Links (server-rendered): `<nav class="orca-segmented" aria-label="View">` of `<a class="orca-segmented__item" aria-current="page">` with icon + label.
- In place: radios inside `<fieldset class="orca-segmented">` labels.
- Remember the choice per user; default to cards on phones.

#### Example: View toggle

```django
<nav class="orca-segmented orca-segmented--dense" aria-label="View">
  <a class="orca-segmented__item" href="#" aria-current="page">{% icon "grid" %}Cards</a>
  <a class="orca-segmented__item" href="#">{% icon "list" %}Table</a>
</nav>
```

**Classes:** `.orca-segmented`, `.orca-segmented__item`, `.orca-segmented--dense`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Practical UI R11: Visible choices for small sets

**ORCA guide items covered:** View toggle (cards, table)

---

## Settings toggle

`id: settings-toggle` · level: component · source: ORCA

An icon button that opens the display settings panel (theme, density).

Built from: `icon-button`

### Why

Display preferences are needed rarely, so they sit behind one familiar icon (Hick's law, S04) that states its state with aria-expanded.

### When to use

- Top bar or page head of products that offer display settings.

### How to use

- `<button class="orca-icon-button" type="button" aria-label="Display settings" aria-expanded="false" aria-controls="panel-id" data-orca-disclose>{% icon "sliders" %}</button>`.
- The panel itself is a pattern (settings panel); it can contain the theme toggle.

#### Example: Settings toggle

```django
<button class="orca-icon-button orca-icon-button--outlined" type="button" aria-label="Display settings" aria-expanded="false" aria-controls="st-panel" data-orca-disclose>{% icon "sliders" %}</button>
<div id="st-panel" hidden style="margin-top: var(--orca-space-8); padding: var(--orca-space-16); max-width: 22rem" class="orca-elevation-2">
  <fieldset class="orca-segmented" data-orca-theme-choice><legend class="orca-label">Theme</legend>
    <label class="orca-segmented__item"><input type="radio" name="st-theme" value="auto" checked>Auto</label><label class="orca-segmented__item"><input type="radio" name="st-theme" value="light">Light</label><label class="orca-segmented__item"><input type="radio" name="st-theme" value="dark">Dark</label>
  </fieldset>
</div>
```

**Classes:** `.orca-icon-button`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI S04: Reveal secondary information when needed

**Related:** `theme-toggle`

**ORCA guide items covered:** Settings toggle

---

## Create button (floating on phones)

`id: create-button` · level: component · source: ORCA

The page's create action: a primary button in the page head that becomes a floating button on phones.

Built from: `button`, `fab`

### Why

On desktop the create action belongs beside the title; on phones it must stay in thumb reach while scrolling (Fitts's law). One element serves both so the action is never duplicated.

### When to use

- List pages with one create action (Add camera, New report).

### How to use

- `<a class="orca-button orca-button--primary orca-create" href=…>{% icon "plus" %}Add camera</a>` in the page head.
- Below 620px it floats at the bottom right (respecting safe areas); add 5rem of bottom padding to the page so it never covers the last row.

#### Example: Create button

```django
<a class="orca-button orca-button--primary orca-create orca-create--static" href="#">{% icon "plus" %}Add camera</a>
```

**Classes:** `.orca-create`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI B03: One primary action

**ORCA guide items covered:** Create button (floating on phones)

---
