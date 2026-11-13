# Data and filtering

Tables, panels and the controls that narrow them: filter bars, list headers, summary tiles, record cards.

## Data table

`id: data-table` · level: pattern · source: Tangerine

A table of records with a toolbar, selectable rows, sortable headers, row actions and a pager; rows become cards on phones.

Built from: `table-toolbar`, `sortable-header`, `row-actions`, `table-pager`, `row-select`, `status-light`

### General description

A grid of rows and columns for comparing records across several attributes. It usually supports sorting, selecting rows, searching and paging.

#### Use cases

- Lists of users, orders, devices or documents.
- Comparing records on several fields at once.
- Acting on many rows together.

#### When not to use it

- Browsing items mostly by image: use a card grid.
- Layout of a page: use layout elements, not a table.
- Two or three simple facts per item: use a list.

#### Best practices

- Give every column a clear header and a table caption.
- Align numbers to the right and text to the left.
- Show a helpful empty state when there are no rows.
- Keep search, bulk actions and paging close to the table.

### When to use

- Lists of records people compare, sort or act on in bulk.

### When not to use

- Browsing items mostly by image: use a card grid.

### How to use

- `<div class="orca-data-table">`: a table toolbar, then `.orca-table-wrap` > `table.orca-table.orca-table--cards` with a caption, sortable headers, an optional `.orca-table__select` column and row actions; then a table pager.
- Each `td` has `data-label` so phones show 'Label: value' cards; the name cell is `.orca-table__name`.
- Selected rows get `aria-selected="true"` and the toolbar becomes the selection bar. Right-align numbers (`.is-num`). When empty, show a no-data state in one full-width cell.
- Long tables: set `--orca-table-max: 32rem` on the wrapper for a scrolling body with a sticky header.

#### Example: Videos

```django
<div class="orca-data-table">
  <div class="orca-toolbar__selection" role="region" aria-label="Selection">
    <strong>1 selected</strong>
    <button class="orca-button orca-button--dense" type="button">Disable</button>
    <button class="orca-button orca-button--link" type="button">Clear selection</button>
  </div>
  <div class="orca-table-wrap">
    <table class="orca-table orca-table--cards">
      <caption class="orca-sr-only">Videos, sorted by name</caption>
      <thead>
        <tr>
          <th scope="col" class="orca-table__select">
            <label class="orca-check">
              <input type="checkbox" aria-label="Select all videos">
              <span class="orca-check__box"></span>
            </label>
          </th>
          <th scope="col" aria-sort="ascending">
            <a class="orca-sort" href="#">
              Video
              {% icon "arrow-up" %}
            </a>
          </th>
          <th scope="col">Site</th>
          <th scope="col">Status</th>
          <th scope="col" class="is-num">
            <a class="orca-sort" href="#">
              Today
              {% icon "arrow-up" %}
            </a>
          </th>
          <th scope="col">Last seen</th>
          <th scope="col">
            <span class="orca-sr-only">Actions</span>
          </th>
        </tr>
      </thead>
      <tbody>
        {% for c in sample.videos %}
          <tr{% if forloop.first %} aria-selected="true"{% endif %}>
            <td class="orca-table__select">
              <label class="orca-check">
                <input type="checkbox" aria-label="Select {{ c.name }}"{% if forloop.first %} checked{% endif %}>
                <span class="orca-check__box"></span>
              </label>
            </td>
            <td class="orca-table__name" data-label="Video">
              <a href="#">{{ c.name }}</a>
            </td>
            <td data-label="Site">{{ c.site }}</td>
            <td data-label="Status">
              <span class="orca-status"><span class="orca-dot orca-dot--{{ c.status }}"></span>{{ c.status_text }}</span>
            </td>
            <td class="is-num" data-label="Today">{{ c.today }}</td>
            <td data-label="Last seen" class="is-muted">{{ c.last }}</td>
            <td data-label="">
              <div class="orca-row-actions">
                <button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="More actions for {{ c.name }}">
                  {% icon "more" %}
                </button>
              </div>
            </td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
  <div class="orca-table-pager">
    <span class="orca-num">1–5 of 12</span>
    <span class="orca-table-pager__nav">
      <button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Previous page" disabled>
        {% icon "chevron-left" %}
      </button>
      <button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Next page">
        {% icon "chevron-right" %}
      </button>
    </span>
  </div>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Sorting and bulk actions

```python
# videos/views.py
from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from .models import Video

