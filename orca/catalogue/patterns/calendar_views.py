from ..registry import add, category
from . import Pattern

C = category(
    "calendar-views", "Calendar views",
    "Whole calendars rendered on the server from a list of events: month, week, day, multi-day, agenda and year, plus the toolbar, sidebar and legend around them.",
    level="pattern",
)

EVENTS_HOW = ("Events are dicts: `title`, `start` and `end` (ISO date or datetime), `all_day`, `color` (1–8, the chart palette, "
              "or any CSS colour), `url`, `location`, `status` ('tentative', 'cancelled'). Pass your queryset as `.values()` or build the dicts in the view.")
TODAY_HOW = "Pass `today` (and `now` for time grids) from the view in the site's timezone; tests and previews pin them to a fixed date."
NAV_HOW = "Navigation is plain links with the period in the query string (`?month=2026-11`), so back, refresh and sharing work; htmx can swap only the grid."

add(Pattern(
    "month-calendar", "Month calendar", C,
    "Weeks of day cells showing each day's events, with '+N more' when a day overflows and a count dot on phones.",
    why="A month shows how busy each day is and where the gaps are, which is what people plan with (Miller's law: a few events per cell, the rest behind '+N more'). On phones the grid becomes counts and tapping a day opens its agenda (Fitts's law).",
    when=["Planning across weeks: bookings, rotas, events, deadlines."],
    avoid=["Detailed times on one or two days: use the week or day view."],
    how=["`{% templatetag openblock %} orca_month_calendar events month=\"2026-11\" today=today selected=day day_url=\"?day={date}\" holidays=holidays max_per_day=3 {% templatetag closeblock %}`.",
         EVENTS_HOW, TODAY_HOW, NAV_HOW,
         "Multi-day all-day events show as bars on each day they cover; holidays label the cell."],
    a11y=["Each day is a link or cell labelled with its full date and event count; the table has weekday column headers."],
    classes=[".orca-month-view", ".orca-cal-cell__count"],
    laws=["miller", "fitts", "jakob"],
    uses=["calendar-header", "weekday-header", "week-row", "day-cell", "event-chip", "more-events-link", "holiday-label"],
    examples=[("November 2026", '{% orca_month_calendar sample.events month="2026-11" today=sample.today holidays=sample.holidays day_url="#{date}" %}')],
    guide=["Month calendar"],
))

add(Pattern(
    "week-view", "Week view", C,
    "Seven day columns on an hour grid with events positioned by time, an all-day row and a line at the current time.",
    why="Seeing time as height makes durations, gaps and overlaps obvious (Practical UI L01, grouping: each day a column); overlapping events share the width side by side so none hides another.",
    when=["Scheduling within a week: meetings, installs, shifts."],
    how=["`{% templatetag openblock %} orca_week_view events start=monday today=today now=now start_hour=7 end_hour=19 {% templatetag closeblock %}` (start defaults to today's week start).",
         EVENTS_HOW, TODAY_HOW, NAV_HOW,
         "The grid scrolls horizontally on narrow screens; offer day view as the phone default."],
    a11y=["Every event is a link or button whose text gives title, day and times; the now-line is decorative."],
    classes=[".orca-timegrid", ".orca-timegrid__head", ".orca-timegrid__allday", ".orca-timegrid__body", ".orca-timegrid__col", ".orca-timegrid__event", ".orca-timegrid__now"],
    laws=["L01", "jakob", "miller"],
    uses=["week-header", "all-day-row", "hour-row", "time-slot", "event-card", "calendar-header"],
    examples=[("This week", '{% orca_week_view sample.events start="2026-11-02" today=sample.today now=sample.now start_hour=8 end_hour=19 %}')],
    guide=["Week view"],
))

add(Pattern(
    "day-view", "Day view", C,
    "One day on the hour grid: the full detail of a single day, and the phone default.",
    why="One column leaves room for each event's title, time and place, so there is no truncation and no tooltip hunting (Fitts's law: large targets on touch screens).",
    when=["Phones; a person's or a room's day; dense days."],
    how=["`{% templatetag openblock %} orca_week_view events start=day days=1 today=today now=now {% templatetag closeblock %}`.", EVENTS_HOW, TODAY_HOW,
         "Pair with a mini calendar or a date strip to change day."],
    classes=[".orca-timegrid--day"],
    laws=["fitts", "jakob"],
    uses=["hour-row", "time-slot", "event-card", "calendar-navigation"],
    examples=[("Friday 6 November", '{% orca_week_view sample.events start=sample.today days=1 today=sample.today now=sample.now start_hour=9 end_hour=18 %}')],
    guide=["Day view"],
))

