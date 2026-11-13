from ..registry import add, category
from . import Pattern

C = category(
    "page-frame", "Page frame",
    "The parts that surround every page: headers, top bar, sidebar, footer, page head, messages, drawers and filter panels.",
    level="pattern",
)

add(Pattern(
    "site-header", "Header", C,
    "Header of public pages: logo, a few section links and one or two actions, sticky at the top.",
    why="People expect the logo top-left (home) and the main sections beside it on every site (Jakob's law); one primary action keeps the next step obvious (Hick's law).",
    when=["Public and marketing pages, documentation sites, sign-in pages."],
    avoid=["Inside the application: use the top bar."],
    how=["`<header class=\"orca-site-header\">` with the logo, `<nav aria-label=\"Main\"><ul class=\"orca-site-header__nav\">` and `.orca-site-header__actions`.",
         "At most 5 links; the current one gets `aria-current=\"page\"`. On phones the links wrap under the logo."],
    classes=[".orca-site-header", ".orca-site-header__nav", ".orca-site-header__actions"],
    laws=["jakob", "hick", "B03"],
    uses=["logo-link", "primary-navigation", "call-to-action"],
    examples=[("Header", """<header class="orca-site-header" style="position: static">
  {% orca_logo href="#" %}
  <nav aria-label="Main"><ul class="orca-site-header__nav"><li><a href="#" aria-current="page">Product</a></li><li><a href="#">Pricing</a></li><li><a href="#">Docs</a></li></ul></nav>
  <div class="orca-site-header__actions"><a class="orca-button orca-button--ghost" href="#">Sign in</a><a class="orca-button orca-button--brand" href="#">Start free trial</a></div>
</header>""")],
    guide=["Header"],
))

add(Pattern(
    "top-bar", "Top bar", C,
    "The application's top bar: menu button, logo, main sections, search and user tools.",
    why="A persistent bar in the expected place anchors every page of an application (Jakob's law); dense controls keep it to 56px so content stays in view (Practical UI F03).",
    when=["Every authenticated page of an application."],
    how=["`<header class=\"orca-topbar\">` with `.orca-topbar__start` (menu or sidebar toggle, logo, primary navigation) and `.orca-topbar__end` (search, utility navigation).",
         "It is the wise_people_analyzer bar: `--orca-brand-bar` (the brand colour mixed with 30% black, darkened further if white text would fall below 4.5:1) with `--orca-brand-bar-on` text.",
         "Below 1036px, navigation and search move into the drawer, opened by the menu button."],
    classes=[".orca-topbar", ".orca-topbar__start", ".orca-topbar__end"],
    tokens=["brand-bar", "brand-bar-on", "brand-bar-hover"],
    laws=["jakob", "F03", "fitts"],
    uses=["logo-link", "primary-navigation", "utility-navigation", "search-field"],
    examples=[("Top bar", """<div class="orca-stack" style="gap: var(--orca-space-16)">
<header class="orca-topbar" style="position: static">
  <div class="orca-topbar__start"><button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Open menu">{% icon "menu" %}</button>{% orca_logo href="#" %}
    <nav aria-label="Main"><ul class="orca-topnav"><li><a href="#" aria-current="page">Dashboard</a></li><li><a href="#">Videos</a></li><li><a href="#">Reports</a></li></ul></nav></div>
  <div class="orca-topbar__end"><div class="orca-search">{% icon "search" %}<input class="orca-input orca-input--dense" type="search" placeholder="Search" aria-label="Search"></div>
    <a class="orca-icon-button orca-has-count" href="#" aria-label="Notifications, 3 unread">{% icon "notifications" %}<span class="orca-count" aria-hidden="true">3</span></a>
    <button class="orca-user-chip" type="button"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span class="orca-user-chip__text"><span class="orca-user-chip__name">Ada Lovelace</span></span></button></div>
</header></div>""")],
    guide=["Top bar"], source="Tangerine",
))