SORTABLE = {"title", "-title", "recorded_on", "-recorded_on", "views_today", "-views_today"}


class VideoList(ListView):
    model = Video
    paginate_by = 25

    def get_ordering(self):
        sort = self.request.GET.get("sort", "title")     # sortable headers link to ?sort=-recorded_on
        return sort if sort in SORTABLE else "title"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["sort"] = self.get_ordering()                 # the header marks aria-sort from it
        return ctx


@require_POST
def bulk_archive(request):
    """The table is a form; each row checkbox is name="selected" value="{{ video.pk }}"."""
    ids = request.POST.getlist("selected")
    count = Video.objects.filter(pk__in=ids, owner=request.user).update(archived=True)
    messages.success(request, f"{count} videos archived.")
    return redirect("video-list")
```

**Classes:** `.orca-data-table`, `.orca-table--cards`, `.orca-table__select`, `.orca-table__name`, `.orca-table__empty`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI L14: Reduce travel between related actions; Practical UI W11: Make numbers scannable; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Data table

---

## Accuracy table

`id: accuracy-table` · level: pattern · source: Tangerine

Counted and reference values per video, with the difference and an accuracy bar coloured by threshold.

Built from: `table-card`, `progress-with-counts`

### General description

A table comparing a measured value with a reference value, showing the difference and how close it is. Colour and words flag results that are too far off.

#### Use cases

- Checking automatic counts against manual counts.
- Comparing model or test runs with expected results.
- Reviewing measurement quality across sites.

#### When not to use it

- Showing a single score: use a progress bar or stat.
- Trends over time: use a chart.

#### Best practices

- Show the difference as a signed number so direction is clear.
- Say what the thresholds are in a caption.
- Flag poor results with a word, not only colour.
- Right-align the numbers so they compare easily.

### When to use

- Validating counts against manual tallies; comparing models or runs.

### How to use

- A table with Counted, Reference, Difference (signed, `.orca-diff--up/down`) and Accuracy (`.orca-accuracy` with a bar `--orca-value`; `--caution` below 95%, `--negative` below 90%, with the word).
- Explain the thresholds in the caption or help text.

#### Example: Accuracy

```django
<div class="orca-table-wrap">
  <table class="orca-table">
    <caption class="orca-small orca-muted" style="text-align: start; padding-bottom: var(--orca-space-8)">Good from 95%, check below 95%, poor below 90%.</caption>
    <thead>
      <tr>
        <th scope="col">Video</th>
        <th scope="col" class="is-num">Counted</th>
        <th scope="col" class="is-num">Reference</th>
        <th scope="col" class="is-num">Difference</th>
        <th scope="col">Accuracy</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Entrance A</td>
        <td class="is-num">4,812</td>
        <td class="is-num">4,920</td>
        <td class="is-num orca-diff--down">−108</td>
        <td>
          <span class="orca-accuracy"><span class="orca-accuracy__bar" style="--orca-value: 97.8%"><span></span></span>97.8%</span>
        </td>
      </tr>
      <tr>
        <td>Gate 1</td>
        <td class="is-num">2,140</td>
        <td class="is-num">2,342</td>
        <td class="is-num orca-diff--down">−202</td>
        <td>
          <span class="orca-accuracy orca-accuracy--negative"><span class="orca-accuracy__bar" style="--orca-value: 91.4%"><span></span></span>91.4% · check</span>
        </td>
      </tr>
      <tr>
        <td>Car park</td>
        <td class="is-num">640</td>
        <td class="is-num">612</td>
        <td class="is-num orca-diff--up">+28</td>
        <td>
          <span class="orca-accuracy orca-accuracy--caution"><span class="orca-accuracy__bar" style="--orca-value: 95.4%"><span></span></span>95.4%</span>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

**Classes:** `.orca-accuracy`, `.orca-accuracy__bar`, `.orca-accuracy--caution`, `.orca-accuracy--negative`, `.orca-diff--up`, `.orca-diff--down`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Practical UI C03: Communicate meaning beyond colour; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Accuracy table

---

## Filter bar

`id: filter-bar` · level: pattern · source: Tangerine

The row above results showing applied filters as removable tags, the result count and Clear all.

Built from: `applied-filters`

### General description

A row above a list or table that shows which filters are active, usually as removable tags, with the result count and a way to clear them all.

#### Use cases

- Showing which filters narrow a list.
- Letting people remove one filter at a time.
- Confirming how many results match.

#### When not to use it

