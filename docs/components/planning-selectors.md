# Planning selectors

Controls that choose days, repeats, reminders, periods, granularity and calendar views.

## Weekday selector

`id: weekday-selector` · level: component · source: ORCA

Seven weekday toggles with presets for weekdays, every day and clear.

Built from: `weekday-toggle`, `tag`

### General description

A weekday selector lets people pick one or more days of the week, usually with seven toggles and shortcuts for common sets.

#### Use cases

- Choosing which days an event repeats.
- Setting opening days or shift patterns.
- Picking days for a schedule or report.

#### When not to use it

- Choosing a single date; use a date picker.
- Picking one day only; use a select or radio group.

#### Best practices

- Offer presets such as weekdays and every day.
- Start the week on the local first day.
- Give each day a full accessible name.
- Show clearly which days are selected.

### When to use

- Repeat on days, opening days, shift patterns.

### How to use

- `.orca-field` with a weekday-toggle fieldset (id) and `.orca-presets` of tags with `data-orca-weekdays="mon,tue,wed,thu,fri"` and `aria-controls` pointing at the fieldset.
- Start on the locale's first weekday.

#### Example: Days

```django
<div class="orca-field">
  <fieldset class="orca-weekday-toggles" id="ws-days">
    <legend class="orca-label">Open on</legend>
    <label class="orca-weekday">
      <input type="checkbox" name="d" value="mon" checked>
      <span aria-hidden="true">M</span>
      <span class="orca-sr-only">Monday</span>
    </label>
    <label class="orca-weekday">
      <input type="checkbox" name="d" value="tue" checked>
      <span aria-hidden="true">T</span>
      <span class="orca-sr-only">Tuesday</span>
    </label>
    <label class="orca-weekday">
      <input type="checkbox" name="d" value="wed" checked>
      <span aria-hidden="true">W</span>
      <span class="orca-sr-only">Wednesday</span>
    </label>
    <label class="orca-weekday">
      <input type="checkbox" name="d" value="thu" checked>
      <span aria-hidden="true">T</span>
      <span class="orca-sr-only">Thursday</span>
    </label>
    <label class="orca-weekday">
      <input type="checkbox" name="d" value="fri" checked>
      <span aria-hidden="true">F</span>
      <span class="orca-sr-only">Friday</span>
    </label>
    <label class="orca-weekday">
      <input type="checkbox" name="d" value="sat">
      <span aria-hidden="true">S</span>
      <span class="orca-sr-only">Saturday</span>
    </label>
    <label class="orca-weekday">
      <input type="checkbox" name="d" value="sun">
      <span aria-hidden="true">S</span>
      <span class="orca-sr-only">Sunday</span>
    </label>
  </fieldset>
  <div class="orca-presets" role="group" aria-label="Day presets" style="margin-top: var(--orca-space-8)">
    <button class="orca-tag" type="button" aria-pressed="true" data-orca-weekdays="mon,tue,wed,thu,fri" aria-controls="ws-days">Weekdays</button>
    <button class="orca-tag" type="button" aria-pressed="false" data-orca-weekdays="mon,tue,wed,thu,fri,sat,sun" aria-controls="ws-days">Every day</button>
    <button class="orca-tag" type="button" aria-pressed="false" data-orca-weekdays="" aria-controls="ws-days">Clear</button>
  </div>
</div>
```

**Classes:** `.orca-presets`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Weekday selector

---

## Recurrence selector

`id: recurrence-selector` · level: component · source: ORCA

A repeat select with common rules and a Custom option that reveals interval, days and end.

Built from: `recurrence-select`, `weekday-toggle`, `number-input`, `radio`

### General description

A recurrence selector lets people set how an event repeats, with common choices like daily or weekly and a custom option for complex rules.

#### Use cases

- Repeating calendar events and tasks.
- Scheduling recurring reports or runs.
- Setting repeating billing or reminders.

#### When not to use it

- One-off events; do not show repeat options.
- Showing every custom field up front; reveal them only when needed.

#### Best practices

- Offer the most common rules first.
- Name options with the real day, such as 'Weekly on Thursday'.
- Summarize the custom rule in words.
- Let people choose when the repeat ends.

### When to use

- Repeating events, runs and reports.

### How to use

- `<select class="orca-select" data-orca-reveal="custom-id" data-orca-reveal-value="custom">` with recurrence options; a hidden `.orca-recurrence__custom` panel with: every N (number) + unit (select), weekday toggles, and ends (never, on date, after N times) as a radio group.
- Name options with the real day from the start date ('Weekly on Thursday') and summarise the custom rule in words below.

#### Example: Recurrence

