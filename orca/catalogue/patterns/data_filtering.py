from ..registry import add, category
from . import Pattern

C = category(
    "data-filtering", "Data and filtering",
    "Tables, panels and the controls that narrow them: filter bars, list headers, summary tiles and record cards.",
    level="pattern",
)

ROWS = """{% for c in sample.videos %}<tr{% if forloop.first %} aria-selected="true"{% endif %}>
  <td class="orca-table__select"><label class="orca-check"><input type="checkbox" aria-label="Select {{ c.name }}"{% if forloop.first %} checked{% endif %}><span class="orca-check__box"></span></label></td>
  <td class="orca-table__name" data-label="Video"><a href="#">{{ c.name }}</a></td><td data-label="Site">{{ c.site }}</td>
  <td data-label="Status"><span class="orca-status"><span class="orca-dot orca-dot--{{ c.status }}"></span>{{ c.status_text }}</span></td>
  <td class="is-num" data-label="Today">{{ c.today }}</td><td data-label="Last seen" class="is-muted">{{ c.last }}</td>
  <td data-label=""><div class="orca-row-actions"><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="More actions for {{ c.name }}">{% icon "more" %}</button></div></td></tr>{% endfor %}"""

add(Pattern(
    "data-table", "Data table", C,
    "A table of records with a toolbar, selectable rows, sortable headers, row actions and a pager; rows become cards on phones.",
    why="Tables are the fastest way to compare records on several attributes (Miller's law); keeping search, bulk actions and paging next to the rows they affect shortens every task (Practical UI L14).",
    when=["Lists of records people compare, sort or act on in bulk."],
    avoid=["Browsing items mostly by image: use a card grid."],
    how=["`<div class=\"orca-data-table\">`: a table toolbar, then `.orca-table-wrap` > `table.orca-table.orca-table--cards` with a caption, sortable headers, an optional `.orca-table__select` column and row actions; then a table pager.",
         "Each `td` carries `data-label` so phones show 'Label: value' cards; the name cell is `.orca-table__name`.",
         "Selected rows `aria-selected=\"true\"` and the toolbar switches to the selection bar. Numbers right-aligned (`.is-num`). Empty: a no-data state in one full-width cell.",
         "Long tables: set `--orca-table-max: 32rem` on the wrapper for a scrolling body with a sticky header."],
    classes=[".orca-data-table", ".orca-table--cards", ".orca-table__select", ".orca-table__name", ".orca-table__empty"],
    laws=["miller", "L14", "W11", "postel"],
    uses=["table-toolbar", "sortable-header", "row-actions", "table-pager", "checkbox", "status-light"],
    examples=[("Videos", """<div class="orca-data-table">
  <div class="orca-toolbar__selection" role="region" aria-label="Selection"><strong>1 selected</strong><button class="orca-button orca-button--dense" type="button">Disable</button><button class="orca-button orca-button--link" type="button">Clear selection</button></div>
  <div class="orca-table-wrap"><table class="orca-table orca-table--cards"><caption class="orca-sr-only">Videos, sorted by name</caption>
    <thead><tr><th scope="col" class="orca-table__select"><label class="orca-check"><input type="checkbox" aria-label="Select all videos"><span class="orca-check__box"></span></label></th>
      <th scope="col" aria-sort="ascending"><a class="orca-sort" href="#">Video{% icon "arrow-up" %}</a></th><th scope="col">Site</th><th scope="col">Status</th><th scope="col" class="is-num"><a class="orca-sort" href="#">Today{% icon "arrow-up" %}</a></th><th scope="col">Last seen</th><th scope="col"><span class="orca-sr-only">Actions</span></th></tr></thead>
    <tbody>""" + ROWS + """</tbody></table></div>
  <div class="orca-table-pager"><span class="orca-num">1–5 of 12</span><span class="orca-table-pager__nav"><button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Previous page" disabled>{% icon "chevron-left" %}</button><button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Next page">{% icon "chevron-right" %}</button></span></div>
</div>""")],
    guide=["Data table"], source="Tangerine",
))