add(Pattern(
    "sidebar", "Sidebar", C,
    "Side navigation for an application: grouped section links that collapse to an icon rail, remembered per person.",
    why="Products with many sections need a persistent, scannable list; groups chunk it (Miller's law) and collapsing gives space back to dense screens (Tesler's law: the person decides).",
    when=["Applications with more than about 5 sections."],
    how=["`<div class=\"orca-app\">` holds `<nav class=\"orca-sidebar\" id=… aria-label=\"Sections\">` and `<main class=\"orca-app__main\">`.",
         "Sections: `.orca-sidebar__section` with an optional `.orca-sidebar__label` and side links; `.orca-sidebar__foot` holds the collapse toggle (`data-orca-sidebar-toggle aria-controls=…`).",
         "Collapsed (`data-collapsed=\"true\"`): labels are hidden visually but still read by screen readers, and the rail keeps icons. Give each link a `title` for tooltips.",
         "The state is remembered per sidebar in `localStorage` under `orca-sidebar:<id>`, so give the sidebar an `id`.",
         "Nest a nav tree inside a section for long lists, such as this documentation's navigation; hide it when collapsed.",
         "Below 620px the sidebar hides; put the same links in a drawer opened from the top bar."],
    classes=[".orca-app", ".orca-app__main", ".orca-sidebar", ".orca-sidebar__section", ".orca-sidebar__label", ".orca-sidebar__foot"],
    laws=["miller", "tesler", "jakob"],
    uses=["sidebar-link", "nav-tree", "collapse-toggle"],
    examples=[("Sidebar with collapse", """<div class="orca-app" style="min-height: 22rem; border: var(--orca-border-width) solid var(--orca-border)">
  <nav class="orca-sidebar" id="sb-demo" aria-label="Sections" data-collapsed="false">
    <div class="orca-sidebar__section"><ul class="orca-side-nav">
      <li><a class="orca-side-link" href="#" aria-current="page">{% icon "home" %}<span class="orca-side-link__label">Dashboard</span></a></li>
      <li><a class="orca-side-link" href="#">{% icon "snapshot" %}<span class="orca-side-link__label">Videos</span><span class="orca-count orca-count--neutral">12</span></a></li>
      <li><a class="orca-side-link" href="#">{% icon "statistics" %}<span class="orca-side-link__label">Reports</span></a></li></ul></div>
    <div class="orca-sidebar__section"><p class="orca-sidebar__label">Admin</p><ul class="orca-side-nav"><li><a class="orca-side-link" href="#">{% icon "user" %}<span class="orca-side-link__label">Users</span></a></li><li><a class="orca-side-link" href="#">{% icon "settings" %}<span class="orca-side-link__label">Settings</span></a></li></ul></div>
    <div class="orca-sidebar__foot"><button class="orca-icon-button orca-sidebar__toggle" type="button" aria-controls="sb-demo" aria-expanded="true" aria-label="Collapse navigation" data-orca-sidebar-toggle>{% icon "chevron-left" %}</button></div>
  </nav>
  <main class="orca-app__main"><h1 class="orca-page-title">Dashboard</h1></main>
</div>""")],
    guide=["Sidebar"], source="Tangerine",
))

add(Pattern(
    "footer", "Footer", C,
    "The bottom of public pages: link columns, legal text and version.",
    why="People look at the bottom for legal, contact and help links (Jakob's law); grouping them in titled columns makes them findable (Miller's law).",
    when=["Public and documentation sites; a slim version (legal and version only) in applications."],
    how=["`<footer class=\"orca-footer\">` with `.orca-footer__cols` of `<ul class=\"orca-footer__col\">` (first item `.orca-footer__col-title`) and `.orca-footer__legal`."],
    classes=[".orca-footer", ".orca-footer__cols", ".orca-footer__col", ".orca-footer__col-title", ".orca-footer__legal"],
    laws=["jakob", "miller"],
    uses=["logo-link", "link-column", "fine-print"],
    examples=[("Footer", """<footer class="orca-footer">
  {% orca_logo href="" %}
  <div class="orca-footer__cols">
    <ul class="orca-footer__col"><li class="orca-footer__col-title">Product</li><li><a href="#">Features</a></li><li><a href="#">Pricing</a></li></ul>
    <ul class="orca-footer__col"><li class="orca-footer__col-title">Help</li><li><a href="#">Documentation</a></li><li><a href="#">Contact support</a></li></ul>
  </div>
  <p class="orca-footer__legal">© 2026 Acme · <a href="#">Privacy</a> · <a href="#">Terms</a> · Version 0.3.0</p>
</footer>""")],
    guide=["Footer"],
))

