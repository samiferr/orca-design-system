# Event editing

Creating, viewing and answering events: full editor, popover, panel, quick add, reminders, attendees and RSVP.

## Event editor

`id: event-editor` · level: pattern · source: ORCA

The full form for an event: title, date and time (or all day), repeat, place, people, reminders, calendar and notes.

Built from: `form-stack`, `datetime-picker`, `recurrence-selector`, `reminder-selector`, `multi-picker`, `conflict-warning`

### Why

Events have many optional fields; putting the essentials first (title, when) and the rest in labelled sections keeps the form short to read (Practical UI F01, F05) while still complete. Defaults (next round half hour, 1 hour, 15-minute reminder) mean most events need two fields (Tesler's law).

### When to use

- Creating or editing an event in full, on its own page or in a drawer.

### How to use

- A form stack: title (autofocus), date-time range with an 'All day' switch, recurrence selector, location, attendees (multi picker), reminders, calendar (select with colour), notes.
- Warn about conflicts inline (conflict warning) without blocking save; keep 'Save' and 'Cancel' at the bottom and 'Delete' apart from them.

#### Example: New event

```django
<form class="orca-form-stack" style="max-width: 32rem" onsubmit="return false">
  <div class="orca-field"><label class="orca-label" for="ee-t">Title</label><input class="orca-input" id="ee-t" value="Audit"></div>
  <fieldset class="orca-inline-fields" data-orca-range><legend class="orca-label">When</legend><div class="orca-field"><label class="orca-label" for="ee-a">Starts</label><input class="orca-input" type="datetime-local" id="ee-a" value="2026-11-06T10:00"></div><span class="orca-inline-fields__sep" aria-hidden="true">–</span><div class="orca-field"><label class="orca-label" for="ee-b">Ends</label><input class="orca-input" type="datetime-local" id="ee-b" value="2026-11-06T11:30"></div><p class="orca-inline-fields__note" data-orca-range-output aria-live="polite">1 h 30 min</p></fieldset>
  <label class="orca-switch"><input type="checkbox" role="switch"><span class="orca-switch__track"></span><span>All day</span></label>
  <div class="orca-field"><label class="orca-label" for="ee-r">Repeat</label><select class="orca-select" id="ee-r"><option>Does not repeat</option><option>Weekly on Friday</option></select></div>
  <div class="orca-field"><label class="orca-label" for="ee-l">Location <span class="orca-optional">(optional)</span></label><input class="orca-input" id="ee-l" value="North building"></div>
  <div class="orca-callout orca-callout--caution" role="status">{% icon "warning" %}<p class="orca-callout__title">Overlaps Supplier call, 10:30–11:00</p></div>
  <div class="orca-form-actions"><button class="orca-button orca-button--primary" type="submit">Save event</button><button class="orca-button" type="button">Cancel</button></div></form>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Form

```python
# events/forms.py
from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "starts_at", "ends_at", "all_day", "place", "calendar", "notes"]
        widgets = {"starts_at": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
                   "ends_at": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M")}

    def clean(self):
        data = super().clean()
        if data.get("starts_at") and data.get("ends_at") and data["ends_at"] <= data["starts_at"]:
            self.add_error("ends_at", "Choose an end after the start.")
        return data
```

**Classes:** `.orca-form-stack`

**Principles applied:** Practical UI F01: Design for a diverse audience; Practical UI F05: Build a design system with tokens and usage guidance; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Event editor

---

## Event detail popover

`id: event-popover` · level: pattern · source: ORCA

A small card that opens over the calendar when an event is clicked: title, time, place, people and quick actions.

Built from: `event-chip`, `panel-header`, `button-group`

### Why

Most clicks on an event just check details; a popover answers in place without losing the calendar (Doherty threshold, Jakob's law) and offers Edit for the rest.

### When to use

- Clicking an event in month, week or day views on wide screens.

### When not to use

- Phones: open the event detail panel as a page or bottom drawer instead.

### How to use

- A native popover: `<div class="orca-event-popover" id="…" popover>` opened by `<button popovertarget="…">` on the event; `--orca-event` colours its edge.
- Head with title and close button; body lines with icons (time, place, calendar); foot with Edit, Delete and 'Open'. Escape and outside click close it (built into popover).

#### Example: Popover

```django
<button class="orca-event-chip" type="button" popovertarget="ep-1" style="max-width: 12rem"><span class="orca-event-dot" style="--orca-event: var(--orca-chart-2)"></span><span class="orca-event-chip__time">10:00</span><span class="orca-event-chip__title">Audit</span></button>
<div class="orca-event-popover" id="ep-1" popover style="--orca-event: var(--orca-chart-2)"><div class="orca-event-popover__head"><h3 class="orca-event-popover__title">Audit</h3><button class="orca-icon-button orca-icon-button--sm" type="button" popovertarget="ep-1" popovertargetaction="hide" aria-label="Close">{% icon "close" %}</button></div>
  <div class="orca-event-popover__body"><span>{% icon "clock" size="xs" %}Friday 6 November, 10:00–11:30</span><span>{% icon "location" size="xs" %}North building</span><span>{% icon "user" size="xs" %}Ada Lovelace, Grace Hopper</span></div>
  <div class="orca-event-popover__foot"><button class="orca-button orca-button--dense" type="button">Edit</button><button class="orca-button orca-button--dense orca-button--ghost" type="button">Delete</button></div></div>
```

**Classes:** `.orca-event-popover`, `.orca-event-popover__head`, `.orca-event-popover__title`, `.orca-event-popover__body`, `.orca-event-popover__foot`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Jakob's law: work the way products people already know work; Practical UI L09: Set spacing by relationship

**ORCA guide items covered:** Event detail popover

---

## Event detail panel

`id: event-detail-panel` · level: pattern · source: ORCA

All of an event's details in a panel or page: title, status, time, place, description, attendees and actions.

Built from: `key-value-list`, `attendee-list`, `invitation-response-bar`, `record-actions`

### Why

When people need the whole event (notes, everyone's answers) a panel gives room and stays readable on phones (Practical UI L01); the coloured top edge ties it to its calendar (Practical UI F09).

### When to use

- Opening an event on phones, from notifications or from lists; a drawer beside the calendar.

### How to use

- `<article class="orca-event-panel" style="--orca-event: …">` with the title, a key–value list (when, where, calendar, repeat), the description, the attendee list and the invitation response bar at the bottom.

#### Example: Audit

```django
<article class="orca-event-panel" style="--orca-event: var(--orca-chart-2)"><div class="orca-row" style="justify-content: space-between"><h2 class="orca-h3" style="margin: 0">Audit</h2><span class="orca-badge orca-badge--subtle orca-badge--caution">Tentative</span></div>
  <dl class="orca-kv"><div><dt>When</dt><dd>Friday 6 November, 10:00–11:30</dd></div><div><dt>Where</dt><dd>North building</dd></div><div><dt>Calendar</dt><dd>Installs and audits</dd></div></dl>
  <p class="orca-p">Yearly count audit with the landlord. Bring the October reports.</p>
  <div class="orca-row"><button class="orca-button" type="button">{% icon "edit" %}Edit</button><button class="orca-button orca-button--ghost" type="button">Duplicate</button></div></article>
```

**Classes:** `.orca-event-panel`

**Principles applied:** Practical UI L01: Group related information; Practical UI F09: Keep visual and functional behaviour consistent

**ORCA guide items covered:** Event detail panel

---

## Quick-add event

`id: quick-add-event` · level: pattern · source: ORCA

One text field that creates an event from a sentence ('Audit Friday 10:00 at North building'), showing what it understood before saving.

Built from: `input-group`

### Why

Typing one sentence is faster than filling a form for simple events (Tesler's law); previewing the parsed date and time prevents wrong events (Practical UI R22).

### When to use

- Fast entry at the top of a calendar or task list; command palettes.

### How to use

- `<form class="orca-quick-add">` with `.orca-quick-add__row` (input + Add button) and `.orca-quick-add__preview` (aria-live) showing the parsed result; parse on the server and return the preview with htmx.
- Link to the full editor for anything more.

#### Example: Quick add

```django
<form class="orca-quick-add" onsubmit="return false"><label class="orca-label" for="qa-i">Add an event</label><div class="orca-quick-add__row"><input class="orca-input" id="qa-i" value="Audit Friday 10:00 at North building" aria-describedby="qa-p"><button class="orca-button orca-button--primary" type="submit">Add</button></div>
  <p class="orca-quick-add__preview" id="qa-p" aria-live="polite">{% icon "calendar" size="xs" %}Audit · Friday 6 November, 10:00–11:00 · North building <a class="orca-link" href="#">More options</a></p></form>
```

**Classes:** `.orca-quick-add`, `.orca-quick-add__row`, `.orca-quick-add__preview`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Practical UI R22: Live feedback only when it helps

**ORCA guide items covered:** Quick-add event

---

## Reminder manager

`id: reminder-manager` · level: pattern · source: ORCA

The list of upcoming reminders with Snooze and Done, and the defaults for new events.

Built from: `reminder-item`, `reminder-selector`

### Why

Reminders only help if acting on them is one tap (Fitts's law); grouping due-now apart from later keeps the urgent ones on top (Von Restorff, Practical UI L03).

### When to use

- A reminders page or panel; notification settings for events.

### How to use

- Groups ('Due now', 'Later today', 'Tomorrow') of reminder items; each has Snooze (with durations in a menu) and Done.
- Below, the default reminders for new events using the reminder selector.

#### Example: Reminders

```django
<div class="orca-stack" style="max-width: 34rem"><h3 class="orca-task-list__group">Due now</h3>
  <div class="orca-plan-row">{% icon "notifications" %}<span class="orca-plan-row__body"><span>Audit at North building</span><span class="orca-plan-row__meta">Starts in 15 minutes</span></span><span class="orca-row"><button class="orca-button orca-button--sm" type="button">Snooze</button><button class="orca-button orca-button--sm" type="button">Done</button></span></div>
  <h3 class="orca-task-list__group">Tomorrow</h3>
  <div class="orca-plan-row">{% icon "notifications" %}<span class="orca-plan-row__body"><span>Licence renewal</span><span class="orca-plan-row__meta">Saturday, 09:00</span></span><span class="orca-row"><button class="orca-button orca-button--sm" type="button">Snooze</button><button class="orca-button orca-button--sm" type="button">Done</button></span></div></div>
```

**Classes:** `.orca-plan-row`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI L03: Establish an order of importance

**ORCA guide items covered:** Reminder manager

---

## Attendee list

`id: attendee-list` · level: pattern · source: ORCA

People invited to an event with their answers, a summary count and controls to add or remove.

Built from: `list-item`, `multi-picker`, `remove-row-button`

### Why

Organisers need to know who is coming at a glance; the summary ('3 yes, 1 waiting') answers first (Practical UI W05) and each answer has an icon and a word, not just a colour.

### When to use

- Event editor and event detail panel.

### How to use

- `<p class="orca-attendees__summary">` then `<ul class="orca-attendees">` of `.orca-attendee`: avatar, name (and role 'Organiser'), and `.orca-attendee__resp--yes|no|maybe|waiting` with icon and text.
- In the editor, add people with a multi picker and remove with an icon button per row.

#### Example: Attendees

```django
<div style="max-width: 26rem"><p class="orca-attendees__summary">2 going, 1 maybe, 1 waiting</p><ul class="orca-attendees">
  <li class="orca-attendee"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span>Ada Lovelace <span class="orca-small orca-muted">Organiser</span></span><span class="orca-attendee__resp orca-attendee__resp--yes">{% icon "success" size="xs" %}Going</span></li>
  <li class="orca-attendee"><span class="orca-avatar orca-avatar--s" aria-hidden="true">GH</span><span>Grace Hopper</span><span class="orca-attendee__resp orca-attendee__resp--yes">{% icon "success" size="xs" %}Going</span></li>
  <li class="orca-attendee"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AT</span><span>Alan Turing</span><span class="orca-attendee__resp orca-attendee__resp--maybe">{% icon "help" size="xs" %}Maybe</span></li>
  <li class="orca-attendee"><span class="orca-avatar orca-avatar--s" aria-hidden="true">KJ</span><span>Katherine Johnson</span><span class="orca-attendee__resp orca-attendee__resp--waiting">{% icon "hourglass" size="xs" %}Waiting</span></li></ul></div>
```

**Classes:** `.orca-attendees`, `.orca-attendee`, `.orca-attendee__resp`, `.orca-attendees__summary`

**Principles applied:** Practical UI W05: Order explanations as an inverted pyramid; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Attendee list

---

## Invitation response bar

`id: invitation-response-bar` · level: pattern · source: ORCA

A bar on an invitation asking 'Going?' with Yes, Maybe and No, showing the current answer.

Built from: `button-group`, `choice-group`

### Why

Answering an invitation should be one click where the question is asked (Fitts's law); the pressed state shows the current answer and can be changed (Practical UI B03).

### When to use

- On an event the viewer is invited to: detail panel, popover, invitation email landing page.

### How to use

- `<div class="orca-rsvp">` with `.orca-rsvp__question` and a segmented group of three buttons using `aria-pressed`; post the answer and update the attendee list.
- Offer 'Add a note' only after answering.

#### Example: Going?

```django
<div class="orca-rsvp" style="max-width: 32rem"><span class="orca-rsvp__question">Going?</span><div class="orca-segmented orca-segmented--dense" role="group" aria-label="Your answer"><button class="orca-segmented__item" type="button" aria-pressed="true">Yes</button><button class="orca-segmented__item" type="button" aria-pressed="false">Maybe</button><button class="orca-segmented__item" type="button" aria-pressed="false">No</button></div></div>
```

**Classes:** `.orca-rsvp`, `.orca-rsvp__question`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI B03: One primary action

**ORCA guide items covered:** Invitation response bar

---
