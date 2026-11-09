# Schedule parts

Rows and messages for opening hours, availability, exceptions, time off and bookings.

## Schedule row

`id: schedule-row` · level: component · source: ORCA

One line of a weekly schedule: day, start time, end time and a remove button.

Built from: `select`, `time-input`, `remove-row-button`

### Why

Opening hours vary by day and may split around lunch; one row per span handles every case without special fields (Tesler's law), and rows read like a timetable (Jakob's law).

### When to use

- Opening hours, working hours, capture schedules.

### How to use

- `<div class="orca-schedule-row" data-orca-row>` with a day select, start time, `.orca-schedule-row__sep` '–', end time and a remove-row button; rows live in `<div class="orca-schedule" id=…>`.
- Invalid rows get `--invalid` and a `.orca-schedule-row__msg` error (end before start, overlap).
- Django: one formset row per span; the add-row button clones the empty form.

#### Example: Opening hours

```django
<div class="orca-schedule" id="sr-list">
  <div class="orca-schedule-row" data-orca-row><select class="orca-select" aria-label="Day"><option>Monday</option><option>Tuesday</option><option>Wednesday</option><option>Thursday</option><option>Friday</option><option>Saturday</option><option>Sunday</option></select><input class="orca-input" type="time" value="08:00" aria-label="Opens"><span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" value="12:00" aria-label="Closes"><button class="orca-icon-button" type="button" aria-label="Remove Monday 08:00 to 12:00" data-orca-remove-row>{% icon "delete" %}</button></div>
  <div class="orca-schedule-row orca-schedule-row--invalid" data-orca-row><select class="orca-select" aria-label="Day"><option>Monday</option><option>Tuesday</option><option>Wednesday</option><option>Thursday</option><option>Friday</option><option>Saturday</option><option>Sunday</option></select><input class="orca-input" type="time" value="13:00" aria-label="Opens" aria-invalid="true" aria-describedby="sr-err"><span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" value="12:30" aria-label="Closes" aria-invalid="true" aria-describedby="sr-err"><button class="orca-icon-button" type="button" aria-label="Remove Monday 13:00 to 12:30" data-orca-remove-row>{% icon "delete" %}</button>
    <p class="orca-error orca-schedule-row__msg" id="sr-err">{% icon "error" %}<span>Closing time must be after opening time.</span></p></div>
</div>
```

**Classes:** `.orca-schedule`, `.orca-schedule-row`, `.orca-schedule-row__sep`, `.orca-schedule-row--invalid`, `.orca-schedule-row__msg`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Schedule row (day, start, end)

---

## Add-row button

`id: add-row-button` · level: component · source: ORCA

A ghost button that adds one more row to a repeating group and focuses it.

Built from: `button`, `icon`

### Why

