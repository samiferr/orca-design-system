# Calendar parts

The building blocks of month, week, day and agenda views. Each gives screen readers the date in words.

## Day cell

`id: day-cell` · level: component · source: ORCA

One day of a month view: day number, up to three events and a '+N more' link.

Built from: `day-number`, `today-marker`, `event-chip`, `more-events-link`, `holiday-label`

### General description

One day in a month calendar. It shows the date number and a few events for that day.

#### Use cases

- Showing a month of days in a grid.
- Marking today, weekends and holidays.
- Giving a quick view of what is on each day.

#### When not to use it

- Detailed schedules with times: use a week or day view.
- Long lists of events: use an agenda list.

#### Best practices

- Mark today clearly and not by colour alone.
- Limit visible events and link to the rest.
- Make the day number a link to the day view.
- Keep cell heights equal so weeks line up.

### When to use

- Month views.

### How to use

- `<td class="orca-cal-cell">` with `.orca-cal-cell__inner`: the day number as a link to the day view (`.orca-cal-cell__day`, `aria-label` with the full date), event chips, holiday label, more-events link.
- States: `--today` (filled red day number + `aria-current="date"`), `--outside`, `--weekend`, `--holiday`, `--selected`, `--closed` (hatched).
- On phones cells shrink and chips hide; the day's dot and count stay.

#### Example: Cells

```django
<table class="orca-cal-month" style="max-width: 36rem">
  <tbody>
    <tr>
      <td class="orca-cal-cell">
        <div class="orca-cal-cell__inner">
          <a class="orca-cal-cell__day" href="#" aria-label="Thursday 5 November">5</a>
          <button class="orca-event-chip" type="button">
            <span class="orca-event-dot" style="--orca-event: var(--orca-chart-1)"></span>
            <span class="orca-event-chip__time">09:00</span>
            <span class="orca-event-chip__title">Delivery</span>
          </button>
        </div>
      </td>
      <td class="orca-cal-cell orca-cal-cell--today">
        <div class="orca-cal-cell__inner">
          <a class="orca-cal-cell__day" href="#" aria-current="date" aria-label="Friday 6 November, today">6</a>
          <button class="orca-event-chip" type="button">
            <span class="orca-event-dot" style="--orca-event: var(--orca-chart-2)"></span>
            <span class="orca-event-chip__time">10:00</span>
            <span class="orca-event-chip__title">Audit</span>
          </button>
          <button class="orca-event-chip" type="button">
            <span class="orca-event-dot" style="--orca-event: var(--orca-chart-1)"></span>
            <span class="orca-event-chip__time">14:00</span>
            <span class="orca-event-chip__title">Training</span>
          </button>
          <button class="orca-more-link" type="button" aria-label="3 more events on 6 November">+3 more</button>
        </div>
      </td>
      <td class="orca-cal-cell orca-cal-cell--weekend orca-cal-cell--holiday">
        <div class="orca-cal-cell__inner">
          <a class="orca-cal-cell__day" href="#" aria-label="Saturday 7 November, Founders day">7</a>
          <span class="orca-holiday-label">Founders day</span>
        </div>
      </td>
    </tr>
  </tbody>
</table>
```

**Classes:** `.orca-cal-cell`, `.orca-cal-cell__inner`, `.orca-cal-cell__day`, `.orca-cal-cell--today`, `.orca-cal-cell--outside`, `.orca-cal-cell--weekend`, `.orca-cal-cell--holiday`, `.orca-cal-cell--selected`, `.orca-cal-cell--closed`

**Principles applied:** Jakob's law: work the way products people already know work; Miller's law: chunk information so working memory is not overloaded; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Day cell

---

## Week header

`id: week-header` · level: component · source: ORCA

The week number and its date range, heading a week view.

Built from: `week-number`, `date-label`

### General description

A heading for a week view that shows the week number and the dates it covers.

#### Use cases

- Titling a week view or weekly planner.
- Roster and sprint pages that plan by week.
- Showing which dates a week covers.

#### When not to use it

- Month views: use a month heading.
- Single-day views: show the full date instead.

#### Best practices

- Show both the week number and the date range.
- Include the year when the range crosses a year end.
- Use the local way of numbering weeks.
- Mark dates with a proper date format for assistive tools.

### When to use

- Week views, sprint and roster pages.

### How to use

- `<div class="orca-week-header">` with a week number and `.orca-week-header__range` dates ('2–8 November 2026').

#### Example: Week 45

