from ..registry import add, category
from . import Component

C = category(
    "calendar-parts", "Calendar parts",
    "The building blocks of month, week, day and agenda views. Each gives screen readers the date in words.",
    level="component",
)

add(Component(
    "day-cell", "Day cell", C,
    "One day of a month view: day number, up to three events and a '+N more' link.",
    why="A fixed cell height keeps weeks aligned so the month reads as a grid (Jakob's law); capping visible events and linking to the rest keeps cells legible (Miller's law).",
    when=["Month views."],
    how=["`<td class=\"orca-cal-cell\">` with `.orca-cal-cell__inner`: the day number as a link to the day view (`.orca-cal-cell__day`, `aria-label` with the full date), event chips, holiday label, more-events link.",
         "States: `--today` (filled red day number + `aria-current=\"date\"`), `--outside`, `--weekend`, `--holiday`, `--selected`, `--closed` (hatched).",
         "On phones cells shrink and chips hide; the day's dot and count stay."],
    classes=[".orca-cal-cell", ".orca-cal-cell__inner", ".orca-cal-cell__day", ".orca-cal-cell--today", ".orca-cal-cell--outside", ".orca-cal-cell--weekend",
             ".orca-cal-cell--holiday", ".orca-cal-cell--selected", ".orca-cal-cell--closed"],
    laws=["jakob", "miller", "C03"],
    uses=["day-number", "today-marker", "event-chip", "more-events-link", "holiday-label"],
    examples=[("Cells", """<table class="orca-cal-month" style="max-width: 36rem"><tbody><tr>
  <td class="orca-cal-cell"><div class="orca-cal-cell__inner"><a class="orca-cal-cell__day" href="#" aria-label="Thursday 5 November">5</a><button class="orca-event-chip" type="button"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-1)"></span><span class="orca-event-chip__time">09:00</span><span class="orca-event-chip__title">Delivery</span></button></div></td>
  <td class="orca-cal-cell orca-cal-cell--today"><div class="orca-cal-cell__inner"><a class="orca-cal-cell__day" href="#" aria-current="date" aria-label="Friday 6 November, today">6</a><button class="orca-event-chip" type="button"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-2)"></span><span class="orca-event-chip__time">10:00</span><span class="orca-event-chip__title">Audit</span></button><button class="orca-event-chip" type="button"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-1)"></span><span class="orca-event-chip__time">14:00</span><span class="orca-event-chip__title">Training</span></button><button class="orca-more-link" type="button" aria-label="3 more events on 6 November">+3 more</button></div></td>
  <td class="orca-cal-cell orca-cal-cell--weekend orca-cal-cell--holiday"><div class="orca-cal-cell__inner"><a class="orca-cal-cell__day" href="#" aria-label="Saturday 7 November, Founders day">7</a><span class="orca-holiday-label">Founders day</span></div></td>
</tr></tbody></table>""")],
    guide=["Day cell"],
))

add(Component(
    "week-header", "Week header", C,
    "The week number and its date range, heading a week view.",
    why="Teams that plan in weeks need the number; the range confirms which days it covers (Tesler's law: no mental arithmetic).",
    when=["Week views, sprint and roster pages."],
    how=["`<div class=\"orca-week-header\">` with a week number and `.orca-week-header__range` dates ('2–8 November 2026')."],
    classes=[".orca-week-header", ".orca-week-header__range"],
    laws=["tesler", "miller"],
    uses=["week-number", "date-label"],
    examples=[("Week 45", """<div class="orca-week-header"><span class="orca-week-number" title="Week 45">W45</span><span class="orca-week-header__range"><time datetime="2026-11-02">2</time>–<time datetime="2026-11-08">8 November 2026</time></span></div>""")],
    guide=["Week header"],
))

add(Component(
    "weekday-header", "Weekday header", C,
    "The row of weekday names above a month or week grid.",
    why="Column headers tell people which day each column is; short uppercase labels fit narrow columns (Practical UI W07) and the full name is in the abbreviation.",
    when=["Top of month and week grids."],
    how=["`<thead class=\"orca-cal-weekdays\"><tr>` of `<th scope=\"col\"><abbr title=\"Monday\">Mon</abbr></th>`; weekend columns get `.is-weekend`.",
         "Start on the locale's first weekday."],
    classes=[".orca-cal-weekdays"],
    laws=["W07", "jakob"],
    uses=["weekday-name"],
    examples=[("Header", """<table class="orca-cal-month"><thead class="orca-cal-weekdays"><tr><th scope="col"><abbr title="Monday">Mon</abbr></th><th scope="col"><abbr title="Tuesday">Tue</abbr></th><th scope="col"><abbr title="Wednesday">Wed</abbr></th><th scope="col"><abbr title="Thursday">Thu</abbr></th><th scope="col"><abbr title="Friday">Fri</abbr></th><th scope="col" class="is-weekend"><abbr title="Saturday">Sat</abbr></th><th scope="col" class="is-weekend"><abbr title="Sunday">Sun</abbr></th></tr></thead></table>""")],
    guide=["Weekday header"],
))

