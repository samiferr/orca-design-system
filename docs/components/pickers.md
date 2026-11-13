# Date and time pickers

Native date and time inputs plus shortcuts, ranges, time zones and a month grid. Native comes first: every device already knows how to pick a date.

## Date picker

`id: date-picker` · level: component · source: ORCA

A native date input with shortcut buttons for common dates.

Built from: `date-input`, `tag`, `help-text`

### General description

A field for choosing a date, usually through the browser's calendar or typing. Shortcuts can speed up the most common choices.

#### Use cases

- Due dates, start dates and report dates.
- Booking or scheduling a single day.
- Filtering by a date.

#### When not to use it

- Birthdates and other dates far in the past; use separate day, month and year fields.
- Choosing a period; use a date range picker.

#### Best practices

- Use the native date input where possible.
- Label the field and state the allowed range.
- Offer shortcuts like Today and Tomorrow.
- Allow typing as well as picking.
- Show the date format people should use.

### When to use

- One date near today, such as a report, due or start date.

### When not to use

- Distant past dates people know by heart: use the split date input.

### How to use

- `.orca-field` with label, help and `<input class="orca-input" type="date">`, then `.orca-shortcuts` of tags `<button class="orca-tag" type="button" aria-pressed="false" data-orca-set-date="0" aria-controls="input-id">Today</button>` (+1 Tomorrow, +7 In a week).
- Set `min`/`max` and say the allowed range in the help text.
- Django: `{% orca_field form.due %}` renders a DateField as a native date input.

#### Example: Due date

```django
<div class="orca-field" style="max-width: 20rem">
  <label class="orca-label" for="dp-1">Due date</label>
  <input class="orca-input" type="date" id="dp-1" name="due">
  <div class="orca-shortcuts" role="group" aria-label="Quick dates">
    <button class="orca-tag" type="button" aria-pressed="false" data-orca-set-date="0" aria-controls="dp-1">Today</button>
    <button class="orca-tag" type="button" aria-pressed="false" data-orca-set-date="1" aria-controls="dp-1">Tomorrow</button>
    <button class="orca-tag" type="button" aria-pressed="false" data-orca-set-date="7" aria-controls="dp-1">In a week</button>
  </div>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Form

```python
# videos/forms.py
from django import forms


class PublishForm(forms.Form):
    # orca_field renders a DateField as a native <input type="date"> with its label and help.
    publish_on = forms.DateField(label="Publish on", help_text="The video goes live at 08:00 that day.")
```

**Classes:** `.orca-field`, `.orca-shortcuts`

**Principles applied:** Jakob's law: work the way products people already know work; Tesler's law: move unavoidable complexity from the user to the system; Fitts's law: big, close, well-spaced targets are faster and safer

**Related:** `mini-calendar`, `date-range-picker`

**ORCA guide items covered:** Date picker

---

## Time picker

`id: time-picker` · level: component · source: ORCA

A labelled native time input with a step and its timezone.

Built from: `time-input`, `timezone-label`

### General description

A field for choosing a time of day. It follows the person's 12 or 24 hour habit and often moves in set steps.

#### Use cases

- Start times and reminders.
- Opening hours.
- Scheduling appointments.

#### When not to use it

- Lengths of time such as 90 minutes; use a duration picker.
- Both a date and a time; use a date and time picker.

#### Best practices

- Use the native time input.
- Use steps such as 15 minutes when exact minutes do not matter.
- Show the time zone when it could be unclear.
- Label the field clearly.

### When to use

- Start times, reminder times, opening hours.

### How to use

- `.orca-field` > label + `.orca-row` containing `<input class="orca-input" type="time" step="900">` and a timezone label.
- Leave out the timezone label when all times on the page use the reader's zone.

#### Example: Opening time

```django
<div class="orca-field" style="max-width: 20rem">
  <label class="orca-label" for="tp-1">Opens at</label>
  <div class="orca-row">
    <input class="orca-input" type="time" id="tp-1" value="08:30" step="900" style="max-width: 9rem">
    <abbr class="orca-tz" title="Europe/Paris (UTC+01:00)">CET</abbr>
  </div>
