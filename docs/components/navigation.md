# Navigation

How people move between pages. The current location is marked with aria-current and a shape, not colour alone.

## Primary navigation

`id: primary-navigation` · level: component · source: ORCA

Top-bar links to the product's main sections.

Built from: `text-link`

### General description

A row of links, usually across the top of a site or app, that leads to its main sections. It is always visible so people know where they are.

#### Use cases

- Switching between the main areas of a website or application.
- Showing the current section on every page.
- Giving first-time visitors a quick overview of what the product offers.

#### When not to use it

- Many top-level sections that do not fit in one row: use a sidebar or a grouped menu.
- Steps of a single task: use a stepper or back and next buttons.

#### Best practices

- Keep to a handful of clear, short labels.
- Mark the current section visibly, not by colour alone.
- Use the same links in the same order on every page.
- Collapse to a menu on small screens.

### When to use

- Products with 2 to about 6 top-level sections.

### When not to use

- More sections: use the sidebar.

### How to use

- `<nav aria-label="Main"><ul class="orca-topnav">` with links; the current link gets `aria-current="page"` (or `"true"` for a section).
- Use nouns people know ('Videos', 'Reports'). Icons are optional, never alone.
- Below 1036px, move the links into the sidebar drawer (pattern level).

#### Example: Top-bar links

```django
<nav aria-label="Main">
  <ul class="orca-topnav" style="min-height: var(--orca-nav-height)">
    <li>
      <a href="#" aria-current="page">Dashboard</a>
    </li>
    <li>
      <a href="#">Videos</a>
    </li>
    <li>
      <a href="#">Reports</a>
    </li>
    <li>
      <a href="#">Alerts</a>
    </li>
  </ul>
</nav>
```

**Classes:** `.orca-topnav`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI C03: Communicate meaning beyond colour; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Primary navigation

---

## Utility navigation

`id: utility-navigation` · level: component · source: ORCA

Help, notifications and the user chip at the end of the top bar.

Built from: `icon-button`, `count-badge`, `avatar`

### General description

A small group of links and buttons, usually at the far end of the header, for account, help, notifications and other tools that are not main sections.

#### Use cases

- Opening the user account menu or signing out.
- Showing notifications and a help link.
- Offering search, language or settings shortcuts in the header.

#### When not to use it

- Main sections of the product: put them in the primary navigation.
- Long lists of options: use a menu or a settings page.

#### Best practices

- Keep it to a few well-known items.
- Place it in the same corner on every page.
- Give icon-only items a text label for screen readers.
- Show a count only when something needs attention.

### When to use

- End of the top bar on every signed-in page.

### How to use

- `<ul class="orca-utility-nav">` with icon buttons (each with `aria-label`; the notifications one with a count) and the user chip.
- Use dense icon buttons on desktop; they grow to 44px on touch.

#### Example: Utility links

```django
<ul class="orca-utility-nav">
  <li>
    <a class="orca-icon-button" href="#" aria-label="Help">
      {% icon "help" %}
    </a>
  </li>
  <li>
    <a class="orca-icon-button orca-has-count" href="#" aria-label="Notifications, 3 unread">
      {% icon "notifications" %}
      <span class="orca-count" aria-hidden="true">3</span>
    </a>
  </li>
  <li>
    <button class="orca-user-chip" type="button" aria-haspopup="menu" aria-expanded="false">
      <span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span>
      <span class="orca-user-chip__text">
        <span class="orca-user-chip__name">Ada Lovelace</span>
        <span class="orca-user-chip__role">Administrator</span>
      </span>
    </button>
  </li>
</ul>
```

**Classes:** `.orca-utility-nav`

**Principles applied:** Jakob's law: work the way products people already know work; Miller's law: chunk information so working memory is not overloaded

**Related:** `user-chip`

**ORCA guide items covered:** Utility navigation

---

## Sidebar link

`id: sidebar-link` · level: component · source: Tangerine

One sidebar destination: icon, label and optional count.

Built from: `icon`, `count-badge`

### General description

One link in a vertical navigation list at the side of a page, usually with an icon, a label and sometimes a count of items.

#### Use cases

- Moving between sections of an app with many areas.
- Showing how many items wait in a section, such as unread alerts.
- Grouping related pages under a nested link.

#### When not to use it

