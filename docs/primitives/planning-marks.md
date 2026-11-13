# Planning marks

Marks for calendars, schedules and timelines. Each state pairs colour with a shape, pattern or word.

## Today marker

`id: today-marker` · level: primitive · source: ORCA

Today's day number outlined in red, bold.

### General description

A visual mark that highlights the current day in a calendar so people can find 'now' quickly.

#### Use cases

- Highlighting today in a month grid.
- Marking today in mini calendars and date pickers.
- Orienting people in a schedule.

#### When not to use it

- Marking a chosen day: use a selected-day marker.
- Marking events: use an event dot or bar.

#### Best practices

- Mark only one day per view.
- Use shape or weight as well as colour.
- Tell screen readers it is the current date.
- Keep it different from the selected-day style.

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

### General description

A visual mark showing which calendar day or range the user has chosen.

#### Use cases

- Showing the chosen date in a date picker.
- Marking the start and end of a date range.
- Showing the active day in a calendar view.

#### When not to use it

- Marking today: use a today marker.
- Showing days with events: use event dots.

#### Best practices

- Use a strong fill that stands out from other days.
- Do not rely on colour alone.
- Tell screen readers which day is selected.
- Make today and selected states look different.

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

### General description

A style for days that belong to the previous or next month but appear in a month grid to complete full weeks.

#### Use cases

- Filling the first and last weeks of a month grid.
- Letting people jump to a neighbouring month.
- Keeping calendar rows a regular length.

#### When not to use it

- Days that are unavailable: use a disabled style.
- Days with no real meaning: leave the cells empty.

#### Best practices

- Mute them so the current month stands out.
- Keep them readable and keep enough contrast.
- Let them open their own month when clicked.
- Label them clearly for screen readers.

### When to use

- Leading and trailing days of a month grid.

### How to use

- Add `.orca-day--outside`. They stay clickable and open their month.

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

### General description

A light tint or style that sets weekend days apart from weekdays in calendars and schedules.

#### Use cases

- Month grids and week views.
- Gantt charts and resource schedulers.
- Date pickers where weekends matter.

#### When not to use it

- Days that are closed or unavailable: use a holiday or off marker.
- Locales with different weekends: do not hard-code Saturday and Sunday.

#### Best practices

- Keep the tint subtle so events stay clear.
- Follow the user's local weekend days.
- Do not use colour as the only cue where it matters.
- Keep contrast for text on the tint.

### When to use

- Month grids, week views, Gantt columns.

### How to use

- `.orca-day--weekend` on days; `background: var(--orca-weekend-bg)` on columns. Weekend days follow the locale.

#### Example: Example

```django
<div class="orca-row" style="gap: 0">
  <button class="orca-day" type="button">6</button>
  <button class="orca-day orca-day--weekend" type="button">7</button>
  <button class="orca-day orca-day--weekend" type="button">8</button>
</div>
```

**Classes:** `.orca-day--weekend`

**Tokens:** `--orca-weekend-bg`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Weekend marker

---

## Holiday marker

`id: holiday-marker` · level: primitive · source: ORCA

A purple tint and underline on holidays and closed days, plus the holiday's name.

### General description

A mark on calendar days that are public holidays or closure days, often with the holiday name.

#### Use cases

- Showing public holidays in a calendar.
- Marking days a business is closed.
- Warning that a date may be unavailable.

#### When not to use it

- Ordinary weekends: use a weekend marker.
- Events: use event markers.

#### Best practices

- Show the holiday name, not just a colour.
- Combine tint with a shape or underline.
- Say the holiday in labels for screen readers.
- Let users hide holidays they do not need.

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

A small dot showing a day has events, or marking an event's calendar.

### General description

A small dot in a calendar cell that shows a day has events, or colour-codes an event's calendar.

#### Use cases

- Showing which days have events in a mini calendar.
- Colour-coding calendars in an agenda.
- Saving space where full event titles do not fit.

#### When not to use it

- Showing event details: use an event bar or a list.
- Many events per day: show a count instead.

#### Best practices

- Make the day's events one tap away.
- Say 'has events' in the day's label.
- Do not use colour as the only key.
- Keep dots few and spaced clearly.

### When to use

- Mini calendars (day has events), agenda rows (calendar colour).

### How to use

- `<span class="orca-event-dot" style="--orca-event: var(--orca-chart-3)"></span>`; on a day: `.orca-day--has-events` and say 'has events' in its label.

#### Example: Example

```django
<div class="orca-row">
  <span class="orca-with-icon"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-3)"></span>Maintenance</span>
  <button class="orca-day orca-day--has-events" type="button" aria-label="14 November, has events">14</button>
</div>
```

**Classes:** `.orca-event-dot`, `.orca-day--has-events`

