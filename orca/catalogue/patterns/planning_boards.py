from ..registry import add, category
from . import Pattern

C = category(
    "planning-boards", "Planning boards and timelines",
    "Show and manage work over time: task lists, boards, Gantt charts, roadmaps, milestones, capacity, deadlines and plan summaries.",
    level="pattern",
)

TASKS = """{% for t in sample.tasks %}<div class="orca-task{% if t.status == "done" %} orca-task--done{% endif %}"><label class="orca-check"><input type="checkbox" aria-label="{{ t.title }}"{% if t.status == "done" %} checked{% endif %}><span class="orca-check__box"></span></label><span class="orca-task__title">{{ t.title }}</span>
  <div class="orca-task__meta"><span class="orca-avatar orca-avatar--xs" aria-hidden="true">{{ t.assignee }}</span>{% if t.status != "done" %}<span class="orca-chip{% if t.due_state %} orca-chip--{{ t.due_state }}{% endif %}">{% icon "calendar" %}{{ t.due }}</span>{% endif %}<span class="orca-chip orca-chip--{{ t.status }}">{{ t.status|capfirst }}</span></div></div>
{% endfor %}"""


def _card(cid, title, tag, due, who, state=""):
    return (f'<li class="orca-board-card" id="{cid}" draggable="true"><div class="orca-board-card__head"><button class="orca-drag-handle" type="button" aria-label="Move {title}">{{% icon "drag" %}}</button>'
            f'<h4 class="orca-board-card__title"><a href="#">{title}</a></h4></div><div class="orca-row"><span class="orca-tag">{tag}</span></div>'
            f'<div class="orca-board-card__foot"><span class="orca-chip{" orca-chip--" + state if state else ""}">{{% icon "calendar" %}}{due}</span><span class="orca-avatar orca-avatar--xs" title="{who}">{who}</span></div></li>')


def _col(key, name, cards, limit="", over=False):
    lim = f'<span class="orca-board__limit">limit {limit}</span>' if limit else ""
    return (f'<section class="orca-board__col{" is-over" if over else ""}" aria-label="{name}"><h3 class="orca-board__head">{name} <span class="orca-badge orca-badge--grey" data-orca-count>{len(cards)}</span>{lim}</h3>'
            f'<ul class="orca-board__cards" data-orca-column="{key}">{"".join(cards)}</ul></section>')


BOARD = ('<div class="orca-board" data-orca-board aria-label="Installation board">'
         + _col("planned", "Planned", [_card("kb-1", "Draw zones for Gate 1", "Zones", "Fri 13 Nov", "GH")])
         + _col("progress", "In progress", [_card("kb-2", "Trim Entrance A video", "Video", "Tomorrow", "AL", "soon"),
                                            _card("kb-3", "Connect Gate 1 media server", "Network", "Mon 9 Nov", "AT")], limit="2")
         + _col("done", "Done", [_card("kb-4", "Mount Gate 1 bracket", "Install", "2 Nov", "AT")])
         + "</div>")

add(Pattern(
    "task-list", "Task list", C,
    "Tasks grouped by status or due date, each with checkbox, assignee, due date and status, plus a row to add more.",
    why="A checklist is the most familiar planning tool (Jakob's law); ticking a task off gives immediate progress (Peak–end rule). Groups keep the list scannable (Practical UI L09).",
    when=["Personal and team to-dos, and tasks tied to one record (a video's maintenance)."],
    how=["`<div class=\"orca-task-list\">` with `h3.orca-task-list__group` headings and task items, ending with `.orca-task-list__add` (input + Add).",
         "Ticking saves at once (htmx) and moves the task to Done with an undo toast. Sort overdue tasks first."],
    classes=[".orca-task-list", ".orca-task-list__group", ".orca-task-list__add"],
    laws=["jakob", "peak-end", "L09"],
    uses=["task-item", "status-chip"],
    examples=[("Tasks", '<div class="orca-task-list" style="max-width: 40rem"><h3 class="orca-task-list__group">This week</h3>' + TASKS
              + '<form class="orca-task-list__add" onsubmit="return false"><input class="orca-input orca-input--dense" aria-label="New task" placeholder="Add a task"><button class="orca-button orca-button--dense" type="submit">Add</button></form></div>')],
    guide=["Task list"],
))