</div>
```

**Classes:** `.orca-field`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Time picker

---

## Date-time picker

`id: datetime-picker` · level: component · source: ORCA

A date field and a time field in one group, with the timezone.

Built from: `date-input`, `time-input`, `timezone-label`

### General description

A pair of fields for a date and a time, together describing one moment. Keeping them separate makes each easy to fill in and correct.

#### Use cases

- When a task starts or access expires.
- Scheduling a message or publication.
- Setting a deadline with a time.

#### When not to use it

- Date only; use a date picker.
- A start and an end; use a date range picker.

#### Best practices

- Group the date and time under one label.
- Show the time zone.
- Store the moment in a standard form such as UTC.
- Check that the moment is allowed, for example not in the past.

### When to use

- A single moment, such as when a run starts or access expires.

### How to use

- `<fieldset class="orca-inline-fields">` with a legend, a date field and a time field (`.orca-field`), and a timezone label.
- Combine on the server in the site's timezone; store UTC.

#### Example: Run start

```django
<fieldset class="orca-inline-fields">
  <legend class="orca-label">Start the run</legend>
  <div class="orca-field">
    <label class="orca-label" for="dtp-d">Date</label>
    <input class="orca-input" type="date" id="dtp-d" value="2026-11-07">
  </div>
  <div class="orca-field">
    <label class="orca-label" for="dtp-t">Time</label>
    <input class="orca-input" type="time" id="dtp-t" value="07:00" step="900">
  </div>
  <abbr class="orca-tz orca-inline-fields__sep" title="Europe/Paris">CET</abbr>
</fieldset>
```

**Classes:** `.orca-inline-fields`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Date-time picker

---

## Date-range picker

`id: date-range-picker` · level: component · source: ORCA

Start and end dates with presets, always in order, and the length in days.

Built from: `date-input`, `preset-buttons`

### General description

A control to choose a start and end date. Presets like Last 7 days make common periods quick, and the end stays after the start.

#### Use cases

- Report periods.
- Booking time off or travel dates.
- Filtering lists by date.

#### When not to use it

- A single day; use a date picker.
- Ranges of time within one day; use a time range input.

#### Best practices

- Offer common presets.
- Keep the end date on or after the start date.
- Show the length of the chosen range.
- Label the start and the end clearly.
- Say whether the end date is included.

### When to use

- Report periods, time off, exceptions, filters.

### How to use

- `<fieldset class="orca-inline-fields" data-orca-range>` with a legend, a From date field, a To date field and `<p class="orca-inline-fields__note" data-orca-range-output aria-live="polite">`.
- Presets go in a row above it (Today, This week, Last 7 days, This month).
- orca.js sets the end field's `min` to the start and moves the end when needed.

#### Example: Report period

```django
<fieldset class="orca-inline-fields" data-orca-range>
  <legend class="orca-label">Report period</legend>
  <div class="orca-field">
    <label class="orca-label" for="dr-a">From</label>
    <input class="orca-input" type="date" id="dr-a" value="2026-11-02">
  </div>
  <span class="orca-inline-fields__sep" aria-hidden="true">–</span>
  <div class="orca-field">
    <label class="orca-label" for="dr-b">To</label>
    <input class="orca-input" type="date" id="dr-b" value="2026-11-08">
  </div>
  <p class="orca-inline-fields__note" data-orca-range-output aria-live="polite">7 days</p>
</fieldset>
```

**Classes:** `.orca-inline-fields`, `.orca-inline-fields__note`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Postel's law: accept varied input, output reliable and accessible UI; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Date-range picker

---

## Time-range input (start and end)

`id: time-range-input` · level: component · source: ORCA

Start and end times with the duration, noting when it ends the next day.

Built from: `time-input`, `duration-label`

### General description

Two time fields for a start and an end, usually with the resulting length. It helps people set periods within a day, including overnight ones.

#### Use cases

- Opening hours.
- Work shifts.
- Booking windows.

#### When not to use it

- Periods across several days; use a date range picker.
- Only a length of time; use a duration picker.

#### Best practices

- Show the length that results.
- Say clearly when the end is the next day.
- Validate on the server as well.
- Label start and end clearly.
- Use steps that suit the task, such as 15 minutes.

### When to use

- Opening hours, shifts, booking windows.

### How to use

- `<fieldset class="orca-inline-fields" data-orca-range>` with Start and End time fields and an `orca-inline-fields__note` output.
- Also validate on the server; decide whether overnight ranges are allowed and say so.

#### Example: Shift

```django
<fieldset class="orca-inline-fields" data-orca-range>
  <legend class="orca-label">Shift</legend>
  <div class="orca-field">
    <label class="orca-label" for="trg-a">Start</label>
    <input class="orca-input" type="time" id="trg-a" value="22:00" step="900">
  </div>
  <span class="orca-inline-fields__sep" aria-hidden="true">–</span>
  <div class="orca-field">
    <label class="orca-label" for="trg-b">End</label>
    <input class="orca-input" type="time" id="trg-b" value="06:00" step="900">
  </div>
  <p class="orca-inline-fields__note" data-orca-range-output aria-live="polite">8 h, ends the next day</p>