- The filter controls themselves: use a filter panel or drawer.
- Choosing one view among a few: use tabs.

#### Best practices

- Show only filters that are applied.
- Make each tag removable with one click.
- Offer a single 'Clear all' action.
- Announce the new result count to screen readers.

### When to use

- Any list, table, gallery or report with at least one filter applied.

### When not to use

- Filter fields in a row above the results: use the filter drawer, opened from the page actions.

### How to use

- `<div class="orca-filter-bar"><div class="orca-filter-bar__applied">` with 'Filtered by', one removable tag per applied filter and a 'Clear all' link button.
- Each tag's remove button is a link (or submits the GET form) without that filter; announce the new count politely.
- The controls are in the `filter-drawer`, opened by the Filters button in the page actions.

#### Example: Applied filters

```django
<div class="orca-filter-bar">
  <div class="orca-filter-bar__applied">
    <span class="orca-small orca-muted">Filtered by</span>
    <span class="orca-tag">
      <span class="orca-tag__text">Album: Summer 2026</span>
      <button class="orca-tag__remove" type="button" aria-label="Remove filter Album: Summer 2026">
        {% icon "close" %}
      </button>
    </span>
    <span class="orca-tag">
      <span class="orca-tag__text">Type: Video</span>
      <button class="orca-tag__remove" type="button" aria-label="Remove filter Type: Video">
        {% icon "close" %}
      </button>
    </span>
    <button class="orca-button orca-button--link" type="button">Clear all</button>
    <span class="orca-small orca-muted" role="status">14 videos</span>
  </div>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Filter form and list view

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
    template_name = "orca/generic/list.html"   # or "orca/layouts/simple_data.html"
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

**Classes:** `.orca-filter-bar`, `.orca-filter-bar__applied`

**Principles applied:** Practical UI S06: Make essential content visible or discoverable; Hick's law: fewer, clearer choices mean faster decisions; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Filter bar

---

## Panel

`id: panel` · level: pattern · source: Tangerine

A bordered page section with a header, a body and optional footer actions.

Built from: `panel-header`

### General description

A bordered section of a page with a header and a body, grouping related content into one clearly labelled block. It may have actions in a footer.

#### Use cases

- Dashboard blocks such as charts or summaries.
- Sections of a settings or detail page.
- Grouping a form's related fields.

#### When not to use it

- Wrapping every small item: too many boxes create clutter.
- Content that needs to stay hidden until asked for: use an accordion.

#### Best practices

- Give every panel a clear title that says what it answers.
- Put actions that affect the panel in its header or footer.
- Keep panels in a grid that reflows on small screens.
- Avoid nesting panels inside panels.

### When to use

- Dashboards, detail pages and settings: any self-contained block of content.

### How to use

- `<section class="orca-panel" aria-labelledby=…>` with a panel header, `.orca-panel__body` (`--flush` for tables and lists), and `.orca-panel__foot` for actions.
- Lay several panels out in `.orca-panels` (a responsive grid).

#### Example: Two panels

```django
<div class="orca-panels">
  <section class="orca-panel" aria-labelledby="pn-1">
    <div class="orca-panel-header">
      <div class="orca-panel-header__text">
        <h2 class="orca-panel-title" id="pn-1">People inside</h2>
        <p class="orca-panel-header__desc">All entrances</p>
      </div>
    </div>
    <div class="orca-panel__body">
      <p class="orca-stat-value orca-stat-value--lg">1,204</p>
      <progress class="orca-progress" value="1204" max="1500" aria-label="1,204 of 1,500 capacity"></progress>
    </div>
  </section>
  <section class="orca-panel" aria-labelledby="pn-2">
    <div class="orca-panel-header">
      <div class="orca-panel-header__text">
        <h2 class="orca-panel-title" id="pn-2">Notes</h2>
      </div>
    </div>
    <div class="orca-panel__body">
      <p class="orca-p">Gate 1 is closed after 18:00.</p>
    </div>
    <div class="orca-panel__foot">
      <button class="orca-button orca-button--dense" type="button">Edit notes</button>
    </div>
  </section>