add(Pattern(
    "page-head", "Page head", C,
    "The top of a page's content: breadcrumbs or back link, title, subtitle, meta info and page actions.",
    why="One consistent head answers 'where am I, what is this, what can I do here' before anything else (Jakob's law); one primary action keeps the priority clear (Practical UI B03).",
    when=["The top of every application page."],
    how=["`<div class=\"orca-page-head\">` with `.orca-page-head__text` (breadcrumbs or back link, `h1.orca-page-title`, `.orca-page-subtitle`, `.orca-page-head__meta`) and `.orca-page-head__actions`.",
         "Actions: secondary buttons first, then the primary or create button; on phones they stretch full width."],
    classes=[".orca-page-head", ".orca-page-head__text", ".orca-page-head__meta", ".orca-page-head__actions"],
    laws=["jakob", "B03", "L03"],
    uses=["page-heading", "breadcrumbs", "create-button"],
    examples=[("Page head", """<div class="orca-page-head">
  <div class="orca-page-head__text"><nav class="orca-breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="#">Sites</a></li><li><span aria-current="page">North building</span></li></ol></nav>
    <h1 class="orca-page-title">Videos</h1><p class="orca-page-subtitle">Every video from North building.</p>
    <p class="orca-page-head__meta"><span class="orca-status"><span class="orca-dot orca-dot--positive"></span>11 online</span><span class="orca-status"><span class="orca-dot orca-dot--negative"></span>1 offline</span></p></div>
  <div class="orca-page-head__actions"><button class="orca-button" type="button">{% icon "upload" %}Export</button><a class="orca-button orca-button--primary orca-create orca-create--static" href="#">{% icon "plus" %}Add video</a></div>
</div>""")],
    guide=["Page head"], source="Tangerine",
))

add(Pattern(
    "messages-region", "Messages region", C,
    "A region under the page head that shows the result of the last action, announced politely.",
    why="Results always in the same place are found at once (Jakob's law); a live region announces them to screen-reader users (Postel's law).",
    when=["Every page, in the base template, between the page head and the content."],
    how=["`<div class=\"orca-messages-region\" aria-live=\"polite\">{% templatetag openblock %} orca_messages {% templatetag closeblock %}</div>`; errors inside use `role=\"alert\"`.",
         "Toasts float elsewhere; this region keeps messages until they are read."],
    classes=[".orca-messages-region", ".orca-messages"],
    laws=["jakob", "postel", "peak-end"],
    uses=["flash-message"],
    examples=[("Region", """<div class="orca-messages-region" aria-live="polite"><div class="orca-messages">
  <div class="orca-alert orca-alert--positive" role="status">{% status_icon "positive" %}<p class="orca-alert__body">Video “Gate 1” added. Draw its zones next.</p><button class="orca-icon-button orca-icon-button--dense orca-alert__close" type="button" aria-label="Dismiss message" data-orca-dismiss>{% icon "close" %}</button></div>
</div></div>""")],
    guide=["Messages region"], source="Tangerine",
))

add(Pattern(
    "drawer", "Drawer", C,
    "A panel that slides in over the page from one edge, built on the native dialog.",
    why="A drawer keeps the page in view behind it, for tasks that refer to the page (Practical UI L14); the native dialog traps focus and closes with Escape (Postel's law).",
    when=["Navigation on phones, filters, details of a selected row, quick settings."],
    avoid=["Long forms: use a page."],
    how=["`<dialog class=\"orca-drawer\" id=… aria-labelledby=… data-orca-light-dismiss>` with `.orca-drawer__header` (title + close), `.orca-drawer__body`, `.orca-drawer__footer`.",
         "Open with `data-orca-dialog-open=\"id\"`; `--left` for navigation. A click on the backdrop closes it."],
    classes=[".orca-drawer", ".orca-drawer--left", ".orca-drawer__header", ".orca-drawer__body", ".orca-drawer__footer"],
    laws=["L14", "postel", "fitts"],
    uses=["dialog", "form-actions"],
    examples=[("Details drawer", """<button class="orca-button" type="button" data-orca-dialog-open="dr-demo">Show video details</button>
<dialog class="orca-drawer" id="dr-demo" aria-labelledby="dr-demo-t" data-orca-light-dismiss>
  <div class="orca-drawer__header"><h2 class="orca-dialog-title" id="dr-demo-t">Entrance A</h2><button class="orca-icon-button" type="button" aria-label="Close" data-orca-dialog-close>{% icon "close" %}</button></div>
  <div class="orca-drawer__body"><dl class="orca-kv orca-kv--stacked"><div><dt>Status</dt><dd>Online</dd></div><div><dt>Today</dt><dd>4,812 visitors</dd></div></dl></div>
  <div class="orca-drawer__footer"><a class="orca-button orca-button--primary" href="#">Open video</a><button class="orca-button" type="button" data-orca-dialog-close>Close</button></div>
</dialog>""")],
    guide=["Drawer"], source="Tangerine",
))

