from ..registry import add, category
from . import Pattern

C = category(
    "scheduler", "Scheduler",
    "Editing when things and people are available, and booking time against that availability.",
    level="pattern",
)

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def _span(day, a, b, n):
    return (f'<div class="orca-schedule-row" data-orca-row><input class="orca-input" type="time" value="{a}" aria-label="{day} span {n} opens">'
            f'<span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" value="{b}" aria-label="{day} span {n} closes">'
            f'<button class="orca-icon-button" type="button" aria-label="Remove {day} {a} to {b}" data-orca-remove-row>{{% icon "delete" %}}</button></div>')


def _day(day, spans, open_=True):
    key = day[:3].lower()
    toggle = (f'<label class="orca-switch"><input type="checkbox" role="switch" {"checked" if open_ else ""} aria-label="Open on {day}">'
              f'<span class="orca-switch__track"></span></label>')
    body = ("".join(_span(day, a, b, i + 1) for i, (a, b) in enumerate(spans))
            if open_ else '<span class="orca-week-editor__closed">Closed</span>')
    add_btn = (f'<button class="orca-button orca-button--ghost orca-button--dense" type="button" data-orca-add-row="we-tpl" aria-controls="we-{key}">{{% icon "plus" %}}Add hours</button>'
               if open_ else "")
    return (f'<div class="orca-week-editor__day"><span class="orca-week-editor__name">{toggle} {day}</span>'
            f'<div class="orca-week-editor__spans"><div class="orca-schedule" id="we-{key}">{body}</div>{add_btn}</div></div>')


WEEK = "".join(_day(d, [("08:00", "12:00"), ("13:00", "18:00")] if i < 5 else [("09:00", "13:00")], open_=i < 6) for i, d in enumerate(DAYS))
TPL = ('<template id="we-tpl"><div class="orca-schedule-row" data-orca-row><input class="orca-input" type="time" aria-label="Opens">'
       '<span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" aria-label="Closes">'
       '<button class="orca-icon-button" type="button" aria-label="Remove row" data-orca-remove-row>{% icon "delete" %}</button></div></template>')

add(Pattern(
    "weekly-availability-editor", "Weekly availability editor", C,
    "Each day of the week with an open switch and one or more time spans, to set when something is open or someone is available.",
    why="Availability is naturally weekly with breaks (lunch, split shifts); a row per day with add and remove spans fits that model exactly (Tesler's law). Overlaps and reversed times are flagged on the row, not at the top (Practical UI R21).",
    when=["Opening hours of a site, a person's availability, video recording schedules."],
    avoid=["One-off dates: use the exception and holiday editor."],
    how=["`<div class=\"orca-week-editor\">` with one `.orca-week-editor__day` per weekday: a switch and name, then `.orca-week-editor__spans` holding schedule rows and an 'Add hours' button.",
         "Offer 'Copy Monday to weekdays' when most days are the same; validate on the server (end after start, no overlaps) and show the overlap warning on the row.",
         "Store spans as `(weekday, start, end)` in the site's timezone and show that timezone."],
    classes=[".orca-week-editor", ".orca-week-editor__day", ".orca-week-editor__name", ".orca-week-editor__spans", ".orca-week-editor__closed"],
    laws=["tesler", "R21", "L09"],
    uses=["add-row-button", "switch", "overlap-warning"],
    examples=[("Opening hours", f'<div class="orca-week-editor" style="max-width: 40rem">{WEEK}</div>{TPL}')],
    guide=["Weekly availability editor"],
))