</div>
```

**Classes:** `.orca-panel`, `.orca-panel__body`, `.orca-panel__body--flush`, `.orca-panel__foot`, `.orca-panels`

**Principles applied:** Practical UI L01: Group related information; Practical UI L14: Reduce travel between related actions; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Panel

---

## Tabbed panel set

`id: tabbed-panel-set` · level: pattern · source: Tangerine

One panel whose body switches between related views with tabs.

Built from: `panel`, `tab-bar`

### General description

A single box with tabs along the top that switch between related views of the same thing. Only one view shows at a time.

#### Use cases

- Switching a metric between day, week and month.
- Showing the same data as a chart or a table.
- Splitting a detail view into a few related parts.

#### When not to use it

- Steps that must happen in order: use a stepper.
- Views people need to compare side by side: show them together.

#### Best practices

- Keep tab labels short and clear.
- Keep the content height steady so the page does not jump.
- Remember the last selected tab where that helps.
- Limit tabs to a handful.

### When to use

- Today / This week / This month of the same metric; Chart / Table of the same data.

### How to use

- `.orca-panel` containing a panel header and an `.orca-tabs` with in-page tabs; each tab panel holds one view.
- Keep the same height across tabs to avoid jumps; remember the last tab per person when useful.

#### Example: Chart or table

```django
<section class="orca-panel" aria-labelledby="tps-t">
  <div class="orca-panel-header">
    <div class="orca-panel-header__text">
      <h2 class="orca-panel-title" id="tps-t">Visitors this week</h2>
    </div>
  </div>
  <div class="orca-tabs">
    <div class="orca-tabs__list" role="tablist" aria-label="View" data-orca-tabs>
      <button class="orca-tab" role="tab" type="button" id="tps-a" aria-controls="tps-pa" aria-selected="true">Chart</button>
      <button class="orca-tab" role="tab" type="button" id="tps-b" aria-controls="tps-pb" aria-selected="false">Summary</button>
    </div>
    <div class="orca-tabs__panel" role="tabpanel" id="tps-pa" aria-labelledby="tps-a">
      {% orca_chart "bar" sample.visitors_week %}
    </div>
    <div class="orca-tabs__panel" role="tabpanel" id="tps-pb" aria-labelledby="tps-b" hidden>
      <dl class="orca-kv">
        <div>
          <dt>Busiest day</dt>
          <dd>Saturday, 9,530</dd>
        </div>
        <div>
          <dt>Total</dt>
          <dd>49,920</dd>
        </div>
      </dl>
    </div>
  </div>
</section>
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
        # Each tab's chart: labels and one series per line.
        ctx["by_day"] = {"labels": ["Mon", "Tue", "Wed"], "series": [{"name": "Views", "values": [120, 180, 150]}]}
        return ctx
```

**Classes:** `.orca-panel`, `.orca-tabs`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI S06: Make essential content visible or discoverable; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Tabbed panel set

---

## Card list

`id: card-list` · level: pattern · source: Tangerine

Records as a vertical list of cards with name, key facts and actions; a phone-friendly alternative to a table.

Built from: `status-light`, `linked-card`, `record-actions`

### General description

A vertical list where each record is a card showing its name, a few key facts and actions. It reads well on narrow screens.

#### Use cases

- Showing records on phones.
- Browsing items with long names.
- Lists where people read more than they compare.

#### When not to use it

- Comparing many attributes across rows: use a table.
- Image-led browsing: use a card grid.

#### Best practices

- Make the whole card easy to tap.
- Put the most important fact first.
- Keep every card in the same layout.
- Keep actions few and clearly labelled.

### When to use

- Phones; lists people browse more than compare; records with long names.

### How to use

- `<ul class="orca-card-list">` of `<li class="orca-record-card">`: a leading visual, `.orca-record-card__title` with the link (it covers the card), `.orca-record-card__meta` and `.orca-record-card__end` actions.
- Offer it as the 'Cards' side of the view toggle, or use `orca-table--cards` to switch automatically.

#### Example: Record cards

```django
<ul class="orca-card-list" style="max-width: 32rem">
  {% for c in sample.videos|slice:":3" %}
    <li class="orca-record-card">
      <span class="orca-dot orca-dot--{{ c.status }}" aria-hidden="true"></span>
      <h3 class="orca-record-card__title">
        <a href="#">{{ c.name }}</a>
      </h3>
      <div class="orca-record-card__end">
        <button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="More actions for {{ c.name }}">
          {% icon "more" %}
        </button>
      </div>
      <p class="orca-record-card__meta">
        <span>{{ c.status_text }}</span>
        <span>{{ c.site }}</span>
        <span class="orca-num">{{ c.today }} today</span>
      </p>
    </li>
  {% endfor %}
