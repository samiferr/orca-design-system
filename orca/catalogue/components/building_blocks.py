"""Components that group primitives patterns used to reach for directly.

Each ORCA level is a group of the level below it, so a pattern is built from components only. These components
name the small groups of primitives that patterns kept assembling by hand (a logo that links home, a page
heading, a captioned image, the applied filters...). They join the existing component categories.
"""

from ..registry import add
from . import Component

IDENTITY = "identity-controls"
CONTENT = "content-blocks"
DATA = "data-display"
FORMS = "forms"
NAV = "navigation"
FEEDBACK = "feedback"

# ---------------------------------------------------------------- identity and controls

add(Component(
    "logo-link", "Logo link", IDENTITY,
    "The product logo as a link to the home page.",
    why="People expect the logo to take them home (Jakob's law); one component makes it the same link with the same "
        "accessible name in the top bar, the site header, the footer, sign-in and emails.",
    when=["Top bar, site header, footer, sign-in card, error pages and emails."],
    avoid=["A second home link next to it with the same destination."],
    how=["`{% orca_logo href=\"/\" %}`: the brand logo (or the name as a wordmark) inside a link named after the product.",
         "Leave `href` empty where the page is already home, such as the sign-in page; the logo is then not a link."],
    a11y=["The link's accessible name is the product name from `settings.ORCA[\"BRAND\"][\"name\"]`."],
    classes=[".orca-logo"],
    laws=["jakob", "fitts"],
    uses=["logo"],
    examples=[("Logo link", """{% orca_logo href="#" %}""")],
    related=["top-bar", "site-header", "footer"],
))

add(Component(
    "collapse-toggle", "Collapse toggle", IDENTITY,
    "An icon button that collapses or expands a region, says which it will do, and remembers the choice.",
    why="A collapsible region gives space back without losing the way back (Practical UI S04); the button's name "
        "changes with the state so it never lies about what a press will do (Postel's law).",
    when=["The foot of a collapsible sidebar; side panels that can shrink to a rail."],
    how=["`<button class=\"orca-icon-button orca-sidebar__toggle\" type=\"button\" aria-controls=… aria-expanded=\"true\" "
         "aria-label=\"Collapse navigation\" data-orca-sidebar-toggle>{% icon \"chevron-left\" %}</button>`.",
         "The script flips `aria-expanded`, the label and the chevron, and stores the state."],
    a11y=["`aria-expanded` and `aria-controls` tell assistive technology what the button changes."],
    classes=[".orca-sidebar__toggle"],
    laws=["S04", "postel"],
    uses=["icon-button"],
    examples=[("Collapse toggle", """<button class="orca-icon-button orca-sidebar__toggle" type="button" aria-controls="ct-demo" aria-expanded="true" aria-label="Collapse navigation" data-orca-sidebar-toggle>{% icon "chevron-left" %}</button>""")],
    related=["sidebar"],
))

# ---------------------------------------------------------------- navigation

add(Component(
    "skip-navigation", "Skip navigation", NAV,
    "The skip link and the focusable main landmark it jumps to.",
    why="Keyboard and screen-reader users skip the repeated navigation in one key press (WCAG 2.4.1, Fitts's law for the "
        "keyboard); the link only works with a target that can take focus, so the two belong together.",
    when=["Every page: the base layout writes it."],
    how=["First in `<body>`: `<a class=\"orca-skip-link\" href=\"#main\">Skip to main content</a>`; the target is "
         "`<main id=\"main\" tabindex=\"-1\">`.",
         "Keep one main landmark per page."],
    a11y=["The link is the first focusable element; it shows when focused."],
    classes=[".orca-skip-link"],
    laws=["fitts", "F01"],
    uses=["skip-link"],
    examples=[("Skip navigation (press Tab inside this example)", """<div style="position: relative; height: 3rem; overflow: hidden">
  <a class="orca-skip-link" href="#sn-main">Skip to main content</a>
  <div id="sn-main" tabindex="-1" class="orca-small orca-muted" style="padding: var(--orca-space-8)">Main content starts here.</div>
</div>""")],
    related=["base-layout"],
))

