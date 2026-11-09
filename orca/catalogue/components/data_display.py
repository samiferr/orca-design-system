from ..registry import add, category
from . import Component

C = category(
    "data-display", "Data display",
    "Ways to present records and numbers: stat cards, lists, key/value lists, cards, tables, timelines and small charts.",
    level="component",
)

add(Component(
    "stat-card", "Stat card", C,
    "One measured value with its label, change and context, optionally with a sparkline.",
    why="A KPI is read in a second when the number dominates and its label and comparison sit right next to it (Von Restorff, Miller's law).",
    when=["Dashboards and summary rows: counts, rates, durations."],
    avoid=["More than about six cards in a row competing for attention: group them or pick the important ones."],
    how=["`<div class=\"orca-stat-card\">` with `orca-stat-label`, `orca-stat-value`, then `.orca-stat-card__foot` with a delta and the comparison period; optional `{% templatetag openblock %} orca_sparkline values {% templatetag closeblock %}`.",
         "Make the whole card a link (`<a class=\"orca-stat-card\">`) when it leads to the detail."],
    classes=[".orca-stat-card", ".orca-stat-card__foot"],
    laws=["restorff", "miller", "W11"],
    uses=["stat-label", "stat-value", "delta", "sparkline"],
    examples=[("Stat cards", """<div class="orca-card-grid" style="grid-template-columns: repeat(auto-fill, minmax(13rem, 1fr))">
  <div class="orca-stat-card"><p class="orca-stat-label">Visitors today</p><p class="orca-stat-value">12,480</p><div class="orca-stat-card__foot"><span class="orca-delta orca-delta--up">{% icon "arrow-up" size="xs" %}+8%</span>vs last Friday</div>{% orca_sparkline "820,940,1200,1100,1480,1620,1540" "Visitors per hour today, rising" %}</div>
  <a class="orca-stat-card" href="#"><p class="orca-stat-label">Inside now</p><p class="orca-stat-value">1,204</p><div class="orca-stat-card__foot">of 1,500 capacity</div></a>
  <div class="orca-stat-card"><p class="orca-stat-label">Average visit</p><p class="orca-stat-value">23 min</p><div class="orca-stat-card__foot"><span class="orca-delta orca-delta--flat">{% icon "minus" size="xs" %}0%</span>vs last week</div></div>
</div>""")],
    guide=["Stat card"], source="Tangerine",
))

add(Component(
    "key-value-list", "Key/value list", C,
    "Properties of a record as label and value pairs.",
    why="Aligned labels and values are scanned down one edge and compared quickly (Practical UI L12, Miller's law).",
    when=["Detail pages and side panels: a camera's address, model, location."],
    how=["`<dl class=\"orca-kv\">` with `<div><dt>Label</dt><dd>Value</dd></div>` pairs; `--stacked` puts labels above values (narrow panels). Below 620px it stacks automatically.",
         "Empty values: write 'Not set' in muted text; never leave a blank."],
    classes=[".orca-kv", ".orca-kv--stacked"],
    laws=["L12", "miller", "L15"],
    uses=["muted-text"],
    examples=[("Camera properties", """<dl class="orca-kv" style="max-width: 30rem">
  <div><dt>Model</dt><dd>Hikvision DS-2CD2143G2</dd></div>
  <div><dt>Address</dt><dd><code class="orca-code">192.168.1.40:554</code></dd></div>
  <div><dt>Site</dt><dd>North building</dd></div>
  <div><dt>Notes</dt><dd class="orca-muted">Not set</dd></div>
</dl>""")],
    guide=["Key/value list"],
))

add(Component(
    "list", "List", C,
    "A divided list of items with optional visual, text and end detail.",
    why="A vertical list with consistent rows is the quickest structure to scan (Miller's law); hairline dividers separate items without boxes (Practical UI L01).",
    when=["Short collections in panels: recent events, members, files."],
    avoid=["Comparing several attributes: use a table."],
    how=["`<ul class=\"orca-list\">` of `<li>` each containing one list item.",
         "Make the item itself the link or button (`a.orca-list-item`) so the whole row is the target."],
    classes=[".orca-list"],
    laws=["miller", "L01", "fitts"],
    uses=["list-item"],
    examples=[("Members", """<ul class="orca-list" style="max-width: 26rem">
  <li><a class="orca-list-item" href="#"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span class="orca-list-item__text"><span class="orca-list-item__title">Ada Lovelace</span><span class="orca-list-item__desc">Administrator</span></span><span class="orca-list-item__end">Active today</span></a></li>
  <li><a class="orca-list-item" href="#"><span class="orca-avatar orca-avatar--s" aria-hidden="true">GH</span><span class="orca-list-item__text"><span class="orca-list-item__title">Grace Hopper</span><span class="orca-list-item__desc">Operator</span></span><span class="orca-list-item__end">3 days ago</span></a></li>
</ul>""")],
    guide=["List"], source="Tangerine",
))

