from ..registry import add, category
from . import Component

C = category(
    "planning-selectors", "Planning selectors",
    "Controls that choose days, repeats, reminders, periods, granularity and calendar views.",
    level="component",
)

WEEK = "".join(
    f'<label class="orca-weekday"><input type="checkbox" name="d" value="{v}"{" checked" if on else ""}><span aria-hidden="true">{s}</span><span class="orca-sr-only">{n}</span></label>'
    for v, s, n, on in [("mon", "M", "Monday", 1), ("tue", "T", "Tuesday", 1), ("wed", "W", "Wednesday", 1), ("thu", "T", "Thursday", 1),
                        ("fri", "F", "Friday", 1), ("sat", "S", "Saturday", 0), ("sun", "S", "Sunday", 0)]
)

add(Component(
    "weekday-selector", "Weekday selector", C,
    "Seven weekday toggles with presets for weekdays, every day and clear.",
    why="Presets cover the common sets in one tap (Hick's law); the toggles stay for exceptions (Tesler's law).",
    when=["Repeat on days, opening days, shift patterns."],
    how=["`.orca-field` with a weekday-toggle fieldset (id) and `.orca-presets` of tags with `data-orca-weekdays=\"mon,tue,wed,thu,fri\"` and `aria-controls` pointing at the fieldset.",
         "Start on the locale's first weekday."],
    classes=[".orca-presets"],
    laws=["hick", "tesler"],
    uses=["weekday-toggle", "tag"],
    examples=[("Days", f"""<div class="orca-field">
  <fieldset class="orca-weekday-toggles" id="ws-days"><legend class="orca-label">Open on</legend>{WEEK}</fieldset>
  <div class="orca-presets" role="group" aria-label="Day presets" style="margin-top: var(--orca-space-8)"><button class="orca-tag" type="button" aria-pressed="true" data-orca-weekdays="mon,tue,wed,thu,fri" aria-controls="ws-days">Weekdays</button><button class="orca-tag" type="button" aria-pressed="false" data-orca-weekdays="mon,tue,wed,thu,fri,sat,sun" aria-controls="ws-days">Every day</button><button class="orca-tag" type="button" aria-pressed="false" data-orca-weekdays="" aria-controls="ws-days">Clear</button></div>
</div>""")],
    guide=["Weekday selector"],
))

add(Component(
    "recurrence-selector", "Recurrence selector", C,
    "A repeat select with common rules and a Custom option that reveals interval, days and end.",
    why="Most repeats are one of a few rules (Hick's law); the full editor appears only when chosen (Practical UI S04, Tesler's law).",
    when=["Repeating events, runs and reports."],
    how=["`<select class=\"orca-select\" data-orca-reveal=\"custom-id\" data-orca-reveal-value=\"custom\">` with recurrence options; a hidden `.orca-recurrence__custom` panel with: every N (number) + unit (select), weekday toggles, and ends (never, on date, after N times) as a radio group.",
         "Name options with the real day from the start date ('Weekly on Thursday') and summarise the custom rule in words below."],
    classes=[".orca-recurrence__custom"],
    laws=["hick", "S04", "tesler"],
    uses=["recurrence-select", "weekday-toggle", "number-input", "radio"],
    examples=[("Recurrence", f"""<div class="orca-field" style="max-width: 30rem">
  <label class="orca-label" for="rs-sel">Repeat</label>
  <select class="orca-select" id="rs-sel" data-orca-reveal="rs-custom" data-orca-reveal-value="custom"><option>Does not repeat</option><option>Daily</option><option>Every weekday (Monday to Friday)</option><option>Weekly on Thursday</option><option value="custom" selected>Custom…</option></select>
  <div class="orca-recurrence__custom" id="rs-custom">
    <div class="orca-row"><label for="rs-n">Every</label><input class="orca-input orca-input--w4" id="rs-n" type="number" min="1" value="2"><select class="orca-select" aria-label="Unit" style="width: auto"><option>days</option><option selected>weeks</option><option>months</option></select></div>
    <fieldset class="orca-weekday-toggles"><legend class="orca-label">On</legend>{WEEK}</fieldset>
    <fieldset class="orca-choice-group"><legend class="orca-label">Ends</legend><div class="orca-choice-group__items">
      <label class="orca-radio"><input type="radio" name="rs-end" checked><span class="orca-radio__dot"></span>Never</label>
      <label class="orca-radio"><input type="radio" name="rs-end"><span class="orca-radio__dot"></span>After 10 times</label></div></fieldset>
    <p class="orca-small orca-muted">Every 2 weeks on weekdays, no end date.</p>
  </div>
</div>""")],
    guide=["Recurrence selector"],
))