- A short list of 2 to 5 sections: top navigation is simpler.
- Actions that change data: use a button, not a link.

#### Best practices

- Write short labels that fit on one line.
- Highlight the current page with more than colour.
- Make the whole row clickable, not just the text.
- Keep icons consistent and always paired with a label.

### When to use

- Every sidebar item.

### How to use

- `<a class="orca-side-link" href=…>{% icon … %}<span class="orca-side-link__label">Videos</span><span class="orca-count orca-count--neutral">12</span></a>` inside `<ul class="orca-side-nav">`.
- `aria-current="page"` on the current link; `--l2` for a nested link.
- Labels never wrap; long ones are cut with an ellipsis and get a `title`.

#### Example: Side links

```django
<nav aria-label="Sections" style="max-width: 15rem; background: var(--orca-bg-alt)">
  <ul class="orca-side-nav">
    <li>
      <a class="orca-side-link" href="#">
        {% icon "home" %}
        <span class="orca-side-link__label">Dashboard</span>
      </a>
    </li>
    <li>
      <a class="orca-side-link" href="#" aria-current="page">
        {% icon "snapshot" %}
        <span class="orca-side-link__label">Videos</span>
        <span class="orca-count orca-count--neutral">12</span>
      </a>
    </li>
    <li>
      <a class="orca-side-link orca-side-link--l2" href="#">
        <span class="orca-side-link__label">Media servers</span>
      </a>
    </li>
    <li>
      <a class="orca-side-link" href="#">
        {% icon "notifications" %}
        <span class="orca-side-link__label">Alerts</span>
        <span class="orca-count">3</span>
      </a>
    </li>
  </ul>
</nav>
```

**Classes:** `.orca-side-nav`, `.orca-side-link`, `.orca-side-link__label`, `.orca-side-link--l2`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI C03: Communicate meaning beyond colour; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Sidebar link

---

## Breadcrumbs

`id: breadcrumbs` · level: component · source: ORCA

The path from the top level down to the current page.

Built from: `text-link`, `chevron-separator`

### General description

A trail of links showing where the current page sits in the site, from the top level down. Each step links back to a higher level.

#### Use cases

- Helping people find their way in sites with deep levels.
- Jumping back up to a parent section in one click.
- Showing context on product, document or category pages.

#### When not to use it

- Sites with only one or two levels: a simple back link is enough.
- Showing the steps someone took or a process: use a stepper.

#### Best practices

- Show the real hierarchy, not the browsing history.
- Make the last item the current page and do not link it.
- Keep labels short and match page titles.
- Place the trail near the top of the page.

### When to use

- Pages two or more levels deep (Site › Building › Video).

### When not to use

- Flat products, or instead of a back link in a linear flow.

### How to use

- `<nav class="orca-breadcrumbs" aria-label="Breadcrumb"><ol>` with links, the last item a `<span aria-current="page">`.
- Separators come from CSS and mirror in right-to-left languages.
- On phones, show only the parent as a back link when space is short.

#### Example: Breadcrumbs

```django
<nav class="orca-breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li>
      <a href="#">Sites</a>
    </li>
    <li>
      <a href="#">North building</a>
    </li>
    <li>
      <span aria-current="page">Entrance A</span>
    </li>
  </ol>
</nav>
```

**Classes:** `.orca-breadcrumbs`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Breadcrumbs

---

## Pagination

`id: pagination` · level: component · source: ORCA

Previous, page numbers with gaps, next, and a summary of what is shown.

Built from: `pagination-gap`, `icon`

### General description

Controls that split a long list or set of results into numbered pages, with links to move to the previous, next or a specific page.

#### Use cases

- Browsing search results or long product lists.
- Moving through large tables of data.
- Letting people return to a known page of results.

#### When not to use it

- Short lists that fit on one screen: show everything.
- Endless feeds read in one pass: use infinite scroll or a load more button.

#### Best practices

- Show the current page clearly and mark it for screen readers.
- Make links big enough to tap.
- Keep the page in the web address so it can be shared.
- Use previous and next links as well as numbers.

### When to use

- Lists and tables with more than one page.

### When not to use

- Feeds people read continuously: use 'Load more'.

### How to use

- Django: `{% orca_pagination page_obj noun="videos" %}` keeps the other query parameters (filters, sort).
- Markup: `<nav class="orca-pagination" aria-label="Pages"><ul>` of `.orca-page-link` links; current with `aria-current="page"`; disabled ends with `aria-disabled="true"`; gaps are `.orca-page-gap`.
- Number links carry `aria-label="Page 7"`.

