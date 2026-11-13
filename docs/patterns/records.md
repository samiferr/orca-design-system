# Record management

Showing and changing one record and its children: detail panels, child tabs, activity, protected deletes and confirmations.

## Detail panel

`id: detail-panel` · level: pattern · source: Tangerine

One record's summary: title and status, its actions, and a table of its properties.

Built from: `record-actions`, `key-value-list`, `status-light`

### When to use

- The main panel of a detail page; a side panel for the selected row.

### How to use

- `<section class="orca-detail-panel">` with `.orca-detail-panel__head` (`__title`: name + status light; record actions) and a key/value list or table card below.

#### Example: Video

```django
<section class="orca-detail-panel" aria-labelledby="dp-t" style="max-width: 36rem">
  <div class="orca-detail-panel__head">
    <div class="orca-detail-panel__title">
      <h2 id="dp-t">Entrance A</h2>
      <span class="orca-status orca-small"><span class="orca-dot orca-dot--positive"></span>Online <span class="orca-status__meta">for 12 days</span></span>
    </div>
    <div class="orca-record-actions">
      <a class="orca-button orca-button--dense" href="#">
        {% icon "edit" %}
        Edit video
      </a>
      <button class="orca-icon-button orca-icon-button--dense orca-icon-button--outlined" type="button" aria-label="More actions for Entrance A">
        {% icon "more" %}
      </button>
    </div>
  </div>
  <dl class="orca-kv">
    <div>
      <dt>Site</dt>
      <dd>North building</dd>
    </div>
    <div>
      <dt>Format</dt>
      <dd>MP4, 1080p</dd>
    </div>
    <div>
      <dt>Address</dt>
      <dd>
        <code class="orca-code">media.example.com/v/4821</code>
      </dd>
    </div>
    <div>
      <dt>Views today</dt>
      <dd class="orca-num">4,812</dd>
    </div>
  </dl>
</section>
```

**Classes:** `.orca-detail-panel`, `.orca-detail-panel__head`, `.orca-detail-panel__title`

**Principles applied:** Practical UI L03: Establish an order of importance; Miller's law: chunk information so working memory is not overloaded; Practical UI B03: One primary action

**ORCA guide items covered:** Detail panel (header + actions + table)

---

## Parent record with child tabs

`id: parent-child-tabs` · level: pattern · source: ORCA

A parent record's summary followed by tabs, one per kind of child, each with its count.

Built from: `page-head`, `child-tabs`, `stat-card`

### When to use

- Records that own lists of other records: a site's videos, zones and users.

### How to use

- `<div class="orca-parent">` with the page head, `.orca-parent__summary` (stat cards or key facts) and child tabs as page links; the active tab's panel holds the child list tab.
- Each tab is its own URL so it can be shared and survives a reload.

#### Example: Site

```django
<div class="orca-parent">
  <div class="orca-page-head" style="margin: 0">
    <div class="orca-page-head__text">
      <h1 class="orca-page-title">North building</h1>
      <p class="orca-page-subtitle">12 Rue de la Gare, Lille</p>
    </div>
    <div class="orca-page-head__actions">
      <a class="orca-button" href="#">
        {% icon "edit" %}
        Edit site
      </a>
    </div>
  </div>
  <div class="orca-parent__summary">
    <div class="orca-stat-card">
      <div class="orca-stat-card__head">
        <span class="orca-stat-card__icon" aria-hidden="true">
          {% icon "user" %}
        </span>
        <p class="orca-stat-label">Visitors today</p>
      </div>
      <p class="orca-stat-value">9,530</p>
    </div>
    <div class="orca-stat-card">
      <div class="orca-stat-card__head">
        <span class="orca-stat-card__icon" aria-hidden="true">
          {% icon "statistics" %}
        </span>
        <p class="orca-stat-label">Videos online</p>
      </div>
      <p class="orca-stat-value">11 of 12</p>
    </div>
  </div>
  <nav class="orca-tabs__list" aria-label="North building">
    <a class="orca-tab" href="#">Overview</a>
    <a class="orca-tab" href="#" aria-current="page">Videos <span class="orca-count orca-count--neutral">12</span></a>
    <a class="orca-tab" href="#">Zones <span class="orca-count orca-count--neutral">5</span></a>
    <a class="orca-tab" href="#">Users <span class="orca-count orca-count--neutral">3</span></a>
  </nav>
</div>
```

**Classes:** `.orca-parent`, `.orca-parent__summary`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI S06: Make essential content visible or discoverable; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Parent record with child tabs

---

## Child list tab

`id: child-list-tab` · level: pattern · source: ORCA

The content of one child tab: a list header scoped to the parent, the children's table and an empty state.

Built from: `list-header`, `data-table`, `empty-state`

### When to use

- Inside parent-with-child-tabs pages.

### How to use

- A list header ('Videos 12', search, 'Add video' that links to the form with `?site=…`), then a data table or card list; when empty, an empty state with the same create action.

#### Example: Empty child list

```django
<div>
  <div class="orca-list-header">
    <h2 class="orca-list-header__title">Users <span class="orca-list-header__count">0</span></h2>
    <div class="orca-list-header__tools">
      <a class="orca-button orca-button--primary orca-button--dense" href="#">
        {% icon "plus" %}
        Add user to North building
      </a>
    </div>
  </div>
  <div class="orca-empty">
    {% orca_illustration "empty" %}
    <h3 class="orca-empty-title">No users for this site</h3>
    <p class="orca-empty-text">Add the people who should see North building's counts.</p>
  </div>
</div>
```