```django
<div class="orca-week-header">
  <span class="orca-week-number" title="Week 45">W45</span>
  <span class="orca-week-header__range"><time datetime="2026-11-02">2</time>–<time datetime="2026-11-08">8 November 2026</time></span>
</div>
```

**Classes:** `.orca-week-header`, `.orca-week-header__range`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Week header

---

## Weekday header

`id: weekday-header` · level: component · source: ORCA

The row of weekday names above a month or week grid.

Built from: `weekday-name`

### General description

The row of day names, such as Mon to Sun, above the columns of a calendar grid.

#### Use cases

- Labelling columns in a month or week calendar.
- Showing which days are weekends.
- Date pickers and booking grids.

#### When not to use it

- Views where each row is a day: label the rows with full dates.

#### Best practices

- Start the week on the day people in that region expect.
- Use short names, with the full name available to screen readers.
- Set the weekend apart without relying on colour alone.
- Mark them as column headers for assistive tools.

### When to use

- Top of month and week grids.

### How to use

- `<thead class="orca-cal-weekdays"><tr>` of `<th scope="col"><abbr title="Monday">Mon</abbr></th>`; weekend columns get `.is-weekend`.
- Start on the locale's first weekday.

#### Example: Header

```django
<table class="orca-cal-month">
  <thead class="orca-cal-weekdays">
    <tr>
      <th scope="col">
        <abbr title="Monday">Mon</abbr>
      </th>
      <th scope="col">
        <abbr title="Tuesday">Tue</abbr>
      </th>
      <th scope="col">
        <abbr title="Wednesday">Wed</abbr>
      </th>
      <th scope="col">
        <abbr title="Thursday">Thu</abbr>
      </th>
      <th scope="col">
        <abbr title="Friday">Fri</abbr>
      </th>
      <th scope="col" class="is-weekend">
        <abbr title="Saturday">Sat</abbr>
      </th>
      <th scope="col" class="is-weekend">
        <abbr title="Sunday">Sun</abbr>
      </th>
    </tr>
  </thead>
</table>
```

**Classes:** `.orca-cal-weekdays`

**Principles applied:** Practical UI W07: Reserve uppercase for short labels; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Weekday header

---

## Week row

`id: week-row` · level: component · source: ORCA

One row of a month grid: the week number and seven day cells.

Built from: `day-cell`, `week-number`

### General description

One row of a month calendar covering seven days, often with its week number at the start.

#### Use cases

- Building a month grid from week by week.
- Showing week numbers beside each row.
- Grouping days so the month is easier to scan.

#### When not to use it

- Week views with hours: use hour rows and day columns.

#### Best practices

- Always show exactly seven days per row.
- Show week numbers only if people plan by week.
- Mark the row's week number as a row header.
- Keep rows equal in height.

### When to use

- Month views.

### How to use

- `<tr class="orca-cal-week">` with an optional `<th scope="row">45</th>` then seven `td.orca-cal-cell`.

#### Example: Row

```django
<table class="orca-cal-month">
  <tbody>
    <tr class="orca-cal-week">
      <th scope="row">
        <abbr title="Week 45">45</abbr>
      </th>
      {% for d in "2345678" %}
        <td class="orca-cal-cell{% if forloop.counter > 5 %} orca-cal-cell--weekend{% endif %}" style="height: 3rem">
          <div class="orca-cal-cell__inner">
            <a class="orca-cal-cell__day" href="#">{{ d }}</a>
          </div>
        </td>
      {% endfor %}
    </tr>
  </tbody>
</table>
```

**Classes:** `.orca-cal-week`, `.orca-cal-month`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Week row

---

## Hour row

`id: hour-row` · level: component · source: ORCA

One hour of a day or week view: the hour label and two half-hour slots.

Built from: `hour-gridline`, `time-slot`, `time-label`

### General description

One hour of a day or week schedule, with a time label and space for events.

#### Use cases

- Day and week views with a time scale.
- Resource and room schedulers.
- Booking tools that show free and busy times.

#### When not to use it

- Month views, where days are too small for hours.
- Short lists of events: use an agenda list.

#### Best practices

- Show working hours first and scroll to the current time.
- Keep the lines faint so events stand out.
- Use the same hour height across the whole view.
- Use a 12 or 24 hour clock that matches local habits.

### When to use

- Day and week views, resource schedulers.

### How to use

- `<div class="orca-hour-row">` with `.orca-hour-row__label` (`<time>`) and `.orca-hour-row__slots` holding two time slots.
- Show working hours by default and scroll to 'now' on load.

#### Example: Two hours

