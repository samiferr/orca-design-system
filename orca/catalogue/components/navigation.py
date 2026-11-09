from ..registry import add, category
from . import Component

C = category(
    "navigation", "Navigation",
    "How people move between places and pages. The current location is always marked with aria-current and a shape, not only colour.",
    level="component",
)

add(Component(
    "primary-navigation", "Primary navigation", C,
    "The top-bar links to the main sections of the product.",
    why="A short, always-visible set of sections in the familiar top position lets people know where they are and where they can go (Jakob's law); the 3px bar marks the current section without colour alone (C03).",
    when=["Products with 2 to about 6 top-level sections, in the top bar."],
    avoid=["More sections: use the sidebar."],
    how=["`<nav aria-label=\"Main\"><ul class=\"orca-topnav\">` with links; the current section's link gets `aria-current=\"page\"` (or `\"true\"` for a section).",
         "Labels are nouns people use: 'Videos', 'Reports'. Icons optional, never alone.",
         "Below 1036px move the links into the sidebar drawer (pattern level)."],
    classes=[".orca-topnav"],
    laws=["jakob", "C03", "hick"],
    uses=["text-link"],
    examples=[("Top-bar links", """<nav aria-label="Main"><ul class="orca-topnav" style="min-height: var(--orca-nav-height)">
  <li><a href="#" aria-current="page">Dashboard</a></li><li><a href="#">Videos</a></li><li><a href="#">Reports</a></li><li><a href="#">Alerts</a></li>
</ul></nav>""")],
    guide=["Primary navigation"],
))

add(Component(
    "utility-navigation", "Utility navigation", C,
    "Help, notifications and the user chip at the end of the top bar.",
    why="Account and help live in the top-right corner of almost every product (Jakob's law); grouping them separates personal tools from sections (Miller's law).",
    when=["The end of the top bar, in every authenticated page."],
    how=["`<ul class=\"orca-utility-nav\">` with icon buttons (each with `aria-label`; the notifications one with a count) and the user chip.",
         "Use dense icon buttons on desktop; they grow to 44px on touch."],
    classes=[".orca-utility-nav"],
    laws=["jakob", "miller"],
    uses=["icon-button", "count-badge", "avatar"],
    related=["user-chip"],
    examples=[("Utility links", """<ul class="orca-utility-nav">
  <li><a class="orca-icon-button" href="#" aria-label="Help">{% icon "help" %}</a></li>
  <li><a class="orca-icon-button orca-has-count" href="#" aria-label="Notifications, 3 unread">{% icon "notifications" %}<span class="orca-count" aria-hidden="true">3</span></a></li>
  <li><button class="orca-user-chip" type="button" aria-haspopup="menu" aria-expanded="false"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span class="orca-user-chip__text"><span class="orca-user-chip__name">Ada Lovelace</span><span class="orca-user-chip__role">Administrator</span></span></button></li>
</ul>""")],
    guide=["Utility navigation"],
))

add(Component(
    "sidebar-link", "Sidebar link", C,
    "One destination in the side navigation: icon, label and an optional count.",
    why="A consistent row (icon, label, count) is scanned quickly and its full width is the target (Fitts's law); the current page gets a fill and a 3px bar.",
    when=["Every item of the sidebar."],
    how=["`<a class=\"orca-side-link\" href=…>{% templatetag openblock %} icon … {% templatetag closeblock %}<span class=\"orca-side-link__label\">Videos</span><span class=\"orca-count orca-count--neutral\">12</span></a>` inside `<ul class=\"orca-side-nav\">`.",
         "`aria-current=\"page\"` on the current link; `--l2` for a nested link.",
         "Labels never wrap; a long one is cut with an ellipsis and has a `title`."],
    classes=[".orca-side-nav", ".orca-side-link", ".orca-side-link__label", ".orca-side-link--l2"],
    laws=["fitts", "C03", "jakob"],
    uses=["icon", "count-badge"],
    examples=[("Side links", """<nav aria-label="Sections" style="max-width: 15rem; background: var(--orca-bg-alt)"><ul class="orca-side-nav">
  <li><a class="orca-side-link" href="#">{% icon "home" %}<span class="orca-side-link__label">Dashboard</span></a></li>
  <li><a class="orca-side-link" href="#" aria-current="page">{% icon "snapshot" %}<span class="orca-side-link__label">Videos</span><span class="orca-count orca-count--neutral">12</span></a></li>
  <li><a class="orca-side-link orca-side-link--l2" href="#"><span class="orca-side-link__label">Media servers</span></a></li>
  <li><a class="orca-side-link" href="#">{% icon "notifications" %}<span class="orca-side-link__label">Alerts</span><span class="orca-count">3</span></a></li>
</ul></nav>""")],
    guide=["Sidebar link"], source="Tangerine",
))