**Classes:** `.orca-list-header`, `.orca-data-table`

**Principles applied:** Jakob's law: work the way products people already know work; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Child list tab

---

## Activity feed

`id: activity-feed` · level: pattern · source: ORCA

Changes to a record or a site, grouped by day, each with who, what, when and the before and after values.

Built from: `activity-entry`

### When to use

- A history tab on records; an audit page for administrators.

### How to use

- `<div class="orca-activity-feed">` with `<h3 class="orca-activity-feed__day">` headings and activity entries; 'Load older' at the end (never infinite scroll in an audit log).

#### Example: Feed

```django
<div class="orca-activity-feed" style="max-width: 36rem">
  <h3 class="orca-activity-feed__day">Today</h3>
  <div class="orca-activity">
    <span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span>
    <div class="orca-activity__head"><span class="orca-badge orca-badge--subtle orca-badge--info">Updated</span><strong>Ada Lovelace</strong> changed Entrance A<time class="orca-activity__time" datetime="2026-11-06T08:14">08:14</time></div>
    <dl class="orca-activity__change">
      <dt>Interval</dt>
      <dd><del>15 min</del> → <ins>5 min</ins></dd>
    </dl>
  </div>
  <h3 class="orca-activity-feed__day">Yesterday</h3>
  <div class="orca-activity">
    <span class="orca-avatar orca-avatar--s" aria-hidden="true">GH</span>
    <div class="orca-activity__head"><span class="orca-badge orca-badge--subtle orca-badge--positive">Created</span><strong>Grace Hopper</strong> added Gate 1<time class="orca-activity__time" datetime="2026-11-05T16:02">16:02</time></div>
  </div>
  <div style="padding-top: var(--orca-space-12)">
    <button class="orca-button orca-button--ghost" type="button">Load older activity</button>
  </div>
</div>
```

**Classes:** `.orca-activity-feed`, `.orca-activity-feed__day`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Activity feed

---

## Delete-blocked notice

`id: delete-blocked-notice` · level: pattern · source: Tangerine

Why a record cannot be deleted yet, which records depend on it, and how to proceed.

Built from: `callout`, `list`, `button-group`

### When to use

- Deleting a record that protected relations still use (Django `ProtectedError`).

### How to use

- A negative callout titled 'Entrance A cannot be deleted yet', the reason, `<ul class="orca-blocked-list">` of linked dependants with counts, and the alternative (disable or archive) as a button.
- Build it from `ProtectedError.protected_objects`, grouped by model.

#### Example: Blocked

```django
<div class="orca-callout orca-callout--negative" role="alert" style="max-width: 36rem">
  {% icon "error" %}
  <p class="orca-callout__title">Entrance A cannot be deleted yet</p>
  <div class="orca-callout__body">
    <p class="orca-p">These still use it. Remove or move them first.</p>
    <ul class="orca-blocked-list">
      <li><a class="orca-link" href="#">2 zones</a> (Door line, Staff area)</li>
      <li><a class="orca-link" href="#">1 alert rule</a> (Over capacity)</li>
    </ul>
    <div class="orca-row">
      <button class="orca-button orca-button--dense" type="button">Disable video instead</button>
    </div>
  </div>
</div>
```

**Classes:** `.orca-blocked-list`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Practical UI W15: Help people recover from errors; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Delete-blocked notice (protected delete)

---

## Confirm action panel

`id: confirm-action-panel` · level: pattern · source: Tangerine

A full-page confirmation for consequential actions: what will happen, what is kept, and the named action.

Built from: `confirm-dialog`, `form-actions`

### When to use

- Deleting a site, revoking a user, stopping all runs; the fallback of a confirm dialog.

### How to use

- `<form class="orca-confirm-panel" method="post">` with a `.orca-confirm-panel__title` question, a list of what is removed and what is kept, an acknowledgement checkbox for irreversible cases, and form actions (danger button naming the action, Cancel link back).
- `--neutral` for non-destructive confirmations.

#### Example: Delete site

```django
<form class="orca-confirm-panel" method="post" onsubmit="return false">
  <h1 class="orca-confirm-panel__title">Delete North building?</h1>
  <div>
    <p class="orca-p">
      <strong>Deleted:</strong>
    </p>
    <ul>
      <li>12 videos and their zones</li>
      <li>5 alert rules</li>
    </ul>
  </div>
  <div>
    <p class="orca-p"><strong>Kept:</strong> counts in past reports.</p>
  </div>
  <label class="orca-check"><input type="checkbox" required><span class="orca-check__box"></span>I understand this cannot be undone</label>
  <div class="orca-form-actions">
    <button class="orca-button orca-button--danger" type="submit">Delete site</button>
    <a class="orca-button" href="#">Cancel</a>
  </div>
</form>
```

**Classes:** `.orca-confirm-panel`, `.orca-confirm-panel__title`, `.orca-confirm-panel--neutral`

**Principles applied:** Practical UI B13: Scale friction to the consequence; Doherty threshold: respond within 400 ms; show progress for anything slower; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Confirm action panel

---
