# Planning icons

Icons for time and scheduling ideas, drawn by ORCA on the same 16px grid as the rest of the set.

## Planning icons

`id: planning-icons` · level: primitive · source: ORCA

calendar, clock, repeat, bell (notifications), alarm, timer, hourglass, flag, pin, calendar-plus, today.

### When to use

- calendar: date fields and date navigation · clock: times and durations · repeat: recurring items · bell/alarm: reminders · timer/hourglass: countdowns and waits · flag: deadlines · pin: pinned dates · calendar-plus: add event · today: jump to today.

### When not to use

- Using a planning icon without its word, except in icon buttons with an aria-label.

### How to use

- `{% icon "calendar" %}` etc. Aliases: `bell` → notifications, `date-pin` → pin, `calendar-today` → today.
- 'Today' buttons should show the word 'Today'; the icon is optional.

#### Example: Planning glyphs

```django
<div class="orca-row orca-row--16">
  <span class="orca-with-icon">
    {% icon "calendar" %}
    <span class="orca-small">calendar</span>
  </span>
  <span class="orca-with-icon">
    {% icon "clock" %}
    <span class="orca-small">clock</span>
  </span>
  <span class="orca-with-icon">
    {% icon "repeat" %}
    <span class="orca-small">repeat</span>
  </span>
  <span class="orca-with-icon">
    {% icon "notifications" %}
    <span class="orca-small">notifications</span>
  </span>
  <span class="orca-with-icon">
    {% icon "alarm" %}
    <span class="orca-small">alarm</span>
  </span>
  <span class="orca-with-icon">
    {% icon "timer" %}
    <span class="orca-small">timer</span>
  </span>
  <span class="orca-with-icon">
    {% icon "hourglass" %}
    <span class="orca-small">hourglass</span>
  </span>
  <span class="orca-with-icon">
    {% icon "flag" %}
    <span class="orca-small">flag</span>
  </span>
  <span class="orca-with-icon">
    {% icon "pin" %}
    <span class="orca-small">pin</span>
  </span>
  <span class="orca-with-icon">
    {% icon "calendar-plus" %}
    <span class="orca-small">calendar-plus</span>
  </span>
  <span class="orca-with-icon">
    {% icon "today" %}
    <span class="orca-small">today</span>
  </span>
</div>
```

**Classes:** `.orca-icon`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI F09: Keep visual and functional behaviour consistent; Hick's law: fewer, clearer choices mean faster decisions

**Related:** `icon-set`

**ORCA guide items covered:** Calendar; Clock; Repeat; Bell (reminder); Alarm; Timer; Hourglass; Flag; Pin (date); Calendar-plus; Today (jump to today)

---