</fieldset>
```

**Classes:** `.orca-inline-fields`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Time-range input (start and end)

---

## Duration picker

`id: duration-picker` · level: component · source: ORCA

Hours and minutes fields with quick choices for common durations.

Built from: `duration-input`, `tag`

### General description

A control for entering a length of time, such as hours and minutes. Quick choices cover usual lengths while fields allow exact values.

#### Use cases

- Meeting lengths.
- Timeouts and retention periods.
- Reminder offsets.

#### When not to use it

- A specific time of day; use a time picker.
- A start and end; use a time range input.

#### Best practices

- Show units next to each field.
- Offer common lengths as quick buttons.
- Accept values like 90 minutes and tidy them up.
- Set sensible minimum and maximum limits.

### When to use

- Meeting lengths, retention, timeouts, reminder offsets.

### How to use

- `.orca-field` containing a duration input (two parts with addons) and `.orca-shortcuts` tags (15 min, 30 min, 1 h).
- Shortcuts set both parts by script or server round-trip; normalise minutes over 59 on the server.

#### Example: Meeting length

```django
<div class="orca-field">
  <fieldset class="orca-duration" style="border: 0; padding: 0; margin: 0">
    <legend class="orca-label">Length</legend>
    <span class="orca-duration__part">
      <input class="orca-input" type="number" min="0" value="0" aria-label="Hours">
      <span class="orca-addon">h</span>
    </span>
    <span class="orca-duration__part">
      <input class="orca-input" type="number" min="0" step="5" value="30" aria-label="Minutes">
      <span class="orca-addon">min</span>
    </span>
  </fieldset>
  <div class="orca-shortcuts" role="group" aria-label="Common lengths">
    <button class="orca-tag" type="button" aria-pressed="false">15 min</button>
    <button class="orca-tag" type="button" aria-pressed="true">30 min</button>
    <button class="orca-tag" type="button" aria-pressed="false">1 h</button>
  </div>
</div>
```

**Classes:** `.orca-shortcuts`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Postel's law: accept varied input, output reliable and accessible UI; Practical UI R13: Steppers for small numeric changes

**ORCA guide items covered:** Duration picker

---

## Timezone selector

`id: timezone-selector` · level: component · source: Tangerine

A timezone select with a 'Use my timezone' button and the current offset.

Built from: `timezone-select`, `button`

### General description

A control for choosing a time zone, often with a button to use the person's own. It prevents mix-ups when schedules cross regions.

#### Use cases

- Account or site settings.
- Scheduling events for people in other places.
- Reports that depend on local time.

#### When not to use it

- Sites where everything uses one fixed zone; just state the zone.
- Guessing the zone silently; let people confirm it.

#### Best practices

- Detect the person's zone and let them change it.
- Show the zone's current offset or local time.
- Make the list searchable and use readable place names.
- Store the zone by its standard name.

### When to use

- Site, video and profile settings.

### How to use

- `.orca-field` with label, help showing the current local time, a `.orca-row` with `<select class="orca-select">{% orca_timezone_options current %}</select>` and a ghost button `data-orca-detect-tz aria-controls="select-id"`.
- Store the IANA name.

#### Example: Site timezone

```django
<div class="orca-field" style="max-width: 30rem">
  <label class="orca-label" for="tzs">Site timezone</label>
  <p class="orca-help" id="tzs-help">Reports and schedules use this zone.</p>
  <div class="orca-row" style="flex-wrap: nowrap">
    <select class="orca-select" id="tzs" aria-describedby="tzs-help">
      {% orca_timezone_options "Europe/Paris" %}
    </select>
    <button class="orca-button orca-button--ghost" type="button" data-orca-detect-tz aria-controls="tzs">Use my timezone</button>
  </div>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Form and middleware

```python
# accounts/forms.py — {% orca_field form.timezone %} with the "Use my time zone" button
import zoneinfo

from django import forms


class TimezoneForm(forms.Form):
    timezone = forms.ChoiceField(choices=[(z, z.replace("_", " ")) for z in sorted(zoneinfo.available_timezones())])


# accounts/middleware.py — add "accounts.middleware.TimezoneMiddleware" to MIDDLEWARE
from django.utils import timezone


class TimezoneMiddleware:
    """Show every date and time in the person's own time zone."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        name = request.session.get("timezone")
        if name:
            timezone.activate(zoneinfo.ZoneInfo(name))
        else:
            timezone.deactivate()
        return self.get_response(request)
```