add(Component(
    "list-item", "List item", C,
    "One row of a list: leading visual, title and description, trailing detail; static, link, button or selected.",
    why="Fixed slots mean every row reads the same way (Practical UI F09); a 48px row with the whole width clickable is easy to hit (Fitts's law).",
    when=["Inside a list; inside menus of rich options."],
    how=["`.orca-list-item` (a `span`, `a` or `button`) with an optional avatar, thumbnail or icon, `.orca-list-item__text` (`__title`, `__desc`) and `.orca-list-item__end`.",
         "Selected: `aria-current=\"true\"` (navigation) or `aria-selected=\"true\"` (selection lists)."],
    classes=[".orca-list-item", ".orca-list-item__text", ".orca-list-item__title", ".orca-list-item__desc", ".orca-list-item__end", ".orca-list-item--selected"],
    laws=["F09", "fitts"],
    uses=["avatar", "thumbnail", "icon"],
    examples=[("Variants", """<ul class="orca-list" style="max-width: 26rem">
  <li><span class="orca-list-item">{% icon "file" size="m" %}<span class="orca-list-item__text"><span class="orca-list-item__title">weekly-report.csv</span><span class="orca-list-item__desc">48 KB</span></span></span></li>
  <li><button class="orca-list-item" type="button" aria-current="true">{% icon "snapshot" size="m" %}<span class="orca-list-item__text"><span class="orca-list-item__title">Entrance A</span><span class="orca-list-item__desc">Selected</span></span>{% icon "check" %}</button></li>
</ul>""")],
    guide=["List item"], source="Tangerine",
))

add(Component(
    "timeline-item", "Timeline item", C,
    "One event in a vertical timeline: status dot, title, time and description.",
    why="A line joining dots shows sequence at a glance (Gestalt continuity, Practical UI L01); the dot's tone shows what kind of event it was.",
    when=["History of a record, a run's steps, an incident log."],
    how=["`<ol class=\"orca-timeline\">` of `<li class=\"orca-timeline__item\">` with a dot, then a body containing `.orca-timeline__head` (`__title` + `__time`) and `.orca-timeline__desc`.",
         "Newest first for logs; oldest first for processes. Always give a time."],
    classes=[".orca-timeline", ".orca-timeline__item", ".orca-timeline__head", ".orca-timeline__title", ".orca-timeline__time", ".orca-timeline__desc"],
    laws=["L01", "C03"],
    uses=["status-dot", "time-label"],
    examples=[("Run history", """<ol class="orca-timeline" style="max-width: 28rem">
  <li class="orca-timeline__item"><span class="orca-dot orca-dot--positive"></span><div><div class="orca-timeline__head"><span class="orca-timeline__title">Run finished</span><time class="orca-timeline__time" datetime="2026-11-06T09:12">09:12</time></div><p class="orca-timeline__desc">118 of 120 shots taken.</p></div></li>
  <li class="orca-timeline__item"><span class="orca-dot orca-dot--caution"></span><div><div class="orca-timeline__head"><span class="orca-timeline__title">2 shots failed</span><time class="orca-timeline__time" datetime="2026-11-06T08:40">08:40</time></div><p class="orca-timeline__desc">Loading dock did not answer.</p></div></li>
  <li class="orca-timeline__item"><span class="orca-dot"></span><div><div class="orca-timeline__head"><span class="orca-timeline__title">Run started</span><time class="orca-timeline__time" datetime="2026-11-06T08:00">08:00</time></div></div></li>
</ol>""")],
    guide=["Timeline item"], source="Tangerine",
))

add(Component(
    "sortable-header", "Sortable column header", C,
    "A table header that sorts the column, showing the direction with an arrow and aria-sort.",
    why="Sorting turns a table into an answer ('which camera counted most?') (Tesler's law); the arrow and aria-sort show the order to everyone (C03).",
    when=["Columns people compare: names, counts, dates, status."],
    how=["`<th scope=\"col\" aria-sort=\"descending\"><a class=\"orca-sort\" href=\"?sort=-count\">Count{% templatetag openblock %} icon \"arrow-up\" {% templatetag closeblock %}</a></th>`; columns not sorted have no aria-sort.",
         "Server-side: keep the other query parameters in the link; first click sorts the most useful way (descending for numbers and dates)."],
    classes=[".orca-sort"],
    laws=["tesler", "C03"],
    uses=["icon"],
    examples=[("Header row", """<table class="orca-table" style="max-width: 32rem"><thead><tr>
  <th scope="col" aria-sort="ascending"><a class="orca-sort" href="#">Camera{% icon "arrow-up" %}</a></th>
  <th scope="col" class="is-num" aria-sort="none"><a class="orca-sort" href="#">Count{% icon "arrow-up" %}</a></th>
  <th scope="col"><a class="orca-sort" href="#">Last seen{% icon "arrow-up" %}</a></th>
</tr></thead><tbody><tr><td>Entrance A</td><td class="is-num">1,204</td><td>2 min ago</td></tr><tr><td>Entrance B</td><td class="is-num">980</td><td>5 min ago</td></tr></tbody></table>""")],
    guide=["Sortable column header"], source="Tangerine",
))

