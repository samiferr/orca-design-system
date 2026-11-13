# Calendar views

Whole calendars rendered on the server from a list of events: month, week, day, multi-day, agenda and year, plus the toolbar, sidebar and legend around them.

## Month calendar

`id: month-calendar` · level: pattern · source: ORCA

Weeks of day cells showing each day's events, with '+N more' when a day overflows and a count dot on phones.

Built from: `calendar-header`, `weekday-header`, `week-row`

### When to use

- Planning across weeks: bookings, rotas, events, deadlines.

### When not to use

- Detailed times on one or two days: use the week or day view.

### How to use

- `{% orca_month_calendar events month="2026-11" today=today selected=day day_url="?day={date}" holidays=holidays max_per_day=3 %}`.
- Events are dicts: `title`, `start` and `end` (ISO date or datetime), `all_day`, `color` (1–8, the chart palette, or any CSS colour), `url`, `location`, `status` ('tentative', 'cancelled'). Pass your queryset as `.values()` or build the dicts in the view.
- Pass `today` (and `now` for time grids) from the view in the site's timezone; tests and previews pin them to a fixed date.
- Navigation is plain links with the period in the query string (`?month=2026-11`), so back, refresh and sharing work; htmx can swap only the grid.
- Multi-day all-day events show as bars on each day they cover; holidays label the cell.

### Accessibility

- Each day is a link or cell labelled with its full date and event count; the table has weekday column headers.

#### Example: November 2026

```django
{% orca_month_calendar sample.events month="2026-11" today=sample.today holidays=sample.holidays day_url="#{date}" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
import datetime as dt

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Event


class CalendarView(TemplateView):
    template_name = "videos/calendar.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        month = dt.date.fromisoformat(self.request.GET.get("month", today.strftime("%Y-%m")) + "-01")
        # Events are dicts or objects with title, start, end (date or datetime), all_day, color (1–8 or a
        # CSS colour), url, location and status ("tentative", "cancelled"). Aware datetimes are shown in the
        # active time zone.
        ctx["events"] = [
            {"title": e.title, "start": e.starts_at, "end": e.ends_at, "all_day": e.all_day,
             "color": e.calendar.color, "url": e.get_absolute_url(), "location": e.place}
            for e in Event.objects.filter(starts_at__date__lte=month + dt.timedelta(days=42),
                                          ends_at__date__gte=month - dt.timedelta(days=7))
        ]
        ctx["holidays"] = {"2026-11-11": "Armistice Day"}  # date → name
        ctx.update(month=month, today=today, now=timezone.localtime())
        return ctx
```

**Classes:** `.orca-month-view`, `.orca-cal-cell__count`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Fitts's law: big, close, well-spaced targets are faster and safer; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Month calendar

---

## Week view

`id: week-view` · level: pattern · source: ORCA

Seven day columns on an hour grid with events positioned by time, an all-day row and a line at the current time.

Built from: `week-header`, `all-day-row`, `hour-row`, `event-card`, `calendar-header`

### When to use

- Scheduling within a week: meetings, installs, shifts.

### How to use

