# Charts

Charts drawn by Chart.js in a chart frame, in token colours, each with a text summary and its data as a table. One template tag; no chart code to write.

## Bar chart

`id: bar-chart` · level: pattern · source: ORCA

Bars comparing values across categories; grouped, stacked or horizontal.

Built from: `chart-frame`

### When to use

- Comparing quantities across categories or a few periods: visitors per day, alerts per site.

### When not to use

- Many periods (more than about 15): use a line chart.
- Parts of a whole: a stacked bar, or a doughnut for 2–5 parts.

### How to use

- `stacked=True` stacks series; `horizontal=True` for long category names or many categories.
- Start the value axis at zero; sort categories by value unless they have a natural order (days, hours).
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec; `orca.js` loads the vendored Chart.js only on pages with charts and draws it in the `--orca-chart-*` colours, redrawing when the theme changes.
- The canvas carries a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which also works without JavaScript.
- Never write a Chart.js configuration yourself: pass data to the tag so every chart reads the same.

### Accessibility

- Colour is never the only key: series have a legend; lines change dash; scatter series change shape.

#### Example: Bar chart

```django
{% orca_chart "bar" sample.visitors_week title="Visitors per day" subtitle="This week, people" caption="Source: line counts" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View: the chart data

```python
# videos/views.py
import datetime as dt

from django.db.models import Count
from django.db.models.functions import ExtractHour, TruncDate
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Visit


class ReportView(TemplateView):
    template_name = "videos/report.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        start = today - dt.timedelta(days=6)
        # Categories as labels, one series per bar colour; stacked=True or horizontal=True.
        rows = (Visit.objects.filter(at__date__gte=start).annotate(day=TruncDate("at"))
                .values_list("day", "entrance").annotate(n=Count("id")))
        counts = {(day, entrance): n for day, entrance, n in rows}
        days = [start + dt.timedelta(days=i) for i in range(7)]
        entrances = sorted({entrance for _, entrance, _ in rows})
        ctx["visits"] = {"labels": [d.strftime("%a") for d in days],
                         "series": [{"name": e, "values": [counts.get((d, e), 0) for d in days]} for e in entrances]}
        # Template: {% orca_chart "bar" visits title="Visitors per day" subtitle="This week" %}
        return ctx
