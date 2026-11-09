"""Patterns that templates used to assemble from components directly.

A template is a group of patterns, so the sections templates kept writing by hand get a name here: the landmarks
every page has, an error message, a grid of cards, loading placeholders and the no-results state.
"""

from ..registry import add
from . import Pattern

FRAME = "page-frame"
GRIDS = "grids"
DATA = "data-filtering"

add(Pattern(
    "page-landmarks", "Page landmarks", FRAME,
    "The regions every page has: skip navigation, the main landmark and the place dialogs open in.",
    why="Landmarks let assistive technology jump straight to the content (WCAG 1.3.1, 2.4.1) and give dialogs one place "
        "outside the content flow, so focus and stacking work the same on every page (Jakob's law, Tesler's law).",
    when=["Every page: the base layout writes them, so pages never do."],
    how=["`<body>` starts with the skip navigation; `<main id=\"main\" tabindex=\"-1\">` holds the content; dialogs and "
         "drawers go in `{% block modal %}` after `</main>`."],
    a11y=["One `<main>` per page; dialogs outside it are opened with `showModal()` so the page behind is inert."],
    classes=[".orca-skip-link"],
    laws=["jakob", "tesler", "F01"],
    uses=["skip-navigation", "dialog"],
    examples=[("Landmarks (press Tab inside this example)", """<div style="position: relative; overflow: hidden; border: var(--orca-border-width) solid var(--orca-border)">
  <a class="orca-skip-link" href="#pl-main">Skip to main content</a>
  <div id="pl-main" tabindex="-1" style="padding: var(--orca-space-16)"><p class="orca-p">Main content.</p></div>
</div>""")],
    related=["base-layout"],
))

add(Pattern(
    "error-message", "Error message", FRAME,
    "What an error page says: the code, what happened in plain words, what to do, and a way back.",
    why="An error is a low point of the experience; saying what happened and offering the next step softens it "
        "(Peak–end rule, Practical UI W15), and the logo link is the familiar way out (Jakob's law).",
    when=["403, 404 and 500 pages; a section that cannot load at all."],
    how=["`<div class=\"orca-error-layout\">` with the logo link, an illustration, `.orca-error-layout__code`, "
         "the empty-state title and text, and one action (Go to the dashboard) plus a back link.",
         "Never blame the person; never show a stack trace."],
    classes=[".orca-error-layout", ".orca-error-layout__body", ".orca-error-layout__code"],
    laws=["peak-end", "W15", "jakob"],
    uses=["empty-state", "logo-link", "back-link"],
    examples=[("Not found", """<div class="orca-error-layout" style="min-height: 0">{% orca_logo href="#" %}<div class="orca-error-layout__body">{% orca_illustration "search" %}<p class="orca-error-layout__code">404</p><h1 class="orca-empty-title">This page does not exist</h1><p class="orca-empty-text">The link may be old, or the page was moved.</p><a class="orca-button orca-button--primary" href="#">Go to the dashboard</a></div></div>""")],
    related=["error-layouts"],
))

add(Pattern(
    "card-grid", "Card grid", GRIDS,
    "Cards for records, products or people in as many equal columns as fit.",
    why="Equal cards in a grid let people compare items by position and shape (Miller's law, Practical UI L11) and adapt "
        "to any width without a breakpoint.",
    when=["Collections people browse: records, products, people."],
    avoid=["Records people compare field by field: use a data table."],
    how=["`<ul class=\"orca-card-grid\">` with one card per `<li>`; a linked card when the whole card opens the record.",
         "Keep every card's content in the same order so the grid reads as a table."],
    classes=[".orca-card-grid"],
    laws=["miller", "L11"],
    uses=["linked-card", "person-block"],
    examples=[("Cards", """<ul class="orca-card-grid"><li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Harbour at dusk</h3><p class="orca-card-meta">Video · 4 min</p></div></li><li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Summer 2026</h3><p class="orca-card-meta">Album · 36 images</p></div></li><li class="orca-card"><div class="orca-card__body"><div class="orca-person"><span class="orca-avatar" aria-hidden="true">AL</span><span class="orca-person__text"><span class="orca-person__name">Ada Lovelace</span><span class="orca-person__role">Editor</span></span></div></div></li></ul>""")],
    related=["card-grid-layout", "person-block-grid"],
))

add(Pattern(
    "loading-placeholder", "Loading placeholder", GRIDS,
    "Placeholder cards in the shape of the content while a grid or feed loads, announced to screen readers.",
    why="Placeholders in the final shape make waiting feel shorter and keep the layout still (Doherty threshold); the busy "
        "region tells assistive technology that content is on its way.",
    when=["Grids and feeds that load after the page, or load more on scroll."],
    how=["A region with `aria-busy=\"true\"` and `aria-label=\"Loading videos\"` holding two or three card skeletons; replace the "
         "whole region when the content arrives."],
    a11y=["Remove `aria-busy` when the content is in; announce the result count politely."],
    laws=["doherty"],
    uses=["card-skeleton"],
    examples=[("Loading", """<div class="orca-row orca-row--16" aria-busy="true" aria-label="Loading videos" style="align-items: flex-start"><div style="width: 12rem; padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border)"><div aria-hidden="true"><div class="orca-skeleton orca-aspect-16x9" style="margin-bottom: var(--orca-space-8)"></div><div class="orca-skeleton orca-skeleton--title"></div></div></div><div style="width: 12rem; padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border)"><div aria-hidden="true"><div class="orca-skeleton orca-aspect-16x9" style="margin-bottom: var(--orca-space-8)"></div><div class="orca-skeleton orca-skeleton--title"></div></div></div></div>""")],
    related=["feed-skeleton", "video-grid"],
))

add(Pattern(
    "no-results", "No results", DATA,
    "What a list, table or feed shows when it has nothing: the empty state, and the applied filters when filters hide everything.",
    why="An empty list is a dead end unless it says why and what to do (Peak–end rule, Practical UI W15). When filters "
        "caused it, showing them with Clear all is the fastest way back (Postel's law).",
    when=["Every list, table, grid and feed, for the empty and the filtered-empty cases."],
    how=["First use: the empty state with the create action ('Add your first video').",
         "Filtered empty: the empty state ('No videos match these filters') above the applied filters with Clear all."],
    laws=["peak-end", "W15", "postel"],
    uses=["empty-state", "applied-filters"],
    examples=[("Filtered empty", """<div class="orca-empty">{% orca_illustration "search" %}<h2 class="orca-empty-title">No videos match these filters</h2><p class="orca-empty-text">Remove a filter, or clear them all to see every video.</p>
<div class="orca-filter-bar__applied" style="justify-content: center"><span class="orca-tag"><span class="orca-tag__text">Album: Summer 2026</span><button class="orca-tag__remove" type="button" aria-label="Remove filter Album: Summer 2026">{% icon "close" %}</button></span><button class="orca-button orca-button--link" type="button">Clear all</button></div></div>""")],
    related=["generic-list", "simple-data-page", "feed-skeleton"],
))