add(Pattern(
    "agenda-view", "Agenda view", C,
    "Upcoming events listed by day, with times, colours and places: the most readable calendar on any screen.",
    why="A list is read top to bottom without decoding a grid (Jakob's law: like a to-do list) and works on every screen and with screen readers. Empty days are skipped so the list stays short.",
    when=["Phones, 'what's next' panels, screen-reader friendly alternative to grids, printing."],
    how=["`{% templatetag openblock %} orca_agenda events start=today days=7 today=today {% templatetag closeblock %}`.", EVENTS_HOW,
         "Show an empty state when nothing is planned ('Nothing planned this week')."],
    classes=[".orca-agenda-view", ".orca-agenda-view__day"],
    laws=["jakob", "L03"],
    uses=["agenda-item", "date-badge", "empty-state"],
    examples=[("This week", '{% orca_agenda sample.events start="2026-11-02" days=7 today=sample.today %}')],
    guide=["Agenda (list) view"],
))

add(Pattern(
    "year-view", "Year view", C,
    "Twelve small months with event days marked, to see a year's rhythm and jump to any day.",
    why="Long-range planning (holidays, seasons, launches) needs the whole year at once (Practical UI L09: months grouped in a grid); each day links to its detail.",
    when=["Holiday planning, annual schedules, picking dates far ahead."],
    how=["`{% templatetag openblock %} orca_year_view year=2026 events=events today=today url=\"?day={date}\" {% templatetag closeblock %}`.",
         "Days with events carry a dot; the URL template gets the ISO date."],
    classes=[".orca-year-view"],
    laws=["L09", "miller"],
    uses=["mini-calendar"],
    examples=[("2026", '{% orca_year_view year=2026 events=sample.events today=sample.today url="#{date}" %}')],
    guide=["Year view"],
))

add(Pattern(
    "multi-day-view", "Multi-day view", C,
    "Three (or any number of) days on the hour grid, between the day and week views.",
    why="Three days fit a tablet or a narrow panel while still showing what comes next (Miller's law); it keeps the hour grid's clarity without the week's horizontal scroll.",
    when=["Tablets, side panels, 'today and the next two days'."],
    how=["`{% templatetag openblock %} orca_week_view events start=today days=3 today=today now=now {% templatetag closeblock %}`.", EVENTS_HOW],
    classes=[".orca-timegrid"],
    laws=["miller", "jakob"],
    uses=["week-header", "all-day-row", "event-card"],
    examples=[("Next three days", '{% orca_week_view sample.events start="2026-11-04" days=3 today=sample.today now=sample.now start_hour=8 end_hour=18 %}')],
    guide=["Multi-day view"],
))

add(Pattern(
    "calendar-toolbar", "Calendar toolbar", C,
    "The bar above any calendar view: previous, Today, next, the period title, the view switcher and a create button.",
    why="People move through time and change zoom constantly; the same controls in the same place across every view (Jakob's law) and a large 'Today' to get home (Fitts's law) make that effortless.",
    when=["Above every month, week, day, agenda and year view."],
    how=["`<div class=\"orca-cal-header\">` with the calendar navigation, `h2.orca-cal-header__title` and the view switcher in `.orca-cal-header__end`; add the create button last.",
         NAV_HOW, "The title announces the period politely when it changes (`aria-live`)."],
    classes=[".orca-cal-header", ".orca-cal-header__title", ".orca-cal-header__end"],
    laws=["jakob", "fitts"],
    uses=["calendar-header", "calendar-navigation", "calendar-view-switcher", "create-button"],
    examples=[("Toolbar", """<div class="orca-cal-header"><div class="orca-cal-nav"><a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Previous week">{% icon "chevron-left" %}</a><a class="orca-button" href="#">Today</a><a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Next week">{% icon "chevron-right" %}</a></div>
  <h2 class="orca-cal-header__title" aria-live="polite">2–8 November 2026</h2>
  <div class="orca-row orca-cal-header__end"><nav class="orca-segmented orca-segmented--dense" aria-label="Calendar view"><a class="orca-segmented__item" href="#">Day</a><a class="orca-segmented__item" href="#" aria-current="page">Week</a><a class="orca-segmented__item" href="#">Month</a><a class="orca-segmented__item" href="#">Agenda</a></nav><a class="orca-button orca-button--primary" href="#">{% icon "plus" %}New event</a></div></div>""")],
    guide=["Calendar toolbar"],
))