add(Component(
    "legend-item", "Legend item", C,
    "A swatch, a series name and optionally its value, keying a chart.",
    why="Every colour on a chart needs a name next to the same colour, or colour-blind readers lose the chart (Practical UI C03).",
    when=["Below or beside every multi-series chart and map."],
    how=["`<ul class=\"orca-legend\">` of `<li class=\"orca-legend__item\">` with a swatch (or line swatch, or chart dot shape), the name and `.orca-legend__value`.",
         "`--column` for a vertical legend with values aligned right."],
    classes=[".orca-legend", ".orca-legend__item", ".orca-legend__value", ".orca-legend--column"],
    laws=["C03", "miller"],
    uses=["swatch", "chart-dot"],
    examples=[("Legend", """<ul class="orca-legend orca-legend--column" style="max-width: 16rem">
  <li class="orca-legend__item"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-1)"></span>Entrance A<span class="orca-legend__value">1,204</span></li>
  <li class="orca-legend__item"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-2)"></span>Entrance B<span class="orca-legend__value">980</span></li>
  <li class="orca-legend__item"><span class="orca-swatch orca-swatch--line" style="--orca-swatch: var(--orca-chart-3)"></span>Target<span class="orca-legend__value">1,000</span></li>
</ul>""")],
    guide=["Legend item"],
))

add(Component(
    "zone-row", "Zone row", C,
    "A counting zone in a list: its swatch, name, type, count and actions.",
    why="The same swatch as on the video lets people match a zone to its row instantly (Miller's law); the type is a word, not only a pattern (C03).",
    when=["Zone lists beside the zone editor and on camera pages."],
    how=["`<div class=\"orca-zone-row\">` with a zone swatch, `.orca-zone-row__name` (name + type badge), `.orca-zone-row__count` and row actions."],
    classes=[".orca-zone-row", ".orca-zone-row__name", ".orca-zone-row__count"],
    laws=["miller", "C03"],
    uses=["zone-swatch", "badge", "row-actions"],
    examples=[("Zones", """<div style="max-width: 30rem">
  <div class="orca-zone-row"><span class="orca-zone-swatch" style="--orca-zone: var(--orca-teal-500)"></span><span class="orca-zone-row__name">Door line <span class="orca-badge orca-badge--grey">Count</span></span><span class="orca-zone-row__count orca-num">1,204</span><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="Edit Door line">{% icon "edit" %}</button></div>
  <div class="orca-zone-row"><span class="orca-zone-swatch orca-zone-swatch--exclude" style="--orca-zone: var(--orca-orange-500)"></span><span class="orca-zone-row__name">Staff area <span class="orca-badge orca-badge--grey">Excluded</span></span><span class="orca-zone-row__count orca-muted">–</span><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="Edit Staff area">{% icon "edit" %}</button></div>
</div>""")],
    guide=["Zone row"],
))

add(Component(
    "line-count-item", "Line-count item", C,
    "A counting line with people in and out, each with a direction arrow.",
    why="In and out are the two numbers people compare; arrows and words make the direction clear without colour (C03), and tabular digits keep them aligned.",
    when=["Line-crossing counts on camera and run pages."],
    how=["`<div class=\"orca-line-count\">` with a swatch, `.orca-line-count__name`, and two `.orca-line-count__dir` spans ('↓ 612 in', '↑ 598 out') using arrow icons and hidden words."],
    classes=[".orca-line-count", ".orca-line-count__name", ".orca-line-count__dir"],
    laws=["C03", "W11"],
    uses=["swatch", "icon", "tabular-number"],
    examples=[("Lines", """<div style="max-width: 30rem">
  <div class="orca-line-count"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-1)"></span><span class="orca-line-count__name">Main door</span><span class="orca-line-count__dir">{% icon "arrow-down" %}612<span class="orca-sr-only"> in</span></span><span class="orca-line-count__dir">{% icon "arrow-up" %}598<span class="orca-sr-only"> out</span></span></div>
  <div class="orca-line-count"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-2)"></span><span class="orca-line-count__name">Side door</span><span class="orca-line-count__dir">{% icon "arrow-down" %}88<span class="orca-sr-only"> in</span></span><span class="orca-line-count__dir">{% icon "arrow-up" %}91<span class="orca-sr-only"> out</span></span></div>
</div>""")],
    guide=["Line-count item"],
))