add(Pattern(
    "accuracy-table", "Accuracy table", C,
    "Counted versus reference values per video, with the difference and an accuracy bar coloured by threshold.",
    why="Comparing two numbers is easier with the difference computed (Tesler's law); a bar and a word for each threshold make poor accuracy visible without colour alone (C03).",
    when=["Validating counts against manual tallies; comparing models or runs."],
    how=["A table with Counted, Reference, Difference (signed, `.orca-diff--up/down`) and Accuracy (`.orca-accuracy` with a bar `--orca-value`; `--caution` below 95%, `--negative` below 90%, with the word).",
         "Explain the thresholds in the caption or help text."],
    classes=[".orca-accuracy", ".orca-accuracy__bar", ".orca-accuracy--caution", ".orca-accuracy--negative", ".orca-diff--up", ".orca-diff--down"],
    laws=["tesler", "C03", "W11"],
    uses=["table-card", "progress-bar"],
    examples=[("Accuracy", """<div class="orca-table-wrap"><table class="orca-table"><caption class="orca-small orca-muted" style="text-align: start; padding-bottom: var(--orca-space-8)">Good from 95%, check below 95%, poor below 90%.</caption>
  <thead><tr><th scope="col">Video</th><th scope="col" class="is-num">Counted</th><th scope="col" class="is-num">Reference</th><th scope="col" class="is-num">Difference</th><th scope="col">Accuracy</th></tr></thead>
  <tbody><tr><td>Entrance A</td><td class="is-num">4,812</td><td class="is-num">4,920</td><td class="is-num orca-diff--down">−108</td><td><span class="orca-accuracy"><span class="orca-accuracy__bar" style="--orca-value: 97.8%"><span></span></span>97.8%</span></td></tr>
  <tr><td>Gate 1</td><td class="is-num">2,140</td><td class="is-num">2,342</td><td class="is-num orca-diff--down">−202</td><td><span class="orca-accuracy orca-accuracy--negative"><span class="orca-accuracy__bar" style="--orca-value: 91.4%"><span></span></span>91.4% · check</span></td></tr>
  <tr><td>Car park</td><td class="is-num">640</td><td class="is-num">612</td><td class="is-num orca-diff--up">+28</td><td><span class="orca-accuracy orca-accuracy--caution"><span class="orca-accuracy__bar" style="--orca-value: 95.4%"><span></span></span>95.4%</span></td></tr></tbody></table></div>""")],
    guide=["Accuracy table"], source="Tangerine",
))

add(Pattern(
    "filter-bar", "Filter bar", C,
    "The row above the results that shows the applied filters as removable tags, the result count and Clear all.",
    why="Filters that are on must stay visible and reversible without reopening anything (Practical UI S06, Postel's law); "
        "the controls themselves live in the filter drawer, so the page head keeps one Filters button instead of a row of fields (Hick's law).",
    when=["Every list, table, gallery or report while at least one filter is applied."],
    avoid=["Filter fields in a row above the results: put them in the filter drawer, opened from the page actions."],
    how=["`<div class=\"orca-filter-bar\"><div class=\"orca-filter-bar__applied\">` with 'Filtered by', one removable tag per applied filter and a 'Clear all' link button.",
         "Each tag's remove button is a link (or submits the GET form) without that filter; announce the new count politely.",
         "The controls are in the `filter-drawer`, opened by the Filters button in the page actions."],
    classes=[".orca-filter-bar", ".orca-filter-bar__applied"],
    laws=["S06", "hick", "postel"],
    uses=["tag", "link-action"],
    examples=[("Applied filters", """<div class="orca-filter-bar">
  <div class="orca-filter-bar__applied"><span class="orca-small orca-muted">Filtered by</span><span class="orca-tag"><span class="orca-tag__text">Album: Summer 2026</span><button class="orca-tag__remove" type="button" aria-label="Remove filter Album: Summer 2026">{% icon "close" %}</button></span><span class="orca-tag"><span class="orca-tag__text">Type: Video</span><button class="orca-tag__remove" type="button" aria-label="Remove filter Type: Video">{% icon "close" %}</button></span><button class="orca-button orca-button--link" type="button">Clear all</button><span class="orca-small orca-muted" role="status">14 videos</span></div>
</div>""")],
    guide=["Filter bar"], source="Tangerine",
))

add(Pattern(
    "panel", "Panel", C,
    "A bordered section of a page with a header, a body and optional footer actions.",
    why="A panel answers one question in a clear region (Practical UI L01); its header names the question and holds the actions that affect it (L14).",
    when=["Dashboards, detail pages and settings: any self-contained block of content."],
    how=["`<section class=\"orca-panel\" aria-labelledby=…>` with a panel header, `.orca-panel__body` (`--flush` for tables and lists), and `.orca-panel__foot` for actions.",
         "Lay several panels out in `.orca-panels` (a responsive grid)."],
    classes=[".orca-panel", ".orca-panel__body", ".orca-panel__body--flush", ".orca-panel__foot", ".orca-panels"],
    laws=["L01", "L14", "miller"],
    uses=["panel-header"],
    examples=[("Two panels", """<div class="orca-panels">
  <section class="orca-panel" aria-labelledby="pn-1"><div class="orca-panel-header"><div class="orca-panel-header__text"><h2 class="orca-panel-title" id="pn-1">People inside</h2><p class="orca-panel-header__desc">All entrances</p></div></div>
    <div class="orca-panel__body"><p class="orca-stat-value orca-stat-value--lg">1,204</p><progress class="orca-progress" value="1204" max="1500" aria-label="1,204 of 1,500 capacity"></progress></div></section>
  <section class="orca-panel" aria-labelledby="pn-2"><div class="orca-panel-header"><div class="orca-panel-header__text"><h2 class="orca-panel-title" id="pn-2">Notes</h2></div></div>
    <div class="orca-panel__body"><p class="orca-p">Gate 1 is closed after 18:00.</p></div><div class="orca-panel__foot"><button class="orca-button orca-button--dense" type="button">Edit notes</button></div></section>
</div>""")],
    guide=["Panel"], source="Tangerine",
))