add(Component(
    "link-column", "Link column", NAV,
    "A titled list of links, as in a footer or a site map.",
    why="A short title over a few links lets people scan a footer by topic (Miller's law: chunking, Practical UI L01).",
    when=["Footer columns, site maps, 'Related' lists at the end of documentation pages."],
    avoid=["More than about eight links in one column: split it by topic."],
    how=["`<ul class=\"orca-footer__col\"><li class=\"orca-footer__col-title\">Product</li><li><a href=…>Features</a></li>…</ul>`.",
         "Link text names the destination (W14)."],
    classes=[".orca-footer__col", ".orca-footer__col-title"],
    laws=["miller", "L01", "W14"],
    uses=["text-link"],
    examples=[("Link column", """<ul class="orca-footer__col"><li class="orca-footer__col-title">Help</li><li><a href="#">Documentation</a></li><li><a href="#">Contact support</a></li></ul>""")],
    related=["footer"],
))

# ---------------------------------------------------------------- content blocks

add(Component(
    "page-heading", "Page heading", CONTENT,
    "The page title, the one-sentence subtitle and an optional meta line with status badges.",
    why="People confirm where they are from the title first and what the page is for from the subtitle (Jakob's law, "
        "Practical UI W04); keeping the three together keeps their spacing and order the same on every page.",
    when=["Inside the page head of application pages and documentation pages."],
    how=["`<div class=\"orca-page-head__text\">` with `h1.orca-page-title`, `p.orca-page-subtitle` and "
         "`p.orca-page-head__meta` (facts in small text, status as badges with a word)."],
    a11y=["The title is the page's only `<h1>`."],
    classes=[".orca-page-head__text", ".orca-page-head__meta"],
    laws=["jakob", "W04", "L03"],
    uses=["page-title", "page-subtitle", "small-text", "badge"],
    examples=[("Page heading", """<div class="orca-page-head__text">
  <h1 class="orca-page-title">Videos</h1>
  <p class="orca-page-subtitle">Every video from North building.</p>
  <p class="orca-page-head__meta"><span class="orca-badge orca-badge--subtle orca-badge--positive">{% icon "success" %}Published</span><span>Updated 2 minutes ago</span></p>
</div>""")],
    related=["page-head", "docs-page-header"],
))

add(Component(
    "section-heading", "Section heading", CONTENT,
    "A section title with an optional one-paragraph introduction.",
    why="A title and one sentence of why let people decide whether a section concerns them before reading it "
        "(Practical UI W05: inverted pyramid, L01: grouping).",
    when=["Form sections, settings groups, documentation sections."],
    how=["`<h2 class=\"orca-section-title\">` then `<p class=\"orca-p\">` of one or two sentences.",
         "Keep heading levels in order on the page."],
    classes=[".orca-section-title"],
    laws=["W05", "L01"],
    uses=["section-title", "paragraph"],
    examples=[("Section heading", """<h2 class="orca-section-title">Thumbnails</h2>
<p class="orca-p orca-muted">How often thumbnails are taken and how long videos are kept.</p>""")],
    related=["form-section"],
))

add(Component(
    "feature-item", "Feature item", CONTENT,
    "One feature: an icon, a short title and one sentence.",
    why="An icon and a title are recognised before the sentence is read (Miller's law); one sentence per feature keeps "
        "the list scannable (Practical UI W01).",
    when=["Feature grids on marketing pages; 'What you can do' lists on empty dashboards."],
    how=["`<li class=\"orca-feature\">{% icon \"statistics\" size=\"l\" %}<h3 class=\"orca-feature__title\">…</h3>"
         "<p class=\"orca-feature__text\">…</p></li>`.",
         "The title says the benefit in two to four words."],
    a11y=["The icon is decorative; the title carries the meaning."],
    classes=[".orca-feature", ".orca-feature__title", ".orca-feature__text"],
    laws=["miller", "W01"],
    uses=["icon", "heading", "paragraph"],
    examples=[("Feature item", """<ul style="list-style: none; margin: 0; padding: 0; max-width: 18rem"><li class="orca-feature">{% icon "notifications" size="l" %}<h3 class="orca-feature__title">Upload alerts</h3><p class="orca-feature__text">Get an email when a video fails to process.</p></li></ul>""")],
    related=["feature-grid"],
))