add(Pattern(
    "top-actions-header", "Top actions header", C,
    "A thin row above a detail or form page with a back link on one side and page actions on the other.",
    why="Putting the way back and the actions on the same line saves height and keeps them at the top where people look first (Fitts's law, Practical UI B09).",
    when=["Detail and form pages reached from a list, especially on tablets and phones."],
    how=["`<div class=\"orca-top-actions\">` with a back link and `.orca-top-actions__end` (record actions)."],
    classes=[".orca-top-actions", ".orca-top-actions__end"],
    laws=["fitts", "B09"],
    uses=["back-link", "record-actions"],
    examples=[("Top actions", """<div class="orca-top-actions"><a class="orca-back-link" href="#">{% icon "chevron-left" size="xs" %}Back to videos</a><div class="orca-top-actions__end"><a class="orca-button orca-button--dense" href="#">{% icon "edit" %}Edit</a><button class="orca-icon-button orca-icon-button--dense orca-icon-button--outlined" type="button" aria-label="More actions">{% icon "more" %}</button></div></div>""")],
    guide=["Top actions header (back link + actions)"], source="Tangerine",
))

add(Pattern(
    "settings-panel", "Settings panel", C,
    "Grouped display preferences, theme and density, applied live. ORCA has one appearance; the project sets brand colours.",
    why="People adapt the interface to their eyes and work (Tesler's law); grouping preferences and applying them at once confirms each choice (Doherty threshold).",
    when=["A drawer or popover opened by the settings toggle; an account preferences page."],
    how=["`<div class=\"orca-settings-panel\">` of `<fieldset class=\"orca-settings-panel__group\">`: the theme toggle (Auto, Light, Dark, Paper), and switches for personal preferences such as reduced motion or compact tables.",
         "Apply at once and remember per person. Brand colour, accent and rounding are project settings (brand tokens), not personal: ORCA keeps one shape language."],
    classes=[".orca-settings-panel", ".orca-settings-panel__group"],
    laws=["tesler", "doherty", "R14"],
    uses=["theme-toggle", "toggle-field", "settings-toggle"],
    examples=[("Panel", """<div class="orca-settings-panel" style="max-width: 24rem">
  <fieldset class="orca-segmented orca-settings-panel__group" data-orca-theme-choice style="flex-direction: row"><legend>Theme</legend>
    <label class="orca-segmented__item"><input type="radio" name="sp-theme" value="auto" checked>Auto</label><label class="orca-segmented__item"><input type="radio" name="sp-theme" value="light">Light</label><label class="orca-segmented__item"><input type="radio" name="sp-theme" value="dark">Dark</label><label class="orca-segmented__item"><input type="radio" name="sp-theme" value="paper">Paper</label></fieldset>
  <fieldset class="orca-settings-panel__group"><legend>Tables</legend><label class="orca-switch"><input type="checkbox" role="switch"><span class="orca-switch__track"></span><span>Compact rows</span></label></fieldset>
</div>""")],
    guide=["Settings panel (appearance, theme, accent, rounding, card shadow)"], source="Tangerine",
))