add(Pattern(
    "tabbed-panel-set", "Tabbed panel set", C,
    "One panel whose body switches between related views with tabs.",
    why="Related views of the same data share one frame instead of stacking (Miller's law), and the tabs show what else is available (Practical UI S06).",
    when=["Today / This week / This month of the same metric; Chart / Table of the same data."],
    how=["`.orca-panel` containing a panel header and an `.orca-tabs` with in-page tabs; each tab panel holds one view.",
         "Keep the same height across tabs to avoid jumps; remember the last tab per person when useful."],
    classes=[".orca-panel", ".orca-tabs"],
    laws=["miller", "S06", "doherty"],
    uses=["panel", "tab-bar"],
    examples=[("Chart or table", """<section class="orca-panel" aria-labelledby="tps-t"><div class="orca-panel-header"><div class="orca-panel-header__text"><h2 class="orca-panel-title" id="tps-t">Visitors this week</h2></div></div>
  <div class="orca-tabs"><div class="orca-tabs__list" role="tablist" aria-label="View" data-orca-tabs><button class="orca-tab" role="tab" type="button" id="tps-a" aria-controls="tps-pa" aria-selected="true">Chart</button><button class="orca-tab" role="tab" type="button" id="tps-b" aria-controls="tps-pb" aria-selected="false">Summary</button></div>
    <div class="orca-tabs__panel" role="tabpanel" id="tps-pa" aria-labelledby="tps-a">{% orca_chart "bar" sample.visitors_week %}</div>
    <div class="orca-tabs__panel" role="tabpanel" id="tps-pb" aria-labelledby="tps-b" hidden><dl class="orca-kv"><div><dt>Busiest day</dt><dd>Saturday, 9,530</dd></div><div><dt>Total</dt><dd>49,920</dd></div></dl></div></div>
</section>""")],
    guide=["Tabbed panel set"], source="Tangerine",
))

add(Pattern(
    "card-list", "Card list", C,
    "Records as a vertical list of cards: name, key facts and actions; the phone-friendly alternative to a table.",
    why="On narrow screens a table loses columns; cards keep every record readable and its whole area tappable (Fitts's law, Postel's law).",
    when=["Phones; lists people browse more than compare; records with long names."],
    how=["`<ul class=\"orca-card-list\">` of `<li class=\"orca-record-card\">`: a leading visual, `.orca-record-card__title` with the link (it covers the card), `.orca-record-card__meta` and `.orca-record-card__end` actions.",
         "Offer it as the 'Cards' side of the view toggle, or use `orca-table--cards` to switch automatically."],
    classes=[".orca-card-list", ".orca-record-card", ".orca-record-card__title", ".orca-record-card__meta", ".orca-record-card__end"],
    laws=["fitts", "postel", "miller"],
    uses=["status-dot", "linked-card", "icon-button"],
    examples=[("Record cards", """<ul class="orca-card-list" style="max-width: 32rem">{% for c in sample.videos|slice:":3" %}<li class="orca-record-card"><span class="orca-dot orca-dot--{{ c.status }}" aria-hidden="true"></span><h3 class="orca-record-card__title"><a href="#">{{ c.name }}</a></h3>
  <div class="orca-record-card__end"><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="More actions for {{ c.name }}">{% icon "more" %}</button></div>
  <p class="orca-record-card__meta"><span>{{ c.status_text }}</span><span>{{ c.site }}</span><span class="orca-num">{{ c.today }} today</span></p></li>{% endfor %}</ul>""")],
    guide=["Card list (record cards)"], source="Tangerine",
))