add(Pattern(
    "kanban-board", "Kanban board", C,
    "Status columns of cards that move by drag and drop or a 'Move to' menu, with work-in-progress limits.",
    why="Columns make the flow of work visible and bottlenecks obvious (Practical UI L01, grouping); WIP limits that turn red when exceeded stop overloading (Von Restorff). The menu alternative makes moving possible by keyboard and touch.",
    when=["Team workflows with a few stages, such as installation jobs or support tickets."],
    avoid=["More than ~6 columns or hundreds of cards: use a table with a status filter."],
    how=["`<div class=\"orca-board\" data-orca-board>` of `section.orca-board__col` each with a head (name, `[data-orca-count]` badge, `.orca-board__limit`) and `<ul class=\"orca-board__cards\" data-orca-column=\"key\">` of board cards with `draggable=\"true\"` and an `id`.",
         "Save on the `orca:moved` event (`detail.id`, `from`, `to`). Give each card a 'Move to' dropdown for keyboard and touch.",
         "Mark a column `is-over` when its count exceeds the limit."],
    a11y=["Drag and drop is never the only way: each card has a 'Move to' menu; moves are announced."],
    classes=[".orca-board", ".orca-board__col", ".orca-board__head", ".orca-board__limit", ".orca-board__cards"],
    laws=["L01", "restorff", "jakob"],
    uses=["board-card", "column-header", "dropdown-menu"],
    examples=[("Board", BOARD)],
    guide=["Kanban board"],
))

add(Pattern(
    "gantt-chart", "Gantt chart", C,
    "Task bars on a time scale, showing progress, dependencies, milestones and a today line.",
    why="Bars on a shared time scale show sequence, overlap and slippage at once (Practical UI L01, grouping); a today line makes 'are we late?' instant (Von Restorff).",
    when=["Projects with dated, dependent tasks, such as rollouts and installations."],
    avoid=["Undated work: use a board or task list."],
    how=["`<div class=\"orca-gantt-chart\" style=\"--orca-cols: 7\">` with `.orca-gantt-chart__scale` (label column then period labels, `is-today`), then the Gantt rows, and `.orca-gantt-chart__today` with `--orca-at` (0–1) inside the gantt.",
         "Compute the `--orca-start` and `--orca-span` percentages in the view. Late bars get the late modifier and the word 'Late'."],
    classes=[".orca-gantt-chart", ".orca-gantt-chart__scale", ".orca-gantt-chart__today"],
    laws=["L01", "restorff"],
    uses=["gantt-bar", "milestone-item"],
    examples=[("Week 45", """<div class="orca-table-wrap"><div class="orca-gantt-chart" style="--orca-cols: 7"><div class="orca-gantt-chart__scale"><span></span><span>Mon 2</span><span>Tue 3</span><span>Wed 4</span><span>Thu 5</span><span class="is-today">Fri 6</span><span>Sat 7</span><span>Sun 8</span></div>
  <div class="orca-gantt" style="--orca-cols: 7" role="list" aria-label="Installation plan, week 45"><span class="orca-gantt-chart__today" style="--orca-at: 0.64" aria-hidden="true"></span>
    <div class="orca-gantt-row" role="listitem"><span class="orca-gantt-row__label">Upload videos</span><span class="orca-gantt-row__lane"><a class="orca-gantt-bar orca-gantt-bar--done" href="#" style="--orca-start: 0%; --orca-span: 28%; --orca-progress: 100%">Done</a></span></div>
    <div class="orca-gantt-row" role="listitem"><span class="orca-gantt-row__label">Connect media servers</span><span class="orca-gantt-row__lane"><a class="orca-gantt-bar" href="#" style="--orca-start: 28%; --orca-span: 43%; --orca-progress: 60%">60%</a></span></div>
    <div class="orca-gantt-row" role="listitem"><span class="orca-gantt-row__label">Draw zones</span><span class="orca-gantt-row__lane"><a class="orca-gantt-bar orca-gantt-bar--late" href="#" style="--orca-start: 43%; --orca-span: 28%">Late</a><span class="orca-milestone" style="--orca-start: 92%" role="img" aria-label="Go live milestone, Sunday 8"></span></span></div></div></div></div>""")],
    guide=["Gantt chart"],
))

