from .registry import Element, add, category

INP = category(
    "planning-inputs", "Planning inputs",
    "Date, time and schedule inputs. Native pickers first: they are what people already know, on every device.",
)
TXT = category(
    "planning-text", "Planning text",
    "How dates, times and durations are written. Always machine-readable (`<time datetime>`) and formatted for the reader's locale and timezone.",
)
MRK = category(
    "planning-marks", "Planning marks",
    "Marks drawn on calendars, schedules and timelines. Each state pairs colour with a shape, a pattern or a word.",
)
ICN = category(
    "planning-icons", "Planning icons",
    "Icons for time and scheduling ideas, drawn by ORCA on the same 16px grid as the rest of the set.",
)

TIME = "Format with Django's `date` filter and `TIME_FORMAT` / `DATE_FORMAT` (locale aware) after converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`)."

# ------------------------------------------------------------------ inputs
add(Element(
    "date-input", "Date input", INP,
    "A native date field (`type=\"date\"`) with ORCA styling.",
    why="The platform date picker is familiar, accessible and localised (Jakob's law, Postel's law); the guide's own advice "
        "is to prefer native date and time inputs for planning UI.",
    when=["Picking a single day: a deadline, a report date, a holiday."],
    avoid=["Dates people know by heart and type faster (birth dates): use the split date input (phase 2) or three numeric fields."],
    how=["`<input class=\"orca-input\" type=\"date\" id=… name=… min=… max=…>`.",
         "Set `min`/`max` for allowed ranges; explain the range in help text.",
         "Prefill sensible defaults (today, next working day) rather than leaving it empty (Tesler's law).",
         "The server always receives ISO `YYYY-MM-DD`."],
    a11y=["Label it with the event, not the format: 'Report date', not 'dd/mm/yyyy'."],
    classes=[".orca-input[type=date]"], tokens=["bg-input"],
    laws=["jakob", "postel", "tesler"],
    examples=[("Date", """<label class="orca-label" for="d1">Report date</label>
<input class="orca-input" type="date" id="d1" value="2026-11-06" max="2026-12-31">""")],
    guide=["Date input"], related=["time-input", "datetime-input"], source="ORCA",
))

add(Element(
    "time-input", "Time input", INP,
    "A native time field (`type=\"time\"`).",
    why="Native time fields follow the reader's 12/24-hour convention automatically (Postel's law) and open the platform picker on phones (Jakob's law).",
    when=["Start and end times, reminder times, opening hours."],
    how=["`<input class=\"orca-input\" type=\"time\" step=\"900\">` (step in seconds: 900 = 15 minutes).",
         "Show the timezone next to it with a timezone label when people may be in another zone than the place."],
    classes=[".orca-input[type=time]"],
    laws=["postel", "jakob"],
    examples=[("Time with timezone", """<label class="orca-label" for="t1">Opens at</label>
<div class="orca-row"><input class="orca-input" type="time" id="t1" value="08:30" step="900"><span class="orca-tz" title="Europe/Paris">CET</span></div>""")],
    guide=["Time input"], related=["timezone-label"], source="ORCA",
))

add(Element(
    "datetime-input", "Date-time input", INP,
    "A native `datetime-local` field for one moment.",
    why="One control for one moment avoids mismatched date and time pairs (Postel's law).",
    when=["A single event moment: when a run starts, when a link expires."],
    avoid=["Ranges: use two fields (start, end) side by side."],
    how=["`<input class=\"orca-input\" type=\"datetime-local\" step=\"60\">`. The value has no timezone: store it with the place's timezone on the server."],
    classes=[".orca-input[type=datetime-local]"],
    laws=["postel"],
    examples=[("Date-time", """<label class="orca-label" for="dt1">Start run at</label>
<input class="orca-input" type="datetime-local" id="dt1" value="2026-11-07T07:00">""")],
    guide=["Date-time input"], source="ORCA",
))

