from ..registry import add, category
from . import Pattern

C = category(
    "page-frame", "Page frame",
    "The parts every page sits in: headers, top bar, sidebar, footer, page head, messages, drawers and filter panels.",
    level="pattern",
)

add(Pattern(
    "site-header", "Header", C,
    "The public site header: logo, a few section links and one or two actions, sticky at the top.",
    why="People expect the logo top-left (home) and the main sections beside it on every site (Jakob's law); one primary action keeps the next step obvious (Hick's law).",
    when=["Public and marketing pages, documentation sites, sign-in pages."],
    avoid=["Inside the application: use the top bar."],
    how=["`<header class=\"orca-site-header\">` with the logo, `<nav aria-label=\"Main\"><ul class=\"orca-site-header__nav\">` and `.orca-site-header__actions`.",
         "At most 5 links; the current one gets `aria-current=\"page\"`. On phones the links wrap under the logo."],
    classes=[".orca-site-header", ".orca-site-header__nav", ".orca-site-header__actions"],
    laws=["jakob", "hick", "B03"],
    uses=["logo", "primary-navigation", "button"],
    examples=[("Header", """<header class="orca-site-header" style="position: static">
  {% orca_logo href="#" %}
  <nav aria-label="Main"><ul class="orca-site-header__nav"><li><a href="#" aria-current="page">Product</a></li><li><a href="#">Pricing</a></li><li><a href="#">Docs</a></li></ul></nav>
  <div class="orca-site-header__actions"><a class="orca-button orca-button--ghost" href="#">Sign in</a><a class="orca-button orca-button--brand" href="#">Start free trial</a></div>
</header>""")],
    guide=["Header"],
))

add(Pattern(
    "top-bar", "Top bar", C,
    "The application bar: menu button, logo, main sections, search and the user's tools.",
    why="A persistent bar in the expected place anchors every page of an application (Jakob's law); dense controls keep it to 56px so content stays in view (Practical UI F03).",
    when=["Every authenticated page of an application."],
    how=["`<header class=\"orca-topbar\">` with `.orca-topbar__start` (menu or sidebar toggle, logo, primary navigation) and `.orca-topbar__end` (search, utility navigation).",
         "`--brand` paints it in the brand colour darkened by 30% with white text (the wise_people_analyzer bar); check the brand colour reads at 4.5:1 there.",
         "Below 1036px the navigation and search move into the drawer; the menu button opens it."],
    classes=[".orca-topbar", ".orca-topbar__start", ".orca-topbar__end", ".orca-topbar--brand"],
    laws=["jakob", "F03", "fitts"],
    uses=["logo", "primary-navigation", "utility-navigation", "search-input", "icon-button"],
    examples=[("Default and brand", """<div class="orca-stack" style="gap: var(--orca-space-16)">
<header class="orca-topbar" style="position: static">
  <div class="orca-topbar__start"><button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Open menu">{% icon "menu" %}</button>{% orca_logo href="#" %}
    <nav aria-label="Main"><ul class="orca-topnav"><li><a href="#" aria-current="page">Dashboard</a></li><li><a href="#">Cameras</a></li><li><a href="#">Reports</a></li></ul></nav></div>
  <div class="orca-topbar__end"><div class="orca-search">{% icon "search" %}<input class="orca-input orca-input--dense" type="search" placeholder="Search" aria-label="Search"></div>
    <a class="orca-icon-button orca-has-count" href="#" aria-label="Notifications, 3 unread">{% icon "notifications" %}<span class="orca-count" aria-hidden="true">3</span></a>
    <button class="orca-user-chip" type="button"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span class="orca-user-chip__text"><span class="orca-user-chip__name">Ada Lovelace</span></span></button></div>
</header>
<header class="orca-topbar orca-topbar--brand" style="position: static">
  <div class="orca-topbar__start"><button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Open menu">{% icon "menu" %}</button>{% orca_logo href="#" %}</div>
  <div class="orca-topbar__end"><a class="orca-icon-button" href="#" aria-label="Help">{% icon "help" %}</a><button class="orca-user-chip" type="button"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span class="orca-user-chip__text"><span class="orca-user-chip__name">Ada Lovelace</span><span class="orca-user-chip__role">Administrator</span></span></button></div>
</header></div>""")],
    guide=["Top bar"], source="Tangerine",
))

