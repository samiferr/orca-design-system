from ..registry import add, category
from . import Pattern

C = category(
    "event-editing", "Event editing",
    "Creating, viewing and answering events: full editor, popover, panel, quick add, reminders, attendees and RSVP.",
    level="pattern",
)

add(Pattern(
    "event-editor", "Event editor", C,
    "The full form for an event: title, date and time (or all day), repeat, place, people, reminders, calendar and notes.",
    why="Events have many optional fields; putting the essentials first (title, when) and the rest in labelled sections keeps the form short to read (Practical UI F01, F05) while still complete. Defaults (next round half hour, 1 hour, 15-minute reminder) mean most events need two fields (Tesler's law).",
    when=["Creating or editing an event in full, on its own page or in a drawer."],
    how=["A form stack: title (autofocus), date-time range with an 'All day' switch, recurrence selector, location, attendees (multi picker), reminders, calendar (select with colour), notes.",
         "Warn about conflicts inline (conflict warning) without blocking save; keep 'Save' and 'Cancel' at the bottom and 'Delete' apart from them."],
    classes=[".orca-form-stack"],
    laws=["F01", "F05", "tesler"],
    uses=["form-stack", "datetime-picker", "recurrence-selector", "reminder-selector", "multi-picker", "conflict-warning"],
    examples=[("New event", """<form class="orca-form-stack" style="max-width: 32rem" onsubmit="return false">
  <div class="orca-field"><label class="orca-label" for="ee-t">Title</label><input class="orca-input" id="ee-t" value="Audit"></div>
  <fieldset class="orca-inline-fields" data-orca-range><legend class="orca-label">When</legend><div class="orca-field"><label class="orca-label" for="ee-a">Starts</label><input class="orca-input" type="datetime-local" id="ee-a" value="2026-11-06T10:00"></div><span class="orca-inline-fields__sep" aria-hidden="true">–</span><div class="orca-field"><label class="orca-label" for="ee-b">Ends</label><input class="orca-input" type="datetime-local" id="ee-b" value="2026-11-06T11:30"></div><p class="orca-inline-fields__note" data-orca-range-output aria-live="polite">1 h 30 min</p></fieldset>
  <label class="orca-switch"><input type="checkbox" role="switch"><span class="orca-switch__track"></span><span>All day</span></label>
  <div class="orca-field"><label class="orca-label" for="ee-r">Repeat</label><select class="orca-select" id="ee-r"><option>Does not repeat</option><option>Weekly on Friday</option></select></div>
  <div class="orca-field"><label class="orca-label" for="ee-l">Location <span class="orca-optional">(optional)</span></label><input class="orca-input" id="ee-l" value="North building"></div>
  <div class="orca-callout orca-callout--caution" role="status">{% icon "warning" %}<p class="orca-callout__title">Overlaps Supplier call, 10:30–11:00</p></div>
  <div class="orca-form-actions"><button class="orca-button orca-button--primary" type="submit">Save event</button><button class="orca-button" type="button">Cancel</button></div></form>""")],
    guide=["Event editor"],
))

add(Pattern(
    "event-popover", "Event detail popover", C,
    "A small card that opens over the calendar when an event is clicked: title, time, place, people and quick actions.",
    why="Most clicks on an event just check details; a popover answers in place without losing the calendar (Doherty threshold, Jakob's law) and offers Edit for the rest.",
    when=["Clicking an event in month, week or day views on wide screens."],
    avoid=["Phones: open the event detail panel as a page or bottom drawer instead."],
    how=["A native popover: `<div class=\"orca-event-popover\" id=\"…\" popover>` opened by `<button popovertarget=\"…\">` on the event; `--orca-event` colours its edge.",
         "Head with title and close button; body lines with icons (time, place, calendar); foot with Edit, Delete and 'Open'. Escape and outside click close it (built into popover)."],
    classes=[".orca-event-popover", ".orca-event-popover__head", ".orca-event-popover__title", ".orca-event-popover__body", ".orca-event-popover__foot"],
    laws=["doherty", "jakob", "L09"],
    uses=["event-chip", "panel-header", "button-group"],
    examples=[("Popover", """<button class="orca-event-chip" type="button" popovertarget="ep-1" style="max-width: 12rem"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-2)"></span><span class="orca-event-chip__time">10:00</span><span class="orca-event-chip__title">Audit</span></button>
<div class="orca-event-popover" id="ep-1" popover style="--orca-event: var(--orca-chart-2)"><div class="orca-event-popover__head"><h3 class="orca-event-popover__title">Audit</h3><button class="orca-icon-button orca-icon-button--sm" type="button" popovertarget="ep-1" popovertargetaction="hide" aria-label="Close">{% icon "close" %}</button></div>
  <div class="orca-event-popover__body"><span>{% icon "clock" size="xs" %}Friday 6 November, 10:00–11:30</span><span>{% icon "location" size="xs" %}North building</span><span>{% icon "user" size="xs" %}Ada Lovelace, Grace Hopper</span></div>
  <div class="orca-event-popover__foot"><button class="orca-button orca-button--dense" type="button">Edit</button><button class="orca-button orca-button--dense orca-button--ghost" type="button">Delete</button></div></div>""")],
    guide=["Event detail popover"],
))