add(Element(
    "duration-input", "Duration input", INP,
    "Hours and minutes as two short numeric fields with their units.",
    why="Two labelled parts are faster and less error-prone than a free-text '1h30' or a long dropdown (Practical UI R13, "
        "Postel's law: accept the parts and normalise).",
    when=["Durations: shift length, retention, reminder offset."],
    how=["`<fieldset class=\"orca-duration\">` with a legend and two `.orca-duration__part` groups: number input + `.orca-addon` (h, min).",
         "Accept minutes over 59 and normalise on the server (90 min → 1 h 30 min).", "Display with `{{ minutes|orca_duration }}`."],
    classes=[".orca-duration", ".orca-duration__part"],
    laws=["R13", "postel"],
    examples=[("Duration", """<fieldset class="orca-duration" style="border: 0; padding: 0; margin: 0">
  <legend class="orca-label">Shift length</legend>
  <span class="orca-duration__part"><input class="orca-input" type="number" min="0" max="23" value="7" aria-label="Hours" id="du-h"><span class="orca-addon">h</span></span>
  <span class="orca-duration__part"><input class="orca-input" type="number" min="0" step="5" value="30" aria-label="Minutes" id="du-m"><span class="orca-addon">min</span></span>
</fieldset>""")],
    guide=["Duration input"], source="ORCA",
))

add(Element(
    "timezone-select", "Timezone select", INP,
    "A native select of IANA timezones, grouped by region, preselected from context.",
    why="Timezones are inherent complexity; ORCA moves it to the system by listing real zones and preselecting the "
        "site's or browser's zone so most people never touch it (Tesler's law).",
    when=["Setting a site's, camera's or user's timezone."],
    how=["`<select class=\"orca-select\">{% orca_timezone_options current_zone %}</select>`.",
         "Preselect from the object (site), then the user profile, then the browser (`Intl.DateTimeFormat().resolvedOptions().timeZone`).",
         "Store the IANA name ('Europe/Paris'), never an offset."],
    classes=[".orca-select"],
    laws=["tesler", "postel"],
    examples=[("Timezone", """<label class="orca-label" for="tz1">Site timezone</label>
<select class="orca-select" id="tz1" style="max-width: 20rem">{% orca_timezone_options "Europe/Paris" %}</select>""")],
    guide=["Timezone select"], related=["timezone-label"], source="Tangerine",
))

add(Element(
    "weekday-toggle", "Weekday toggle", INP,
    "Seven square toggles for picking days of the week.",
    why="All seven days visible and toggled in place is faster than seven checkboxes or a multi-select (Practical UI F03, R11), "
        "and the checked fill plus bold text show state without colour alone.",
    when=["Recurrence on chosen days, opening days, shift days."],
    how=["`<fieldset class=\"orca-weekday-toggles\"><legend class=\"orca-sr-only\">Repeat on</legend>` with one `<label class=\"orca-weekday\"><input type=\"checkbox\" name=\"days\" value=\"mon\"><span aria-hidden=\"true\">M</span><span class=\"orca-sr-only\">Monday</span></label>` per day.",
         "Start the week on the locale's first day (`FIRST_DAY_OF_WEEK`).", "Offer presets (Weekdays, Every day) next to it."],
    a11y=["The visible letter is hidden from screen readers; the full day name is read."],
    classes=[".orca-weekday-toggles", ".orca-weekday"], tokens=["accent", "border-strong"],
    laws=["F03", "R11", "C03"],
    examples=[("Days", """<fieldset class="orca-weekday-toggles"><legend class="orca-label">Repeat on</legend>
<label class="orca-weekday"><input type="checkbox" checked><span aria-hidden="true">M</span><span class="orca-sr-only">Monday</span></label><label class="orca-weekday"><input type="checkbox" checked><span aria-hidden="true">T</span><span class="orca-sr-only">Tuesday</span></label><label class="orca-weekday"><input type="checkbox" checked><span aria-hidden="true">W</span><span class="orca-sr-only">Wednesday</span></label><label class="orca-weekday"><input type="checkbox" checked><span aria-hidden="true">T</span><span class="orca-sr-only">Thursday</span></label><label class="orca-weekday"><input type="checkbox" checked><span aria-hidden="true">F</span><span class="orca-sr-only">Friday</span></label><label class="orca-weekday"><input type="checkbox"><span aria-hidden="true">S</span><span class="orca-sr-only">Saturday</span></label><label class="orca-weekday"><input type="checkbox"><span aria-hidden="true">S</span><span class="orca-sr-only">Sunday</span></label>
</fieldset>""")],
    guide=["Weekday toggle"], source="ORCA",
))

