# Charts

Charts drawn by Chart.js in a chart frame, in token colours, each with a text summary and a data table. One template tag, no chart code.

## Bar chart

`id: bar-chart` · level: pattern · source: ORCA

Bars comparing values across categories; grouped, stacked or horizontal.

Built from: `chart-frame`

### General description

A chart that compares values across categories using bars of different lengths. Bars can be vertical or horizontal.

#### Use cases

- Comparing amounts across categories.
- Showing values over a few time periods.
- Ranking items from largest to smallest.

#### When not to use it

- Many time points showing a trend: use a line chart.
- Showing parts of a whole: use a pie or stacked bar.

#### Best practices

- Start the value axis at zero.
- Sort bars by value unless the order is natural.
- Use horizontal bars for long labels.
- Label bars or provide a data table.

### When to use

- Comparing categories or a few periods, such as visitors per day or alerts per site.

### When not to use

- Many periods (more than about 15): use a line chart.
- Parts of a whole: a stacked bar, or a doughnut for 2–5 parts.

### How to use

- `stacked=True` stacks series; `horizontal=True` for long category names or many categories.
- Start the value axis at zero; sort categories by value unless they have a natural order (days, hours).
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec. `orca.js` loads the vendored Chart.js only on pages with charts, draws it in the `--orca-chart-*` colours and redraws on theme change.
- The canvas has a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which works without JavaScript too.
- Never write Chart.js configuration yourself; pass data to the tag so all charts look the same.

### Accessibility

- Colour is never the only key: series have a legend, lines vary in dash and scatter series vary in shape.

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

### General description

A chart that connects points with lines to show how a value changes over time.

#### Use cases

- Showing trends over days, months or years.
- Comparing a value with an earlier period.
- Spotting rises, falls and patterns.

#### When not to use it

- A few unordered categories: use a bar chart.
- More than a few series: split into smaller charts.

#### Best practices

- Put time on the horizontal axis.
- Limit to about four lines.
- Vary line style as well as colour.
- Label the lines directly or in a legend.

### When to use

- Values over many time points: visitors per hour, accuracy per day.

### When not to use

- Few categories with no order: use bars.
- More than 4 series: split into small multiples.

### How to use

- Use `"area"` as the kind for one series when volume matters.
- The second series is dashed so it differs without colour; label the reference ('Last Friday').
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec. `orca.js` loads the vendored Chart.js only on pages with charts, draws it in the `--orca-chart-*` colours and redraws on theme change.
- The canvas has a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which works without JavaScript too.
- Never write Chart.js configuration yourself; pass data to the tag so all charts look the same.

### Accessibility

- Colour is never the only key: series have a legend, lines vary in dash and scatter series vary in shape.

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

A circle split into shares of one total, with a legend showing each value and percentage.

Built from: `chart-frame`

### General description

A circle divided into slices that show how a total splits into parts.

#### Use cases

- Showing shares of a total.
- Showing a simple split between a few groups.
- Giving a quick overview of proportions.

#### When not to use it

- More than five parts or close values: use a bar chart.
- Comparing values over time: use a line chart.

#### Best practices

- Keep to two to five slices.
- Order slices from largest, starting at the top.
- Show exact values or percentages in a legend.
- Group small slices as 'Other'.

### When to use

- 2–5 shares of one total.

### When not to use

- More than 5 parts or similar shares: use a horizontal bar chart.

### How to use

- Order slices from largest, clockwise from 12 o'clock; group small ones into 'Other'.
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec. `orca.js` loads the vendored Chart.js only on pages with charts, draws it in the `--orca-chart-*` colours and redraws on theme change.
- The canvas has a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which works without JavaScript too.
- Never write Chart.js configuration yourself; pass data to the tag so all charts look the same.

### Accessibility

- Colour is never the only key: series have a legend, lines vary in dash and scatter series vary in shape.

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

### General description

A pie chart with a hole in the middle, where the total or a key figure can be shown.

#### Use cases

- Showing shares of a total with the total in the centre.
- Showing progress toward a goal.
- Giving a compact overview of a split.

#### When not to use it

- More than five parts: use a bar chart.
- Comparing values precisely: use a bar chart.

#### Best practices

- Show the total in the centre.
- Keep to a few slices.
- Provide values in a legend or table.
- Order slices by size.

### When to use

- Shares of a total where the total itself matters: visitors today by entrance.

### When not to use

- More than 5 parts: use bars.

### How to use

- Same rules as the pie chart; the centre shows the total.
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec. `orca.js` loads the vendored Chart.js only on pages with charts, draws it in the `--orca-chart-*` colours and redraws on theme change.
- The canvas has a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which works without JavaScript too.
- Never write Chart.js configuration yourself; pass data to the tag so all charts look the same.