add(Component(
    "week-row", "Week row", C,
    "One row of a month grid: the week number and seven day cells.",
    why="Grouping days into week rows chunks the month (Miller's law); the week number on the row helps teams that plan by week.",
    when=["Month views."],
    how=["`<tr class=\"orca-cal-week\">` with an optional `<th scope=\"row\">45</th>` then seven `td.orca-cal-cell`."],
    classes=[".orca-cal-week", ".orca-cal-month"],
    laws=["miller"],
    uses=["day-cell", "week-number"],
    examples=[("Row", """<table class="orca-cal-month"><tbody><tr class="orca-cal-week"><th scope="row"><abbr title="Week 45">45</abbr></th>{% for d in "2345678" %}<td class="orca-cal-cell{% if forloop.counter > 5 %} orca-cal-cell--weekend{% endif %}" style="height: 3rem"><div class="orca-cal-cell__inner"><a class="orca-cal-cell__day" href="#">{{ d }}</a></div></td>{% endfor %}</tr></tbody></table>""")],
    guide=["Week row"],
))

add(Component(
    "hour-row", "Hour row", C,
    "One hour of a day or week view: the hour label and two half-hour slots.",
    why="Hour lines give the day a scale (Practical UI S02: faint, not competing); the label in the gutter keeps the slots free for events.",
    when=["Day and week views, resource schedulers."],
    how=["`<div class=\"orca-hour-row\">` with `.orca-hour-row__label` (`<time>`) and `.orca-hour-row__slots` holding two time slots.",
         "Show working hours by default and scroll to 'now' on load."],
    classes=[".orca-hour-row", ".orca-hour-row__label", ".orca-hour-row__slots"],
    laws=["S02", "jakob"],
    uses=["hour-gridline", "time-slot", "time-label"],
    examples=[("Two hours", """<div style="max-width: 24rem; padding-top: var(--orca-space-8)">
  <div class="orca-hour-row"><time class="orca-hour-row__label" datetime="09:00">09:00</time><div class="orca-hour-row__slots"><button class="orca-slot" type="button" aria-label="Add event at 09:00"><span class="orca-slot__hint">+ Add</span></button><button class="orca-slot" type="button" aria-label="Add event at 09:30"><span class="orca-slot__hint">+ Add</span></button></div></div>
  <div class="orca-hour-row"><time class="orca-hour-row__label" datetime="10:00">10:00</time><div class="orca-hour-row__slots"><span class="orca-slot orca-slot--busy">Busy</span><button class="orca-slot" type="button" aria-label="Add event at 10:30"><span class="orca-slot__hint">+ Add</span></button></div></div>
</div>""")],
    guide=["Hour row"],
))

add(Component(
    "time-slot", "Time slot", C,
    "An empty half-hour in a day view that creates an event when chosen; free, busy or selected.",
    why="Clicking where the event should go is the most direct way to create it (Practical UI F03, Fitts's law); the hint appears on hover and focus only, so the grid stays calm.",
    when=["Day and week views, booking grids."],
    how=["`<button class=\"orca-slot\" type=\"button\" aria-label=\"Add event at 09:30, Friday 6 November\">` with a `.orca-slot__hint`; busy slots are spans with `--busy`; chosen slots use `aria-pressed=\"true\"`.",
         "Keep slots at least 24px high; snap new events to the slot."],
    classes=[".orca-slot", ".orca-slot__hint", ".orca-slot--busy"],
    laws=["F03", "fitts", "C03"],
    uses=["availability-color"],
    examples=[("Slots", """<div style="max-width: 16rem; border: var(--orca-hairline) solid var(--orca-border-weak)"><button class="orca-slot" type="button" aria-label="Add event at 09:00"><span class="orca-slot__hint">+ Add event</span></button><span class="orca-slot orca-slot--busy">Busy</span><button class="orca-slot" type="button" aria-pressed="true" aria-label="10:00, selected">10:00 selected</button></div>""")],
    guide=["Time slot"],
))