add(Pattern(
    "roadmap", "Roadmap", C,
    "Lanes of themes or teams across quarters or months, with each item in its planned period.",
    why="A roadmap communicates intent, not dates: coarse periods (Now, Next, Later or quarters) set honest expectations (Peak–end rule), and lanes group work by theme (Practical UI L01, grouping).",
    when=["Product and rollout plans shared with stakeholders."],
    avoid=["Day-level scheduling: use a Gantt chart."],
    how=["`<div class=\"orca-roadmap\" style=\"--orca-cols: 4\">`: a corner then `.orca-roadmap__head` per period (current one `is-now`), then per lane `.orca-roadmap__lane` and one `.orca-roadmap__cell` per period holding `.orca-roadmap__item` links (`--orca-event` for the theme colour)."],
    classes=[".orca-roadmap", ".orca-roadmap__head", ".orca-roadmap__lane", ".orca-roadmap__cell", ".orca-roadmap__item"],
    laws=["L01", "peak-end"],
    uses=["gantt-bar"],
    examples=[("2026–27", """<div class="orca-table-wrap"><div class="orca-roadmap" style="--orca-cols: 4"><span></span><span class="orca-roadmap__head">Q3 2026</span><span class="orca-roadmap__head is-now">Q4 2026</span><span class="orca-roadmap__head">Q1 2027</span><span class="orca-roadmap__head">Q2 2027</span>
  <span class="orca-roadmap__lane">Counting</span><div class="orca-roadmap__cell"><a class="orca-roadmap__item" href="#" style="--orca-event: var(--orca-chart-1)">Zone counts</a></div><div class="orca-roadmap__cell"><a class="orca-roadmap__item" href="#" style="--orca-event: var(--orca-chart-1)">Dwell time</a></div><div class="orca-roadmap__cell"><a class="orca-roadmap__item" href="#" style="--orca-event: var(--orca-chart-1)">Queue length</a></div><div class="orca-roadmap__cell"></div>
  <span class="orca-roadmap__lane">Sites</span><div class="orca-roadmap__cell"></div><div class="orca-roadmap__cell"><a class="orca-roadmap__item" href="#" style="--orca-event: var(--orca-chart-3)">Warehouse live</a><a class="orca-roadmap__item" href="#" style="--orca-event: var(--orca-chart-3)">Car park live</a></div><div class="orca-roadmap__cell"><a class="orca-roadmap__item" href="#" style="--orca-event: var(--orca-chart-3)">Second city</a></div><div class="orca-roadmap__cell"></div></div></div>""")],
    guide=["Roadmap"],
))

add(Pattern(
    "milestone-timeline", "Milestone timeline", C,
    "Key dates on one line: reached, next and upcoming milestones with their dates.",
    why="A handful of milestones on a line tells the story of a project at a glance (Miller's law), and the next one shows how far is left.",
    when=["Project overviews, status reports, onboarding journeys."],
    how=["`<ol class=\"orca-milestones\" style=\"--orca-cols: 4\">` of items with a milestone marker (done or upcoming), `.orca-milestones__name` and the date.",
         "Keep to 3–7 milestones; the next one carries 'in N days'."],
    classes=[".orca-milestones", ".orca-milestones__name"],
    laws=["miller", "peak-end"],
    uses=["milestone-item"],
    examples=[("Rollout", """<div class="orca-table-wrap"><ol class="orca-milestones" style="--orca-cols: 4">
  <li><span class="orca-milestone orca-milestone--done" aria-hidden="true"></span><span class="orca-milestones__name">Pilot live</span><span class="orca-muted">3 March 2026 · reached</span></li>
  <li><span class="orca-milestone orca-milestone--done" aria-hidden="true"></span><span class="orca-milestones__name">North building</span><span class="orca-muted">2 November · reached</span></li>
  <li><span class="orca-milestone orca-milestone--upcoming" aria-hidden="true"></span><span class="orca-milestones__name">All sites live</span><span>1 December · in 25 days</span></li>
  <li><span class="orca-milestone orca-milestone--upcoming" aria-hidden="true"></span><span class="orca-milestones__name">Second city</span><span class="orca-muted">March 2027</span></li></ol></div>""")],
    guide=["Milestone timeline"],
))

