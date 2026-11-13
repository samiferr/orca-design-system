# Planning text

How dates, times and durations are written: machine-readable (`<time datetime>`) and formatted for the reader's locale and timezone.

## Day number

`id: day-number` · level: primitive · source: ORCA

The day of the month in a calendar cell or date badge.

### General description

The number of the day within a month, shown in a calendar cell or date badge, such as 6 or 23.

#### Use cases

- Showing each day in a month calendar.
- Labelling small date badges on cards or lists.
- Building mini calendars in date pickers.

#### When not to use it

- Showing a full date: write the whole date in words instead.
- Showing the day of the week: use the weekday name.

#### Best practices

- Align numbers in columns so they are easy to scan.
- Leave out the leading zero.
- Add the full date in markup for assistive technology.
- Keep the size consistent across cells.

### When to use

- Calendar cells, mini calendars, date badges.

### How to use

- `<time class="orca-day-number" datetime="2026-11-06">{{ day|date:"j" }}</time>` (no leading zero).
- After converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`), format with Django's `date` filter and the locale-aware `TIME_FORMAT` / `DATE_FORMAT`.

### Accessibility

- Use `<time datetime="…">` with the ISO value, so assistive technology and scripts get the exact moment.

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

### General description

The name of a day of the week, short in column headers (Mon) or in full in lists (Monday).

#### Use cases

- Heading the columns of a calendar.
- Labelling rows in an agenda or schedule.
- Writing dates in a readable way, like 'Friday 6 November'.

#### When not to use it

- Where the date number alone is clear.
- Long text where full words fit: avoid cryptic abbreviations.

#### Best practices

- Use short forms only where space is tight.
- Keep abbreviations consistent across the page.
- Follow the user's language and locale.
- Provide the full name in a title or label.

### When to use

- Calendar column headers (short: MON), agenda rows and date labels (full: Monday).

### How to use

- Header: `<abbr class="orca-weekday-name" title="Monday">{{ d|date:"D" }}</abbr>`.
- Full: `{{ d|date:"l" }}`.
- After converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`), format with Django's `date` filter and the locale-aware `TIME_FORMAT` / `DATE_FORMAT`.

### Accessibility

- Use `<time datetime="…">` with the ISO value, so assistive technology and scripts get the exact moment.

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

The month, with its year, heading a calendar or group of agenda items.

### General description

The name of a month, often with its year, used as a heading for a calendar or a group of dated items.

#### Use cases

- Heading a calendar view.
- Separating groups in an agenda or timeline.
- Labelling a month in a report or archive.

#### When not to use it

- Showing exact dates: use a full date instead.
- Very short space: a short month form or number may fit better.

#### Best practices

- Show the year when it is not the current one.
- Spell out the month to avoid day-month confusion.
- Use a real heading so people can navigate.
- Follow the user's language.

### When to use

- Calendar headers, month separators in agendas and timelines.

### How to use

- `<h2 class="orca-month-name"><time datetime="2026-11">{{ d|date:"F" }}</time> <span class="orca-year">{{ d|date:"Y" }}</span></h2>`.
- Omit the year when it is the current year and context is clear.
- After converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`), format with Django's `date` filter and the locale-aware `TIME_FORMAT` / `DATE_FORMAT`.

### Accessibility

- Use `<time datetime="…">` with the ISO value, so assistive technology and scripts get the exact moment.

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

### General description

The year shown as a small, quiet label next to a month or as the heading of a yearly view.

#### Use cases

- Showing the year beside a month name.
- Heading a year view or archive.
- Marking dates that fall outside the current year.

#### When not to use it

- When the year is obvious from context: leave it out.
- Showing a complete date: write the whole date together.

#### Best practices

- Keep it less prominent than the month or day.
- Use four digits to avoid confusion.
- Show it when the year is not the current one.
- Keep it right next to what it describes.

### When to use

- Beside month names, in year view headings, and on dates outside the current year.

### How to use

- `<span class="orca-year">2026</span>`; full-strength as a year-view heading.
- After converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`), format with Django's `date` filter and the locale-aware `TIME_FORMAT` / `DATE_FORMAT`.