add(Component(
    "media-object", "Media object", C,
    "An image or avatar beside a block of text.",
    why="Pairing a picture with its text binds them by proximity (Practical UI L01) and lets the eye recognise the item before reading.",
    when=["Comments, notifications, search results, people and product summaries."],
    how=["`<div class=\"orca-media\">` with the media (thumbnail, avatar, icon) and `.orca-media__body`; `--center` aligns them vertically.",
         "The media is decorative (`alt=\"\"`) when the body names the thing."],
    classes=[".orca-media", ".orca-media__body", ".orca-media--center"],
    laws=["L01", "miller"],
    uses=["thumbnail", "avatar"],
    examples=[("Media object", """<div class="orca-media" style="max-width: 28rem"><img class="orca-thumb" src="{% static "orca/img/sample-street.svg" %}" alt="" width="48" height="48"><div class="orca-media__body"><span class="orca-card-title">Entrance A</span><span class="orca-small orca-muted">2 people at the door · 08:14</span></div></div>""")],
    guide=["Media object"],
))

add(Component(
    "card", "Card", C,
    "A container for one object: optional media, body and footer. Outlined (default), elevated or filled.",
    why="A card groups everything about one object in a common region (Practical UI L01) so grids of objects can be scanned and compared.",
    when=["Collections of objects people browse: cameras, sites, reports.", "Outlined in content; elevated over maps or media; filled inside panels."],
    avoid=["Wrapping every section of a page in a card: use spacing and section titles."],
    how=["`<article class=\"orca-card\">` with `.orca-card__media` (image in a reserved 16:9 box), `.orca-card__body` (kicker, title, meta, text) and `.orca-card__footer`.",
         "Variants: `--elevated`, `--filled`. Lay cards out in `.orca-card-grid`."],
    classes=[".orca-card", ".orca-card--elevated", ".orca-card--filled", ".orca-card__media", ".orca-card__body", ".orca-card-grid"],
    laws=["L01", "C12"],
    uses=["card-kicker", "card-title", "card-meta"],
    examples=[("Three variants", """<ul class="orca-card-grid">
  <li><article class="orca-card"><div class="orca-card__body"><p class="orca-card-kicker">Outlined</p><h3 class="orca-card-title">North building</h3><p class="orca-card-meta">12 cameras · 5 zones</p></div></article></li>
  <li><article class="orca-card orca-card--elevated"><div class="orca-card__body"><p class="orca-card-kicker">Elevated</p><h3 class="orca-card-title">Warehouse</h3><p class="orca-card-meta">4 cameras · 2 zones</p></div></article></li>
  <li><article class="orca-card orca-card--filled"><div class="orca-card__body"><p class="orca-card-kicker">Filled</p><h3 class="orca-card-title">Car park</h3><p class="orca-card-meta">2 cameras</p></div></article></li>
</ul>""")],
    guide=["Card", "Card (outlined, elevated, filled)"], source="Tangerine",
    related=["card-footer", "linked-card"],
))

add(Component(
    "card-footer", "Card footer", C,
    "The bottom strip of a card for status and actions.",
    why="Keeping actions in the same place on every card makes them predictable (Practical UI F09) and separates reading from acting.",
    when=["Cards with a status or one or two actions."],
    how=["`<div class=\"orca-card__footer\">` with a status on the left and `.orca-card__footer-end` holding icon buttons or a small button.",
         "Footer controls stay clickable inside a linked card (they sit above the stretched link)."],
    classes=[".orca-card__footer", ".orca-card__footer-end"],
    laws=["F09", "L14"],
    uses=["status-dot", "icon-button"],
    examples=[("Footer", """<article class="orca-card" style="max-width: 18rem"><div class="orca-card__body"><h3 class="orca-card-title">Entrance A</h3><p class="orca-card-meta">North building</p></div>
  <div class="orca-card__footer"><span class="orca-status orca-small"><span class="orca-dot orca-dot--positive"></span>Online</span><span class="orca-card__footer-end"><button class="orca-icon-button orca-icon-button--sm orca-pin" type="button" aria-pressed="false" aria-label="Pin Entrance A" data-orca-toggle>{% icon "pin" %}</button><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="More actions for Entrance A">{% icon "more" %}</button></span></div></article>""")],
    guide=["Card footer"],
))

add(Component(
    "linked-card", "Linked card", C,
    "A card whose whole area opens the object, built with one real link on the title.",
    why="The whole card is a large target (Fitts's law) while screen readers hear one clear link, the title, instead of a card full of link text.",
    when=["Cards whose main action is opening the object."],
    how=["Add `--link` to the card and put `<a class=\"orca-card__link\" href=…>` around the title text; its `::after` covers the card.",
         "Other controls inside go in the footer, which sits above the link. Never nest links."],
    classes=[".orca-card--link", ".orca-card__link"],
    laws=["fitts", "W14"],
    uses=["card"],
    examples=[("Linked cards", """<ul class="orca-card-grid">
  <li><article class="orca-card orca-card--link"><div class="orca-card__media"><img src="{% static "orca/img/sample-street.svg" %}" alt=""></div><div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">Entrance A</a></h3><p class="orca-card-meta">North building · online</p></div></article></li>
  <li><article class="orca-card orca-card--link"><div class="orca-card__media"><img src="{% static "orca/img/sample-floor.svg" %}" alt=""></div><div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">North building plan</a></h3><p class="orca-card-meta">Updated 3 March</p></div></article></li>
</ul>""")],
    guide=["Linked card"],
))