**Classes:** `.orca-field`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Timezone selector

---

## Month and year switcher

`id: month-year-switcher` · level: component · source: ORCA

Previous and next buttons around a month select and a year select.

Built from: `icon-button`, `select`, `month-name`, `year-label`

### General description

Buttons and selects for moving a calendar or report between months and years. Arrows handle small steps and the selects allow big jumps.

#### Use cases

- Calendar headers.
- Monthly reports.
- Browsing archives by month.

#### When not to use it

- Picking one date to submit; use a date picker.
- Browsing only a few days; use simple next and previous links.

#### Best practices

- Name the previous and next buttons with the month they lead to.
- Show the current month and year clearly.
- Limit years to a useful range.
- Let people return to today quickly.

### When to use

- Calendars and reports browsed by month, especially far from today.

### How to use

- `<div class="orca-month-switcher" role="group" aria-label="Month">` with a previous icon button, a month select, a year select and a next icon button.
- Server-rendered: a GET form with `data-orca-autosubmit` on the selects and links for the arrows.

#### Example: Switcher

```django
<form class="orca-month-switcher" role="group" aria-label="Month" onsubmit="return false">
  <a class="orca-icon-button" href="#" aria-label="Previous month, October 2026">
    {% icon "chevron-left" %}
  </a>
  <select class="orca-select orca-select--dense" aria-label="Month">
    <option>October</option>
    <option selected>November</option>
    <option>December</option>
  </select>
  <select class="orca-select orca-select--dense" aria-label="Year">
    <option>2025</option>
    <option selected>2026</option>
    <option>2027</option>
  </select>
  <a class="orca-icon-button" href="#" aria-label="Next month, December 2026">
    {% icon "chevron-right" %}
  </a>
</form>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py — the switcher submits ?month=2026-11 on change
import datetime as dt

from django.utils import timezone


def chosen_month(request):
    value = request.GET.get("month", "")
    try:
        return dt.date.fromisoformat(value + "-01")
    except ValueError:
        return timezone.localdate().replace(day=1)
```

**Classes:** `.orca-month-switcher`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Month and year switcher

---

## Mini calendar

`id: mini-calendar` · level: component · source: Tangerine

A server-rendered month grid with today, selected, outside, weekend and holiday days.

Built from: `day-number`, `weekday-name`, `today-marker`, `selected-day-marker`, `outside-day-marker`, `weekend-marker`, `holiday-marker`, `event-dot`

### General description

A small month grid that shows dates in context. Days can be marked as today, selected, holidays or days with events.

#### Use cases

- Sidebars on calendar pages.
- Filtering a list by day.
- Showing which days have events.

#### When not to use it

- Picking a single date in a form; a date input is simpler.
- Detailed schedules with times; use a full calendar view.

#### Best practices

- Mark today and the selected day clearly, with more than colour.
- Name each day with its full date for screen readers.
- Start the week on the day people expect.
- Make day cells large enough to tap.

### When to use

- Calendar sidebars, date filters, marking days that have events.

### When not to use

- Picking one date in a form: use the simpler native date input.

### How to use

- `{% orca_mini_calendar month selected=day url="/events/?day={date}" nav_url="?month={month}" events=event_days holidays=holiday_map week_numbers=True %}`.
- Without `url`, days render as buttons with `data-date` for your own script.
- Each day is named by its full date plus any today, holiday or 'has events' note.

#### Example: November 2026

```django
{% orca_mini_calendar "2026-11-01" selected="2026-11-12" today="2026-11-06" url="#{date}" nav_url="#{month}" events="2026-11-04" week_numbers=True %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
from django.utils import timezone

month = chosen_month(self.request)   # see Month and year switcher
days_with_events = Event.objects.filter(starts_at__year=month.year, starts_at__month=month.month)
ctx.update(
    month=month,
    today=timezone.localdate(),
    event_days=sorted({e.starts_at.date().isoformat() for e in days_with_events}),
)
# Template: {% orca_mini_calendar month selected=day today=today url="/calendar/{date}/" events=event_days %}
```

**Classes:** `.orca-mini-calendar`, `.orca-mini-calendar__head`, `.orca-calendar`, `.orca-calendar__week`

**Principles applied:** Jakob's law: work the way products people already know work; Tesler's law: move unavoidable complexity from the user to the system; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Mini calendar

---