```django
<div style="max-width: 24rem; padding-top: var(--orca-space-8)">
  <div class="orca-hour-row">
    <time class="orca-hour-row__label" datetime="09:00">09:00</time>
    <div class="orca-hour-row__slots">
      <button class="orca-slot" type="button" aria-label="Add event at 09:00">
        <span class="orca-slot__hint">+ Add</span>
      </button>
      <button class="orca-slot" type="button" aria-label="Add event at 09:30">
        <span class="orca-slot__hint">+ Add</span>
      </button>
    </div>
  </div>
  <div class="orca-hour-row">
    <time class="orca-hour-row__label" datetime="10:00">10:00</time>
    <div class="orca-hour-row__slots">
      <span class="orca-slot orca-slot--busy">Busy</span>
      <button class="orca-slot" type="button" aria-label="Add event at 10:30">
        <span class="orca-slot__hint">+ Add</span>
      </button>
    </div>
  </div>
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

### General description

A block of time, often half an hour, in a schedule. People pick it to book or add an event.

#### Use cases

- Booking an appointment at a free time.
- Adding an event by clicking where it should go.
- Showing which times are free or busy.

#### When not to use it

- Picking a date only: use a date picker.
- Long events: show them as event blocks across the slots.

#### Best practices

- Make every free slot large enough to tap.
- Show busy and selected slots without relying on colour alone.
- Name each slot with its date and time for screen readers.
- Reveal hints on hover or focus to keep the grid calm.

### When to use

- Day and week views, booking grids.

### How to use

- `<button class="orca-slot" type="button" aria-label="Add event at 09:30, Friday 6 November">` with a `.orca-slot__hint`; busy slots are spans with `--busy`; chosen slots use `aria-pressed="true"`.
- Keep slots at least 24px high; snap new events to the slot.

#### Example: Slots

```django
<div style="max-width: 16rem; border: var(--orca-hairline) solid var(--orca-border-weak)">
  <button class="orca-slot" type="button" aria-label="Add event at 09:00">
    <span class="orca-slot__hint">+ Add event</span>
  </button>
  <span class="orca-slot orca-slot--busy">Busy</span>
  <button class="orca-slot" type="button" aria-pressed="true" aria-label="10:00, selected">10:00 selected</button>
</div>
```

**Classes:** `.orca-slot`, `.orca-slot__hint`, `.orca-slot--busy`

**Principles applied:** Practical UI F03: Reduce the total effort of a task; Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Time slot

---

## All-day row

`id: all-day-row` · level: component · source: ORCA

The strip above a week view's hours that holds all-day and multi-day bars.

Built from: `allday-bar`

### General description

A strip at the top of a day or week calendar for events that last all day or span several days.

#### Use cases

- Holidays, birthdays and day-long events.
- Trips and multi-day events across columns.
- Keeping all-day items apart from timed events.

#### When not to use it

- Events with a start and end time: place them in the hour grid.

#### Best practices

- Keep it above the timed hours.
- Stretch multi-day events across the days they cover.
- Show when an event continues past the visible days.
- Label the row clearly, for example 'All day'.

### When to use

- Week and day views.

### How to use

- `<div class="orca-allday-row">` with `.orca-allday-row__label` ('All day') and `.orca-allday-row__lane` (`--orca-days` columns); place all-day bars with `grid-column: 2 / span 3`.

#### Example: All day

```django
<div class="orca-allday-row" style="max-width: 36rem">
  <span class="orca-allday-row__label">All day</span>
  <div class="orca-allday-row__lane">
    <div class="orca-allday-bar" style="--orca-event: var(--orca-chart-1); grid-column: 1 / span 1">Inventory</div>
    <div class="orca-allday-bar orca-allday-bar--continues-after" style="--orca-event: var(--orca-chart-4); grid-column: 3 / span 5">Trade fair, 4–9 November</div>
  </div>