add(Component(
    "captioned-media", "Captioned media", CONTENT,
    "An image or video in its aspect-ratio frame, with a caption or a flag over a solid bar.",
    why="The frame reserves the space so nothing jumps while the media loads (Doherty threshold); a caption on a "
        "solid bar stays readable over any picture (Practical UI T12).",
    when=["Photo posts, gallery stages, story images, editors that draw over an image."],
    how=["`<figure class=\"orca-ratio orca-ratio--16x9\"><img …><figcaption class=\"orca-frame__caption\">…</figcaption></figure>`.",
         "Without a caption, the frame alone: `<div class=\"orca-ratio orca-ratio--4x3\"><img …></div>`."],
    a11y=["Alt text says what matters in the image; the caption repeats source and time visibly."],
    classes=[".orca-ratio", ".orca-frame__caption"],
    laws=["doherty", "T12"],
    uses=["media-frame", "snapshot-image"],
    examples=[("Captioned image", """<figure class="orca-ratio orca-ratio--16x9" style="max-width: 20rem; margin: 0">
  <img src="{% static "orca/img/sample-street.svg" %}" alt="City street at night">
  <figcaption class="orca-frame__caption"><span>Harbour timelapse</span><time datetime="2026-11-06T08:14:03">08:14:03</time></figcaption>
</figure>""")],
    related=["photo-post", "image-gallery", "story-feature"],
))

add(Component(
    "thumbnail-strip", "Thumbnail strip", CONTENT,
    "A row of thumbnail buttons that choose the image shown, the current one marked.",
    why="Thumbnails show what is there and let people jump straight to an image (Miller's law: recognition over recall); "
        "the current one changes shape, not only colour (C03).",
    when=["Image galleries and media pickers with up to about twenty items."],
    how=["`<ul class=\"orca-gallery__thumbs\"><li><button class=\"orca-gallery__thumb\" type=\"button\" aria-current=\"true\" "
         "aria-label=\"Image 1, 08:14\"><img src=… alt=\"\"></button></li>…</ul>`."],
    a11y=["Each button is named after the image it shows; `aria-current` marks the one on stage."],
    classes=[".orca-gallery__thumbs", ".orca-gallery__thumb"],
    laws=["miller", "C03"],
    uses=["thumbnail"],
    examples=[("Thumbnails", """<ul class="orca-gallery__thumbs"><li><button class="orca-gallery__thumb" type="button" aria-current="true" aria-label="Image 1, street"><img src="{% static "orca/img/sample-street.svg" %}" alt=""></button></li><li><button class="orca-gallery__thumb" type="button" aria-label="Image 2, floor plan"><img src="{% static "orca/img/sample-floor.svg" %}" alt=""></button></li></ul>""")],
    related=["image-gallery"],
))

add(Component(
    "video-player", "Video player", CONTENT,
    "A native video in its frame, with a live or recording flag and the current time.",
    why="Native controls are familiar and keyboard accessible (Jakob's law, Postel's law); a worded flag makes "
        "'live' or 'recording' impossible to miss (Von Restorff, C03).",
    when=["Recorded clips, live streams, tutorials."],
    how=["`<div class=\"orca-ratio orca-ratio--16x9\"><video class=\"orca-video\" controls preload=\"metadata\" poster=…></video></div>`.",
         "Live or recording: add `.orca-frame--recording` and `<span class=\"orca-frame__flag\">` with a pulsing dot and the word.",
         "Never autoplay with sound."],
    a11y=["Provide captions for speech; name the video with `aria-label` when no visible title is next to it."],
    classes=[".orca-video", ".orca-frame--recording", ".orca-frame__flag"],
    laws=["jakob", "postel", "restorff", "C03"],
    uses=["video-frame", "recording-frame", "time-label"],
    examples=[("Live video", """<div class="orca-ratio orca-ratio--16x9 orca-frame--recording" style="max-width: 20rem">
  <video class="orca-video" controls preload="none" poster="{% static "orca/img/sample-street.svg" %}" aria-label="Harbour, live"></video>
  <span class="orca-frame__flag"><span class="orca-dot orca-dot--sm orca-dot--pulse"></span>Live · <time datetime="2026-11-06T08:14">08:14</time></span>
</div>""")],
    related=["recording-player", "live-stream-panel"],
))