```django
<div class="orca-field" style="max-width: 30rem">
  <label class="orca-label" for="rs-sel">Repeat</label>
  <select class="orca-select" id="rs-sel" data-orca-reveal="rs-custom" data-orca-reveal-value="custom">
    <option>Does not repeat</option>
    <option>Daily</option>
    <option>Every weekday (Monday to Friday)</option>
    <option>Weekly on Thursday</option>
    <option value="custom" selected>Custom…</option>
  </select>
  <div class="orca-recurrence__custom" id="rs-custom">
    <div class="orca-row">
      <label for="rs-n">Every</label>
      <input class="orca-input orca-input--w4" id="rs-n" type="number" min="1" value="2">
      <select class="orca-select" aria-label="Unit" style="width: auto">
        <option>days</option>
        <option selected>weeks</option>
        <option>months</option>
      </select>
    </div>
    <fieldset class="orca-weekday-toggles">
      <legend class="orca-label">On</legend>
      <label class="orca-weekday">
        <input type="checkbox" name="d" value="mon" checked>
        <span aria-hidden="true">M</span>
        <span class="orca-sr-only">Monday</span>
      </label>
      <label class="orca-weekday">
        <input type="checkbox" name="d" value="tue" checked>
        <span aria-hidden="true">T</span>
        <span class="orca-sr-only">Tuesday</span>
      </label>
      <label class="orca-weekday">
        <input type="checkbox" name="d" value="wed" checked>
        <span aria-hidden="true">W</span>
        <span class="orca-sr-only">Wednesday</span>
      </label>
      <label class="orca-weekday">
        <input type="checkbox" name="d" value="thu" checked>
        <span aria-hidden="true">T</span>
        <span class="orca-sr-only">Thursday</span>
      </label>
      <label class="orca-weekday">
        <input type="checkbox" name="d" value="fri" checked>
        <span aria-hidden="true">F</span>
        <span class="orca-sr-only">Friday</span>
      </label>
      <label class="orca-weekday">
        <input type="checkbox" name="d" value="sat">
        <span aria-hidden="true">S</span>
        <span class="orca-sr-only">Saturday</span>
      </label>
      <label class="orca-weekday">
        <input type="checkbox" name="d" value="sun">
        <span aria-hidden="true">S</span>
        <span class="orca-sr-only">Sunday</span>
      </label>
    </fieldset>
    <fieldset class="orca-choice-group">
      <legend class="orca-label">Ends</legend>
      <div class="orca-choice-group__items">
        <label class="orca-radio"><input type="radio" name="rs-end" checked><span class="orca-radio__dot"></span>Never</label>
        <label class="orca-radio"><input type="radio" name="rs-end"><span class="orca-radio__dot"></span>After 10 times</label>
      </div>
    </fieldset>
    <p class="orca-small orca-muted">Every 2 weeks on weekdays, no end date.</p>
  </div>
</div>
```

**Classes:** `.orca-recurrence__custom`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI S04: Reveal secondary information when needed; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Recurrence selector

---

## Reminder selector

`id: reminder-selector` · level: component · source: ORCA

One or more reminder offsets, each removable, with an Add reminder button.

Built from: `reminder-select`, `add-row-button`, `remove-row-button`

### General description

A reminder selector lets people choose how long before an event or deadline they are notified, and add several reminders.

#### Use cases

- Setting alerts before events.
- Adding notifications to tasks and deadlines.
- Offering more than one reminder for one item.

#### When not to use it

- Requiring a reminder; make it optional.
- Free-typed times when standard offsets suffice.

#### Best practices

- Offer standard time offsets.
- Let people add and remove reminders.
- Default to the last choice.
- Cap the number of reminders.

### When to use

- Events, deadlines and tasks with notifications.

### How to use

- `<ul class="orca-reminders" id=…>` of `<li data-orca-row>` with a reminder select and a remove icon button; an add-row button with a `<template>`.
- Default to the user's last choice; at most five reminders.

#### Example: Reminders

```django
<p class="orca-label">Reminders</p>
<ul class="orca-reminders" id="rm-list">
  <li data-orca-row>
    <select class="orca-select" aria-label="Reminder 1">
      <option>At time of event</option>
      <option selected>15 minutes before</option>
      <option>1 hour before</option>
      <option>1 day before</option>
    </select>
    <button class="orca-icon-button" type="button" aria-label="Remove reminder 15 minutes before" data-orca-remove-row>
      {% icon "close" %}
    </button>
  </li>
</ul>
<template id="rm-tpl">
  <li data-orca-row>
    <select class="orca-select" aria-label="Reminder">
      <option>At time of event</option>
      <option>15 minutes before</option>
      <option selected>1 hour before</option>
      <option>1 day before</option>
    </select>
    <button class="orca-icon-button" type="button" aria-label="Remove reminder" data-orca-remove-row>
      {% icon "close" %}
    </button>
  </li>
</template>
<button class="orca-button orca-button--ghost" type="button" data-orca-add-row="rm-tpl" aria-controls="rm-list" style="margin-top: var(--orca-space-8)">
  {% icon "plus" %}
  Add reminder
</button>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Formset

```python
# videos/forms.py
from django import forms