add(Component(
    "breadcrumbs", "Breadcrumbs", C,
    "The path from the top of the hierarchy to the current page.",
    why="Breadcrumbs show where a page sits and offer one-click routes upward (Jakob's law); the list structure is announced as 'list, 3 items'.",
    when=["Pages two or more levels deep in a hierarchy (Site › Building › Video)."],
    avoid=["Flat products, or as a substitute for a back link on a linear flow."],
    how=["`<nav class=\"orca-breadcrumbs\" aria-label=\"Breadcrumb\"><ol>` with links, the last item a `<span aria-current=\"page\">`.",
         "Separators come from CSS and mirror in right-to-left languages.",
         "On phones, show only the parent as a back link if space is short."],
    classes=[".orca-breadcrumbs"],
    laws=["jakob", "postel"],
    uses=["text-link", "chevron-separator"],
    examples=[("Breadcrumbs", """<nav class="orca-breadcrumbs" aria-label="Breadcrumb"><ol>
  <li><a href="#">Sites</a></li><li><a href="#">North building</a></li><li><span aria-current="page">Entrance A</span></li>
</ol></nav>""")],
    guide=["Breadcrumbs"],
))

add(Component(
    "pagination", "Pagination", C,
    "Previous, page numbers with gaps, next, and a summary of what is shown.",
    why="Numbered pages tell people how much there is and let them jump (Miller's law); gaps keep the control short (Hick's law); big targets avoid mis-taps (Fitts's law).",
    when=["Lists and tables with more than one page of results."],
    avoid=["Feeds people read continuously: use 'Load more'."],
    how=["Django: `{% orca_pagination page_obj noun=\"videos\" %}` keeps the other query parameters (filters, sort).",
         "Markup: `<nav class=\"orca-pagination\" aria-label=\"Pages\"><ul>` of `.orca-page-link` links; current with `aria-current=\"page\"`; disabled ends with `aria-disabled=\"true\"`; gaps are `.orca-page-gap`.",
         "Each link is a page-link: number links carry `aria-label=\"Page 7\"`."],
    classes=[".orca-pagination", ".orca-page-link"],
    laws=["miller", "hick", "fitts"],
    uses=["pagination-gap", "icon"],
    examples=[("Pagination", """<nav class="orca-pagination" aria-label="Pages"><ul>
  <li><a class="orca-page-link" href="#" rel="prev">{% icon "chevron-left" %}<span>Previous</span></a></li>
  <li><a class="orca-page-link" href="#" aria-label="Page 1">1</a></li><li><span class="orca-page-gap" aria-hidden="true">…</span></li>
  <li><a class="orca-page-link" href="#" aria-label="Page 6">6</a></li><li><a class="orca-page-link" href="#" aria-current="page" aria-label="Page 7, current">7</a></li><li><a class="orca-page-link" href="#" aria-label="Page 8">8</a></li>
  <li><span class="orca-page-gap" aria-hidden="true">…</span></li><li><a class="orca-page-link" href="#" aria-label="Page 16">16</a></li>
  <li><a class="orca-page-link" href="#" rel="next"><span>Next</span>{% icon "chevron-right" %}</a></li>
</ul></nav>""")],
    guide=["Pagination", "Pagination link"],
    related=["pagination-summary", "table-pager"],
))

add(Component(
    "pagination-summary", "Pagination summary", C,
    "'Showing 121–140 of 312 videos': what part of the list is on screen.",
    why="A count anchors people in a long list and confirms filters worked (Miller's law, Peak–end rule).",
    when=["Under or above any paginated list, and alone when there is a single page."],
    how=["`<p class=\"orca-pagination-summary\">Showing 121–140 of 312 videos</p>`, with an en dash and grouping separators.",
         "Zero results: 'No videos match these filters' and an empty state below."],
    classes=[".orca-pagination-summary"],
    laws=["miller", "W11"],
    uses=["tabular-number"],
    examples=[("Summary", """<p class="orca-pagination-summary">Showing 121–140 of 312 videos</p>""")],
    guide=["Pagination summary"],
))