#### Example: Pagination

```django
<nav class="orca-pagination" aria-label="Pages">
  <ul>
    <li>
      <a class="orca-page-link" href="#" rel="prev">
        {% icon "chevron-left" %}
        <span>Previous</span>
      </a>
    </li>
    <li>
      <a class="orca-page-link" href="#" aria-label="Page 1">1</a>
    </li>
    <li>
      <span class="orca-page-gap" aria-hidden="true">…</span>
    </li>
    <li>
      <a class="orca-page-link" href="#" aria-label="Page 6">6</a>
    </li>
    <li>
      <a class="orca-page-link" href="#" aria-current="page" aria-label="Page 7, current">7</a>
    </li>
    <li>
      <a class="orca-page-link" href="#" aria-label="Page 8">8</a>
    </li>
    <li>
      <span class="orca-page-gap" aria-hidden="true">…</span>
    </li>
    <li>
      <a class="orca-page-link" href="#" aria-label="Page 16">16</a>
    </li>
    <li>
      <a class="orca-page-link" href="#" rel="next">
        <span>Next</span>
        {% icon "chevron-right" %}
      </a>
    </li>
  </ul>
</nav>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
from django.views.generic import ListView

from .models import Video


class VideoList(ListView):
    model = Video
    paginate_by = 25          # gives the template page_obj
    # Template: {% orca_pagination page_obj noun="videos" %} — the links keep the other query
    # parameters (filters, sort) and the summary says "Showing 26–50 of 312 videos".
```

**Classes:** `.orca-pagination`, `.orca-page-link`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Hick's law: fewer, clearer choices mean faster decisions; Fitts's law: big, close, well-spaced targets are faster and safer

**Related:** `pagination-summary`, `table-pager`

**ORCA guide items covered:** Pagination; Pagination link

---

## Pagination summary

`id: pagination-summary` · level: component · source: ORCA

'Showing 121–140 of 312 videos': which part of the list is on screen.

Built from: `tabular-number`

### General description

A line of text that tells people which part of a list they are viewing and how many items there are in total, such as 'Showing 21 to 40 of 312'.

#### Use cases

- Confirming how many results a search or filter returned.
- Orienting people within a long paginated list.
- Showing a total next to page controls.

#### When not to use it

- Lists whose total is unknown or constantly changing: say 'many results' or use load more.
- Short lists on one page: a simple count is enough.

#### Best practices

- Use real numbers and group digits in long numbers.
- Update the text as soon as filters change.
- Say what the items are, such as videos or orders.
- Handle zero results with a clear message.

### When to use

- Above or below any paginated list; alone when there is one page.

### How to use

- `<p class="orca-pagination-summary">Showing 121–140 of 312 videos</p>`, with an en dash and grouping separators.
- No results: say 'No videos match these filters' and show an empty state below.

#### Example: Summary

```django
<p class="orca-pagination-summary">Showing 121–140 of 312 videos</p>
```

**Classes:** `.orca-pagination-summary`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Pagination summary

---

## Table pager

`id: table-pager` · level: component · source: ORCA

A compact pager under a table: rows per page, range shown, previous and next.

Built from: `select`, `icon-button`, `pagination-summary`

### General description

A compact set of controls beneath a data table that lets people choose how many rows to show per page and move between pages.

#### Use cases

- Browsing large data tables in admin screens.
- Letting people pick 20, 50 or 100 rows per page.
- Showing the range of rows currently displayed.

#### When not to use it

- Small tables that fit on one screen: show all rows.
- Card grids or content lists: use regular pagination or load more.

#### Best practices

- Put it directly below the table, close to the rows.
- Disable previous on the first page and next on the last.
- Offer a few sensible page sizes.
- Remember the chosen page size between visits.

### When to use

- Footers of data tables and table cards.

### How to use

- `<div class="orca-table-pager">`: a label with a dense select of sizes (20, 50, 100), the range summary, and `.orca-table-pager__nav` with two icon buttons.
- Disable previous on the first page and next on the last. Keep page sizes small so pages load fast.

#### Example: Pager