### Accessibility

- Colour is never the only key: series have a legend, lines vary in dash and scatter series vary in shape.

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

### General description

A chart that places points by two number values to show whether and how they are related.

#### Use cases

- Checking whether two measures are related.
- Spotting outliers in data.
- Showing clusters of similar items.

#### When not to use it

- One measure only: use a bar or line chart.
- Time trends: use a line chart.

#### Best practices

- Label both axes with units.
- Use different marker shapes for groups.
- Avoid too many points that overlap.
- Mention any pattern in text.

### When to use

- Two numeric measures per item: dwell time against visits per hour.

### When not to use

- One measure: use bars or a line.

### How to use

- Each series gets its own marker shape; name both axes in the subtitle with their units.
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec. `orca.js` loads the vendored Chart.js only on pages with charts, draws it in the `--orca-chart-*` colours and redraws on theme change.
- The canvas has a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which works without JavaScript too.
- Never write Chart.js configuration yourself; pass data to the tag so all charts look the same.

### Accessibility

- Colour is never the only key: series have a legend, lines vary in dash and scatter series vary in shape.

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

### General description

A scatter chart where the size of each point shows a third value.

#### Use cases

- Comparing items across three measures.
- Showing size alongside position, such as sales and share.
- Spotting groups or outliers with weight.

#### When not to use it

- Comparing exact sizes: use a table or bars.
- Only two measures: use a scatter chart.

#### Best practices

- Scale bubble area, not radius, to value.
- Label the axes and what size means.
- Keep the number of bubbles manageable.
- Provide a table with exact values.

### When to use

- Three measures per item, where the third is secondary: sites by dwell, visits and number of videos.

### When not to use

- Exact comparison of the third value: use a table.

### How to use

- Values are `x:y:size`; size scales by area, not radius.
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec. `orca.js` loads the vendored Chart.js only on pages with charts, draws it in the `--orca-chart-*` colours and redraws on theme change.
- The canvas has a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which works without JavaScript too.
- Never write Chart.js configuration yourself; pass data to the tag so all charts look the same.

### Accessibility

- Colour is never the only key: series have a legend, lines vary in dash and scatter series vary in shape.

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

### General description

A chart that shows scores on several axes as a polygon, so the shape reveals strengths and gaps.

#### Use cases

- Comparing one or two items across several criteria.
- Showing a profile, such as skills or health scores.
- Spotting weak areas at a glance.

#### When not to use it

- More than two items: use a table or bars.
- Criteria on different scales: use bars.

#### Best practices

- Use the same scale on every axis.
- Use four to eight axes.
- Order axes in a meaningful way.
- Provide a table for exact values.

### When to use

- Comparing one or two items across 4–8 scored criteria on the same scale.

### When not to use

- More than two items, or different scales: use a table or bars.

### How to use

- All axes must share the same scale (for example 0–100).
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec. `orca.js` loads the vendored Chart.js only on pages with charts, draws it in the `--orca-chart-*` colours and redraws on theme change.
- The canvas has a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which works without JavaScript too.
- Never write Chart.js configuration yourself; pass data to the tag so all charts look the same.

### Accessibility

- Colour is never the only key: series have a legend, lines vary in dash and scatter series vary in shape.

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

### General description

A round chart with equal-angle segments, where each segment's distance from the centre shows its value.

#### Use cases

- Showing counts across repeating categories, such as weekdays.
- Giving a compact overview by type.
- Comparing a handful of values in a round layout.

#### When not to use it

- Precise comparisons: use a bar chart.
- Parts of a whole: use a pie or doughnut chart.

#### Best practices

- Order segments by time or size.
- Label each segment.
- Use a scale that starts at zero.
- Provide a table with exact values.

### When to use

- Cyclic categories or a compact overview of counts by type: alerts by type, visits by weekday.

### When not to use

- Precise comparison: use bars.

### How to use

- Order segments meaningfully (by time or by size).
- Every chart: `{% orca_chart kind data title="…" subtitle="unit and period" caption="source" unit="%" %}`.
- `data` is a dict `{"labels": […], "series": [{"name", "values"}]}` or a string `"labels=Mon,Tue | Entrance A=120,180"`.
- The tag writes a `<canvas>` with the chart spec. `orca.js` loads the vendored Chart.js only on pages with charts, draws it in the `--orca-chart-*` colours and redraws on theme change.
- The canvas has a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table, which works without JavaScript too.
- Never write Chart.js configuration yourself; pass data to the tag so all charts look the same.

### Accessibility

- Colour is never the only key: series have a legend, lines vary in dash and scatter series vary in shape.

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
