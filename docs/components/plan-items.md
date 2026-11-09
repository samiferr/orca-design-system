# Plan items

Tasks, milestones, deadlines and reminders, and the chips that describe them: assignee, due date, status, priority, progress.

## Task item

`id: task-item` · level: component · source: ORCA

A task row: completion checkbox, title and chips for assignee, due date and priority.

Built from: `checkbox`, `assignee-chip`, `due-date-chip`, `priority-chip`

### Why

The checkbox is the fastest way to complete a task in place (Fitts's law); chips in a fixed order make many tasks scannable (Miller's law).

### When to use

- Task lists, checklists, project and run follow-ups.

### How to use

- `<div class="orca-task">` with a checkbox (label = task title for screen readers), `.orca-task__title`, `.orca-task__meta` chips and optional `.orca-task__end` actions.
- Done: `--done` strikes the title; save immediately and offer Undo in a toast.

#### Example: Tasks

```django
<div style="max-width: 36rem">
  <div class="orca-task"><label class="orca-check"><input type="checkbox" aria-label="Trim Entrance A video"><span class="orca-check__box"></span></label><span class="orca-task__title">Trim Entrance A video</span>
    <div class="orca-task__meta"><span class="orca-chip"><span class="orca-avatar orca-avatar--xs" aria-hidden="true">AL</span><span class="orca-chip__text">Ada Lovelace</span></span><span class="orca-chip orca-chip--soon">{% icon "calendar" %}Due tomorrow</span><span class="orca-chip"><span class="orca-priority orca-priority--high"><span class="orca-priority__bars" aria-hidden="true"><i></i><i></i><i></i></span>High</span></span></div></div>
  <div class="orca-task orca-task--done"><label class="orca-check"><input type="checkbox" checked aria-label="Draw zones for Gate 1"><span class="orca-check__box"></span></label><span class="orca-task__title">Draw zones for Gate 1</span><div class="orca-task__meta"><span class="orca-chip orca-chip--done">Done</span></div></div>
</div>
```

**Classes:** `.orca-task`, `.orca-task__title`, `.orca-task__meta`, `.orca-task__end`, `.orca-task--done`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Miller's law: chunk information so working memory is not overloaded; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Task item

---

## Subtask item

`id: subtask-item` · level: component · source: ORCA

A smaller, indented task under its parent with a connecting line.

Built from: `task-item`, `progress-chip`

### Why

Indentation and a guide line show which task each step belongs to (Gestalt, Practical UI L01); a smaller style keeps the parent dominant.

### When to use

- Breaking a task into steps.

### How to use

- `<div class="orca-task orca-task--sub">` after the parent; show the parent's progress as a progress chip ('2/5').

#### Example: Subtasks

```django
<div style="max-width: 36rem">
  <div class="orca-task"><label class="orca-check"><input type="checkbox" aria-label="Upload Gate 1 video"><span class="orca-check__box"></span></label><span class="orca-task__title">Upload Gate 1 video</span><div class="orca-task__meta"><span class="orca-chip"><span class="orca-chip__bar" style="--orca-value: 50%"><span></span></span>1/2</span></div></div>
  <div class="orca-task orca-task--sub orca-task--done"><label class="orca-check"><input type="checkbox" checked aria-label="Mount bracket"><span class="orca-check__box"></span></label><span class="orca-task__title">Mount bracket</span></div>
  <div class="orca-task orca-task--sub"><label class="orca-check"><input type="checkbox" aria-label="Connect to media server"><span class="orca-check__box"></span></label><span class="orca-task__title">Connect to media server</span></div>
</div>
```

**Classes:** `.orca-task--sub`

**Principles applied:** Practical UI L01: Group related information; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Subtask item

---

## Milestone item

`id: milestone-item` · level: component · source: ORCA

A milestone row: diamond marker, name, date and state in words.

Built from: `milestone-marker`, `date-label`, `status-chip`

### Why