**Tokens:** `--orca-chart-3`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Event dot

---

## Event bar

`id: event-bar` · level: primitive · source: ORCA

A timed event: a tinted bar with a 3px leading edge in the calendar colour.

### General description

A horizontal block in a calendar that shows one timed event with its title and time.

#### Use cases

- Showing events in month, week and day views.
- Showing meetings and appointments.
- Showing bookings in a resource schedule.

#### When not to use it

- Events that last all day or several days: use an all-day bar.
- A quick sign that a day has events: use a dot.

#### Best practices

- Show the time and title.
- Truncate long titles and give the full title on hover.
- Mark tentative or cancelled events with more than colour.
- Keep text readable on the tint.

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

### General description

A bar that spans the width of a day or several days to show an event with no set time.

#### Use cases

- Showing all-day events in a week view.
- Showing events that span several days.
- Showing trade fairs, holidays or trips.

#### When not to use it

- Events with a start and end time: use an event bar.
- Single marks on a day: use a dot.

#### Best practices

- Use a solid fill so it stands apart from timed events.
- Show arrow ends when it continues past the view.
- Keep the title readable.
- Group all-day bars in their own row.

### When to use

- All-day rows of week views; multi-day events in month grids.

### How to use

- `<div class="orca-allday-bar" style="--orca-event: var(--orca-chart-1)">Trade fair</div>`; add `--continues-before` / `--continues-after` at the edges of the visible range.

#### Example: Example

```django
<div class="orca-stack" style="max-width: 18rem; gap: 2px">
  <div class="orca-allday-bar" style="--orca-event: var(--orca-chart-1)">Inventory day</div>
  <div class="orca-allday-bar orca-allday-bar--continues-after" style="--orca-event: var(--orca-chart-4)">Trade fair, 6–9 November</div>
</div>
```

**Classes:** `.orca-allday-bar`, `.orca-allday-bar--continues-before`, `.orca-allday-bar--continues-after`

**Tokens:** `--orca-chart-1`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Jakob's law: work the way products people already know work

**ORCA guide items covered:** All-day bar

---

## Hour gridline

`id: hour-gridline` · level: primitive · source: ORCA

Hour and half-hour lines with the hour label in the gutter.

### General description

A faint horizontal line across a day or week view that marks each hour, with a time label.

#### Use cases

- Giving scale to day and week views.
- Resource and room schedulers.
- Helping people place events at the right time.

#### When not to use it

- Views that are not time-based: do not add lines.
- Very dense schedules: avoid heavy lines.

#### Best practices

- Keep lines light so events stand out.
- Label each hour in the side margin.
- Use a dashed or lighter line for half hours.
- Keep spacing consistent.

### When to use

- Day and week views, resource schedulers.

### How to use

- `<div class="orca-hour-line"><span class="orca-hour-line__label">09:00</span></div>` every hour; `--half` (dashed) for half hours.

#### Example: Example

```django
<div style="position: relative; max-width: 18rem; padding-top: 0.75rem">
  <div class="orca-hour-line">
    <span class="orca-hour-line__label">09:00</span>
  </div>
  <div style="height: 1.5rem"></div>
  <div class="orca-hour-line orca-hour-line--half"></div>
  <div style="height: 1.5rem"></div>
  <div class="orca-hour-line">
    <span class="orca-hour-line__label">10:00</span>
  </div>
</div>
```

**Classes:** `.orca-hour-line`, `.orca-hour-line--half`, `.orca-hour-line__label`

**Tokens:** `--orca-gridline`

**Principles applied:** Practical UI S02: Remove styles that compete without communicating

**ORCA guide items covered:** Hour gridline

---

## Now indicator

`id: now-indicator` · level: primitive · source: ORCA

A red line with a dot at the current time across day and week views.

### General description

A line across a day or week view that shows the current time and moves as time passes.

#### Use cases

- Showing the present in a day or week view.
- Showing progress along a timeline.
- Helping people find what is happening now.

#### When not to use it

- Views that show only past or future dates: do not show it.
- Showing a deadline: use a deadline marker.

#### Best practices

- Make it clearly different from events and gridlines.
- Use shape as well as colour, such as a line with a dot.
- Update it every minute.
- Scroll to it when the view opens.

### When to use

- Day and week views, timelines, Gantt charts (vertical).

### How to use

- `<div class="orca-now-line" style="top: …" aria-hidden="true"></div>` positioned by script; update every minute.

#### Example: Example

```django
<div style="padding: var(--orca-space-8) var(--orca-space-16); max-width: 18rem">
  <div class="orca-now-line" aria-hidden="true"></div>
</div>
```

**Classes:** `.orca-now-line`

**Tokens:** `--orca-today`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Now indicator