add(Component(
    "accordion", "Accordion", C,
    "A stack of sections that open and close, built on details and summary.",
    why="Collapsing secondary content lets people see the whole list of topics first and open only what they need (Practical UI S04, Miller's law).",
    when=["FAQs, advanced settings, long lists of grouped details."],
    avoid=["Content most people need: show it.", "Steps of a process: use steps."],
    how=["`<div class=\"orca-accordion\">` of `<details>` with `<summary>` (chevron + heading text) and `.orca-accordion__panel`.",
         "Write summaries as the question or topic people look for. Several sections may be open at once."],
    classes=[".orca-accordion", ".orca-accordion__panel"],
    laws=["S04", "miller", "jakob"],
    uses=["chevron"],
    examples=[("Accordion", """<div class="orca-accordion" style="max-width: 32rem">
  <details open><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>How often are counts updated?</summary><div class="orca-accordion__panel"><p class="orca-p">Every minute. Reports group older data by hour.</p></div></details>
  <details><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>Can I export the data?</summary><div class="orca-accordion__panel"><p class="orca-p">Yes, as CSV from any report.</p></div></details>
</div>""")],
    guide=["Accordion"], source="Tangerine",
))

add(Component(
    "steps", "Steps", C,
    "The steps of a process with done, current and upcoming markers.",
    why="Showing progress through a multi-step task motivates finishing and sets expectations (Peak–end rule, goal gradient); splitting a task into steps lowers each decision (Hick's law).",
    when=["Setup flows and multi-step forms of 3 to 6 steps."],
    how=["`<ol class=\"orca-steps\">` of `.orca-steps__item` (`--done` or `aria-current=\"step\"`) each with a step marker and `.orca-steps__title` (+ `__desc`).",
         "Done steps may link back for review. `--vertical` for side panels; on phones descriptions hide."],
    classes=[".orca-steps", ".orca-steps__item", ".orca-steps__item--done", ".orca-steps__title", ".orca-steps__desc", ".orca-steps--vertical"],
    laws=["peak-end", "hick", "R16"],
    uses=["step-marker"],
    examples=[("Setup steps", """<ol class="orca-steps">
  <li class="orca-steps__item orca-steps__item--done"><span class="orca-step-marker orca-step-marker--done" aria-hidden="true"></span><span class="orca-steps__title"><a href="#">Connect recorder</a><span class="orca-sr-only">, done</span></span></li>
  <li class="orca-steps__item" aria-current="step"><span class="orca-step-marker orca-step-marker--current" aria-hidden="true"></span><span class="orca-steps__title">Choose cameras</span><span class="orca-steps__desc">Pick the doors to count</span></li>
  <li class="orca-steps__item"><span class="orca-step-marker" aria-hidden="true"></span><span class="orca-steps__title">Draw zones</span></li>
</ol>""")],
    guide=["Steps"], source="Tangerine",
))

add(Component(
    "tree", "Tree", C,
    "A hierarchy of items that expand and collapse: sites, buildings, cameras.",
    why="Nested disclosure shows structure and hides depth until needed (Practical UI S04); indentation and a guide line show who belongs to whom (Gestalt).",
    when=["Browsing a hierarchy of objects, such as locations or folders."],
    avoid=["Navigation between pages: use the nav tree."],
    how=["`<ul class=\"orca-tree\">` with `<li><details><summary>` for branches and `.orca-tree__leaf` for leaves; `.orca-tree__meta` for counts.",
         "Built on details, so it works with the keyboard and screen readers without script; current leaf `aria-current=\"true\"`."],
    classes=[".orca-tree", ".orca-tree__leaf", ".orca-tree__meta"],
    laws=["S04", "miller"],
    uses=["chevron"],
    examples=[("Sites", """<ul class="orca-tree" style="max-width: 20rem">
  <li><details open><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>North building<span class="orca-tree__meta">3</span></summary>
    <ul><li><a class="orca-tree__leaf" href="#" aria-current="true">Entrance A</a></li><li><a class="orca-tree__leaf" href="#">Entrance B</a></li>
      <li><details><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>Basement<span class="orca-tree__meta">1</span></summary><ul><li><a class="orca-tree__leaf" href="#">Loading dock</a></li></ul></details></li></ul></details></li>
  <li><details><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>Warehouse<span class="orca-tree__meta">4</span></summary><ul><li><a class="orca-tree__leaf" href="#">Gate 1</a></li></ul></details></li>
</ul>""")],
    guide=["Tree"], source="Tangerine",
))