add(Element(
    "recurrence-select", "Recurrence select", INP,
    "A select of common repeat rules with a 'Custom…' option that reveals more fields.",
    why="Most repeats are a few common rules; listing them keeps the choice quick (Hick's law) and reveals the full "
        "rule editor only when needed (Practical UI S04, Tesler's law).",
    when=["Repeating events, reports, capture runs."],
    how=["Options: Does not repeat · Daily · Every weekday (Mon–Fri) · Weekly on {day} · Monthly on day {n} · Yearly on {date} · Custom…",
         "Write options with the actual day from the chosen date ('Weekly on Thursday').",
         "Choosing Custom… reveals the weekday toggle and interval fields."],
    classes=[".orca-select"],
    laws=["hick", "S04", "tesler"],
    examples=[("Recurrence", """<label class="orca-label" for="rec">Repeat</label>
<select class="orca-select" id="rec" style="max-width: 20rem">
  <option value="">Does not repeat</option><option>Daily</option><option selected>Every weekday (Monday to Friday)</option>
  <option>Weekly on Thursday</option><option>Monthly on day 6</option><option>Yearly on 6 November</option><option value="custom">Custom…</option>
</select>""")],
    guide=["Recurrence select"], source="ORCA",
))

add(Element(
    "reminder-select", "Reminder select", INP,
    "A select of reminder offsets before an event.",
    why="A short list of standard offsets is faster than typing a duration (Hick's law) and matches calendar apps people know (Jakob's law).",
    when=["Event and deadline reminders."],
    how=["Options: No reminder · At time of event · 5, 10, 15, 30 minutes before · 1 hour before · 1 day before · Custom…",
         "Default to the user's last choice (Tesler's law). Several reminders: repeat the select with an Add reminder link."],
    classes=[".orca-select"],
    laws=["hick", "jakob", "tesler"],
    examples=[("Reminder", """<label class="orca-label" for="rem">Remind me</label>
<select class="orca-select" id="rem" style="max-width: 16rem">
  <option>No reminder</option><option>At time of event</option><option>5 minutes before</option><option selected>15 minutes before</option>
  <option>1 hour before</option><option>1 day before</option><option value="custom">Custom…</option>
</select>""")],
    guide=["Reminder select"], source="ORCA",
))

# ------------------------------------------------------------------ text


def _txt(eid, name, summary, why, when, how, example, guide, classes, laws=("postel",), avoid=()):
    add(Element(eid, name, TXT, summary, why=why, when=when, how=list(how) + [TIME], avoid=list(avoid),
                a11y=["Wrap in `<time datetime=\"…\">` with the ISO value so assistive technology and scripts get the exact moment."],
                classes=classes, laws=list(laws), examples=[("Example", example)], guide=[guide], source="ORCA"))


_txt("day-number", "Day number", "The day of the month in a calendar cell or date badge.",
     "Tabular digits keep calendar columns aligned and scannable (Practical UI W11).",
     ["Calendar cells, mini calendars, date badges."],
     ["`<time class=\"orca-day-number\" datetime=\"2026-11-06\">{{ day|date:\"j\" }}</time>` (no leading zero)."],
     """<time class="orca-day-number" datetime="2026-11-06">6</time>""", "Day number", [".orca-day-number"], ("W11",))
_txt("weekday-name", "Weekday name", "The day of the week as a short uppercase label or a full word.",
     "Short uppercase labels head calendar columns without crowding them (Practical UI W07: uppercase only for short labels).",
     ["Calendar column headers (short: MON), agenda rows and date labels (full: Monday)."],
     ["Header: `<abbr class=\"orca-weekday-name\" title=\"Monday\">{{ d|date:\"D\" }}</abbr>`.", "Full: `{{ d|date:\"l\" }}`."],
     """<div class="orca-row orca-row--16"><abbr class="orca-weekday-name" title="Monday">Mon</abbr><abbr class="orca-weekday-name" title="Tuesday">Tue</abbr><span>Friday</span></div>""",
     "Weekday name", [".orca-weekday-name"], ("W07",))
_txt("month-name", "Month name", "The month (and year) heading a calendar or a group of agenda items.",
     "A clear month heading orients people in time before they scan days (Miller's law).",
     ["Calendar headers, month separators in agendas and timelines."],
     ["`<h2 class=\"orca-month-name\"><time datetime=\"2026-11\">{{ d|date:\"F\" }}</time> <span class=\"orca-year\">{{ d|date:\"Y\" }}</span></h2>`.",
      "Omit the year when it is the current year and context is clear."],
     """<h2 class="orca-month-name"><time datetime="2026-11">November</time> <span class="orca-year">2026</span></h2>""",
     "Month name", [".orca-month-name"], ("miller",))
_txt("year-label", "Year label", "The year, muted, beside a month or in a year view.",
     "The year is context, not content: muting it keeps the month as the focus (Practical UI L03).",
     ["Beside month names; year view headings; date labels outside the current year."],
     ["`<span class=\"orca-year\">2026</span>`; full-strength as a year-view heading."],
     """<span class="orca-year">2026</span>""", "Year label", [".orca-year"], ("L03",))