---

## Availability colour (free, busy, tentative)

`id: availability-color` · level: primitive · source: ORCA

Free, busy, tentative and off states as filled, solid, hatched and dashed marks.

### General description

A set of marks that show whether time slots or people are free, busy, tentative or away.

#### Use cases

- Showing when people or rooms are available.
- Offering free slots for booking.
- Comparing availability across many people.

#### When not to use it

- Showing events themselves: use event bars.
- Only free versus busy: fewer states may be clearer.

#### Best practices

- Use patterns or labels as well as colour.
- Provide a legend that explains each state.
- Name the state in each slot's label.
- Keep the number of states small.

### When to use

- Availability legends, booking slots, resource schedulers, people pickers.

### How to use

- Legend item: `<span class="orca-avail orca-avail--free">Free</span>`; `--busy`, `--tentative`, `--off`.
- Fill a slot: `.orca-avail-fill--free`, `--busy`, `--tentative` on the slot element, with the state in its label.

#### Example: Example

```django
<div class="orca-row orca-row--16">
  <span class="orca-avail orca-avail--free">Free</span>
  <span class="orca-avail orca-avail--busy">Busy</span>
  <span class="orca-avail orca-avail--tentative">Tentative</span>
  <span class="orca-avail orca-avail--off">Not working</span>
</div>
```

**Classes:** `.orca-avail`, `.orca-avail--free`, `.orca-avail--busy`, `.orca-avail--tentative`, `.orca-avail-fill--free`

**Tokens:** `--orca-positive`, `--orca-neutral-fill`, `--orca-caution`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Availability colour (free, busy, tentative)

---

## Priority marker

`id: priority-marker` · level: primitive · source: ORCA

Signal bars plus a word: low, medium, high, urgent.

### General description

A small mark that shows how important a task, ticket or alert is, such as low, medium, high or urgent.

#### Use cases

- Ranking tasks in lists and boards.
- Showing urgency on support tickets.
- Sorting alerts by importance.

#### When not to use it

- Showing progress or status: use a status badge.
- Items that are all the same importance: do not mark them.

#### Best practices

- Use a word as well as an icon or colour.
- Make levels clearly different in shape or size.
- Keep the scale short, with four levels at most.
- Use the same scale everywhere.

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

### General description

A mark that shows when something is due, usually a flag icon with the date.

#### Use cases

- Showing due dates on tasks.
- Marking deadlines on plans and timelines.
- Warning that a due date is close.

#### When not to use it

- Showing something already late: use an overdue marker.
- Showing a completed date: use a plain date label.

#### Best practices

- Show the date next to the flag.
- Change the look when the deadline is close.
- Use words like 'Due tomorrow' for close dates.
- Do not rely on colour alone.

### When to use

- Tasks, plans, Gantt bars (`.orca-deadline-line` as a vertical rule).

### How to use

- `<span class="orca-deadline">{% icon "flag" %}<span>Due <time datetime=…>Fri 13 Nov</time></span></span>`; add `--soon` within 2 days.

#### Example: Example

```django
<div class="orca-row orca-row--16">
  <span class="orca-deadline">
    {% icon "flag" %}
    <span>Due <time datetime="2026-11-20">Fri 20 Nov</time></span>
  </span>
  <span class="orca-deadline orca-deadline--soon">
    {% icon "flag" %}
    <span>Due tomorrow</span>
  </span>
</div>
```

**Classes:** `.orca-deadline`, `.orca-deadline--soon`, `.orca-deadline-line`

**Tokens:** `--orca-caution`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Deadline marker

---

## Overdue marker

`id: overdue-marker` · level: primitive · source: ORCA

Bold red text with the error glyph and how late it is.

### General description

A strong mark that shows something has passed its due date, ideally saying how late it is.

#### Use cases

- Marking late tasks and invoices.
- Highlighting missed deadlines in a list.
- Prompting people to act on late work.

#### When not to use it

- Items not yet due: use a deadline marker.
- Items that are finished: show them as done.

#### Best practices

- Say how late it is, such as 'Overdue by 2 days'.
- Combine colour with an icon and words.
- Keep it distinct but not alarming for minor delays.
- Remove it once the item is done.

### When to use

- Tasks and deadlines past due.

### How to use

- `<span class="orca-overdue">{% icon "error" %}Overdue by 2 days</span>`.
- Say by how much; never only 'Late'.

#### Example: Example

```django
<span class="orca-overdue">
  {% icon "error" %}
  Overdue by 2 days
</span>
```

**Classes:** `.orca-overdue`

**Tokens:** `--orca-negative`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI C04: Reserve status colours for their meanings

**ORCA guide items covered:** Overdue marker

---

## Milestone marker