add(Pattern(
    "period-overview", "Sprint or period overview", C,
    "A sprint or period at a glance: dates, days left, goal, progress, plan summary and open work.",
    why="One page answering 'how is this sprint going' (progress and days left side by side) keeps teams honest about scope; the goal in words keeps focus (Von Restorff).",
    when=["Sprint pages, monthly plans, campaign periods."],
    how=["`<div class=\"orca-period-overview\">` with a page head (period name, dates, period selector), summary tiles (done, open, late, days left), the goal callout, the planning summary and a task list or board."],
    classes=[".orca-period-overview"],
    laws=["peak-end", "restorff"],
    uses=["summary-tiles", "planning-summary", "period-selector", "callout"],
    examples=[("Sprint 45", """<div class="orca-period-overview" style="max-width: 44rem"><div class="orca-row" style="justify-content: space-between"><div><h2 class="orca-h3" style="margin: 0">Sprint 45</h2><p class="orca-small orca-muted">2–13 November · 5 working days left</p></div><nav class="orca-segmented orca-segmented--dense" aria-label="Sprint"><a class="orca-segmented__item" href="#">44</a><a class="orca-segmented__item" href="#" aria-current="page">45</a><a class="orca-segmented__item" href="#">46</a></nav></div>
  <div class="orca-callout">{% icon "flag" %}<p class="orca-callout__title">Goal: Warehouse videos published by Friday 13</p></div>
  <dl class="orca-summary-tiles"><div class="orca-summary-tile"><dt>Done</dt><dd>12</dd></div><div class="orca-summary-tile"><dt>Open</dt><dd>6</dd></div><div class="orca-summary-tile"><dt>Late</dt><dd>2</dd></div></dl>
  <progress class="orca-progress" value="12" max="20" aria-label="12 of 20 tasks done"></progress></div>""")],
    guide=["Sprint or period overview"],
))

add(Pattern(
    "capacity-planner", "Capacity planner", C,
    "One row per person showing booked hours per day against capacity, with totals and over-allocation flagged.",
    why="Assigning work without seeing load leads to burnout and slippage; per-day cells and a total against capacity make over-allocation visible before it happens (Von Restorff, Practical UI L01, grouping).",
    when=["Assigning tasks or shifts, weekly planning meetings."],
    how=["`<div class=\"orca-capacity\">` with `.orca-capacity__scale` (days and 'Total') then resource rows plus `.orca-capacity__total` (`is-over` when above capacity, with an icon and words)."],
    classes=[".orca-capacity", ".orca-capacity__scale", ".orca-capacity__total"],
    laws=["restorff", "L01"],
    uses=["resource-row", "availability-legend"],
    examples=[("This week", """<div class="orca-table-wrap"><div class="orca-capacity"><div class="orca-capacity__scale" style="--orca-cols: 5"><span></span><span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Total</span></div>
{% for p in sample.people %}<div class="orca-resource-row" style="--orca-cols: 5"><div class="orca-resource-row__who"><span class="orca-avatar orca-avatar--s" aria-hidden="true">{{ p.initials }}</span><span><span>{{ p.name }}</span><br><span class="orca-resource-row__load">{{ p.role }}</span></span></div>
  <div class="orca-resource-row__slots">{% for h in p.days %}<span class="{% if h %}orca-avail-fill--busy{% else %}orca-avail-fill--free{% endif %}" aria-label="{{ h }} h">{{ h }}</span>{% endfor %}</div>
  <span class="orca-capacity__total{% if p.hours > p.capacity %} is-over{% endif %}">{% if p.hours > p.capacity %}{% icon "error" size="xs" %}{% endif %}{{ p.hours }} / {{ p.capacity }} h</span></div>
{% endfor %}</div></div>""")],
    guide=["Capacity planner (workload by resource)"],
))

