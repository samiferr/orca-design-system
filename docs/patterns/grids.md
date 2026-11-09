# Grids and collections

Repeating one component in a responsive grid or sequence: products, cameras, KPIs, a heat map, an event timeline.

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
<ul class="orca-product-grid">{% for n in "1234" %}<li><article class="orca-product"><div class="orca-product__image"><img src="{% static "orca/img/sample-street.svg" %}" alt=""></div><h3 class="orca-product__name"><a href="#">Dome camera {{ n }}, 4 MP</a></h3><p class="orca-product__price" style="margin: 0">€1{{ n }}9</p></article></li>{% endfor %}</ul>
```

**Classes:** `.orca-product-grid`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Product grid

---

## Camera grid

`id: camera-grid` · level: pattern · source: Tangerine

Camera cards in a grid, pinned cameras first, offline cameras clearly marked.

Built from: `camera-card`, `view-toggle`, `skeleton`

### Why

Operators scan cameras by their live view (Miller's law); keeping pinned cameras first saves the daily search (Fitts's law) and offline ones stand out by badge and word (Von Restorff, C03).

### When to use

- Dashboards and camera lists in card view.

### How to use

- `<ul class="orca-camera-grid">` of camera cards; order pinned first, then by name. Each image sits in a reserved 16:9 frame so the grid never jumps.
- Pair with the view toggle (cards or table) and a skeleton while snapshots load.

#### Example: Grid

```django
<ul class="orca-camera-grid">{% for c in sample.cameras|slice:":3" %}<li><article class="orca-card orca-card--link orca-camera-card">{% if c.status == "negative" %}<div class="orca-ratio orca-ratio--16x9 orca-frame--removed">No image since {{ c.last }}</div><span class="orca-badge orca-badge--negative orca-camera-card__flag">Offline</span>{% else %}<div class="orca-ratio orca-ratio--16x9"><img src="{% static "orca/img/sample-street.svg" %}" alt=""></div>{% endif %}
  <div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">{{ c.name }}</a></h3><span class="orca-status orca-small"><span class="orca-dot orca-dot--{{ c.status }}"></span>{{ c.status_text }} · {{ c.site }}</span></div></article></li>{% endfor %}</ul>
```

**Classes:** `.orca-camera-grid`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Fitts's law: big, close, well-spaced targets are faster and safer; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Camera grid

---

## KPI grid

`id: kpi-grid` · level: pattern · source: Tangerine

A row of stat cards summarising the state of things, linking to the detail behind each.

Built from: `stat-card`, `sparkline`, `delta`

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
  <a class="orca-stat-card" href="#"><p class="orca-stat-label">Visitors today</p><p class="orca-stat-value">12,480</p><div class="orca-stat-card__foot"><span class="orca-delta orca-delta--up">{% icon "arrow-up" size="xs" %}+8%</span>vs last Friday</div></a>
  <a class="orca-stat-card" href="#"><p class="orca-stat-label">Inside now</p><p class="orca-stat-value">1,204</p><div class="orca-stat-card__foot">of 1,500 capacity</div></a>
  <a class="orca-stat-card" href="#"><p class="orca-stat-label">Cameras online</p><p class="orca-stat-value">11 of 12</p><div class="orca-stat-card__foot"><span class="orca-with-icon">{% status_icon "negative" size="xs" %}Loading dock offline</span></div></a>
  <a class="orca-stat-card" href="#"><p class="orca-stat-label">Count accuracy</p><p class="orca-stat-value">96.4%</p><div class="orca-stat-card__foot">last 7 days</div></a>
</div>
```

**Classes:** `.orca-kpi-grid`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** KPI grid

---

## Capacity heat map

`id: capacity-heat-map` · level: pattern · source: Tangerine

Occupancy by weekday and hour as shaded cells with the value printed, and a legend of the scale.

Built from: `heat-cell`, `legend-item`

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

Built from: `timeline-item`, `thumbnail`, `relative-time`

### Why

Grouping by day chunks a long log (Miller's law); the timeline line and status dots show sequence and severity at a glance.

### When to use

- Alert lists, audit and incident views, a camera's history.

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
