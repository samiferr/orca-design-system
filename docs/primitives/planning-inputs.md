# Planning inputs

Date, time and schedule inputs. Native pickers first: they are what people already know, on every device.

## Date input

`id: date-input` · level: primitive · source: ORCA

A native date field (`type="date"`) with ORCA styling.

### Why

The platform date picker is familiar, accessible and localised (Jakob's law, Postel's law); the guide's own advice is to prefer native date and time inputs for planning UI.

### When to use

- Picking a single day: a deadline, a report date, a holiday.

### When not to use

- Dates people know by heart and type faster (birth dates): use the split date input (phase 2) or three numeric fields.

### How to use

- `<input class="orca-input" type="date" id=… name=… min=… max=…>`.
- Set `min`/`max` for allowed ranges; explain the range in help text.
- Prefill sensible defaults (today, next working day) rather than leaving it empty (Tesler's law).
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

### Why

Native time fields follow the reader's 12/24-hour convention automatically (Postel's law) and open the platform picker on phones (Jakob's law).

### When to use

- Start and end times, reminder times, opening hours.

### How to use

- `<input class="orca-input" type="time" step="900">` (step in seconds: 900 = 15 minutes).
- Show the timezone next to it with a timezone label when people may be in another zone than the place.

#### Example: Time with timezone

```django
<label class="orca-label" for="t1">Opens at</label>
<div class="orca-row"><input class="orca-input" type="time" id="t1" value="08:30" step="900"><span class="orca-tz" title="Europe/Paris">CET</span></div>
```

**Classes:** `.orca-input[type=time]`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Jakob's law: work the way products people already know work

**Related:** `timezone-label`

**ORCA guide items covered:** Time input

---

## Date-time input

`id: datetime-input` · level: primitive · source: ORCA

A native `datetime-local` field for one moment.

### Why

One control for one moment avoids mismatched date and time pairs (Postel's law).

### When to use

- A single event moment: when a run starts, when a link expires.

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

### Why

Two labelled parts are faster and less error-prone than a free-text '1h30' or a long dropdown (Practical UI R13, Postel's law: accept the parts and normalise).

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
  <span class="orca-duration__part"><input class="orca-input" type="number" min="0" max="23" value="7" aria-label="Hours" id="du-h"><span class="orca-addon">h</span></span>
  <span class="orca-duration__part"><input class="orca-input" type="number" min="0" step="5" value="30" aria-label="Minutes" id="du-m"><span class="orca-addon">min</span></span>
</fieldset>
```

**Classes:** `.orca-duration`, `.orca-duration__part`

**Principles applied:** Practical UI R13: Steppers for small numeric changes; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Duration input

---

## Timezone select

`id: timezone-select` · level: primitive · source: Tangerine

A native select of IANA timezones, grouped by region, preselected from context.

### Why

Timezones are inherent complexity; ORCA moves it to the system by listing real zones and preselecting the site's or browser's zone so most people never touch it (Tesler's law).

### When to use

- Setting a site's, camera's or user's timezone.

### How to use

- `<select class="orca-select">{% orca_timezone_options current_zone %}</select>`.
- Preselect from the object (site), then the user profile, then the browser (`Intl.DateTimeFormat().resolvedOptions().timeZone`).
- Store the IANA name ('Europe/Paris'), never an offset.

#### Example: Timezone

```django
<label class="orca-label" for="tz1">Site timezone</label>
<select class="orca-select" id="tz1" style="max-width: 20rem">{% orca_timezone_options "Europe/Paris" %}</select>
```

**Classes:** `.orca-select`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Postel's law: accept varied input, output reliable and accessible UI

**Related:** `timezone-label`

**ORCA guide items covered:** Timezone select

---

## Weekday toggle

`id: weekday-toggle` · level: primitive · source: ORCA

Seven square toggles for picking days of the week.

### Why

All seven days visible and toggled in place is faster than seven checkboxes or a multi-select (Practical UI F03, R11), and the checked fill plus bold text show state without colour alone.

### When to use

- Recurrence on chosen days, opening days, shift days.

### How to use

- `<fieldset class="orca-weekday-toggles"><legend class="orca-sr-only">Repeat on</legend>` with one `<label class="orca-weekday"><input type="checkbox" name="days" value="mon"><span aria-hidden="true">M</span><span class="orca-sr-only">Monday</span></label>` per day.
- Start the week on the locale's first day (`FIRST_DAY_OF_WEEK`).
- Offer presets (Weekdays, Every day) next to it.

### Accessibility

- The visible letter is hidden from screen readers; the full day name is read.

#### Example: Days

```django
<fieldset class="orca-weekday-toggles"><legend class="orca-label">Repeat on</legend>
<label class="orca-weekday"><input type="checkbox" checked><span aria-hidden="true">M</span><span class="orca-sr-only">Monday</span></label><label class="orca-weekday"><input type="checkbox" checked><span aria-hidden="true">T</span><span class="orca-sr-only">Tuesday</span></label><label class="orca-weekday"><input type="checkbox" checked><span aria-hidden="true">W</span><span class="orca-sr-only">Wednesday</span></label><label class="orca-weekday"><input type="checkbox" checked><span aria-hidden="true">T</span><span class="orca-sr-only">Thursday</span></label><label class="orca-weekday"><input type="checkbox" checked><span aria-hidden="true">F</span><span class="orca-sr-only">Friday</span></label><label class="orca-weekday"><input type="checkbox"><span aria-hidden="true">S</span><span class="orca-sr-only">Saturday</span></label><label class="orca-weekday"><input type="checkbox"><span aria-hidden="true">S</span><span class="orca-sr-only">Sunday</span></label>
</fieldset>
```

**Classes:** `.orca-weekday-toggles`, `.orca-weekday`

**Tokens:** `--orca-accent`, `--orca-border-strong`

**Principles applied:** Practical UI F03: Reduce the total effort of a task; Practical UI R11: Visible choices for small sets; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Weekday toggle

---

## Recurrence select

`id: recurrence-select` · level: primitive · source: ORCA

A select of common repeat rules with a 'Custom…' option that reveals more fields.

### Why

Most repeats are a few common rules; listing them keeps the choice quick (Hick's law) and reveals the full rule editor only when needed (Practical UI S04, Tesler's law).

### When to use

- Repeating events, reports, capture runs.

### How to use

- Options: Does not repeat · Daily · Every weekday (Mon–Fri) · Weekly on {day} · Monthly on day {n} · Yearly on {date} · Custom…
- Write options with the actual day from the chosen date ('Weekly on Thursday').
- Choosing Custom… reveals the weekday toggle and interval fields.

#### Example: Recurrence

```django
<label class="orca-label" for="rec">Repeat</label>
<select class="orca-select" id="rec" style="max-width: 20rem">
  <option value="">Does not repeat</option><option>Daily</option><option selected>Every weekday (Monday to Friday)</option>
  <option>Weekly on Thursday</option><option>Monthly on day 6</option><option>Yearly on 6 November</option><option value="custom">Custom…</option>
</select>
```

**Classes:** `.orca-select`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI S04: Reveal secondary information when needed; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Recurrence select

---

## Reminder select

`id: reminder-select` · level: primitive · source: ORCA

A select of reminder offsets before an event.

### Why

A short list of standard offsets is faster than typing a duration (Hick's law) and matches calendar apps people know (Jakob's law).

### When to use

- Event and deadline reminders.

### How to use

- Options: No reminder · At time of event · 5, 10, 15, 30 minutes before · 1 hour before · 1 day before · Custom…
- Default to the user's last choice (Tesler's law). Several reminders: repeat the select with an Add reminder link.

#### Example: Reminder

```django
<label class="orca-label" for="rem">Remind me</label>
<select class="orca-select" id="rem" style="max-width: 16rem">
  <option>No reminder</option><option>At time of event</option><option>5 minutes before</option><option selected>15 minutes before</option>
  <option>1 hour before</option><option>1 day before</option><option value="custom">Custom…</option>
</select>
```

**Classes:** `.orca-select`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Jakob's law: work the way products people already know work; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Reminder select

---
