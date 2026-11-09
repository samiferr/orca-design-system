# Page-type skeletons

The app shell set up for one kind of screen: dashboard, calendar, scheduler, board, timeline, booking, event editor and simple data page. Pass data in the context; override a block only to change a region.

## Dashboard

`id: dashboard` · level: template · source: ORCA

An overview page: a period switch, a stat grid, charts in two columns and room for lists below.

Built from: `app-shell`, `kpi-grid`, `bar-chart`, `line-chart`, `two-column-grid`

### Why

A dashboard answers 'how are we doing?' at a glance: a few headline numbers first (Miller's law), then the charts that explain them, all for one clearly stated period (Practical UI W11).

### When to use

- The home of an analytics or operations application; the overview of a site or team.

### How to use

- Extend it: `{% extends "orca/layouts/dashboard.html" %}`, then fill only the blocks you need.
- Pass `stats` (label, value, icon, foot, delta, trend, url), `charts` (kind, data, title, subtitle) and `periods`.
- Keep it to 4–6 stats and 2–4 charts; link each stat to the list behind it.

Extend: `{% extends "orca/layouts/dashboard.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `dashboard_period`, `dashboard_stats`, `dashboard_main`, `dashboard_extra`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `stats`, `charts`, `periods`.

#### Example: Child template

```django
{% extends "orca/layouts/dashboard.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# reports/views.py
from django.views.generic import TemplateView


class Dashboard(TemplateView):
    template_name = "orca/layouts/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        period = self.request.GET.get("period", "week")
        ctx["periods"] = [{"label": label, "url": f"?period={key}", "current": key == period}
                          for key, label in [("day", "Today"), ("week", "This week"), ("month", "This month")]]
        ctx["stats"] = [
            {"label": "Views", "value": "12,480", "icon": "show", "delta": "+8%", "trend": "up", "foot": " vs last week", "url": "/reports/views/"},
            {"label": "Videos published", "value": 36, "icon": "play", "foot": "of 40 planned"},
        ]
        # Each chart: kind, data (labels and series, as for {% orca_chart %}), title and subtitle.
        ctx["charts"] = [{"kind": "bar", "data": views_per_day(period), "title": "Views per day", "subtitle": "People"},
                         {"kind": "line", "data": views_per_hour(), "title": "Views per hour", "subtitle": "Today and last Friday"}]
        ctx["title"] = "Dashboard"
        return ctx
```

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI W11: Make numbers scannable; Practical UI L03: Establish an order of importance

**ORCA guide items covered:** Dashboard

---

## Calendar page

`id: calendar-page` · level: template · source: ORCA

A full calendar: toolbar (previous, Today, next, period, view switch), a side panel with a mini calendar and calendars legend, and the month, week, day or agenda view.

Built from: `calendar-toolbar`, `mini-calendar-sidebar`, `calendar-legend`, `month-calendar`, `week-view`, `agenda-view`

### Why

The same toolbar and side panel around every view means people only learn one calendar (Jakob's law); the side panel jumps to any date in one click (Fitts's law).

### When to use

- Event, booking and shift calendars.

### How to use

- Extend it: `{% extends "orca/layouts/calendar.html" %}`, then fill only the blocks you need.
- Pass `events`, `view` ("month", "week", "day", "agenda"), `month`, `day`, `today`, `now`, the navigation URLs and `views`.
- Navigation is plain links with the period in the query string; `calendars` lists the legend checkboxes.

Extend: `{% extends "orca/layouts/calendar.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `calendar_toolbar`, `calendar_side`, `calendar_view`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `events`, `view`, `month`, `day`, `today`, `now`, `holidays`, `event_days`.
- `period_title`, `prev_url`, `next_url`, `today_url`, `day_url`, `month_url`, `views`, `calendars`, `create_url`.

#### Example: Child template

```django
{% extends "orca/layouts/calendar.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# events/views.py
import datetime as dt

from django.urls import reverse
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Calendar, Event


class CalendarPage(TemplateView):
    template_name = "orca/layouts/calendar.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        view = self.request.GET.get("view", "month")                  # month, week, day or agenda
        day = dt.date.fromisoformat(self.request.GET.get("day", today.isoformat()))
        month = day.replace(day=1)
        step = {"month": dt.timedelta(days=31), "week": dt.timedelta(days=7)}.get(view, dt.timedelta(days=1))
        url = lambda d, v=view: f"?view={v}&day={d.isoformat()}"
        ctx.update(
            title="Calendar", view=view, day=day, month=month, today=today, now=timezone.localtime(),
            # Events: dicts (or objects) with title, start, end, all_day, color, url, location, status.
            events=[{"title": e.title, "start": e.starts_at, "end": e.ends_at, "all_day": e.all_day,
                     "color": e.calendar.color, "url": e.get_absolute_url(), "location": e.place}
                    for e in Event.objects.filter(starts_at__date__gte=month - dt.timedelta(days=7),
                                                  starts_at__date__lte=month + dt.timedelta(days=42))],
            holidays={"2026-11-11": "Armistice Day"},
            period_title=day.strftime("%B %Y") if view == "month" else day.strftime("%-d %B %Y"),
            prev_url=url(day - step), next_url=url(day + step), today_url=url(today),
            day_url="?view=day&day={date}", month_url="?view=month&day={month}-01",
            views=[{"label": v.title(), "url": url(day, v), "current": v == view} for v in ("month", "week", "day", "agenda")],
            calendars=[{"key": c.slug, "label": c.name, "color": c.color, "checked": True} for c in Calendar.objects.all()],
            create_url=reverse("event-create"),
        )
        return ctx
```

**Classes:** `.orca-cal-main`

**Principles applied:** Jakob's law: work the way products people already know work; Fitts's law: big, close, well-spaced targets are faster and safer; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Calendar page (toolbar + view + side panel)

---

## Scheduler page

`id: scheduler-page` · level: template · source: ORCA

Resources by time for one day: a date toolbar, a row per person, room or vehicle with bookings placed by time, and the legend.

Built from: `resource-scheduler`, `calendar-toolbar`

### Why

Rows per resource answer 'who is free when' in one look (Practical UI L01); placing bookings by time makes gaps and double bookings visible.

### When to use

- Dispatching installers, booking rooms, planning vehicles.

### How to use

- Extend it: `{% extends "orca/layouts/scheduler.html" %}`, then fill only the blocks you need.
- Pass `resources`: `[{"name", "bookings": [events]}]`, `start_hour` and `end_hour`; `{% orca_scheduler %}` places the cards.

Extend: `{% extends "orca/layouts/scheduler.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `scheduler_toolbar`, `scheduler`, `scheduler_legend`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `resources`, `start_hour`, `end_hour`, `period_title`, `prev_url`, `next_url`, `today_url`.

#### Example: Child template

```django
{% extends "orca/layouts/scheduler.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# bookings/views.py
import datetime as dt

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Booking, Room


class Scheduler(TemplateView):
    template_name = "orca/layouts/scheduler.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        day = dt.date.fromisoformat(self.request.GET.get("day", today.isoformat()))
        bookings = Booking.objects.filter(starts_at__date=day)
        # One row per resource; its bookings are events (title, start, end, status, url).
        ctx["resources"] = [{"name": room.name, "url": room.get_absolute_url(),
                             "bookings": [{"title": b.title, "start": b.starts_at, "end": b.ends_at, "status": b.status}
                                          for b in bookings if b.room_id == room.pk]}
                            for room in Room.objects.all()]
        ctx.update(title="Rooms", start_hour=8, end_hour=18, period_title=day.strftime("%A %-d %B"),
                   prev_url=f"?day={day - dt.timedelta(days=1)}", next_url=f"?day={day + dt.timedelta(days=1)}",
                   today_url=f"?day={today}")
        return ctx
```

**Principles applied:** Practical UI L01: Group related information; Practical UI L09: Set spacing by relationship

**ORCA guide items covered:** Scheduler page (resources by time)

---

## Planning board page

`id: planning-board-page` · level: template · source: ORCA

A kanban board page: filters on top and columns of cards that move by drag and drop.

Built from: `kanban-board`, `plan-filter-bar`

### Why

Columns show the flow of work and where it is stuck (Practical UI L01); work-in-progress limits that turn red stop overloading (Von Restorff).

### When to use

- Team workflows with a few stages.

### How to use

- Extend it: `{% extends "orca/layouts/board.html" %}`, then fill only the blocks you need.
- Pass `board_columns`: `[{"key", "name", "limit", "cards": [{"id", "title", "tags", "due", "due_state", "assignee", "url"}]}]` and a GET `filter_form`.
- Listen for the `orca:moved` event to save a move.

Extend: `{% extends "orca/layouts/board.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `filter_panel`, `board`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `board_columns`, `filter_form`, `create_url`.

#### Example: Child template

```django
{% extends "orca/layouts/board.html" %}
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

**Principles applied:** Practical UI L01: Group related information; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Planning board page

---

## Timeline page

`id: timeline-page` · level: template · source: ORCA

A Gantt timeline: period toolbar, task bars on a day scale with progress, milestones and a today line.

Built from: `gantt-chart`, `milestone-timeline`

### Why

Bars on a shared scale show sequence, overlap and slippage at once; the today line makes 'are we late?' instant (Von Restorff).

### When to use

- Project plans, rollouts, installation schedules.

### How to use

- Extend it: `{% extends "orca/layouts/timeline.html" %}`, then fill only the blocks you need.
- Pass `rows`: `[{"label", "start", "end", "progress", "state", "milestone", "url"}]`, `start` and `days`; `orca_gantt` computes the positions.

Extend: `{% extends "orca/layouts/timeline.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `timeline_toolbar`, `timeline`, `timeline_extra`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `rows`, `start`, `days`, `today`, `period_title`, navigation URLs.

#### Example: Child template

```django
{% extends "orca/layouts/timeline.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# projects/views.py
import datetime as dt

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Task


class Timeline(TemplateView):
    template_name = "orca/layouts/timeline.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        start = dt.date.fromisoformat(self.request.GET.get("start", (today - dt.timedelta(days=today.weekday())).isoformat()))
        # Rows: label, start, end (dates, end included), progress 0–100, state "done" or "late", url, milestone.
        ctx["rows"] = [{"label": t.title, "start": t.starts_on, "end": t.due_on, "progress": t.progress,
                        "state": "done" if t.done else ("late" if t.due_on < today else ""), "url": t.get_absolute_url()}
                       for t in Task.objects.filter(due_on__gte=start)]
        ctx.update(title="Timeline", start=start, days=14, today=today,
                   period_title=f"{start:%-d %b} – {start + dt.timedelta(days=13):%-d %b %Y}",
                   prev_url=f"?start={start - dt.timedelta(days=14)}", next_url=f"?start={start + dt.timedelta(days=14)}",
                   today_url="?")
        return ctx
```

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI L01: Group related information

**ORCA guide items covered:** Timeline page

---

## Booking flow

`id: booking-flow` · level: template · source: ORCA

A step-by-step booking page: steps on top, the current step's choices, and a summary of the booking so far beside it.

Built from: `booking-slot-picker`, `appointment-picker`, `split-layout`

### Why

Steps break a booking into small decisions (Practical UI R16, Hick's law); the running summary keeps earlier choices visible and ends the flow on a clear result (Peak–end rule).

### When to use

- Appointment and slot booking, any short purchase-like flow.

### How to use

- Extend it: `{% extends "orca/layouts/booking.html" %}`, then fill only the blocks you need.
- Pass `steps` (names) and `step` (1-based); fill `booking_step` with the current choices (service radio cards, slot picker, contact form).
- Put Back and Continue at the end of each step; `summary` is a list of `(label, value)`.

Extend: `{% extends "orca/layouts/booking.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `booking_steps`, `booking_step`, `booking_summary`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `steps`, `step`, `summary`.

#### Example: Child template

```django
{% extends "orca/layouts/booking.html" %}
{% block booking_step %}<p class="orca-small orca-muted">30 minutes · Paris time</p>
<ul class="orca-date-strip" aria-label="Day"><li><button type="button" aria-pressed="false">Mon<strong>9</strong></button></li><li><button type="button" aria-pressed="true">Tue<strong>10</strong></button></li><li><button type="button" disabled>Wed<strong>11</strong>Full</button></li><li><button type="button" aria-pressed="false">Thu<strong>12</strong></button></li></ul>
<div><h3 class="orca-booking__group">Morning</h3><ul class="orca-booking-slots"><li><button class="orca-booking-slot" type="button" aria-pressed="false">09:00</button></li><li><button class="orca-booking-slot" type="button" aria-pressed="true">09:30</button></li><li><button class="orca-booking-slot" type="button" disabled>10:00<span class="orca-booking-slot__note">Booked</span></button></li></ul></div>
<div class="orca-row"><a class="orca-button" href="#">Back</a><button class="orca-button orca-button--primary" type="button">Continue</button></div>{% endblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# bookings/views.py — one view per step, sharing what was chosen in the session
from django.shortcuts import redirect, render

STEPS = ["Service", "Date and time", "Your details", "Confirm"]


def book_time(request):
    chosen = request.session.setdefault("booking", {})
    form = SlotForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        chosen["slot"] = form.cleaned_data["slot"].isoformat()
        request.session.modified = True
        return redirect("book-details")
    summary = [("Service", chosen.get("service", "")), ("Time", chosen.get("slot", ""))]
    return render(request, "bookings/time.html", {      # extends "orca/layouts/booking.html"
        "title": "Choose a time", "steps": STEPS, "step": 2, "summary": [s for s in summary if s[1]], "form": form,
    })
```

**Principles applied:** Practical UI R16: Break long forms into sensible steps; Hick's law: fewer, clearer choices mean faster decisions; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Booking flow

---

## Event editor page

`id: event-editor-page` · level: template · source: ORCA

Create or edit an event on its own page: the form on the left, conflicts and attendees on the right, Delete apart from Save.

Built from: `event-editor`, `attendee-list`, `split-layout`

### Why

Context beside the form (clashes, who is invited) lets people fix problems before saving (Practical UI W15, L14); Delete sits away from Save so it is never hit by mistake (B13).

### When to use

- Creating and editing events, shifts, bookings in full.

### How to use

- Extend it: `{% extends "orca/layouts/event_editor.html" %}`, then fill only the blocks you need.
- Pass an event `form`; `conflicts` (sentences) appear as caution callouts in `event_aside`; `delete_url` shows Delete.

Extend: `{% extends "orca/layouts/event_editor.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `form_fields`, `event_aside`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `form`, `object`, `conflicts`, `delete_url`, `cancel_url`, `submit_label`.

#### Example: Child template

```django
{% extends "orca/layouts/event_editor.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# events/views.py
from django.urls import reverse
from django.views.generic import UpdateView

from orca.mixins import OrcaPageMixin

from .forms import EventForm
from .models import Event


class EventEdit(OrcaPageMixin, UpdateView):
    model = Event
    form_class = EventForm                     # see Event editor
    template_name = "orca/layouts/event_editor.html"
    list_url_name = "calendar"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        event = self.object
        # Bookings that overlap this one, shown as conflict warnings above the form.
        ctx["conflicts"] = [str(e) for e in Event.objects.filter(place=event.place, starts_at__lt=event.ends_at,
                                                                  ends_at__gt=event.starts_at).exclude(pk=event.pk)]
        ctx.update(title=f"Edit {event}", submit_label="Save event",
                   delete_url=reverse("event-delete", args=[event.pk]), cancel_url=reverse("calendar"))
        return ctx
```

**Principles applied:** Practical UI W15: Help people recover from errors; Practical UI L14: Reduce travel between related actions; Practical UI B13: Scale friction to the consequence

**ORCA guide items covered:** Event editor page

---

## Simple data page

`id: simple-data-page` · level: template · source: ORCA

A data page with everything in one place: title bar, summary tiles that filter, search, a filter drawer and the table.

Built from: `summary-tiles`, `list-header`, `filter-drawer`, `data-table`, `no-results`

### Why

Summary tiles answer 'how many of each' and double as the most used filters (Hick's law); the rest of the filters wait in a drawer so the table keeps the space (Practical UI S04).

### When to use

- Operational lists where counts by status matter: videos, alerts, tickets.

### How to use

- Extend it: `{% extends "orca/layouts/simple_data.html" %}`, then fill only the blocks you need.
- Use OrcaPageMixin with a ListView; pass `tiles` (label, value, url, tone, current), a GET `filter_form` and `active_filters` (count).

Extend: `{% extends "orca/layouts/simple_data.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `list_actions`, `summary`, `list_header`, `list`, `filter_panel`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `object_list`, `page_obj`, `columns`, `tiles`, `filter_form`, `active_filters`, URLs as in the generic list.

#### Example: Child template

```django
{% extends "orca/layouts/simple_data.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/forms.py
from django import forms

from .models import Album, Video


class VideoFilterForm(forms.Form):
    q = forms.CharField(label="Title contains", required=False)
    album = forms.ModelChoiceField(Album.objects.all(), required=False, empty_label="Any album")
    status = forms.MultipleChoiceField(choices=Video.Status.choices, required=False,
                                       widget=forms.CheckboxSelectMultiple)


# videos/views.py
from django.views.generic import ListView

from orca.mixins import OrcaPageMixin

from .forms import VideoFilterForm
from .models import Video


class VideoList(OrcaPageMixin, ListView):
    model = Video
    paginate_by = 25
    template_name = "orca/layouts/simple_data.html"
    list_columns = ["title", "album", "status", ("Views today", "views_today")]
    detail_url_name, create_url_name = "video-detail", "video-create"

    def get_queryset(self):
        qs = super().get_queryset()
        self.filter_form = VideoFilterForm(self.request.GET or None)
        if self.filter_form.is_valid():
            data = self.filter_form.cleaned_data
            if data["q"]:
                qs = qs.filter(title__icontains=data["q"])
            if data["album"]:
                qs = qs.filter(album=data["album"])
            if data["status"]:
                qs = qs.filter(status__in=data["status"])
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # The template puts the Filters button in the page actions and the form in the right drawer.
        ctx["filter_form"] = self.filter_form
        data = self.filter_form.cleaned_data if self.filter_form.is_valid() else {}
        ctx["active_filters"] = sum(1 for value in data.values() if value)
        return ctx
```

#### Summary tiles

```python
# videos/views.py (in the list view's get_context_data)
from django.db.models import Count
from django.http import QueryDict

counts = dict(Video.objects.values_list("status").annotate(n=Count("id")))
current = self.request.GET.get("status", "")


def tile_url(status):
    query = self.request.GET.copy()          # keep the other filters
    query.pop("page", None)
    if status:
        query["status"] = status
    else:
        query.pop("status", None)
    return "?" + query.urlencode()


ctx["tiles"] = [{"label": "All videos", "value": sum(counts.values()), "url": tile_url(""), "current": not current}] + [
    {"label": label, "value": counts.get(value, 0), "url": tile_url(value), "current": current == value,
     "tone": {"published": "positive", "draft": "neutral", "failed": "negative"}.get(value, "")}
    for value, label in Video.Status.choices
]
```

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI S04: Reveal secondary information when needed; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Simple data page (title bar, search, filter drawer, summary tiles, table)

---