add(Component(
    "all-day-row", "All-day row", C,
    "The strip above a week view's hours that holds all-day and multi-day bars.",
    why="Separating all-day items from timed ones keeps both readable (Miller's law) and shows multi-day spans across columns (Gestalt continuity).",
    when=["Week and day views."],
    how=["`<div class=\"orca-allday-row\">` with `.orca-allday-row__label` ('All day') and `.orca-allday-row__lane` (`--orca-days` columns); place all-day bars with `grid-column: 2 / span 3`."],
    classes=[".orca-allday-row", ".orca-allday-row__label", ".orca-allday-row__lane"],
    laws=["miller", "L01"],
    uses=["allday-bar"],
    examples=[("All day", """<div class="orca-allday-row" style="max-width: 36rem"><span class="orca-allday-row__label">All day</span><div class="orca-allday-row__lane"><div class="orca-allday-bar" style="--orca-event: var(--orca-chart-1); grid-column: 1 / span 1">Inventory</div><div class="orca-allday-bar orca-allday-bar--continues-after" style="--orca-event: var(--orca-chart-4); grid-column: 3 / span 5">Trade fair, 4–9 November</div></div></div>""")],
    guide=["All-day row"],
))

add(Component(
    "event-chip", "Event chip", C,
    "A one-line event in a month cell: colour dot, time and title.",
    why="In a small cell the time and the start of the title identify an event (Practical UI W04); the dot keys its calendar without filling the cell with colour.",
    when=["Month views and mini lists."],
    how=["`<button class=\"orca-event-chip\" type=\"button\">` (or a link) with an event dot, `.orca-event-chip__time` and `.orca-event-chip__title`; `--cancelled` strikes it through.",
         "Accessible name: the full event ('Audit, 10:00 to 11:00')."],
    classes=[".orca-event-chip", ".orca-event-chip__time", ".orca-event-chip__title", ".orca-event-chip--cancelled"],
    laws=["W04", "C03"],
    uses=["event-dot", "time-label"],
    examples=[("Chips", """<div class="orca-stack" style="max-width: 10rem; gap: 2px"><button class="orca-event-chip" type="button" aria-label="Delivery, 09:00 to 10:00"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-1)"></span><span class="orca-event-chip__time">09:00</span><span class="orca-event-chip__title">Delivery window</span></button><button class="orca-event-chip orca-event-chip--cancelled" type="button" aria-label="Training, cancelled"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-4)"></span><span class="orca-event-chip__time">14:00</span><span class="orca-event-chip__title">Training</span></button></div>""")],
    guide=["Event chip"],
))

add(Component(
    "event-card", "Event card", C,
    "An event block in a day or week view: title, time, place and its calendar colour edge.",
    why="Blocks sized to their duration show the shape of a day at a glance (Jakob's law); a tinted fill keeps text readable (C01) and hatching marks tentative events without colour alone (C03).",
    when=["Day and week views; the trigger for an event's detail popover."],
    how=["`<button class=\"orca-event-card\" style=\"--orca-event: var(--orca-chart-2)\">` with `.orca-event-card__title` and `.orca-event-card__meta` (time and place); height follows duration (the view positions it).",
         "`--tentative` for unconfirmed events. Overlapping events share the column width."],
    classes=[".orca-event-card", ".orca-event-card__title", ".orca-event-card__meta", ".orca-event-card--tentative"],
    laws=["jakob", "C01", "C03"],
    uses=["event-bar", "time-label"],
    examples=[("Cards", """<div class="orca-row" style="align-items: stretch; max-width: 30rem">
  <button class="orca-event-card" type="button" style="--orca-event: var(--orca-chart-1); height: 5rem; width: 12rem"><span class="orca-event-card__title">Delivery window</span><span class="orca-event-card__meta"><time datetime="09:00">09:00</time>–<time datetime="10:30">10:30</time></span><span class="orca-event-card__meta">{% icon "location" size="xs" %}Loading dock</span></button>
  <button class="orca-event-card orca-event-card--tentative" type="button" style="--orca-event: var(--orca-chart-2); height: 3.5rem; width: 12rem"><span class="orca-event-card__title">Audit (tentative)</span><span class="orca-event-card__meta">10:00–11:00</span></button>
</div>""")],
    guide=["Event card"],
))

add(Component(
    "agenda-item", "Agenda item", C,
    "One event in a list view: time column, colour dot, title and details.",
    why="A list is the most readable calendar view on small screens and for screen readers (Postel's law); a fixed time column makes the day scannable.",
    when=["Agenda view, upcoming events panels, phone calendars."],
    how=["`<ol class=\"orca-agenda\">` of `<li class=\"orca-agenda-item\">` with `.orca-agenda-item__when` and `.orca-agenda-item__body` (event dot, `__title`, `__meta`).",
         "Group by day with a date badge or a day heading; all-day items first."],
    classes=[".orca-agenda", ".orca-agenda-item", ".orca-agenda-item__when", ".orca-agenda-item__body", ".orca-agenda-item__title", ".orca-agenda-item__meta"],
    laws=["postel", "miller"],
    uses=["event-dot", "time-label", "date-badge"],
    examples=[("Agenda", """<ol class="orca-agenda" style="max-width: 32rem">
  <li class="orca-agenda-item"><span class="orca-agenda-item__when">All day</span><span class="orca-agenda-item__body"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-4)"></span><span class="orca-agenda-item__title">Trade fair</span><span class="orca-agenda-item__meta">Day 3 of 6</span></span></li>
  <li class="orca-agenda-item"><span class="orca-agenda-item__when"><time datetime="09:00">09:00</time>–<time datetime="10:30">10:30</time></span><span class="orca-agenda-item__body"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-1)"></span><span class="orca-agenda-item__title">Delivery window</span><span class="orca-agenda-item__meta">Loading dock · 3 people</span></span></li>
</ol>""")],
    guide=["Agenda item"],
))

