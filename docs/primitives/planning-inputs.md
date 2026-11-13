# Planning inputs

Date, time and schedule inputs. Native pickers come first: people already know them on every device.

## Date input

`id: date-input` · level: primitive · source: ORCA

A native date field (`type="date"`) with ORCA styling.

### General description

A form field for choosing one calendar date, usually with a pop-up calendar picker. It keeps dates in a consistent format.

#### Use cases

- Setting a deadline, due date or report date.
- Booking an appointment or delivery day.
- Filtering a list by a single day.

#### When not to use it

- Birth dates or dates far in the past: separate day, month and year fields are faster to type.
- A start and end together: use a date range picker.

#### Best practices

- Label the field with what the date means, not with the format.
- Set minimum and maximum dates when only some days are allowed.
- Prefill a likely default, such as today.
- Explain the accepted range in help text.

### When to use

- Picking one day, such as a deadline, report date or holiday.

### When not to use

- Dates people type faster than they pick, like birth dates: use the split date input (phase 2) or three numeric fields.

### How to use

- `<input class="orca-input" type="date" id=… name=… min=… max=…>`.
- Set `min`/`max` for the allowed range and explain it in help text.
- Prefill a sensible default (today, next working day) instead of leaving it empty (Tesler's law).
- The server always receives ISO `YYYY-MM-DD`.

### Accessibility

- Label it with the event, not the format: 'Report date', not 'dd/mm/yyyy'.

#### Example: Date

```django
<label class="orca-label" for="d1">Report date</label>
<input class="orca-input" type="date" id="d1" value="2026-11-06" max="2026-12-31">
```

**Classes:** `.orca-input[type=date]`

**Tokens:** `--orca-bg-input`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI; Tesler's law: move unavoidable complexity from the user to the system

**Related:** `time-input`, `datetime-input`

**ORCA guide items covered:** Date input

---

## Time input

`id: time-input` · level: primitive · source: ORCA

A native time field (`type="time"`).

### General description

A form field for entering a time of day, in hours and minutes. Browsers show it in the user's 12 or 24-hour style.

#### Use cases

- Choosing a start or end time for an event.
- Setting opening hours.
- Picking a time for a reminder.

#### When not to use it

- A length of time, like 90 minutes: use a duration field.
- A full date and time together: use a date-time field.

#### Best practices

- Use a sensible step, such as 15 minutes, to avoid awkward values.
- Show the timezone when users may be in a different one.
- Label the field clearly, for example 'Starts at'.
- Validate that end times come after start times.

### When to use

- Start and end times, reminder times, opening hours.

### How to use

- `<input class="orca-input" type="time" step="900">` (step in seconds: 900 = 15 minutes).
- Add a timezone label when people may be in a different zone from the place.

#### Example: Time with timezone

```django
<label class="orca-label" for="t1">Opens at</label>
<div class="orca-row">
  <input class="orca-input" type="time" id="t1" value="08:30" step="900">
  <span class="orca-tz" title="Europe/Paris">CET</span>
</div>
```

**Classes:** `.orca-input[type=time]`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Jakob's law: work the way products people already know work

**Related:** `timezone-label`

**ORCA guide items covered:** Time input

---

## Date-time input

`id: datetime-input` · level: primitive · source: ORCA

A native `datetime-local` field for one moment.

### General description

A single form field for choosing a date and a time together. It captures one exact moment without needing two separate controls.

#### Use cases

- Scheduling when a task or message should run.
- Setting when a link or offer expires.
- Recording when an incident happened.

#### When not to use it

- A start and end: use two fields side by side.
- Only a date or only a time: use the simpler field.

#### Best practices

- State which timezone the value uses, as the field itself holds none.
- Label it with the event, such as 'Start run at'.
- Set limits so users cannot pick impossible moments.
- Test on phones, where pickers differ from desktop.

### When to use

- One moment, such as when a run starts or a link expires.

### When not to use

- Ranges: use two fields (start, end) side by side.

### How to use

- `<input class="orca-input" type="datetime-local" step="60">`. The value has no timezone: store it with the place's timezone on the server.

#### Example: Date-time

```django
<label class="orca-label" for="dt1">Start run at</label>
<input class="orca-input" type="datetime-local" id="dt1" value="2026-11-07T07:00">
```

**Classes:** `.orca-input[type=datetime-local]`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Date-time input

---

## Duration input

`id: duration-input` · level: primitive · source: ORCA

Hours and minutes as two short numeric fields with their units.

### General description

A form field for entering a length of time, such as hours and minutes. Separate labelled parts make the unit clear.

#### Use cases

- Setting how long a shift or meeting lasts.
- Choosing how long data is kept.
- Setting a reminder offset, like 15 minutes before.

#### When not to use it

- A specific time of day: use a time field.
- A short fixed list of lengths: use a select.

#### Best practices

- Show the unit next to each number.
- Accept values like 90 minutes and tidy them into 1 h 30 min.
- Set sensible minimum and maximum values.
- Show the total in plain words after entry.

### When to use

- Durations: shift length, retention, reminder offset.

### How to use

- `<fieldset class="orca-duration">` with a legend and two `.orca-duration__part` groups: number input + `.orca-addon` (h, min).
- Accept minutes over 59 and normalise on the server (90 min → 1 h 30 min).
- Display with `{{ minutes|orca_duration }}`.

#### Example: Duration

```django
<fieldset class="orca-duration" style="border: 0; padding: 0; margin: 0">
  <legend class="orca-label">Shift length</legend>
  <span class="orca-duration__part">
    <input class="orca-input" type="number" min="0" max="23" value="7" aria-label="Hours" id="du-h">
    <span class="orca-addon">h</span>
  </span>
  <span class="orca-duration__part">
    <input class="orca-input" type="number" min="0" step="5" value="30" aria-label="Minutes" id="du-m">
    <span class="orca-addon">min</span>
  </span>
</fieldset>
```

**Classes:** `.orca-duration`, `.orca-duration__part`

**Principles applied:** Practical UI R13: Steppers for small numeric changes; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Duration input

---

## Timezone select

`id: timezone-select` · level: primitive · source: Tangerine

A native select of IANA timezones, grouped by region, preselected from context.

### General description

A dropdown for choosing a timezone, usually listed by region or city name. It makes sure times mean the same to everyone.

#### Use cases

- Setting a user's profile timezone.
- Setting the timezone of a site, team or event.
- Showing a meeting time to people in different regions.

#### When not to use it

- When the browser's timezone is enough: detect it instead of asking.
- Choosing a country or language: those are separate settings.

#### Best practices

- Preselect a likely zone from the user's profile or browser.
- List places by name, such as Europe/Paris, not only offsets.
- Store the zone name, not a fixed offset, so daylight saving works.
- Make long lists searchable.

### When to use

- Setting a site's, an album's or a user's timezone.

### How to use

- `<select class="orca-select">{% orca_timezone_options current_zone %}</select>`.
- Preselect from the object (site), then the user profile, then the browser (`Intl.DateTimeFormat().resolvedOptions().timeZone`).
- Store the IANA name ('Europe/Paris'), never an offset.

#### Example: Timezone

```django
<label class="orca-label" for="tz1">Site timezone</label>
<select class="orca-select" id="tz1" style="max-width: 20rem">
  {% orca_timezone_options "Europe/Paris" %}
</select>
```

**Classes:** `.orca-select`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Postel's law: accept varied input, output reliable and accessible UI

**Related:** `timezone-label`

**ORCA guide items covered:** Timezone select

---

## Weekday toggle

`id: weekday-toggle` · level: primitive · source: ORCA

Seven square toggles for picking days of the week.

### General description

A row of seven buttons for choosing days of the week. People switch each day on or off in place.

#### Use cases

- Choosing which days a task or event repeats.
- Setting opening days or working days.
- Selecting days for alerts or reports.

#### When not to use it

- Picking one single day of the week: use a select or radio buttons.
- Picking specific dates: use a calendar.

#### Best practices

- Start the week on the day the user's region uses.
- Offer shortcuts like 'Weekdays' and 'Every day'.
- Show selected days with more than colour alone.
- Give each toggle its full day name for screen readers.

### When to use

- Recurrence on chosen days, opening days, shift days.

### How to use

- `<fieldset class="orca-weekday-toggles"><legend class="orca-sr-only">Repeat on</legend>` with one `<label class="orca-weekday"><input type="checkbox" name="days" value="mon"><span aria-hidden="true">M</span><span class="orca-sr-only">Monday</span></label>` per day.
- Start the week on the locale's first day (`FIRST_DAY_OF_WEEK`).
- Offer presets (Weekdays, Every day) next to it.

### Accessibility

- Screen readers skip the visible letter and read the full day name.

#### Example: Days

```django
<fieldset class="orca-weekday-toggles">
  <legend class="orca-label">Repeat on</legend>
  <label class="orca-weekday">
    <input type="checkbox" checked>
    <span aria-hidden="true">M</span>
    <span class="orca-sr-only">Monday</span>
  </label>
  <label class="orca-weekday">
    <input type="checkbox" checked>
    <span aria-hidden="true">T</span>
    <span class="orca-sr-only">Tuesday</span>
  </label>
  <label class="orca-weekday">
    <input type="checkbox" checked>
    <span aria-hidden="true">W</span>
    <span class="orca-sr-only">Wednesday</span>
  </label>
  <label class="orca-weekday">
    <input type="checkbox" checked>
    <span aria-hidden="true">T</span>
    <span class="orca-sr-only">Thursday</span>
  </label>
  <label class="orca-weekday">
    <input type="checkbox" checked>
    <span aria-hidden="true">F</span>
    <span class="orca-sr-only">Friday</span>
  </label>
  <label class="orca-weekday">
    <input type="checkbox">
    <span aria-hidden="true">S</span>
    <span class="orca-sr-only">Saturday</span>
  </label>
  <label class="orca-weekday">
    <input type="checkbox">
    <span aria-hidden="true">S</span>
    <span class="orca-sr-only">Sunday</span>
  </label>
</fieldset>
```

**Classes:** `.orca-weekday-toggles`, `.orca-weekday`

**Tokens:** `--orca-accent`, `--orca-border-strong`

**Principles applied:** Practical UI F03: Reduce the total effort of a task; Practical UI R11: Visible choices for small sets; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Weekday toggle

---

## Recurrence select

`id: recurrence-select` · level: primitive · source: ORCA

A select of common repeat rules, with a 'Custom…' option that shows more fields.

### General description

A dropdown of common repeat patterns, like daily or weekly, with a custom option for more detailed rules.

#### Use cases

- Making an event or task repeat.
- Scheduling a recurring report or export.
- Setting up repeating bookings or reminders.

#### When not to use it

- A one-off event: do not show repeat options.
- Very complex schedules only: use a dedicated schedule editor.

#### Best practices

- Show the actual day in options, such as 'Weekly on Thursday'.
- Put 'Does not repeat' first as the default.
- Reveal extra fields only when 'Custom' is chosen.
- Let users set when the repeat ends.

### When to use

- Repeating events, reports, video exports.

### How to use

- Options: Does not repeat · Daily · Every weekday (Mon–Fri) · Weekly on {day} · Monthly on day {n} · Yearly on {date} · Custom…
- Write options with the actual day from the chosen date ('Weekly on Thursday').
- Choosing Custom… reveals the weekday toggle and interval fields.

#### Example: Recurrence

```django
<label class="orca-label" for="rec">Repeat</label>
<select class="orca-select" id="rec" style="max-width: 20rem">
  <option value="">Does not repeat</option>
  <option>Daily</option>
  <option selected>Every weekday (Monday to Friday)</option>
  <option>Weekly on Thursday</option>
  <option>Monthly on day 6</option>
  <option>Yearly on 6 November</option>
  <option value="custom">Custom…</option>
</select>
```

**Classes:** `.orca-select`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI S04: Reveal secondary information when needed; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Recurrence select

---

## Reminder select

`id: reminder-select` · level: primitive · source: ORCA

A select of reminder offsets before an event.

### General description

A dropdown for choosing how long before an event a reminder is sent. It offers common lead times in one short list.

#### Use cases

- Reminding people before an appointment or meeting.
- Warning ahead of a task deadline.
- Setting alerts for bookings or renewals.

#### When not to use it

- Exact reminder times unrelated to an event: use a date-time field.
- Urgent alerts that need no setup: send them directly.

#### Best practices

- Offer a short list of common lead times.
- Include 'No reminder' and 'At time of event'.
- Remember the user's last choice as the default.
- Allow more than one reminder per event.

### When to use

- Event and deadline reminders.

### How to use

- Options: No reminder · At time of event · 5, 10, 15, 30 minutes before · 1 hour before · 1 day before · Custom…
- Default to the user's last choice (Tesler's law). Several reminders: repeat the select with an Add reminder link.

#### Example: Reminder

```django
<label class="orca-label" for="rem">Remind me</label>
<select class="orca-select" id="rem" style="max-width: 16rem">
  <option>No reminder</option>
  <option>At time of event</option>
  <option>5 minutes before</option>
  <option selected>15 minutes before</option>
  <option>1 hour before</option>
  <option>1 day before</option>
  <option value="custom">Custom…</option>
</select>
```

**Classes:** `.orca-select`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Jakob's law: work the way products people already know work; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Reminder select

---