add(Pattern(
    "working-hours-editor", "Working-hours editor", C,
    "A compact editor for regular hours: the working days, one start and end time, a break and the timezone.",
    why="Most people work the same hours every working day; asking for days plus one time range is far quicker than editing seven rows (Hick's law, Tesler's law). The summary sentence confirms the result in words.",
    when=["A person's or team's standard hours; anything where days share the same hours."],
    avoid=["Hours that differ by day: use the weekly availability editor."],
    how=["A form stack with the weekday selector, a time range input, an optional break range and the timezone selector, ending with a summary line ('Monday to Friday, 08:00–17:00, Paris time').",
         "Offer 'Different hours per day' as a link to the weekly editor."],
    classes=[".orca-form-stack"],
    laws=["hick", "tesler"],
    uses=["weekday-selector", "time-range-input", "timezone-selector", "form-stack"],
    examples=[("Working hours", """<form class="orca-form-stack" style="max-width: 30rem" onsubmit="return false">
  <fieldset class="orca-weekday-toggles"><legend class="orca-label">Working days</legend>{% for d in "MTWTFSS" %}<label class="orca-weekday"><input type="checkbox" {% if forloop.counter < 6 %}checked{% endif %}><span aria-hidden="true">{{ d }}</span><span class="orca-sr-only">{% cycle "Monday" "Tuesday" "Wednesday" "Thursday" "Friday" "Saturday" "Sunday" %}</span></label>{% endfor %}</fieldset>
  <fieldset class="orca-inline-fields"><legend class="orca-label">Hours</legend><div class="orca-field"><label class="orca-label" for="wh-a">Start</label><input class="orca-input" type="time" id="wh-a" value="08:00"></div><span class="orca-inline-fields__sep" aria-hidden="true">–</span><div class="orca-field"><label class="orca-label" for="wh-b">End</label><input class="orca-input" type="time" id="wh-b" value="17:00"></div></fieldset>
  <div class="orca-field"><label class="orca-label" for="wh-tz">Timezone</label><select class="orca-select" id="wh-tz"><option>Europe/Paris</option><option>Europe/London</option></select></div>
  <p class="orca-small orca-muted">Monday to Friday, 08:00–17:00, Paris time. <a class="orca-link" href="#">Different hours per day</a></p>
  <div class="orca-form-actions"><button class="orca-button orca-button--primary" type="submit">Save hours</button></div></form>""")],
    guide=["Working-hours editor"],
))

add(Pattern(
    "recurrence-editor", "Recurrence editor", C,
    "Repeat rules for an event or task: frequency, interval, days, end condition and a plain-language summary.",
    why="Recurrence rules are complex; common presets cover most needs in one choice (Hick's law) and the summary sentence ('Every 2 weeks on Monday and Thursday, 10 times') catches mistakes before saving (Practical UI R22).",
    when=["Events, reminders, tasks and reports that repeat."],
    how=["Start with the recurrence selector (presets plus Custom…); the custom part reveals interval, weekdays (for weekly), day-of-month or weekday-of-month (for monthly) and the end (never, on a date, after N times).",
         "Store as an RFC 5545 RRULE; show the next three dates as a check."],
    classes=[".orca-recurrence__custom"],
    laws=["hick", "R22", "tesler"],
    uses=["recurrence-selector", "weekday-selector", "choice-group", "date-input"],
    examples=[("Repeat", """<div class="orca-field" style="max-width: 30rem"><label class="orca-label" for="re-sel">Repeat</label>
  <select class="orca-select" id="re-sel" data-orca-reveal="re-custom" data-orca-reveal-value="custom"><option>Does not repeat</option><option>Daily</option><option>Weekly on Friday</option><option value="custom" selected>Custom…</option></select>
  <div class="orca-recurrence__custom" id="re-custom">
    <div class="orca-row"><label for="re-n">Every</label><input class="orca-input orca-input--w4" id="re-n" type="number" min="1" value="2"><select class="orca-select" aria-label="Unit" style="width: auto"><option>days</option><option selected>weeks</option><option>months</option></select></div>
    <fieldset class="orca-weekday-toggles"><legend class="orca-label">On</legend>{% for d in "MTWTFSS" %}<label class="orca-weekday"><input type="checkbox" {% if forloop.counter == 1 or forloop.counter == 4 %}checked{% endif %}><span aria-hidden="true">{{ d }}</span><span class="orca-sr-only">{% cycle "Monday" "Tuesday" "Wednesday" "Thursday" "Friday" "Saturday" "Sunday" %}</span></label>{% endfor %}</fieldset>
    <fieldset class="orca-choice-group"><legend class="orca-label">Ends</legend><div class="orca-choice-group__items"><label class="orca-radio"><input type="radio" name="re-end"><span class="orca-radio__dot"></span>Never</label><label class="orca-radio"><input type="radio" name="re-end" checked><span class="orca-radio__dot"></span>After 10 times</label></div></fieldset>
    <p class="orca-small orca-muted" aria-live="polite">Every 2 weeks on Monday and Thursday, 10 times. Next: 9, 12 and 23 November.</p></div></div>""")],
    guide=["Recurrence editor"],
))