add(Pattern(
    "mini-calendar-sidebar", "Mini-calendar sidebar", C,
    "A sidebar beside the main calendar: create button, mini calendar to jump to any date, and the calendars legend.",
    why="Jumping weeks ahead with arrows is slow; a mini calendar gets there in one click (Fitts's law), and the legend filters what the main view shows (Hick's law: hide what does not matter now). It moves below the calendar on narrow screens.",
    when=["Full calendar pages with more than one calendar or long-range navigation."],
    how=["`<div class=\"orca-cal-layout\">` with `<aside class=\"orca-cal-sidebar\">` first and the toolbar and view second.",
         "The mini calendar's selected day matches the main view; event days carry a dot."],
    classes=[".orca-cal-layout", ".orca-cal-sidebar"],
    laws=["fitts", "hick"],
    uses=["mini-calendar", "create-button"],
    examples=[("Sidebar", """<div class="orca-cal-layout"><aside class="orca-cal-sidebar" aria-label="Calendar options"><a class="orca-button orca-button--primary" href="#">{% icon "plus" %}New event</a>
    {% orca_mini_calendar "2026-11-01" selected="2026-11-06" today="2026-11-06" url="#{date}" nav_url="#{month}" events="2026-11-02,2026-11-03,2026-11-04,2026-11-05,2026-11-06,2026-11-10" %}
    <fieldset class="orca-cal-legend"><legend>Calendars</legend><label class="orca-check" style="--orca-event: var(--orca-chart-1)"><input type="checkbox" checked><span class="orca-check__box"></span>Deliveries</label><label class="orca-check" style="--orca-event: var(--orca-chart-3)"><input type="checkbox" checked><span class="orca-check__box"></span>Meetings</label></fieldset></aside>
  {% orca_agenda sample.events start="2026-11-06" days=5 today=sample.today %}</div>""")],
    guide=["Mini-calendar sidebar"],
))

add(Pattern(
    "calendar-legend", "Calendar legend", C,
    "The list of calendars, each a checkbox in its colour, to show or hide its events.",
    why="Colour identifies a calendar only if the key is visible (Practical UI C03); checkboxes let people declutter the view to what matters now (Hick's law). Names carry the meaning so colour is never the only cue.",
    when=["Any calendar showing events from more than one source, person or type."],
    how=["`<fieldset class=\"orca-cal-legend\">` with a `legend` and `label.orca-check` items, each setting `--orca-event` to the calendar's colour.",
         "Submit changes as a GET filter (`?cal=deliveries&cal=meetings`) or toggle with htmx."],
    classes=[".orca-cal-legend"],
    laws=["C03", "hick"],
    uses=["checkbox", "legend-item"],
    examples=[("Calendars", """<fieldset class="orca-cal-legend"><legend>Calendars</legend>
  <label class="orca-check" style="--orca-event: var(--orca-chart-1)"><input type="checkbox" checked><span class="orca-check__box"></span>Deliveries</label>
  <label class="orca-check" style="--orca-event: var(--orca-chart-2)"><input type="checkbox" checked><span class="orca-check__box"></span>Installs and audits</label>
  <label class="orca-check" style="--orca-event: var(--orca-chart-3)"><input type="checkbox" checked><span class="orca-check__box"></span>Meetings</label>
  <label class="orca-check" style="--orca-event: var(--orca-chart-4)"><input type="checkbox"><span class="orca-check__box"></span>Public holidays</label></fieldset>""")],
    guide=["Calendar legend (calendars and colours)"],
))