add(Component(
    "call-to-action", "Call to action", CONTENT,
    "The one or two actions a section asks for: the primary button and an optional quieter alternative.",
    why="One clear primary action per section (Practical UI B03, Hick's law) with the alternative visibly quieter (B05).",
    when=["Site headers, heroes, email frames, empty pages."],
    avoid=["Three or more actions: keep one, move the rest to a menu or a link."],
    how=["`<div class=\"orca-site-header__actions\"><a class=\"orca-button orca-button--ghost\" href=…>Sign in</a>"
         "<a class=\"orca-button orca-button--brand\" href=…>Start free trial</a></div>`.",
         "In emails the button is a table-based link with the address written below it."],
    classes=[".orca-site-header__actions"],
    laws=["B03", "B05", "hick"],
    uses=["button", "text-link"],
    examples=[("Call to action", """<div class="orca-site-header__actions"><a class="orca-button orca-button--ghost" href="#">Sign in</a><a class="orca-button orca-button--brand" href="#">Start free trial</a></div>""")],
    related=["site-header", "email-frame", "hero"],
))

add(Component(
    "fine-print", "Fine print", CONTENT,
    "Small legal and version text on one line, with its policy links.",
    why="Legal text must be there but must not compete (Practical UI S02); small, muted and on one line it stays "
        "findable without taking attention (T13: quieter text stays legible).",
    when=["Footers, email footers, sign-in pages."],
    how=["`<p class=\"orca-footer__legal\">© 2026 Acme · <a href=…>Privacy</a> · <a href=…>Terms</a> · Version 0.4.0</p>`."],
    classes=[".orca-footer__legal"],
    laws=["S02", "T13"],
    uses=["small-text", "text-link"],
    examples=[("Fine print", """<p class="orca-footer__legal">© 2026 Acme · <a href="#">Privacy</a> · <a href="#">Terms</a> · Version 0.4.0</p>""")],
    related=["footer", "email-frame"],
))

# ---------------------------------------------------------------- data display

add(Component(
    "big-number", "Big number", DATA,
    "One large figure with the statement it supports and where it comes from.",
    why="A single striking number is remembered (Von Restorff, Peak–end rule); the statement and the source keep it honest.",
    when=["Editorial factoids, live counts beside a video, report highlights."],
    avoid=["Several big numbers side by side: use stat cards in a KPI grid."],
    how=["`<figure class=\"orca-factoid\"><span class=\"orca-factoid__number\">−34%</span><figcaption><p class=\"orca-factoid__text\">…</p>"
         "<p class=\"orca-factoid__source\">…</p></figcaption></figure>`.",
         "Numbers as digits with separators and the sign written (W11)."],
    classes=[".orca-factoid", ".orca-factoid__number", ".orca-factoid__text", ".orca-factoid__source"],
    laws=["restorff", "peak-end", "W11"],
    uses=["stat-value", "small-text"],
    examples=[("Big number", """<figure class="orca-factoid" style="margin: 0"><span class="orca-factoid__number">2,480</span><figcaption><p class="orca-factoid__text">videos published this year</p><p class="orca-factoid__source">Library, November 2026</p></figcaption></figure>""")],
    related=["factoid"],
))