add(Pattern(
    "list-header", "List header", C,
    "Above a list: its title with the count, a search, the view toggle and, for a list panel inside a page, its create action.",
    why="Everything that changes the list sits together above it in a predictable order (Jakob's law, Practical UI L14); the count confirms what the search did.",
    when=["The top of every list page or list panel."],
    how=["`<div class=\"orca-list-header\">` with `h2.orca-list-header__title` + `.orca-list-header__count`, then `.orca-list-header__tools` (search field, view toggle, create button).",
         "The page's Filters button is not here: it goes in the page actions and opens the filter drawer.",
         "On phones the tools take the full width under the title."],
    classes=[".orca-list-header", ".orca-list-header__title", ".orca-list-header__count", ".orca-list-header__tools"],
    laws=["jakob", "L14", "doherty"],
    uses=["search-field", "view-toggle", "create-button"],
    examples=[("List header", """<div class="orca-list-header"><h2 class="orca-list-header__title">Videos <span class="orca-list-header__count">12</span></h2>
  <div class="orca-list-header__tools"><div class="orca-search">{% icon "search" %}<input class="orca-input orca-input--dense" type="search" placeholder=" " aria-label="Search videos"><button class="orca-search__clear" type="button" aria-label="Clear search" data-orca-clear>{% icon "close" %}</button></div>
    <nav class="orca-segmented orca-segmented--dense orca-segmented--icons" aria-label="View"><a class="orca-segmented__item" href="#" aria-current="page" aria-label="Cards">{% icon "grid" %}</a><a class="orca-segmented__item" href="#" aria-label="Table">{% icon "list" %}</a></nav>
    <a class="orca-button orca-button--primary orca-button--dense orca-create orca-create--static" href="#">{% icon "plus" %}Add video</a></div></div>""")],
    guide=["List header (search + filter + create)"], source="Tangerine",
))

add(Pattern(
    "summary-tiles", "Summary tiles", C,
    "A row of small counts by status that also act as quick filters.",
    why="Counts by state answer 'how many need attention?' immediately (Miller's law) and clicking one filters the list to it, a one-step path (Fitts's law, Tesler's law).",
    when=["Above lists with a few meaningful states: online/offline, open/closed, by severity."],
    how=["`<ul class=\"orca-summary-tiles\">` of links or toggle buttons `.orca-summary-tile` with `__value` and `__label` (status dot + word); the active one `aria-current=\"true\"`.",
         "Include 'All' as the first tile."],
    classes=[".orca-summary-tiles", ".orca-summary-tile", ".orca-summary-tile__value", ".orca-summary-tile__label"],
    laws=["miller", "fitts", "tesler"],
    uses=["stat-value", "status-dot"],
    examples=[("Tiles", """<ul class="orca-summary-tiles">
  <li><a class="orca-summary-tile" href="#" aria-current="true"><span class="orca-summary-tile__value">12</span><span class="orca-summary-tile__label">All videos</span></a></li>
  <li><a class="orca-summary-tile" href="#"><span class="orca-summary-tile__value">10</span><span class="orca-summary-tile__label"><span class="orca-dot orca-dot--positive"></span>Online</span></a></li>
  <li><a class="orca-summary-tile" href="#"><span class="orca-summary-tile__value">1</span><span class="orca-summary-tile__label"><span class="orca-dot orca-dot--caution"></span>Degraded</span></a></li>
  <li><a class="orca-summary-tile" href="#"><span class="orca-summary-tile__value">1</span><span class="orca-summary-tile__label"><span class="orca-dot orca-dot--negative"></span>Offline</span></a></li>
</ul>""")],
    guide=["Summary tiles"], source="Tangerine",
))

add(Pattern(
    "autocomplete-results-table", "Autocomplete results table", C,
    "Search-as-you-type results shown as a compact table with the matched text highlighted.",
    why="When results have several attributes, a table under the search compares them at a glance (Miller's law); highlighting shows why each result matched (Practical UI R12).",
    when=["Searching records by name or code where people must tell similar results apart (two 'Entrance A' on different sites)."],
    how=["A search field whose results (htmx, `hx-trigger=\"input changed delay:300ms\"`) replace a `table.orca-table.orca-table--compact.orca-results-table`; matches wrapped in `<mark>`.",
         "At most 10 rows, then 'Show all 37 results'. Announce the count in a status element."],
    classes=[".orca-results-table"],
    laws=["miller", "R12", "doherty"],
    uses=["search-field", "table-card"],
    examples=[("Results", """<div class="orca-search-field" style="max-width: 32rem"><div class="orca-search">{% icon "search" %}<input class="orca-input" type="search" value="entr" aria-label="Search videos" aria-describedby="art-count"></div><p class="orca-search-field__count" id="art-count" role="status">2 results</p></div>
<div class="orca-table-wrap" style="max-width: 32rem"><table class="orca-table orca-table--compact orca-results-table"><thead><tr><th scope="col">Video</th><th scope="col">Site</th><th scope="col">Status</th></tr></thead>
  <tbody><tr><td><a class="orca-link orca-link--plain" href="#"><mark>Entr</mark>ance A</a></td><td>North building</td><td>Online</td></tr><tr><td><a class="orca-link orca-link--plain" href="#"><mark>Entr</mark>ance B</a></td><td>North building</td><td>Online</td></tr></tbody></table></div>""")],
    guide=["Autocomplete results table"],
))