add(Pattern(
    "event-detail-panel", "Event detail panel", C,
    "All of an event's details in a panel or page: title, status, time, place, description, attendees and actions.",
    why="When people need the whole event (notes, everyone's answers) a panel gives room and stays readable on phones (Practical UI L01); the coloured top edge ties it to its calendar (Practical UI F09).",
    when=["Opening an event on phones, from notifications or from lists; a drawer beside the calendar."],
    how=["`<article class=\"orca-event-panel\" style=\"--orca-event: …\">` with the title, a key–value list (when, where, calendar, repeat), the description, the attendee list and the invitation response bar at the bottom."],
    classes=[".orca-event-panel"],
    laws=["L01", "F09"],
    uses=["key-value-list", "attendee-list", "invitation-response-bar", "record-actions"],
    examples=[("Audit", """<article class="orca-event-panel" style="--orca-event: var(--orca-chart-2)"><div class="orca-row" style="justify-content: space-between"><h2 class="orca-h3" style="margin: 0">Audit</h2><span class="orca-badge orca-badge--subtle orca-badge--caution">Tentative</span></div>
  <dl class="orca-kv"><div><dt>When</dt><dd>Friday 6 November, 10:00–11:30</dd></div><div><dt>Where</dt><dd>North building</dd></div><div><dt>Calendar</dt><dd>Installs and audits</dd></div></dl>
  <p class="orca-p">Yearly count audit with the landlord. Bring the October reports.</p>
  <div class="orca-row"><button class="orca-button" type="button">{% icon "edit" %}Edit</button><button class="orca-button orca-button--ghost" type="button">Duplicate</button></div></article>""")],
    guide=["Event detail panel"],
))

add(Pattern(
    "quick-add-event", "Quick-add event", C,
    "One text field that creates an event from a sentence ('Audit Friday 10:00 at North building'), showing what it understood before saving.",
    why="Typing one sentence is faster than filling a form for simple events (Tesler's law); previewing the parsed date and time prevents wrong events (Practical UI R22).",
    when=["Fast entry at the top of a calendar or task list; command palettes."],
    how=["`<form class=\"orca-quick-add\">` with `.orca-quick-add__row` (input + Add button) and `.orca-quick-add__preview` (aria-live) showing the parsed result; parse on the server and return the preview with htmx.",
         "Link to the full editor for anything more."],
    classes=[".orca-quick-add", ".orca-quick-add__row", ".orca-quick-add__preview"],
    laws=["tesler", "R22"],
    uses=["input-group"],
    examples=[("Quick add", """<form class="orca-quick-add" onsubmit="return false"><label class="orca-label" for="qa-i">Add an event</label><div class="orca-quick-add__row"><input class="orca-input" id="qa-i" value="Audit Friday 10:00 at North building" aria-describedby="qa-p"><button class="orca-button orca-button--primary" type="submit">Add</button></div>
  <p class="orca-quick-add__preview" id="qa-p" aria-live="polite">{% icon "calendar" size="xs" %}Audit · Friday 6 November, 10:00–11:00 · North building <a class="orca-link" href="#">More options</a></p></form>""")],
    guide=["Quick-add event"],
))

