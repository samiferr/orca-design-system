# Grids and collections

Repeating one component in a responsive grid or sequence: products, videos, KPIs, a heat map, an event timeline.

## Product grid

`id: product-grid` · level: pattern · source: ORCA

Product items in a responsive grid that adapts the number of columns to the screen.

Built from: `product-item`, `list-header`, `pagination`

### Why

A grid of equal tiles lets people compare many products by sight (Miller's law: recognition); responsive columns keep tiles readable on every screen (Postel's law).

### When to use

- Catalogues and shop listings.

### How to use

- `<ul class="orca-product-grid">` of `<li>` product items; tiles are at least 12rem wide.
- Above the grid: the list header with count, sort and filters; below it: pagination.

#### Example: Grid

```django
<ul class="orca-product-grid">{% for n in "1234" %}<li><article class="orca-product"><div class="orca-product__image"><img src="{% static "orca/img/sample-street.svg" %}" alt=""></div><h3 class="orca-product__name"><a href="#">Dome video {{ n }}, 4 MP</a></h3><p class="orca-product__price" style="margin: 0">€1{{ n }}9</p></article></li>{% endfor %}</ul>
```

**Classes:** `.orca-product-grid`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Product grid

---

## Video grid

`id: video-grid` · level: pattern · source: Tangerine

Video cards in a grid, pinned videos first, offline videos clearly marked.

Built from: `video-card`, `view-toggle`, `card-skeleton`

### Why

Operators scan videos by their live view (Miller's law); keeping pinned videos first saves the daily search (Fitts's law) and offline ones stand out by badge and word (Von Restorff, C03).

### When to use

- Dashboards and video lists in card view.

### How to use

- `<ul class="orca-video-grid">` of video cards; order pinned first, then by name. Each image sits in a reserved 16:9 frame so the grid never jumps.
- Pair with the view toggle (cards or table) and a skeleton while snapshots load.

#### Example: Grid

```django
<ul class="orca-video-grid">{% for c in sample.videos|slice:":3" %}<li><article class="orca-card orca-card--link orca-video-card">{% if c.status == "negative" %}<div class="orca-ratio orca-ratio--16x9 orca-frame--removed">No image since {{ c.last }}</div><span class="orca-badge orca-badge--negative orca-video-card__flag">Offline</span>{% else %}<div class="orca-ratio orca-ratio--16x9"><img src="{% static "orca/img/sample-street.svg" %}" alt=""></div>{% endif %}
  <div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">{{ c.name }}</a></h3><span class="orca-status orca-small"><span class="orca-dot orca-dot--{{ c.status }}"></span>{{ c.status_text }} · {{ c.site }}</span></div></article></li>{% endfor %}</ul>
```

**Classes:** `.orca-video-grid`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Fitts's law: big, close, well-spaced targets are faster and safer; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Video grid

---

## KPI grid

`id: kpi-grid` · level: pattern · source: Tangerine

A row of stat cards summarising the state of things, linking to the detail behind each.

Built from: `stat-card`

### Why