```django
<div class="orca-table-pager" style="border: var(--orca-border-width) solid var(--orca-border)">
  <label>Rows per page <select class="orca-select orca-select--dense"><option>20</option><option selected>50</option><option>100</option></select></label>
  <span class="orca-num">51–100 of 312</span>
  <span class="orca-table-pager__nav">
    <a class="orca-icon-button orca-icon-button--dense" href="#" aria-label="Previous page">
      {% icon "chevron-left" %}
    </a>
    <a class="orca-icon-button orca-icon-button--dense" href="#" aria-label="Next page">
      {% icon "chevron-right" %}
    </a>
  </span>
</div>
```

**Classes:** `.orca-table-pager`, `.orca-table-pager__nav`

**Principles applied:** Practical UI L14: Reduce travel between related actions; Tesler's law: move unavoidable complexity from the user to the system; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Table pager

---

## Tab bar

`id: tab-bar` · level: component · source: Tangerine

Tabs that switch between views of one object, in place or by page.

Built from: `focus-ring`, `count-badge`, `text-link`

### General description

A row of labelled tabs that switches between related views of the same content or object, showing one view at a time.

#### Use cases

- Splitting a detail page into overview, activity and settings.
- Showing different views of the same data in the same space.
- Keeping a long page short by grouping content.

#### When not to use it

- Steps that must happen in order: use a stepper.
- Unrelated pages or sections of a site: use navigation links.

#### Best practices

- Use short, clear labels.
- Always show which tab is selected.
- Support arrow keys to move between tabs.
- Keep the number of tabs small and avoid hiding critical content.

### When to use

- 2 to about 7 views of one thing: Overview, Zones, Recordings.

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
  <div class="orca-tabs__list" role="tablist" aria-label="Video" data-orca-tabs>
    <button class="orca-tab" role="tab" type="button" id="tb-1" aria-controls="tp-1" aria-selected="true">Overview</button>
    <button class="orca-tab" role="tab" type="button" id="tb-2" aria-controls="tp-2" aria-selected="false">Zones</button>
    <button class="orca-tab" role="tab" type="button" id="tb-3" aria-controls="tp-3" aria-selected="false">Recordings</button>
  </div>
  <div class="orca-tabs__panel" role="tabpanel" id="tp-1" aria-labelledby="tb-1" tabindex="0">
    <p class="orca-p">Counting since 3 March. 12,480 people this week.</p>
  </div>
  <div class="orca-tabs__panel" role="tabpanel" id="tp-2" aria-labelledby="tb-2" tabindex="0" hidden>
    <p class="orca-p">2 zones: Door line, Staff area.</p>
  </div>
  <div class="orca-tabs__panel" role="tabpanel" id="tp-3" aria-labelledby="tb-3" tabindex="0" hidden>
    <p class="orca-p">No recordings in the last 24 hours.</p>
  </div>
</div>
```

**Classes:** `.orca-tabs`, `.orca-tabs__list`, `.orca-tab`, `.orca-tabs__panel`, `.orca-tabs--brand`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Jakob's law: work the way products people already know work

**Related:** `child-tabs`

**ORCA guide items covered:** Tab bar

---

## Child tabs (with counts)

`id: child-tabs` · level: component · source: ORCA

Page tabs on a parent record, one per kind of child, each with a count.

Built from: `count-badge`

### General description

Tabs on the page of a parent record, each leading to one kind of related item and showing how many it holds, such as Users (12).

#### Use cases

- Showing the lists that belong to an account, site or project.
- Letting people see at a glance which sections have content.
- Navigating between related lists without leaving the parent.

#### When not to use it

- Views that are not related items of one record: use plain tabs or navigation.
- Steps of a process: use a stepper.

#### Best practices

- Show a count so empty sections are clear before clicking.
- Keep the parent summary visible above the tabs.
- Order tabs by how often people use them.
- Mark the current tab with more than colour.

### When to use

- A parent record's page with lists of children (a site's videos, zones, users).

### How to use

- `<nav class="orca-tabs__list" aria-label=…>` of `<a class="orca-tab">Videos <span class="orca-count orca-count--neutral">12</span></a>`; current tab `aria-current="page"`.
- Keep the parent summary above the tabs so context stays visible.

#### Example: Child tabs

```django
<nav class="orca-tabs__list" aria-label="North building">
  <a class="orca-tab" href="#">Overview</a>
  <a class="orca-tab" href="#" aria-current="page">Videos <span class="orca-count orca-count--neutral">12</span></a>
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