_txt("week-number", "Week number", "The ISO week number, labelled.",
     "Many teams plan in weeks; showing the number avoids mental calendar arithmetic (Tesler's law).",
     ["Left column of month views, week view headers, sprint labels."],
     ["`<span class=\"orca-week-number\" title=\"Week 45\">W45</span>` with `{{ d|date:\"W\" }}`.", "Only show where the audience uses week numbers."],
     """<span class="orca-week-number" title="Week 45">W45</span>""", "Week number", [".orca-week-number"], ("tesler",))
_txt("time-label", "Time label", "A clock time in the reader's 12- or 24-hour convention.",
     "Times must read in the convention people use, and stay aligned in columns (Postel's law, W11).",
     ["Event times, hour labels, log entries."],
     ["`<time class=\"orca-time\" datetime=\"2026-11-06T08:30\">{{ t|time:\"TIME_FORMAT\" }}</time>`.",
      "Ranges: '08:30–10:00' with an en dash, no spaces; across days include both dates."],
     """<time class="orca-time" datetime="2026-11-06T08:30">08:30</time>–<time class="orca-time" datetime="2026-11-06T10:00">10:00</time>""",
     "Time label", [".orca-time"], ("postel", "W11"))
_txt("date-label", "Date label", "A date written for people: '6 November 2026', 'Fri 6 Nov'.",
     "Written months avoid the 06/11 vs 11/06 ambiguity across countries (Postel's law).",
     ["Anywhere a date is shown to people."],
     ["`<time class=\"orca-date\" datetime=\"2026-11-06\">{{ d|date:\"j F Y\" }}</time>`; short form `{{ d|date:\"D j M\" }}` in dense tables.",
      "Never show numeric-only dates (06/11/2026) to mixed audiences."],
     """<time class="orca-date" datetime="2026-11-06">6 November 2026</time> · <time class="orca-date" datetime="2026-11-06">Fri 6 Nov</time>""",
     "Date label", [".orca-date"], ("postel",))
_txt("relative-time", "Relative time label", "'2 minutes ago', 'in 3 days', with the exact time on hover and for screen readers.",
     "Recent events are judged by how long ago they happened; the exact time stays available (Postel's law).",
     ["Activity feeds, 'last seen', 'updated' stamps up to about a week old."],
     ["`<time class=\"orca-relative-time\" datetime=\"2026-11-06T08:14\" title=\"6 November 2026, 08:14\">{{ t|naturaltime }}</time>` (`django.contrib.humanize`).",
      "Switch to an absolute date after 7 days."],
     """<time class="orca-relative-time" datetime="2026-11-06T08:14" title="6 November 2026, 08:14">2 minutes ago</time>""",
     "Relative time label", [".orca-relative-time"], ("postel",), avoid=["Logs and audit trails: use absolute times."])
_txt("timezone-label", "Timezone label", "A small outlined abbreviation of the timezone, with the full zone in its title.",
     "When people and places are in different zones, an explicit label prevents missed meetings (Postel's law, Tesler's law).",
     ["Beside times whose zone may differ from the reader's: site schedules, shared events."],
     ["`<abbr class=\"orca-tz\" title=\"Europe/Paris (UTC+01:00)\">CET</abbr>` using `{{ t|date:\"T\" }}`.", "Hide it when every time on the page is in the reader's zone."],
     """<span class="orca-time">08:30</span> <abbr class="orca-tz" title="Europe/Paris (UTC+01:00)">CET</abbr>""",
     "Timezone label", [".orca-tz"], ("postel", "tesler"))
_txt("duration-label", "Duration label", "A length of time: '45 min', '1 h 30 min', '3 d'.",
     "Short, consistent units are scanned faster than '90 minutes' or '1.5h' (Practical UI W11).",
     ["Event lengths, dwell times, durations in tables."],
     ["`<span class=\"orca-duration-label\">{{ minutes|orca_duration }}</span>`; machine value in `<time datetime=\"PT1H30M\">` where useful."],
     """<time class="orca-duration-label" datetime="PT1H30M">1 h 30 min</time>""", "Duration label", [".orca-duration-label"], ("W11",))