</ul>
```

**Classes:** `.orca-card-list`, `.orca-record-card`, `.orca-record-card__title`, `.orca-record-card__meta`, `.orca-record-card__end`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Postel's law: accept varied input, output reliable and accessible UI; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Card list (record cards)

---

## List header

`id: list-header` · level: pattern · source: Tangerine

The bar above a list: title with count, search, view toggle and, for a list panel in a page, its create action.

Built from: `search-field`, `view-toggle`, `create-button`

### General description

The area above a list with its title, item count, search, view options and create button. It gathers the controls that change the list.

#### Use cases

- Top of a list page.
- Top of a list inside a dashboard panel.
- Putting search and create actions together.

#### When not to use it

- Page titles with no list below: use a page header.
- Complex filtering: use a filter panel.

#### Best practices

- Show the count next to the title.
- Keep controls in a predictable order.
- Put the main create action at the end.
- Stack the tools below the title on small screens.

### When to use

- The top of every list page or list panel.

### How to use

- `<div class="orca-list-header">` with `h2.orca-list-header__title` + `.orca-list-header__count`, then `.orca-list-header__tools` (search field, view toggle, create button).
- The page's Filters button goes in the page actions, not here, and opens the filter drawer.
- On phones the tools take the full width under the title.

#### Example: List header

```django
<div class="orca-list-header">
  <h2 class="orca-list-header__title">Videos <span class="orca-list-header__count">12</span></h2>
  <div class="orca-list-header__tools">
    <div class="orca-search">
      {% icon "search" %}
      <input class="orca-input orca-input--dense" type="search" placeholder=" " aria-label="Search videos">
      <button class="orca-search__clear" type="button" aria-label="Clear search" data-orca-clear>
        {% icon "close" %}
      </button>
    </div>
    <nav class="orca-segmented orca-segmented--dense orca-segmented--icons" aria-label="View">
      <a class="orca-segmented__item" href="#" aria-current="page" aria-label="Cards">
        {% icon "grid" %}
      </a>
      <a class="orca-segmented__item" href="#" aria-label="Table">
        {% icon "list" %}
      </a>
    </nav>
    <a class="orca-button orca-button--primary orca-button--dense orca-create orca-create--static" href="#">
      {% icon "plus" %}
      Add video
    </a>
  </div>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Search in the list view

```python
# videos/views.py — the list header's search submits ?q=…
from django.db.models import Q
from django.views.generic import ListView


class VideoList(ListView):
    model = Video
    paginate_by = 25

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(album__title__icontains=q))
        return qs
```

**Classes:** `.orca-list-header`, `.orca-list-header__title`, `.orca-list-header__count`, `.orca-list-header__tools`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI L14: Reduce travel between related actions; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** List header (search + filter + create)

---

## Summary tiles

`id: summary-tiles` · level: pattern · source: Tangerine

A row of small counts by status that also act as quick filters.

Built from: `summary-tile`

### General description

A row of small tiles, each showing a count for a status or group. They give a quick overview and often act as shortcuts to filter a list.

#### Use cases

- Counting items by state such as online or offline.
- Showing open and closed tasks.
- Counting issues by severity.

#### When not to use it

- Trends over time: use a chart.
- Many categories: use a filter menu or a table.

#### Best practices

- Put a clear label with each number.
- Start with an 'All' tile.
- Highlight the active tile with more than colour.
- Keep to a few meaningful states.

### When to use

- Above lists with a few meaningful states: online/offline, open/closed, by severity.

### How to use

- `<ul class="orca-summary-tiles">` of links or toggle buttons `.orca-summary-tile` with `__value` and `__label` (status dot + word); the active one `aria-current="true"`.
- Include 'All' as the first tile.

#### Example: Tiles