from .models import Reminder, Video

ReminderFormSet = forms.inlineformset_factory(
    Video, Reminder, fields=["minutes_before", "method"], extra=0, can_delete=True,
)


# videos/views.py
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReminderFormSet
from .models import Video


def edit_reminders(request, pk):
    video = get_object_or_404(Video, pk=pk)
    formset = ReminderFormSet(request.POST or None, instance=video, prefix="reminders")
    if request.method == "POST" and formset.is_valid():
        formset.save()
        return redirect("video-detail", pk=video.pk)
    # Template: {{ formset.management_form }}, one [data-orca-row] per form, and a <template id="reminder-row">
    # holding {{ formset.empty_form }} (its names contain __prefix__). The add-row button points at it with
    # data-orca-add-row="reminder-row" and data-orca-total="id_reminders-TOTAL_FORMS".
    return render(request, "videos/reminders.html", {"video": video, "formset": formset})
```

**Classes:** `.orca-reminders`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Jakob's law: work the way products people already know work; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Reminder selector

---

## Period selector

`id: period-selector` · level: component · source: ORCA

A segmented choice of Today, This week, This month and Custom, revealing a date range for Custom.

Built from: `date-range-picker`, `date-label`

### General description

A period selector lets people choose a time range for data, such as today, this week or a custom range.

#### Use cases

- Filtering reports and dashboards by time.
- Switching between common time windows.
- Choosing a custom date range.

#### When not to use it

- Picking one exact date; use a date picker.
- Long lists of periods; use a select.

#### Best practices

- Show the common periods as one visible set.
- Print the actual dates that result.
- Make the selected period obvious.
- Keep the custom option for exceptions.

### When to use

- Report and dashboard period filters.

### How to use

- Server-rendered links `<nav class="orca-segmented" aria-label="Period">` with `aria-current="page"`, or a radio fieldset.
- Custom shows a date-range picker; always print the resolved dates below ('2–8 November 2026').

#### Example: Period

```django
<div class="orca-stack" style="align-items: flex-start">
  <nav class="orca-segmented" aria-label="Period">
    <a class="orca-segmented__item" href="#">Today</a>
    <a class="orca-segmented__item" href="#" aria-current="page">This week</a>
    <a class="orca-segmented__item" href="#">This month</a>
    <a class="orca-segmented__item" href="#">Custom</a>
  </nav>
  <p class="orca-small orca-muted"><time datetime="2026-11-02">2</time>–<time datetime="2026-11-08">8 November 2026</time></p>
</div>
```

**Classes:** `.orca-segmented`, `.orca-segmented__item`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI R11: Visible choices for small sets; Practical UI S04: Reveal secondary information when needed

**ORCA guide items covered:** Period selector

---

## Granularity selector

`id: granularity-selector` · level: component · source: Tangerine

A segmented choice of how data is grouped: hour, day, week or month.

Built from: `radio`

### General description

A granularity selector lets people choose how time-based data is grouped, such as by hour, day, week or month.

#### Use cases

- Changing the time grouping of a chart.
- Summarizing a report by week or month.
- Zooming between detail and overview.

#### When not to use it

- Data with no time dimension; do not offer it.
- Offering groupings that would give unreadable results.

#### Best practices

- Place it next to the chart it changes.
- Disable choices that make no sense for the period.
- Explain why a choice is unavailable.
- Choose a sensible default.

### When to use

- Charts and reports with time on one axis.

### How to use

- `<fieldset class="orca-segmented orca-segmented--dense">` with a hidden legend and radios (Hour, Day, Week, Month); disable options that give too many or too few points and say why in a tooltip or help text.
- Keep it next to the chart it changes.

#### Example: Granularity

```django
<fieldset class="orca-segmented orca-segmented--dense">
  <legend class="orca-sr-only">Group by</legend>
  <label class="orca-segmented__item"><input type="radio" name="gr" value="hour">Hour</label>
  <label class="orca-segmented__item"><input type="radio" name="gr" value="day" checked>Day</label>
  <label class="orca-segmented__item"><input type="radio" name="gr" value="week">Week</label>
  <label class="orca-segmented__item"><input type="radio" name="gr" value="month">Month</label>