</div>
```

**Classes:** `.orca-allday-row`, `.orca-allday-row__label`, `.orca-allday-row__lane`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI L01: Group related information

**ORCA guide items covered:** All-day row

---

## Event chip

`id: event-chip` · level: component · source: ORCA

A one-line event in a month cell: colour dot, time and title.

Built from: `event-dot`, `time-label`

### General description

A small one-line label for an event, usually with a colour dot, a time and a title. It fits in a tight space.

#### Use cases

- Showing events inside month calendar cells.
- Compact lists of events.
- Linking a short entry to its full details.

#### When not to use it

- Roomy views: use an event card with more detail.
- Long lists: use an agenda list.

#### Best practices

- Show the start time and the first words of the title.
- Use a dot to show which calendar it belongs to.
- Give each chip a full spoken name.
- Mark cancelled events with more than colour alone.

### When to use

- Month views and mini lists.

### How to use

- `<button class="orca-event-chip" type="button">` (or a link) with an event dot, `.orca-event-chip__time` and `.orca-event-chip__title`; `--cancelled` strikes it through.
- Accessible name: the full event ('Audit, 10:00 to 11:00').

#### Example: Chips

```django
<div class="orca-stack" style="max-width: 10rem; gap: 2px">
  <button class="orca-event-chip" type="button" aria-label="Delivery, 09:00 to 10:00">
    <span class="orca-event-dot" style="--orca-event: var(--orca-chart-1)"></span>
    <span class="orca-event-chip__time">09:00</span>
    <span class="orca-event-chip__title">Delivery window</span>
  </button>
  <button class="orca-event-chip orca-event-chip--cancelled" type="button" aria-label="Training, cancelled">
    <span class="orca-event-dot" style="--orca-event: var(--orca-chart-4)"></span>
    <span class="orca-event-chip__time">14:00</span>
    <span class="orca-event-chip__title">Training</span>
  </button>
</div>
```

**Classes:** `.orca-event-chip`, `.orca-event-chip__time`, `.orca-event-chip__title`, `.orca-event-chip--cancelled`

**Principles applied:** Practical UI W04: Lead with the information people seek; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Event chip

---

## Event card

`id: event-card` · level: component · source: ORCA

An event block in a day or week view: title, time, place and its calendar colour edge.

Built from: `event-bar`, `time-label`

### General description

A block that represents an event in a day or week calendar, showing its title, time and place.

#### Use cases

- Showing events in day and week views.
- Opening the details of an event.
- Showing how long events last.

#### When not to use it

- Crowded month cells: use small chips.
- Simple lists: use an agenda item.

#### Best practices

- Size each block to the event's length.
- Show title first, then time and place.
- Mark tentative events with a pattern, not colour alone.
- Keep text readable against the card colour.
- Let overlapping events share the width.

### When to use

- Day and week views; the trigger for an event's detail popover.

### How to use

- `<button class="orca-event-card" style="--orca-event: var(--orca-chart-2)">` with `.orca-event-card__title` and `.orca-event-card__meta` (time and place); height follows duration (the view positions it).
- `--tentative` for unconfirmed events. Overlapping events share the column width.

#### Example: Cards

```django
<div class="orca-row" style="align-items: stretch; max-width: 30rem">
  <button class="orca-event-card" type="button" style="--orca-event: var(--orca-chart-1); height: 5rem; width: 12rem">
    <span class="orca-event-card__title">Delivery window</span>
    <span class="orca-event-card__meta"><time datetime="09:00">09:00</time>–<time datetime="10:30">10:30</time></span>
    <span class="orca-event-card__meta">
      {% icon "location" size="xs" %}
      Loading dock
    </span>
  </button>
  <button class="orca-event-card orca-event-card--tentative" type="button" style="--orca-event: var(--orca-chart-2); height: 3.5rem; width: 12rem">
    <span class="orca-event-card__title">Audit (tentative)</span>
    <span class="orca-event-card__meta">10:00–11:00</span>
  </button>
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

### General description

One entry in a list of events, usually with the time on the left and the title and details beside it.

#### Use cases

- Upcoming event lists.
- Calendars on small phone screens.
- A day's schedule in text form.

#### When not to use it

- Seeing free and busy gaps at a glance: use a day or week grid.

#### Best practices

- Group events under day headings.
- Put all-day events first.
- Keep the time in a fixed column so it is easy to scan.
- Show only the details people need, such as place.

### When to use

- Agenda view, upcoming events panels, phone calendars.

### How to use

- `<ol class="orca-agenda">` of `<li class="orca-agenda-item">` with `.orca-agenda-item__when` and `.orca-agenda-item__body` (event dot, `__title`, `__meta`).
- Group by day with a date badge or a day heading; all-day items first.

#### Example: Agenda