add(Pattern(
    "filter-panel", "Filter panel", C,
    "Labelled groups of filters with a result count and Clear all: the content of the filter drawer.",
    why="Seeing all filters and the result count at once lets people narrow a list confidently (Miller's law, Doherty threshold); grouping keeps a long set of filters scannable.",
    when=["Inside the filter drawer of every page with filters."],
    avoid=["A side column of filters beside the list: page filters always open in the right drawer."],
    how=["`<div class=\"orca-drawer__body orca-filter-panel\">` inside the filter drawer's form (`method=\"get\"`).",
         "One `<fieldset class=\"orca-filter-panel__group\">` per dimension with checkbox lists; a search field that narrows the list goes first.",
         "Announce the number of results; the drawer footer's primary button repeats it ('Show 11 videos')."],
    classes=[".orca-filter-panel", ".orca-filter-panel__head", ".orca-filter-panel__group"],
    laws=["miller", "doherty", "S04"],
    uses=["choice-group", "panel-header", "search-field"],
    examples=[("Panel", """<form class="orca-filter-panel" method="get" aria-label="Filters" style="max-width: 15rem" onsubmit="return false">
  <div class="orca-filter-panel__head"><span class="orca-panel-title">Filters</span><button class="orca-button orca-button--link" type="reset">Clear all</button></div>
  <fieldset class="orca-filter-panel__group"><legend>Status</legend><div class="orca-choice-group__items">
    <label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Online <span class="orca-muted">11</span></label>
    <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Offline <span class="orca-muted">1</span></label></div></fieldset>
  <fieldset class="orca-filter-panel__group"><legend>Site</legend><div class="orca-choice-group__items">
    <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>North building</label><label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Warehouse</label></div></fieldset>
  <p class="orca-small orca-muted" role="status">11 videos match</p>
</form>""")],
    guide=["Filter panel"], source="Tangerine",
))

add(Pattern(
    "filter-drawer", "Filter drawer", C,
    "Page filters in a right drawer opened by a Filters button in the page actions, with Show results and Clear all.",
    why="Filters change what a page shows without taking people away from it: a right drawer keeps the results behind the scrim, keeps the page head "
        "to one Filters button (Hick's law, Practical UI S04: reveal secondary controls when needed), and opens from the same place on every page and "
        "every screen width, so people know where to look (Jakob's law). An explicit Show results avoids reloading on every tap (Doherty threshold).",
    when=["Every page with filters, at every screen width: lists, tables, galleries, boards and reports."],
    avoid=["A row of filter fields above the results or a side column of filters: both move here.",
           "The Filters button in the list header or toolbar: it belongs to the page actions."],
    how=["The Filters button (filter icon, number of applied filters) is in the page actions: `{% block page_actions %}`, `.orca-page-head__actions`. "
         "It has `data-orca-dialog-open=\"filters\"`; put it before the primary action.",
         "`<dialog class=\"orca-drawer\" id=\"filters\" data-orca-light-dismiss>` (right side) holding a GET form: header with title and Close, "
         "`.orca-drawer__body.orca-filter-panel`, footer with 'Show 11 videos' (primary, the count updates live) and 'Clear all'.",
         "Above the results, the `filter-bar` lists the applied filters as removable tags."],
    classes=[".orca-drawer", ".orca-filter-panel"],
    laws=["S04", "hick", "jakob", "doherty"],
    uses=["filter-button", "dialog", "filter-panel"],
    examples=[("Filters from the page actions", """<div class="orca-page-head"><div class="orca-page-head__text"><h1 class="orca-page-title">Videos</h1><p class="orca-page-subtitle">128 videos in the library.</p></div>
  <div class="orca-page-head__actions"><button class="orca-button" type="button" data-orca-dialog-open="fd-demo">{% icon "filter" %}Filters<span class="orca-count orca-count--accent" aria-hidden="true">1</span><span class="orca-sr-only">, 1 active</span></button><a class="orca-button orca-button--primary" href="#">{% icon "plus" %}Add video</a></div></div>
<dialog class="orca-drawer" id="fd-demo" aria-labelledby="fd-demo-t" data-orca-light-dismiss><form method="dialog" style="display: contents">
  <div class="orca-drawer__header"><h2 class="orca-dialog-title" id="fd-demo-t">Filters</h2><button class="orca-icon-button" type="button" aria-label="Close" data-orca-dialog-close>{% icon "close" %}</button></div>
  <div class="orca-drawer__body orca-filter-panel"><fieldset class="orca-filter-panel__group"><legend>Status</legend><div class="orca-choice-group__items"><label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Published</label><label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Draft</label></div></fieldset></div>
  <div class="orca-drawer__footer"><button class="orca-button orca-button--primary" type="submit" value="apply">Show 11 videos</button><button class="orca-button orca-button--ghost" type="reset">Clear all</button></div>
</form></dialog>""")],
    guide=["Filter drawer"], source="Tangerine",
))
