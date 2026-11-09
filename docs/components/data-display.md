# Data display

Ways to present records and numbers: stat cards, lists, key/value lists, cards, tables, timelines and small charts.

## Stat card

`id: stat-card` · level: component · source: Tangerine

One measured value with its label, a descriptive icon, the change and its context, optionally with a sparkline.

Built from: `stat-label`, `delta`, `icon`, `sparkline`

### Why

A KPI is read in a second when the number dominates and its label and comparison sit right next to it (Von Restorff, Miller's law); a descriptive icon beside the label lets people find the card they want in a grid before reading (Miller's law: recognition), as in wise_people_analyzer.

### When to use

- Dashboards and summary rows: counts, rates, durations.

### When not to use

- More than about six cards in a row competing for attention: group them or pick the important ones.

### How to use

- `<div class="orca-stat-card">` with `.orca-stat-card__head` (`orca-stat-label` and `<span class="orca-stat-card__icon" aria-hidden="true">{% icon "user" %}</span>`), `orca-stat-value`, then `.orca-stat-card__foot` with a delta and the comparison period; optional `{% orca_sparkline values %}`.
- The icon describes what is measured (people, time, videos, accuracy), never its trend or status; it is decorative because the label says it. Use one icon per card and a different one for each card of a grid. In templates, pass `icon` with each stat.
- Make the whole card a link (`<a class="orca-stat-card">`) when it leads to the detail.

#### Example: Stat cards

```django
<div class="orca-card-grid" style="grid-template-columns: repeat(auto-fill, minmax(13rem, 1fr))">
  <div class="orca-stat-card"><div class="orca-stat-card__head"><p class="orca-stat-label">Visitors today</p><span class="orca-stat-card__icon" aria-hidden="true">{% icon "user" %}</span></div><p class="orca-stat-value">12,480</p><div class="orca-stat-card__foot"><span class="orca-delta orca-delta--up">{% icon "arrow-up" size="xs" %}+8%</span>vs last Friday</div>{% orca_sparkline "820,940,1200,1100,1480,1620,1540" "Visitors per hour today, rising" %}</div>
  <a class="orca-stat-card" href="#"><div class="orca-stat-card__head"><p class="orca-stat-label">Inside now</p><span class="orca-stat-card__icon" aria-hidden="true">{% icon "home" %}</span></div><p class="orca-stat-value">1,204</p><div class="orca-stat-card__foot">of 1,500 capacity</div></a>
  <div class="orca-stat-card"><div class="orca-stat-card__head"><p class="orca-stat-label">Average visit</p><span class="orca-stat-card__icon" aria-hidden="true">{% icon "clock" %}</span></div><p class="orca-stat-value">23 min</p><div class="orca-stat-card__foot"><span class="orca-delta orca-delta--flat">{% icon "minus" size="xs" %}0%</span>vs last week</div></div>
</div>
```

**Classes:** `.orca-stat-card`, `.orca-stat-card__head`, `.orca-stat-card__icon`, `.orca-stat-card__foot`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Miller's law: chunk information so working memory is not overloaded; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Stat card

---

## Key/value list

`id: key-value-list` · level: component · source: ORCA

Properties of a record as label and value pairs.

Built from: `muted-text`

### Why