```django
<ul class="orca-summary-tiles">
  <li>
    <a class="orca-summary-tile" href="#" aria-current="true">
      <span class="orca-summary-tile__value">12</span>
      <span class="orca-summary-tile__label">All videos</span>
    </a>
  </li>
  <li>
    <a class="orca-summary-tile" href="#">
      <span class="orca-summary-tile__value">10</span>
      <span class="orca-summary-tile__label"><span class="orca-dot orca-dot--positive"></span>Online</span>
    </a>
  </li>
  <li>
    <a class="orca-summary-tile" href="#">
      <span class="orca-summary-tile__value">1</span>
      <span class="orca-summary-tile__label"><span class="orca-dot orca-dot--caution"></span>Degraded</span>
    </a>
  </li>
  <li>
    <a class="orca-summary-tile" href="#">
      <span class="orca-summary-tile__value">1</span>
      <span class="orca-summary-tile__label"><span class="orca-dot orca-dot--negative"></span>Offline</span>
    </a>
  </li>
</ul>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Counts by status

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

**Classes:** `.orca-summary-tiles`, `.orca-summary-tile`, `.orca-summary-tile__value`, `.orca-summary-tile__label`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Fitts's law: big, close, well-spaced targets are faster and safer; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Summary tiles

---

## Autocomplete results table

`id: autocomplete-results-table` · level: pattern · source: ORCA

Search-as-you-type results shown as a compact table with the matched text highlighted.

Built from: `search-field`, `table-card`

### General description

Search results shown as you type, in a compact table with the matching text highlighted. Several attributes per result help people tell them apart.

#### Use cases

- Finding records by name or code.
- Telling apart similar names on different sites.
- Quick lookup before opening a record.

#### When not to use it

- Choosing one value from a short fixed list: use a select.
- Single-field suggestions: use a plain suggestion list.

#### Best practices

- Wait a moment after typing before searching.
- Highlight the matching text.
- Limit the rows and link to the full results.
- Announce the result count to screen readers.

### When to use

- Searching records by name or code when similar results must be told apart (two 'Entrance A' on different sites).

### How to use

- A search field whose results (htmx, `hx-trigger="input changed delay:300ms"`) replace a `table.orca-table.orca-table--compact.orca-results-table`; matches wrapped in `<mark>`.
- At most 10 rows, then 'Show all 37 results'. Announce the count in a status element.

#### Example: Results

```django
<div class="orca-search-field" style="max-width: 32rem">
  <div class="orca-search">
    {% icon "search" %}
    <input class="orca-input" type="search" value="entr" aria-label="Search videos" aria-describedby="art-count">
  </div>
  <p class="orca-search-field__count" id="art-count" role="status">2 results</p>
</div>
<div class="orca-table-wrap" style="max-width: 32rem">
  <table class="orca-table orca-table--compact orca-results-table">
    <thead>
      <tr>
        <th scope="col">Video</th>
        <th scope="col">Site</th>
        <th scope="col">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <a class="orca-link orca-link--plain" href="#"><mark>Entr</mark>ance A</a>
        </td>
        <td>North building</td>
        <td>Online</td>
      </tr>
      <tr>
        <td>
          <a class="orca-link orca-link--plain" href="#"><mark>Entr</mark>ance B</a>
        </td>
        <td>North building</td>
        <td>Online</td>
      </tr>
    </tbody>
  </table>
</div>
```

**Classes:** `.orca-results-table`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI R12: Autocomplete for long lists; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Autocomplete results table

---

## No results

`id: no-results` · level: pattern · source: ORCA

What a list, table or feed shows when empty: the empty state, plus the applied filters when filters hide everything.

Built from: `empty-state`, `applied-filters`

### General description

A no-results state is what a list, table or search shows when there is nothing to display. It explains why and what to do next.

#### Use cases

- A new list with no items yet.
- A search or filter that matches nothing.
- A feed that is empty.

#### When not to use it

- Content that is still loading: show a loading state.
- Errors: use an error message.

#### Best practices

- Say whether it is empty or filtered.
- Offer a clear next step.
- Show the active filters and a Clear all action.
- Keep the tone calm.

### When to use

- Every list, table, grid and feed, for the empty and the filtered-empty cases.

### How to use

- First use: the empty state with the create action ('Add your first video').
- Filtered empty: the empty state ('No videos match these filters') above the applied filters with Clear all.

#### Example: Filtered empty

```django
<div class="orca-empty">
  {% orca_illustration "search" %}
  <h2 class="orca-empty-title">No videos match these filters</h2>
  <p class="orca-empty-text">Remove a filter, or clear them all to see every video.</p>
  <div class="orca-filter-bar__applied" style="justify-content: center">
    <span class="orca-tag">
      <span class="orca-tag__text">Album: Summer 2026</span>
      <button class="orca-tag__remove" type="button" aria-label="Remove filter Album: Summer 2026">
        {% icon "close" %}
      </button>
    </span>
    <button class="orca-button orca-button--link" type="button">Clear all</button>
  </div>
</div>
```

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Practical UI W15: Help people recover from errors; Postel's law: accept varied input, output reliable and accessible UI

**Related:** `generic-list`, `simple-data-page`, `feed-skeleton`

---