add(Component(
    "avatar-group", "Avatar group", C,
    "Overlapping avatars of the people involved, with '+N' for the rest.",
    why="A few faces show who is involved at a glance without listing everyone (Miller's law); the count tells how many more there are.",
    when=["Assignees, attendees, members on cards and headers."],
    how=["`<ul class=\"orca-avatar-group\" aria-label=\"5 members\">` of `<li>` avatars (each with the person's name as `title`/`aria-label`), ending with `.orca-avatar-group__more` '+2'.",
         "Show at most 3 to 5; link the group to the full list."],
    classes=[".orca-avatar-group", ".orca-avatar-group__more"],
    laws=["miller"],
    uses=["avatar"],
    examples=[("Members", """<ul class="orca-avatar-group" aria-label="5 members: Ada Lovelace, Grace Hopper, Alan Turing and 2 more">
  <li><span class="orca-avatar orca-avatar--s" title="Ada Lovelace">AL</span></li><li><span class="orca-avatar orca-avatar--s" title="Grace Hopper">GH</span></li><li><span class="orca-avatar orca-avatar--s" title="Alan Turing">AT</span></li><li><span class="orca-avatar orca-avatar--s orca-avatar-group__more">+2</span></li>
</ul>""")],
    guide=["Avatar group"], source="Tangerine",
))

add(Component(
    "table-card", "Table card", C,
    "A panel holding a titled table and its pager.",
    why="A titled frame tells people what the rows are before they read them, and keeps the table's actions and paging next to it (Practical UI L01, L14).",
    when=["Tables on dashboards and detail pages."],
    how=["`<section class=\"orca-table-card\">` with a panel header (title, description, actions), `.orca-table-wrap` > `table.orca-table`, then a table pager.",
         "Numbers right-aligned with `.is-num`; `--compact` table for dense data. Empty: a no-data state in one full-width cell."],
    classes=[".orca-table-card", ".orca-table", ".orca-table-wrap", ".orca-table--compact"],
    laws=["L01", "L14", "W11"],
    uses=["panel-header", "table-pager", "sortable-header"],
    examples=[("Table card", """<section class="orca-table-card" aria-labelledby="tc-t">
  <div class="orca-panel-header"><div class="orca-panel-header__text"><h2 class="orca-panel-title" id="tc-t">Busiest entrances</h2><p class="orca-panel-header__desc">Today, all sites</p></div><div class="orca-panel-header__actions"><a class="orca-button orca-button--ghost orca-button--dense" href="#">View report</a></div></div>
  <div class="orca-table-wrap"><table class="orca-table"><thead><tr><th scope="col">Entrance</th><th scope="col">Site</th><th scope="col" class="is-num">Visitors</th></tr></thead>
    <tbody><tr><td>Entrance A</td><td>North building</td><td class="is-num">4,812</td></tr><tr><td>Gate 1</td><td>Warehouse</td><td class="is-num">2,140</td></tr><tr><td>Entrance B</td><td>North building</td><td class="is-num">1,980</td></tr></tbody></table></div>
  <div class="orca-table-pager"><span class="orca-num">1–3 of 14</span><span class="orca-table-pager__nav"><button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Previous page" disabled>{% icon "chevron-left" %}</button><button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Next page">{% icon "chevron-right" %}</button></span></div>
</section>""")],
    guide=["Table card"],
))

add(Component(
    "property-row", "Property row", C,
    "One editable key and value pair with a remove button, repeated to edit free-form properties.",
    why="Free-form metadata is inherently variable (Tesler's law); one row per pair with Add and Remove keeps it structured and forgiving (Postel's law).",
    when=["Custom properties, labels, HTTP headers, environment values."],
    how=["`<div class=\"orca-property-rows\" id=…>` of `<div class=\"orca-property-row\" data-orca-row>` (key field, value field, remove icon button `data-orca-remove-row`).",
         "An add-row button with `data-orca-add-row=\"template-id\"` clones a `<template>`; Django formsets: use `__prefix__` in the template and point `data-orca-total` at TOTAL_FORMS.",
         "Name the remove button after the key ('Remove property site-code')."],
    classes=[".orca-property-row", ".orca-property-rows"],
    laws=["tesler", "postel"],
    uses=["text-input", "icon-button", "label"],
    examples=[("Properties", """<div class="orca-property-rows" id="pr-list">
  <div class="orca-property-row" data-orca-row><div><label class="orca-label" for="pr-k0">Key</label><input class="orca-input" id="pr-k0" value="site-code"></div><div><label class="orca-label" for="pr-v0">Value</label><input class="orca-input" id="pr-v0" value="NB-01"></div><button class="orca-icon-button" type="button" aria-label="Remove property site-code" data-orca-remove-row>{% icon "delete" %}</button></div>
</div>
<template id="pr-tpl"><div class="orca-property-row" data-orca-row><div><label class="orca-label" for="pr-k__prefix__">Key</label><input class="orca-input" id="pr-k__prefix__"></div><div><label class="orca-label" for="pr-v__prefix__">Value</label><input class="orca-input" id="pr-v__prefix__"></div><button class="orca-icon-button" type="button" aria-label="Remove property" data-orca-remove-row>{% icon "delete" %}</button></div></template>
<button class="orca-button orca-button--ghost" type="button" data-orca-add-row="pr-tpl" aria-controls="pr-list" style="margin-top: var(--orca-space-8)">{% icon "plus" %}Add property</button>""")],
    guide=["Property row (key, value, remove)"],
))