`id: milestone-marker` · level: primitive · source: ORCA

A diamond: filled (reached), outlined (upcoming), red outline (missed), green (done).

### General description

A diamond-shaped mark on a plan or timeline that shows a key point or achievement.

#### Use cases

- Marking key dates on roadmaps.
- Showing phases on Gantt charts.
- Tracking project stages.

#### When not to use it

- Regular tasks with a length: use a bar.
- Single deadlines on a task: use a deadline marker.

#### Best practices

- Show state with fill or outline, not colour alone.
- Name each milestone in text.
- State whether it is done, upcoming or missed.
- Use the diamond shape consistently.

### When to use

- Roadmaps, Gantt charts, milestone timelines.

### How to use

- `<span class="orca-milestone orca-milestone--upcoming" aria-hidden="true"></span>` before the milestone name; states `--done`, `--missed`, `--upcoming`, default (reached).
- Write the state in text too.

#### Example: Example

```django
<div class="orca-stack">
  <span class="orca-with-icon"><span class="orca-milestone orca-milestone--done" aria-hidden="true"></span>Pilot live · done</span>
  <span class="orca-with-icon"><span class="orca-milestone orca-milestone--upcoming" aria-hidden="true"></span>All sites live · 1 Dec</span>
  <span class="orca-with-icon"><span class="orca-milestone orca-milestone--missed" aria-hidden="true"></span>Training complete · missed</span>
</div>
```

**Classes:** `.orca-milestone`, `.orca-milestone--done`, `.orca-milestone--missed`, `.orca-milestone--upcoming`

**Tokens:** `--orca-positive`, `--orca-negative`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Milestone marker

---

## Drag handle

`id: drag-handle` · level: primitive · source: ORCA

A grip button for moving an item, usable by keyboard too.

### General description

A small grip control that lets people pick up an item and move it, often to reorder a list.

#### Use cases

- Reordering list rows or cards.
- Moving events in a schedule.
- Moving cards between board columns.

#### When not to use it

- Items that never move: do not add a handle.
- As the only way to reorder: also offer buttons or keys.

#### Best practices

- Offer a keyboard or button alternative to dragging.
- Make the handle large enough to grab.
- Show that the item is lifted while dragging.
- Announce moves to screen readers.

### When to use

- Reorderable rows, schedule rows, board cards, events in a week view.

### How to use

- `<button class="orca-drag-handle" type="button" aria-label="Move Entrance A" aria-describedby="drag-help">{% icon "drag" %}</button>`.
- Keyboard: Space picks up (`aria-pressed="true"`), arrows move, Space drops, Escape cancels; announce moves in a live region.
- While dragging add `.orca-is-dragging` to the item (lifted shadow).

### Accessibility

- Always offer a way to move without dragging (up/down buttons or the keyboard flow).

#### Example: Example

```django
<div class="orca-row" style="max-width: 20rem; padding: var(--orca-space-4); border: var(--orca-border-width) solid var(--orca-border)">
  <button class="orca-drag-handle" type="button" aria-label="Move Entrance A">
    {% icon "drag" %}
  </button>
  Entrance A
</div>
```

**Classes:** `.orca-drag-handle`, `.orca-is-dragging`

**Tokens:** `--orca-text-muted`, `--orca-shadow-dragged`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Drag handle

---

## Resize handle

`id: resize-handle` · level: primitive · source: ORCA

A grip on the edge of an event or panel that changes its length.

### General description

A grip on the edge of an item or panel that lets people drag to change its size or length.

#### Use cases

- Changing the length of an event in a calendar.
- Resizing side panels or columns.
- Adjusting the length of bars in a Gantt chart.

#### When not to use it

- Precise values: offer a field to type them.
- Items with a fixed size: do not add a handle.

#### Best practices

- Show the new value while resizing.
- Snap to sensible steps, such as 15 minutes.
- Offer a keyboard or form alternative.
- Make the grip big enough to reach easily.

### When to use

- Bottom edge of events in day/week views; edges of Gantt bars (`--x`).

### How to use

- `<button class="orca-resize-handle" type="button" aria-label="Change end time of Delivery">` at the bottom edge; `.orca-resize-handle--x` for horizontal.
- Snap to 15 minutes; show the new time while resizing.

#### Example: Example

```django
<div style="max-width: 12rem">
  <div class="orca-event-bar" style="--orca-event: var(--orca-chart-1); min-height: 3rem; align-items: flex-start; padding-top: var(--orca-space-4)">Delivery</div>
  <button class="orca-resize-handle" type="button" aria-label="Change end time of Delivery"></button>
</div>
```

**Classes:** `.orca-resize-handle`, `.orca-resize-handle--x`

**Tokens:** `--orca-text-muted`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Resize handle

---