A few key numbers at the top answer 'is everything fine?' at a glance (Miller's law); limiting them keeps each one meaningful (Von Restorff).

### When to use

- The top of dashboards and report pages.

### When not to use

- More than about six cards: choose the ones people act on.

### How to use

- `<div class="orca-kpi-grid">` of stat cards (as links when they lead somewhere), each with its comparison and, where useful, a sparkline.

#### Example: KPIs

```django
<div class="orca-kpi-grid">
  <a class="orca-stat-card" href="#"><div class="orca-stat-card__head"><span class="orca-stat-card__icon" aria-hidden="true">{% icon "user" %}</span><p class="orca-stat-label">Visitors today</p></div><p class="orca-stat-value">12,480</p><div class="orca-stat-card__foot"><span class="orca-delta orca-delta--up">{% icon "arrow-up" size="xs" %}+8%</span>vs last Friday</div></a>
  <a class="orca-stat-card" href="#"><div class="orca-stat-card__head"><span class="orca-stat-card__icon" aria-hidden="true">{% icon "home" %}</span><p class="orca-stat-label">Inside now</p></div><p class="orca-stat-value">1,204</p><div class="orca-stat-card__foot">of 1,500 capacity</div></a>
  <a class="orca-stat-card" href="#"><div class="orca-stat-card__head"><span class="orca-stat-card__icon" aria-hidden="true">{% icon "play" %}</span><p class="orca-stat-label">Videos online</p></div><p class="orca-stat-value">11 of 12</p><div class="orca-stat-card__foot"><span class="orca-with-icon">{% status_icon "negative" size="xs" %}Loading dock offline</span></div></a>
  <a class="orca-stat-card" href="#"><div class="orca-stat-card__head"><span class="orca-stat-card__icon" aria-hidden="true">{% icon "statistics" %}</span><p class="orca-stat-label">Count accuracy</p></div><p class="orca-stat-value">96.4%</p><div class="orca-stat-card__foot">last 7 days</div></a>
</div>
```

**Classes:** `.orca-kpi-grid`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** KPI grid

---

## Capacity heat map

`id: capacity-heat-map` · level: pattern · source: Tangerine

Occupancy by weekday and hour as shaded cells with the value printed, and a legend of the scale.

Built from: `heat-row`, `legend-item`

### Why

The busiest hours jump out from lightness alone (pre-attentive processing) while printed values keep it exact and accessible (Practical UI C03, W11).

### When to use

- Capacity reports, staffing and opening-hours decisions.

### How to use

- `<table class="orca-heatmap">` with a caption, hour headers (`th scope="col"`), weekday headers (`th scope="row"`) and `td.orca-heat.orca-heat--0…5` cells; `--empty` for no data.
- Put the scale under it in `.orca-heatmap-legend` with the range each level covers; wrap in `.orca-table-wrap` for phones.

#### Example: Heat map

```django
<div class="orca-table-wrap"><table class="orca-heatmap"><caption class="orca-panel-title" style="text-align: start; padding-bottom: var(--orca-space-8)">People inside, average by hour</caption>
  <thead><tr><td></td><th scope="col">09</th><th scope="col">11</th><th scope="col">13</th><th scope="col">15</th><th scope="col">17</th><th scope="col">19</th></tr></thead>
  <tbody>
    <tr><th scope="row">Mon</th><td class="orca-heat orca-heat--1">120</td><td class="orca-heat orca-heat--2">340</td><td class="orca-heat orca-heat--3">610</td><td class="orca-heat orca-heat--2">420</td><td class="orca-heat orca-heat--3">580</td><td class="orca-heat orca-heat--1">190</td></tr>
    <tr><th scope="row">Fri</th><td class="orca-heat orca-heat--1">160</td><td class="orca-heat orca-heat--3">620</td><td class="orca-heat orca-heat--5">1,010</td><td class="orca-heat orca-heat--4">760</td><td class="orca-heat orca-heat--4">910</td><td class="orca-heat orca-heat--2">310</td></tr>
    <tr><th scope="row">Sun</th><td class="orca-heat orca-heat--empty">–</td><td class="orca-heat orca-heat--0">40</td><td class="orca-heat orca-heat--1">150</td><td class="orca-heat orca-heat--1">180</td><td class="orca-heat orca-heat--0">70</td><td class="orca-heat orca-heat--empty">–</td></tr>
  </tbody></table></div>
<p class="orca-heatmap-legend">Fewer <span class="orca-heat orca-heat--0"></span><span class="orca-heat orca-heat--1"></span><span class="orca-heat orca-heat--2"></span><span class="orca-heat orca-heat--3"></span><span class="orca-heat orca-heat--4"></span><span class="orca-heat orca-heat--5"></span> More · – closed</p>
```

**Classes:** `.orca-heatmap`, `.orca-heatmap-legend`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI W11: Make numbers scannable; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Capacity heat map

---

## Event timeline

`id: event-timeline` · level: pattern · source: Tangerine

Alerts and events grouped by day, newest first, each with its status, time and snapshot.

Built from: `timeline-item`, `media-object`

### Why

Grouping by day chunks a long log (Miller's law); the timeline line and status dots show sequence and severity at a glance.

### When to use

- Alert lists, audit and incident views, a video's history.

### How to use

- `<div class="orca-event-timeline">` of day groups: `<h3 class="orca-event-timeline__day">Today</h3>` then a timeline of items.
- Each item: status dot, title, time, description and an optional thumbnail; link to the event detail.

#### Example: Timeline

```django
<div class="orca-event-timeline" style="max-width: 32rem">
  <section><h3 class="orca-event-timeline__day">Today</h3><ol class="orca-timeline">
    <li class="orca-timeline__item"><span class="orca-dot orca-dot--negative"></span><div><div class="orca-timeline__head"><a class="orca-timeline__title orca-link orca-link--plain" href="#">Loading dock offline</a><time class="orca-timeline__time" datetime="2026-11-06T08:14">08:14</time></div><p class="orca-timeline__desc">No stream for 5 minutes. Email sent to 2 people.</p></div></li>
    <li class="orca-timeline__item"><span class="orca-dot orca-dot--caution"></span><div><div class="orca-timeline__head"><a class="orca-timeline__title orca-link orca-link--plain" href="#">Over capacity, Entrance A</a><time class="orca-timeline__time" datetime="2026-11-06T07:55">07:55</time></div><p class="orca-timeline__desc">1,560 inside, limit 1,500.</p></div></li></ol></section>
  <section><h3 class="orca-event-timeline__day">Yesterday</h3><ol class="orca-timeline"><li class="orca-timeline__item"><span class="orca-dot orca-dot--positive"></span><div><div class="orca-timeline__head"><span class="orca-timeline__title">Gate 1 back online</span><time class="orca-timeline__time" datetime="2026-11-05T16:02">16:02</time></div></div></li></ol></section>
</div>
```

**Classes:** `.orca-event-timeline`, `.orca-event-timeline__day`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Event timeline

---

## Card grid

`id: card-grid` · level: pattern · source: ORCA

Cards for records, products or people in as many equal columns as fit.

Built from: `linked-card`, `person-block`

### Why

Equal cards in a grid let people compare items by position and shape (Miller's law, Practical UI L11) and adapt to any width without a breakpoint.

### When to use

- Collections people browse: records, products, people.

### When not to use

- Records people compare field by field: use a data table.

### How to use

- `<ul class="orca-card-grid">` with one card per `<li>`; a linked card when the whole card opens the record.
- Keep every card's content in the same order so the grid reads as a table.

#### Example: Cards

```django
<ul class="orca-card-grid"><li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Harbour at dusk</h3><p class="orca-card-meta">Video · 4 min</p></div></li><li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Summer 2026</h3><p class="orca-card-meta">Album · 36 images</p></div></li><li class="orca-card"><div class="orca-card__body"><div class="orca-person"><span class="orca-avatar" aria-hidden="true">AL</span><span class="orca-person__text"><span class="orca-person__name">Ada Lovelace</span><span class="orca-person__role">Editor</span></span></div></div></li></ul>
```

**Classes:** `.orca-card-grid`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI L11: Align the layout with a responsive grid

**Related:** `card-grid-layout`, `person-block-grid`

---

## Loading placeholder

`id: loading-placeholder` · level: pattern · source: ORCA

Placeholder cards in the shape of the content while a grid or feed loads, announced to screen readers.

Built from: `card-skeleton`

### Why

Placeholders in the final shape make waiting feel shorter and keep the layout still (Doherty threshold); the busy region tells assistive technology that content is on its way.

### When to use

- Grids and feeds that load after the page, or load more on scroll.

### How to use

- A region with `aria-busy="true"` and `aria-label="Loading videos"` holding two or three card skeletons; replace the whole region when the content arrives.

### Accessibility

- Remove `aria-busy` when the content is in; announce the result count politely.

#### Example: Loading

```django
<div class="orca-row orca-row--16" aria-busy="true" aria-label="Loading videos" style="align-items: flex-start"><div style="width: 12rem; padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border)"><div aria-hidden="true"><div class="orca-skeleton orca-aspect-16x9" style="margin-bottom: var(--orca-space-8)"></div><div class="orca-skeleton orca-skeleton--title"></div></div></div><div style="width: 12rem; padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border)"><div aria-hidden="true"><div class="orca-skeleton orca-aspect-16x9" style="margin-bottom: var(--orca-space-8)"></div><div class="orca-skeleton orca-skeleton--title"></div></div></div></div>
```

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower

**Related:** `feed-skeleton`, `video-grid`

---