add(Component(
    "activity-entry", "Activity entry", C,
    "One change in an audit log: what happened, who did it, when, and the before and after values.",
    why="Trust in shared data depends on knowing who changed what (Peak–end rule); showing the old value struck through beside the new one makes the change readable without comparing screens.",
    when=["Activity feeds and history tabs of records."],
    how=["`<div class=\"orca-activity\">` with the actor's avatar, `.orca-activity__head` (action badge, actor, `.orca-activity__time`), and a `<dl class=\"orca-activity__change\">` of field, `<del>` old and `<ins>` new values.",
         "Times are absolute in logs ('6 Nov, 08:14'), relative in feeds."],
    classes=[".orca-activity", ".orca-activity__head", ".orca-activity__time", ".orca-activity__change"],
    laws=["peak-end", "C03"],
    uses=["avatar", "badge", "time-label"],
    examples=[("Change", """<div class="orca-activity" style="max-width: 34rem"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span>
  <div class="orca-activity__head"><span class="orca-badge orca-badge--subtle orca-badge--info">Updated</span><strong>Ada Lovelace</strong> changed Entrance A<time class="orca-activity__time" datetime="2026-11-06T08:14">6 Nov, 08:14</time></div>
  <dl class="orca-activity__change"><dt>Name</dt><dd><del>Front door</del> → <ins>Entrance A</ins></dd><dt>Interval</dt><dd><del>15 min</del> → <ins>5 min</ins></dd></dl></div>""")],
    guide=["Activity entry (badge, actor, time, before and after)"],
))

add(Component(
    "carousel", "Carousel", C,
    "One slide at a time with previous and next buttons, dots and a count.",
    why="When only one image fits, controls and a count ('2 of 5') show there is more and where you are (Practical UI S06); native scroll-snap keeps swiping natural on touch.",
    when=["A few related images: snapshots of an event, product photos."],
    avoid=["Important content people must not miss: list it.", "Auto-advancing slides."],
    how=["`<section class=\"orca-carousel\" data-orca-carousel aria-roledescription=\"carousel\" aria-label=…>` with a `.orca-carousel__track` list of slides and `.orca-carousel__controls` (prev and next icon buttons with `data-orca-prev`/`data-orca-next`, dots with `data-orca-slide=\"i\"`, `.orca-carousel__count`).",
         "Each slide's image has its own alt text; hidden slides get `aria-hidden` from orca.js."],
    classes=[".orca-carousel", ".orca-carousel__track", ".orca-carousel__controls", ".orca-carousel__dots", ".orca-carousel__count"],
    laws=["S06", "jakob"],
    uses=["carousel-dot", "icon-button", "media-frame"],
    examples=[("Event snapshots", """<section class="orca-carousel" data-orca-carousel aria-roledescription="carousel" aria-label="Event snapshots" style="max-width: 24rem">
  <ul class="orca-carousel__track">
    <li><div class="orca-ratio orca-ratio--16x9"><img src="{% static "orca/img/sample-street.svg" %}" alt="08:14, two people at the door"></div></li>
    <li><div class="orca-ratio orca-ratio--16x9"><img src="{% static "orca/img/sample-floor.svg" %}" alt="Floor plan with the door highlighted"></div></li>
    <li><div class="orca-ratio orca-ratio--16x9"><img src="{% static "orca/img/sample-street.svg" %}" alt="08:15, the door is clear"></div></li>
  </ul>
  <div class="orca-carousel__controls">
    <button class="orca-icon-button" type="button" aria-label="Previous image" data-orca-prev>{% icon "chevron-left" %}</button>
    <div class="orca-carousel__dots"><button class="orca-carousel-dot" type="button" aria-label="Image 1" data-orca-slide="0"></button><button class="orca-carousel-dot" type="button" aria-label="Image 2" data-orca-slide="1"></button><button class="orca-carousel-dot" type="button" aria-label="Image 3" data-orca-slide="2"></button></div>
    <button class="orca-icon-button" type="button" aria-label="Next image" data-orca-next>{% icon "chevron-right" %}</button>
    <span class="orca-carousel__count" aria-live="polite">1 of 3</span>
  </div>
</section>""")],
    guide=["Carousel"],
))

add(Component(
    "scroller", "Scroller", C,
    "A horizontal row that scrolls and snaps, showing part of the next item.",
    why="A peeking next item is the clue that more exists (Practical UI S06); snapping stops half-visible items.",
    when=["Rows of cards on phones; quick filters; recent items."],
    how=["`<ul class=\"orca-scroller\" tabindex=\"0\" aria-label=…>` of items (each 80% wide up to 16rem).",
         "The scroller is focusable so keyboard users can scroll it with arrow keys."],
    classes=[".orca-scroller"],
    laws=["S06", "fitts"],
    uses=["card"],
    examples=[("Scroller", """<ul class="orca-scroller" tabindex="0" aria-label="Sites" style="max-width: 30rem; padding-inline: 0">
  <li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">North building</h3><p class="orca-card-meta">12 cameras</p></div></li>
  <li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Warehouse</h3><p class="orca-card-meta">4 cameras</p></div></li>
  <li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Car park</h3><p class="orca-card-meta">2 cameras</p></div></li>
</ul>""")],
    guide=["Scroller (scroll-snap region)"],
))

