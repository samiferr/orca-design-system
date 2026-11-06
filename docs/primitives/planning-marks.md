# Planning marks

Marks drawn on calendars, schedules and timelines. Each state pairs colour with a shape, a pattern or a word.

## Today marker

`id: today-marker` · level: primitive · source: ORCA

Today's day number outlined in red, bold.

### Why

People orient on 'now' first in any calendar (Von Restorff); outline plus weight works without colour (C03).

### When to use

- Today in month grids, mini calendars, date pickers.

### How to use

- `<button class="orca-day" aria-current="date">6</button>` (or `.orca-day--today`).
- Only one per view.

### Accessibility

- `aria-current="date"` announces 'current date'.

#### Example: Example

```django
<button class="orca-day" type="button" aria-current="date" aria-label="6 November, today">6</button>
```

**Classes:** `.orca-day`, `.orca-day--today`

**Tokens:** `--orca-today`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Today marker

---

## Selected-day marker

`id: selected-day-marker` · level: primitive · source: ORCA

The chosen day filled with the accent colour.

### Why

Selection uses the system's 'on' colour and a fill (shape change), consistent with ticks and radios (Practical UI F09).

### When to use

- The chosen day or the ends of a chosen range.

### How to use

- `<button class="orca-day" aria-pressed="true">` in pickers, `aria-selected="true"` in grids.

#### Example: Example

```django
<button class="orca-day" type="button" aria-pressed="true" aria-label="12 November, selected">12</button>
```

**Classes:** `.orca-day--selected`

**Tokens:** `--orca-accent`

**Principles applied:** Practical UI F09: Keep visual and functional behaviour consistent; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Selected-day marker

---

## Out-of-month day marker

`id: outside-day-marker` · level: primitive · source: ORCA

Days of the previous or next month shown muted.

### Why

Muting days outside the month keeps full weeks visible while keeping focus on the month (Practical UI L03).

### When to use

- Leading and trailing days of a month grid.

### How to use

- Add `.orca-day--outside`; they stay clickable and navigate to their month.

#### Example: Example

```django
<button class="orca-day orca-day--outside" type="button" aria-label="31 October">31</button>
```

**Classes:** `.orca-day--outside`

**Tokens:** `--orca-text-muted`

**Principles applied:** Practical UI L03: Establish an order of importance

**ORCA guide items covered:** Out-of-month day marker

---

## Weekend marker

`id: weekend-marker` · level: primitive · source: ORCA

A faint tint behind weekend days and columns.

### Why