_txt("countdown-label", "Countdown label", "Time left until a moment, updating live.",
     "A visible countdown makes a deadline concrete and turns urgent in the final minute (Von Restorff), without "
     "announcing every second to screen readers.",
     ["Session expiry, booking holds, run start."],
     ["`<time class=\"orca-countdown\" datetime=\"2026-11-06T09:00:00Z\" data-orca-countdown role=\"timer\">15:00</time>` (orca.js updates it).",
      "Render the initial value on the server so it reads correctly without script."],
     """<time class="orca-countdown" datetime="2030-01-01T00:00:00Z" data-orca-countdown role="timer" aria-label="Time left">–:–</time>""",
     "Countdown label", [".orca-countdown", ".orca-countdown--urgent"], ("restorff", "doherty"))

# ------------------------------------------------------------------ marks


def _mark(eid, name, summary, why, when, how, example, guide, classes, tokens=(), laws=("C03",), avoid=(), a11y=()):
    add(Element(eid, name, MRK, summary, why=why, when=when, how=how, avoid=list(avoid), a11y=list(a11y),
                classes=classes, tokens=list(tokens), laws=list(laws), examples=[("Example", example)], guide=[guide], source="ORCA"))


_mark("today-marker", "Today marker", "Today's day number outlined in red, bold.",
      "People orient on 'now' first in any calendar (Von Restorff); outline plus weight works without colour (C03).",
      ["Today in month grids, mini calendars, date pickers."],
      ["`<button class=\"orca-day\" aria-current=\"date\">6</button>` (or `.orca-day--today`).", "Only one per view."],
      """<button class="orca-day" type="button" aria-current="date" aria-label="6 November, today">6</button>""",
      "Today marker", [".orca-day", ".orca-day--today"], ["today"], ("restorff", "C03"),
      a11y=["`aria-current=\"date\"` announces 'current date'."])
_mark("selected-day-marker", "Selected-day marker", "The chosen day filled with the accent colour.",
      "Selection uses the system's 'on' colour and a fill (shape change), consistent with ticks and radios (Practical UI F09).",
      ["The chosen day or the ends of a chosen range."],
      ["`<button class=\"orca-day\" aria-pressed=\"true\">` in pickers, `aria-selected=\"true\"` in grids."],
      """<button class="orca-day" type="button" aria-pressed="true" aria-label="12 November, selected">12</button>""",
      "Selected-day marker", [".orca-day--selected"], ["accent"], ("F09", "C03"))
_mark("outside-day-marker", "Out-of-month day marker", "Days of the previous or next month shown muted.",
      "Muting days outside the month keeps full weeks visible while keeping focus on the month (Practical UI L03).",
      ["Leading and trailing days of a month grid."],
      ["Add `.orca-day--outside`; they stay clickable and navigate to their month."],
      """<button class="orca-day orca-day--outside" type="button" aria-label="31 October">31</button>""",
      "Out-of-month day marker", [".orca-day--outside"], ["text-muted"], ("L03",))
_mark("weekend-marker", "Weekend marker", "A faint tint behind weekend days and columns.",
      "A subtle tint separates working days without competing with events (Miller's law: chunking the week).",
      ["Month grids, week views, Gantt columns."],
      ["`.orca-day--weekend` on days; `background: var(--orca-weekend-bg)` on columns. Weekend days follow the locale."],
      """<div class="orca-row" style="gap: 0"><button class="orca-day" type="button">6</button><button class="orca-day orca-day--weekend" type="button">7</button><button class="orca-day orca-day--weekend" type="button">8</button></div>""",
      "Weekend marker", [".orca-day--weekend"], ["weekend-bg"], ("miller",))
_mark("holiday-marker", "Holiday marker", "A purple tint and underline mark on holidays and closed days, with the holiday's name.",
      "Closed days change plans; tint plus a mark plus the name make them noticed and understood (C03).",
      ["Public holidays, site closures, exceptions."],
      ["`.orca-day--holiday` with `title` and an `aria-label` that include the holiday name.", "List the name in the day cell or agenda (holiday label component)."],
      """<button class="orca-day orca-day--holiday" type="button" title="Armistice Day" aria-label="11 November, Armistice Day, closed">11</button>""",
      "Holiday marker", [".orca-day--holiday"], ["holiday-bg", "purple"], ("C03",))
_mark("event-dot", "Event dot", "A small dot that says 'there are events here' or keys an event's calendar.",
      "In small cells a dot shows presence without text (Miller's law); the count or list must be one tap away.",
      ["Mini calendars (day has events), agenda rows (calendar colour)."],
      ["`<span class=\"orca-event-dot\" style=\"--orca-event: var(--orca-chart-3)\"></span>`; on a day: `.orca-day--has-events` and say 'has events' in its label."],
      """<div class="orca-row"><span class="orca-with-icon"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-3)"></span>Maintenance</span><button class="orca-day orca-day--has-events" type="button" aria-label="14 November, has events">14</button></div>""",
      "Event dot", [".orca-event-dot", ".orca-day--has-events"], ["chart-3"], ("miller",))
