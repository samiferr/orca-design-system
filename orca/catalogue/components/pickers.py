from ..registry import add, category
from . import Component

C = category(
    "pickers", "Date and time pickers",
    "Native date and time inputs, composed with shortcuts, ranges, time zones and a month grid. Native first: every device already knows how to pick a date.",
    level="component",
)

add(Component(
    "date-picker", "Date picker", C,
    "A labelled native date input with shortcut buttons for the most common dates.",
    why="The native picker is familiar and accessible on every device (Jakob's law); one-tap shortcuts for the dates people choose most remove the picker entirely in common cases (Tesler's law, Fitts's law).",
    when=["Choosing one date near today: a report date, a due date, a start date."],
    avoid=["Dates far in the past people know by heart: use the split date input."],
    how=["`.orca-field` with label, help and `<input class=\"orca-input\" type=\"date\">`, then `.orca-shortcuts` of tags `<button class=\"orca-tag\" type=\"button\" aria-pressed=\"false\" data-orca-set-date=\"0\" aria-controls=\"input-id\">Today</button>` (+1 Tomorrow, +7 In a week).",
         "Set `min`/`max` and say the allowed range in the help text.",
         "Django: `{% templatetag openblock %} orca_field form.due {% templatetag closeblock %}` renders a DateField as a native date input."],
    classes=[".orca-field", ".orca-shortcuts"],
    laws=["jakob", "tesler", "fitts"],
    uses=["date-input", "tag", "help-text"],
    examples=[("Due date", """<div class="orca-field" style="max-width: 20rem">
  <label class="orca-label" for="dp-1">Due date</label>
  <input class="orca-input" type="date" id="dp-1" name="due">
  <div class="orca-shortcuts" role="group" aria-label="Quick dates"><button class="orca-tag" type="button" aria-pressed="false" data-orca-set-date="0" aria-controls="dp-1">Today</button><button class="orca-tag" type="button" aria-pressed="false" data-orca-set-date="1" aria-controls="dp-1">Tomorrow</button><button class="orca-tag" type="button" aria-pressed="false" data-orca-set-date="7" aria-controls="dp-1">In a week</button></div>
</div>""")],
    guide=["Date picker"],
    related=["mini-calendar", "date-range-picker"],
))

add(Component(
    "time-picker", "Time picker", C,
    "A labelled native time input with a step and its timezone.",
    why="Native time fields follow the reader's 12/24-hour habit (Postel's law); a step of 15 minutes matches how people plan and removes fiddly values.",
    when=["Start times, reminder times, opening hours."],
    how=["`.orca-field` > label + `.orca-row` containing `<input class=\"orca-input\" type=\"time\" step=\"900\">` and a timezone label.",
         "Omit the timezone label when every time on the page is in the reader's zone."],
    classes=[".orca-field"],
    laws=["postel", "jakob"],
    uses=["time-input", "timezone-label"],
    examples=[("Opening time", """<div class="orca-field" style="max-width: 20rem"><label class="orca-label" for="tp-1">Opens at</label><div class="orca-row"><input class="orca-input" type="time" id="tp-1" value="08:30" step="900" style="max-width: 9rem"><abbr class="orca-tz" title="Europe/Paris (UTC+01:00)">CET</abbr></div></div>""")],
    guide=["Time picker"],
))

add(Component(
    "datetime-picker", "Date-time picker", C,
    "A date and a time as two labelled fields in one group, with the timezone.",
    why="Two separate native fields are easier to fill and correct than one combined control, and they work the same in every browser (Postel's law).",
    when=["One moment: when a run starts, when access expires."],
    how=["`<fieldset class=\"orca-inline-fields\">` with a legend, a date field and a time field (`.orca-field`), and a timezone label.",
         "Combine on the server in the site's timezone; store UTC."],
    classes=[".orca-inline-fields"],
    laws=["postel", "tesler"],
    uses=["date-input", "time-input", "timezone-label"],
    examples=[("Run start", """<fieldset class="orca-inline-fields"><legend class="orca-label">Start the run</legend>
  <div class="orca-field"><label class="orca-label" for="dtp-d">Date</label><input class="orca-input" type="date" id="dtp-d" value="2026-11-07"></div>
  <div class="orca-field"><label class="orca-label" for="dtp-t">Time</label><input class="orca-input" type="time" id="dtp-t" value="07:00" step="900"></div>
  <abbr class="orca-tz orca-inline-fields__sep" title="Europe/Paris">CET</abbr>
</fieldset>""")],
    guide=["Date-time picker"],
))