add(Pattern(
    "exception-editor", "Exception and holiday editor", C,
    "The list of dates that differ from the regular hours (closed days, short days) with a form to add one.",
    why="Regular hours plus exceptions is how people think about schedules (Tesler's law); listing exceptions by date with a date badge makes the next one easy to spot (Practical UI L09).",
    when=["Public holidays, closures, special opening hours for a site or person."],
    how=["A panel listing exception entries sorted by date (past ones hidden behind 'Show past'), followed by an add form: date, 'Closed all day' switch or a time range, and a reason.",
         "Offer 'Import public holidays' for the site's country."],
    classes=[".orca-exception"],
    laws=["tesler", "L09"],
    uses=["exception-entry", "date-input", "time-range-input", "switch", "panel"],
    examples=[("Exceptions", """<section class="orca-panel" style="max-width: 32rem" aria-labelledby="ex-t"><div class="orca-panel-header"><div class="orca-panel-header__text"><h2 class="orca-panel-title" id="ex-t">Exceptions</h2></div><div class="orca-panel-header__actions"><button class="orca-button orca-button--dense" type="button">Import public holidays</button></div></div>
  <div class="orca-exception"><time class="orca-date-badge" datetime="2026-11-11"><span class="orca-date-badge__month">Nov</span><span class="orca-date-badge__day">11</span><span class="orca-date-badge__weekday">Wed</span></time><div class="orca-exception__body"><span><span class="orca-badge orca-badge--grey">Closed</span></span><span class="orca-exception__meta">Armistice Day</span></div><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="Edit 11 November">{% icon "edit" %}</button></div>
  <div class="orca-exception"><time class="orca-date-badge" datetime="2026-12-24"><span class="orca-date-badge__month">Dec</span><span class="orca-date-badge__day">24</span><span class="orca-date-badge__weekday">Thu</span></time><div class="orca-exception__body"><span class="orca-num">08:00–14:00</span><span class="orca-exception__meta">Christmas Eve, short day</span></div><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="Edit 24 December">{% icon "edit" %}</button></div>
  <button class="orca-button orca-button--ghost" type="button" style="align-self: flex-start">{% icon "plus" %}Add exception</button></section>""")],
    guide=["Exception and holiday editor"],
))

add(Pattern(
    "time-off-editor", "Time-off editor", C,
    "A request form for time off (type, dates, half days, note) beside the person's balance and their existing requests.",
    why="Showing the balance and the working days the request costs before submitting prevents rejected requests (Practical UI R22, Peak–end rule); the list of existing requests shows status at a glance.",
    when=["Holiday, sick leave and training requests; approving them."],
    how=["A form stack: type (radio cards or select), date range picker, 'Half day' options for the first and last day, an optional note, and a live summary ('3 working days, 22 left').",
         "Below, time-off entries with status chips; managers get Approve and Decline on each."],
    classes=[".orca-time-off"],
    laws=["R22", "peak-end"],
    uses=["date-range-picker", "time-off-entry", "form-stack"],
    examples=[("Request time off", """<div class="orca-stack" style="max-width: 32rem"><form class="orca-form-stack" onsubmit="return false">
  <div class="orca-field"><label class="orca-label" for="to-type">Type</label><select class="orca-select" id="to-type"><option>Holiday</option><option>Sick leave</option><option>Training</option></select></div>
  <fieldset class="orca-inline-fields" data-orca-range><legend class="orca-label">Dates</legend><div class="orca-field"><label class="orca-label" for="to-a">From</label><input class="orca-input" type="date" id="to-a" value="2026-11-16"></div><span class="orca-inline-fields__sep" aria-hidden="true">–</span><div class="orca-field"><label class="orca-label" for="to-b">To</label><input class="orca-input" type="date" id="to-b" value="2026-11-18"></div><p class="orca-inline-fields__note" data-orca-range-output aria-live="polite">3 days</p></fieldset>
  <p class="orca-small">3 working days. <strong>22 days left</strong> after this request.</p>
  <div class="orca-form-actions"><button class="orca-button orca-button--primary" type="submit">Send request</button></div></form>
  <div class="orca-time-off"><span class="orca-avatar orca-avatar--s" aria-hidden="true">GH</span><div class="orca-time-off__body"><span>Holiday</span><span class="orca-time-off__meta">2–6 October · 5 days</span></div><span class="orca-chip orca-chip--done">Approved</span></div></div>""")],
    guide=["Time-off editor"],
))