Aligned labels and values are scanned down one edge and compared quickly (Practical UI L12, Miller's law).

### When to use

- Detail pages and side panels: a video's address, model, location.

### How to use

- `<dl class="orca-kv">` with `<div><dt>Label</dt><dd>Value</dd></div>` pairs; `--stacked` puts labels above values (narrow panels). Below 620px it stacks automatically.
- Empty values: write 'Not set' in muted text; never leave a blank.

#### Example: Video properties

```django
<dl class="orca-kv" style="max-width: 30rem">
  <div><dt>Format</dt><dd>MP4, 1080p</dd></div>
  <div><dt>Address</dt><dd><code class="orca-code">media.example.com/v/4821</code></dd></div>
  <div><dt>Site</dt><dd>North building</dd></div>
  <div><dt>Notes</dt><dd class="orca-muted">Not set</dd></div>
</dl>
```

**Classes:** `.orca-kv`, `.orca-kv--stacked`

**Principles applied:** Practical UI L12: Give text a stable alignment anchor; Miller's law: chunk information so working memory is not overloaded; Practical UI L15: Design for long and unusual content

**ORCA guide items covered:** Key/value list

---

## List

`id: list` · level: component · source: Tangerine

A divided list of items with optional visual, text and end detail.

Built from: `list-item`

### Why

A vertical list with consistent rows is the quickest structure to scan (Miller's law); hairline dividers separate items without boxes (Practical UI L01).

### When to use

- Short collections in panels: recent events, members, files.

### When not to use

- Comparing several attributes: use a table.

### How to use

- `<ul class="orca-list">` of `<li>` each containing one list item.
- Make the item itself the link or button (`a.orca-list-item`) so the whole row is the target.

#### Example: Members

```django
<ul class="orca-list" style="max-width: 26rem">
  <li><a class="orca-list-item" href="#"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span class="orca-list-item__text"><span class="orca-list-item__title">Ada Lovelace</span><span class="orca-list-item__desc">Administrator</span></span><span class="orca-list-item__end">Active today</span></a></li>
  <li><a class="orca-list-item" href="#"><span class="orca-avatar orca-avatar--s" aria-hidden="true">GH</span><span class="orca-list-item__text"><span class="orca-list-item__title">Grace Hopper</span><span class="orca-list-item__desc">Operator</span></span><span class="orca-list-item__end">3 days ago</span></a></li>
</ul>
```

**Classes:** `.orca-list`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI L01: Group related information; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** List

---

## List item

`id: list-item` · level: component · source: Tangerine

One row of a list: leading visual, title and description, trailing detail; static, link, button or selected.

Built from: `avatar`, `thumbnail`, `icon`

### Why

Fixed slots mean every row reads the same way (Practical UI F09); a 48px row with the whole width clickable is easy to hit (Fitts's law).

### When to use

- Inside a list; inside menus of rich options.

### How to use

- `.orca-list-item` (a `span`, `a` or `button`) with an optional avatar, thumbnail or icon, `.orca-list-item__text` (`__title`, `__desc`) and `.orca-list-item__end`.
- Selected: `aria-current="true"` (navigation) or `aria-selected="true"` (selection lists).

#### Example: Variants

```django
<ul class="orca-list" style="max-width: 26rem">
  <li><span class="orca-list-item">{% icon "file" size="m" %}<span class="orca-list-item__text"><span class="orca-list-item__title">weekly-report.csv</span><span class="orca-list-item__desc">48 KB</span></span></span></li>
  <li><button class="orca-list-item" type="button" aria-current="true">{% icon "snapshot" size="m" %}<span class="orca-list-item__text"><span class="orca-list-item__title">Entrance A</span><span class="orca-list-item__desc">Selected</span></span>{% icon "check" %}</button></li>
</ul>
```

**Classes:** `.orca-list-item`, `.orca-list-item__text`, `.orca-list-item__title`, `.orca-list-item__desc`, `.orca-list-item__end`, `.orca-list-item--selected`

**Principles applied:** Practical UI F09: Keep visual and functional behaviour consistent; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** List item

---

## Timeline item

`id: timeline-item` · level: component · source: Tangerine

One event in a vertical timeline: status dot, title, time and description.

Built from: `status-dot`, `time-label`

### Why

A line joining dots shows sequence at a glance (Gestalt continuity, Practical UI L01); the dot's tone shows what kind of event it was.

### When to use

- History of a record, a run's steps, an incident log.

### How to use

- `<ol class="orca-timeline">` of `<li class="orca-timeline__item">` with a dot, then a body containing `.orca-timeline__head` (`__title` + `__time`) and `.orca-timeline__desc`.
- Newest first for logs; oldest first for processes. Always give a time.

#### Example: Run history

```django
<ol class="orca-timeline" style="max-width: 28rem">
  <li class="orca-timeline__item"><span class="orca-dot orca-dot--positive"></span><div><div class="orca-timeline__head"><span class="orca-timeline__title">Run finished</span><time class="orca-timeline__time" datetime="2026-11-06T09:12">09:12</time></div><p class="orca-timeline__desc">118 of 120 shots taken.</p></div></li>
  <li class="orca-timeline__item"><span class="orca-dot orca-dot--caution"></span><div><div class="orca-timeline__head"><span class="orca-timeline__title">2 shots failed</span><time class="orca-timeline__time" datetime="2026-11-06T08:40">08:40</time></div><p class="orca-timeline__desc">Loading dock did not answer.</p></div></li>
  <li class="orca-timeline__item"><span class="orca-dot"></span><div><div class="orca-timeline__head"><span class="orca-timeline__title">Run started</span><time class="orca-timeline__time" datetime="2026-11-06T08:00">08:00</time></div></div></li>
</ol>
```

**Classes:** `.orca-timeline`, `.orca-timeline__item`, `.orca-timeline__head`, `.orca-timeline__title`, `.orca-timeline__time`, `.orca-timeline__desc`

**Principles applied:** Practical UI L01: Group related information; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Timeline item

---

## Sortable column header

`id: sortable-header` · level: component · source: Tangerine

A table header that sorts the column, showing the direction with an arrow and aria-sort.

Built from: `icon`

### Why

Sorting turns a table into an answer ('which video counted most?') (Tesler's law); the arrow and aria-sort show the order to everyone (C03).

### When to use

- Columns people compare: names, counts, dates, status.

### How to use

- `<th scope="col" aria-sort="descending"><a class="orca-sort" href="?sort=-count">Count{% icon "arrow-up" %}</a></th>`; columns not sorted have no aria-sort.
- Server-side: keep the other query parameters in the link; first click sorts the most useful way (descending for numbers and dates).

#### Example: Header row

```django
<table class="orca-table" style="max-width: 32rem"><thead><tr>
  <th scope="col" aria-sort="ascending"><a class="orca-sort" href="#">Video{% icon "arrow-up" %}</a></th>
  <th scope="col" class="is-num" aria-sort="none"><a class="orca-sort" href="#">Count{% icon "arrow-up" %}</a></th>
  <th scope="col"><a class="orca-sort" href="#">Last seen{% icon "arrow-up" %}</a></th>
</tr></thead><tbody><tr><td>Entrance A</td><td class="is-num">1,204</td><td>2 min ago</td></tr><tr><td>Entrance B</td><td class="is-num">980</td><td>5 min ago</td></tr></tbody></table>
```

**Classes:** `.orca-sort`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Sortable column header

---

## Legend item

`id: legend-item` · level: component · source: ORCA

A swatch, a series name and optionally its value, keying a chart.

Built from: `swatch`, `chart-dot`

### Why

Every colour on a chart needs a name next to the same colour, or colour-blind readers lose the chart (Practical UI C03).

### When to use

- Below or beside every multi-series chart and map.

### How to use

- `<ul class="orca-legend">` of `<li class="orca-legend__item">` with a swatch (or line swatch, or chart dot shape), the name and `.orca-legend__value`.
- `--column` for a vertical legend with values aligned right.

#### Example: Legend

```django
<ul class="orca-legend orca-legend--column" style="max-width: 16rem">
  <li class="orca-legend__item"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-1)"></span>Entrance A<span class="orca-legend__value">1,204</span></li>
  <li class="orca-legend__item"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-2)"></span>Entrance B<span class="orca-legend__value">980</span></li>
  <li class="orca-legend__item"><span class="orca-swatch orca-swatch--line" style="--orca-swatch: var(--orca-chart-3)"></span>Target<span class="orca-legend__value">1,000</span></li>
</ul>
```

**Classes:** `.orca-legend`, `.orca-legend__item`, `.orca-legend__value`, `.orca-legend--column`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Legend item

---

## Zone row

`id: zone-row` · level: component · source: ORCA

A counting zone in a list: its swatch, name, type, count and actions.

Built from: `zone-swatch`, `badge`, `row-actions`

### Why

The same swatch as on the video lets people match a zone to its row instantly (Miller's law); the type is a word, not only a pattern (C03).

### When to use

- Zone lists beside the zone editor and on video pages.

### How to use

- `<div class="orca-zone-row">` with a zone swatch, `.orca-zone-row__name` (name + type badge), `.orca-zone-row__count` and row actions.

#### Example: Zones

```django
<div style="max-width: 30rem">
  <div class="orca-zone-row"><span class="orca-zone-swatch" style="--orca-zone: var(--orca-teal-500)"></span><span class="orca-zone-row__name">Door line <span class="orca-badge orca-badge--grey">Count</span></span><span class="orca-zone-row__count orca-num">1,204</span><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="Edit Door line">{% icon "edit" %}</button></div>
  <div class="orca-zone-row"><span class="orca-zone-swatch orca-zone-swatch--exclude" style="--orca-zone: var(--orca-orange-500)"></span><span class="orca-zone-row__name">Staff area <span class="orca-badge orca-badge--grey">Excluded</span></span><span class="orca-zone-row__count orca-muted">–</span><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="Edit Staff area">{% icon "edit" %}</button></div>
</div>
```

**Classes:** `.orca-zone-row`, `.orca-zone-row__name`, `.orca-zone-row__count`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Zone row

---

## Line-count item

`id: line-count-item` · level: component · source: ORCA

A counting line with people in and out, each with a direction arrow.

Built from: `swatch`, `icon`, `tabular-number`

### Why

In and out are the two numbers people compare; arrows and words make the direction clear without colour (C03), and tabular digits keep them aligned.

### When to use

- Line-crossing counts on video and run pages.

### How to use

- `<div class="orca-line-count">` with a swatch, `.orca-line-count__name`, and two `.orca-line-count__dir` spans ('↓ 612 in', '↑ 598 out') using arrow icons and hidden words.

#### Example: Lines

```django
<div style="max-width: 30rem">
  <div class="orca-line-count"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-1)"></span><span class="orca-line-count__name">Main door</span><span class="orca-line-count__dir">{% icon "arrow-down" %}612<span class="orca-sr-only"> in</span></span><span class="orca-line-count__dir">{% icon "arrow-up" %}598<span class="orca-sr-only"> out</span></span></div>
  <div class="orca-line-count"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-2)"></span><span class="orca-line-count__name">Side door</span><span class="orca-line-count__dir">{% icon "arrow-down" %}88<span class="orca-sr-only"> in</span></span><span class="orca-line-count__dir">{% icon "arrow-up" %}91<span class="orca-sr-only"> out</span></span></div>
</div>
```

**Classes:** `.orca-line-count`, `.orca-line-count__name`, `.orca-line-count__dir`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Line-count item

---

## Media object

`id: media-object` · level: component · source: ORCA

An image or avatar beside a block of text.

Built from: `thumbnail`, `avatar`

### Why

Pairing a picture with its text binds them by proximity (Practical UI L01) and lets the eye recognise the item before reading.

### When to use

- Comments, notifications, search results, people and product summaries.

### How to use

- `<div class="orca-media">` with the media (thumbnail, avatar, icon) and `.orca-media__body`; `--center` aligns them vertically.
- The media is decorative (`alt=""`) when the body names the thing.

#### Example: Media object

```django
<div class="orca-media" style="max-width: 28rem"><img class="orca-thumb" src="{% static "orca/img/sample-street.svg" %}" alt="" width="48" height="48"><div class="orca-media__body"><span class="orca-card-title">Entrance A</span><span class="orca-small orca-muted">2 people at the door · 08:14</span></div></div>
```

**Classes:** `.orca-media`, `.orca-media__body`, `.orca-media--center`

**Principles applied:** Practical UI L01: Group related information; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Media object

---

## Card

`id: card` · level: component · source: Tangerine

A container for one object: optional media, body and footer. Outlined (default), elevated or filled.

Built from: `card-kicker`, `card-title`, `card-meta`

### Why

A card groups everything about one object in a common region (Practical UI L01) so grids of objects can be scanned and compared.

### When to use

- Collections of objects people browse: videos, sites, reports.
- Outlined in content; elevated over maps or media; filled inside panels.

### When not to use

- Wrapping every section of a page in a card: use spacing and section titles.

### How to use

- `<article class="orca-card">` with `.orca-card__media` (image in a reserved 16:9 box), `.orca-card__body` (kicker, title, meta, text) and `.orca-card__footer`.
- Variants: `--elevated`, `--filled`. Lay cards out in `.orca-card-grid`.

#### Example: Three variants

```django
<ul class="orca-card-grid">
  <li><article class="orca-card"><div class="orca-card__body"><p class="orca-card-kicker">Outlined</p><h3 class="orca-card-title">North building</h3><p class="orca-card-meta">12 videos · 5 zones</p></div></article></li>
  <li><article class="orca-card orca-card--elevated"><div class="orca-card__body"><p class="orca-card-kicker">Elevated</p><h3 class="orca-card-title">Warehouse</h3><p class="orca-card-meta">4 videos · 2 zones</p></div></article></li>
  <li><article class="orca-card orca-card--filled"><div class="orca-card__body"><p class="orca-card-kicker">Filled</p><h3 class="orca-card-title">Car park</h3><p class="orca-card-meta">2 videos</p></div></article></li>
</ul>
```

**Classes:** `.orca-card`, `.orca-card--elevated`, `.orca-card--filled`, `.orca-card__media`, `.orca-card__body`, `.orca-card-grid`

**Principles applied:** Practical UI L01: Group related information; Practical UI C12: Use elevation consistently

**Related:** `card-footer`, `linked-card`

**ORCA guide items covered:** Card; Card (outlined, elevated, filled)

---

## Card footer

`id: card-footer` · level: component · source: ORCA

The bottom strip of a card for status and actions.

Built from: `status-dot`, `icon-button`

### Why

Keeping actions in the same place on every card makes them predictable (Practical UI F09) and separates reading from acting.

### When to use

- Cards with a status or one or two actions.

### How to use

- `<div class="orca-card__footer">` with a status on the left and `.orca-card__footer-end` holding icon buttons or a small button.
- Footer controls stay clickable inside a linked card (they sit above the stretched link).

#### Example: Footer

```django
<article class="orca-card" style="max-width: 18rem"><div class="orca-card__body"><h3 class="orca-card-title">Entrance A</h3><p class="orca-card-meta">North building</p></div>
  <div class="orca-card__footer"><span class="orca-status orca-small"><span class="orca-dot orca-dot--positive"></span>Online</span><span class="orca-card__footer-end"><button class="orca-icon-button orca-icon-button--sm orca-pin" type="button" aria-pressed="false" aria-label="Pin Entrance A" data-orca-toggle>{% icon "pin" %}</button><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="More actions for Entrance A">{% icon "more" %}</button></span></div></article>
```

**Classes:** `.orca-card__footer`, `.orca-card__footer-end`

**Principles applied:** Practical UI F09: Keep visual and functional behaviour consistent; Practical UI L14: Reduce travel between related actions

**ORCA guide items covered:** Card footer

---

## Linked card

`id: linked-card` · level: component · source: ORCA

A card whose whole area opens the object, built with one real link on the title.

Built from: `card`

### Why

The whole card is a large target (Fitts's law) while screen readers hear one clear link, the title, instead of a card full of link text.

### When to use

- Cards whose main action is opening the object.

### How to use

- Add `--link` to the card and put `<a class="orca-card__link" href=…>` around the title text; its `::after` covers the card.
- Other controls inside go in the footer, which sits above the link. Never nest links.

#### Example: Linked cards

```django
<ul class="orca-card-grid">
  <li><article class="orca-card orca-card--link"><div class="orca-card__media"><img src="{% static "orca/img/sample-street.svg" %}" alt=""></div><div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">Entrance A</a></h3><p class="orca-card-meta">North building · online</p></div></article></li>
  <li><article class="orca-card orca-card--link"><div class="orca-card__media"><img src="{% static "orca/img/sample-floor.svg" %}" alt=""></div><div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">North building plan</a></h3><p class="orca-card-meta">Updated 3 March</p></div></article></li>
</ul>
```

**Classes:** `.orca-card--link`, `.orca-card__link`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI W14: Give links meaningful destination names

**ORCA guide items covered:** Linked card

---

## Accordion

`id: accordion` · level: component · source: Tangerine

A stack of sections that open and close, built on details and summary.

Built from: `chevron`

### Why

Collapsing secondary content lets people see the whole list of topics first and open only what they need (Practical UI S04, Miller's law).

### When to use

- FAQs, advanced settings, long lists of grouped details.

### When not to use

- Content most people need: show it.
- Steps of a process: use steps.

### How to use

- `<div class="orca-accordion">` of `<details>` with `<summary>` (chevron + heading text) and `.orca-accordion__panel`.
- Write summaries as the question or topic people look for. Several sections may be open at once.

#### Example: Accordion

```django
<div class="orca-accordion" style="max-width: 32rem">
  <details open><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>How often are counts updated?</summary><div class="orca-accordion__panel"><p class="orca-p">Every minute. Reports group older data by hour.</p></div></details>
  <details><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>Can I export the data?</summary><div class="orca-accordion__panel"><p class="orca-p">Yes, as CSV from any report.</p></div></details>
</div>
```

**Classes:** `.orca-accordion`, `.orca-accordion__panel`

**Principles applied:** Practical UI S04: Reveal secondary information when needed; Miller's law: chunk information so working memory is not overloaded; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Accordion

---

## Steps

`id: steps` · level: component · source: Tangerine

The steps of a process with done, current and upcoming markers.

Built from: `step-marker`

### Why

Showing progress through a multi-step task motivates finishing and sets expectations (Peak–end rule, goal gradient); splitting a task into steps lowers each decision (Hick's law).

### When to use

- Setup flows and multi-step forms of 3 to 6 steps.

### How to use

- `<ol class="orca-steps">` of `.orca-steps__item` (`--done` or `aria-current="step"`) each with a step marker and `.orca-steps__title` (+ `__desc`).
- Done steps may link back for review. `--vertical` for side panels; on phones descriptions hide.

#### Example: Setup steps

```django
<ol class="orca-steps">
  <li class="orca-steps__item orca-steps__item--done"><span class="orca-step-marker orca-step-marker--done" aria-hidden="true"></span><span class="orca-steps__title"><a href="#">Connect media server</a><span class="orca-sr-only">, done</span></span></li>
  <li class="orca-steps__item" aria-current="step"><span class="orca-step-marker orca-step-marker--current" aria-hidden="true"></span><span class="orca-steps__title">Choose videos</span><span class="orca-steps__desc">Pick the doors to count</span></li>
  <li class="orca-steps__item"><span class="orca-step-marker" aria-hidden="true"></span><span class="orca-steps__title">Draw zones</span></li>
</ol>
```

**Classes:** `.orca-steps`, `.orca-steps__item`, `.orca-steps__item--done`, `.orca-steps__title`, `.orca-steps__desc`, `.orca-steps--vertical`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Hick's law: fewer, clearer choices mean faster decisions; Practical UI R16: Break long forms into sensible steps

**ORCA guide items covered:** Steps

---

## Tree

`id: tree` · level: component · source: Tangerine

A hierarchy of items that expand and collapse: sites, buildings, videos.

Built from: `chevron`

### Why

Nested disclosure shows structure and hides depth until needed (Practical UI S04); indentation and a guide line show who belongs to whom (Gestalt).

### When to use

- Browsing a hierarchy of objects, such as locations or folders.

### When not to use

- Navigation between pages: use the nav tree.

### How to use

- `<ul class="orca-tree">` with `<li><details><summary>` for branches and `.orca-tree__leaf` for leaves; `.orca-tree__meta` for counts.
- Built on details, so it works with the keyboard and screen readers without script; current leaf `aria-current="true"`.

#### Example: Sites

```django
<ul class="orca-tree" style="max-width: 20rem">
  <li><details open><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>North building<span class="orca-tree__meta">3</span></summary>
    <ul><li><a class="orca-tree__leaf" href="#" aria-current="true">Entrance A</a></li><li><a class="orca-tree__leaf" href="#">Entrance B</a></li>
      <li><details><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>Basement<span class="orca-tree__meta">1</span></summary><ul><li><a class="orca-tree__leaf" href="#">Loading dock</a></li></ul></details></li></ul></details></li>
  <li><details><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>Warehouse<span class="orca-tree__meta">4</span></summary><ul><li><a class="orca-tree__leaf" href="#">Gate 1</a></li></ul></details></li>
</ul>
```

**Classes:** `.orca-tree`, `.orca-tree__leaf`, `.orca-tree__meta`

**Principles applied:** Practical UI S04: Reveal secondary information when needed; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Tree

---

## Avatar group

`id: avatar-group` · level: component · source: Tangerine

Overlapping avatars of the people involved, with '+N' for the rest.

Built from: `avatar`

### Why

A few faces show who is involved at a glance without listing everyone (Miller's law); the count tells how many more there are.

### When to use

- Assignees, attendees, members on cards and headers.

### How to use

- `<ul class="orca-avatar-group" aria-label="5 members">` of `<li>` avatars (each with the person's name as `title`/`aria-label`), ending with `.orca-avatar-group__more` '+2'.
- Show at most 3 to 5; link the group to the full list.

#### Example: Members

```django
<ul class="orca-avatar-group" aria-label="5 members: Ada Lovelace, Grace Hopper, Alan Turing and 2 more">
  <li><span class="orca-avatar orca-avatar--s" title="Ada Lovelace">AL</span></li><li><span class="orca-avatar orca-avatar--s" title="Grace Hopper">GH</span></li><li><span class="orca-avatar orca-avatar--s" title="Alan Turing">AT</span></li><li><span class="orca-avatar orca-avatar--s orca-avatar-group__more">+2</span></li>
</ul>
```

**Classes:** `.orca-avatar-group`, `.orca-avatar-group__more`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Avatar group

---

## Table card

`id: table-card` · level: component · source: ORCA

A panel holding a titled table and its pager.

Built from: `panel-header`, `table-pager`, `sortable-header`

### Why

A titled frame tells people what the rows are before they read them, and keeps the table's actions and paging next to it (Practical UI L01, L14).

### When to use

- Tables on dashboards and detail pages.

### How to use

- `<section class="orca-table-card">` with a panel header (title, description, actions), `.orca-table-wrap` > `table.orca-table`, then a table pager.
- Numbers right-aligned with `.is-num`; `--compact` table for dense data. Empty: a no-data state in one full-width cell.

#### Example: Table card

```django
<section class="orca-table-card" aria-labelledby="tc-t">
  <div class="orca-panel-header"><div class="orca-panel-header__text"><h2 class="orca-panel-title" id="tc-t">Busiest entrances</h2><p class="orca-panel-header__desc">Today, all sites</p></div><div class="orca-panel-header__actions"><a class="orca-button orca-button--ghost orca-button--dense" href="#">View report</a></div></div>
  <div class="orca-table-wrap"><table class="orca-table"><thead><tr><th scope="col">Entrance</th><th scope="col">Site</th><th scope="col" class="is-num">Visitors</th></tr></thead>
    <tbody><tr><td>Entrance A</td><td>North building</td><td class="is-num">4,812</td></tr><tr><td>Gate 1</td><td>Warehouse</td><td class="is-num">2,140</td></tr><tr><td>Entrance B</td><td>North building</td><td class="is-num">1,980</td></tr></tbody></table></div>
  <div class="orca-table-pager"><span class="orca-num">1–3 of 14</span><span class="orca-table-pager__nav"><button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Previous page" disabled>{% icon "chevron-left" %}</button><button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Next page">{% icon "chevron-right" %}</button></span></div>
</section>
```

**Classes:** `.orca-table-card`, `.orca-table`, `.orca-table-wrap`, `.orca-table--compact`

**Principles applied:** Practical UI L01: Group related information; Practical UI L14: Reduce travel between related actions; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Table card

---

## Property row

`id: property-row` · level: component · source: ORCA

One editable key and value pair with a remove button, repeated to edit free-form properties.

Built from: `text-input`, `icon-button`, `label`

### Why

Free-form metadata is inherently variable (Tesler's law); one row per pair with Add and Remove keeps it structured and forgiving (Postel's law).

### When to use

- Custom properties, labels, HTTP headers, environment values.

### How to use

- `<div class="orca-property-rows" id=…>` of `<div class="orca-property-row" data-orca-row>` (key field, value field, remove icon button `data-orca-remove-row`).
- An add-row button with `data-orca-add-row="template-id"` clones a `<template>`; Django formsets: use `__prefix__` in the template and point `data-orca-total` at TOTAL_FORMS.
- Name the remove button after the key ('Remove property site-code').

#### Example: Properties

```django
<div class="orca-property-rows" id="pr-list">
  <div class="orca-property-row" data-orca-row><div><label class="orca-label" for="pr-k0">Key</label><input class="orca-input" id="pr-k0" value="site-code"></div><div><label class="orca-label" for="pr-v0">Value</label><input class="orca-input" id="pr-v0" value="NB-01"></div><button class="orca-icon-button" type="button" aria-label="Remove property site-code" data-orca-remove-row>{% icon "delete" %}</button></div>
</div>
<template id="pr-tpl"><div class="orca-property-row" data-orca-row><div><label class="orca-label" for="pr-k__prefix__">Key</label><input class="orca-input" id="pr-k__prefix__"></div><div><label class="orca-label" for="pr-v__prefix__">Value</label><input class="orca-input" id="pr-v__prefix__"></div><button class="orca-icon-button" type="button" aria-label="Remove property" data-orca-remove-row>{% icon "delete" %}</button></div></template>
<button class="orca-button orca-button--ghost" type="button" data-orca-add-row="pr-tpl" aria-controls="pr-list" style="margin-top: var(--orca-space-8)">{% icon "plus" %}Add property</button>
```

**Classes:** `.orca-property-row`, `.orca-property-rows`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Property row (key, value, remove)

---

## Activity entry

`id: activity-entry` · level: component · source: ORCA

One change in an audit log: what happened, who did it, when, and the before and after values.

Built from: `avatar`, `badge`, `time-label`

### Why

Trust in shared data depends on knowing who changed what (Peak–end rule); showing the old value struck through beside the new one makes the change readable without comparing screens.

### When to use

- Activity feeds and history tabs of records.

### How to use

- `<div class="orca-activity">` with the actor's avatar, `.orca-activity__head` (action badge, actor, `.orca-activity__time`), and a `<dl class="orca-activity__change">` of field, `<del>` old and `<ins>` new values.
- Times are absolute in logs ('6 Nov, 08:14'), relative in feeds.

#### Example: Change

```django
<div class="orca-activity" style="max-width: 34rem"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span>
  <div class="orca-activity__head"><span class="orca-badge orca-badge--subtle orca-badge--info">Updated</span><strong>Ada Lovelace</strong> changed Entrance A<time class="orca-activity__time" datetime="2026-11-06T08:14">6 Nov, 08:14</time></div>
  <dl class="orca-activity__change"><dt>Name</dt><dd><del>Front door</del> → <ins>Entrance A</ins></dd><dt>Interval</dt><dd><del>15 min</del> → <ins>5 min</ins></dd></dl></div>
```

**Classes:** `.orca-activity`, `.orca-activity__head`, `.orca-activity__time`, `.orca-activity__change`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Activity entry (badge, actor, time, before and after)

---

## Carousel

`id: carousel` · level: component · source: ORCA

One slide at a time with previous and next buttons, dots and a count.

Built from: `carousel-dot`, `icon-button`, `media-frame`

### Why

When only one image fits, controls and a count ('2 of 5') show there is more and where you are (Practical UI S06); native scroll-snap keeps swiping natural on touch.

### When to use

- A few related images: snapshots of an event, product photos.

### When not to use

- Important content people must not miss: list it.
- Auto-advancing slides.

### How to use

- `<section class="orca-carousel" data-orca-carousel aria-roledescription="carousel" aria-label=…>` with a `.orca-carousel__track` list of slides and `.orca-carousel__controls` (prev and next icon buttons with `data-orca-prev`/`data-orca-next`, dots with `data-orca-slide="i"`, `.orca-carousel__count`).
- Each slide's image has its own alt text; hidden slides get `aria-hidden` from orca.js.

#### Example: Event snapshots

```django
<section class="orca-carousel" data-orca-carousel aria-roledescription="carousel" aria-label="Event snapshots" style="max-width: 24rem">
  <ul class="orca-carousel__track">
    <li><div class="orca-ratio orca-ratio--16x9"><img src="{% static "orca/img/sample-street.svg" %}" alt="08:14, two people at the door"></div></li>
    <li><div class="orca-ratio orca-ratio--16x9"><img src="{% static "orca/img/sample-floor.svg" %}" alt="Floor plan with the door highlighted"></div></li>
    <li><div class="orca-ratio orca-ratio--16x9"><img src="{% static "orca/img/sample-street.svg" %}" alt="08:15, the door is clear"></div></li>
  </ul>
  <div class="orca-carousel__controls">
    <button class="orca-icon-button" type="button" aria-label="Previous image" data-orca-prev>{% icon "chevron-left" %}</button>
    <div class="orca-carousel__dots"><button class="orca-carousel-dot" type="button" aria-label="Image 1" data-orca-slide="0"></button><button class="orca-carousel-dot" type="button" aria-label="Image 2" data-orca-slide="1"></button><button class="orca-carousel-dot" type="button" aria-label="Image 3" data-orca-slide="2"></button></div>
    <button class="orca-icon-button" type="button" aria-label="Next image" data-orca-next>{% icon "chevron-right" %}</button>
    <span class="orca-carousel__count" aria-live="polite">1 of 3</span>
  </div>
</section>
```

**Classes:** `.orca-carousel`, `.orca-carousel__track`, `.orca-carousel__controls`, `.orca-carousel__dots`, `.orca-carousel__count`

**Principles applied:** Practical UI S06: Make essential content visible or discoverable; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Carousel

---

## Scroller

`id: scroller` · level: component · source: ORCA

A horizontal row that scrolls and snaps, showing part of the next item.

Built from: `card`

### Why

A peeking next item is the clue that more exists (Practical UI S06); snapping stops half-visible items.

### When to use

- Rows of cards on phones; quick filters; recent items.

### How to use

- `<ul class="orca-scroller" tabindex="0" aria-label=…>` of items (each 80% wide up to 16rem).
- The scroller is focusable so keyboard users can scroll it with arrow keys.

#### Example: Scroller

```django
<ul class="orca-scroller" tabindex="0" aria-label="Sites" style="max-width: 30rem; padding-inline: 0">
  <li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">North building</h3><p class="orca-card-meta">12 videos</p></div></li>
  <li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Warehouse</h3><p class="orca-card-meta">4 videos</p></div></li>
  <li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Car park</h3><p class="orca-card-meta">2 videos</p></div></li>
</ul>
```

**Classes:** `.orca-scroller`

**Principles applied:** Practical UI S06: Make essential content visible or discoverable; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Scroller (scroll-snap region)

---

## Sparkline

`id: sparkline` · level: component · source: ORCA

A tiny trend line without axes, ending with a dot on the latest value.

Built from: `stat-value`

### Why

The shape of a trend is understood pre-attentively; a sparkline adds that context to a number without a full chart (Miller's law). The end dot marks 'now'.

### When to use

- Beside a stat value or in a table cell.

### When not to use

- When exact values matter: use a chart with axes.

### How to use

- `{% orca_sparkline values "Visitors per hour today, rising" %}` from a list or a comma-separated string.
- Always pair it with the number it summarises; the label is read by screen readers.

#### Example: Sparklines

```django
<div class="orca-stack" style="max-width: 12rem">{% orca_sparkline "5,8,6,9,12,10,14,13,16" %}{% orca_sparkline "20,18,19,15,12,13,9" "Errors per day, falling" %}</div>
```

**Classes:** `.orca-sparkline`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Sparkline

---

## Donut chart

`id: donut-chart` · level: component · source: ORCA

A ring of up to about five shares with the total in the middle and a legend with values.

Built from: `legend-item`

### Why

A part-of-whole split is grasped quickly when there are few parts; the legend gives the exact numbers and names every colour (Practical UI C03).

### When to use

- 2 to 5 shares of one total: visitors by entrance, alerts by type.

### When not to use

- More than 5 parts or comparing similar shares: use a bar chart.

### How to use

- `{% orca_donut segments total_label="Visitors" %}` with `[("Entrance A", 4812), …]`, dicts, or a string `"Entrance A:4812, Gate 1:2140"`.
- Series use `--orca-chart-1…8` in order; the SVG's label lists every share in words.

#### Example: Visitors by entrance

```django
{% orca_donut "Entrance A:4812, Gate 1:2140, Entrance B:1980, Car park:640" total_label="Visitors" %}
```

**Classes:** `.orca-donut`, `.orca-donut__chart`, `.orca-donut__total`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Donut chart

---

## Chart frame

`id: chart-frame` · level: component · source: ORCA

The frame every chart sits in: title, subtitle, legend, a reserved plot area, a source line and the data as a table.

Built from: `legend-item`, `no-data-state`, `panel-title`

### Why

A chart is only useful with its title, units and source (Practical UI W04); reserving the plot area prevents layout jumps (Doherty), and the data table gives everyone the exact values (Postel's law).

### When to use

- Every chart, whatever draws it (SVG, canvas, a charting library).

### How to use

- `<figure class="orca-chart-frame">` with `.orca-chart-frame__head` (title + subtitle with the unit; actions), the legend, `.orca-chart-frame__plot` (set `--orca-ratio`), `<figcaption class="orca-chart-frame__caption">` for source and time zone, and `<details><summary>Show data</summary>` with a table.
- Colours from `--orca-chart-*` tokens; text inside charts uses text tokens so both themes work.

#### Example: Frame with a placeholder plot

```django
<figure class="orca-chart-frame" style="max-width: 36rem">
  <div class="orca-chart-frame__head"><div><h3 class="orca-panel-title">Visitors per hour</h3><p class="orca-small orca-muted">Today, people per hour, all entrances</p></div><button class="orca-button orca-button--ghost orca-button--dense" type="button">Export</button></div>
  <ul class="orca-legend"><li class="orca-legend__item"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-1)"></span>Entrance A</li><li class="orca-legend__item"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-2)"></span>Entrance B</li></ul>
  <div class="orca-chart-frame__plot" style="--orca-ratio: 3 / 1"><div class="orca-no-data" style="height: 100%"><strong>Chart area</strong>Draw the chart here.</div></div>
  <figcaption class="orca-chart-frame__caption">Source: line counts · Europe/Paris · updated 09:14</figcaption>
  <details><summary>Show data</summary><table class="orca-table orca-table--compact"><thead><tr><th scope="col">Hour</th><th scope="col" class="is-num">Entrance A</th><th scope="col" class="is-num">Entrance B</th></tr></thead><tbody><tr><td>08:00</td><td class="is-num">412</td><td class="is-num">380</td></tr></tbody></table></details>
</figure>
```

**Classes:** `.orca-chart-frame`, `.orca-chart-frame__head`, `.orca-chart-frame__plot`, `.orca-chart-frame__caption`

**Principles applied:** Practical UI W04: Lead with the information people seek; Doherty threshold: respond within 400 ms; show progress for anything slower; Postel's law: accept varied input, output reliable and accessible UI; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Chart frame

---

## Big number

`id: big-number` · level: component · source: ORCA

One large figure with the statement it supports and where it comes from.

Built from: `stat-value`, `small-text`

### Why

A single striking number is remembered (Von Restorff, Peak–end rule); the statement and the source keep it honest.

### When to use

- Editorial factoids, live counts beside a video, report highlights.

### When not to use

- Several big numbers side by side: use stat cards in a KPI grid.

### How to use

- `<figure class="orca-factoid"><span class="orca-factoid__number">−34%</span><figcaption><p class="orca-factoid__text">…</p><p class="orca-factoid__source">…</p></figcaption></figure>`.
- Numbers as digits with separators and the sign written (W11).

#### Example: Big number

```django
<figure class="orca-factoid" style="margin: 0"><span class="orca-factoid__number">2,480</span><figcaption><p class="orca-factoid__text">videos published this year</p><p class="orca-factoid__source">Library, November 2026</p></figcaption></figure>
```

**Classes:** `.orca-factoid`, `.orca-factoid__number`, `.orca-factoid__text`, `.orca-factoid__source`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Peak–end rule: people judge an experience by its peak and its end; Practical UI W11: Make numbers scannable

**Related:** `factoid`

---

## Summary tile

`id: summary-tile` · level: component · source: ORCA

A count with its status word, as a link that filters the list to that status.

Built from: `stat-value`, `status-dot`

### Why

Counts by status answer 'how many need me?' at a glance (Miller's law) and double as the quickest filter (Fitts's law: a large target); the dot is paired with a word (C03).

### When to use

- Above lists and tables whose records have a status.

### How to use

- `<a class="orca-summary-tile" href="?status=offline"><span class="orca-summary-tile__value">1</span><span class="orca-summary-tile__label"><span class="orca-dot orca-dot--negative"></span>Offline</span></a>`.
- The tile for the current filter has `aria-current="true"`.

#### Example: Summary tile

```django
<a class="orca-summary-tile" href="#" style="max-width: 10rem"><span class="orca-summary-tile__value">10</span><span class="orca-summary-tile__label"><span class="orca-dot orca-dot--positive"></span>Published</span></a>
```

**Classes:** `.orca-summary-tile`, `.orca-summary-tile__value`, `.orca-summary-tile__label`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI C03: Communicate meaning beyond colour

**Related:** `summary-tiles`

---

## Heat-map row

`id: heat-row` · level: component · source: ORCA

One labelled row of heat-map cells, each with its value printed.

Built from: `heat-cell`

### Why

A row per weekday or resource lets people compare hours along a line (Miller's law); printing the value means the shade is never the only carrier of meaning (C03).

### When to use

- Capacity and occupancy heat maps, availability grids.

### How to use

- `<tr><th scope="row">Mon</th><td class="orca-heat orca-heat--3">142</td>…</tr>` inside `table.orca-heatmap`.

### Accessibility

- The row header names the row; the column headers name the hours.

#### Example: Row

```django
<table class="orca-heatmap"><tbody><tr><th scope="row">Mon</th><td class="orca-heat orca-heat--1">12</td><td class="orca-heat orca-heat--3">142</td><td class="orca-heat orca-heat--5">310</td></tr></tbody></table>
```

**Classes:** `.orca-heatmap`, `.orca-heat`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI C03: Communicate meaning beyond colour

**Related:** `capacity-heat-map`

---

## Column header

`id: column-header` · level: component · source: ORCA

A board column's title with its card count and, when set, its limit.

Built from: `badge`

### Why

The count and the limit show at a glance where work piles up (Miller's law, Von Restorff when over the limit).

### When to use

- Kanban columns, grouped lists.

### How to use

- `<h3 class="orca-board__head">In progress <span class="orca-badge orca-badge--grey">3</span><span class="orca-board__limit">limit 4</span></h3>`; over the limit, the column gets `.is-over`.

#### Example: Column header

```django
<h3 class="orca-board__head">In progress <span class="orca-badge orca-badge--grey">3</span><span class="orca-board__limit">limit 4</span></h3>
```

**Classes:** `.orca-board__head`, `.orca-board__limit`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**Related:** `kanban-board`

---