</fieldset>
```

**Classes:** `.orca-segmented`, `.orca-segmented--dense`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Practical UI L14: Reduce travel between related actions; Practical UI B07: Explain necessary disabled states

**ORCA guide items covered:** Granularity selector

---

## Calendar view switcher

`id: calendar-view-switcher` · level: component · source: ORCA

Day, Week, Month and Agenda views as a segmented control.

Built from: `button`

### General description

A calendar view switcher lets people change how a calendar displays time, such as day, week, month or agenda.

#### Use cases

- Switching between detailed and overview views of a calendar.
- Viewing a list of upcoming events.
- Adapting to different screen sizes.

#### When not to use it

- Switching between unrelated pages; use tabs or navigation.
- Offering unusual views people do not expect.

#### Best practices

- Keep the selected date when switching views.
- Use the standard view names.
- Mark the current view clearly.
- Use the agenda view by default on phones.

### When to use

- Calendar headers.

### How to use

- `<nav class="orca-segmented orca-segmented--dense" aria-label="View">` of links with `aria-current="page"` on the current view; keep the selected date when switching.
- On phones default to Agenda; Week becomes 3 days.

#### Example: Views

```django
<nav class="orca-segmented orca-segmented--dense" aria-label="Calendar view">
  <a class="orca-segmented__item" href="#">Day</a>
  <a class="orca-segmented__item" href="#" aria-current="page">Week</a>
  <a class="orca-segmented__item" href="#">Month</a>
  <a class="orca-segmented__item" href="#">Agenda</a>
</nav>
```

**Classes:** `.orca-segmented`

**Principles applied:** Jakob's law: work the way products people already know work; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Calendar view switcher (day, week, month, agenda)

---

## Preset buttons

`id: preset-buttons` · level: component · source: ORCA

A row of one-tap choices (Today, Weekdays, This week, Next 7 days) that fill a more detailed control.

Built from: `tag`

### General description

Preset buttons are a row of one-tap shortcuts that fill in a more detailed control with common values.

#### Use cases

- Choosing common date ranges.
- Choosing common sets of days.
- Filling in typical durations.

#### When not to use it

- Replacing a detailed control entirely; keep it for exceptions.
- Long lists of presets; use a select.

#### Best practices

- Offer only a few presets.
- Name them by outcome.
- Show which preset matches the current value.
- Keep the detailed control available.

### When to use

- Next to date ranges, weekday toggles and durations.

### How to use

- `<div class="orca-presets" role="group" aria-label=…>` of `<button class="orca-tag" type="button" aria-pressed>`; the preset that matches the current value is pressed.
- Four presets at most; name them by outcome.

#### Example: Presets

```django
<div class="orca-presets" role="group" aria-label="Quick periods">
  <button class="orca-tag" type="button" aria-pressed="false">Today</button>
  <button class="orca-tag" type="button" aria-pressed="false">Weekdays</button>
  <button class="orca-tag" type="button" aria-pressed="true">This week</button>
  <button class="orca-tag" type="button" aria-pressed="false">Next 7 days</button>
</div>
```

**Classes:** `.orca-presets`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI S08: Simplify decisions: remove, group, stage, recommend

**ORCA guide items covered:** Preset buttons (Today, Weekdays, This week, Next 7 days)

---

## Calendar navigation

`id: calendar-navigation` · level: component · source: ORCA

Previous, Today and Next buttons with the visible period's label.

Built from: `icon-button`, `button`, `planning-icons`

### General description

Calendar navigation is a group of controls for moving to the previous or next period or jumping back to today, with a label for the period shown.

#### Use cases

- Moving through weeks or months in a calendar.
- Stepping through report periods.
- Returning to today quickly.

#### When not to use it

- Jumping far in time; add a date picker.
- Leaving out the visible period label.

#### Best practices

- Show the current period label.
- Name arrows by period, such as 'Previous week'.
- Disable Today when it is already visible.
- Announce label changes politely to screen readers.

### When to use

- Calendar headers, schedule and report headers that move by period.

### How to use

- `<div class="orca-cal-nav">` with an icon button (Previous week), a 'Today' button, an icon button (Next week), and `<h2 class="orca-cal-nav__label" aria-live="polite">`.
- Name the arrows with the period ('Previous week'); disable Today when today is visible.

#### Example: Navigation

```django
<div class="orca-cal-nav">
  <a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Previous week">
    {% icon "chevron-left" %}
  </a>
  <a class="orca-button" href="#">Today</a>
  <a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Next week">
    {% icon "chevron-right" %}
  </a>
  <h2 class="orca-cal-nav__label" aria-live="polite">2–8 November 2026</h2>
</div>
```

**Classes:** `.orca-cal-nav`, `.orca-cal-nav__label`

**Principles applied:** Jakob's law: work the way products people already know work; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Calendar navigation (previous, today, next)

---