add(Pattern(
    "deadline-list", "Deadline list", C,
    "Deadlines grouped as Overdue, This week and Later, each with its date and time left.",
    why="Overdue items first and in red get attention (Practical UI L03, Von Restorff); relative times ('in 3 days') are understood faster than dates, with the date kept for precision.",
    when=["Dashboards, record sidebars, compliance and renewal tracking."],
    how=["`<div class=\"orca-deadline-list\">` with `h3.orca-deadline-list__group` (overdue modifier) and deadline items."],
    classes=[".orca-deadline-list", ".orca-deadline-list__group", ".orca-deadline-list__group--overdue"],
    laws=["L03", "restorff"],
    uses=["deadline-item"],
    examples=[("Deadlines", """<div class="orca-deadline-list" style="max-width: 32rem"><h3 class="orca-deadline-list__group orca-deadline-list__group--overdue">Overdue</h3>
  <div class="orca-plan-row">{% icon "flag" %}<span class="orca-plan-row__body"><span>Quarterly report</span><span class="orca-plan-row__meta">Due 4 November 2026</span></span><span class="orca-overdue">{% icon "error" %}Overdue by 2 days</span></div>
  <h3 class="orca-deadline-list__group">This week</h3>
  <div class="orca-plan-row">{% icon "flag" %}<span class="orca-plan-row__body"><span>Licence renewal</span><span class="orca-plan-row__meta">Due 9 November 2026</span></span><span class="orca-chip orca-chip--soon">{% icon "calendar" %}In 3 days</span></div>
  <h3 class="orca-deadline-list__group">Later</h3>
  <div class="orca-plan-row">{% icon "flag" %}<span class="orca-plan-row__body"><span>All sites live</span><span class="orca-plan-row__meta">Due 1 December 2026</span></span><span class="orca-chip">{% icon "calendar" %}In 25 days</span></div></div>""")],
    guide=["Deadline list"],
))

add(Pattern(
    "planning-summary", "Planning summary", C,
    "Paired bars comparing planned with done for each team, person or category, with the numbers.",
    why="Comparing what was planned with what was done shows whether plans are realistic (Peak–end rule: honest retrospectives); an outline for planned and a fill for done reads without colour (Practical UI C03).",
    when=["Sprint reviews, monthly reports, period overviews."],
    how=["`<ul class=\"orca-plan-summary\">` of `.orca-plan-summary__row`: label, `.orca-plan-summary__bar` with `.orca-plan-summary__planned` (`--orca-planned`) and `.orca-plan-summary__done` (`--orca-done`) widths relative to the largest plan, and `.orca-plan-summary__value` ('12 of 15')."],
    classes=[".orca-plan-summary", ".orca-plan-summary__row", ".orca-plan-summary__bar", ".orca-plan-summary__planned", ".orca-plan-summary__done", ".orca-plan-summary__value"],
    laws=["peak-end", "C03"],
    uses=["legend-item"],
    examples=[("Planned vs done", """<ul class="orca-plan-summary" aria-label="Tasks planned and done by person">
  <li class="orca-plan-summary__row"><span>Ada Lovelace</span><span class="orca-plan-summary__bar" aria-hidden="true"><span class="orca-plan-summary__planned" style="--orca-planned: 100%"></span><span class="orca-plan-summary__done" style="--orca-done: 80%"></span></span><span class="orca-plan-summary__value">12 of 15</span></li>
  <li class="orca-plan-summary__row"><span>Grace Hopper</span><span class="orca-plan-summary__bar" aria-hidden="true"><span class="orca-plan-summary__planned" style="--orca-planned: 67%"></span><span class="orca-plan-summary__done" style="--orca-done: 67%"></span></span><span class="orca-plan-summary__value">10 of 10</span></li>
  <li class="orca-plan-summary__row"><span>Alan Turing</span><span class="orca-plan-summary__bar" aria-hidden="true"><span class="orca-plan-summary__planned" style="--orca-planned: 53%"></span><span class="orca-plan-summary__done" style="--orca-done: 20%"></span></span><span class="orca-plan-summary__value">3 of 8</span></li></ul>""")],
    guide=["Planning summary (planned vs done)"],
))