- `{% orca_week_view events start=monday today=today now=now start_hour=7 end_hour=19 %}` (start defaults to today's week start).
- Events are dicts: `title`, `start` and `end` (ISO date or datetime), `all_day`, `color` (1–8, the chart palette, or any CSS colour), `url`, `location`, `status` ('tentative', 'cancelled'). Pass your queryset as `.values()` or build the dicts in the view.
- Pass `today` (and `now` for time grids) from the view in the site's timezone; tests and previews pin them to a fixed date.
- Navigation is plain links with the period in the query string (`?month=2026-11`), so back, refresh and sharing work; htmx can swap only the grid.
- The grid scrolls horizontally on narrow screens; offer day view as the phone default.

### Accessibility

- Every event is a link or button whose text gives title, day and times; the now-line is decorative.

#### Example: This week

```django
{% orca_week_view sample.events start="2026-11-02" today=sample.today now=sample.now start_hour=8 end_hour=19 %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
import datetime as dt

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Event


class CalendarView(TemplateView):
    template_name = "videos/calendar.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        month = dt.date.fromisoformat(self.request.GET.get("month", today.strftime("%Y-%m")) + "-01")
        # Events are dicts or objects with title, start, end (date or datetime), all_day, color (1–8 or a
        # CSS colour), url, location and status ("tentative", "cancelled"). Aware datetimes are shown in the
        # active time zone.
        ctx["events"] = [
            {"title": e.title, "start": e.starts_at, "end": e.ends_at, "all_day": e.all_day,
             "color": e.calendar.color, "url": e.get_absolute_url(), "location": e.place}
            for e in Event.objects.filter(starts_at__date__lte=month + dt.timedelta(days=42),
                                          ends_at__date__gte=month - dt.timedelta(days=7))
        ]
        ctx["holidays"] = {"2026-11-11": "Armistice Day"}  # date → name
        ctx.update(month=month, today=today, now=timezone.localtime())
        return ctx
```

**Classes:** `.orca-timegrid`, `.orca-timegrid__head`, `.orca-timegrid__allday`, `.orca-timegrid__body`, `.orca-timegrid__col`, `.orca-timegrid__event`, `.orca-timegrid__now`

**Principles applied:** Practical UI L01: Group related information; Jakob's law: work the way products people already know work; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Week view

---

## Day view

`id: day-view` · level: pattern · source: ORCA

One day on the hour grid: the full detail of a single day, and the phone default.

Built from: `hour-row`, `event-card`, `calendar-navigation`

### When to use

- Phones; a person's or a room's day; dense days.

### How to use

- `{% orca_week_view events start=day days=1 today=today now=now %}`.
- Events are dicts: `title`, `start` and `end` (ISO date or datetime), `all_day`, `color` (1–8, the chart palette, or any CSS colour), `url`, `location`, `status` ('tentative', 'cancelled'). Pass your queryset as `.values()` or build the dicts in the view.
- Pass `today` (and `now` for time grids) from the view in the site's timezone; tests and previews pin them to a fixed date.
- Pair with a mini calendar or a date strip to change day.

#### Example: Friday 6 November

```django
{% orca_week_view sample.events start=sample.today days=1 today=sample.today now=sample.now start_hour=9 end_hour=18 %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
import datetime as dt

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Event


class CalendarView(TemplateView):
    template_name = "videos/calendar.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        month = dt.date.fromisoformat(self.request.GET.get("month", today.strftime("%Y-%m")) + "-01")
        # Events are dicts or objects with title, start, end (date or datetime), all_day, color (1–8 or a
        # CSS colour), url, location and status ("tentative", "cancelled"). Aware datetimes are shown in the
        # active time zone.
        ctx["events"] = [
            {"title": e.title, "start": e.starts_at, "end": e.ends_at, "all_day": e.all_day,
             "color": e.calendar.color, "url": e.get_absolute_url(), "location": e.place}
            for e in Event.objects.filter(starts_at__date__lte=month + dt.timedelta(days=42),
                                          ends_at__date__gte=month - dt.timedelta(days=7))
        ]
        ctx["holidays"] = {"2026-11-11": "Armistice Day"}  # date → name
        ctx.update(month=month, today=today, now=timezone.localtime())
        return ctx
```

**Classes:** `.orca-timegrid--day`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Day view

---

## Agenda view

`id: agenda-view` · level: pattern · source: ORCA

Upcoming events listed by day, with times, colours and places: the most readable calendar on any screen.

Built from: `agenda-item`, `empty-state`

### When to use

- Phones, 'what's next' panels, screen-reader friendly alternative to grids, printing.

### How to use

- `{% orca_agenda events start=today days=7 today=today %}`.
- Events are dicts: `title`, `start` and `end` (ISO date or datetime), `all_day`, `color` (1–8, the chart palette, or any CSS colour), `url`, `location`, `status` ('tentative', 'cancelled'). Pass your queryset as `.values()` or build the dicts in the view.
- Show an empty state when nothing is planned ('Nothing planned this week').

#### Example: This week

```django
{% orca_agenda sample.events start="2026-11-02" days=7 today=sample.today %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
import datetime as dt

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Event


class CalendarView(TemplateView):
    template_name = "videos/calendar.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        month = dt.date.fromisoformat(self.request.GET.get("month", today.strftime("%Y-%m")) + "-01")
        # Events are dicts or objects with title, start, end (date or datetime), all_day, color (1–8 or a
        # CSS colour), url, location and status ("tentative", "cancelled"). Aware datetimes are shown in the
        # active time zone.
        ctx["events"] = [
            {"title": e.title, "start": e.starts_at, "end": e.ends_at, "all_day": e.all_day,
             "color": e.calendar.color, "url": e.get_absolute_url(), "location": e.place}
            for e in Event.objects.filter(starts_at__date__lte=month + dt.timedelta(days=42),
                                          ends_at__date__gte=month - dt.timedelta(days=7))
        ]
        ctx["holidays"] = {"2026-11-11": "Armistice Day"}  # date → name
        ctx.update(month=month, today=today, now=timezone.localtime())
        return ctx
```

**Classes:** `.orca-agenda-view`, `.orca-agenda-view__day`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI L03: Establish an order of importance

**ORCA guide items covered:** Agenda (list) view

---

## Year view

`id: year-view` · level: pattern · source: ORCA

Twelve small months with event days marked, to see a year's rhythm and jump to any day.

Built from: `mini-calendar`

### When to use

- Holiday planning, annual schedules, picking dates far ahead.

### How to use

- `{% orca_year_view year=2026 events=events today=today url="?day={date}" %}`.
- Days with events carry a dot; the URL template gets the ISO date.

#### Example: 2026

```django
{% orca_year_view year=2026 events=sample.events today=sample.today url="#{date}" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
import datetime as dt

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Event


class CalendarView(TemplateView):
    template_name = "videos/calendar.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        month = dt.date.fromisoformat(self.request.GET.get("month", today.strftime("%Y-%m")) + "-01")
        # Events are dicts or objects with title, start, end (date or datetime), all_day, color (1–8 or a
        # CSS colour), url, location and status ("tentative", "cancelled"). Aware datetimes are shown in the
        # active time zone.
        ctx["events"] = [
            {"title": e.title, "start": e.starts_at, "end": e.ends_at, "all_day": e.all_day,
             "color": e.calendar.color, "url": e.get_absolute_url(), "location": e.place}
            for e in Event.objects.filter(starts_at__date__lte=month + dt.timedelta(days=42),
                                          ends_at__date__gte=month - dt.timedelta(days=7))
        ]
        ctx["holidays"] = {"2026-11-11": "Armistice Day"}  # date → name
        ctx.update(month=month, today=today, now=timezone.localtime())
        return ctx
```

**Classes:** `.orca-year-view`

**Principles applied:** Practical UI L09: Set spacing by relationship; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Year view

---

## Multi-day view

`id: multi-day-view` · level: pattern · source: ORCA

Three (or any number of) days on the hour grid, between the day and week views.

Built from: `week-header`, `all-day-row`, `event-card`

### When to use

- Tablets, side panels, 'today and the next two days'.

### How to use

- `{% orca_week_view events start=today days=3 today=today now=now %}`.
- Events are dicts: `title`, `start` and `end` (ISO date or datetime), `all_day`, `color` (1–8, the chart palette, or any CSS colour), `url`, `location`, `status` ('tentative', 'cancelled'). Pass your queryset as `.values()` or build the dicts in the view.

#### Example: Next three days

```django
{% orca_week_view sample.events start="2026-11-04" days=3 today=sample.today now=sample.now start_hour=8 end_hour=18 %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
import datetime as dt

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Event


class CalendarView(TemplateView):
    template_name = "videos/calendar.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        month = dt.date.fromisoformat(self.request.GET.get("month", today.strftime("%Y-%m")) + "-01")
        # Events are dicts or objects with title, start, end (date or datetime), all_day, color (1–8 or a
        # CSS colour), url, location and status ("tentative", "cancelled"). Aware datetimes are shown in the
        # active time zone.
        ctx["events"] = [
            {"title": e.title, "start": e.starts_at, "end": e.ends_at, "all_day": e.all_day,
             "color": e.calendar.color, "url": e.get_absolute_url(), "location": e.place}
            for e in Event.objects.filter(starts_at__date__lte=month + dt.timedelta(days=42),
                                          ends_at__date__gte=month - dt.timedelta(days=7))
        ]
        ctx["holidays"] = {"2026-11-11": "Armistice Day"}  # date → name
        ctx.update(month=month, today=today, now=timezone.localtime())
        return ctx
```

**Classes:** `.orca-timegrid`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Multi-day view

---

## Calendar toolbar

`id: calendar-toolbar` · level: pattern · source: ORCA

The bar above any calendar view: previous, Today, next, the period title, the view switcher and a create button.

Built from: `calendar-header`, `create-button`

### When to use

- Above every month, week, day, agenda and year view.

### How to use

- `<div class="orca-cal-header">` with the calendar navigation, `h2.orca-cal-header__title` and the view switcher in `.orca-cal-header__end`; add the create button last.
- Navigation is plain links with the period in the query string (`?month=2026-11`), so back, refresh and sharing work; htmx can swap only the grid.
- The title announces the period politely when it changes (`aria-live`).

#### Example: Toolbar

```django
<div class="orca-cal-header">
  <div class="orca-cal-nav">
    <a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Previous week">
      {% icon "chevron-left" %}
    </a>
    <a class="orca-button" href="#">Today</a>
    <a class="orca-icon-button orca-icon-button--outlined" href="#" aria-label="Next week">
      {% icon "chevron-right" %}
    </a>
  </div>
  <h2 class="orca-cal-header__title" aria-live="polite">2–8 November 2026</h2>
  <div class="orca-row orca-cal-header__end">
    <nav class="orca-segmented orca-segmented--dense" aria-label="Calendar view">
      <a class="orca-segmented__item" href="#">Day</a>
      <a class="orca-segmented__item" href="#" aria-current="page">Week</a>
      <a class="orca-segmented__item" href="#">Month</a>
      <a class="orca-segmented__item" href="#">Agenda</a>
    </nav>
    <a class="orca-button orca-button--primary" href="#">
      {% icon "plus" %}
      New event
    </a>
  </div>
</div>
```

**Classes:** `.orca-cal-header`, `.orca-cal-header__title`, `.orca-cal-header__end`

**Principles applied:** Jakob's law: work the way products people already know work; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Calendar toolbar

---

## Mini-calendar sidebar

`id: mini-calendar-sidebar` · level: pattern · source: ORCA

A sidebar beside the main calendar: create button, mini calendar to jump to any date, and the calendars legend.

Built from: `mini-calendar`, `create-button`

### When to use

- Full calendar pages with more than one calendar or long-range navigation.

### How to use

- `<div class="orca-cal-layout">` with `<aside class="orca-cal-sidebar">` first and the toolbar and view second.
- The mini calendar's selected day matches the main view; event days carry a dot.

#### Example: Sidebar

```django
<div class="orca-cal-layout">
  <aside class="orca-cal-sidebar" aria-label="Calendar options">
    <a class="orca-button orca-button--primary" href="#">
      {% icon "plus" %}
      New event
    </a>
    {% orca_mini_calendar "2026-11-01" selected="2026-11-06" today="2026-11-06" url="#{date}" nav_url="#{month}" events="2026-11-02,2026-11-03,2026-11-04,2026-11-05,2026-11-06,2026-11-10" %}
    <fieldset class="orca-cal-legend">
      <legend>Calendars</legend>
      <label class="orca-check" style="--orca-event: var(--orca-chart-1)"><input type="checkbox" checked><span class="orca-check__box"></span>Deliveries</label>
      <label class="orca-check" style="--orca-event: var(--orca-chart-3)"><input type="checkbox" checked><span class="orca-check__box"></span>Meetings</label>
    </fieldset>
  </aside>
  {% orca_agenda sample.events start="2026-11-06" days=5 today=sample.today %}
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
import datetime as dt

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Event


class CalendarView(TemplateView):
    template_name = "videos/calendar.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        month = dt.date.fromisoformat(self.request.GET.get("month", today.strftime("%Y-%m")) + "-01")
        # Events are dicts or objects with title, start, end (date or datetime), all_day, color (1–8 or a
        # CSS colour), url, location and status ("tentative", "cancelled"). Aware datetimes are shown in the
        # active time zone.
        ctx["events"] = [
            {"title": e.title, "start": e.starts_at, "end": e.ends_at, "all_day": e.all_day,
             "color": e.calendar.color, "url": e.get_absolute_url(), "location": e.place}
            for e in Event.objects.filter(starts_at__date__lte=month + dt.timedelta(days=42),
                                          ends_at__date__gte=month - dt.timedelta(days=7))
        ]
        ctx["holidays"] = {"2026-11-11": "Armistice Day"}  # date → name
        ctx.update(month=month, today=today, now=timezone.localtime())
        return ctx
```

**Classes:** `.orca-cal-layout`, `.orca-cal-sidebar`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Mini-calendar sidebar

---

## Calendar legend

`id: calendar-legend` · level: pattern · source: ORCA

The list of calendars, each a checkbox in its colour, to show or hide its events.

Built from: `choice-group`, `legend-item`

### When to use

- Any calendar showing events from more than one source, person or type.

### How to use

- `<fieldset class="orca-cal-legend">` with a `legend` and `label.orca-check` items, each setting `--orca-event` to the calendar's colour.
- Submit changes as a GET filter (`?cal=deliveries&cal=meetings`) or toggle with htmx.

#### Example: Calendars

```django
<fieldset class="orca-cal-legend">
  <legend>Calendars</legend>
  <label class="orca-check" style="--orca-event: var(--orca-chart-1)"><input type="checkbox" checked><span class="orca-check__box"></span>Deliveries</label>
  <label class="orca-check" style="--orca-event: var(--orca-chart-2)"><input type="checkbox" checked><span class="orca-check__box"></span>Installs and audits</label>
  <label class="orca-check" style="--orca-event: var(--orca-chart-3)"><input type="checkbox" checked><span class="orca-check__box"></span>Meetings</label>
  <label class="orca-check" style="--orca-event: var(--orca-chart-4)"><input type="checkbox"><span class="orca-check__box"></span>Public holidays</label>
</fieldset>
```

**Classes:** `.orca-cal-legend`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Calendar legend (calendars and colours)

---