add(Component(
    "date-range-picker", "Date-range picker", C,
    "Start and end dates with presets, kept in order, and the length in days.",
    why="Most ranges are standard periods; presets choose them in one tap (Hick's law) and keeping the end after the start prevents an impossible range (Postel's law). Showing the length confirms the choice.",
    when=["Report periods, time off, exceptions, filters."],
    how=["`<fieldset class=\"orca-inline-fields\" data-orca-range>` with a legend, a From date field, a To date field and `<p class=\"orca-inline-fields__note\" data-orca-range-output aria-live=\"polite\">`.",
         "Presets: a preset-buttons row above it (Today, This week, Last 7 days, This month).",
         "orca.js sets the end field's `min` to the start and moves the end when needed."],
    classes=[".orca-inline-fields", ".orca-inline-fields__note"],
    laws=["hick", "postel", "doherty"],
    uses=["date-input", "preset-buttons"],
    examples=[("Report period", """<fieldset class="orca-inline-fields" data-orca-range><legend class="orca-label">Report period</legend>
  <div class="orca-field"><label class="orca-label" for="dr-a">From</label><input class="orca-input" type="date" id="dr-a" value="2026-11-02"></div>
  <span class="orca-inline-fields__sep" aria-hidden="true">–</span>
  <div class="orca-field"><label class="orca-label" for="dr-b">To</label><input class="orca-input" type="date" id="dr-b" value="2026-11-08"></div>
  <p class="orca-inline-fields__note" data-orca-range-output aria-live="polite">7 days</p>
</fieldset>""")],
    guide=["Date-range picker"],
))

add(Component(
    "time-range-input", "Time-range input (start and end)", C,
    "Start and end times with the resulting duration, saying when it ends the next day.",
    why="People check a time range by its length; computing it live catches typos (Doherty threshold), and saying 'ends the next day' makes overnight shifts explicit instead of an error (Postel's law).",
    when=["Opening hours, shifts, booking windows."],
    how=["`<fieldset class=\"orca-inline-fields\" data-orca-range>` with Start and End time fields and an `orca-inline-fields__note` output.",
         "Validate on the server too; decide whether overnight ranges are allowed and say so."],
    classes=[".orca-inline-fields"],
    laws=["doherty", "postel"],
    uses=["time-input", "duration-label"],
    examples=[("Shift", """<fieldset class="orca-inline-fields" data-orca-range><legend class="orca-label">Shift</legend>
  <div class="orca-field"><label class="orca-label" for="trg-a">Start</label><input class="orca-input" type="time" id="trg-a" value="22:00" step="900"></div>
  <span class="orca-inline-fields__sep" aria-hidden="true">–</span>
  <div class="orca-field"><label class="orca-label" for="trg-b">End</label><input class="orca-input" type="time" id="trg-b" value="06:00" step="900"></div>
  <p class="orca-inline-fields__note" data-orca-range-output aria-live="polite">8 h, ends the next day</p>
</fieldset>""")],
    guide=["Time-range input (start and end)"],
))

add(Component(
    "duration-picker", "Duration picker", C,
    "Hours and minutes fields with quick choices for common durations.",
    why="Common durations in one tap (Hick's law) plus exact fields for the rest; parts with units remove format guessing (Postel's law, Practical UI R13).",
    when=["Meeting lengths, retention, timeouts, reminder offsets."],
    how=["`.orca-field` containing a duration input (two parts with addons) and `.orca-shortcuts` tags (15 min, 30 min, 1 h).",
         "Shortcuts set both parts with a small script or a server round-trip; normalise minutes over 59 on the server."],
    classes=[".orca-shortcuts"],
    laws=["hick", "postel", "R13"],
    uses=["duration-input", "tag"],
    examples=[("Meeting length", """<div class="orca-field"><fieldset class="orca-duration" style="border: 0; padding: 0; margin: 0"><legend class="orca-label">Length</legend>
  <span class="orca-duration__part"><input class="orca-input" type="number" min="0" value="0" aria-label="Hours"><span class="orca-addon">h</span></span>
  <span class="orca-duration__part"><input class="orca-input" type="number" min="0" step="5" value="30" aria-label="Minutes"><span class="orca-addon">min</span></span></fieldset>
  <div class="orca-shortcuts" role="group" aria-label="Common lengths"><button class="orca-tag" type="button" aria-pressed="false">15 min</button><button class="orca-tag" type="button" aria-pressed="true">30 min</button><button class="orca-tag" type="button" aria-pressed="false">1 h</button></div></div>""")],
    guide=["Duration picker"],
))

