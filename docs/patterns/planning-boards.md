# Planning boards and timelines

Show and manage work over time: task lists, boards, Gantt charts, roadmaps, milestones, capacity, deadlines and plan summaries.

## Task list

`id: task-list` · level: pattern · source: ORCA

Tasks grouped by status or due date, each with checkbox, assignee, due date and status, plus a row to add more.

Built from: `task-item`, `status-chip`

### General description

A list of things to do, each with a checkbox so people can tick them off. Tasks often show who owns them and when they are due.

#### Use cases

- Personal to-do lists and team checklists.
- Showing the open steps of a project or record.
- Tracking what is due this week.

#### When not to use it

- Work with several stages needs a board, not a flat list.
- Tasks with dependencies and dates are clearer on a Gantt chart.

#### Best practices

- Group tasks by status or due date so the list is easy to scan.
- Let people add a task right in the list.
- Show who owns each task and when it is due.
- Offer undo after a task is ticked off by mistake.
- Put overdue tasks first.

### When to use

- Personal and team to-dos, and tasks tied to one record (a video's maintenance).

### How to use

- `<div class="orca-task-list">` with `h3.orca-task-list__group` headings and task items, ending with `.orca-task-list__add` (input + Add).
- Ticking saves at once (htmx) and moves the task to Done with an undo toast. Sort overdue tasks first.

#### Example: Tasks

```django
<div class="orca-task-list" style="max-width: 40rem">
  <h3 class="orca-task-list__group">This week</h3>
  {% for t in sample.tasks %}
    <div class="orca-task{% if t.status == "done" %} orca-task--done{% endif %}">
      <label class="orca-check">
        <input type="checkbox" aria-label="{{ t.title }}"{% if t.status == "done" %} checked{% endif %}>
        <span class="orca-check__box"></span>
      </label>
      <span class="orca-task__title">{{ t.title }}</span>
      <div class="orca-task__meta">
        <span class="orca-avatar orca-avatar--xs" aria-hidden="true">{{ t.assignee }}</span>
        {% if t.status != "done" %}
          <span class="orca-chip{% if t.due_state %} orca-chip--{{ t.due_state }}{% endif %}">
            {% icon "calendar" %}
            {{ t.due }}
          </span>
        {% endif %}
        <span class="orca-chip orca-chip--{{ t.status }}">{{ t.status|capfirst }}</span>
      </div>
    </div>
  {% endfor %}
  <form class="orca-task-list__add" onsubmit="return false">
    <input class="orca-input orca-input--dense" aria-label="New task" placeholder="Add a task">
    <button class="orca-button orca-button--dense" type="submit">Add</button>
  </form>
</div>
```

**Classes:** `.orca-task-list`, `.orca-task-list__group`, `.orca-task-list__add`

**Principles applied:** Jakob's law: work the way products people already know work; Peak–end rule: people judge an experience by its peak and its end; Practical UI L09: Set spacing by relationship

**ORCA guide items covered:** Task list

---

## Kanban board

`id: kanban-board` · level: pattern · source: ORCA

Status columns of cards that move by drag and drop or a 'Move to' menu, with work-in-progress limits.

Built from: `board-card`, `column-header`, `dropdown-menu`

### General description

A board of columns, one per stage of work, with cards that move from left to right as work progresses. It makes the flow of work visible.

#### Use cases

- Team workflows with a few stages.
- Support tickets, hiring pipelines or installation jobs.
- Spotting bottlenecks where cards pile up.

#### When not to use it

- Hundreds of cards or many columns are hard to read; use a filtered table.
- Work with fixed dates is better shown on a timeline.

#### Best practices

- Keep to a handful of columns with clear names.
- Limit how many cards can be in progress at once.
- Offer a non-drag way to move cards, for keyboard and touch.
- Keep card content short: title, owner and date.
- Show a count at the top of each column.

### When to use

- Team workflows with a few stages, such as installation jobs or support tickets.

### When not to use

- More than ~6 columns or hundreds of cards: use a table with a status filter.

### How to use

- `<div class="orca-board" data-orca-board>` of `section.orca-board__col` each with a head (name, `[data-orca-count]` badge, `.orca-board__limit`) and `<ul class="orca-board__cards" data-orca-column="key">` of board cards with `draggable="true"` and an `id`.
- Save on the `orca:moved` event (`detail.id`, `from`, `to`). Give each card a 'Move to' dropdown for keyboard and touch.
- Mark a column `is-over` when its count exceeds the limit.

### Accessibility

- Drag and drop is never the only way: each card has a 'Move to' menu; moves are announced.

#### Example: Board

```django
<div class="orca-board" data-orca-board aria-label="Installation board">
  <section class="orca-board__col" aria-label="Planned">
    <h3 class="orca-board__head">Planned <span class="orca-badge orca-badge--grey" data-orca-count>1</span></h3>
    <ul class="orca-board__cards" data-orca-column="planned">
      <li class="orca-board-card" id="kb-1" draggable="true">
        <div class="orca-board-card__head">
          <button class="orca-drag-handle" type="button" aria-label="Move Draw zones for Gate 1">
            {% icon "drag" %}
          </button>
          <h4 class="orca-board-card__title">
            <a href="#">Draw zones for Gate 1</a>
          </h4>
        </div>
        <div class="orca-row">
          <span class="orca-tag">Zones</span>
        </div>
        <div class="orca-board-card__foot">
          <span class="orca-chip">
            {% icon "calendar" %}
            Fri 13 Nov
          </span>
          <span class="orca-avatar orca-avatar--xs" title="GH">GH</span>
        </div>
      </li>
    </ul>
  </section>
  <section class="orca-board__col" aria-label="In progress">
    <h3 class="orca-board__head">In progress <span class="orca-badge orca-badge--grey" data-orca-count>2</span><span class="orca-board__limit">limit 2</span></h3>
    <ul class="orca-board__cards" data-orca-column="progress">
      <li class="orca-board-card" id="kb-2" draggable="true">
        <div class="orca-board-card__head">
          <button class="orca-drag-handle" type="button" aria-label="Move Trim Entrance A video">
            {% icon "drag" %}
          </button>
          <h4 class="orca-board-card__title">
            <a href="#">Trim Entrance A video</a>
          </h4>
        </div>
        <div class="orca-row">
          <span class="orca-tag">Video</span>
        </div>
        <div class="orca-board-card__foot">
          <span class="orca-chip orca-chip--soon">
            {% icon "calendar" %}
            Tomorrow
          </span>
          <span class="orca-avatar orca-avatar--xs" title="AL">AL</span>
        </div>
      </li>
      <li class="orca-board-card" id="kb-3" draggable="true">
        <div class="orca-board-card__head">
          <button class="orca-drag-handle" type="button" aria-label="Move Connect Gate 1 media server">
            {% icon "drag" %}
          </button>
          <h4 class="orca-board-card__title">
            <a href="#">Connect Gate 1 media server</a>
          </h4>
        </div>
        <div class="orca-row">
          <span class="orca-tag">Network</span>
        </div>
        <div class="orca-board-card__foot">
          <span class="orca-chip">
            {% icon "calendar" %}
            Mon 9 Nov
          </span>
          <span class="orca-avatar orca-avatar--xs" title="AT">AT</span>
        </div>
      </li>
    </ul>
  </section>
  <section class="orca-board__col" aria-label="Done">
    <h3 class="orca-board__head">Done <span class="orca-badge orca-badge--grey" data-orca-count>1</span></h3>
    <ul class="orca-board__cards" data-orca-column="done">
      <li class="orca-board-card" id="kb-4" draggable="true">
        <div class="orca-board-card__head">
          <button class="orca-drag-handle" type="button" aria-label="Move Mount Gate 1 bracket">
            {% icon "drag" %}
          </button>
          <h4 class="orca-board-card__title">
            <a href="#">Mount Gate 1 bracket</a>
          </h4>
        </div>
        <div class="orca-row">
          <span class="orca-tag">Install</span>
        </div>
        <div class="orca-board-card__foot">
          <span class="orca-chip">
            {% icon "calendar" %}
            2 Nov
          </span>
          <span class="orca-avatar orca-avatar--xs" title="AT">AT</span>
        </div>
      </li>
    </ul>
  </section>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Board view and move endpoint

```python
# tasks/views.py
import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from .models import Task


class Board(TemplateView):
    template_name = "orca/layouts/board.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        tasks = Task.objects.select_related("assignee")
        ctx["board_columns"] = [
            {"key": key, "name": name, "limit": 4 if key == "progress" else None,
             "cards": [{"id": t.pk, "title": t.title, "url": t.get_absolute_url(), "tags": t.tag_names,
                        "due": t.due.strftime("%a %-d %b") if t.due else "", "due_state": t.due_state,
                        "assignee": t.assignee.get_full_name() if t.assignee else ""}
                       for t in tasks if t.status == key]}
            for key, name in Task.Status.choices
        ]
        ctx["title"] = "Board"
        return ctx


@login_required
@require_POST
def move_task(request):
    """Called by the page script when a card is dropped in another column."""
    data = json.loads(request.body)
    task = get_object_or_404(Task, pk=data["id"].removeprefix("card-"))
    task.status = data["to"]
    task.save(update_fields=["status"])
    return JsonResponse({"ok": True})


# The page script (in {% block extra_scripts %}): send each move to the view.
#   document.addEventListener("orca:moved", (e) => fetch("/tasks/move/", {
#     method: "POST", headers: {"X-CSRFToken": csrftoken, "Content-Type": "application/json"},
#     body: JSON.stringify(e.detail),   // {id: "card-12", from: "planned", to: "progress"}
#   }));
```

**Classes:** `.orca-board`, `.orca-board__col`, `.orca-board__head`, `.orca-board__limit`, `.orca-board__cards`

**Principles applied:** Practical UI L01: Group related information; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Kanban board

---

## Gantt chart

`id: gantt-chart` · level: pattern · source: ORCA

Task bars on a time scale, showing progress, dependencies, milestones and a today line.

Built from: `gantt-bar`, `milestone-item`

### General description

A chart that shows tasks as horizontal bars along a time scale. It shows when each task starts and ends, how tasks overlap and how far along they are.

#### Use cases

- Planning projects with dated tasks and dependencies.
- Tracking rollouts or installations over weeks.
- Seeing which tasks are running late.

#### When not to use it

- Work without dates is better on a board or task list.
- High-level plans for stakeholders suit a roadmap.

#### Best practices

- Mark today with a clear line.
- Show progress inside each bar.
- Label late tasks with a word, not only a colour.
- Order tasks so dependencies read top to bottom.
- Keep the time scale short enough to read without scrolling.

### When to use

- Projects with dated, dependent tasks, such as rollouts and installations.

### When not to use

- Undated work: use a board or task list.

### How to use

- `<div class="orca-gantt-chart" style="--orca-cols: 7">` with `.orca-gantt-chart__scale` (label column then period labels, `is-today`), then the Gantt rows, and `.orca-gantt-chart__today` with `--orca-at` (0–1) inside the gantt.
- Compute the `--orca-start` and `--orca-span` percentages in the view. Late bars get the late modifier and the word 'Late'.

#### Example: Week 45

```django
<div class="orca-table-wrap">
  <div class="orca-gantt-chart" style="--orca-cols: 7">
    <div class="orca-gantt-chart__scale">
      <span></span>
      <span>Mon 2</span>
      <span>Tue 3</span>
      <span>Wed 4</span>
      <span>Thu 5</span>
      <span class="is-today">Fri 6</span>
      <span>Sat 7</span>
      <span>Sun 8</span>
    </div>
    <div class="orca-gantt" style="--orca-cols: 7" role="list" aria-label="Installation plan, week 45">
      <span class="orca-gantt-chart__today" style="--orca-at: 0.64" aria-hidden="true"></span>
      <div class="orca-gantt-row" role="listitem">
        <span class="orca-gantt-row__label">Upload videos</span>
        <span class="orca-gantt-row__lane">
          <a class="orca-gantt-bar orca-gantt-bar--done" href="#" style="--orca-start: 0%; --orca-span: 28%; --orca-progress: 100%">Done</a>
        </span>
      </div>
      <div class="orca-gantt-row" role="listitem">
        <span class="orca-gantt-row__label">Connect media servers</span>
        <span class="orca-gantt-row__lane">
          <a class="orca-gantt-bar" href="#" style="--orca-start: 28%; --orca-span: 43%; --orca-progress: 60%">60%</a>
        </span>
      </div>
      <div class="orca-gantt-row" role="listitem">
        <span class="orca-gantt-row__label">Draw zones</span>
        <span class="orca-gantt-row__lane">
          <a class="orca-gantt-bar orca-gantt-bar--late" href="#" style="--orca-start: 43%; --orca-span: 28%">Late</a>
          <span class="orca-milestone" style="--orca-start: 92%" role="img" aria-label="Go live milestone, Sunday 8"></span>
        </span>
      </div>
    </div>
  </div>
</div>
```

**Classes:** `.orca-gantt-chart`, `.orca-gantt-chart__scale`, `.orca-gantt-chart__today`

**Principles applied:** Practical UI L01: Group related information; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Gantt chart

---

## Roadmap

`id: roadmap` · level: pattern · source: ORCA

Lanes of themes or teams across quarters or months, with each item in its planned period.

Built from: `gantt-bar`

### General description

A high-level plan showing what is planned for which period, such as quarters or Now, Next and Later. It shares direction without promising exact dates.

#### Use cases

- Sharing product or rollout plans with stakeholders.
- Showing themes of work across the year.
- Aligning teams on priorities.

#### When not to use it

- Day-level scheduling belongs on a Gantt chart.
- A single list of to-dos belongs in a task list.

#### Best practices

- Use coarse periods so the plan does not promise too much.
- Group work into lanes by theme or team.
- Highlight the current period.
- Keep item names short and in plain words.
- Update it regularly so it stays trusted.

### When to use

- Product and rollout plans shared with stakeholders.

### When not to use

- Day-level scheduling: use a Gantt chart.

### How to use

- `<div class="orca-roadmap" style="--orca-cols: 4">`: a corner then `.orca-roadmap__head` per period (current one `is-now`), then per lane `.orca-roadmap__lane` and one `.orca-roadmap__cell` per period holding `.orca-roadmap__item` links (`--orca-event` for the theme colour).

#### Example: 2026–27

```django
<div class="orca-table-wrap">
  <div class="orca-roadmap" style="--orca-cols: 4">
    <span></span>
    <span class="orca-roadmap__head">Q3 2026</span>
    <span class="orca-roadmap__head is-now">Q4 2026</span>
    <span class="orca-roadmap__head">Q1 2027</span>
    <span class="orca-roadmap__head">Q2 2027</span>
    <span class="orca-roadmap__lane">Counting</span>
    <div class="orca-roadmap__cell">
      <a class="orca-roadmap__item" href="#" style="--orca-event: var(--orca-chart-1)">Zone counts</a>
    </div>
    <div class="orca-roadmap__cell">
      <a class="orca-roadmap__item" href="#" style="--orca-event: var(--orca-chart-1)">Dwell time</a>
    </div>
    <div class="orca-roadmap__cell">
      <a class="orca-roadmap__item" href="#" style="--orca-event: var(--orca-chart-1)">Queue length</a>
    </div>
    <div class="orca-roadmap__cell"></div>
    <span class="orca-roadmap__lane">Sites</span>
    <div class="orca-roadmap__cell"></div>
    <div class="orca-roadmap__cell">
      <a class="orca-roadmap__item" href="#" style="--orca-event: var(--orca-chart-3)">Warehouse live</a>
      <a class="orca-roadmap__item" href="#" style="--orca-event: var(--orca-chart-3)">Car park live</a>
    </div>
    <div class="orca-roadmap__cell">
      <a class="orca-roadmap__item" href="#" style="--orca-event: var(--orca-chart-3)">Second city</a>
    </div>
    <div class="orca-roadmap__cell"></div>
  </div>
</div>
```

**Classes:** `.orca-roadmap`, `.orca-roadmap__head`, `.orca-roadmap__lane`, `.orca-roadmap__cell`, `.orca-roadmap__item`

**Principles applied:** Practical UI L01: Group related information; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Roadmap

---

## Milestone timeline

`id: milestone-timeline` · level: pattern · source: ORCA

Key dates on one line: reached, next and upcoming milestones with their dates.

Built from: `milestone-item`

### General description

A line of key dates that marks important points in a project, showing which are reached and which are still ahead.

#### Use cases

- Project overviews and status reports.
- Onboarding or customer journeys.
- Showing how far a rollout has come.

#### When not to use it

- Detailed task scheduling needs a Gantt chart.
- A long list of dates is better shown as a deadline list.

#### Best practices

- Keep to a handful of milestones, about 3 to 7.
- Show each date next to its name.
- Make reached and upcoming milestones look different, and say which in words.
- Point out the next milestone and how soon it is.

### When to use

- Project overviews, status reports, onboarding journeys.

### How to use

- `<ol class="orca-milestones" style="--orca-cols: 4">` of items with a milestone marker (done or upcoming), `.orca-milestones__name` and the date.
- Keep to 3–7 milestones; the next one carries 'in N days'.

#### Example: Rollout

```django
<div class="orca-table-wrap">
  <ol class="orca-milestones" style="--orca-cols: 4">
    <li>
      <span class="orca-milestone orca-milestone--done" aria-hidden="true"></span>
      <span class="orca-milestones__name">Pilot live</span>
      <span class="orca-muted">3 March 2026 · reached</span>
    </li>
    <li>
      <span class="orca-milestone orca-milestone--done" aria-hidden="true"></span>
      <span class="orca-milestones__name">North building</span>
      <span class="orca-muted">2 November · reached</span>
    </li>
    <li>
      <span class="orca-milestone orca-milestone--upcoming" aria-hidden="true"></span>
      <span class="orca-milestones__name">All sites live</span>
      <span>1 December · in 25 days</span>
    </li>
    <li>
      <span class="orca-milestone orca-milestone--upcoming" aria-hidden="true"></span>
      <span class="orca-milestones__name">Second city</span>
      <span class="orca-muted">March 2027</span>
    </li>
  </ol>
</div>
```

**Classes:** `.orca-milestones`, `.orca-milestones__name`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Milestone timeline

---

## Sprint or period overview

`id: period-overview` · level: pattern · source: ORCA

A sprint or period at a glance: dates, days left, goal, progress, plan summary and open work.

Built from: `summary-tiles`, `planning-summary`, `period-selector`, `callout`

### General description

A summary page for a sprint, month or other period. It shows the dates, the goal, progress and the work still open.

#### Use cases

- Sprint pages in software teams.
- Monthly plans and reviews.
- Campaign periods with a goal and a deadline.

#### When not to use it

- A single task list is enough when there is no goal or period.
- Long-term direction belongs on a roadmap.

#### Best practices

- Show days left next to progress.
- State the goal in one sentence.
- Count done, open and late work separately.
- Let people switch to the previous or next period.
- Link each number to the tasks behind it.

### When to use

- Sprint pages, monthly plans, campaign periods.

### How to use

- `<div class="orca-period-overview">` with a page head (period name, dates, period selector), summary tiles (done, open, late, days left), the goal callout, the planning summary and a task list or board.

#### Example: Sprint 45

```django
<div class="orca-period-overview" style="max-width: 44rem">
  <div class="orca-row" style="justify-content: space-between">
    <div>
      <h2 class="orca-h3" style="margin: 0">Sprint 45</h2>
      <p class="orca-small orca-muted">2–13 November · 5 working days left</p>
    </div>
    <nav class="orca-segmented orca-segmented--dense" aria-label="Sprint">
      <a class="orca-segmented__item" href="#">44</a>
      <a class="orca-segmented__item" href="#" aria-current="page">45</a>
      <a class="orca-segmented__item" href="#">46</a>
    </nav>
  </div>
  <div class="orca-callout">
    {% icon "flag" %}
    <p class="orca-callout__title">Goal: Warehouse videos published by Friday 13</p>
  </div>
  <dl class="orca-summary-tiles">
    <div class="orca-summary-tile">
      <dt>Done</dt>
      <dd>12</dd>
    </div>
    <div class="orca-summary-tile">
      <dt>Open</dt>
      <dd>6</dd>
    </div>
    <div class="orca-summary-tile">
      <dt>Late</dt>
      <dd>2</dd>
    </div>
  </dl>
  <progress class="orca-progress" value="12" max="20" aria-label="12 of 20 tasks done"></progress>
</div>
```

**Classes:** `.orca-period-overview`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Sprint or period overview

---

## Capacity planner

`id: capacity-planner` · level: pattern · source: ORCA

One row per person showing booked hours per day against capacity, with totals and over-allocation flagged.

Built from: `resource-row`, `availability-legend`

### General description

A grid of people against days that shows how many hours each person is booked compared with what they can do. It makes overloaded people easy to spot.

#### Use cases

- Assigning tasks or shifts fairly.
- Weekly planning meetings.
- Checking whether a team can take on more work.

#### When not to use it

- Tracking tasks themselves is better in a task list or board.
- Showing availability only is clearer in a calendar.

#### Best practices

- Show each person's total against their capacity.
- Flag over-allocation with an icon and words, not only colour.
- Show hours per day, not only a weekly total.
- Include each person's role for context.

### When to use

- Assigning tasks or shifts, weekly planning meetings.

### How to use

- `<div class="orca-capacity">` with `.orca-capacity__scale` (days and 'Total') then resource rows plus `.orca-capacity__total` (`is-over` when above capacity, with an icon and words).

#### Example: This week

```django
<div class="orca-table-wrap">
  <div class="orca-capacity">
    <div class="orca-capacity__scale" style="--orca-cols: 5">
      <span></span>
      <span>Mon</span>
      <span>Tue</span>
      <span>Wed</span>
      <span>Thu</span>
      <span>Fri</span>
      <span>Total</span>
    </div>
    {% for p in sample.people %}
      <div class="orca-resource-row" style="--orca-cols: 5">
        <div class="orca-resource-row__who">
          <span class="orca-avatar orca-avatar--s" aria-hidden="true">{{ p.initials }}</span>
          <span>
            <span>{{ p.name }}</span>
            <br>
            <span class="orca-resource-row__load">{{ p.role }}</span>
          </span>
        </div>
        <div class="orca-resource-row__slots">
          {% for h in p.days %}
            <span class="{% if h %}orca-avail-fill--busy{% else %}orca-avail-fill--free{% endif %}" aria-label="{{ h }} h">{{ h }}</span>
          {% endfor %}
        </div>
        <span class="orca-capacity__total{% if p.hours > p.capacity %} is-over{% endif %}">
          {% if p.hours > p.capacity %}
            {% icon "error" size="xs" %}
          {% endif %}
          {{ p.hours }}
          /
          {{ p.capacity }}
          h
        </span>
      </div>
    {% endfor %}
  </div>
</div>
```

**Classes:** `.orca-capacity`, `.orca-capacity__scale`, `.orca-capacity__total`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI L01: Group related information

**ORCA guide items covered:** Capacity planner (workload by resource)

---

## Deadline list

`id: deadline-list` · level: pattern · source: ORCA

Deadlines grouped as Overdue, This week and Later, each with its date and time left.

Built from: `deadline-item`

### General description

A list of upcoming due dates, usually grouped as overdue, this week and later. It helps people see what needs attention first.

#### Use cases

- Dashboards and record sidebars.
- Compliance and renewal tracking.
- Reminding people what is due soon.

#### When not to use it

- Work with many stages is better on a board.
- Events at a set time belong in a calendar.

#### Best practices

- Put overdue items first and mark them clearly.
- Show relative times like 'in 3 days' next to the date.
- Group by urgency, not by date alone.
- Keep each row to a name, a date and a state.

### When to use

- Dashboards, record sidebars, compliance and renewal tracking.

### How to use

- `<div class="orca-deadline-list">` with `h3.orca-deadline-list__group` (overdue modifier) and deadline items.

#### Example: Deadlines

```django
<div class="orca-deadline-list" style="max-width: 32rem">
  <h3 class="orca-deadline-list__group orca-deadline-list__group--overdue">Overdue</h3>
  <div class="orca-plan-row">
    {% icon "flag" %}
    <span class="orca-plan-row__body">
      <span>Quarterly report</span>
      <span class="orca-plan-row__meta">Due 4 November 2026</span>
    </span>
    <span class="orca-overdue">
      {% icon "error" %}
      Overdue by 2 days
    </span>
  </div>
  <h3 class="orca-deadline-list__group">This week</h3>
  <div class="orca-plan-row">
    {% icon "flag" %}
    <span class="orca-plan-row__body">
      <span>Licence renewal</span>
      <span class="orca-plan-row__meta">Due 9 November 2026</span>
    </span>
    <span class="orca-chip orca-chip--soon">
      {% icon "calendar" %}
      In 3 days
    </span>
  </div>
  <h3 class="orca-deadline-list__group">Later</h3>
  <div class="orca-plan-row">
    {% icon "flag" %}
    <span class="orca-plan-row__body">
      <span>All sites live</span>
      <span class="orca-plan-row__meta">Due 1 December 2026</span>
    </span>
    <span class="orca-chip">
      {% icon "calendar" %}
      In 25 days
    </span>
  </div>
</div>
```

**Classes:** `.orca-deadline-list`, `.orca-deadline-list__group`, `.orca-deadline-list__group--overdue`

**Principles applied:** Practical UI L03: Establish an order of importance; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Deadline list

---

## Planning summary

`id: planning-summary` · level: pattern · source: ORCA

Paired bars comparing planned with done for each team, person or category, with the numbers.

Built from: `legend-item`

### General description

A summary that compares what was planned with what was done, usually as paired bars with numbers, for each team, person or category.

#### Use cases

- Sprint reviews and monthly reports.
- Checking whether plans are realistic.
- Comparing workload across people or teams.

#### When not to use it

- Trends over many periods are better shown in a line chart.
- A single progress figure only needs a progress bar.

#### Best practices

- Show the numbers as well as the bars.
- Use outline and fill, not only colour, to tell planned from done.
- Scale all bars against the same maximum.
- Label each bar with a name.

### When to use

- Sprint reviews, monthly reports, period overviews.

### How to use

- `<ul class="orca-plan-summary">` of `.orca-plan-summary__row`: label, `.orca-plan-summary__bar` with `.orca-plan-summary__planned` (`--orca-planned`) and `.orca-plan-summary__done` (`--orca-done`) widths relative to the largest plan, and `.orca-plan-summary__value` ('12 of 15').

#### Example: Planned vs done

```django
<ul class="orca-plan-summary" aria-label="Tasks planned and done by person">
  <li class="orca-plan-summary__row">
    <span>Ada Lovelace</span>
    <span class="orca-plan-summary__bar" aria-hidden="true">
      <span class="orca-plan-summary__planned" style="--orca-planned: 100%"></span>
      <span class="orca-plan-summary__done" style="--orca-done: 80%"></span>
    </span>
    <span class="orca-plan-summary__value">12 of 15</span>
  </li>
  <li class="orca-plan-summary__row">
    <span>Grace Hopper</span>
    <span class="orca-plan-summary__bar" aria-hidden="true">
      <span class="orca-plan-summary__planned" style="--orca-planned: 67%"></span>
      <span class="orca-plan-summary__done" style="--orca-done: 67%"></span>
    </span>
    <span class="orca-plan-summary__value">10 of 10</span>
  </li>
  <li class="orca-plan-summary__row">
    <span>Alan Turing</span>
    <span class="orca-plan-summary__bar" aria-hidden="true">
      <span class="orca-plan-summary__planned" style="--orca-planned: 53%"></span>
      <span class="orca-plan-summary__done" style="--orca-done: 20%"></span>
    </span>
    <span class="orca-plan-summary__value">3 of 8</span>
  </li>
</ul>
```

**Classes:** `.orca-plan-summary`, `.orca-plan-summary__row`, `.orca-plan-summary__bar`, `.orca-plan-summary__planned`, `.orca-plan-summary__done`, `.orca-plan-summary__value`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Planning summary (planned vs done)

---

## Plan filter bar

`id: plan-filter-bar` · level: pattern · source: ORCA

A bar above a plan showing the period, applied assignee and status filters as removable chips, and the result count.

Built from: `filter-bar`, `period-selector`

### General description

A bar above a plan that shows the period being viewed and the filters applied, with a count of results. It keeps the plan's current view clear.

#### Use cases

- Above task lists, boards and Gantt charts.
- Narrowing a plan by period, person or status.
- Showing which filters are currently active.

#### When not to use it

- Pages with no filters do not need it.
- Many filters at once belong in a filter panel.

#### Best practices

- Show applied filters as chips that can be removed one by one.
- Offer one 'Clear all' action.
- Show the number of results.
- Keep the period control always visible.

### When to use

- Above task lists, boards, Gantt charts and deadline lists.

### How to use

- A row with the period selector, the applied filters as removable chips with 'Clear all', and a result count announced politely.
- Assignee and status are chosen in the `filter-drawer`, opened by the Filters button in the page actions.

#### Example: Plan filters

```django
<div class="orca-filter-bar">
  <nav class="orca-segmented orca-segmented--dense" aria-label="Period">
    <a class="orca-segmented__item" href="#" aria-current="page">This week</a>
    <a class="orca-segmented__item" href="#">Next week</a>
    <a class="orca-segmented__item" href="#">This month</a>
  </nav>
  <div class="orca-filter-bar__applied">
    <span class="orca-small orca-muted">Filtered by</span>
    <span class="orca-tag">
      <span class="orca-tag__text">Assignee: Alan Turing</span>
      <button class="orca-tag__remove" type="button" aria-label="Remove filter Assignee: Alan Turing">
        {% icon "close" %}
      </button>
    </span>
    <button class="orca-button orca-button--link" type="button">Clear all</button>
    <span class="orca-small orca-muted" aria-live="polite">2 tasks</span>
  </div>
</div>
```

**Classes:** `.orca-filter-bar`, `.orca-filter-bar__applied`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI S08: Simplify decisions: remove, group, stage, recommend

**ORCA guide items covered:** Plan filter bar (period, assignee, status)

---

## Date-range filter bar

`id: date-range-filter-bar` · level: pattern · source: ORCA

A period filter for reports and plans: quick presets or a custom from–to range, with the chosen dates shown.

Built from: `date-range-picker`, `filter-bar`

### General description

A control for choosing a time period, with quick presets such as 'last 30 days' and a custom start and end date.

#### Use cases

- Filtering reports and charts by period.
- Choosing the dates of a plan view.
- Setting the range of an export.

#### When not to use it

- Picking a single date is simpler with a date picker.
- Filtering by something other than time needs a regular filter.

#### Best practices

- Put common presets first.
- Always show the exact dates chosen.
- Use a clear format for dates.
- Reveal the custom range only when asked.

### When to use

- Above charts, reports, plan views and exports.

### How to use

- A filter bar with preset buttons (`aria-pressed`), a date range picker revealed by 'Custom', and the resolved dates; submit as `?from=…&to=…`.
- The period is a view control and stays visible; other page filters go in the filter drawer.

#### Example: Period

```django
<form class="orca-filter-bar" method="get" onsubmit="return false">
  <div class="orca-presets" role="group" aria-label="Quick periods">
    <button class="orca-tag" type="button" aria-pressed="false">Today</button>
    <button class="orca-tag" type="button" aria-pressed="true">This week</button>
    <button class="orca-tag" type="button" aria-pressed="false">Last 30 days</button>
    <button class="orca-tag" type="button" aria-pressed="false">Custom</button>
  </div>
  <fieldset class="orca-inline-fields" data-orca-range>
    <legend class="orca-sr-only">Custom period</legend>
    <div class="orca-field">
      <label class="orca-label" for="drf-a">From</label>
      <input class="orca-input orca-input--dense" type="date" id="drf-a" value="2026-11-02">
    </div>
    <span class="orca-inline-fields__sep" aria-hidden="true">–</span>
    <div class="orca-field">
      <label class="orca-label" for="drf-b">To</label>
      <input class="orca-input orca-input--dense" type="date" id="drf-b" value="2026-11-08">
    </div>
    <p class="orca-inline-fields__note" data-orca-range-output aria-live="polite">7 days</p>
  </fieldset>
</form>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Form and view helper

```python
# videos/forms.py
from django import forms


class PeriodForm(forms.Form):
    start = forms.DateField(label="From")
    end = forms.DateField(label="To")

    def clean(self):
        data = super().clean()
        if data.get("start") and data.get("end") and data["end"] < data["start"]:
            self.add_error("end", "Choose an end date on or after the start date.")
        return data


# videos/views.py
import datetime as dt

from django.utils import timezone


def period(request):
    """The chosen period from ?start=…&end=…, the last 7 days by default."""
    form = PeriodForm(request.GET or None)
    if form.is_valid():
        return form.cleaned_data["start"], form.cleaned_data["end"]
    today = timezone.localdate()
    return today - dt.timedelta(days=6), today
```

**Classes:** `.orca-filter-bar`, `.orca-presets`

**Principles applied:** Practical UI S08: Simplify decisions: remove, group, stage, recommend; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Date-range filter bar

---