3 to 5 main sections as icon-and-label buttons fixed to the bottom of phone screens.

Built from: `icon`, `count-badge`

### General description

A bar fixed to the bottom of a phone screen with three to five main destinations, each shown as an icon with a short label.

#### Use cases

- Switching between the main areas of a mobile app or site.
- Making key destinations easy to reach with a thumb.
- Showing a badge for new items on a destination.

#### When not to use it

- Desktop screens: use a top bar or sidebar.
- More than five destinations: use a menu or a navigation drawer.

#### Best practices

- Pair every icon with a short label.
- Mark the current destination clearly.
- Keep the same items on every screen.
- Leave space for the bar so it does not cover content.

### When to use

- Phone layouts with 3 to 5 often-used main sections.

### When not to use

- Desktop, or more than 5 sections.

### How to use

- `<nav class="orca-bottom-nav" aria-label="Main">` with links containing an icon and a short label; current link `aria-current="page"`.
- Add bottom padding so content is not hidden behind it (it includes the safe area).
- Show it below 620px only; on wider screens use the sidebar or top bar.

#### Example: Bottom bar (shown in place)

```django
<nav class="orca-bottom-nav orca-bottom-nav--static" aria-label="Main" style="max-width: 24rem">
  <a href="#" aria-current="page">
    {% icon "home" %}
    Home
  </a>
  <a href="#">
    {% icon "snapshot" %}
    Videos
  </a>
  <a href="#">
    {% icon "notifications" %}
    Alerts
    <span class="orca-count" aria-label="3 new">3</span>
  </a>
  <a href="#">
    {% icon "user" %}
    Profile
  </a>
</nav>
```

**Classes:** `.orca-bottom-nav`, `.orca-bottom-nav--static`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Jakob's law: work the way products people already know work; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Bottom navigation bar

---

## Nav tree

`id: nav-tree` · level: component · source: ORCA

Collapsible groups of navigation links for large hierarchies.

Built from: `chevron`, `count-badge`

### General description

A navigation list with collapsible groups, where each group opens to show its links. It organises many destinations into a readable hierarchy.

#### Use cases

- Navigating large documentation sites or settings areas.
- Grouping many pages under named sections.
- Showing the user's place inside a deep structure.

#### When not to use it

- Short lists of links: show them flat.
- Deeply nested content with more than three levels: simplify the structure or add search.

#### Best practices

- Open the group that holds the current page.
- Show open and closed state with an icon and text, not colour alone.
- Limit nesting to two levels.
- Make groups work with the keyboard.

### When to use

- Sidebars and documentation with more than about 12 grouped destinations.

### How to use

- `<nav aria-label=…><ul class="orca-nav-tree">` with `<details>` sections: `<summary>` (icon on first-level parents, name, optional count, small chevron at the end) and a `<ul>` of leaf links.
- Open the section that contains the current page; leaves use `aria-current="page"`.
- First-level parents start with an icon (`{% icon "name" %}`). The chevron (`size="xs"`) points right when closed and down when open.
- Nest a second level of details without icons for sub-sections; avoid a third.

#### Example: Tree

```django
<nav aria-label="Settings" style="max-width: 16rem">
  <ul class="orca-nav-tree">
    <li>
      <details open>
        <summary>
          {% icon "settings" %}
          Organisation
          <span class="orca-count orca-count--neutral">3</span>
          <span class="orca-chevron">
            {% icon "chevron-down" size="xs" %}
          </span>
        </summary>
        <ul>
          <li>
            <a href="#">Profile</a>
          </li>
          <li>
            <a href="#" aria-current="page">Users</a>
          </li>
          <li>
            <a href="#">Billing</a>
          </li>
        </ul>
      </details>
    </li>
    <li>
      <details>
        <summary>
          {% icon "snapshot" %}
          Devices
          <span class="orca-count orca-count--neutral">2</span>
          <span class="orca-chevron">
            {% icon "chevron-down" size="xs" %}
          </span>
        </summary>
        <ul>
          <li>
            <a href="#">Videos</a>
          </li>
          <li>
            <a href="#">Media servers</a>
          </li>
        </ul>
      </details>
    </li>
  </ul>
</nav>
```

**Classes:** `.orca-nav-tree`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI S04: Reveal secondary information when needed

