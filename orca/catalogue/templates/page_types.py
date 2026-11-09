"""Level 4: page-type skeletons, the app shell specialised for one kind of screen."""

from ..registry import add, category
from . import Template
from .layouts import APP_BLOCKS, APP_CONTEXT, extend

C = category(
    "page-types", "Page-type skeletons",
    "The app shell set up for one kind of screen: dashboard, calendar, scheduler, board, timeline, booking, event "
    "editor and simple data page. Pass data in the context; override a block only to change a region.",
    level="template",
)


def page(eid, name, template, summary, why, when, how, laws, uses, guide, blocks, context, classes=(), avoid=()):
    add(Template(eid, name, C, summary, why=why, when=list(when), avoid=list(avoid), how=[extend(template)] + list(how),
                 laws=list(laws), uses=list(uses), guide=list(guide), template=template, preview=eid,
                 blocks=APP_BLOCKS + list(blocks), context=APP_CONTEXT + list(context), classes=list(classes), source="ORCA"))


page("dashboard", "Dashboard", "orca/layouts/dashboard.html",
     "An overview page: a period switch, a stat grid, charts in two columns and room for lists below.",
     "A dashboard answers 'how are we doing?' at a glance: a few headline numbers first (Miller's law), then the charts that explain them, "
     "all for one clearly stated period (Practical UI W11).",
     ["The home of an analytics or operations application; the overview of a site or team."],
     ["Pass `stats` (label, value, foot, delta, trend, url), `charts` (kind, data, title, subtitle) and `periods`.",
      "Keep it to 4–6 stats and 2–4 charts; link each stat to the list behind it."],
     ["miller", "W11", "L03"], ["app-shell", "kpi-grid", "bar-chart", "line-chart", "two-column-grid"], ["Dashboard"],
     ["dashboard_period", "dashboard_stats", "dashboard_main", "dashboard_extra"], ["`stats`, `charts`, `periods`."])

page("calendar-page", "Calendar page", "orca/layouts/calendar.html",
     "A full calendar: toolbar (previous, Today, next, period, view switch), a side panel with a mini calendar and calendars legend, and the month, week, day or agenda view.",
     "The same toolbar and side panel around every view means people only learn one calendar (Jakob's law); the side panel jumps to any date in one click (Fitts's law).",
     ["Event, booking and shift calendars."],
     ["Pass `events`, `view` (\"month\", \"week\", \"day\", \"agenda\"), `month`, `day`, `today`, `now`, the navigation URLs and `views`.",
      "Navigation is plain links with the period in the query string; `calendars` lists the legend checkboxes."],
     ["jakob", "fitts", "hick"], ["calendar-toolbar", "mini-calendar-sidebar", "calendar-legend", "month-calendar", "week-view", "agenda-view"],
     ["Calendar page (toolbar + view + side panel)"], ["calendar_toolbar", "calendar_side", "calendar_view"],
     ["`events`, `view`, `month`, `day`, `today`, `now`, `holidays`, `event_days`.", "`period_title`, `prev_url`, `next_url`, `today_url`, `day_url`, `month_url`, `views`, `calendars`, `create_url`."],
     classes=[".orca-cal-main"])

page("scheduler-page", "Scheduler page", "orca/layouts/scheduler.html",
     "Resources by time for one day: a date toolbar, a row per person, room or vehicle with bookings placed by time, and the legend.",
     "Rows per resource answer 'who is free when' in one look (Practical UI L01); placing bookings by time makes gaps and double bookings visible.",
     ["Dispatching installers, booking rooms, planning vehicles."],
     ["Pass `resources`: `[{\"name\", \"bookings\": [events]}]`, `start_hour` and `end_hour`; `{% templatetag openblock %} orca_scheduler {% templatetag closeblock %}` places the cards."],
     ["L01", "L09"], ["resource-scheduler", "calendar-navigation"],
     ["Scheduler page (resources by time)"], ["scheduler_toolbar", "scheduler", "scheduler_legend"],
     ["`resources`, `start_hour`, `end_hour`, `period_title`, `prev_url`, `next_url`, `today_url`."])