add(Component(
    "summary-tile", "Summary tile", DATA,
    "A count with its status word, as a link that filters the list to that status.",
    why="Counts by status answer 'how many need me?' at a glance (Miller's law) and double as the quickest filter (Fitts's "
        "law: a large target); the dot is paired with a word (C03).",
    when=["Above lists and tables whose records have a status."],
    how=["`<a class=\"orca-summary-tile\" href=\"?status=offline\"><span class=\"orca-summary-tile__value\">1</span>"
         "<span class=\"orca-summary-tile__label\"><span class=\"orca-dot orca-dot--negative\"></span>Offline</span></a>`.",
         "The tile for the current filter has `aria-current=\"true\"`."],
    classes=[".orca-summary-tile", ".orca-summary-tile__value", ".orca-summary-tile__label"],
    laws=["miller", "fitts", "C03"],
    uses=["stat-value", "status-dot"],
    examples=[("Summary tile", """<a class="orca-summary-tile" href="#" style="max-width: 10rem"><span class="orca-summary-tile__value">10</span><span class="orca-summary-tile__label"><span class="orca-dot orca-dot--positive"></span>Published</span></a>""")],
    related=["summary-tiles"],
))

add(Component(
    "heat-row", "Heat-map row", DATA,
    "One labelled row of heat-map cells, each with its value printed.",
    why="A row per weekday or resource lets people compare hours along a line (Miller's law); printing the value means "
        "the shade is never the only carrier of meaning (C03).",
    when=["Capacity and occupancy heat maps, availability grids."],
    how=["`<tr><th scope=\"row\">Mon</th><td class=\"orca-heat orca-heat--3\">142</td>…</tr>` inside `table.orca-heatmap`."],
    a11y=["The row header names the row; the column headers name the hours."],
    classes=[".orca-heatmap", ".orca-heat"],
    laws=["miller", "C03"],
    uses=["heat-cell"],
    examples=[("Row", """<table class="orca-heatmap"><tbody><tr><th scope="row">Mon</th><td class="orca-heat orca-heat--1">12</td><td class="orca-heat orca-heat--3">142</td><td class="orca-heat orca-heat--5">310</td></tr></tbody></table>""")],
    related=["capacity-heat-map"],
))

add(Component(
    "column-header", "Column header", DATA,
    "A board column's title with its card count and, when set, its limit.",
    why="The count and the limit show at a glance where work piles up (Miller's law, Von Restorff when over the limit).",
    when=["Kanban columns, grouped lists."],
    how=["`<h3 class=\"orca-board__head\">In progress <span class=\"orca-badge orca-badge--grey\">3</span>"
         "<span class=\"orca-board__limit\">limit 4</span></h3>`; over the limit, the column gets `.is-over`."],
    classes=[".orca-board__head", ".orca-board__limit"],
    laws=["miller", "restorff"],
    uses=["badge"],
    examples=[("Column header", """<h3 class="orca-board__head">In progress <span class="orca-badge orca-badge--grey">3</span><span class="orca-board__limit">limit 4</span></h3>""")],
    related=["kanban-board"],
))

# ---------------------------------------------------------------- forms

add(Component(
    "row-select", "Row selection", FORMS,
    "A checkbox per table row and a select-all checkbox in the header.",
    why="Selecting rows before choosing an action lets people act on many records at once (Practical UI F03); checkboxes "
        "are the familiar control for it (Jakob's law, R14).",
    when=["Tables that offer bulk actions."],
    how=["Header: `<th scope=\"col\" class=\"orca-table__select\"><label class=\"orca-check\"><input type=\"checkbox\" "
         "aria-label=\"Select all videos\"><span class=\"orca-check__box\"></span></label></th>`; one per row named after the row.",
         "When rows are selected, the table toolbar shows the count and the bulk actions."],
    a11y=["Each checkbox is named after its row ('Select Entrance A')."],
    classes=[".orca-table__select"],
    laws=["F03", "jakob", "R14"],
    uses=["checkbox"],
    examples=[("Select cells", """<table class="orca-table"><thead><tr><th scope="col" class="orca-table__select"><label class="orca-check"><input type="checkbox" aria-label="Select all videos"><span class="orca-check__box"></span></label></th><th scope="col">Video</th></tr></thead>
<tbody><tr><td class="orca-table__select"><label class="orca-check"><input type="checkbox" checked aria-label="Select Harbour at dusk"><span class="orca-check__box"></span></label></td><td>Harbour at dusk</td></tr></tbody></table>""")],
    related=["data-table", "table-toolbar"],
))