A subtle tint separates working days without competing with events (Miller's law: chunking the week).

### When to use

- Month grids, week views, Gantt columns.

### How to use

- `.orca-day--weekend` on days; `background: var(--orca-weekend-bg)` on columns. Weekend days follow the locale.

#### Example: Example

```django
<div class="orca-row" style="gap: 0"><button class="orca-day" type="button">6</button><button class="orca-day orca-day--weekend" type="button">7</button><button class="orca-day orca-day--weekend" type="button">8</button></div>
```

**Classes:** `.orca-day--weekend`

**Tokens:** `--orca-weekend-bg`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Weekend marker

---

## Holiday marker

`id: holiday-marker` · level: primitive · source: ORCA

A purple tint and underline mark on holidays and closed days, with the holiday's name.

### Why

Closed days change plans; tint plus a mark plus the name make them noticed and understood (C03).

### When to use

- Public holidays, site closures, exceptions.

### How to use

- `.orca-day--holiday` with `title` and an `aria-label` that include the holiday name.
- List the name in the day cell or agenda (holiday label component).

#### Example: Example

```django
<button class="orca-day orca-day--holiday" type="button" title="Armistice Day" aria-label="11 November, Armistice Day, closed">11</button>
```

**Classes:** `.orca-day--holiday`

**Tokens:** `--orca-holiday-bg`, `--orca-purple`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Holiday marker

---

## Event dot

`id: event-dot` · level: primitive · source: ORCA

A small dot that says 'there are events here' or keys an event's calendar.

### Why

In small cells a dot shows presence without text (Miller's law); the count or list must be one tap away.

### When to use

- Mini calendars (day has events), agenda rows (calendar colour).

### How to use

- `<span class="orca-event-dot" style="--orca-event: var(--orca-chart-3)"></span>`; on a day: `.orca-day--has-events` and say 'has events' in its label.

#### Example: Example

```django
<div class="orca-row"><span class="orca-with-icon"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-3)"></span>Maintenance</span><button class="orca-day orca-day--has-events" type="button" aria-label="14 November, has events">14</button></div>
```

**Classes:** `.orca-event-dot`, `.orca-day--has-events`

**Tokens:** `--orca-chart-3`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Event dot

---

## Event bar

`id: event-bar` · level: primitive · source: ORCA

A timed event in a day: tinted bar with a 3px leading edge in the calendar colour.

### Why

The coloured edge keys the calendar while the light tint keeps the title readable (C01); tentative events are hatched and cancelled ones struck through, so status never relies on colour (C03).

### When to use

- Events in month cells and week/day columns.

### How to use

- `<div class="orca-event-bar" style="--orca-event: var(--orca-chart-1)"><time>08:30</time> Delivery</div>`.
- States: `--tentative` (hatched), `--cancelled` (struck through, muted). Long titles truncate; full title in `title`.

#### Example: Example

```django
<div class="orca-stack" style="max-width: 14rem; gap: 2px">
  <div class="orca-event-bar" style="--orca-event: var(--orca-chart-1)"><time class="orca-time" datetime="08:30">08:30</time> Delivery window</div>
  <div class="orca-event-bar orca-event-bar--tentative" style="--orca-event: var(--orca-chart-2)"><time class="orca-time" datetime="10:00">10:00</time> Audit (tentative)</div>
  <div class="orca-event-bar orca-event-bar--cancelled" style="--orca-event: var(--orca-chart-4)"><time class="orca-time" datetime="14:00">14:00</time> Training</div>
</div>
```

**Classes:** `.orca-event-bar`, `.orca-event-bar--tentative`, `.orca-event-bar--cancelled`

**Tokens:** `--orca-chart-1`

**Principles applied:** Practical UI C01: Check contrast for meaningful content; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Event bar

---

## All-day bar

`id: allday-bar` · level: primitive · source: ORCA

A solid bar for all-day and multi-day events, with arrow ends when it continues.

### Why

Solid fill separates all-day events from timed ones at a glance (Von Restorff); arrow ends show continuation without words (Jakob's law: familiar from calendars).

### When to use

- All-day rows of week views; multi-day events in month grids.

### How to use

- `<div class="orca-allday-bar" style="--orca-event: var(--orca-chart-1)">Trade fair</div>`; add `--continues-before` / `--continues-after` at the edges of the visible range.

#### Example: Example

```django
<div class="orca-stack" style="max-width: 18rem; gap: 2px"><div class="orca-allday-bar" style="--orca-event: var(--orca-chart-1)">Inventory day</div><div class="orca-allday-bar orca-allday-bar--continues-after" style="--orca-event: var(--orca-chart-4)">Trade fair, 6–9 November</div></div>
```

**Classes:** `.orca-allday-bar`, `.orca-allday-bar--continues-before`, `.orca-allday-bar--continues-after`

**Tokens:** `--orca-chart-1`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Jakob's law: work the way products people already know work

**ORCA guide items covered:** All-day bar

---

## Hour gridline

`id: hour-gridline` · level: primitive · source: ORCA

Hour and half-hour lines with the hour label in the gutter.

### Why

Faint gridlines give scale to a day without competing with events (Practical UI S02).

### When to use

- Day and week views, resource schedulers.

### How to use

- `<div class="orca-hour-line"><span class="orca-hour-line__label">09:00</span></div>` every hour; `--half` (dashed) for half hours.

#### Example: Example

```django
<div style="position: relative; max-width: 18rem; padding-top: 0.75rem"><div class="orca-hour-line"><span class="orca-hour-line__label">09:00</span></div><div style="height: 1.5rem"></div><div class="orca-hour-line orca-hour-line--half"></div><div style="height: 1.5rem"></div><div class="orca-hour-line"><span class="orca-hour-line__label">10:00</span></div></div>
```

**Classes:** `.orca-hour-line`, `.orca-hour-line--half`, `.orca-hour-line__label`

**Tokens:** `--orca-gridline`

**Principles applied:** Practical UI S02: Remove styles that compete without communicating

**ORCA guide items covered:** Hour gridline

---

## Now indicator

`id: now-indicator` · level: primitive · source: ORCA

A red line with a dot at the current time across day and week views.

### Why

The present moment is the anchor of any schedule (Von Restorff); the line plus dot shape reads without colour.

### When to use

- Day and week views, timelines, Gantt charts (vertical).

### How to use

- `<div class="orca-now-line" style="top: …" aria-hidden="true"></div>` positioned by script; update every minute.

#### Example: Example

```django
<div style="padding: var(--orca-space-8) var(--orca-space-16); max-width: 18rem"><div class="orca-now-line" aria-hidden="true"></div></div>
```

**Classes:** `.orca-now-line`

**Tokens:** `--orca-today`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Now indicator

---

## Availability colour (free, busy, tentative)

`id: availability-color` · level: primitive · source: ORCA

Free, busy, tentative and off states as filled, solid, hatched and dashed marks.

### Why

Availability is compared across many slots; four distinct patterns (not just four colours) keep it readable for everyone (C03, Miller's law).

### When to use

- Availability legends, booking slots, resource schedulers, people pickers.

### How to use

- Legend item: `<span class="orca-avail orca-avail--free">Free</span>`; `--busy`, `--tentative`, `--off`.
- Fill a slot: `.orca-avail-fill--free`, `--busy`, `--tentative` on the slot element, with the state in its label.

#### Example: Example

```django
<div class="orca-row orca-row--16"><span class="orca-avail orca-avail--free">Free</span><span class="orca-avail orca-avail--busy">Busy</span><span class="orca-avail orca-avail--tentative">Tentative</span><span class="orca-avail orca-avail--off">Not working</span></div>
```

**Classes:** `.orca-avail`, `.orca-avail--free`, `.orca-avail--busy`, `.orca-avail--tentative`, `.orca-avail-fill--free`

**Tokens:** `--orca-positive`, `--orca-neutral-fill`, `--orca-caution`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Availability colour (free, busy, tentative)

---

## Priority marker

`id: priority-marker` · level: primitive · source: ORCA

Signal bars plus a word: low, medium, high, urgent.

### Why

Bars rise with priority so the order is visible in greyscale (C03); the word removes doubt.

### When to use

- Tasks, tickets, alerts in lists and boards.

### How to use

- `<span class="orca-priority orca-priority--high"><span class="orca-priority__bars" aria-hidden="true"><i></i><i></i><i></i></span>High</span>`.

#### Example: Example

```django
<div class="orca-row orca-row--16">
  <span class="orca-priority orca-priority--low"><span class="orca-priority__bars" aria-hidden="true"><i></i><i></i><i></i></span>Low</span>
  <span class="orca-priority orca-priority--medium"><span class="orca-priority__bars" aria-hidden="true"><i></i><i></i><i></i></span>Medium</span>
  <span class="orca-priority orca-priority--high"><span class="orca-priority__bars" aria-hidden="true"><i></i><i></i><i></i></span>High</span>
  <span class="orca-priority orca-priority--urgent"><span class="orca-priority__bars" aria-hidden="true"><i></i><i></i><i></i></span>Urgent</span>
</div>
```

**Classes:** `.orca-priority`, `.orca-priority--low`, `.orca-priority--medium`, `.orca-priority--high`, `.orca-priority--urgent`

**Tokens:** `--orca-caution`, `--orca-negative`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Priority marker

---

## Deadline marker

`id: deadline-marker` · level: primitive · source: ORCA

A flag icon with the due date; a caution flag when it is close.

### Why

A due date with a flag is found by scanning (Von Restorff); turning the icon amber when close prevents a negative peak (Peak–end rule).

### When to use

- Tasks, plans, Gantt bars (`.orca-deadline-line` as a vertical rule).

### How to use

- `<span class="orca-deadline">{% icon "flag" %}<span>Due <time datetime=…>Fri 13 Nov</time></span></span>`; add `--soon` within 2 days.

#### Example: Example

```django
<div class="orca-row orca-row--16"><span class="orca-deadline">{% icon "flag" %}<span>Due <time datetime="2026-11-20">Fri 20 Nov</time></span></span><span class="orca-deadline orca-deadline--soon">{% icon "flag" %}<span>Due tomorrow</span></span></div>
```

**Classes:** `.orca-deadline`, `.orca-deadline--soon`, `.orca-deadline-line`

**Tokens:** `--orca-caution`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Deadline marker

---

## Overdue marker

`id: overdue-marker` · level: primitive · source: ORCA

Bold red text with the error glyph and how late it is.

### Why

Overdue items need action now; red, bold, a glyph and the word 'Overdue' together are unmistakable (C03, C04).

### When to use

- Tasks and deadlines past due.

### How to use

- `<span class="orca-overdue">{% icon "error" %}Overdue by 2 days</span>`.
- Say by how much; never only 'Late'.

#### Example: Example

```django
<span class="orca-overdue">{% icon "error" %}Overdue by 2 days</span>
```

**Classes:** `.orca-overdue`

**Tokens:** `--orca-negative`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI C04: Reserve status colours for their meanings

**ORCA guide items covered:** Overdue marker

---

## Milestone marker

`id: milestone-marker` · level: primitive · source: ORCA

A diamond: filled (reached), outlined (upcoming), red outline (missed), green (done).

### Why

The diamond is the convention for milestones in plans and Gantt charts (Jakob's law); fill versus outline shows state without colour.

### When to use

- Roadmaps, Gantt charts, milestone timelines.

### How to use

- `<span class="orca-milestone orca-milestone--upcoming" aria-hidden="true"></span>` before the milestone name; states `--done`, `--missed`, `--upcoming`, default (reached).
- Write the state in text too.

#### Example: Example

```django
<div class="orca-stack"><span class="orca-with-icon"><span class="orca-milestone orca-milestone--done" aria-hidden="true"></span>Pilot live · done</span><span class="orca-with-icon"><span class="orca-milestone orca-milestone--upcoming" aria-hidden="true"></span>All sites live · 1 Dec</span><span class="orca-with-icon"><span class="orca-milestone orca-milestone--missed" aria-hidden="true"></span>Training complete · missed</span></div>
```

**Classes:** `.orca-milestone`, `.orca-milestone--done`, `.orca-milestone--missed`, `.orca-milestone--upcoming`

**Tokens:** `--orca-positive`, `--orca-negative`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Milestone marker

---

## Drag handle

`id: drag-handle` · level: primitive · source: ORCA

A grip button for moving an item, usable by keyboard too.

### Why

A visible grip tells people the item can be moved (affordance, Jakob's law); a keyboard alternative keeps it usable for everyone (Postel's law).

### When to use

- Reorderable rows, schedule rows, board cards, events in a week view.

### How to use

- `<button class="orca-drag-handle" type="button" aria-label="Move Entrance A" aria-describedby="drag-help">{% icon "drag" %}</button>`.
- Keyboard: Space picks up (`aria-pressed="true"`), arrows move, Space drops, Escape cancels; announce moves in a live region.
- While dragging add `.orca-is-dragging` to the item (lifted shadow).

### Accessibility

- Always provide a non-drag way (move up/down buttons or the keyboard flow).

#### Example: Example

```django
<div class="orca-row" style="max-width: 20rem; padding: var(--orca-space-4); border: var(--orca-border-width) solid var(--orca-border)"><button class="orca-drag-handle" type="button" aria-label="Move Entrance A">{% icon "drag" %}</button>Entrance A</div>
```

**Classes:** `.orca-drag-handle`, `.orca-is-dragging`

**Tokens:** `--orca-text-muted`, `--orca-shadow-dragged`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Drag handle

---

## Resize handle

`id: resize-handle` · level: primitive · source: ORCA

A grip on the edge of an event or panel that changes its length.

### Why

A visible grip on the edge shows the item can be stretched (affordance); a precise field elsewhere remains the accessible way (Postel's law).

### When to use

- Bottom edge of events in day/week views; edges of Gantt bars (`--x`).

### How to use

- `<button class="orca-resize-handle" type="button" aria-label="Change end time of Delivery">` at the bottom edge; `.orca-resize-handle--x` for horizontal.
- Snap to 15 minutes; show the new time while resizing.

#### Example: Example

```django
<div style="max-width: 12rem"><div class="orca-event-bar" style="--orca-event: var(--orca-chart-1); min-height: 3rem; align-items: flex-start; padding-top: var(--orca-space-4)">Delivery</div><button class="orca-resize-handle" type="button" aria-label="Change end time of Delivery"></button></div>
```

**Classes:** `.orca-resize-handle`, `.orca-resize-handle--x`

**Tokens:** `--orca-text-muted`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Resize handle

---