**ORCA guide items covered:** Nav tree (collapsible sections); Tree leaf

---

## Back link

`id: back-link` · level: component · source: ORCA

A link to the previous level, above the page title.

Built from: `text-link`, `icon`

### General description

A link that takes people to the previous level or page, usually placed above the page heading, labelled with where it goes.

#### Use cases

- Returning from a detail page to its list.
- Leaving a step in a multi-page form.
- Giving phone users a short way back when breadcrumbs do not fit.

#### When not to use it

- Replacing the browser's back button behaviour: link to a real page instead.
- Deep hierarchies where people need many levels: use breadcrumbs.

#### Best practices

- Name the destination, such as 'Back to orders'.
- Place it consistently above the title.
- Link to the actual parent page so it works from shared links.
- Include a visible arrow as a hint.

### When to use

- Detail and form pages reached from a list; steps of a flow.

### How to use

- `<a class="orca-back-link" href=…>{% icon "chevron-left" %}Back to videos</a>` above the title.
- Name the destination ('Back to videos'), not just 'Back'. Link to the real parent, not `history.back()`, so it works from a shared link.

#### Example: Back link

```django
<a class="orca-back-link" href="#">
  {% icon "chevron-left" size="xs" %}
  Back to videos
</a>
```

**Classes:** `.orca-back-link`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI B09: Position multi-step navigation carefully; Practical UI W14: Give links meaningful destination names

**ORCA guide items covered:** Back link

---

## View toggle (cards, table)

`id: view-toggle` · level: component · source: ORCA

A segmented control that switches a collection between cards and a table.

Built from: `button`, `icon`

### General description

A small control that lets people switch how the same collection is shown, for example as cards or as a table, without changing the content.

#### Use cases

- Switching a list between a visual grid and a dense table.
- Letting people choose between map and list views.
- Matching the view to the task, browsing or comparing.

#### When not to use it

- Switching between different content: use tabs.
- Turning a setting on or off: use a switch or checkbox.

#### Best practices

- Show all options at once with an icon and a label.
- Mark the active view clearly.
- Remember the choice for next time.
- Keep filters and sorting when the view changes.

### When to use

- Collections where both browsing and comparing are common.

### How to use

- Links (server-rendered): `<nav class="orca-segmented" aria-label="View">` of `<a class="orca-segmented__item" aria-current="page">` with icon + label.
- In place: radios inside `<fieldset class="orca-segmented">` labels.
- Remember the choice per user; default to cards on phones.

#### Example: View toggle

```django
<nav class="orca-segmented orca-segmented--dense" aria-label="View">
  <a class="orca-segmented__item" href="#" aria-current="page">
    {% icon "grid" %}
    Cards
  </a>
  <a class="orca-segmented__item" href="#">
    {% icon "list" %}
    Table
  </a>
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

### General description

A button, usually an icon, that opens or closes a panel of display or app settings without leaving the page.

#### Use cases

- Opening quick display settings such as theme or density.
- Showing options that are used rarely.
- Keeping the main screen simple while settings stay close.

#### When not to use it

- Important settings people need often: show them directly.
- Large sets of preferences: use a full settings page.

#### Best practices

- Use a familiar icon with a text label for assistive tools.
- Tell screen readers if the panel is open or closed.
- Let Escape close the panel.
- Save changes right away and show the result.

### When to use

- Top bar or page head of products with display settings.

### How to use

- `<button class="orca-icon-button" type="button" aria-label="Display settings" aria-expanded="false" aria-controls="panel-id" data-orca-disclose>{% icon "sliders" %}</button>`.
- The panel is a separate pattern (settings panel) and can hold the theme toggle.

#### Example: Settings toggle

```django
<button class="orca-icon-button orca-icon-button--outlined" type="button" aria-label="Display settings" aria-expanded="false" aria-controls="st-panel" data-orca-disclose>
  {% icon "sliders" %}
</button>
<div id="st-panel" hidden style="margin-top: var(--orca-space-8); padding: var(--orca-space-16); max-width: 22rem" class="orca-elevation-2">
  <fieldset class="orca-segmented" data-orca-theme-choice>
    <legend class="orca-label">Theme</legend>
    <label class="orca-segmented__item"><input type="radio" name="st-theme" value="auto" checked>Auto</label>
    <label class="orca-segmented__item"><input type="radio" name="st-theme" value="light">Light</label>
    <label class="orca-segmented__item"><input type="radio" name="st-theme" value="dark">Dark</label>
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