add(Component(
    "formatting-toolbar", "Formatting toolbar", FORMS,
    "A row of pressed-state icon buttons for bold, italic, lists and links over a text area.",
    why="Formatting commands are recognised by their familiar glyphs (Jakob's law); pressed states show what applies to "
        "the selection (Practical UI F10).",
    when=["Above a rich text field."],
    how=["`<div class=\"orca-richtext__toolbar\" role=\"toolbar\" aria-label=\"Formatting\">` with dense icon buttons using "
         "`aria-pressed`, groups separated by a vertical divider."],
    a11y=["Arrow keys move between the buttons of the toolbar; each has an accessible name."],
    classes=[".orca-richtext__toolbar"],
    laws=["jakob", "F10"],
    uses=["icon-button", "divider"],
    examples=[("Toolbar", """<div class="orca-richtext__toolbar" role="toolbar" aria-label="Formatting" style="max-width: 20rem"><button class="orca-icon-button orca-icon-button--dense" type="button" aria-pressed="true" aria-label="Bold"><b>B</b></button><button class="orca-icon-button orca-icon-button--dense" type="button" aria-pressed="false" aria-label="Italic"><i>I</i></button><span class="orca-divider orca-divider--vertical" role="separator"></span><button class="orca-icon-button orca-icon-button--dense" type="button" aria-pressed="false" aria-label="Bulleted list">{% icon "list" %}</button></div>""")],
    related=["rich-text-editor"],
))

add(Component(
    "applied-filters", "Applied filters", FORMS,
    "The filters in effect as removable tags, with Clear all and the number of results.",
    why="Filters that are on must stay visible and reversible (Practical UI S06, Postel's law); the count confirms "
        "what they did (Doherty threshold).",
    when=["Above results while at least one filter is applied; inside a no-results state."],
    how=["`<div class=\"orca-filter-bar__applied\"><span class=\"orca-small orca-muted\">Filtered by</span>` then one removable "
         "tag per filter, a 'Clear all' link button and the count in `role=\"status\"`."],
    a11y=["Each remove button names the filter it removes."],
    classes=[".orca-filter-bar__applied"],
    laws=["S06", "postel", "doherty"],
    uses=["tag", "link-action"],
    examples=[("Applied filters", """<div class="orca-filter-bar__applied"><span class="orca-small orca-muted">Filtered by</span><span class="orca-tag"><span class="orca-tag__text">Type: Video</span><button class="orca-tag__remove" type="button" aria-label="Remove filter Type: Video">{% icon "close" %}</button></span><button class="orca-button orca-button--link" type="button">Clear all</button><span class="orca-small orca-muted" role="status">14 videos</span></div>""")],
    related=["filter-bar", "no-results"],
))

# ---------------------------------------------------------------- feedback

add(Component(
    "card-skeleton", "Card skeleton", FEEDBACK,
    "The grey shape of a card (image, title, two lines) while the real card loads.",
    why="A placeholder in the final shape shows that content is coming and where (Doherty threshold) and prevents the "
        "layout from jumping when it arrives.",
    when=["Grids and feeds that load cards after the page."],
    avoid=["Content that arrives in under a second: show nothing."],
    how=["`<div aria-hidden=\"true\"><div class=\"orca-skeleton orca-aspect-16x9\"></div><div class=\"orca-skeleton orca-skeleton--title\"></div>"
         "<div class=\"orca-skeleton orca-skeleton--text\"></div></div>`; the region around the placeholders has `aria-busy=\"true\"` and a label."],
    a11y=["Placeholders are hidden from assistive technology; the region's label says what is loading."],
    classes=[".orca-skeleton", ".orca-skeleton--title", ".orca-skeleton--text"],
    laws=["doherty"],
    uses=["skeleton"],
    examples=[("Card skeleton", """<div aria-busy="true" aria-label="Loading video" style="max-width: 16rem; padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border)"><div aria-hidden="true"><div class="orca-skeleton orca-aspect-16x9" style="margin-bottom: var(--orca-space-8)"></div><div class="orca-skeleton orca-skeleton--title"></div><div class="orca-skeleton orca-skeleton--text" style="max-width: 70%"></div></div></div>""")],
    related=["video-grid", "loading-placeholder"],
))