add(Component(
    "reminder-selector", "Reminder selector", C,
    "One or more reminder offsets, each removable, with an Add reminder button.",
    why="Standard offsets are fastest (Hick's law, Jakob's law); allowing several reminders without a fixed number of fields keeps the form small (Tesler's law).",
    when=["Events, deadlines and tasks with notifications."],
    how=["`<ul class=\"orca-reminders\" id=…>` of `<li data-orca-row>` with a reminder select and a remove icon button; an add-row button with a `<template>`.",
         "Default to the user's last choice; at most five reminders."],
    classes=[".orca-reminders"],
    laws=["hick", "jakob", "tesler"],
    uses=["reminder-select", "add-row-button", "remove-row-button"],
    examples=[("Reminders", """<p class="orca-label">Reminders</p>
<ul class="orca-reminders" id="rm-list"><li data-orca-row><select class="orca-select" aria-label="Reminder 1"><option>At time of event</option><option selected>15 minutes before</option><option>1 hour before</option><option>1 day before</option></select><button class="orca-icon-button" type="button" aria-label="Remove reminder 15 minutes before" data-orca-remove-row>{% icon "close" %}</button></li></ul>
<template id="rm-tpl"><li data-orca-row><select class="orca-select" aria-label="Reminder"><option>At time of event</option><option>15 minutes before</option><option selected>1 hour before</option><option>1 day before</option></select><button class="orca-icon-button" type="button" aria-label="Remove reminder" data-orca-remove-row>{% icon "close" %}</button></li></template>
<button class="orca-button orca-button--ghost" type="button" data-orca-add-row="rm-tpl" aria-controls="rm-list" style="margin-top: var(--orca-space-8)">{% icon "plus" %}Add reminder</button>""")],
    guide=["Reminder selector"],
))

add(Component(
    "period-selector", "Period selector", C,
    "A segmented choice of Today, This week, This month and Custom, revealing a date range for Custom.",
    why="Reports are mostly read for standard periods (Hick's law); a segmented control shows them all at once and Custom keeps the exception possible (Practical UI R11, S04).",
    when=["Report and dashboard period filters."],
    how=["Server-rendered links `<nav class=\"orca-segmented\" aria-label=\"Period\">` with `aria-current=\"page\"`, or a radio fieldset.",
         "Custom shows a date-range picker; always print the resolved dates below ('2–8 November 2026')."],
    classes=[".orca-segmented", ".orca-segmented__item"],
    laws=["hick", "R11", "S04"],
    uses=["date-range-picker", "date-label"],
    examples=[("Period", """<div class="orca-stack" style="align-items: flex-start">
  <nav class="orca-segmented" aria-label="Period"><a class="orca-segmented__item" href="#">Today</a><a class="orca-segmented__item" href="#" aria-current="page">This week</a><a class="orca-segmented__item" href="#">This month</a><a class="orca-segmented__item" href="#">Custom</a></nav>
  <p class="orca-small orca-muted"><time datetime="2026-11-02">2</time>–<time datetime="2026-11-08">8 November 2026</time></p>
</div>""")],
    guide=["Period selector"],
))