add(Component(
    "sparkline", "Sparkline", C,
    "A tiny trend line without axes, ending with a dot on the latest value.",
    why="The shape of a trend is understood pre-attentively; a sparkline adds that context to a number without a full chart (Miller's law). The end dot marks 'now'.",
    when=["Beside a stat value or in a table cell."],
    avoid=["When exact values matter: use a chart with axes."],
    how=["`{% templatetag openblock %} orca_sparkline values \"Visitors per hour today, rising\" {% templatetag closeblock %}` from a list or a comma-separated string.",
         "Always pair it with the number it summarises; the label is read by screen readers."],
    classes=[".orca-sparkline"],
    laws=["miller", "C03"],
    uses=["stat-value"],
    examples=[("Sparklines", """<div class="orca-stack" style="max-width: 12rem">{% orca_sparkline "5,8,6,9,12,10,14,13,16" %}{% orca_sparkline "20,18,19,15,12,13,9" "Errors per day, falling" %}</div>""")],
    guide=["Sparkline"],
))

add(Component(
    "donut-chart", "Donut chart", C,
    "A ring of up to about five shares with the total in the middle and a legend with values.",
    why="A part-of-whole split is grasped quickly when there are few parts; the legend gives the exact numbers and names every colour (Practical UI C03).",
    when=["2 to 5 shares of one total: visitors by entrance, alerts by type."],
    avoid=["More than 5 parts or comparing similar shares: use a bar chart."],
    how=["`{% templatetag openblock %} orca_donut segments total_label=\"Visitors\" {% templatetag closeblock %}` with `[(\"Entrance A\", 4812), …]`, dicts, or a string `\"Entrance A:4812, Gate 1:2140\"`.",
         "Series use `--orca-chart-1…8` in order; the SVG's label lists every share in words."],
    classes=[".orca-donut", ".orca-donut__chart", ".orca-donut__total"],
    laws=["C03", "miller"],
    uses=["legend-item", "swatch"],
    examples=[("Visitors by entrance", """{% orca_donut "Entrance A:4812, Gate 1:2140, Entrance B:1980, Car park:640" total_label="Visitors" %}""")],
    guide=["Donut chart"],
))

add(Component(
    "chart-frame", "Chart frame", C,
    "The frame every chart sits in: title, subtitle, legend, a reserved plot area, a source line and the data as a table.",
    why="A chart is only useful with its title, units and source (Practical UI W04); reserving the plot area prevents layout jumps (Doherty), and the data table gives everyone the exact values (Postel's law).",
    when=["Every chart, whatever draws it (SVG, canvas, a charting library)."],
    how=["`<figure class=\"orca-chart-frame\">` with `.orca-chart-frame__head` (title + subtitle with the unit; actions), the legend, `.orca-chart-frame__plot` (set `--orca-ratio`), `<figcaption class=\"orca-chart-frame__caption\">` for source and time zone, and `<details><summary>Show data</summary>` with a table.",
         "Colours from `--orca-chart-*` tokens; text inside charts uses text tokens so both themes work."],
    classes=[".orca-chart-frame", ".orca-chart-frame__head", ".orca-chart-frame__plot", ".orca-chart-frame__caption"],
    laws=["W04", "doherty", "postel", "C03"],
    uses=["legend-item", "no-data-state", "panel-title"],
    examples=[("Frame with a placeholder plot", """<figure class="orca-chart-frame" style="max-width: 36rem">
  <div class="orca-chart-frame__head"><div><h3 class="orca-panel-title">Visitors per hour</h3><p class="orca-small orca-muted">Today, people per hour, all entrances</p></div><button class="orca-button orca-button--ghost orca-button--dense" type="button">Export</button></div>
  <ul class="orca-legend"><li class="orca-legend__item"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-1)"></span>Entrance A</li><li class="orca-legend__item"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-2)"></span>Entrance B</li></ul>
  <div class="orca-chart-frame__plot" style="--orca-ratio: 3 / 1"><div class="orca-no-data" style="height: 100%"><strong>Chart area</strong>Draw the chart here.</div></div>
  <figcaption class="orca-chart-frame__caption">Source: line counts · Europe/Paris · updated 09:14</figcaption>
  <details><summary>Show data</summary><table class="orca-table orca-table--compact"><thead><tr><th scope="col">Hour</th><th scope="col" class="is-num">Entrance A</th><th scope="col" class="is-num">Entrance B</th></tr></thead><tbody><tr><td>08:00</td><td class="is-num">412</td><td class="is-num">380</td></tr></tbody></table></details>
</figure>""")],
    guide=["Chart frame"],
))