add(Pattern(
    "resource-scheduler", "Resource scheduler", C,
    "Resources (people, rooms, videos) as rows against a time scale, with bookings as bars on each row.",
    why="Rows per resource answer 'who is free when' directly (Practical UI L01, grouping), which a calendar per person cannot. Bars are positioned by time so gaps and double bookings are visible.",
    when=["Assigning installers, rooms or vehicles; seeing a team's day."],
    how=["`<div class=\"orca-scheduler\" style=\"--orca-cols: 10\">`: a corner and `.orca-scheduler__scale` of hours, then per resource `.orca-scheduler__who` and `.orca-scheduler__lane` containing event cards placed with `--orca-start` and `--orca-span` (percentages of the day).",
         "Compute the percentages in the view: `(start - day_start) / (day_end - day_start)`; wrap in `.orca-table-wrap` to scroll on phones."],
    classes=[".orca-scheduler", ".orca-scheduler__corner", ".orca-scheduler__scale", ".orca-scheduler__who", ".orca-scheduler__lane"],
    laws=["L01", "L09"],
    uses=["event-card", "avatar", "availability-legend"],
    examples=[("Installers, Friday", """<div class="orca-table-wrap"><div class="orca-scheduler" style="--orca-cols: 10">
  <div class="orca-scheduler__corner"></div><div class="orca-scheduler__scale">{% for h in "89" %}<span>0{{ h }}</span>{% endfor %}{% for h in "01234567" %}<span>1{{ h }}</span>{% endfor %}</div>
  <div class="orca-scheduler__who"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span>Ada Lovelace</div><div class="orca-scheduler__lane"><a class="orca-event-card" href="#" style="--orca-event: var(--orca-chart-2); --orca-start: 20%; --orca-span: 15%"><span class="orca-event-card__title">Audit</span><span class="orca-event-card__meta">10:00–11:30</span></a><a class="orca-event-card" href="#" style="--orca-event: var(--orca-chart-1); --orca-start: 60%; --orca-span: 15%"><span class="orca-event-card__title">Training</span><span class="orca-event-card__meta">14:00–15:30</span></a></div>
  <div class="orca-scheduler__who"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AT</span>Alan Turing</div><div class="orca-scheduler__lane"><a class="orca-event-card" href="#" style="--orca-event: var(--orca-chart-5); --orca-start: 0%; --orca-span: 40%"><span class="orca-event-card__title">Install, Gate 1</span><span class="orca-event-card__meta">08:00–12:00</span></a></div>
  <div class="orca-scheduler__who"><span class="orca-avatar orca-avatar--s" aria-hidden="true">GH</span>Grace Hopper</div><div class="orca-scheduler__lane"><span class="orca-event-card orca-event-card--tentative" style="--orca-event: var(--orca-chart-8); --orca-start: 0%; --orca-span: 100%"><span class="orca-event-card__title">On holiday</span></span></div>
</div></div>""")],
    guide=["Resource scheduler (resources by time)"],
))