_mark("event-bar", "Event bar", "A timed event in a day: tinted bar with a 3px leading edge in the calendar colour.",
      "The coloured edge keys the calendar while the light tint keeps the title readable (C01); tentative events are "
      "hatched and cancelled ones struck through, so status never relies on colour (C03).",
      ["Events in month cells and week/day columns."],
      ["`<div class=\"orca-event-bar\" style=\"--orca-event: var(--orca-chart-1)\"><time>08:30</time> Delivery</div>`.",
       "States: `--tentative` (hatched), `--cancelled` (struck through, muted). Long titles truncate; full title in `title`."],
      """<div class="orca-stack" style="max-width: 14rem; gap: 2px">
  <div class="orca-event-bar" style="--orca-event: var(--orca-chart-1)"><time class="orca-time" datetime="08:30">08:30</time> Delivery window</div>
  <div class="orca-event-bar orca-event-bar--tentative" style="--orca-event: var(--orca-chart-2)"><time class="orca-time" datetime="10:00">10:00</time> Audit (tentative)</div>
  <div class="orca-event-bar orca-event-bar--cancelled" style="--orca-event: var(--orca-chart-4)"><time class="orca-time" datetime="14:00">14:00</time> Training</div>
</div>""",
      "Event bar", [".orca-event-bar", ".orca-event-bar--tentative", ".orca-event-bar--cancelled"], ["chart-1"], ("C01", "C03"))
_mark("allday-bar", "All-day bar", "A solid bar for all-day and multi-day events, with arrow ends when it continues.",
      "Solid fill separates all-day events from timed ones at a glance (Von Restorff); arrow ends show continuation without words (Jakob's law: familiar from calendars).",
      ["All-day rows of week views; multi-day events in month grids."],
      ["`<div class=\"orca-allday-bar\" style=\"--orca-event: var(--orca-chart-1)\">Trade fair</div>`; add `--continues-before` / `--continues-after` at the edges of the visible range."],
      """<div class="orca-stack" style="max-width: 18rem; gap: 2px"><div class="orca-allday-bar" style="--orca-event: var(--orca-chart-1)">Inventory day</div><div class="orca-allday-bar orca-allday-bar--continues-after" style="--orca-event: var(--orca-chart-4)">Trade fair, 6–9 November</div></div>""",
      "All-day bar", [".orca-allday-bar", ".orca-allday-bar--continues-before", ".orca-allday-bar--continues-after"], ["chart-1"], ("restorff", "jakob"))
_mark("hour-gridline", "Hour gridline", "Hour and half-hour lines with the hour label in the gutter.",
      "Faint gridlines give scale to a day without competing with events (Practical UI S02).",
      ["Day and week views, resource schedulers."],
      ["`<div class=\"orca-hour-line\"><span class=\"orca-hour-line__label\">09:00</span></div>` every hour; `--half` (dashed) for half hours."],
      """<div style="position: relative; max-width: 18rem; padding-top: 0.75rem"><div class="orca-hour-line"><span class="orca-hour-line__label">09:00</span></div><div style="height: 1.5rem"></div><div class="orca-hour-line orca-hour-line--half"></div><div style="height: 1.5rem"></div><div class="orca-hour-line"><span class="orca-hour-line__label">10:00</span></div></div>""",
      "Hour gridline", [".orca-hour-line", ".orca-hour-line--half", ".orca-hour-line__label"], ["gridline"], ("S02",))
_mark("now-indicator", "Now indicator", "A red line with a dot at the current time across day and week views.",
      "The present moment is the anchor of any schedule (Von Restorff); the line plus dot shape reads without colour.",
      ["Day and week views, timelines, Gantt charts (vertical)."],
      ["`<div class=\"orca-now-line\" style=\"top: …\" aria-hidden=\"true\"></div>` positioned by script; update every minute."],
      """<div style="padding: var(--orca-space-8) var(--orca-space-16); max-width: 18rem"><div class="orca-now-line" aria-hidden="true"></div></div>""",
      "Now indicator", [".orca-now-line"], ["today"], ("restorff",))