```django
<ol class="orca-agenda" style="max-width: 32rem">
  <li class="orca-agenda-item">
    <span class="orca-agenda-item__when">All day</span>
    <span class="orca-agenda-item__body">
      <span class="orca-event-dot" style="--orca-event: var(--orca-chart-4)"></span>
      <span class="orca-agenda-item__title">Trade fair</span>
      <span class="orca-agenda-item__meta">Day 3 of 6</span>
    </span>
  </li>
  <li class="orca-agenda-item">
    <span class="orca-agenda-item__when"><time datetime="09:00">09:00</time>–<time datetime="10:30">10:30</time></span>
    <span class="orca-agenda-item__body">
      <span class="orca-event-dot" style="--orca-event: var(--orca-chart-1)"></span>
      <span class="orca-agenda-item__title">Delivery window</span>
      <span class="orca-agenda-item__meta">Loading dock · 3 people</span>
    </span>
  </li>
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

### General description

A small box that looks like a calendar page, showing the month, day number and weekday.

#### Use cases

- Marking dates beside events in a list.
- Showing deadlines and upcoming dates.
- Headings for each day in an agenda.

#### When not to use it

- Dates in running text: write the date in words.
- Dates with times: show the time too.

#### Best practices

- Keep it small and consistent in every list.
- Give screen readers the full date in words.
- Use the real date tag for assistive tools.
- Do not rely on colour to carry meaning.

### When to use

- Beside events in lists, upcoming deadlines, day groups of an agenda.

### How to use

- `<time class="orca-date-badge" datetime="2026-11-06">` with `.orca-date-badge__month`, `__day` and `__weekday`; add an `aria-label` with the full date.

#### Example: Badge

```django
<time class="orca-date-badge" datetime="2026-11-06" aria-label="Friday 6 November 2026">
  <span class="orca-date-badge__month" aria-hidden="true">Nov</span>
  <span class="orca-date-badge__day" aria-hidden="true">6</span>
  <span class="orca-date-badge__weekday" aria-hidden="true">Fri</span>
</time>
```

**Classes:** `.orca-date-badge`, `.orca-date-badge__month`, `.orca-date-badge__day`, `.orca-date-badge__weekday`

**Principles applied:** Jakob's law: work the way products people already know work

**ORCA guide items covered:** Date badge

---

## Holiday label

`id: holiday-label` · level: component · source: ORCA

The holiday's name on a purple tint with a diamond mark.

Built from: `holiday-marker`

### General description

A short label naming a public holiday or closure on a calendar day.

#### Use cases

- Marking public holidays in a month view.
- Explaining why a site or office is closed.
- Showing closures in schedules.

#### When not to use it

- Personal events: use an event chip.
- Normal working days: show nothing extra.

#### Best practices

- Use the holiday's name, not just a colour.
- Add a mark or pattern so it is not colour-only.
- Say clearly when the place is closed.
- Keep the label short enough to fit the cell.

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

'+3 more' at the bottom of a crowded day cell; opens that day's full list.

Built from: `link-action`

### General description

A short link such as '+3 more' that shows when a calendar day has more events than fit.

#### Use cases

- Crowded cells in a month calendar.
- Opening the full list of one day.
- Showing that events are hidden, not missing.

#### When not to use it

- Days with space: show all events directly.

#### Best practices

- Show the exact number of hidden events.
- Open a popover or the day view with the full list.
- Give the link a spoken name that includes the date.
- Make it big enough to tap on phones.

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

### General description

The top bar of a calendar with the current month or period, arrows to move, and a switch between views.

#### Use cases

- Showing which period is on screen.
- Moving to the previous or next month or week.
- Switching between day, week, month and agenda views.

#### When not to use it

- Date pickers inside forms: use a compact picker header.

#### Best practices

- Show the period in words, such as 'November 2026'.
- Include a Today button to jump back.
- Name the arrows for screen readers.
- Keep the controls in the same place in every view.

### When to use

- Top of every calendar view.

### How to use

- `<div class="orca-cal-header">` with the calendar navigation, `<h2 class="orca-cal-header__title">November 2026</h2>` and the view switcher in `.orca-cal-header__end`.

#### Example: Header

```django
<div class="orca-cal-header">
  <div class="orca-cal-nav">
    <a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Previous month">
      {% icon "chevron-left" %}
    </a>
    <a class="orca-button" href="#">Today</a>
    <a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Next month">
      {% icon "chevron-right" %}
    </a>
  </div>
  <h2 class="orca-cal-header__title">November 2026</h2>
  <nav class="orca-segmented orca-segmented--dense orca-cal-header__end" aria-label="Calendar view">
    <a class="orca-segmented__item" href="#">Week</a>
    <a class="orca-segmented__item" href="#" aria-current="page">Month</a>
    <a class="orca-segmented__item" href="#">Agenda</a>
  </nav>
</div>
```

**Classes:** `.orca-cal-header`, `.orca-cal-header__title`, `.orca-cal-header__end`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI L14: Reduce travel between related actions

**ORCA guide items covered:** Calendar header (month label + navigation)

---