add(Component(
    "timezone-selector", "Timezone selector", C,
    "A timezone select with a 'Use my timezone' button and the current offset.",
    why="Detecting the zone moves the complexity to the system (Tesler's law); keeping the full list lets people choose a site's zone that differs from theirs (Postel's law).",
    when=["Site, video and profile settings."],
    how=["`.orca-field` with label, help showing the current local time, a `.orca-row` with `<select class=\"orca-select\">{% templatetag openblock %} orca_timezone_options current {% templatetag closeblock %}</select>` and a ghost button `data-orca-detect-tz aria-controls=\"select-id\"`.",
         "Store the IANA name."],
    classes=[".orca-field"],
    laws=["tesler", "postel"],
    uses=["timezone-select", "button"],
    examples=[("Site timezone", """<div class="orca-field" style="max-width: 30rem"><label class="orca-label" for="tzs">Site timezone</label><p class="orca-help" id="tzs-help">Reports and schedules use this zone.</p>
  <div class="orca-row" style="flex-wrap: nowrap"><select class="orca-select" id="tzs" aria-describedby="tzs-help">{% orca_timezone_options "Europe/Paris" %}</select><button class="orca-button orca-button--ghost" type="button" data-orca-detect-tz aria-controls="tzs">Use my timezone</button></div></div>""")],
    guide=["Timezone selector"], source="Tangerine",
))

add(Component(
    "month-year-switcher", "Month and year switcher", C,
    "Previous and next buttons around a month select and a year select.",
    why="Arrows serve small moves; selects jump far without many clicks (Fitts's law, Hick's law).",
    when=["Calendars and reports navigated by month, especially far from today."],
    how=["`<div class=\"orca-month-switcher\" role=\"group\" aria-label=\"Month\">` with a previous icon button, a month select, a year select and a next icon button.",
         "Server-rendered: a GET form with `data-orca-autosubmit` on the selects and links for the arrows."],
    classes=[".orca-month-switcher"],
    laws=["fitts", "hick"],
    uses=["icon-button", "select", "month-name", "year-label"],
    examples=[("Switcher", """<form class="orca-month-switcher" role="group" aria-label="Month" onsubmit="return false">
  <a class="orca-icon-button" href="#" aria-label="Previous month, October 2026">{% icon "chevron-left" %}</a>
  <select class="orca-select orca-select--dense" aria-label="Month"><option>October</option><option selected>November</option><option>December</option></select>
  <select class="orca-select orca-select--dense" aria-label="Year"><option>2025</option><option selected>2026</option><option>2027</option></select>
  <a class="orca-icon-button" href="#" aria-label="Next month, December 2026">{% icon "chevron-right" %}</a>
</form>""")],
    guide=["Month and year switcher"],
))

add(Component(
    "mini-calendar", "Mini calendar", C,
    "A server-rendered month grid with today, selected, outside, weekend and holiday days.",
    why="A month grid shows a date in context (weekday, week, neighbours) in the layout everyone knows (Jakob's law); rendering it on the server respects the locale's first weekday without script (Tesler's law).",
    when=["Sidebars of calendars, date filters, showing which days have events."],
    avoid=["Picking one date in a form: the native date input is simpler."],
    how=["`{% templatetag openblock %} orca_mini_calendar month selected=day url=\"/events/?day={date}\" nav_url=\"?month={month}\" events=event_days holidays=holiday_map week_numbers=True {% templatetag closeblock %}`.",
         "Without `url`, days render as buttons with `data-date` for your own script.",
         "Each day's accessible name is the full date plus today, holiday and 'has events' notes."],
    classes=[".orca-mini-calendar", ".orca-mini-calendar__head", ".orca-calendar", ".orca-calendar__week"],
    laws=["jakob", "tesler", "C03"],
    uses=["day-number", "weekday-name", "today-marker", "selected-day-marker", "outside-day-marker", "weekend-marker", "holiday-marker", "event-dot"],
    examples=[("November 2026", """{% orca_mini_calendar "2026-11-01" selected="2026-11-12" today="2026-11-06" url="#{date}" nav_url="#{month}" events="2026-11-04" week_numbers=True %}""")],
    guide=["Mini calendar"], source="Tangerine",
))