The page's create action: a primary button in the page head that floats on phones.

Built from: `button`, `fab`

### General description

The main button for adding a new item, such as a new record or document. It sits near the page title and is the page's primary action.

#### Use cases

- Adding a new item from a list page.
- Starting a new document, report or project.
- Keeping the main create action easy to find on every list.

#### When not to use it

- Pages with several equally important actions: group them in a menu or toolbar.
- Actions that change existing items: use a regular button next to the item.

#### Best practices

- Start the label with a verb and name the item, such as 'Add video'.
- Show only one primary create action per page.
- Make it easy to reach on phones.
- Use an icon only to support the text.

### When to use

- List pages with one create action (Add video, New report).

### How to use

- `<a class="orca-button orca-button--primary orca-create" href=…>{% icon "plus" %}Add video</a>` in the page head.
- Below 620px it floats at the bottom right (respecting safe areas). Add 5rem of bottom padding so it never covers the last row.

#### Example: Create button

```django
<a class="orca-button orca-button--primary orca-create orca-create--static" href="#">
  {% icon "plus" %}
  Add video
</a>
```

**Classes:** `.orca-create`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI B03: One primary action

**ORCA guide items covered:** Create button (floating on phones)

---

## Skip navigation

`id: skip-navigation` · level: component · source: ORCA

A skip link and the focusable main area it jumps to.

Built from: `skip-link`

### General description

A link at the very top of a page that jumps straight to the main content. Keyboard and screen reader users use it to avoid tabbing through the menu on every page.

#### Use cases

- Pages with a long header or menu before the content.
- Any site that people navigate by keyboard.
- Sites that must meet accessibility standards.

#### When not to use it

- Replacing good page structure; headings and landmarks are still needed.
- Hiding it permanently; it must appear when it receives focus.

#### Best practices

- Make it the first thing keyboard focus reaches.
- Show it clearly when focused.
- Point it to a target that can take focus.
- Use words like 'Skip to main content'.
- Use one main area per page.

### When to use

- Every page; the base layout adds it.

### How to use

- First in `<body>`: `<a class="orca-skip-link" href="#main">Skip to main content</a>`; the target is `<main id="main" tabindex="-1">`.
- Keep one main landmark per page.

### Accessibility

- It is the first focusable element and appears on focus.

#### Example: Skip navigation (press Tab inside this example)

```django
<div style="position: relative; height: 3rem; overflow: hidden">
  <a class="orca-skip-link" href="#sn-main">Skip to main content</a>
  <div id="sn-main" tabindex="-1" class="orca-small orca-muted" style="padding: var(--orca-space-8)">Main content starts here.</div>
</div>
```

**Classes:** `.orca-skip-link`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI F01: Design for a diverse audience

**Related:** `base-layout`

---

## Link column

`id: link-column` · level: component · source: ORCA

A titled list of links, as in a footer or a site map.

Built from: `text-link`

### General description

A short heading with a list of related links beneath it. Several columns side by side organise many links by topic.

#### Use cases

- Website footers with product, company and help links.
- Site maps.
- Related links at the end of an article or help page.

#### When not to use it

- Main navigation people use all the time; use a navigation bar or menu.
- Long lists of links in one column; split by topic or search instead.

#### Best practices

- Give each column a clear topic title.
- Keep columns to about eight links or fewer.
- Write link text that names the destination.
- Order links by how often people need them.

### When to use

- Footer columns, site maps, 'Related' lists at the end of documentation pages.

### When not to use

- More than about eight links: split the column by topic.

### How to use

- `<ul class="orca-footer__col"><li class="orca-footer__col-title">Product</li><li><a href=…>Features</a></li>…</ul>`.
- Link text names the destination (W14).

#### Example: Link column

```django
<ul class="orca-footer__col">
  <li class="orca-footer__col-title">Help</li>
  <li>
    <a href="#">Documentation</a>
  </li>
  <li>
    <a href="#">Contact support</a>
  </li>
</ul>
```

**Classes:** `.orca-footer__col`, `.orca-footer__col-title`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI L01: Group related information; Practical UI W14: Give links meaningful destination names

**Related:** `footer`

---
