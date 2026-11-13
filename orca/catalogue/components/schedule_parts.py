from ..registry import add, category
from . import Component

C = category(
    "schedule-parts", "Schedule parts",
    "Rows and messages for opening hours, availability, exceptions, time off and bookings.",
    level="component",
)

DAYS = '<option>Monday</option><option>Tuesday</option><option>Wednesday</option><option>Thursday</option><option>Friday</option><option>Saturday</option><option>Sunday</option>'

add(Component(
    "schedule-row", "Schedule row", C,
    "One line of a weekly schedule: day, start time, end time and a remove button.",
    why="Opening hours vary by day and may split around lunch; one row per span handles every case without special fields (Tesler's law), and rows read like a timetable (Jakob's law).",
    when=["Opening hours, working hours, capture schedules."],
    how=["`<div class=\"orca-schedule-row\" data-orca-row>` with a day select, start time, `.orca-schedule-row__sep` '–', end time and a remove-row button; rows live in `<div class=\"orca-schedule\" id=…>`.",
         "Invalid rows get `--invalid` and a `.orca-schedule-row__msg` error (end before start, overlap).",
         "Django: one formset row per span; the add-row button clones the empty form."],
    classes=[".orca-schedule", ".orca-schedule-row", ".orca-schedule-row__sep", ".orca-schedule-row--invalid", ".orca-schedule-row__msg"],
    laws=["tesler", "jakob", "postel"],
    uses=["select", "time-input", "remove-row-button"],
    examples=[("Opening hours", f"""<div class="orca-schedule" id="sr-list">
  <div class="orca-schedule-row" data-orca-row><select class="orca-select" aria-label="Day">{DAYS}</select><input class="orca-input" type="time" value="08:00" aria-label="Opens"><span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" value="12:00" aria-label="Closes"><button class="orca-icon-button" type="button" aria-label="Remove Monday 08:00 to 12:00" data-orca-remove-row>{{% icon "delete" %}}</button></div>
  <div class="orca-schedule-row orca-schedule-row--invalid" data-orca-row><select class="orca-select" aria-label="Day">{DAYS}</select><input class="orca-input" type="time" value="13:00" aria-label="Opens" aria-invalid="true" aria-describedby="sr-err"><span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" value="12:30" aria-label="Closes" aria-invalid="true" aria-describedby="sr-err"><button class="orca-icon-button" type="button" aria-label="Remove Monday 13:00 to 12:30" data-orca-remove-row>{{% icon "delete" %}}</button>
    <p class="orca-error orca-schedule-row__msg" id="sr-err">{{% icon "error" %}}<span>Closing time must be after opening time.</span></p></div>
</div>""")],
    guide=["Schedule row (day, start, end)"],
))

add(Component(
    "add-row-button", "Add-row button", C,
    "A ghost button that adds a row to a repeating group and focuses it.",
    why="Letting people add rows only when needed keeps the default form short (Practical UI R02); focusing the new row saves a click (Fitts's law).",
    when=["Schedules, reminders, properties, any repeating fields."],
    how=["`<button class=\"orca-button orca-button--ghost\" type=\"button\" data-orca-add-row=\"template-id\" aria-controls=\"list-id\">{% templatetag openblock %} icon \"plus\" {% templatetag closeblock %}Add hours</button>` below the rows.",
         "Name what it adds ('Add hours', 'Add reminder'); at the maximum number of rows, hide it and say the limit."],
    classes=[".orca-button--ghost"],
    laws=["R02", "fitts", "B10"],
    uses=["button", "icon"],
    examples=[("Add row", f"""<div class="orca-schedule" id="ar-list"><div class="orca-schedule-row" data-orca-row><select class="orca-select" aria-label="Day">{DAYS}</select><input class="orca-input" type="time" value="08:00" aria-label="Opens"><span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" value="18:00" aria-label="Closes"><button class="orca-icon-button" type="button" aria-label="Remove row" data-orca-remove-row>{{% icon "delete" %}}</button></div></div>
<template id="ar-tpl"><div class="orca-schedule-row" data-orca-row><select class="orca-select" aria-label="Day">{DAYS}</select><input class="orca-input" type="time" aria-label="Opens"><span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" aria-label="Closes"><button class="orca-icon-button" type="button" aria-label="Remove row" data-orca-remove-row>{{% icon "delete" %}}</button></div></template>
<button class="orca-button orca-button--ghost" type="button" data-orca-add-row="ar-tpl" aria-controls="ar-list" style="margin-top: var(--orca-space-8)">{{% icon "plus" %}}Add hours</button>""")],
    guide=["Add-row button"],
))