_mark("availability-color", "Availability colour (free, busy, tentative)", "Free, busy, tentative and off states as filled, solid, hatched and dashed marks.",
      "Availability is compared across many slots; four distinct patterns (not just four colours) keep it readable for everyone (C03, Miller's law).",
      ["Availability legends, booking slots, resource schedulers, people pickers."],
      ["Legend item: `<span class=\"orca-avail orca-avail--free\">Free</span>`; `--busy`, `--tentative`, `--off`.",
       "Fill a slot: `.orca-avail-fill--free`, `--busy`, `--tentative` on the slot element, with the state in its label."],
      """<div class="orca-row orca-row--16"><span class="orca-avail orca-avail--free">Free</span><span class="orca-avail orca-avail--busy">Busy</span><span class="orca-avail orca-avail--tentative">Tentative</span><span class="orca-avail orca-avail--off">Not working</span></div>""",
      "Availability colour (free, busy, tentative)", [".orca-avail", ".orca-avail--free", ".orca-avail--busy", ".orca-avail--tentative", ".orca-avail-fill--free"],
      ["positive", "neutral-fill", "caution"], ("C03", "miller"))
_mark("priority-marker", "Priority marker", "Signal bars plus a word: low, medium, high, urgent.",
      "Bars rise with priority so the order is visible in greyscale (C03); the word removes doubt.",
      ["Tasks, tickets, alerts in lists and boards."],
      ["`<span class=\"orca-priority orca-priority--high\"><span class=\"orca-priority__bars\" aria-hidden=\"true\"><i></i><i></i><i></i></span>High</span>`."],
      """<div class="orca-row orca-row--16">
  <span class="orca-priority orca-priority--low"><span class="orca-priority__bars" aria-hidden="true"><i></i><i></i><i></i></span>Low</span>
  <span class="orca-priority orca-priority--medium"><span class="orca-priority__bars" aria-hidden="true"><i></i><i></i><i></i></span>Medium</span>
  <span class="orca-priority orca-priority--high"><span class="orca-priority__bars" aria-hidden="true"><i></i><i></i><i></i></span>High</span>
  <span class="orca-priority orca-priority--urgent"><span class="orca-priority__bars" aria-hidden="true"><i></i><i></i><i></i></span>Urgent</span>
</div>""",
      "Priority marker", [".orca-priority", ".orca-priority--low", ".orca-priority--medium", ".orca-priority--high", ".orca-priority--urgent"],
      ["caution", "negative"], ("C03", "restorff"))
_mark("deadline-marker", "Deadline marker", "A flag icon with the due date; a caution flag when it is close.",
      "A due date with a flag is found by scanning (Von Restorff); turning the icon amber when close prevents a negative peak (Peak–end rule).",
      ["Tasks, plans, Gantt bars (`.orca-deadline-line` as a vertical rule)."],
      ["`<span class=\"orca-deadline\">{% icon \"flag\" %}<span>Due <time datetime=…>Fri 13 Nov</time></span></span>`; add `--soon` within 2 days."],
      """<div class="orca-row orca-row--16"><span class="orca-deadline">{% icon "flag" %}<span>Due <time datetime="2026-11-20">Fri 20 Nov</time></span></span><span class="orca-deadline orca-deadline--soon">{% icon "flag" %}<span>Due tomorrow</span></span></div>""",
      "Deadline marker", [".orca-deadline", ".orca-deadline--soon", ".orca-deadline-line"], ["caution"], ("restorff", "peak-end"))
_mark("overdue-marker", "Overdue marker", "Bold red text with the error glyph and how late it is.",
      "Overdue items need action now; red, bold, a glyph and the word 'Overdue' together are unmistakable (C03, C04).",
      ["Tasks and deadlines past due."],
      ["`<span class=\"orca-overdue\">{% icon \"error\" %}Overdue by 2 days</span>`.", "Say by how much; never only 'Late'."],
      """<span class="orca-overdue">{% icon "error" %}Overdue by 2 days</span>""",
      "Overdue marker", [".orca-overdue"], ["negative"], ("C03", "C04"))
_mark("milestone-marker", "Milestone marker", "A diamond: filled (reached), outlined (upcoming), red outline (missed), green (done).",
      "The diamond is the convention for milestones in plans and Gantt charts (Jakob's law); fill versus outline shows state without colour.",
      ["Roadmaps, Gantt charts, milestone timelines."],
      ["`<span class=\"orca-milestone orca-milestone--upcoming\" aria-hidden=\"true\"></span>` before the milestone name; states `--done`, `--missed`, `--upcoming`, default (reached).",
       "Write the state in text too."],
      """<div class="orca-stack"><span class="orca-with-icon"><span class="orca-milestone orca-milestone--done" aria-hidden="true"></span>Pilot live · done</span><span class="orca-with-icon"><span class="orca-milestone orca-milestone--upcoming" aria-hidden="true"></span>All sites live · 1 Dec</span><span class="orca-with-icon"><span class="orca-milestone orca-milestone--missed" aria-hidden="true"></span>Training complete · missed</span></div>""",
      "Milestone marker", [".orca-milestone", ".orca-milestone--done", ".orca-milestone--missed", ".orca-milestone--upcoming"], ["positive", "negative"], ("jakob", "C03"))