add(Pattern(
    "shift-planner", "Shift planner", C,
    "A roster table of people by days with shifts in each cell, weekly totals and over-hours highlighted.",
    why="Rosters are read both ways, 'who works Tuesday' and 'what does Grace work', which a table does best (Practical UI L01, grouping). Totals against contract hours catch overwork before publishing (Von Restorff: over-hours stand out).",
    when=["Weekly staff rotas, on-call schedules."],
    how=["`<table class=\"orca-roster\">`: people as row headers, days as column headers (weekends `is-weekend`), each cell holding `.orca-shift` blocks (`--orca-event` colours the shift type), and a `.orca-roster__total` column; mark over-hours cells `is-over` and say it in text.",
         "Edit a cell in a drawer or popover; publish the roster as one action with a confirmation."],
    classes=[".orca-roster", ".orca-shift", ".orca-roster__total"],
    laws=["L01", "restorff"],
    uses=["avatar", "badge"],
    examples=[("Week 46", """<div class="orca-table-wrap"><table class="orca-roster"><caption class="orca-sr-only">Roster, week of 9 November</caption>
  <thead><tr><th scope="col">Person</th><th scope="col">Mon 9</th><th scope="col">Tue 10</th><th scope="col">Wed 11</th><th scope="col">Thu 12</th><th scope="col">Fri 13</th><th scope="col" class="is-weekend">Sat 14</th><th scope="col" class="orca-roster__total">Hours</th></tr></thead>
  <tbody><tr><th scope="row">Ada Lovelace</th><td><span class="orca-shift" style="--orca-event: var(--orca-chart-1)">08–16<span class="orca-small">Early</span></span></td><td><span class="orca-shift" style="--orca-event: var(--orca-chart-1)">08–16</span></td><td></td><td><span class="orca-shift" style="--orca-event: var(--orca-chart-3)">12–20</span></td><td><span class="orca-shift" style="--orca-event: var(--orca-chart-3)">12–20</span></td><td class="is-weekend"></td><td class="orca-roster__total">32 / 40</td></tr>
  <tr><th scope="row">Grace Hopper</th><td><span class="orca-shift" style="--orca-event: var(--orca-chart-3)">12–21</span></td><td><span class="orca-shift" style="--orca-event: var(--orca-chart-3)">12–21</span></td><td><span class="orca-shift" style="--orca-event: var(--orca-chart-3)">12–21</span></td><td><span class="orca-shift" style="--orca-event: var(--orca-chart-3)">12–21</span></td><td><span class="orca-shift" style="--orca-event: var(--orca-chart-1)">08–16</span></td><td class="is-weekend is-over"><span class="orca-shift" style="--orca-event: var(--orca-chart-5)">10–14</span></td><td class="orca-roster__total"><span class="orca-overdue">{% icon "error" %}48 / 40</span></td></tr></tbody></table></div>""")],
    guide=["Shift planner (roster)"],
))

add(Pattern(
    "booking-slot-picker", "Booking slot picker", C,
    "A strip of dates and the free slots on the chosen date, grouped by part of day, for booking a fixed-length slot.",
    why="Showing only bookable times removes failed attempts (Practical UI R22); grouping by morning and afternoon shortens the scan (Practical UI L09, Hick's law). Full days are visible but disabled so people know why.",
    when=["Booking a visit, a call, a calibration slot: fixed length, chosen by the visitor."],
    how=["`<div class=\"orca-booking\">`: `<ul class=\"orca-date-strip\">` of day buttons (`aria-pressed`, disabled when full), then groups with `.orca-booking__group` headings and booking slots.",
         "Show the duration and timezone above the slots; confirm the choice in a summary before booking."],
    classes=[".orca-booking", ".orca-date-strip", ".orca-booking__group"],
    laws=["R22", "L09", "hick"],
    uses=["booking-slot", "button"],
    examples=[("Book a 30-minute call", """<div class="orca-booking"><p class="orca-small orca-muted">30 minutes · Paris time</p>
  <ul class="orca-date-strip" aria-label="Day"><li><button type="button" aria-pressed="false">Mon<strong>9</strong></button></li><li><button type="button" aria-pressed="true">Tue<strong>10</strong></button></li><li><button type="button" disabled>Wed<strong>11</strong>Full</button></li><li><button type="button" aria-pressed="false">Thu<strong>12</strong></button></li><li><button type="button" aria-pressed="false">Fri<strong>13</strong></button></li></ul>
  <div><h3 class="orca-booking__group">Morning</h3><ul class="orca-booking-slots"><li><button class="orca-booking-slot" type="button" aria-pressed="false">09:00</button></li><li><button class="orca-booking-slot" type="button" aria-pressed="true">09:30</button></li><li><button class="orca-booking-slot" type="button" disabled>10:00<span class="orca-booking-slot__note">Booked</span></button></li></ul></div>
  <div><h3 class="orca-booking__group">Afternoon</h3><ul class="orca-booking-slots"><li><button class="orca-booking-slot" type="button" aria-pressed="false">14:00</button></li><li><button class="orca-booking-slot orca-booking-slot--limited" type="button" aria-pressed="false">15:30<span class="orca-booking-slot__note">Last one</span></button></li></ul></div>
  <div class="orca-row"><button class="orca-button orca-button--primary" type="button">Book Tuesday 10 November, 09:30</button></div></div>""")],
    guide=["Booking slot picker"],
))