Milestones are the checkpoints of a plan; the diamond is their familiar symbol (Jakob's law) and the state word makes 'missed' unmistakable (C03).

### When to use

- Roadmaps, project overviews, milestone timelines.

### How to use

- `<div class="orca-plan-row">` with a milestone marker, `.orca-plan-row__body` (name + `__meta` date) and a status chip.

#### Example: Milestones

```django
<div style="max-width: 32rem">
  <div class="orca-plan-row"><span class="orca-milestone orca-milestone--done" aria-hidden="true"></span><span class="orca-plan-row__body"><span>Pilot live</span><span class="orca-plan-row__meta">3 March 2026</span></span><span class="orca-chip orca-chip--done">Reached</span></div>
  <div class="orca-plan-row"><span class="orca-milestone orca-milestone--upcoming" aria-hidden="true"></span><span class="orca-plan-row__body"><span>All sites live</span><span class="orca-plan-row__meta">1 December 2026 · in 25 days</span></span><span class="orca-chip orca-chip--planned">Planned</span></div>
</div>
```

**Classes:** `.orca-plan-row`, `.orca-plan-row__body`, `.orca-plan-row__meta`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Milestone item

---

## Deadline item

`id: deadline-item` · level: component · source: ORCA

A deadline row: flag, name, due date and how long is left or how late it is.

Built from: `deadline-marker`, `overdue-marker`, `due-date-chip`

### Why

Time left is what people act on (Tesler's law: compute it for them); turning amber when close and red when late, with words, prevents surprises (Peak–end rule, C03).

### When to use

- Deadline lists, compliance dates, renewals.

### How to use

- `.orca-plan-row` with the deadline marker icon, the body (name + due date) and either a due-date chip (`--soon`) or an overdue marker.

#### Example: Deadlines

```django
<div style="max-width: 32rem">
  <div class="orca-plan-row">{% icon "flag" %}<span class="orca-plan-row__body"><span>Licence renewal</span><span class="orca-plan-row__meta">Due 9 November 2026</span></span><span class="orca-chip orca-chip--soon">{% icon "calendar" %}In 3 days</span></div>
  <div class="orca-plan-row">{% icon "flag" %}<span class="orca-plan-row__body"><span>Quarterly report</span><span class="orca-plan-row__meta">Due 4 November 2026</span></span><span class="orca-overdue">{% icon "error" %}Overdue by 2 days</span></div>
</div>
```

**Classes:** `.orca-plan-row`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Peak–end rule: people judge an experience by its peak and its end; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Deadline item

---

## Reminder item

`id: reminder-item` · level: component · source: ORCA

A reminder that has come due: bell, text, time and Snooze or Done.

Built from: `planning-icons`, `button`, `relative-time`

### Why

A reminder is useful only if it can be acted on in place (Fitts's law); Snooze moves it without losing it (Postel's law).

### When to use

- Notification lists, task sidebars.

### How to use

- `.orca-plan-row` with the bell icon, the body (text + time) and two small buttons: Snooze (menu of times) and Done.

#### Example: Reminder

```django
<div class="orca-plan-row" style="max-width: 34rem">{% icon "notifications" %}<span class="orca-plan-row__body"><span>Check Gate 1 framing after install</span><span class="orca-plan-row__meta"><time datetime="2026-11-06T09:00">Today, 09:00</time></span></span><span class="orca-row"><button class="orca-button orca-button--sm" type="button">Snooze</button><button class="orca-button orca-button--sm" type="button">Done</button></span></div>
```

**Classes:** `.orca-plan-row`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Reminder item

---

## Assignee chip

`id: assignee-chip` · level: component · source: ORCA

A small avatar and name showing who is responsible.

Built from: `avatar`

### Why

A face and name identify the owner faster than a name alone (Miller's law); 'Unassigned' is shown explicitly so gaps are visible.

### When to use

- Tasks, board cards, tickets.

### How to use

- `<span class="orca-chip"><span class="orca-avatar orca-avatar--xs" aria-hidden="true">AL</span><span class="orca-chip__text">Ada Lovelace</span></span>`; unassigned: the user icon and 'Unassigned'.

#### Example: Chips

```django
<div class="orca-row"><span class="orca-chip"><span class="orca-avatar orca-avatar--xs" aria-hidden="true">AL</span><span class="orca-chip__text">Ada Lovelace</span></span><span class="orca-chip">{% icon "user" %}<span class="orca-chip__text">Unassigned</span></span></div>
```

**Classes:** `.orca-chip`, `.orca-chip__text`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI S06: Make essential content visible or discoverable

**ORCA guide items covered:** Assignee chip

---

## Due-date chip

`id: due-date-chip` · level: component · source: ORCA

A calendar icon and the due date, amber when close, red and bold when overdue.

Built from: `planning-icons`, `date-label`

### Why

Relative due dates ('Tomorrow') are faster to act on; the shift in border, weight and word as it approaches keeps it from relying on colour (C03, Peak–end rule).

### When to use

- Tasks, cards, deadlines.

### How to use

- `<span class="orca-chip">{% icon "calendar" %}<time datetime=…>Fri 13 Nov</time></span>`; `--soon` within 2 days; `--overdue` with 'Overdue, 4 Nov'.

#### Example: Due dates

```django
<div class="orca-row"><span class="orca-chip">{% icon "calendar" %}<time datetime="2026-11-13">Fri 13 Nov</time></span><span class="orca-chip orca-chip--soon">{% icon "calendar" %}Tomorrow</span><span class="orca-chip orca-chip--overdue">{% icon "calendar" %}Overdue, 4 Nov</span></div>
```

**Classes:** `.orca-chip`, `.orca-chip--soon`, `.orca-chip--overdue`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Peak–end rule: people judge an experience by its peak and its end; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Due-date chip

---

## Status chip (planned, in progress, done, overdue)

`id: status-chip` · level: component · source: ORCA

A plan item's state with a distinct shape per state: empty circle, half circle, full circle, square.

Built from: `badge`

### Why

Each state has its own shape so states are told apart in greyscale (Practical UI C03); words stay consistent across the product (W10).

### When to use

- Tasks, milestones, runs, requests.

### How to use

- `<span class="orca-chip orca-chip--planned">Planned</span>`, `--progress` (In progress), `--done` (Done), `--blocked` (Blocked), `--overdue` (Overdue).

#### Example: States

```django
<div class="orca-row"><span class="orca-chip orca-chip--planned">Planned</span><span class="orca-chip orca-chip--progress">In progress</span><span class="orca-chip orca-chip--done">Done</span><span class="orca-chip orca-chip--blocked">Blocked</span><span class="orca-chip orca-chip--overdue">Overdue</span></div>
```

**Classes:** `.orca-chip--planned`, `.orca-chip--progress`, `.orca-chip--done`, `.orca-chip--blocked`, `.orca-chip--overdue`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI W10: Use one term for one concept

**ORCA guide items covered:** Status chip (planned, in progress, done, overdue)

---

## Priority chip

`id: priority-chip` · level: component · source: ORCA

The priority marker in a chip, for use among other chips.

Built from: `priority-marker`

### Why

Bars rising with priority and a word work without colour (C03), and the chip aligns with other metadata (Practical UI F09).

### When to use

- Tasks and board cards.

### How to use

- `<span class="orca-chip"><span class="orca-priority orca-priority--medium">…bars…Medium</span></span>`. Omit the chip for 'normal' priority to reduce noise.

#### Example: Priorities

```django
<div class="orca-row"><span class="orca-chip"><span class="orca-priority orca-priority--medium"><span class="orca-priority__bars" aria-hidden="true"><i></i><i></i><i></i></span>Medium</span></span><span class="orca-chip"><span class="orca-priority orca-priority--urgent"><span class="orca-priority__bars" aria-hidden="true"><i></i><i></i><i></i></span>Urgent</span></span></div>
```

**Classes:** `.orca-chip`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI F09: Keep visual and functional behaviour consistent; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Priority chip

---

## Progress chip

`id: progress-chip` · level: component · source: ORCA

A tiny bar and a count ('3/5') of completed sub-items.

Built from: `progress-bar`

### Why

A count is exact and a bar is quick; together they show progress without opening the item (Doherty: visible progress).

### When to use

- Tasks with subtasks, checklists, plans.

### How to use

- `<span class="orca-chip"><span class="orca-chip__bar" style="--orca-value: 60%"><span></span></span>3/5</span>` with an `aria-label` '3 of 5 steps done'.

#### Example: Progress

```django
<span class="orca-chip" aria-label="3 of 5 steps done"><span class="orca-chip__bar" style="--orca-value: 60%"><span></span></span>3/5</span>
```

**Classes:** `.orca-chip`, `.orca-chip__bar`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Progress chip

---

## Gantt bar

`id: gantt-bar` · level: component · source: ORCA

A task as a bar positioned on a time grid, with a progress line and milestones as diamonds.

Built from: `milestone-marker`, `progress-bar`

### Why

Seeing tasks along time shows overlaps, gaps and the critical path at a glance (Gestalt, Practical UI L03); the progress line and late outline add state without colour alone.

### When to use

- Project timelines and roadmaps.

### How to use

- `<div class="orca-gantt" style="--orca-cols: 7">` of `.orca-gantt-row`s: `.orca-gantt-row__label` and `.orca-gantt-row__lane` holding `<a class="orca-gantt-bar" style="--orca-start: 14%; --orca-span: 43%; --orca-progress: 60%">`.
- Variants `--done`, `--late`; milestones are milestone markers with `--orca-start`. Wrap in `.orca-table-wrap` for horizontal scroll; offer a list view for screen readers.

#### Example: Timeline

```django
<div class="orca-table-wrap"><div class="orca-gantt" style="--orca-cols: 7" role="list" aria-label="Installation plan, week 45">
  <div class="orca-gantt-row" role="listitem"><span class="orca-gantt-row__label">Upload videos</span><span class="orca-gantt-row__lane"><a class="orca-gantt-bar orca-gantt-bar--done" href="#" style="--orca-start: 0%; --orca-span: 28%; --orca-progress: 100%">Done</a></span></div>
  <div class="orca-gantt-row" role="listitem"><span class="orca-gantt-row__label">Connect media servers</span><span class="orca-gantt-row__lane"><a class="orca-gantt-bar" href="#" style="--orca-start: 28%; --orca-span: 43%; --orca-progress: 60%">60%</a></span></div>
  <div class="orca-gantt-row" role="listitem"><span class="orca-gantt-row__label">Draw zones</span><span class="orca-gantt-row__lane"><a class="orca-gantt-bar orca-gantt-bar--late" href="#" style="--orca-start: 57%; --orca-span: 28%">Late</a><span class="orca-milestone" style="--orca-start: 92%" role="img" aria-label="Go live milestone"></span></span></div>
</div></div>
```

**Classes:** `.orca-gantt`, `.orca-gantt-row`, `.orca-gantt-row__label`, `.orca-gantt-row__lane`, `.orca-gantt-bar`, `.orca-gantt-bar--done`, `.orca-gantt-bar--late`

**Principles applied:** Practical UI L03: Establish an order of importance; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Gantt bar

---

## Plan card

`id: plan-card` · level: component · source: ORCA

A plan's summary: name, period, progress and counts of open, done and late items.

Built from: `linked-card`, `progress-with-counts`, `status-chip`

### Why

A planner judges a plan by whether it is on track; period, progress and late count in one card answer that at a glance (Miller's law, Peak–end rule).

### When to use

- Lists of plans, sprints, projects.

### How to use

- A linked card with the name, the period as date labels, a progress with counts, and a footer of status chips with counts.

#### Example: Plan

```django
<article class="orca-card orca-card--link" style="max-width: 22rem"><div class="orca-card__body"><p class="orca-card-kicker">Rollout</p><h3 class="orca-card-title"><a class="orca-card__link" href="#">North building go-live</a></h3><p class="orca-card-meta"><time datetime="2026-11-02">2 Nov</time>–<time datetime="2026-12-01">1 Dec 2026</time></p>
  <progress class="orca-progress" value="12" max="20" aria-label="12 of 20 tasks done" style="margin-top: var(--orca-space-8)"></progress></div>
  <div class="orca-card__footer"><span class="orca-chip orca-chip--done">12 done</span><span class="orca-chip orca-chip--progress">6 open</span><span class="orca-chip orca-chip--overdue">2 late</span></div></article>
```

**Classes:** `.orca-card`, `.orca-card--link`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Plan card

---

## Board card

`id: board-card` · level: component · source: ORCA

A card on a kanban board: title, labels, due date, assignee and a drag handle.

Built from: `drag-handle`, `tag`, `due-date-chip`, `avatar`

### Why

Boards show work by state; compact cards with the same slots let people scan a column quickly (Miller's law) and the drag handle with keyboard support makes moving accessible (Postel's law).

### When to use

- Kanban boards and planners.

### How to use

- `<article class="orca-board-card">` with `.orca-board-card__head` (drag handle + `.orca-board-card__title` link), tags, and `.orca-board-card__foot` (due-date chip, priority chip, assignee avatar).
- Offer a 'Move to' menu as the non-drag alternative.

#### Example: Card

```django
<article class="orca-board-card" style="max-width: 18rem"><div class="orca-board-card__head"><button class="orca-drag-handle" type="button" aria-label="Move Trim Entrance A video">{% icon "drag" %}</button><h3 class="orca-board-card__title"><a href="#">Trim Entrance A video</a></h3></div>
  <div class="orca-row"><span class="orca-tag">Video</span><span class="orca-tag">North building</span></div>
  <div class="orca-board-card__foot"><span class="orca-chip orca-chip--soon">{% icon "calendar" %}Tomorrow</span><span class="orca-avatar orca-avatar--xs" title="Ada Lovelace">AL</span></div></article>
```

**Classes:** `.orca-board-card`, `.orca-board-card__head`, `.orca-board-card__title`, `.orca-board-card__foot`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Postel's law: accept varied input, output reliable and accessible UI; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Board card

---

## Resource row

`id: resource-row` · level: component · source: ORCA

A person or resource with their load and a row of day cells showing availability.

Built from: `avatar`, `availability-color`

### Why

Planners assign work by comparing who is free when; aligning every resource on the same day columns makes that comparison visual (Miller's law), and patterns plus counts avoid colour-only meaning (C03).

### When to use

- Capacity planners, rosters, resource schedulers.

### How to use

- `<div class="orca-resource-row" style="--orca-cols: 7">` with `.orca-resource-row__who` (avatar, name, `__load` '32 of 40 h') and `.orca-resource-row__slots` of spans using availability fills and hour counts.
- Give each slot an accessible label ('Monday, 8 h, busy').

#### Example: Two people

```django
<div style="max-width: 40rem">
  <div class="orca-resource-row" style="--orca-cols: 5"><div class="orca-resource-row__who"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span><span>Ada Lovelace</span><br><span class="orca-resource-row__load">32 of 40 h</span></span></div>
    <div class="orca-resource-row__slots"><span class="orca-avail-fill--busy" aria-label="Monday, 8 h, busy">8</span><span class="orca-avail-fill--busy" aria-label="Tuesday, 8 h, busy">8</span><span class="orca-avail-fill--free" aria-label="Wednesday, free">0</span><span class="orca-avail-fill--tentative" aria-label="Thursday, 8 h, tentative">8</span><span class="orca-avail-fill--busy" aria-label="Friday, 8 h, busy">8</span></div></div>
  <div class="orca-resource-row" style="--orca-cols: 5"><div class="orca-resource-row__who"><span class="orca-avatar orca-avatar--s" aria-hidden="true">GH</span><span><span>Grace Hopper</span><br><span class="orca-resource-row__load">On holiday</span></span></div>
    <div class="orca-resource-row__slots">{% for i in "12345" %}<span class="orca-avail-fill--busy orca-small" aria-label="Away">Away</span>{% endfor %}</div></div>
</div>
```

**Classes:** `.orca-resource-row`, `.orca-resource-row__who`, `.orca-resource-row__load`, `.orca-resource-row__slots`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Resource row

---