### Accessibility

- Use `<time datetime="…">` with the ISO value, so assistive technology and scripts get the exact moment.

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

### General description

The number of a week within the year, such as W45. Some regions and teams plan by week number.

#### Use cases

- Showing week numbers beside month calendar rows.
- Heading weeks in a planning view.
- Naming sprints, shifts or production weeks.

#### When not to use it

- Audiences who do not use week numbers: use a date range instead.
- Exact days matter: show real dates.

#### Best practices

- Say which numbering system is used, such as ISO weeks.
- Mark it clearly as a week number, for example W45.
- Show it only where the audience uses it.
- Pair it with a date range when space allows.

### When to use

- Left column of month views, week view headers, sprint labels.

### How to use

- `<span class="orca-week-number" title="Week 45">W45</span>` with `{{ d|date:"W" }}`.
- Show only where the audience uses week numbers.
- After converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`), format with Django's `date` filter and the locale-aware `TIME_FORMAT` / `DATE_FORMAT`.

### Accessibility

- Use `<time datetime="…">` with the ISO value, so assistive technology and scripts get the exact moment.

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

### General description

A time of day written as text, such as 08:30 or 8:30 AM, in the format the reader is used to.

#### Use cases

- Showing when an event starts or ends.
- Labelling hours on a day view.
- Timestamps in logs and activity lists.

#### When not to use it

- Recent events where 'ago' reads better: use a relative time.
- A length of time: use a duration label.

#### Best practices

- Follow the reader's 12 or 24-hour habit.
- Align times in columns so they are easy to scan.
- Write ranges with an en dash, like 08:30–10:00.
- Show the timezone when it may differ.

### When to use

- Event times, hour labels, log entries.

### How to use

- `<time class="orca-time" datetime="2026-11-06T08:30">{{ t|time:"TIME_FORMAT" }}</time>`.
- Ranges: '08:30–10:00' with an en dash, no spaces; across days include both dates.
- After converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`), format with Django's `date` filter and the locale-aware `TIME_FORMAT` / `DATE_FORMAT`.

### Accessibility

- Use `<time datetime="…">` with the ISO value, so assistive technology and scripts get the exact moment.

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

### General description

A date written out for people to read, such as 6 November 2026 or Fri 6 Nov.

#### Use cases

- Showing due dates, publish dates or event dates.
- Labelling rows in tables and lists.
- Showing when something was created or changed.

#### When not to use it

- Recent events where '2 minutes ago' reads better: use a relative time.
- Input of a date: use a date field.

#### Best practices

- Spell out the month to avoid confusion between day and month.
- Use shorter forms only in dense tables.
- Follow the reader's language and locale.
- Mark up the exact date for machines and screen readers.

### When to use

- Anywhere a date is shown to people.

### How to use

- `<time class="orca-date" datetime="2026-11-06">{{ d|date:"j F Y" }}</time>`; short form `{{ d|date:"D j M" }}` in dense tables.
- Never show numeric-only dates (06/11/2026) to mixed audiences.
- After converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`), format with Django's `date` filter and the locale-aware `TIME_FORMAT` / `DATE_FORMAT`.

### Accessibility

- Use `<time datetime="…">` with the ISO value, so assistive technology and scripts get the exact moment.

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

### General description

A time written as how long ago or from now it is, such as '2 minutes ago' or 'in 3 days'.

#### Use cases

- Activity feeds and comments.
- 'Last seen' and 'last updated' labels.
- Notifications and recent changes.

#### When not to use it

- Logs, audit trails and legal records: show exact times.
- Dates far from now: show the full date.

#### Best practices

- Show the exact time on hover or in a tooltip.
- Switch to a full date after about a week.
- Keep the text fresh as time passes.
- Make the exact time available to screen readers.

### When to use

- Activity feeds, 'last seen', 'updated' stamps up to about a week old.

### When not to use

- Logs and audit trails: use absolute times.

### How to use

- `<time class="orca-relative-time" datetime="2026-11-06T08:14" title="6 November 2026, 08:14">{{ t|naturaltime }}</time>` (`django.contrib.humanize`).
- Switch to an absolute date after 7 days.
- After converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`), format with Django's `date` filter and the locale-aware `TIME_FORMAT` / `DATE_FORMAT`.