add(Component(
    "date-badge", "Date badge", C,
    "A small calendar-page box with month, day number and weekday.",
    why="The calendar-page shape is recognised instantly as a date (Jakob's law) and anchors lists of dated items.",
    when=["Beside events in lists, upcoming deadlines, day groups of an agenda."],
    how=["`<time class=\"orca-date-badge\" datetime=\"2026-11-06\">` with `.orca-date-badge__month`, `__day` and `__weekday`; add an `aria-label` with the full date."],
    classes=[".orca-date-badge", ".orca-date-badge__month", ".orca-date-badge__day", ".orca-date-badge__weekday"],
    laws=["jakob"],
    uses=["month-name", "day-number", "weekday-name"],
    examples=[("Badge", """<time class="orca-date-badge" datetime="2026-11-06" aria-label="Friday 6 November 2026"><span class="orca-date-badge__month" aria-hidden="true">Nov</span><span class="orca-date-badge__day" aria-hidden="true">6</span><span class="orca-date-badge__weekday" aria-hidden="true">Fri</span></time>""")],
    guide=["Date badge"],
))

add(Component(
    "holiday-label", "Holiday label", C,
    "The holiday's name on a purple tint with a diamond mark.",
    why="Naming the holiday explains why a day is closed or quiet (Peak–end rule); the mark and tint make it findable without colour alone.",
    when=["Day cells, agenda days and schedules on public holidays and closures."],
    how=["`<span class=\"orca-holiday-label\">Armistice Day</span>`; add '(closed)' when the site is closed."],
    classes=[".orca-holiday-label"],
    laws=["peak-end", "C03"],
    uses=["holiday-marker"],
    examples=[("Holiday", """<span class="orca-holiday-label">Armistice Day (closed)</span>""")],
    guide=["Holiday label"],
))

add(Component(
    "more-events-link", "More-events link", C,
    "'+3 more' at the bottom of a crowded day cell; opens that day's full list.",
    why="Capping a cell's events keeps the month legible (Miller's law) while the link proves nothing is hidden (Practical UI S06).",
    when=["Month cells with more events than fit."],
    how=["`<button class=\"orca-more-link\" type=\"button\" aria-label=\"3 more events on 6 November\">+3 more</button>` opening a popover or the day view."],
    classes=[".orca-more-link"],
    laws=["miller", "S06"],
    uses=["link-action"],
    examples=[("Link", """<button class="orca-more-link" type="button" aria-label="3 more events on 6 November">+3 more</button>""")],
    guide=['More-events link ("+3 more")'],
))

add(Component(
    "calendar-header", "Calendar header", C,
    "The month or period title with navigation and the view switcher.",
    why="One header that answers 'when am I looking at?' and holds every way to move keeps navigation predictable (Jakob's law, Practical UI L14).",
    when=["Top of every calendar view."],
    how=["`<div class=\"orca-cal-header\">` with the calendar navigation, `<h2 class=\"orca-cal-header__title\">November 2026</h2>` and the view switcher in `.orca-cal-header__end`."],
    classes=[".orca-cal-header", ".orca-cal-header__title", ".orca-cal-header__end"],
    laws=["jakob", "L14"],
    uses=["calendar-navigation", "calendar-view-switcher", "month-name"],
    examples=[("Header", """<div class="orca-cal-header"><div class="orca-cal-nav"><a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Previous month">{% icon "chevron-left" %}</a><a class="orca-button" href="#">Today</a><a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Next month">{% icon "chevron-right" %}</a></div>
  <h2 class="orca-cal-header__title">November 2026</h2>
  <nav class="orca-segmented orca-segmented--dense orca-cal-header__end" aria-label="Calendar view"><a class="orca-segmented__item" href="#">Week</a><a class="orca-segmented__item" href="#" aria-current="page">Month</a><a class="orca-segmented__item" href="#">Agenda</a></nav></div>""")],
    guide=["Calendar header (month label + navigation)"],
))