add(Pattern(
    "sidebar", "Sidebar", C,
    "The application's side navigation: grouped section links, collapsible to an icon rail, remembered per person.",
    why="Products with many sections need a persistent, scannable list; groups chunk it (Miller's law) and collapsing gives space back to dense screens (Tesler's law: the person decides).",
    when=["Applications with more than about 5 sections."],
    how=["`<div class=\"orca-app\">` holds `<nav class=\"orca-sidebar\" id=… aria-label=\"Sections\">` and `<main class=\"orca-app__main\">`.",
         "Sections: `.orca-sidebar__section` with an optional `.orca-sidebar__label` and side links; `.orca-sidebar__foot` holds the collapse toggle (`data-orca-sidebar-toggle aria-controls=…`).",
         "Collapsed (`data-collapsed=\"true\"`): labels become visually hidden but stay readable by screen readers; the rail keeps icons.",
         "Below 620px the sidebar hides; put the same links in a drawer opened from the top bar."],
    classes=[".orca-app", ".orca-app__main", ".orca-sidebar", ".orca-sidebar__section", ".orca-sidebar__label", ".orca-sidebar__foot"],
    laws=["miller", "tesler", "jakob"],
    uses=["sidebar-link", "nav-tree", "icon-button"],
    examples=[("Sidebar with collapse", """<div class="orca-app" style="min-height: 22rem; border: var(--orca-border-width) solid var(--orca-border)">
  <nav class="orca-sidebar" id="sb-demo" aria-label="Sections" data-collapsed="false">
    <div class="orca-sidebar__section"><ul class="orca-side-nav">
      <li><a class="orca-side-link" href="#" aria-current="page">{% icon "home" %}<span class="orca-side-link__label">Dashboard</span></a></li>
      <li><a class="orca-side-link" href="#">{% icon "snapshot" %}<span class="orca-side-link__label">Cameras</span><span class="orca-count orca-count--neutral">12</span></a></li>
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
    uses=["text-link", "logo", "small-text"],
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
    "The top of a page's content: breadcrumbs or back link, title, subtitle, meta and the page's actions.",
    why="One consistent head answers 'where am I, what is this, what can I do here' before anything else (Jakob's law); one primary action keeps the priority clear (Practical UI B03).",
    when=["The top of every application page."],
    how=["`<div class=\"orca-page-head\">` with `.orca-page-head__text` (breadcrumbs or back link, `h1.orca-page-title`, `.orca-page-subtitle`, `.orca-page-head__meta`) and `.orca-page-head__actions`.",
         "Actions: secondary buttons first, the primary (or the create button) last; on phones they stretch full width."],
    classes=[".orca-page-head", ".orca-page-head__text", ".orca-page-head__meta", ".orca-page-head__actions"],
    laws=["jakob", "B03", "L03"],
    uses=["page-title", "page-subtitle", "breadcrumbs", "button", "create-button"],
    examples=[("Page head", """<div class="orca-page-head">
  <div class="orca-page-head__text"><nav class="orca-breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="#">Sites</a></li><li><span aria-current="page">North building</span></li></ol></nav>
    <h1 class="orca-page-title">Cameras</h1><p class="orca-page-subtitle">Every camera counting at North building.</p>
    <p class="orca-page-head__meta"><span class="orca-status"><span class="orca-dot orca-dot--positive"></span>11 online</span><span class="orca-status"><span class="orca-dot orca-dot--negative"></span>1 offline</span></p></div>
  <div class="orca-page-head__actions"><button class="orca-button" type="button">{% icon "upload" %}Export</button><a class="orca-button orca-button--primary orca-create orca-create--static" href="#">{% icon "plus" %}Add camera</a></div>
</div>""")],
    guide=["Page head"], source="Tangerine",
))

add(Pattern(
    "messages-region", "Messages region", C,
    "The place under the page head where results of the last action appear, announced politely.",
    why="Results always in the same place are found at once (Jakob's law); a live region announces them to screen-reader users (Postel's law).",
    when=["Every page, in the base template, between the page head and the content."],
    how=["`<div class=\"orca-messages-region\" aria-live=\"polite\">{% templatetag openblock %} orca_messages {% templatetag closeblock %}</div>`; errors inside use `role=\"alert\"`.",
         "Toasts float elsewhere; this region holds messages that must stay until read."],
    classes=[".orca-messages-region", ".orca-messages"],
    laws=["jakob", "postel", "peak-end"],
    uses=["flash-message", "alert"],
    examples=[("Region", """<div class="orca-messages-region" aria-live="polite"><div class="orca-messages">
  <div class="orca-alert orca-alert--positive" role="status">{% status_icon "positive" %}<p class="orca-alert__body">Camera “Gate 1” added. Draw its zones next.</p><button class="orca-icon-button orca-icon-button--dense orca-alert__close" type="button" aria-label="Dismiss message" data-orca-dismiss>{% icon "close" %}</button></div>
</div></div>""")],
    guide=["Messages region"], source="Tangerine",
))

add(Pattern(
    "drawer", "Drawer", C,
    "A panel that slides over the page from one edge, built on the native dialog.",
    why="A drawer keeps the page in view behind it, for tasks that refer to the page (Practical UI L14); the native dialog traps focus and closes with Escape (Postel's law).",
    when=["Navigation on phones, filters, details of a selected row, quick settings."],
    avoid=["Long forms: use a page."],
    how=["`<dialog class=\"orca-drawer\" id=… aria-labelledby=… data-orca-light-dismiss>` with `.orca-drawer__header` (title + close), `.orca-drawer__body`, `.orca-drawer__footer`.",
         "Open with `data-orca-dialog-open=\"id\"`; `--left` for navigation. A click on the backdrop closes it."],
    classes=[".orca-drawer", ".orca-drawer--left", ".orca-drawer__header", ".orca-drawer__body", ".orca-drawer__footer"],
    laws=["L14", "postel", "fitts"],
    uses=["drawer-backdrop", "dialog-title", "icon-button", "button"],
    examples=[("Details drawer", """<button class="orca-button" type="button" data-orca-dialog-open="dr-demo">Show camera details</button>
<dialog class="orca-drawer" id="dr-demo" aria-labelledby="dr-demo-t" data-orca-light-dismiss>
  <div class="orca-drawer__header"><h2 class="orca-dialog-title" id="dr-demo-t">Entrance A</h2><button class="orca-icon-button" type="button" aria-label="Close" data-orca-dialog-close>{% icon "close" %}</button></div>
  <div class="orca-drawer__body"><dl class="orca-kv orca-kv--stacked"><div><dt>Status</dt><dd>Online</dd></div><div><dt>Today</dt><dd>4,812 visitors</dd></div></dl></div>
  <div class="orca-drawer__footer"><a class="orca-button orca-button--primary" href="#">Open camera</a><button class="orca-button" type="button" data-orca-dialog-close>Close</button></div>
</dialog>""")],
    guide=["Drawer"], source="Tangerine",
))

add(Pattern(
    "top-actions-header", "Top actions header", C,
    "A thin row above a detail or form page: back link on one side, the page's actions on the other.",
    why="Putting the way back and the actions on the same line saves height and keeps them at the top where people look first (Fitts's law, Practical UI B09).",
    when=["Detail and form pages reached from a list, especially on tablets and phones."],
    how=["`<div class=\"orca-top-actions\">` with a back link and `.orca-top-actions__end` (record actions)."],
    classes=[".orca-top-actions", ".orca-top-actions__end"],
    laws=["fitts", "B09"],
    uses=["back-link", "record-actions"],
    examples=[("Top actions", """<div class="orca-top-actions"><a class="orca-back-link" href="#">{% icon "chevron-left" size="xs" %}Back to cameras</a><div class="orca-top-actions__end"><a class="orca-button orca-button--dense" href="#">{% icon "edit" %}Edit</a><button class="orca-icon-button orca-icon-button--dense orca-icon-button--outlined" type="button" aria-label="More actions">{% icon "more" %}</button></div></div>""")],
    guide=["Top actions header (back link + actions)"], source="Tangerine",
))

add(Pattern(
    "settings-panel", "Settings panel", C,
    "Display preferences in groups: theme and density, with a live result. ORCA has one appearance (Tangerine) and brand colours set by the project.",
    why="People adapt the interface to their eyes and work (Tesler's law); grouping preferences and applying them at once confirms each choice (Doherty threshold).",
    when=["A drawer or popover opened by the settings toggle; an account preferences page."],
    how=["`<div class=\"orca-settings-panel\">` of `<fieldset class=\"orca-settings-panel__group\">`: the theme toggle (Auto, Light, Dark, Paper), and switches for personal preferences such as reduced motion or compact tables.",
         "Apply immediately and remember per person. Brand colour, accent and rounding are project settings (brand tokens), not personal ones: ORCA keeps one shape language."],
    classes=[".orca-settings-panel", ".orca-settings-panel__group"],
    laws=["tesler", "doherty", "R14"],
    uses=["theme-toggle", "switch", "settings-toggle"],
    examples=[("Panel", """<div class="orca-settings-panel" style="max-width: 24rem">
  <fieldset class="orca-segmented orca-settings-panel__group" data-orca-theme-choice style="flex-direction: row"><legend>Theme</legend>
    <label class="orca-segmented__item"><input type="radio" name="sp-theme" value="auto" checked>Auto</label><label class="orca-segmented__item"><input type="radio" name="sp-theme" value="light">Light</label><label class="orca-segmented__item"><input type="radio" name="sp-theme" value="dark">Dark</label><label class="orca-segmented__item"><input type="radio" name="sp-theme" value="paper">Paper</label></fieldset>
  <fieldset class="orca-settings-panel__group"><legend>Tables</legend><label class="orca-switch"><input type="checkbox" role="switch"><span class="orca-switch__track"></span><span>Compact rows</span></label></fieldset>
</div>""")],
    guide=["Settings panel (appearance, theme, accent, rounding, card shadow)"], source="Tangerine",
))

add(Pattern(
    "filter-panel", "Filter panel", C,
    "Filters in labelled groups beside a list, with the number of results and Clear all.",
    why="Seeing all filters and the result count at once lets people narrow a list confidently (Miller's law, Doherty threshold); grouping keeps a long set of filters scannable.",
    when=["Lists and catalogues on wide screens with several filter dimensions."],
    how=["`<div class=\"orca-with-filters\">` holding `<form class=\"orca-filter-panel\" method=\"get\" aria-label=\"Filters\">` and the list.",
         "Head: 'Filters' and a Clear all link; then `<fieldset class=\"orca-filter-panel__group\">` per dimension with checkbox lists; apply on change (htmx or `data-orca-autosubmit`) and announce the count.",
         "Below 1036px the panel hides; the same form goes in the filter drawer."],
    classes=[".orca-with-filters", ".orca-filter-panel", ".orca-filter-panel__head", ".orca-filter-panel__group"],
    laws=["miller", "doherty", "S04"],
    uses=["choice-group", "checkbox", "link-action", "search-field"],
    examples=[("Panel", """<form class="orca-filter-panel" method="get" aria-label="Filters" style="max-width: 15rem" onsubmit="return false">
  <div class="orca-filter-panel__head"><span class="orca-panel-title">Filters</span><button class="orca-button orca-button--link" type="reset">Clear all</button></div>
  <fieldset class="orca-filter-panel__group"><legend>Status</legend><div class="orca-choice-group__items">
    <label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Online <span class="orca-muted">11</span></label>
    <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Offline <span class="orca-muted">1</span></label></div></fieldset>
  <fieldset class="orca-filter-panel__group"><legend>Site</legend><div class="orca-choice-group__items">
    <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>North building</label><label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Warehouse</label></div></fieldset>
  <p class="orca-small orca-muted" role="status">11 cameras match</p>
</form>""")],
    guide=["Filter panel"], source="Tangerine",
))

add(Pattern(
    "filter-drawer", "Filter drawer", C,
    "The filter panel in a drawer, with Apply and Clear, for phones and narrow screens.",
    why="On small screens filters must not push the results away; a drawer shows them on demand (Practical UI S04) and an explicit Apply avoids reloading on every tap (Doherty threshold).",
    when=["Below 1036px, or whenever filters do not fit beside the list."],
    how=["A filter button (with the active count) opens a `<dialog class=\"orca-drawer\">` containing the filter panel form.",
         "Footer: 'Show 11 cameras' (primary, the count updates live) and 'Clear all'."],
    classes=[".orca-drawer", ".orca-filter-panel"],
    laws=["S04", "doherty", "fitts"],
    uses=["filter-button", "drawer-backdrop", "button"],
    examples=[("Drawer", """<button class="orca-button" type="button" data-orca-dialog-open="fd-demo">{% icon "filter" %}Filters<span class="orca-count orca-count--accent" aria-hidden="true">1</span><span class="orca-sr-only">, 1 active</span></button>
<dialog class="orca-drawer" id="fd-demo" aria-labelledby="fd-demo-t" data-orca-light-dismiss><form method="dialog" style="display: contents">
  <div class="orca-drawer__header"><h2 class="orca-dialog-title" id="fd-demo-t">Filters</h2><button class="orca-icon-button" type="button" aria-label="Close" data-orca-dialog-close>{% icon "close" %}</button></div>
  <div class="orca-drawer__body orca-filter-panel"><fieldset class="orca-filter-panel__group"><legend>Status</legend><div class="orca-choice-group__items"><label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Online</label><label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Offline</label></div></fieldset></div>
  <div class="orca-drawer__footer"><button class="orca-button orca-button--primary" type="submit" value="apply">Show 11 cameras</button><button class="orca-button orca-button--ghost" type="reset">Clear all</button></div>
</form></dialog>""")],
    guide=["Filter drawer"], source="Tangerine",
))