add(Component(
    "granularity-selector", "Granularity selector", C,
    "A segmented choice of how data is grouped: hour, day, week or month.",
    why="The right grouping depends on the question, so people choose it (Tesler's law); disabling options that make no sense for the period prevents empty or unreadable charts.",
    when=["Charts and reports with time on one axis."],
    how=["`<fieldset class=\"orca-segmented orca-segmented--dense\">` with a hidden legend and radios (Hour, Day, Week, Month); disable options that give too many or too few points and say why in a tooltip or help text.",
         "Keep it next to the chart it changes."],
    classes=[".orca-segmented", ".orca-segmented--dense"],
    laws=["tesler", "L14", "B07"],
    uses=["radio"],
    examples=[("Granularity", """<fieldset class="orca-segmented orca-segmented--dense"><legend class="orca-sr-only">Group by</legend>
  <label class="orca-segmented__item"><input type="radio" name="gr" value="hour">Hour</label><label class="orca-segmented__item"><input type="radio" name="gr" value="day" checked>Day</label><label class="orca-segmented__item"><input type="radio" name="gr" value="week">Week</label><label class="orca-segmented__item"><input type="radio" name="gr" value="month">Month</label>
</fieldset>""")],
    guide=["Granularity selector"], source="Tangerine",
))

add(Component(
    "calendar-view-switcher", "Calendar view switcher", C,
    "Day, Week, Month and Agenda views as a segmented control.",
    why="The four standard calendar views are a convention people know (Jakob's law); showing them all lets people switch in one click.",
    when=["Calendar headers."],
    how=["`<nav class=\"orca-segmented orca-segmented--dense\" aria-label=\"View\">` of links with `aria-current=\"page\"` on the current view; keep the selected date when switching.",
         "On phones default to Agenda; Week becomes 3 days."],
    classes=[".orca-segmented"],
    laws=["jakob", "fitts"],
    uses=["button"],
    examples=[("Views", """<nav class="orca-segmented orca-segmented--dense" aria-label="Calendar view"><a class="orca-segmented__item" href="#">Day</a><a class="orca-segmented__item" href="#" aria-current="page">Week</a><a class="orca-segmented__item" href="#">Month</a><a class="orca-segmented__item" href="#">Agenda</a></nav>""")],
    guide=["Calendar view switcher (day, week, month, agenda)"],
))

add(Component(
    "preset-buttons", "Preset buttons", C,
    "A row of one-tap choices (Today, Weekdays, This week, Next 7 days) that fill a more detailed control.",
    why="Recommending the common answers speeds decisions (Hick's law, Practical UI S08) while the detailed control stays available.",
    when=["Next to date ranges, weekday toggles and durations."],
    how=["`<div class=\"orca-presets\" role=\"group\" aria-label=…>` of `<button class=\"orca-tag\" type=\"button\" aria-pressed>`; the preset that matches the current value is pressed.",
         "Four presets at most; name them by outcome."],
    classes=[".orca-presets"],
    laws=["hick", "S08"],
    uses=["tag"],
    examples=[("Presets", """<div class="orca-presets" role="group" aria-label="Quick periods"><button class="orca-tag" type="button" aria-pressed="false">Today</button><button class="orca-tag" type="button" aria-pressed="false">Weekdays</button><button class="orca-tag" type="button" aria-pressed="true">This week</button><button class="orca-tag" type="button" aria-pressed="false">Next 7 days</button></div>""")],
    guide=["Preset buttons (Today, Weekdays, This week, Next 7 days)"],
))

add(Component(
    "calendar-navigation", "Calendar navigation", C,
    "Previous, Today and Next buttons with the visible period's label.",
    why="Stepping through periods and jumping back to today are the most frequent calendar actions; grouping them with the label shows where you are (Jakob's law, Fitts's law).",
    when=["Calendar headers, schedule and report headers that move by period."],
    how=["`<div class=\"orca-cal-nav\">` with an icon button (Previous week), a 'Today' button, an icon button (Next week), and `<h2 class=\"orca-cal-nav__label\" aria-live=\"polite\">`.",
         "Name the arrows with the period ('Previous week'); disable Today when today is visible."],
    classes=[".orca-cal-nav", ".orca-cal-nav__label"],
    laws=["jakob", "fitts"],
    uses=["icon-button", "button", "planning-icons"],
    examples=[("Navigation", """<div class="orca-cal-nav"><a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Previous week">{% icon "chevron-left" %}</a><a class="orca-button" href="#">Today</a><a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Next week">{% icon "chevron-right" %}</a><h2 class="orca-cal-nav__label" aria-live="polite">2–8 November 2026</h2></div>""")],
    guide=["Calendar navigation (previous, today, next)"],
))