Letting people add rows only when needed keeps the default form short (Practical UI R02); focusing the new row saves a click (Fitts's law).

### When to use

- Schedules, reminders, properties, any repeating set of fields.

### How to use

- `<button class="orca-button orca-button--ghost" type="button" data-orca-add-row="template-id" aria-controls="list-id">{% icon "plus" %}Add hours</button>` below the rows.
- Name what is added ('Add hours', 'Add reminder'); hide it at the maximum number of rows and say the limit.

#### Example: Add row

```django
<div class="orca-schedule" id="ar-list"><div class="orca-schedule-row" data-orca-row><select class="orca-select" aria-label="Day"><option>Monday</option><option>Tuesday</option><option>Wednesday</option><option>Thursday</option><option>Friday</option><option>Saturday</option><option>Sunday</option></select><input class="orca-input" type="time" value="08:00" aria-label="Opens"><span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" value="18:00" aria-label="Closes"><button class="orca-icon-button" type="button" aria-label="Remove row" data-orca-remove-row>{% icon "delete" %}</button></div></div>
<template id="ar-tpl"><div class="orca-schedule-row" data-orca-row><select class="orca-select" aria-label="Day"><option>Monday</option><option>Tuesday</option><option>Wednesday</option><option>Thursday</option><option>Friday</option><option>Saturday</option><option>Sunday</option></select><input class="orca-input" type="time" aria-label="Opens"><span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" aria-label="Closes"><button class="orca-icon-button" type="button" aria-label="Remove row" data-orca-remove-row>{% icon "delete" %}</button></div></template>
<button class="orca-button orca-button--ghost" type="button" data-orca-add-row="ar-tpl" aria-controls="ar-list" style="margin-top: var(--orca-space-8)">{% icon "plus" %}Add hours</button>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Formset

```python
# videos/forms.py
from django import forms

from .models import Chapter, Video

ChapterFormSet = forms.inlineformset_factory(
    Video, Chapter, fields=["title", "starts_at"], extra=0, can_delete=True,
)


# videos/views.py
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ChapterFormSet
from .models import Video


def edit_chapters(request, pk):
    video = get_object_or_404(Video, pk=pk)
    formset = ChapterFormSet(request.POST or None, instance=video, prefix="chapters")
    if request.method == "POST" and formset.is_valid():
        formset.save()
        return redirect("video-detail", pk=video.pk)
    # Template: {{ formset.management_form }}, one [data-orca-row] per form, and a <template id="chapter-row">
    # holding {{ formset.empty_form }} (its names contain __prefix__). The add-row button points at it with
    # data-orca-add-row="chapter-row" and data-orca-total="id_chapters-TOTAL_FORMS".
    return render(request, "videos/chapters.html", {"video": video, "formset": formset})
```

**Classes:** `.orca-button--ghost`

**Principles applied:** Practical UI R02: Ask only for useful, necessary information; Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI B10: Name the action clearly

**ORCA guide items covered:** Add-row button

---

## Remove-row button

`id: remove-row-button` · level: component · source: ORCA

An icon button that removes its row, named after what it removes, with the removal announced.

Built from: `icon-button`

### Why

Removing a row is low risk and easy to redo, so it needs no confirmation (Doherty: friction only where costly), but its name must say which row it removes (Hick's law: labelled icons).

### When to use

- The end of every removable row.

### How to use

- `<button class="orca-icon-button" type="button" aria-label="Remove Monday 08:00 to 12:00" data-orca-remove-row>{% icon "delete" %}</button>`.
- With Django formsets, a `-DELETE` checkbox in the row is ticked and the row hidden instead of removed.
- Focus moves to the next row; the removal is announced.

#### Example: Remove

```django
<button class="orca-icon-button" type="button" aria-label="Remove Monday 08:00 to 12:00">{% icon "delete" %}</button>
```

**Classes:** `.orca-icon-button`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Remove-row button

---

## Availability legend

`id: availability-legend` · level: component · source: ORCA

The key to availability marks: free, busy, tentative and not working.

Built from: `availability-color`, `legend-item`

### Why

Patterns only help if their meaning is stated next to them (Practical UI C03).

### When to use

- Above schedulers, booking grids and resource rows.

### How to use

- `<ul class="orca-legend">` of availability marks: `<li><span class="orca-avail orca-avail--free">Free</span></li>` etc.

#### Example: Legend

```django
<ul class="orca-legend"><li><span class="orca-avail orca-avail--free">Free</span></li><li><span class="orca-avail orca-avail--busy">Busy</span></li><li><span class="orca-avail orca-avail--tentative">Tentative</span></li><li><span class="orca-avail orca-avail--off">Not working</span></li></ul>
```

**Classes:** `.orca-legend`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Availability legend

---

## Exception entry

`id: exception-entry` · level: component · source: ORCA

A one-day override of the usual schedule: date, new hours or Closed, and the reason.

Built from: `date-badge`, `badge`, `row-actions`

### Why

Exceptions are where schedules go wrong; listing each with its date and reason makes them visible and reviewable (Peak–end rule, Practical UI S06).

### When to use

- Holidays, special openings, maintenance days.

### How to use

- `<div class="orca-exception">` with a date badge, `.orca-exception__body` (hours or 'Closed' badge + `.orca-exception__meta` reason) and row actions.

#### Example: Exceptions

```django
<div style="max-width: 30rem">
  <div class="orca-exception"><time class="orca-date-badge" datetime="2026-11-11"><span class="orca-date-badge__month">Nov</span><span class="orca-date-badge__day">11</span><span class="orca-date-badge__weekday">Wed</span></time><div class="orca-exception__body"><span><span class="orca-badge orca-badge--grey">Closed</span></span><span class="orca-exception__meta">Armistice Day</span></div><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="Edit 11 November">{% icon "edit" %}</button></div>
  <div class="orca-exception"><time class="orca-date-badge" datetime="2026-12-24"><span class="orca-date-badge__month">Dec</span><span class="orca-date-badge__day">24</span><span class="orca-date-badge__weekday">Thu</span></time><div class="orca-exception__body"><span class="orca-num">08:00–14:00</span><span class="orca-exception__meta">Christmas Eve, short day</span></div><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="Edit 24 December">{% icon "edit" %}</button></div>
</div>
```

**Classes:** `.orca-exception`, `.orca-exception__body`, `.orca-exception__meta`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Practical UI S06: Make essential content visible or discoverable

**ORCA guide items covered:** Exception entry (date override)

---

## Time-off entry

`id: time-off-entry` · level: component · source: ORCA

A person's absence: who, dates, type and approval status.

Built from: `avatar`, `date-label`, `status-chip`

### Why

Planners need who is away, when and whether it is confirmed in one row (Miller's law); status as a word and shape avoids colour-only meaning (C03).

### When to use

- Time-off lists, team calendars, roster sidebars.

### How to use

- `<div class="orca-time-off">` with an avatar, `.orca-time-off__body` (name + dates and length in `__meta`) and a status chip.

#### Example: Time off

```django
<div style="max-width: 32rem">
  <div class="orca-time-off"><span class="orca-avatar orca-avatar--s" aria-hidden="true">GH</span><div class="orca-time-off__body"><span>Grace Hopper · Holiday</span><span class="orca-time-off__meta"><time datetime="2026-11-16">16</time>–<time datetime="2026-11-20">20 November</time> · 5 days</span></div><span class="orca-chip orca-chip--done">Approved</span></div>
  <div class="orca-time-off"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AT</span><div class="orca-time-off__body"><span>Alan Turing · Training</span><span class="orca-time-off__meta"><time datetime="2026-11-23">23 November</time> · 1 day</span></div><span class="orca-chip orca-chip--planned">Requested</span></div>
</div>
```

**Classes:** `.orca-time-off`, `.orca-time-off__body`, `.orca-time-off__meta`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Time-off entry

---

## Booking slot

`id: booking-slot` · level: component · source: ORCA

A bookable time as a large button: free, limited ('2 left'), full or chosen.

Built from: `time-label`

### Why

Seeing all times at once with their availability makes choosing quick (Hick's law); full slots stay visible but struck and dashed so the pattern of the day is clear without colour (C03); large targets suit phones (Fitts's law).

### When to use

- Appointment and booking flows.

### How to use

- `<ul class="orca-booking-slots">` of `<li><button class="orca-booking-slot" type="button" aria-pressed="false">09:30<span class="orca-booking-slot__note">2 left</span></button></li>`.
- Full slots: `disabled` with 'Full' in the note; limited: `--limited`. The chosen slot `aria-pressed="true"`. Group by morning and afternoon.

#### Example: Slots

```django
<ul class="orca-booking-slots" style="max-width: 32rem">
  <li><button class="orca-booking-slot" type="button" aria-pressed="false">09:00<span class="orca-booking-slot__note">Free</span></button></li>
  <li><button class="orca-booking-slot" type="button" aria-pressed="true">09:30<span class="orca-booking-slot__note">Your choice</span></button></li>
  <li><button class="orca-booking-slot orca-booking-slot--limited" type="button" aria-pressed="false">10:00<span class="orca-booking-slot__note">2 left</span></button></li>
  <li><button class="orca-booking-slot" type="button" disabled>10:30<span class="orca-booking-slot__note">Full</span></button></li>
</ul>
```

**Classes:** `.orca-booking-slots`, `.orca-booking-slot`, `.orca-booking-slot__note`, `.orca-booking-slot--limited`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI C03: Communicate meaning beyond colour; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Booking slot

---

## Conflict warning

`id: conflict-warning` · level: component · source: ORCA

A caution message saying what this plan conflicts with and how to resolve it.

Built from: `callout`, `button`

### Why

Conflicts found early are cheap to fix (Peak–end rule: prevent the negative peak); naming the other item and offering the fix turns a warning into a decision.

### When to use

- Saving an event, shift or run that clashes with another one.

### How to use

- A caution callout: title names the conflict ('Grace Hopper is on holiday that day'), body names the other item with a link, actions offer the fixes ('Pick another person', 'Save anyway').
- Use caution when saving is still allowed; negative when it is blocked.

#### Example: Conflict

```django
<div class="orca-callout orca-callout--caution" role="status">{% icon "warning" %}<p class="orca-callout__title">Grace Hopper is on holiday on 18 November</p><div class="orca-callout__body"><p class="orca-p">See <a class="orca-link" href="#">time off, 16–20 November</a>.</p><div class="orca-row"><button class="orca-button orca-button--dense" type="button">Pick another person</button><button class="orca-button orca-button--link" type="button">Save anyway</button></div></div></div>
```

**Classes:** `.orca-callout--caution`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Practical UI W15: Help people recover from errors

**ORCA guide items covered:** Conflict warning

---

## Overlap warning

`id: overlap-warning` · level: component · source: ORCA

An inline message under a schedule row whose times overlap another row.

Built from: `error-text`, `schedule-row`

### Why

Pointing at the exact row and the row it overlaps lets people fix it in place (Practical UI R21, W15).

### When to use

- Schedule editors, as rows change (after leaving the field).

### How to use

- A `.orca-error` (or caution `.orca-help` with the warning icon when allowed) as `.orca-schedule-row__msg` inside the row: 'Overlaps Monday 08:00–12:00. Change the start or remove one row.'
- Link it with `aria-describedby` from both time inputs.

#### Example: Overlap

```django
<p class="orca-error">{% icon "error" %}<span>Overlaps Monday 08:00–12:00. Change the start or remove one of the rows.</span></p>
```

**Classes:** `.orca-schedule-row__msg`

**Principles applied:** Practical UI R21: Validate after leaving a field when context matters; Practical UI W15: Help people recover from errors

**ORCA guide items covered:** Overlap warning

---

## Working-hours label

`id: working-hours-label` · level: component · source: ORCA

'Open now, closes at 18:00' or 'Closed, opens Monday 08:00', with a status dot.

Built from: `status-dot`, `time-label`

### Why

People want to know whether a place is open now and when that changes (Tesler's law: the system does the arithmetic); the word carries the state, the dot confirms it (C03).

### When to use

- Site headers, booking pages, contact blocks.

### How to use

- `<span class="orca-working-hours">` with a status dot, `.orca-working-hours__state` ('Open') and the next change ('closes at 18:00').
- Compute in the site's timezone; mention it when it differs from the reader's.

#### Example: Open and closed

```django
<div class="orca-stack"><span class="orca-working-hours"><span class="orca-dot orca-dot--positive"></span><span class="orca-working-hours__state">Open</span>closes at <time datetime="18:00">18:00</time></span><span class="orca-working-hours"><span class="orca-dot"></span><span class="orca-working-hours__state">Closed</span>opens Monday at <time datetime="08:00">08:00</time></span></div>
```

**Classes:** `.orca-working-hours`, `.orca-working-hours__state`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Working-hours label

---
