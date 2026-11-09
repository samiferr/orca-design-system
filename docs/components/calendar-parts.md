# Calendar parts

The pieces month, week, day and agenda views are built from. Each states the date in words for screen readers.

## Day cell

`id: day-cell` · level: component · source: ORCA

One day of a month view: day number, up to three events and a '+N more' link.

Built from: `day-number`, `today-marker`, `event-chip`, `more-events-link`, `holiday-label`

### Why

A fixed cell height keeps weeks aligned so the month reads as a grid (Jakob's law); capping visible events and linking to the rest keeps cells legible (Miller's law).

### When to use

- Month views.

### How to use

- `<td class="orca-cal-cell">` with `.orca-cal-cell__inner`: the day number as a link to the day view (`.orca-cal-cell__day`, `aria-label` with the full date), event chips, holiday label, more-events link.
- States: `--today` (filled red day number + `aria-current="date"`), `--outside`, `--weekend`, `--holiday`, `--selected`, `--closed` (hatched).
- On phones cells shrink and chips hide; the day's dot and count stay.

#### Example: Cells

```django
<table class="orca-cal-month" style="max-width: 36rem"><tbody><tr>
  <td class="orca-cal-cell"><div class="orca-cal-cell__inner"><a class="orca-cal-cell__day" href="#" aria-label="Thursday 5 November">5</a><button class="orca-event-chip" type="button"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-1)"></span><span class="orca-event-chip__time">09:00</span><span class="orca-event-chip__title">Delivery</span></button></div></td>
  <td class="orca-cal-cell orca-cal-cell--today"><div class="orca-cal-cell__inner"><a class="orca-cal-cell__day" href="#" aria-current="date" aria-label="Friday 6 November, today">6</a><button class="orca-event-chip" type="button"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-2)"></span><span class="orca-event-chip__time">10:00</span><span class="orca-event-chip__title">Audit</span></button><button class="orca-event-chip" type="button"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-1)"></span><span class="orca-event-chip__time">14:00</span><span class="orca-event-chip__title">Training</span></button><button class="orca-more-link" type="button" aria-label="3 more events on 6 November">+3 more</button></div></td>
  <td class="orca-cal-cell orca-cal-cell--weekend orca-cal-cell--holiday"><div class="orca-cal-cell__inner"><a class="orca-cal-cell__day" href="#" aria-label="Saturday 7 November, Founders day">7</a><span class="orca-holiday-label">Founders day</span></div></td>
</tr></tbody></table>
```

**Classes:** `.orca-cal-cell`, `.orca-cal-cell__inner`, `.orca-cal-cell__day`, `.orca-cal-cell--today`, `.orca-cal-cell--outside`, `.orca-cal-cell--weekend`, `.orca-cal-cell--holiday`, `.orca-cal-cell--selected`, `.orca-cal-cell--closed`

**Principles applied:** Jakob's law: work the way products people already know work; Miller's law: chunk information so working memory is not overloaded; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Day cell

---

## Week header

`id: week-header` · level: component · source: ORCA

The week number and its date range, heading a week view.

Built from: `week-number`, `date-label`

### Why

