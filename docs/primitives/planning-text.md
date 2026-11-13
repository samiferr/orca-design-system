# Planning text

How dates, times and durations are written. Always machine-readable (`<time datetime>`) and formatted for the reader's locale and timezone.

## Day number

`id: day-number` · level: primitive · source: ORCA

The day of the month in a calendar cell or date badge.

### When to use

- Calendar cells, mini calendars, date badges.

### How to use

- `<time class="orca-day-number" datetime="2026-11-06">{{ day|date:"j" }}</time>` (no leading zero).
- Format with Django's `date` filter and `TIME_FORMAT` / `DATE_FORMAT` (locale aware) after converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`).

### Accessibility

- Wrap in `<time datetime="…">` with the ISO value so assistive technology and scripts get the exact moment.

#### Example: Example

```django
<time class="orca-day-number" datetime="2026-11-06">6</time>
```

**Classes:** `.orca-day-number`

**Principles applied:** Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Day number

---

## Weekday name

`id: weekday-name` · level: primitive · source: ORCA

The day of the week as a short uppercase label or a full word.

### When to use

- Calendar column headers (short: MON), agenda rows and date labels (full: Monday).

### How to use

- Header: `<abbr class="orca-weekday-name" title="Monday">{{ d|date:"D" }}</abbr>`.
- Full: `{{ d|date:"l" }}`.
- Format with Django's `date` filter and `TIME_FORMAT` / `DATE_FORMAT` (locale aware) after converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`).

### Accessibility

- Wrap in `<time datetime="…">` with the ISO value so assistive technology and scripts get the exact moment.

#### Example: Example

```django
<div class="orca-row orca-row--16">
  <abbr class="orca-weekday-name" title="Monday">Mon</abbr>
  <abbr class="orca-weekday-name" title="Tuesday">Tue</abbr>
  <span>Friday</span>
</div>
```

**Classes:** `.orca-weekday-name`

**Principles applied:** Practical UI W07: Reserve uppercase for short labels

**ORCA guide items covered:** Weekday name

---

## Month name

`id: month-name` · level: primitive · source: ORCA

The month (and year) heading a calendar or a group of agenda items.

### When to use

- Calendar headers, month separators in agendas and timelines.

### How to use

- `<h2 class="orca-month-name"><time datetime="2026-11">{{ d|date:"F" }}</time> <span class="orca-year">{{ d|date:"Y" }}</span></h2>`.
- Omit the year when it is the current year and context is clear.
- Format with Django's `date` filter and `TIME_FORMAT` / `DATE_FORMAT` (locale aware) after converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`).

### Accessibility

- Wrap in `<time datetime="…">` with the ISO value so assistive technology and scripts get the exact moment.

#### Example: Example

```django
<h2 class="orca-month-name">
  <time datetime="2026-11">November</time>
  <span class="orca-year">2026</span>
</h2>
```

**Classes:** `.orca-month-name`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Month name

---

## Year label

`id: year-label` · level: primitive · source: ORCA

The year, muted, beside a month or in a year view.

### When to use

- Beside month names; year view headings; date labels outside the current year.

### How to use

- `<span class="orca-year">2026</span>`; full-strength as a year-view heading.
- Format with Django's `date` filter and `TIME_FORMAT` / `DATE_FORMAT` (locale aware) after converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`).

### Accessibility

- Wrap in `<time datetime="…">` with the ISO value so assistive technology and scripts get the exact moment.

#### Example: Example

```django
<span class="orca-year">2026</span>
```

**Classes:** `.orca-year`

**Principles applied:** Practical UI L03: Establish an order of importance

**ORCA guide items covered:** Year label

---

## Week number

`id: week-number` · level: primitive · source: ORCA

The ISO week number, labelled.

### When to use

- Left column of month views, week view headers, sprint labels.

### How to use

- `<span class="orca-week-number" title="Week 45">W45</span>` with `{{ d|date:"W" }}`.
- Only show where the audience uses week numbers.
- Format with Django's `date` filter and `TIME_FORMAT` / `DATE_FORMAT` (locale aware) after converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`).

### Accessibility

- Wrap in `<time datetime="…">` with the ISO value so assistive technology and scripts get the exact moment.

#### Example: Example

```django
<span class="orca-week-number" title="Week 45">W45</span>
```

**Classes:** `.orca-week-number`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Week number

---

## Time label

`id: time-label` · level: primitive · source: ORCA

A clock time in the reader's 12- or 24-hour convention.

### When to use

- Event times, hour labels, log entries.

### How to use

- `<time class="orca-time" datetime="2026-11-06T08:30">{{ t|time:"TIME_FORMAT" }}</time>`.
- Ranges: '08:30–10:00' with an en dash, no spaces; across days include both dates.
- Format with Django's `date` filter and `TIME_FORMAT` / `DATE_FORMAT` (locale aware) after converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`).

### Accessibility

