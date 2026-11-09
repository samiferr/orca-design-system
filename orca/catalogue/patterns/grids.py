from ..registry import add, category
from . import Pattern

C = category(
    "grids", "Grids and collections",
    "Repeating one component in a responsive grid or sequence: products, videos, KPIs, a heat map, an event timeline.",
    level="pattern",
)

add(Pattern(
    "product-grid", "Product grid", C,
    "Product items in a responsive grid that adapts the number of columns to the screen.",
    why="A grid of equal tiles lets people compare many products by sight (Miller's law: recognition); responsive columns keep tiles readable on every screen (Postel's law).",
    when=["Catalogues and shop listings."],
    how=["`<ul class=\"orca-product-grid\">` of `<li>` product items; tiles are at least 12rem wide.",
         "Above the grid: the list header with count, sort and filters; below it: pagination."],
    classes=[".orca-product-grid"],
    laws=["miller", "postel"],
    uses=["product-item", "list-header", "pagination"],
    examples=[("Grid", """<ul class="orca-product-grid">{% for n in "1234" %}<li><article class="orca-product"><div class="orca-product__image"><img src="{% static "orca/img/sample-street.svg" %}" alt=""></div><h3 class="orca-product__name"><a href="#">Dome video {{ n }}, 4 MP</a></h3><p class="orca-product__price" style="margin: 0">€1{{ n }}9</p></article></li>{% endfor %}</ul>""")],
    guide=["Product grid"],
))

add(Pattern(
    "video-grid", "Video grid", C,
    "Video cards in a grid, pinned videos first, offline videos clearly marked.",
    why="Operators scan videos by their live view (Miller's law); keeping pinned videos first saves the daily search (Fitts's law) and offline ones stand out by badge and word (Von Restorff, C03).",
    when=["Dashboards and video lists in card view."],
    how=["`<ul class=\"orca-video-grid\">` of video cards; order pinned first, then by name. Each image sits in a reserved 16:9 frame so the grid never jumps.",
         "Pair with the view toggle (cards or table) and a skeleton while snapshots load."],
    classes=[".orca-video-grid"],
    laws=["miller", "fitts", "restorff"],
    uses=["video-card", "view-toggle", "card-skeleton"],
    examples=[("Grid", """<ul class="orca-video-grid">{% for c in sample.videos|slice:":3" %}<li><article class="orca-card orca-card--link orca-video-card">{% if c.status == "negative" %}<div class="orca-ratio orca-ratio--16x9 orca-frame--removed">No image since {{ c.last }}</div><span class="orca-badge orca-badge--negative orca-video-card__flag">Offline</span>{% else %}<div class="orca-ratio orca-ratio--16x9"><img src="{% static "orca/img/sample-street.svg" %}" alt=""></div>{% endif %}
  <div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">{{ c.name }}</a></h3><span class="orca-status orca-small"><span class="orca-dot orca-dot--{{ c.status }}"></span>{{ c.status_text }} · {{ c.site }}</span></div></article></li>{% endfor %}</ul>""")],
    guide=["Video grid"], source="Tangerine",
))

add(Pattern(
    "kpi-grid", "KPI grid", C,
    "A row of stat cards summarising the state of things, linking to the detail behind each.",
    why="A few key numbers at the top answer 'is everything fine?' at a glance (Miller's law); limiting them keeps each one meaningful (Von Restorff).",
    when=["The top of dashboards and report pages."],
    avoid=["More than about six cards: choose the ones people act on."],
    how=["`<div class=\"orca-kpi-grid\">` of stat cards (as links when they lead somewhere), each with its comparison and, where useful, a sparkline."],
    classes=[".orca-kpi-grid"],
    laws=["miller", "restorff"],
    uses=["stat-card"],
    examples=[("KPIs", """<div class="orca-kpi-grid">
  <a class="orca-stat-card" href="#"><div class="orca-stat-card__head"><p class="orca-stat-label">Visitors today</p><span class="orca-stat-card__icon" aria-hidden="true">{% icon "user" %}</span></div><p class="orca-stat-value">12,480</p><div class="orca-stat-card__foot"><span class="orca-delta orca-delta--up">{% icon "arrow-up" size="xs" %}+8%</span>vs last Friday</div></a>
  <a class="orca-stat-card" href="#"><div class="orca-stat-card__head"><p class="orca-stat-label">Inside now</p><span class="orca-stat-card__icon" aria-hidden="true">{% icon "home" %}</span></div><p class="orca-stat-value">1,204</p><div class="orca-stat-card__foot">of 1,500 capacity</div></a>
  <a class="orca-stat-card" href="#"><div class="orca-stat-card__head"><p class="orca-stat-label">Videos online</p><span class="orca-stat-card__icon" aria-hidden="true">{% icon "play" %}</span></div><p class="orca-stat-value">11 of 12</p><div class="orca-stat-card__foot"><span class="orca-with-icon">{% status_icon "negative" size="xs" %}Loading dock offline</span></div></a>
  <a class="orca-stat-card" href="#"><div class="orca-stat-card__head"><p class="orca-stat-label">Count accuracy</p><span class="orca-stat-card__icon" aria-hidden="true">{% icon "statistics" %}</span></div><p class="orca-stat-value">96.4%</p><div class="orca-stat-card__foot">last 7 days</div></a>
</div>""")],
    guide=["KPI grid"], source="Tangerine",
))