### Accessibility

- Use `<time datetime="…">` with the ISO value, so assistive technology and scripts get the exact moment.

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

A small outlined timezone abbreviation, with the full zone in its title.

### General description

A short label, such as CET or UTC+1, that tells readers which timezone a time is in.

#### Use cases

- Showing meeting times to people in different places.
- Labelling a site's opening hours.
- Showing times in shared schedules and logs.

#### When not to use it

- When everyone is in one zone and it is obvious: leave it out.
- Choosing a zone: use a timezone select.

#### Best practices

- Place it right next to the time.
- Give the full zone name in a tooltip.
- Use a familiar abbreviation or UTC offset.
- Be consistent across the page.

### When to use

- Beside times whose zone may differ from the reader's: site schedules, shared events.

### How to use

- `<abbr class="orca-tz" title="Europe/Paris (UTC+01:00)">CET</abbr>` using `{{ t|date:"T" }}`.
- Hide it when every time on the page is in the reader's zone.
- After converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`), format with Django's `date` filter and the locale-aware `TIME_FORMAT` / `DATE_FORMAT`.

### Accessibility

- Use `<time datetime="…">` with the ISO value, so assistive technology and scripts get the exact moment.

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

### General description

A length of time written in short form, such as 45 min, 1 h 30 min or 3 d.

#### Use cases

- Showing how long an event or task lasts.
- Showing time spent in tables and reports.
- Labelling video or audio length.

#### When not to use it

- A point in time: use a date or time label.
- Entering a duration: use a duration field.

#### Best practices

- Use short, consistent units.
- Avoid mixed styles like 90 minutes and 1.5h.
- Skip zero parts, such as '0 min'.
- Include a machine-readable value for assistive tools.

### When to use

- Event lengths, dwell times, durations in tables.

### How to use

- `<span class="orca-duration-label">{{ minutes|orca_duration }}</span>`; machine value in `<time datetime="PT1H30M">` where useful.
- After converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`), format with Django's `date` filter and the locale-aware `TIME_FORMAT` / `DATE_FORMAT`.

### Accessibility

- Use `<time datetime="…">` with the ISO value, so assistive technology and scripts get the exact moment.

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

### General description

A label that shows the time left until a moment and updates as it runs down.

#### Use cases

- Showing when a session is about to expire.
- Holding a booking or basket for a limited time.
- Counting down to the start of an event.

#### When not to use it

- Distant dates: show the date instead.
- Pressure tactics: avoid fake urgency.

#### Best practices

- Show a correct starting value without relying on scripts.
- Do not announce every second to screen readers.
- Make it look more urgent only near the end.
- Say what happens when it reaches zero.

### When to use

- Session expiry, booking holds, run start.

### How to use

- `<time class="orca-countdown" datetime="2026-11-06T09:00:00Z" data-orca-countdown role="timer">15:00</time>` (orca.js updates it).
- Render the starting value on the server so it works without script.
- After converting to the viewer's timezone (`{% load tz %}`, `{% timezone %}`), format with Django's `date` filter and the locale-aware `TIME_FORMAT` / `DATE_FORMAT`.

### Accessibility

- Use `<time datetime="…">` with the ISO value, so assistive technology and scripts get the exact moment.

#### Example: Example

```django
<time class="orca-countdown" datetime="2030-01-01T00:00:00Z" data-orca-countdown role="timer" aria-label="Time left">–:–</time>
```

**Classes:** `.orca-countdown`, `.orca-countdown--urgent`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Countdown label

---