Teams that plan in weeks need the number; the range confirms which days it covers (Tesler's law: no mental arithmetic).

### When to use

- Week views, sprint and roster pages.

### How to use

- `<div class="orca-week-header">` with a week number and `.orca-week-header__range` dates ('2–8 November 2026').

#### Example: Week 45

```django
<div class="orca-week-header"><span class="orca-week-number" title="Week 45">W45</span><span class="orca-week-header__range"><time datetime="2026-11-02">2</time>–<time datetime="2026-11-08">8 November 2026</time></span></div>
```

**Classes:** `.orca-week-header`, `.orca-week-header__range`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Week header

---

## Weekday header

`id: weekday-header` · level: component · source: ORCA

The row of weekday names above a month or week grid.

Built from: `weekday-name`

### Why

Column headers tell people which day each column is; short uppercase labels fit narrow columns (Practical UI W07) and the full name is in the abbreviation.

### When to use

- Top of month and week grids.

### How to use

- `<thead class="orca-cal-weekdays"><tr>` of `<th scope="col"><abbr title="Monday">Mon</abbr></th>`; weekend columns get `.is-weekend`.
- Start on the locale's first weekday.

#### Example: Header

```django
<table class="orca-cal-month"><thead class="orca-cal-weekdays"><tr><th scope="col"><abbr title="Monday">Mon</abbr></th><th scope="col"><abbr title="Tuesday">Tue</abbr></th><th scope="col"><abbr title="Wednesday">Wed</abbr></th><th scope="col"><abbr title="Thursday">Thu</abbr></th><th scope="col"><abbr title="Friday">Fri</abbr></th><th scope="col" class="is-weekend"><abbr title="Saturday">Sat</abbr></th><th scope="col" class="is-weekend"><abbr title="Sunday">Sun</abbr></th></tr></thead></table>
```

**Classes:** `.orca-cal-weekdays`

**Principles applied:** Practical UI W07: Reserve uppercase for short labels; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Weekday header

---

## Week row

`id: week-row` · level: component · source: ORCA

One row of a month grid: the week number and seven day cells.

Built from: `day-cell`, `week-number`

### Why

Grouping days into week rows chunks the month (Miller's law); the week number on the row helps teams that plan by week.

### When to use

- Month views.

### How to use

- `<tr class="orca-cal-week">` with an optional `<th scope="row">45</th>` then seven `td.orca-cal-cell`.

#### Example: Row

```django
<table class="orca-cal-month"><tbody><tr class="orca-cal-week"><th scope="row"><abbr title="Week 45">45</abbr></th>{% for d in "2345678" %}<td class="orca-cal-cell{% if forloop.counter > 5 %} orca-cal-cell--weekend{% endif %}" style="height: 3rem"><div class="orca-cal-cell__inner"><a class="orca-cal-cell__day" href="#">{{ d }}</a></div></td>{% endfor %}</tr></tbody></table>
```

**Classes:** `.orca-cal-week`, `.orca-cal-month`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Week row

---

## Hour row

`id: hour-row` · level: component · source: ORCA

One hour of a day or week view: the hour label and two half-hour slots.

Built from: `hour-gridline`, `time-slot`, `time-label`

### Why

Hour lines give the day a scale (Practical UI S02: faint, not competing); the label in the gutter keeps the slots free for events.

### When to use

- Day and week views, resource schedulers.

### How to use

- `<div class="orca-hour-row">` with `.orca-hour-row__label` (`<time>`) and `.orca-hour-row__slots` holding two time slots.
- Show working hours by default and scroll to 'now' on load.

#### Example: Two hours

```django
<div style="max-width: 24rem; padding-top: var(--orca-space-8)">
  <div class="orca-hour-row"><time class="orca-hour-row__label" datetime="09:00">09:00</time><div class="orca-hour-row__slots"><button class="orca-slot" type="button" aria-label="Add event at 09:00"><span class="orca-slot__hint">+ Add</span></button><button class="orca-slot" type="button" aria-label="Add event at 09:30"><span class="orca-slot__hint">+ Add</span></button></div></div>
  <div class="orca-hour-row"><time class="orca-hour-row__label" datetime="10:00">10:00</time><div class="orca-hour-row__slots"><span class="orca-slot orca-slot--busy">Busy</span><button class="orca-slot" type="button" aria-label="Add event at 10:30"><span class="orca-slot__hint">+ Add</span></button></div></div>
</div>
```

**Classes:** `.orca-hour-row`, `.orca-hour-row__label`, `.orca-hour-row__slots`

**Principles applied:** Practical UI S02: Remove styles that compete without communicating; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Hour row

---

## Time slot

`id: time-slot` · level: component · source: ORCA

An empty half-hour in a day view that creates an event when chosen; free, busy or selected.

Built from: `availability-color`

### Why

Clicking where the event should go is the most direct way to create it (Practical UI F03, Fitts's law); the hint appears on hover and focus only, so the grid stays calm.

### When to use

- Day and week views, booking grids.

### How to use

- `<button class="orca-slot" type="button" aria-label="Add event at 09:30, Friday 6 November">` with a `.orca-slot__hint`; busy slots are spans with `--busy`; chosen slots use `aria-pressed="true"`.
- Keep at least 24px height; snap new events to the slot.

#### Example: Slots

```django
<div style="max-width: 16rem; border: var(--orca-hairline) solid var(--orca-border-weak)"><button class="orca-slot" type="button" aria-label="Add event at 09:00"><span class="orca-slot__hint">+ Add event</span></button><span class="orca-slot orca-slot--busy">Busy</span><button class="orca-slot" type="button" aria-pressed="true" aria-label="10:00, selected">10:00 selected</button></div>
```

**Classes:** `.orca-slot`, `.orca-slot__hint`, `.orca-slot--busy`

**Principles applied:** Practical UI F03: Reduce the total effort of a task; Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Time slot

---

## All-day row

`id: all-day-row` · level: component · source: ORCA

The strip above the hours of a week view holding all-day and multi-day bars.

Built from: `allday-bar`

### Why

Separating all-day items from timed ones keeps both readable (Miller's law) and shows multi-day spans across columns (Gestalt continuity).

### When to use

- Week and day views.

### How to use

- `<div class="orca-allday-row">` with `.orca-allday-row__label` ('All day') and `.orca-allday-row__lane` (`--orca-days` columns); place all-day bars with `grid-column: 2 / span 3`.

#### Example: All day

```django
<div class="orca-allday-row" style="max-width: 36rem"><span class="orca-allday-row__label">All day</span><div class="orca-allday-row__lane"><div class="orca-allday-bar" style="--orca-event: var(--orca-chart-1); grid-column: 1 / span 1">Inventory</div><div class="orca-allday-bar orca-allday-bar--continues-after" style="--orca-event: var(--orca-chart-4); grid-column: 3 / span 5">Trade fair, 4–9 November</div></div></div>
```

**Classes:** `.orca-allday-row`, `.orca-allday-row__label`, `.orca-allday-row__lane`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI L01: Group related information

**ORCA guide items covered:** All-day row

---

## Event chip

`id: event-chip` · level: component · source: ORCA

A one-line event in a month cell: colour dot, time and title.

Built from: `event-dot`, `time-label`

### Why

In a small cell the time and the start of the title identify an event (Practical UI W04); the dot keys its calendar without filling the cell with colour.

### When to use

- Month views and mini lists.

### How to use

- `<button class="orca-event-chip" type="button">` (or a link) with an event dot, `.orca-event-chip__time` and `.orca-event-chip__title`; `--cancelled` strikes it through.
- Accessible name: the full event ('Audit, 10:00 to 11:00').

#### Example: Chips

```django
<div class="orca-stack" style="max-width: 10rem; gap: 2px"><button class="orca-event-chip" type="button" aria-label="Delivery, 09:00 to 10:00"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-1)"></span><span class="orca-event-chip__time">09:00</span><span class="orca-event-chip__title">Delivery window</span></button><button class="orca-event-chip orca-event-chip--cancelled" type="button" aria-label="Training, cancelled"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-4)"></span><span class="orca-event-chip__time">14:00</span><span class="orca-event-chip__title">Training</span></button></div>
```

**Classes:** `.orca-event-chip`, `.orca-event-chip__time`, `.orca-event-chip__title`, `.orca-event-chip--cancelled`

**Principles applied:** Practical UI W04: Lead with the information people seek; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Event chip

---

## Event card

`id: event-card` · level: component · source: ORCA

An event block in a day or week view: title, time, place and its calendar colour edge.

Built from: `event-bar`, `time-label`

### Why

Blocks sized to their duration show the shape of a day at a glance (Jakob's law); a tinted fill keeps text readable (C01) and hatching marks tentative events without colour alone (C03).

### When to use

- Day and week views; event detail popovers' trigger.

### How to use

- `<button class="orca-event-card" style="--orca-event: var(--orca-chart-2)">` with `.orca-event-card__title` and `.orca-event-card__meta` (time and place); height from duration (positioned by the view).
- `--tentative` for unconfirmed events. Overlapping events share the column width.

#### Example: Cards

```django
<div class="orca-row" style="align-items: stretch; max-width: 30rem">
  <button class="orca-event-card" type="button" style="--orca-event: var(--orca-chart-1); height: 5rem; width: 12rem"><span class="orca-event-card__title">Delivery window</span><span class="orca-event-card__meta"><time datetime="09:00">09:00</time>–<time datetime="10:30">10:30</time></span><span class="orca-event-card__meta">{% icon "location" size="xs" %}Loading dock</span></button>
  <button class="orca-event-card orca-event-card--tentative" type="button" style="--orca-event: var(--orca-chart-2); height: 3.5rem; width: 12rem"><span class="orca-event-card__title">Audit (tentative)</span><span class="orca-event-card__meta">10:00–11:00</span></button>
</div>
```

**Classes:** `.orca-event-card`, `.orca-event-card__title`, `.orca-event-card__meta`, `.orca-event-card--tentative`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI C01: Check contrast for meaningful content; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Event card

---

## Agenda item

`id: agenda-item` · level: component · source: ORCA

One event in a list view: time column, colour dot, title and details.

Built from: `event-dot`, `time-label`, `date-badge`

### Why

A list is the most readable calendar view on small screens and for screen readers (Postel's law); a fixed time column makes the day scannable.

### When to use

- Agenda view, upcoming events panels, phone calendars.

### How to use

- `<ol class="orca-agenda">` of `<li class="orca-agenda-item">` with `.orca-agenda-item__when` and `.orca-agenda-item__body` (event dot, `__title`, `__meta`).
- Group by day with a date badge or a day heading; all-day items first.

#### Example: Agenda

```django
<ol class="orca-agenda" style="max-width: 32rem">
  <li class="orca-agenda-item"><span class="orca-agenda-item__when">All day</span><span class="orca-agenda-item__body"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-4)"></span><span class="orca-agenda-item__title">Trade fair</span><span class="orca-agenda-item__meta">Day 3 of 6</span></span></li>
  <li class="orca-agenda-item"><span class="orca-agenda-item__when"><time datetime="09:00">09:00</time>–<time datetime="10:30">10:30</time></span><span class="orca-agenda-item__body"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-1)"></span><span class="orca-agenda-item__title">Delivery window</span><span class="orca-agenda-item__meta">Loading dock · 3 people</span></span></li>
</ol>
```

**Classes:** `.orca-agenda`, `.orca-agenda-item`, `.orca-agenda-item__when`, `.orca-agenda-item__body`, `.orca-agenda-item__title`, `.orca-agenda-item__meta`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Agenda item

---

## Date badge

`id: date-badge` · level: component · source: ORCA

A small calendar-page box with month, day number and weekday.

Built from: `month-name`, `day-number`, `weekday-name`

### Why

The calendar-page shape is recognised instantly as a date (Jakob's law) and anchors lists of dated items.

### When to use

- Beside events in lists, upcoming deadlines, day groups of an agenda.

### How to use

- `<time class="orca-date-badge" datetime="2026-11-06">` with `.orca-date-badge__month`, `__day` and `__weekday`; add an `aria-label` with the full date.

#### Example: Badge

```django
<time class="orca-date-badge" datetime="2026-11-06" aria-label="Friday 6 November 2026"><span class="orca-date-badge__month" aria-hidden="true">Nov</span><span class="orca-date-badge__day" aria-hidden="true">6</span><span class="orca-date-badge__weekday" aria-hidden="true">Fri</span></time>
```

**Classes:** `.orca-date-badge`, `.orca-date-badge__month`, `.orca-date-badge__day`, `.orca-date-badge__weekday`

**Principles applied:** Jakob's law: work the way products people already know work

**ORCA guide items covered:** Date badge

---

## Holiday label

`id: holiday-label` · level: component · source: ORCA

The holiday's name on a purple tint with a diamond mark.

Built from: `holiday-marker`

### Why

Naming the holiday explains why a day is closed or quiet (Peak–end rule); the mark and tint make it findable without colour alone.

### When to use

- Day cells, agenda days and schedules on public holidays and closures.

### How to use

- `<span class="orca-holiday-label">Armistice Day</span>`; add '(closed)' when the site is closed.

#### Example: Holiday

```django
<span class="orca-holiday-label">Armistice Day (closed)</span>
```

**Classes:** `.orca-holiday-label`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Holiday label

---

## More-events link

`id: more-events-link` · level: component · source: ORCA

'+3 more' at the bottom of a crowded day cell, opening the full list of that day.

Built from: `link-action`

### Why

Capping a cell's events keeps the month legible (Miller's law) while the link proves nothing is hidden (Practical UI S06).

### When to use

- Month cells with more events than fit.

### How to use

- `<button class="orca-more-link" type="button" aria-label="3 more events on 6 November">+3 more</button>` opening a popover or the day view.

#### Example: Link

```django
<button class="orca-more-link" type="button" aria-label="3 more events on 6 November">+3 more</button>
```

**Classes:** `.orca-more-link`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI S06: Make essential content visible or discoverable

**ORCA guide items covered:** More-events link ("+3 more")

---

## Calendar header

`id: calendar-header` · level: component · source: ORCA

The month or period title with navigation and the view switcher.

Built from: `calendar-navigation`, `calendar-view-switcher`, `month-name`

### Why

One header that answers 'when am I looking at?' and holds every way to move keeps navigation predictable (Jakob's law, Practical UI L14).

### When to use

- Top of every calendar view.

### How to use

- `<div class="orca-cal-header">` with the calendar navigation, `<h2 class="orca-cal-header__title">November 2026</h2>` and the view switcher in `.orca-cal-header__end`.

#### Example: Header

```django
<div class="orca-cal-header"><div class="orca-cal-nav"><a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Previous month">{% icon "chevron-left" %}</a><a class="orca-button" href="#">Today</a><a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Next month">{% icon "chevron-right" %}</a></div>
  <h2 class="orca-cal-header__title">November 2026</h2>
  <nav class="orca-segmented orca-segmented--dense orca-cal-header__end" aria-label="Calendar view"><a class="orca-segmented__item" href="#">Week</a><a class="orca-segmented__item" href="#" aria-current="page">Month</a><a class="orca-segmented__item" href="#">Agenda</a></nav></div>
```

**Classes:** `.orca-cal-header`, `.orca-cal-header__title`, `.orca-cal-header__end`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI L14: Reduce travel between related actions

**ORCA guide items covered:** Calendar header (month label + navigation)

---