- Wrap in `<time datetime="…">` with the ISO value so assistive technology and scripts get the exact moment.

#### Example: Example

```django
<time class="orca-time" datetime="2026-11-06T08:30">08:30</time>
–
<time class="orca-time" datetime="2026-11-06T10:00">10:00</time>
```

**Classes:** `.orca-time`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Time label

---

## Date label

`id: date-label` · level: primitive · source: ORCA

A date written for people: '6 November 2026', 'Fri 6 Nov'.

### When to use

- Anywhere a date is shown to people.

### How to use

- `<time class="orca-date" datetime="2026-11-06">{{ d|date:"j F Y" }}</time>`; short form `{{ d|date:"D j M" }}` in dense tables.
- Never show numeric-only dates (06/11/2026) to mixed audiences.
- Format with Django's `date` filter and `TIME_FORMAT` / `DATE_FORMAT` (locale aware) after converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`).

### Accessibility

- Wrap in `<time datetime="…">` with the ISO value so assistive technology and scripts get the exact moment.

#### Example: Example

```django
<time class="orca-date" datetime="2026-11-06">6 November 2026</time>
·
<time class="orca-date" datetime="2026-11-06">Fri 6 Nov</time>
```

**Classes:** `.orca-date`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Date label

---

## Relative time label

`id: relative-time` · level: primitive · source: ORCA

'2 minutes ago', 'in 3 days', with the exact time on hover and for screen readers.

### When to use

- Activity feeds, 'last seen', 'updated' stamps up to about a week old.

### When not to use

- Logs and audit trails: use absolute times.

### How to use

- `<time class="orca-relative-time" datetime="2026-11-06T08:14" title="6 November 2026, 08:14">{{ t|naturaltime }}</time>` (`django.contrib.humanize`).
- Switch to an absolute date after 7 days.
- Format with Django's `date` filter and `TIME_FORMAT` / `DATE_FORMAT` (locale aware) after converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`).

### Accessibility

- Wrap in `<time datetime="…">` with the ISO value so assistive technology and scripts get the exact moment.

#### Example: Example

```django
<time class="orca-relative-time" datetime="2026-11-06T08:14" title="6 November 2026, 08:14">2 minutes ago</time>
```

**Classes:** `.orca-relative-time`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Relative time label

---

## Timezone label

`id: timezone-label` · level: primitive · source: ORCA

A small outlined abbreviation of the timezone, with the full zone in its title.

### When to use

- Beside times whose zone may differ from the reader's: site schedules, shared events.

### How to use

- `<abbr class="orca-tz" title="Europe/Paris (UTC+01:00)">CET</abbr>` using `{{ t|date:"T" }}`.
- Hide it when every time on the page is in the reader's zone.
- Format with Django's `date` filter and `TIME_FORMAT` / `DATE_FORMAT` (locale aware) after converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`).

### Accessibility

- Wrap in `<time datetime="…">` with the ISO value so assistive technology and scripts get the exact moment.

#### Example: Example

```django
<span class="orca-time">08:30</span>
<abbr class="orca-tz" title="Europe/Paris (UTC+01:00)">CET</abbr>
```

**Classes:** `.orca-tz`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Timezone label

---

## Duration label

`id: duration-label` · level: primitive · source: ORCA

A length of time: '45 min', '1 h 30 min', '3 d'.

### When to use

- Event lengths, dwell times, durations in tables.

### How to use

- `<span class="orca-duration-label">{{ minutes|orca_duration }}</span>`; machine value in `<time datetime="PT1H30M">` where useful.
- Format with Django's `date` filter and `TIME_FORMAT` / `DATE_FORMAT` (locale aware) after converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`).

### Accessibility

- Wrap in `<time datetime="…">` with the ISO value so assistive technology and scripts get the exact moment.

#### Example: Example

```django
<time class="orca-duration-label" datetime="PT1H30M">1 h 30 min</time>
```

**Classes:** `.orca-duration-label`

**Principles applied:** Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Duration label

---

## Countdown label

`id: countdown-label` · level: primitive · source: ORCA

Time left until a moment, updating live.

### When to use

- Session expiry, booking holds, run start.

### How to use

- `<time class="orca-countdown" datetime="2026-11-06T09:00:00Z" data-orca-countdown role="timer">15:00</time>` (orca.js updates it).
- Render the initial value on the server so it reads correctly without script.
- Format with Django's `date` filter and `TIME_FORMAT` / `DATE_FORMAT` (locale aware) after converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`).

### Accessibility

- Wrap in `<time datetime="…">` with the ISO value so assistive technology and scripts get the exact moment.

#### Example: Example

```django
<time class="orca-countdown" datetime="2030-01-01T00:00:00Z" data-orca-countdown role="timer" aria-label="Time left">–:–</time>
```

**Classes:** `.orca-countdown`, `.orca-countdown--urgent`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Countdown label

---