add(Component(
    "remove-row-button", "Remove-row button", C,
    "An icon button that removes its row; named after the row and announced when used.",
    why="Removing a row is low risk and easy to redo, so it needs no confirmation (Doherty: friction only where costly), but its name must say which row it removes (Hick's law: labelled icons).",
    when=["The end of every removable row."],
    how=["`<button class=\"orca-icon-button\" type=\"button\" aria-label=\"Remove Monday 08:00 to 12:00\" data-orca-remove-row>{% templatetag openblock %} icon \"delete\" {% templatetag closeblock %}</button>`.",
         "With Django formsets, tick the row's `-DELETE` checkbox and hide the row instead of removing it.",
         "Focus moves to the next row; the removal is announced."],
    classes=[".orca-icon-button"],
    laws=["doherty", "hick"],
    uses=["icon-button"],
    examples=[("Remove", """<button class="orca-icon-button" type="button" aria-label="Remove Monday 08:00 to 12:00">{% icon "delete" %}</button>""")],
    guide=["Remove-row button"],
))

add(Component(
    "availability-legend", "Availability legend", C,
    "The key to the availability marks: free, busy, tentative, not working.",
    why="Patterns only help if their meaning is stated next to them (Practical UI C03).",
    when=["Above schedulers, booking grids and resource rows."],
    how=["`<ul class=\"orca-legend\">` of availability marks: `<li><span class=\"orca-avail orca-avail--free\">Free</span></li>` etc."],
    classes=[".orca-legend"],
    laws=["C03"],
    uses=["availability-color", "legend-item"],
    examples=[("Legend", """<ul class="orca-legend"><li><span class="orca-avail orca-avail--free">Free</span></li><li><span class="orca-avail orca-avail--busy">Busy</span></li><li><span class="orca-avail orca-avail--tentative">Tentative</span></li><li><span class="orca-avail orca-avail--off">Not working</span></li></ul>""")],
    guide=["Availability legend"],
))

add(Component(
    "exception-entry", "Exception entry", C,
    "A one-day override of the usual schedule: date, new hours or Closed, and the reason.",
    why="Exceptions are where schedules go wrong; listing each with its date and reason makes them visible and reviewable (Peak–end rule, Practical UI S06).",
    when=["Holidays, special openings, maintenance days."],
    how=["`<div class=\"orca-exception\">` with a date badge, `.orca-exception__body` (hours or 'Closed' badge + `.orca-exception__meta` reason) and row actions."],
    classes=[".orca-exception", ".orca-exception__body", ".orca-exception__meta"],
    laws=["peak-end", "S06"],
    uses=["date-badge", "badge", "row-actions"],
    examples=[("Exceptions", """<div style="max-width: 30rem">
  <div class="orca-exception"><time class="orca-date-badge" datetime="2026-11-11"><span class="orca-date-badge__month">Nov</span><span class="orca-date-badge__day">11</span><span class="orca-date-badge__weekday">Wed</span></time><div class="orca-exception__body"><span><span class="orca-badge orca-badge--grey">Closed</span></span><span class="orca-exception__meta">Armistice Day</span></div><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="Edit 11 November">{% icon "edit" %}</button></div>
  <div class="orca-exception"><time class="orca-date-badge" datetime="2026-12-24"><span class="orca-date-badge__month">Dec</span><span class="orca-date-badge__day">24</span><span class="orca-date-badge__weekday">Thu</span></time><div class="orca-exception__body"><span class="orca-num">08:00–14:00</span><span class="orca-exception__meta">Christmas Eve, short day</span></div><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="Edit 24 December">{% icon "edit" %}</button></div>
</div>""")],
    guide=["Exception entry (date override)"],
))

add(Component(
    "time-off-entry", "Time-off entry", C,
    "A person's absence: who, dates, type and approval status.",
    why="Planners need who is away, when and whether it is confirmed in one row (Miller's law); status as a word and shape avoids colour-only meaning (C03).",
    when=["Time-off lists, team calendars, roster sidebars."],
    how=["`<div class=\"orca-time-off\">` with an avatar, `.orca-time-off__body` (name + dates and length in `__meta`) and a status chip."],
    classes=[".orca-time-off", ".orca-time-off__body", ".orca-time-off__meta"],
    laws=["miller", "C03"],
    uses=["avatar", "date-label", "status-chip"],
    examples=[("Time off", """<div style="max-width: 32rem">
  <div class="orca-time-off"><span class="orca-avatar orca-avatar--s" aria-hidden="true">GH</span><div class="orca-time-off__body"><span>Grace Hopper · Holiday</span><span class="orca-time-off__meta"><time datetime="2026-11-16">16</time>–<time datetime="2026-11-20">20 November</time> · 5 days</span></div><span class="orca-chip orca-chip--done">Approved</span></div>
  <div class="orca-time-off"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AT</span><div class="orca-time-off__body"><span>Alan Turing · Training</span><span class="orca-time-off__meta"><time datetime="2026-11-23">23 November</time> · 1 day</span></div><span class="orca-chip orca-chip--planned">Requested</span></div>
</div>""")],
    guide=["Time-off entry"],
))