add(Component(
    "table-pager", "Table pager", C,
    "A compact pager under a table: rows per page, the range shown, previous and next.",
    why="Dense data screens need paging in a small space near the rows (Practical UI L14) and a choice of page size for different tasks (Tesler's law).",
    when=["The footer of data tables and table cards."],
    how=["`<div class=\"orca-table-pager\">`: a label with a dense select of sizes (20, 50, 100), the range summary, and `.orca-table-pager__nav` with two icon buttons.",
         "Disable previous on the first page and next on the last; keep sizes small to keep pages fast."],
    classes=[".orca-table-pager", ".orca-table-pager__nav"],
    laws=["L14", "tesler", "doherty"],
    uses=["select", "icon-button", "pagination-summary"],
    examples=[("Pager", """<div class="orca-table-pager" style="border: var(--orca-border-width) solid var(--orca-border)">
  <label>Rows per page <select class="orca-select orca-select--dense"><option>20</option><option selected>50</option><option>100</option></select></label>
  <span class="orca-num">51–100 of 312</span>
  <span class="orca-table-pager__nav"><a class="orca-icon-button orca-icon-button--dense" href="#" aria-label="Previous page">{% icon "chevron-left" %}</a><a class="orca-icon-button orca-icon-button--dense" href="#" aria-label="Next page">{% icon "chevron-right" %}</a></span>
</div>""")],
    guide=["Table pager"],
))

add(Component(
    "tab-bar", "Tab bar", C,
    "Tabs that switch between views of the same object, in place or by page.",
    why="Tabs split related content into chunks people can switch between without losing context (Miller's law); the convention is universal (Jakob's law).",
    when=["Two to about seven views of one thing: Overview, Zones, Recordings."],
    avoid=["Steps of a process: use steps.", "Unrelated destinations: use navigation."],
    how=["In-page: `<div class=\"orca-tabs\"><div class=\"orca-tabs__list\" role=\"tablist\" data-orca-tabs aria-label=…>` of `<button class=\"orca-tab\" role=\"tab\" aria-selected aria-controls>`; panels `role=\"tabpanel\"` with `hidden`.",
         "By page (server-rendered): `<nav class=\"orca-tabs__list\">` of `<a class=\"orca-tab\" aria-current=\"page\">` links.",
         "orca.js adds arrow keys, Home and End. On narrow screens the list scrolls sideways."],
    classes=[".orca-tabs", ".orca-tabs__list", ".orca-tab", ".orca-tabs__panel", ".orca-tabs--brand"],
    laws=["miller", "jakob"],
    uses=["focus-ring", "count-badge", "text-link"],
    examples=[("In-page tabs", """<div class="orca-tabs">
  <div class="orca-tabs__list" role="tablist" aria-label="Video" data-orca-tabs>
    <button class="orca-tab" role="tab" type="button" id="tb-1" aria-controls="tp-1" aria-selected="true">Overview</button>
    <button class="orca-tab" role="tab" type="button" id="tb-2" aria-controls="tp-2" aria-selected="false">Zones</button>
    <button class="orca-tab" role="tab" type="button" id="tb-3" aria-controls="tp-3" aria-selected="false">Recordings</button>
  </div>
  <div class="orca-tabs__panel" role="tabpanel" id="tp-1" aria-labelledby="tb-1" tabindex="0"><p class="orca-p">Counting since 3 March. 12,480 people this week.</p></div>
  <div class="orca-tabs__panel" role="tabpanel" id="tp-2" aria-labelledby="tb-2" tabindex="0" hidden><p class="orca-p">2 zones: Door line, Staff area.</p></div>
  <div class="orca-tabs__panel" role="tabpanel" id="tp-3" aria-labelledby="tb-3" tabindex="0" hidden><p class="orca-p">No recordings in the last 24 hours.</p></div>
</div>""")],
    guide=["Tab bar"], source="Tangerine",
    related=["child-tabs"],
))