add(Pattern(
    "capacity-heat-map", "Capacity heat map", C,
    "Occupancy by weekday and hour as shaded cells with the value printed, and a legend of the scale.",
    why="The busiest hours jump out from lightness alone (pre-attentive processing) while printed values keep it exact and accessible (Practical UI C03, W11).",
    when=["Capacity reports, staffing and opening-hours decisions."],
    how=["`<table class=\"orca-heatmap\">` with a caption, hour headers (`th scope=\"col\"`), weekday headers (`th scope=\"row\"`) and `td.orca-heat.orca-heat--0…5` cells; `--empty` for no data.",
         "Put the scale under it in `.orca-heatmap-legend` with the range each level covers; wrap in `.orca-table-wrap` for phones."],
    classes=[".orca-heatmap", ".orca-heatmap-legend"],
    laws=["C03", "W11", "miller"],
    uses=["heat-row", "legend-item"],
    examples=[("Heat map", """<div class="orca-table-wrap"><table class="orca-heatmap"><caption class="orca-panel-title" style="text-align: start; padding-bottom: var(--orca-space-8)">People inside, average by hour</caption>
  <thead><tr><td></td><th scope="col">09</th><th scope="col">11</th><th scope="col">13</th><th scope="col">15</th><th scope="col">17</th><th scope="col">19</th></tr></thead>
  <tbody>
    <tr><th scope="row">Mon</th><td class="orca-heat orca-heat--1">120</td><td class="orca-heat orca-heat--2">340</td><td class="orca-heat orca-heat--3">610</td><td class="orca-heat orca-heat--2">420</td><td class="orca-heat orca-heat--3">580</td><td class="orca-heat orca-heat--1">190</td></tr>
    <tr><th scope="row">Fri</th><td class="orca-heat orca-heat--1">160</td><td class="orca-heat orca-heat--3">620</td><td class="orca-heat orca-heat--5">1,010</td><td class="orca-heat orca-heat--4">760</td><td class="orca-heat orca-heat--4">910</td><td class="orca-heat orca-heat--2">310</td></tr>
    <tr><th scope="row">Sun</th><td class="orca-heat orca-heat--empty">–</td><td class="orca-heat orca-heat--0">40</td><td class="orca-heat orca-heat--1">150</td><td class="orca-heat orca-heat--1">180</td><td class="orca-heat orca-heat--0">70</td><td class="orca-heat orca-heat--empty">–</td></tr>
  </tbody></table></div>
<p class="orca-heatmap-legend">Fewer <span class="orca-heat orca-heat--0"></span><span class="orca-heat orca-heat--1"></span><span class="orca-heat orca-heat--2"></span><span class="orca-heat orca-heat--3"></span><span class="orca-heat orca-heat--4"></span><span class="orca-heat orca-heat--5"></span> More · – closed</p>""")],
    guide=["Capacity heat map"], source="Tangerine",
))

add(Pattern(
    "event-timeline", "Event timeline", C,
    "Alerts and events grouped by day, newest first, each with its status, time and snapshot.",
    why="Grouping by day chunks a long log (Miller's law); the timeline line and status dots show sequence and severity at a glance.",
    when=["Alert lists, audit and incident views, a video's history."],
    how=["`<div class=\"orca-event-timeline\">` of day groups: `<h3 class=\"orca-event-timeline__day\">Today</h3>` then a timeline of items.",
         "Each item: status dot, title, time, description and an optional thumbnail; link to the event detail."],
    classes=[".orca-event-timeline", ".orca-event-timeline__day"],
    laws=["miller", "C03"],
    uses=["timeline-item", "media-object"],
    examples=[("Timeline", """<div class="orca-event-timeline" style="max-width: 32rem">
  <section><h3 class="orca-event-timeline__day">Today</h3><ol class="orca-timeline">
    <li class="orca-timeline__item"><span class="orca-dot orca-dot--negative"></span><div><div class="orca-timeline__head"><a class="orca-timeline__title orca-link orca-link--plain" href="#">Loading dock offline</a><time class="orca-timeline__time" datetime="2026-11-06T08:14">08:14</time></div><p class="orca-timeline__desc">No stream for 5 minutes. Email sent to 2 people.</p></div></li>
    <li class="orca-timeline__item"><span class="orca-dot orca-dot--caution"></span><div><div class="orca-timeline__head"><a class="orca-timeline__title orca-link orca-link--plain" href="#">Over capacity, Entrance A</a><time class="orca-timeline__time" datetime="2026-11-06T07:55">07:55</time></div><p class="orca-timeline__desc">1,560 inside, limit 1,500.</p></div></li></ol></section>
  <section><h3 class="orca-event-timeline__day">Yesterday</h3><ol class="orca-timeline"><li class="orca-timeline__item"><span class="orca-dot orca-dot--positive"></span><div><div class="orca-timeline__head"><span class="orca-timeline__title">Gate 1 back online</span><time class="orca-timeline__time" datetime="2026-11-05T16:02">16:02</time></div></div></li></ol></section>
</div>""")],
    guide=["Event timeline"], source="Tangerine",
))