```

**Classes:** `.orca-chart`, `.orca-chart-frame`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Bar chart

---

## Line chart

`id: line-chart` · level: pattern · source: ORCA

Lines showing how one or more values change over time.

Built from: `chart-frame`

### When to use

- Values over many time points: visitors per hour, accuracy per day.

### When not to use

- Few categories with no order: use bars.
- More than 4 series: split into small multiples.

### How to use

- Use `"area"` as the kind for one series where the volume matters.
- The second series is dashed so it differs without colour; label the reference ('Last Friday').
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec; `orca.js` loads the vendored Chart.js only on pages with charts and draws it in the `--orca-chart-*` colours, redrawing when the theme changes.
- The canvas carries a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which also works without JavaScript.
- Never write a Chart.js configuration yourself: pass data to the tag so every chart reads the same.

### Accessibility

- Colour is never the only key: series have a legend; lines change dash; scatter series change shape.

#### Example: Line chart

```django
{% orca_chart "line" sample.visitors_hours title="Visitors per hour" subtitle="Today compared with last Friday" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View: the chart data

```python
# videos/views.py
import datetime as dt

from django.db.models import Count
from django.db.models.functions import ExtractHour, TruncDate
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Visit


class ReportView(TemplateView):
    template_name = "videos/report.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        start = today - dt.timedelta(days=6)
        # Time points as labels, one series per line.
        hours = range(8, 20)
        last_friday = today - dt.timedelta(days=(today.weekday() - 4) % 7 or 7)

        def per_hour(day):
            counts = dict(Visit.objects.filter(at__date=day).annotate(h=ExtractHour("at"))
                          .values_list("h").annotate(n=Count("id")))
            return [counts.get(h, 0) for h in hours]
        ctx["visits"] = {"labels": [f"{h:02}" for h in hours],
                         "series": [{"name": "Today", "values": per_hour(today)},
                                    {"name": "Last Friday", "values": per_hour(last_friday)}]}
        # Template: {% orca_chart "line" visits title="Visitors per hour" %} ("area" for one series)
        return ctx
```

**Classes:** `.orca-chart`, `.orca-chart-frame`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Line chart

---

## Pie chart

`id: pie-chart` · level: pattern · source: ORCA

A circle split into the shares of one total, with a legend giving each value and percentage.

Built from: `chart-frame`

### When to use

- 2–5 shares of one total.

### When not to use

- More than 5 parts or similar shares: use a horizontal bar chart.

### How to use

- Order slices from largest, clockwise from 12 o'clock; group small ones into 'Other'.
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec; `orca.js` loads the vendored Chart.js only on pages with charts and draws it in the `--orca-chart-*` colours, redrawing when the theme changes.
- The canvas carries a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which also works without JavaScript.
- Never write a Chart.js configuration yourself: pass data to the tag so every chart reads the same.

### Accessibility

- Colour is never the only key: series have a legend; lines change dash; scatter series change shape.

#### Example: Pie chart

```django
{% orca_chart "pie" sample.by_entrance title="Visitors by entrance" subtitle="Today" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View: the chart data

```python
# videos/views.py
import datetime as dt

from django.db.models import Count
from django.db.models.functions import ExtractHour, TruncDate
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Visit


class ReportView(TemplateView):
    template_name = "videos/report.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        start = today - dt.timedelta(days=6)
        # Parts of a whole: labels and one series.
        rows = Visit.objects.filter(at__date=today).values_list("entrance").annotate(n=Count("id")).order_by("-n")
        ctx["share"] = {"labels": [name for name, _ in rows], "series": [{"name": "Visitors", "values": [n for _, n in rows]}]}
        # Template: {% orca_chart "pie" share title="Visitors by entrance" %} — one series; 2 to 5 parts read best
        return ctx
```

**Classes:** `.orca-chart`, `.orca-chart-frame`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Pie chart

---

## Doughnut chart

`id: doughnut-chart` · level: pattern · source: ORCA

A pie with the total in the middle.

Built from: `chart-frame`

### When to use

- Shares of a total where the total itself matters: visitors today by entrance.

### When not to use

- More than 5 parts: use bars.

### How to use

- Same rules as the pie chart; the centre shows the total.
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec; `orca.js` loads the vendored Chart.js only on pages with charts and draws it in the `--orca-chart-*` colours, redrawing when the theme changes.
- The canvas carries a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which also works without JavaScript.
- Never write a Chart.js configuration yourself: pass data to the tag so every chart reads the same.

### Accessibility

- Colour is never the only key: series have a legend; lines change dash; scatter series change shape.

#### Example: Doughnut chart

```django
{% orca_chart "doughnut" sample.by_entrance title="Visitors by entrance" subtitle="Today" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View: the chart data

```python
# videos/views.py
import datetime as dt

from django.db.models import Count
from django.db.models.functions import ExtractHour, TruncDate
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Visit


class ReportView(TemplateView):
    template_name = "videos/report.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        start = today - dt.timedelta(days=6)
        # Parts of a whole: labels and one series.
        rows = Visit.objects.filter(at__date=today).values_list("entrance").annotate(n=Count("id")).order_by("-n")
        ctx["share"] = {"labels": [name for name, _ in rows], "series": [{"name": "Visitors", "values": [n for _, n in rows]}]}
        # Template: {% orca_chart "doughnut" share title="Visitors by entrance" %} — one series; 2 to 5 parts read best
        return ctx
```

**Classes:** `.orca-chart`, `.orca-chart-frame`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Doughnut chart

---

## Scatter chart

`id: scatter-chart` · level: pattern · source: ORCA

Points placed by two values to show a relationship.

Built from: `chart-frame`

### When to use

- Two numeric measures per item: dwell time against visits per hour.

### When not to use

- One measure: use bars or a line.

### How to use

- Each series gets its own marker shape; name both axes in the subtitle with their units.
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec; `orca.js` loads the vendored Chart.js only on pages with charts and draws it in the `--orca-chart-*` colours, redrawing when the theme changes.
- The canvas carries a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which also works without JavaScript.
- Never write a Chart.js configuration yourself: pass data to the tag so every chart reads the same.

### Accessibility

- Colour is never the only key: series have a legend; lines change dash; scatter series change shape.

#### Example: Scatter chart

```django
{% orca_chart "scatter" sample.dwell_vs_visits title="Dwell time and visits" subtitle="x: average dwell (min), y: visits per hour" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View: the chart data

```python
# videos/views.py
import datetime as dt

from django.db.models import Count
from django.db.models.functions import ExtractHour, TruncDate
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Visit


class ReportView(TemplateView):
    template_name = "videos/report.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        start = today - dt.timedelta(days=6)
        # No labels; each series is a list of (x, y).
        # Points are (x, y) pairs; bubbles add a size: (x, y, size).
        ctx["points"] = {"labels": [], "series": [
            {"name": "Weekdays", "values": [(s.avg_dwell, s.visits) for s in weekday_stats]},
            {"name": "Weekends", "values": [(s.avg_dwell, s.visits) for s in weekend_stats]},
        ]}
        # Template: {% orca_chart "scatter" points title="Dwell time and visits" subtitle="x: minutes, y: visits per hour" %}
        return ctx
```

**Classes:** `.orca-chart`, `.orca-chart-frame`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Scatter chart

---

## Bubble chart

`id: bubble-chart` · level: pattern · source: ORCA

A scatter chart whose point size shows a third value.

Built from: `chart-frame`

### When to use

- Three measures per item, where the third is secondary: sites by dwell, visits and number of videos.

### When not to use

- Exact comparison of the third value: use a table.

### How to use

- Values are `x:y:size`; size scales by area, not radius.
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec; `orca.js` loads the vendored Chart.js only on pages with charts and draws it in the `--orca-chart-*` colours, redrawing when the theme changes.
- The canvas carries a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which also works without JavaScript.
- Never write a Chart.js configuration yourself: pass data to the tag so every chart reads the same.

### Accessibility

- Colour is never the only key: series have a legend; lines change dash; scatter series change shape.

#### Example: Bubble chart

```django
{% orca_chart "bubble" sample.sites_bubble title="Sites" subtitle="x: average dwell (min), y: visits per hour, size: videos" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View: the chart data

```python
# videos/views.py
import datetime as dt

from django.db.models import Count
from django.db.models.functions import ExtractHour, TruncDate
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Visit


class ReportView(TemplateView):
    template_name = "videos/report.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        start = today - dt.timedelta(days=6)
        # No labels; each series is a list of (x, y, size).
        # Points are (x, y) pairs; bubbles add a size: (x, y, size).
        ctx["points"] = {"labels": [], "series": [
            {"name": "Weekdays", "values": [(s.avg_dwell, s.visits, s.sites) for s in weekday_stats]},
            {"name": "Weekends", "values": [(s.avg_dwell, s.visits, s.sites) for s in weekend_stats]},
        ]}
        # Template: {% orca_chart "bubble" points title="Dwell time and visits" subtitle="x: minutes, y: visits per hour" %}
        return ctx
```

**Classes:** `.orca-chart`, `.orca-chart-frame`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Bubble chart

---

## Radar chart

`id: radar-chart` · level: pattern · source: ORCA

Scores on several axes drawn as a polygon, comparing one or two items.

Built from: `chart-frame`

### When to use

- Comparing one or two items across 4–8 scored criteria on the same scale.

### When not to use

- More than two items, or different scales: use a table or bars.

### How to use

- All axes must share the same scale (for example 0–100).
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec; `orca.js` loads the vendored Chart.js only on pages with charts and draws it in the `--orca-chart-*` colours, redrawing when the theme changes.
- The canvas carries a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which also works without JavaScript.
- Never write a Chart.js configuration yourself: pass data to the tag so every chart reads the same.

### Accessibility

- Colour is never the only key: series have a legend; lines change dash; scatter series change shape.

#### Example: Radar chart

```django
{% orca_chart "radar" sample.site_scores title="Site health" subtitle="Scores out of 100" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View: the chart data

```python
# videos/views.py
import datetime as dt

from django.db.models import Count
from django.db.models.functions import ExtractHour, TruncDate
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Visit


class ReportView(TemplateView):
    template_name = "videos/report.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        start = today - dt.timedelta(days=6)
        # Axes as labels, one series per shape.
        axes = ["Accuracy", "Uptime", "Coverage", "Freshness", "Calibration"]
        ctx["scores"] = {"labels": axes, "series": [{"name": site.name, "values": [site.score(a) for a in axes]}
                                                    for site in sites]}
        # Template: {% orca_chart "radar" scores title="Site health" unit="" %}
        return ctx
```

**Classes:** `.orca-chart`, `.orca-chart-frame`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Radar chart

---

## Polar area chart

`id: polar-area-chart` · level: pattern · source: ORCA

Equal-angle segments whose radius shows each value.

Built from: `chart-frame`

### When to use

- Cyclic categories or a compact overview of counts by type: alerts by type, visits by weekday.

### When not to use

- Precise comparison: use bars.

### How to use

- Order segments meaningfully (by time or by size).
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec; `orca.js` loads the vendored Chart.js only on pages with charts and draws it in the `--orca-chart-*` colours, redrawing when the theme changes.
- The canvas carries a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which also works without JavaScript.
- Never write a Chart.js configuration yourself: pass data to the tag so every chart reads the same.

### Accessibility

- Colour is never the only key: series have a legend; lines change dash; scatter series change shape.

#### Example: Polar area chart

```django
{% orca_chart "polar" sample.alerts_by_type title="Alerts by type" subtitle="Last 30 days" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View: the chart data

```python
# videos/views.py
import datetime as dt

from django.db.models import Count
from django.db.models.functions import ExtractHour, TruncDate
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Visit


class ReportView(TemplateView):
    template_name = "videos/report.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        start = today - dt.timedelta(days=6)
        # Categories as labels and one series.
        rows = Visit.objects.filter(at__date=today).values_list("entrance").annotate(n=Count("id")).order_by("-n")
        ctx["share"] = {"labels": [name for name, _ in rows], "series": [{"name": "Visitors", "values": [n for _, n in rows]}]}
        # Template: {% orca_chart "polar" share title="Visitors by entrance" %} — one series; 2 to 5 parts read best
        return ctx
```

**Classes:** `.orca-chart`, `.orca-chart-frame`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Polar area chart

---