page("planning-board-page", "Planning board page", "orca/layouts/board.html",
     "A kanban board page: filters on top and columns of cards that move by drag and drop.",
     "Columns show the flow of work and where it is stuck (Practical UI L01); work-in-progress limits that turn red stop overloading (Von Restorff).",
     ["Team workflows with a few stages."],
     ["Pass `board_columns`: `[{\"key\", \"name\", \"limit\", \"cards\": [{\"id\", \"title\", \"tags\", \"due\", \"due_state\", \"assignee\", \"url\"}]}]` and a GET `filter_form`.",
      "Listen for the `orca:moved` event to save a move."],
     ["L01", "restorff", "jakob"], ["kanban-board", "plan-filter-bar"],
     ["Planning board page"], ["filter_panel", "board"], ["`board_columns`, `filter_form`, `create_url`."])

page("timeline-page", "Timeline page", "orca/layouts/timeline.html",
     "A Gantt timeline: period toolbar, task bars on a day scale with progress, milestones and a today line.",
     "Bars on a shared scale show sequence, overlap and slippage at once; the today line makes 'are we late?' instant (Von Restorff).",
     ["Project plans, rollouts, installation schedules."],
     ["Pass `rows`: `[{\"label\", \"start\", \"end\", \"progress\", \"state\", \"milestone\", \"url\"}]`, `start` and `days`; `orca_gantt` computes the positions."],
     ["restorff", "L01"], ["gantt-chart", "milestone-timeline"],
     ["Timeline page"], ["timeline_toolbar", "timeline", "timeline_extra"], ["`rows`, `start`, `days`, `today`, `period_title`, navigation URLs."])

page("booking-flow", "Booking flow", "orca/layouts/booking.html",
     "A step-by-step booking page: steps on top, the current step's choices, and a summary of the booking so far beside it.",
     "Steps break a booking into small decisions (Practical UI R16, Hick's law); the running summary keeps earlier choices visible and ends the flow on a clear result (Peak–end rule).",
     ["Appointment and slot booking, any short purchase-like flow."],
     ["Pass `steps` (names) and `step` (1-based); fill `booking_step` with the current choices (service radio cards, slot picker, contact form).",
      "Put Back and Continue at the end of each step; `summary` is a list of `(label, value)`."],
     ["R16", "hick", "peak-end"], ["booking-slot-picker", "appointment-picker", "split-layout"],
     ["Booking flow"], ["booking_steps", "booking_step", "booking_summary"], ["`steps`, `step`, `summary`."])

page("event-editor-page", "Event editor page", "orca/layouts/event_editor.html",
     "Create or edit an event on its own page: the form on the left, conflicts and attendees on the right, Delete apart from Save.",
     "Context beside the form (clashes, who is invited) lets people fix problems before saving (Practical UI W15, L14); Delete sits away from Save so it is never hit by mistake (B13).",
     ["Creating and editing events, shifts, bookings in full."],
     ["Pass an event `form`; `conflicts` (sentences) appear as caution callouts in `event_aside`; `delete_url` shows Delete."],
     ["W15", "L14", "B13"], ["event-editor", "attendee-list", "split-layout"],
     ["Event editor page"], ["form_fields", "event_aside"], ["`form`, `object`, `conflicts`, `delete_url`, `cancel_url`, `submit_label`."])

page("simple-data-page", "Simple data page", "orca/layouts/simple_data.html",
     "A data page with everything in one place: title bar, summary tiles that filter, search, a filter drawer and the table.",
     "Summary tiles answer 'how many of each' and double as the most used filters (Hick's law); the rest of the filters wait in a drawer so the table keeps the space (Practical UI S04).",
     ["Operational lists where counts by status matter: videos, alerts, tickets."],
     ["Use OrcaPageMixin with a ListView; pass `tiles` (label, value, url, tone, current), a GET `filter_form` and `active_filters` (count)."],
     ["hick", "S04", "miller"], ["summary-tiles", "list-header", "filter-drawer", "data-table", "pagination"],
     ["Simple data page (title bar, search, filter drawer, summary tiles, table)"], ["list_actions", "summary", "list_header", "list", "filter_panel"],
     ["`object_list`, `page_obj`, `columns`, `tiles`, `filter_form`, `active_filters`, URLs as in the generic list."])