add(Pattern(
    "reminder-manager", "Reminder manager", C,
    "The list of upcoming reminders with Snooze and Done, and the defaults for new events.",
    why="Reminders only help if acting on them is one tap (Fitts's law); grouping due-now apart from later keeps the urgent ones on top (Von Restorff, Practical UI L03).",
    when=["A reminders page or panel; notification settings for events."],
    how=["Groups ('Due now', 'Later today', 'Tomorrow') of reminder items; each has Snooze (with durations in a menu) and Done.",
         "Below, the default reminders for new events using the reminder selector."],
    classes=[".orca-plan-row"],
    laws=["fitts", "restorff", "L03"],
    uses=["reminder-item", "reminder-selector"],
    examples=[("Reminders", """<div class="orca-stack" style="max-width: 34rem"><h3 class="orca-task-list__group">Due now</h3>
  <div class="orca-plan-row">{% icon "notifications" %}<span class="orca-plan-row__body"><span>Audit at North building</span><span class="orca-plan-row__meta">Starts in 15 minutes</span></span><span class="orca-row"><button class="orca-button orca-button--sm" type="button">Snooze</button><button class="orca-button orca-button--sm" type="button">Done</button></span></div>
  <h3 class="orca-task-list__group">Tomorrow</h3>
  <div class="orca-plan-row">{% icon "notifications" %}<span class="orca-plan-row__body"><span>Licence renewal</span><span class="orca-plan-row__meta">Saturday, 09:00</span></span><span class="orca-row"><button class="orca-button orca-button--sm" type="button">Snooze</button><button class="orca-button orca-button--sm" type="button">Done</button></span></div></div>""")],
    guide=["Reminder manager"],
))

add(Pattern(
    "attendee-list", "Attendee list", C,
    "People invited to an event with their answers, a summary count and controls to add or remove.",
    why="Organisers need to know who is coming at a glance; the summary ('3 yes, 1 waiting') answers first (Practical UI W05) and each answer has an icon and a word, not just a colour.",
    when=["Event editor and event detail panel."],
    how=["`<p class=\"orca-attendees__summary\">` then `<ul class=\"orca-attendees\">` of `.orca-attendee`: avatar, name (and role 'Organiser'), and `.orca-attendee__resp--yes|no|maybe|waiting` with icon and text.",
         "In the editor, add people with a multi picker and remove with an icon button per row."],
    classes=[".orca-attendees", ".orca-attendee", ".orca-attendee__resp", ".orca-attendees__summary"],
    laws=["W05", "C03"],
    uses=["list-item", "multi-picker", "remove-row-button"],
    examples=[("Attendees", """<div style="max-width: 26rem"><p class="orca-attendees__summary">2 going, 1 maybe, 1 waiting</p><ul class="orca-attendees">
  <li class="orca-attendee"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span>Ada Lovelace <span class="orca-small orca-muted">Organiser</span></span><span class="orca-attendee__resp orca-attendee__resp--yes">{% icon "success" size="xs" %}Going</span></li>
  <li class="orca-attendee"><span class="orca-avatar orca-avatar--s" aria-hidden="true">GH</span><span>Grace Hopper</span><span class="orca-attendee__resp orca-attendee__resp--yes">{% icon "success" size="xs" %}Going</span></li>
  <li class="orca-attendee"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AT</span><span>Alan Turing</span><span class="orca-attendee__resp orca-attendee__resp--maybe">{% icon "help" size="xs" %}Maybe</span></li>
  <li class="orca-attendee"><span class="orca-avatar orca-avatar--s" aria-hidden="true">KJ</span><span>Katherine Johnson</span><span class="orca-attendee__resp orca-attendee__resp--waiting">{% icon "hourglass" size="xs" %}Waiting</span></li></ul></div>""")],
    guide=["Attendee list"],
))

add(Pattern(
    "invitation-response-bar", "Invitation response bar", C,
    "A bar on an invitation asking 'Going?' with Yes, Maybe and No, showing the current answer.",
    why="Answering an invitation should be one click where the question is asked (Fitts's law); the pressed state shows the current answer and can be changed (Practical UI B03).",
    when=["On an event the viewer is invited to: detail panel, popover, invitation email landing page."],
    how=["`<div class=\"orca-rsvp\">` with `.orca-rsvp__question` and a segmented group of three buttons using `aria-pressed`; post the answer and update the attendee list.",
         "Offer 'Add a note' only after answering."],
    classes=[".orca-rsvp", ".orca-rsvp__question"],
    laws=["fitts", "B03"],
    uses=["button-group", "choice-group"],
    examples=[("Going?", """<div class="orca-rsvp" style="max-width: 32rem"><span class="orca-rsvp__question">Going?</span><div class="orca-segmented orca-segmented--dense" role="group" aria-label="Your answer"><button class="orca-segmented__item" type="button" aria-pressed="true">Yes</button><button class="orca-segmented__item" type="button" aria-pressed="false">Maybe</button><button class="orca-segmented__item" type="button" aria-pressed="false">No</button></div></div>""")],
    guide=["Invitation response bar"],
))