add(Component(
    "child-tabs", "Child tabs (with counts)", C,
    "Page tabs on a parent record, one per kind of child, each showing how many there are.",
    why="Counts tell people where the content is before they click (Practical UI S06) and turn empty tabs into information instead of a surprise.",
    when=["A parent record's detail page with lists of children (a site's videos, zones, users)."],
    how=["`<nav class=\"orca-tabs__list\" aria-label=…>` of `<a class=\"orca-tab\">Videos <span class=\"orca-count orca-count--neutral\">12</span></a>`; current tab `aria-current=\"page\"`.",
         "Keep the parent summary above the tabs so context stays visible."],
    classes=[".orca-tabs__list", ".orca-tab"],
    laws=["S06", "miller"],
    uses=["count-badge"],
    related=["tab-bar"],
    examples=[("Child tabs", """<nav class="orca-tabs__list" aria-label="North building">
  <a class="orca-tab" href="#">Overview</a>
  <a class="orca-tab" href="#" aria-current="page">Videos <span class="orca-count orca-count--neutral">12</span></a>
  <a class="orca-tab" href="#">Zones <span class="orca-count orca-count--neutral">5</span></a>
  <a class="orca-tab" href="#">Users <span class="orca-count orca-count--neutral">0</span></a>
</nav>""")],
    guide=["Child tabs (with counts)"],
))

add(Component(
    "bottom-navigation", "Bottom navigation bar", C,
    "Three to five main sections as icon-and-label buttons fixed at the bottom of phone screens.",
    why="The bottom of a phone is in thumb reach (Fitts's law) and the pattern is familiar from mobile platforms (Jakob's law); labels keep icons unambiguous (Hick's law).",
    when=["Phone layouts of products with 3 to 5 main sections used often."],
    avoid=["Desktop, or more than five sections."],
    how=["`<nav class=\"orca-bottom-nav\" aria-label=\"Main\">` with links containing an icon and a short label; current link `aria-current=\"page\"`.",
         "Add bottom padding to the page so content is not hidden behind it (it includes the safe area).",
         "Show it below 620px only; on wider screens use the sidebar or top bar."],
    classes=[".orca-bottom-nav", ".orca-bottom-nav--static"],
    laws=["fitts", "jakob", "hick"],
    uses=["icon", "count-badge"],
    examples=[("Bottom bar (shown in place)", """<nav class="orca-bottom-nav orca-bottom-nav--static" aria-label="Main" style="max-width: 24rem">
  <a href="#" aria-current="page">{% icon "home" %}Home</a><a href="#">{% icon "snapshot" %}Videos</a><a href="#">{% icon "notifications" %}Alerts<span class="orca-count" aria-label="3 new">3</span></a><a href="#">{% icon "user" %}Profile</a>
</nav>""")],
    guide=["Bottom navigation bar"],
))

add(Component(
    "nav-tree", "Nav tree", C,
    "Collapsible sections of navigation links (tree leaves) for large hierarchies.",
    why="Grouping many destinations into named sections keeps a long navigation scannable (Miller's law) and shows only what is relevant (Practical UI S04).",
    when=["Sidebars and documentation with more than about 12 destinations in groups."],
    how=["`<nav aria-label=…><ul class=\"orca-nav-tree\">` with `<details>` sections: `<summary>` (chevron, name, optional count) and a `<ul>` of leaf links.",
         "Open the section that contains the current page; leaves use `aria-current=\"page\"`.",
         "Nest a second level of details for sub-sections; avoid a third."],
    classes=[".orca-nav-tree"],
    laws=["miller", "S04"],
    uses=["chevron", "count-badge"],
    examples=[("Tree", """<nav aria-label="Settings" style="max-width: 16rem"><ul class="orca-nav-tree">
  <li><details open><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>Organisation<span class="orca-count orca-count--neutral">3</span></summary>
    <ul><li><a href="#">Profile</a></li><li><a href="#" aria-current="page">Users</a></li><li><a href="#">Billing</a></li></ul></details></li>
  <li><details><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>Devices<span class="orca-count orca-count--neutral">2</span></summary>
    <ul><li><a href="#">Videos</a></li><li><a href="#">Media servers</a></li></ul></details></li>
</ul></nav>""")],
    guide=["Nav tree (collapsible sections)", "Tree leaf"],
))