add(Pattern(
    "plan-filter-bar", "Plan filter bar", C,
    "A bar above a plan showing the period, applied assignee and status filters as removable chips, and the result count.",
    why="Plans get long; the three questions people ask (when, who, what state) must stay answerable at a glance (Hick's law, Practical UI S08). "
        "The period is a view control, so it stays visible; assignee and status are page filters, so they live in the filter drawer and show here as chips.",
    when=["Above task lists, boards, Gantt charts and deadline lists."],
    how=["A row with the period selector, the applied filters as removable chips with 'Clear all', and a result count announced politely.",
         "Assignee and status are chosen in the `filter-drawer`, opened by the Filters button in the page actions."],
    classes=[".orca-filter-bar", ".orca-filter-bar__applied"],
    laws=["hick", "S08"],
    uses=["filter-bar", "period-selector"],
    examples=[("Plan filters", """<div class="orca-filter-bar"><nav class="orca-segmented orca-segmented--dense" aria-label="Period"><a class="orca-segmented__item" href="#" aria-current="page">This week</a><a class="orca-segmented__item" href="#">Next week</a><a class="orca-segmented__item" href="#">This month</a></nav>
  <div class="orca-filter-bar__applied"><span class="orca-small orca-muted">Filtered by</span><span class="orca-tag"><span class="orca-tag__text">Assignee: Alan Turing</span><button class="orca-tag__remove" type="button" aria-label="Remove filter Assignee: Alan Turing">{% icon "close" %}</button></span><button class="orca-button orca-button--link" type="button">Clear all</button><span class="orca-small orca-muted" aria-live="polite">2 tasks</span></div></div>""")],
    guide=["Plan filter bar (period, assignee, status)"],
))

add(Pattern(
    "date-range-filter-bar", "Date-range filter bar", C,
    "A period filter for reports and plans: quick presets or a custom from–to range, with the chosen dates shown.",
    why="Most people want 'this week' or 'last 30 days' (Practical UI S08, Hick's law), so presets come first; a custom range covers the rest, and the chosen dates are always printed so the period is never ambiguous.",
    when=["Above charts, reports, plan views and exports."],
    how=["A filter bar with preset buttons (`aria-pressed`), a date range picker revealed by 'Custom', and the resolved dates; submit as `?from=…&to=…`.",
         "The period is a view control and stays visible; other page filters go in the filter drawer."],
    classes=[".orca-filter-bar", ".orca-presets"],
    laws=["S08", "hick"],
    uses=["date-range-picker", "filter-bar"],
    examples=[("Period", """<form class="orca-filter-bar" method="get" onsubmit="return false"><div class="orca-presets" role="group" aria-label="Quick periods"><button class="orca-tag" type="button" aria-pressed="false">Today</button><button class="orca-tag" type="button" aria-pressed="true">This week</button><button class="orca-tag" type="button" aria-pressed="false">Last 30 days</button><button class="orca-tag" type="button" aria-pressed="false">Custom</button></div>
  <fieldset class="orca-inline-fields" data-orca-range><legend class="orca-sr-only">Custom period</legend><div class="orca-field"><label class="orca-label" for="drf-a">From</label><input class="orca-input orca-input--dense" type="date" id="drf-a" value="2026-11-02"></div><span class="orca-inline-fields__sep" aria-hidden="true">–</span><div class="orca-field"><label class="orca-label" for="drf-b">To</label><input class="orca-input orca-input--dense" type="date" id="drf-b" value="2026-11-08"></div><p class="orca-inline-fields__note" data-orca-range-output aria-live="polite">7 days</p></fieldset></form>""")],
    guide=["Date-range filter bar"],
))
