# Date and time pickers

Native date and time inputs, composed with shortcuts, ranges, time zones and a month grid. Native first: every device already knows how to pick a date.

## Date picker

`id: date-picker` · level: component · source: ORCA

A labelled native date input with shortcut buttons for the most common dates.

Built from: `date-input`, `tag`, `help-text`

### Why

The native picker is familiar and accessible on every device (Jakob's law); one-tap shortcuts for the dates people choose most remove the picker entirely in common cases (Tesler's law, Fitts's law).

### When to use

- Choosing one date near today: a report date, a due date, a start date.

### When not to use

- Dates far in the past people know by heart: use the split date input.

### How to use

- `.orca-field` with label, help and `<input class="orca-input" type="date">`, then `.orca-shortcuts` of tags `<button class="orca-tag" type="button" aria-pressed="false" data-orca-set-date="0" aria-controls="input-id">Today</button>` (+1 Tomorrow, +7 In a week).
- Set `min`/`max` and say the allowed range in the help text.
- Django: `{% orca_field form.due %}` renders a DateField as a native date input.

#### Example: Due date

```django
<div class="orca-field" style="max-width: 20rem">
  <label class="orca-label" for="dp-1">Due date</label>
  <input class="orca-input" type="date" id="dp-1" name="due">
  <div class="orca-shortcuts" role="group" aria-label="Quick dates"><button class="orca-tag" type="button" aria-pressed="false" data-orca-set-date="0" aria-controls="dp-1">Today</button><button class="orca-tag" type="button" aria-pressed="false" data-orca-set-date="1" aria-controls="dp-1">Tomorrow</button><button class="orca-tag" type="button" aria-pressed="false" data-orca-set-date="7" aria-controls="dp-1">In a week</button></div>
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

### Why

Native time fields follow the reader's 12/24-hour habit (Postel's law); a step of 15 minutes matches how people plan and removes fiddly values.

### When to use

- Start times, reminder times, opening hours.

### How to use

- `.orca-field` > label + `.orca-row` containing `<input class="orca-input" type="time" step="900">` and a timezone label.
- Omit the timezone label when every time on the page is in the reader's zone.

#### Example: Opening time

```django
<div class="orca-field" style="max-width: 20rem"><label class="orca-label" for="tp-1">Opens at</label><div class="orca-row"><input class="orca-input" type="time" id="tp-1" value="08:30" step="900" style="max-width: 9rem"><abbr class="orca-tz" title="Europe/Paris (UTC+01:00)">CET</abbr></div></div>
```

**Classes:** `.orca-field`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Time picker

---

## Date-time picker

`id: datetime-picker` · level: component · source: ORCA

A date and a time as two labelled fields in one group, with the timezone.

Built from: `date-input`, `time-input`, `timezone-label`

### Why

Two separate native fields are easier to fill and correct than one combined control, and they work the same in every browser (Postel's law).

### When to use

- One moment: when a run starts, when access expires.

### How to use

- `<fieldset class="orca-inline-fields">` with a legend, a date field and a time field (`.orca-field`), and a timezone label.
- Combine on the server in the site's timezone; store UTC.

#### Example: Run start

```django
<fieldset class="orca-inline-fields"><legend class="orca-label">Start the run</legend>
  <div class="orca-field"><label class="orca-label" for="dtp-d">Date</label><input class="orca-input" type="date" id="dtp-d" value="2026-11-07"></div>
  <div class="orca-field"><label class="orca-label" for="dtp-t">Time</label><input class="orca-input" type="time" id="dtp-t" value="07:00" step="900"></div>
  <abbr class="orca-tz orca-inline-fields__sep" title="Europe/Paris">CET</abbr>
</fieldset>
```

**Classes:** `.orca-inline-fields`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Date-time picker

---

## Date-range picker

`id: date-range-picker` · level: component · source: ORCA

Start and end dates with presets, kept in order, and the length in days.

Built from: `date-input`, `preset-buttons`

### Why

Most ranges are standard periods; presets choose them in one tap (Hick's law) and keeping the end after the start prevents an impossible range (Postel's law). Showing the length confirms the choice.

### When to use

- Report periods, time off, exceptions, filters.

### How to use

- `<fieldset class="orca-inline-fields" data-orca-range>` with a legend, a From date field, a To date field and `<p class="orca-inline-fields__note" data-orca-range-output aria-live="polite">`.
- Presets: a preset-buttons row above it (Today, This week, Last 7 days, This month).
- orca.js sets the end field's `min` to the start and moves the end when needed.

#### Example: Report period

```django
<fieldset class="orca-inline-fields" data-orca-range><legend class="orca-label">Report period</legend>
  <div class="orca-field"><label class="orca-label" for="dr-a">From</label><input class="orca-input" type="date" id="dr-a" value="2026-11-02"></div>
  <span class="orca-inline-fields__sep" aria-hidden="true">–</span>
  <div class="orca-field"><label class="orca-label" for="dr-b">To</label><input class="orca-input" type="date" id="dr-b" value="2026-11-08"></div>
  <p class="orca-inline-fields__note" data-orca-range-output aria-live="polite">7 days</p>
</fieldset>
```

**Classes:** `.orca-inline-fields`, `.orca-inline-fields__note`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Postel's law: accept varied input, output reliable and accessible UI; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Date-range picker

---

## Time-range input (start and end)

`id: time-range-input` · level: component · source: ORCA

Start and end times with the resulting duration, saying when it ends the next day.

Built from: `time-input`, `duration-label`

### Why

People check a time range by its length; computing it live catches typos (Doherty threshold), and saying 'ends the next day' makes overnight shifts explicit instead of an error (Postel's law).

### When to use

- Opening hours, shifts, booking windows.

### How to use

- `<fieldset class="orca-inline-fields" data-orca-range>` with Start and End time fields and an `orca-inline-fields__note` output.
- Validate on the server too; decide whether overnight ranges are allowed and say so.

#### Example: Shift

```django
<fieldset class="orca-inline-fields" data-orca-range><legend class="orca-label">Shift</legend>
  <div class="orca-field"><label class="orca-label" for="trg-a">Start</label><input class="orca-input" type="time" id="trg-a" value="22:00" step="900"></div>
  <span class="orca-inline-fields__sep" aria-hidden="true">–</span>
  <div class="orca-field"><label class="orca-label" for="trg-b">End</label><input class="orca-input" type="time" id="trg-b" value="06:00" step="900"></div>
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

### Why

Common durations in one tap (Hick's law) plus exact fields for the rest; parts with units remove format guessing (Postel's law, Practical UI R13).

### When to use

- Meeting lengths, retention, timeouts, reminder offsets.

### How to use

- `.orca-field` containing a duration input (two parts with addons) and `.orca-shortcuts` tags (15 min, 30 min, 1 h).
- Shortcuts set both parts with a small script or a server round-trip; normalise minutes over 59 on the server.

#### Example: Meeting length

```django
<div class="orca-field"><fieldset class="orca-duration" style="border: 0; padding: 0; margin: 0"><legend class="orca-label">Length</legend>
  <span class="orca-duration__part"><input class="orca-input" type="number" min="0" value="0" aria-label="Hours"><span class="orca-addon">h</span></span>
  <span class="orca-duration__part"><input class="orca-input" type="number" min="0" step="5" value="30" aria-label="Minutes"><span class="orca-addon">min</span></span></fieldset>
  <div class="orca-shortcuts" role="group" aria-label="Common lengths"><button class="orca-tag" type="button" aria-pressed="false">15 min</button><button class="orca-tag" type="button" aria-pressed="true">30 min</button><button class="orca-tag" type="button" aria-pressed="false">1 h</button></div></div>
```

**Classes:** `.orca-shortcuts`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Postel's law: accept varied input, output reliable and accessible UI; Practical UI R13: Steppers for small numeric changes

**ORCA guide items covered:** Duration picker

---

## Timezone selector

`id: timezone-selector` · level: component · source: Tangerine

A timezone select with a 'Use my timezone' button and the current offset.

Built from: `timezone-select`, `button`

### Why

Detecting the zone moves the complexity to the system (Tesler's law); keeping the full list lets people choose a site's zone that differs from theirs (Postel's law).

### When to use

- Site, video and profile settings.

### How to use

- `.orca-field` with label, help showing the current local time, a `.orca-row` with `<select class="orca-select">{% orca_timezone_options current %}</select>` and a ghost button `data-orca-detect-tz aria-controls="select-id"`.
- Store the IANA name.

#### Example: Site timezone

```django
<div class="orca-field" style="max-width: 30rem"><label class="orca-label" for="tzs">Site timezone</label><p class="orca-help" id="tzs-help">Reports and schedules use this zone.</p>
  <div class="orca-row" style="flex-wrap: nowrap"><select class="orca-select" id="tzs" aria-describedby="tzs-help">{% orca_timezone_options "Europe/Paris" %}</select><button class="orca-button orca-button--ghost" type="button" data-orca-detect-tz aria-controls="tzs">Use my timezone</button></div></div>
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

### Why

Arrows serve small moves; selects jump far without many clicks (Fitts's law, Hick's law).

### When to use

- Calendars and reports navigated by month, especially far from today.

### How to use

- `<div class="orca-month-switcher" role="group" aria-label="Month">` with a previous icon button, a month select, a year select and a next icon button.
- Server-rendered: a GET form with `data-orca-autosubmit` on the selects and links for the arrows.

#### Example: Switcher

```django
<form class="orca-month-switcher" role="group" aria-label="Month" onsubmit="return false">
  <a class="orca-icon-button" href="#" aria-label="Previous month, October 2026">{% icon "chevron-left" %}</a>
  <select class="orca-select orca-select--dense" aria-label="Month"><option>October</option><option selected>November</option><option>December</option></select>
  <select class="orca-select orca-select--dense" aria-label="Year"><option>2025</option><option selected>2026</option><option>2027</option></select>
  <a class="orca-icon-button" href="#" aria-label="Next month, December 2026">{% icon "chevron-right" %}</a>
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

### Why

A month grid shows a date in context (weekday, week, neighbours) in the layout everyone knows (Jakob's law); rendering it on the server respects the locale's first weekday without script (Tesler's law).

### When to use

- Sidebars of calendars, date filters, showing which days have events.

### When not to use

- Picking one date in a form: the native date input is simpler.

### How to use

- `{% orca_mini_calendar month selected=day url="/events/?day={date}" nav_url="?month={month}" events=event_days holidays=holiday_map week_numbers=True %}`.
- Without `url`, days render as buttons with `data-date` for your own script.
- Each day's accessible name is the full date plus today, holiday and 'has events' notes.

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