add(Component(
    "back-link", "Back link", C,
    "A link to the previous level, above the page title.",
    why="A visible way back near the top keeps people oriented, especially on phones where breadcrumbs do not fit (Jakob's law, Practical UI B09).",
    when=["Detail and form pages reached from a list; steps of a flow."],
    how=["`<a class=\"orca-back-link\" href=…>{% templatetag openblock %} icon \"chevron-left\" {% templatetag closeblock %}Back to videos</a>` above the title.",
         "Name the destination ('Back to videos'), never just 'Back'. Link to the real parent, not `history.back()`, so it works from a shared link."],
    classes=[".orca-back-link"],
    laws=["jakob", "B09", "W14"],
    uses=["text-link", "icon"],
    examples=[("Back link", """<a class="orca-back-link" href="#">{% icon "chevron-left" size="xs" %}Back to videos</a>""")],
    guide=["Back link"],
))

add(Component(
    "view-toggle", "View toggle (cards, table)", C,
    "A segmented control switching a collection between cards and a table.",
    why="Cards suit browsing with images; tables suit comparing values. Letting people choose moves the decision to them (Tesler's law), and the segmented shape shows both options at once (Practical UI R11).",
    when=["Collections where both browsing and comparing are common."],
    how=["Links (server-rendered): `<nav class=\"orca-segmented\" aria-label=\"View\">` of `<a class=\"orca-segmented__item\" aria-current=\"page\">` with icon + label.",
         "In place: radios inside `<fieldset class=\"orca-segmented\">` labels.",
         "Remember the choice per user; default to cards on phones."],
    classes=[".orca-segmented", ".orca-segmented__item", ".orca-segmented--dense"],
    laws=["tesler", "R11"],
    uses=["button", "icon"],
    examples=[("View toggle", """<nav class="orca-segmented orca-segmented--dense" aria-label="View">
  <a class="orca-segmented__item" href="#" aria-current="page">{% icon "grid" %}Cards</a>
  <a class="orca-segmented__item" href="#">{% icon "list" %}Table</a>
</nav>""")],
    guide=["View toggle (cards, table)"],
))

add(Component(
    "settings-toggle", "Settings toggle", C,
    "An icon button that opens the display settings panel (theme, density).",
    why="Display preferences are needed rarely, so they sit behind one familiar icon (Hick's law, S04) that states its state with aria-expanded.",
    when=["Top bar or page head of products that offer display settings."],
    how=["`<button class=\"orca-icon-button\" type=\"button\" aria-label=\"Display settings\" aria-expanded=\"false\" aria-controls=\"panel-id\" data-orca-disclose>{% templatetag openblock %} icon \"sliders\" {% templatetag closeblock %}</button>`.",
         "The panel itself is a pattern (settings panel); it can contain the theme toggle."],
    classes=[".orca-icon-button"],
    laws=["hick", "S04"],
    uses=["icon-button"],
    related=["theme-toggle"],
    examples=[("Settings toggle", """<button class="orca-icon-button orca-icon-button--outlined" type="button" aria-label="Display settings" aria-expanded="false" aria-controls="st-panel" data-orca-disclose>{% icon "sliders" %}</button>
<div id="st-panel" hidden style="margin-top: var(--orca-space-8); padding: var(--orca-space-16); max-width: 22rem" class="orca-elevation-2">
  <fieldset class="orca-segmented" data-orca-theme-choice><legend class="orca-label">Theme</legend>
    <label class="orca-segmented__item"><input type="radio" name="st-theme" value="auto" checked>Auto</label><label class="orca-segmented__item"><input type="radio" name="st-theme" value="light">Light</label><label class="orca-segmented__item"><input type="radio" name="st-theme" value="dark">Dark</label>
  </fieldset>
</div>""")],
    guide=["Settings toggle"],
))

add(Component(
    "create-button", "Create button (floating on phones)", C,
    "The page's create action: a primary button in the page head that becomes a floating button on phones.",
    why="On desktop the create action belongs beside the title; on phones it must stay in thumb reach while scrolling (Fitts's law). One element serves both so the action is never duplicated.",
    when=["List pages with one create action (Add video, New report)."],
    how=["`<a class=\"orca-button orca-button--primary orca-create\" href=…>{% templatetag openblock %} icon \"plus\" {% templatetag closeblock %}Add video</a>` in the page head.",
         "Below 620px it floats at the bottom right (respecting safe areas); add 5rem of bottom padding to the page so it never covers the last row."],
    classes=[".orca-create"],
    laws=["fitts", "restorff", "B03"],
    uses=["button", "fab"],
    examples=[("Create button", """<a class="orca-button orca-button--primary orca-create orca-create--static" href="#">{% icon "plus" %}Add video</a>""")],
    guide=["Create button (floating on phones)"],
))