_mark("drag-handle", "Drag handle", "A grip button for moving an item, usable by keyboard too.",
      "A visible grip tells people the item can be moved (affordance, Jakob's law); a keyboard alternative keeps it usable for everyone (Postel's law).",
      ["Reorderable rows, schedule rows, board cards, events in a week view."],
      ["`<button class=\"orca-drag-handle\" type=\"button\" aria-label=\"Move Entrance A\" aria-describedby=\"drag-help\">{% icon \"drag\" %}</button>`.",
       "Keyboard: Space picks up (`aria-pressed=\"true\"`), arrows move, Space drops, Escape cancels; announce moves in a live region.",
       "While dragging add `.orca-is-dragging` to the item (lifted shadow)."],
      """<div class="orca-row" style="max-width: 20rem; padding: var(--orca-space-4); border: var(--orca-border-width) solid var(--orca-border)"><button class="orca-drag-handle" type="button" aria-label="Move Entrance A">{% icon "drag" %}</button>Entrance A</div>""",
      "Drag handle", [".orca-drag-handle", ".orca-is-dragging"], ["text-muted", "shadow-dragged"], ("jakob", "postel", "fitts"),
      a11y=["Always provide a non-drag way (move up/down buttons or the keyboard flow)."])
_mark("resize-handle", "Resize handle", "A grip on the edge of an event or panel that changes its length.",
      "A visible grip on the edge shows the item can be stretched (affordance); a precise field elsewhere remains the accessible way (Postel's law).",
      ["Bottom edge of events in day/week views; edges of Gantt bars (`--x`)."],
      ["`<button class=\"orca-resize-handle\" type=\"button\" aria-label=\"Change end time of Delivery\">` at the bottom edge; `.orca-resize-handle--x` for horizontal.",
       "Snap to 15 minutes; show the new time while resizing."],
      """<div style="max-width: 12rem"><div class="orca-event-bar" style="--orca-event: var(--orca-chart-1); min-height: 3rem; align-items: flex-start; padding-top: var(--orca-space-4)">Delivery</div><button class="orca-resize-handle" type="button" aria-label="Change end time of Delivery"></button></div>""",
      "Resize handle", [".orca-resize-handle", ".orca-resize-handle--x"], ["text-muted"], ("postel", "fitts"))

# ------------------------------------------------------------------ icons
PLANNING_GLYPHS = ["calendar", "clock", "repeat", "notifications", "alarm", "timer", "hourglass", "flag", "pin", "calendar-plus", "today"]

add(Element(
    "planning-icons", "Planning icons", ICN,
    "calendar, clock, repeat, bell (notifications), alarm, timer, hourglass, flag, pin, calendar-plus, today.",
    why="Planning UI repeats a few ideas everywhere (date, time, repeat, reminder); one consistent glyph per idea makes them "
        "recognisable across screens (Jakob's law, Practical UI F09).",
    when=["calendar: date fields and date navigation · clock: times and durations · repeat: recurring items · "
          "bell/alarm: reminders · timer/hourglass: countdowns and waits · flag: deadlines · pin: pinned dates · "
          "calendar-plus: add event · today: jump to today."],
    avoid=["Using a planning icon without its word, except in icon buttons with an aria-label."],
    how=["`{% icon \"calendar\" %}` etc. Aliases: `bell` → notifications, `date-pin` → pin, `calendar-today` → today.",
         "'Today' buttons should show the word 'Today'; the icon is optional."],
    classes=[".orca-icon"],
    laws=["jakob", "F09", "hick"],
    examples=[("Planning glyphs", "<div class=\"orca-row orca-row--16\">\n  "
               + "".join(f'<span class="orca-with-icon">{{% icon "{g}" %}}<span class="orca-small">{g}</span></span>' for g in PLANNING_GLYPHS)
               + "\n</div>")],
    guide=["Calendar", "Clock", "Repeat", "Bell (reminder)", "Alarm", "Timer", "Hourglass", "Flag", "Pin (date)", "Calendar-plus", "Today (jump to today)"],
    related=["icon-set"], source="ORCA",
))