add(Pattern(
    "appointment-picker", "Appointment picker", C,
    "Booking in steps: choose the service and person, then the date and time, then confirm, with a running summary.",
    why="Each choice narrows the next (the person changes the free times), so steps keep each decision small (Hick's law) and the summary keeps earlier choices visible and editable (Peak–end rule).",
    when=["Bookings that depend on a service type, duration or staff member."],
    avoid=["Single service, single person: the booking slot picker alone is enough."],
    how=["Steps at the top; step 1 radio cards for the service (with duration and price), optional person picker; step 2 the booking slot picker; step 3 contact details and a summary with 'Change' links.",
         "Hold the chosen slot for a few minutes and say so ('Held for you until 10:52')."],
    classes=[".orca-booking"],
    laws=["hick", "peak-end"],
    uses=["steps", "booking-slot", "key-value-list"],
    examples=[("Step 1 of 3", """<div class="orca-booking"><ol class="orca-steps"><li class="orca-steps__item" aria-current="step"><span class="orca-step-marker orca-step-marker--current" aria-hidden="true"></span><span class="orca-steps__title">Service</span></li><li class="orca-steps__item"><span class="orca-step-marker" aria-hidden="true"></span><span class="orca-steps__title">Time</span></li><li class="orca-steps__item"><span class="orca-step-marker" aria-hidden="true"></span><span class="orca-steps__title">Confirm</span></li></ol>
  <fieldset class="orca-choice-group"><legend class="orca-label">What do you need?</legend><div class="orca-choice-group__items">
    <label class="orca-radio"><input type="radio" name="ap-s" checked><span class="orca-radio__dot"></span>Video calibration, 30 min</label>
    <label class="orca-radio"><input type="radio" name="ap-s"><span class="orca-radio__dot"></span>New site survey, 1 h</label></div></fieldset>
  <div class="orca-field"><label class="orca-label" for="ap-p">With</label><select class="orca-select" id="ap-p"><option>Anyone available</option><option>Ada Lovelace</option><option>Alan Turing</option></select></div>
  <div class="orca-row"><button class="orca-button orca-button--primary" type="button">Choose a time</button></div></div>""")],
    guide=["Appointment picker"],
))

add(Pattern(
    "conflict-resolver", "Conflict resolver", C,
    "When two bookings clash: both side by side with what conflicts, and clear choices to resolve it.",
    why="Resolving a clash needs both items compared (Practical UI L09); offering concrete resolutions (move, keep both, cancel one) turns a problem into one decision (Hick's law, Peak–end rule).",
    when=["Saving an event that overlaps another for the same person or room; importing schedules."],
    how=["`<div class=\"orca-conflict\">` with a caution callout naming the conflict, `.orca-conflict__pair` of two `label.orca-conflict__option` (radio + event card) to choose which to keep, a 'Keep both' option, and the actions.",
         "Suggest the nearest free time for the moved item."],
    classes=[".orca-conflict", ".orca-conflict__pair", ".orca-conflict__option"],
    laws=["L09", "hick", "peak-end"],
    uses=["conflict-warning", "event-card", "radio"],
    examples=[("Clash", """<div class="orca-conflict" style="max-width: 40rem"><div class="orca-callout orca-callout--caution" role="status">{% icon "warning" %}<p class="orca-callout__title">Ada Lovelace has two things at 10:30 on Friday</p><div class="orca-callout__body"><p class="orca-p">Choose which to keep at that time. The other moves to 11:30, her next free slot.</p></div></div>
  <div class="orca-conflict__pair"><label class="orca-conflict__option"><span class="orca-radio"><input type="radio" name="cf" checked><span class="orca-radio__dot"></span>Keep the audit</span><span class="orca-event-card" style="--orca-event: var(--orca-chart-2)"><span class="orca-event-card__title">Audit</span><span class="orca-event-card__meta">10:00–11:30 · North building</span></span></label>
    <label class="orca-conflict__option"><span class="orca-radio"><input type="radio" name="cf"><span class="orca-radio__dot"></span>Keep the call</span><span class="orca-event-card" style="--orca-event: var(--orca-chart-3)"><span class="orca-event-card__title">Supplier call</span><span class="orca-event-card__meta">10:30–11:00</span></span></label></div>
  <div class="orca-row"><button class="orca-button orca-button--primary" type="button">Move the other to 11:30</button><button class="orca-button" type="button">Keep both</button></div></div>""")],
    guide=["Conflict resolver"],
))