add(Component(
    "booking-slot", "Booking slot", C,
    "A bookable time as a large button: free, limited ('2 left'), full or chosen.",
    why="Seeing all times at once with their availability makes choosing quick (Hick's law); full slots stay visible but struck and dashed so the pattern of the day is clear without colour (C03); large targets suit phones (Fitts's law).",
    when=["Appointment and booking flows."],
    how=["`<ul class=\"orca-booking-slots\">` of `<li><button class=\"orca-booking-slot\" type=\"button\" aria-pressed=\"false\">09:30<span class=\"orca-booking-slot__note\">2 left</span></button></li>`.",
         "Full slots: `disabled` with 'Full' in the note; limited: `--limited`. The chosen slot `aria-pressed=\"true\"`. Group by morning and afternoon."],
    classes=[".orca-booking-slots", ".orca-booking-slot", ".orca-booking-slot__note", ".orca-booking-slot--limited"],
    laws=["hick", "C03", "fitts"],
    uses=["time-label"],
    examples=[("Slots", """<ul class="orca-booking-slots" style="max-width: 32rem">
  <li><button class="orca-booking-slot" type="button" aria-pressed="false">09:00<span class="orca-booking-slot__note">Free</span></button></li>
  <li><button class="orca-booking-slot" type="button" aria-pressed="true">09:30<span class="orca-booking-slot__note">Your choice</span></button></li>
  <li><button class="orca-booking-slot orca-booking-slot--limited" type="button" aria-pressed="false">10:00<span class="orca-booking-slot__note">2 left</span></button></li>
  <li><button class="orca-booking-slot" type="button" disabled>10:30<span class="orca-booking-slot__note">Full</span></button></li>
</ul>""")],
    guide=["Booking slot"],
))

add(Component(
    "conflict-warning", "Conflict warning", C,
    "A caution message naming what the plan conflicts with and how to fix it.",
    why="Conflicts found early are cheap to fix (Peak–end rule: prevent the negative peak); naming the other item and offering the fix turns a warning into a decision.",
    when=["Saving an event, shift or run that clashes with another one."],
    how=["A caution callout: the title names the conflict ('Grace Hopper is on holiday that day'), the body links the other item, actions offer fixes ('Pick another person', 'Save anyway').",
         "Use caution when saving is still allowed; negative when it is blocked."],
    classes=[".orca-callout--caution"],
    laws=["peak-end", "W15"],
    uses=["callout", "button"],
    examples=[("Conflict", """<div class="orca-callout orca-callout--caution" role="status">{% icon "warning" %}<p class="orca-callout__title">Grace Hopper is on holiday on 18 November</p><div class="orca-callout__body"><p class="orca-p">See <a class="orca-link" href="#">time off, 16–20 November</a>.</p><div class="orca-row"><button class="orca-button orca-button--dense" type="button">Pick another person</button><button class="orca-button orca-button--link" type="button">Save anyway</button></div></div></div>""")],
    guide=["Conflict warning"],
))

add(Component(
    "overlap-warning", "Overlap warning", C,
    "An inline message under a schedule row that overlaps another row.",
    why="Pointing at the exact row and the row it overlaps lets people fix it in place (Practical UI R21, W15).",
    when=["Schedule editors, as rows change (after leaving the field)."],
    how=["A `.orca-error` (or caution `.orca-help` with the warning icon when allowed) as `.orca-schedule-row__msg` inside the row: 'Overlaps Monday 08:00–12:00. Change the start or remove one row.'",
         "Link it with `aria-describedby` from both time inputs."],
    classes=[".orca-schedule-row__msg"],
    laws=["R21", "W15"],
    uses=["error-text", "schedule-row"],
    examples=[("Overlap", """<p class="orca-error">{% icon "error" %}<span>Overlaps Monday 08:00–12:00. Change the start or remove one of the rows.</span></p>""")],
    guide=["Overlap warning"],
))

add(Component(
    "working-hours-label", "Working-hours label", C,
    "'Open now, closes at 18:00' or 'Closed, opens Monday 08:00', with a status dot.",
    why="People want to know whether a place is open now and when that changes (Tesler's law: the system does the arithmetic); the word carries the state, the dot confirms it (C03).",
    when=["Site headers, booking pages, contact blocks."],
    how=["`<span class=\"orca-working-hours\">` with a status dot, `.orca-working-hours__state` ('Open') and the next change ('closes at 18:00').",
         "Compute in the site's timezone; mention it when it differs from the reader's."],
    classes=[".orca-working-hours", ".orca-working-hours__state"],
    laws=["tesler", "C03"],
    uses=["status-dot", "time-label"],
    examples=[("Open and closed", """<div class="orca-stack"><span class="orca-working-hours"><span class="orca-dot orca-dot--positive"></span><span class="orca-working-hours__state">Open</span>closes at <time datetime="18:00">18:00</time></span><span class="orca-working-hours"><span class="orca-dot"></span><span class="orca-working-hours__state">Closed</span>opens Monday at <time datetime="08:00">08:00</time></span></div>""")],
    guide=["Working-hours label"],
))
