"""Level 4: template slots, the named Django blocks every ORCA layout offers."""

from html import escape

from ..registry import add, category
from . import Template

C = category(
    "template-slots", "Template slots",
    "The named blocks that ORCA's layouts offer. A page fills slots instead of rewriting the layout. Each slot lists "
    "the layouts that have it and what goes in it.",
    level="template",
)

OB, CB = "{% templatetag openblock %}", "{% templatetag closeblock %}"
ALL = "every layout (from orca/layouts/base.html)"
APP = "the app shell and every template built on it (generic, parent-child and page-type templates)"


def code(text: str) -> str:
    """An example shown as code only (for slots that hold nothing visible)."""
    return f'<div class="orca-code-block"><pre><code>{escape(text)}</code></pre></div>'


def slot(eid, name, block, where, summary, why, how, example, laws, guide, when=None, live=True):
    body = f"{OB} block {block} {CB}{example}{OB} endblock {CB}"
    html = f"{{% block {block} %}}{example}{{% endblock %}}" if live else code(body)
    add(Template(eid, name, C, summary, why=why, when=when or [f"Pages built on {where}."],
                 how=[f"`{OB} block {block} {CB}…{OB} endblock {CB}` in a template that extends {where}."] + list(how),
                 laws=list(laws), uses=[], guide=list(guide), blocks=[block], examples=[(f"{{% block {block} %}}", html)], source="ORCA"))


slot("slot-title", "Title", "title", ALL,
     "The text of the browser tab, before ` · Brand`.",
     "The tab title is how people find a page among open tabs and in history, so it leads with what is specific to the page (Practical UI W04).",
     ["Defaults to `title` from the context; on detail pages, start with the record's name.", "`title_suffix` changes or removes ` · Brand`."],
     "Entrance A · Videos", ["W04"], ["Title"], live=False)
slot("slot-page-title", "Page title", "page_title", APP + ", auth and error layouts",
     "The page's one h1, in the page head.",
     "One h1 per page names it for everyone, including screen-reader users jumping by heading (Practical UI W04, F01).",
     ["Defaults to `title`. Keep it short: the record's name or the list's noun."],
     "Videos", ["W04", "F01"], ["Page title"])
slot("slot-page-subtitle", "Page subtitle", "page_subtitle", APP,
     "One sentence under the title: what the page is for or covers.",
     "A one-line subtitle answers 'am I in the right place?' before people read further (Practical UI W05).",
     ["Defaults to `subtitle` from the context; skip it when the title is enough."],
     '<p class="orca-page-subtitle">Every video from North building.</p>', ["W05"], ["Page subtitle"])
slot("slot-page-actions", "Page actions", "page_actions", APP,
     "The page's buttons at the end of the page head: one primary action, few others.",
     "Actions in the same place on every page are found without looking (Jakob's law); one primary keeps the main task obvious (Practical UI B03).",
     ["List and detail templates fill it from `list_actions` and `detail_actions`; override those instead."],
     '<div class="orca-row"><button class="orca-button" type="button">Export</button><a class="orca-button orca-button--primary" href="#">Add video</a></div>',
     ["jakob", "B03"], ["Page actions"])
slot("slot-breadcrumbs", "Breadcrumbs", "breadcrumbs", APP + " and the docs layout",
     "The trail of parent pages above the title.",
     "Breadcrumbs show where a page sits and give one-click ways up (Jakob's law), most useful on detail pages two or more levels deep.",
     ["Defaults to the `breadcrumbs` context list of `(label, url)`; OrcaPageMixin builds it for detail pages."],
     '<nav class="orca-breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="#">Videos</a></li><li><span aria-current="page">Entrance A</span></li></ol></nav>',
     ["jakob", "L05"], ["Breadcrumbs"])
slot("slot-content", "Content", "content", ALL,
     "The page's own content, inside the main landmark.",
     "Every page fills this one slot and leaves the frame alone, which keeps the frame identical everywhere (Jakob's law).",
     ["Wrap sections in a vertical stack; put two related panels in a two-column grid or split."],
     '<div class="orca-vstack orca-vstack--tight"><p class="orca-p">Your page content.</p></div>', ["jakob", "L09"], ["Content"])
slot("slot-scripts", "Scripts", "scripts", ALL,
     "Script tags at the end of the body, for scripts loaded on every page.",
     "Scripts at the end never block the first paint (Doherty threshold); one slot for site-wide scripts keeps them in one place.",
     ["Set it once in your project's own base template; use `extra_scripts` for one page."],
     '<script src="/static/app/site.js" defer></script>', ["doherty"], ["Scripts"], live=False)
slot("slot-head", "Head", "head", ALL,
     "ORCA's stylesheets, brand values, favicon and script (`orca_head`).",
     "Everything ORCA needs in the head comes from one tag, so a page cannot miss a stylesheet or the brand (Tesler's law).",
     ["Override only to pass options, and keep `orca_head` in it: `orca_head script=False`."],
     "{% templatetag openblock %} orca_head theme_restore=False {% templatetag closeblock %}", ["tesler"], ["Head"], live=False)
slot("slot-body-class", "Body class", "body_class", ALL,
     "Classes on the body element, for page-wide styling.",
     "A body class lets a page adjust its own layout without editing shared CSS (Practical UI F09: change behaviour in one place).",
     ["The app shell sets `orca-shell`; keep it when overriding: `orca-shell my-page`."],
     "orca-shell reports-page", ["F09"], ["Body class"], live=False)
slot("slot-sidebar", "Sidebar", "sidebar", APP + " and the docs layout",
     "The whole sidebar: navigation, extra content and the collapse toggle.",
     "Replacing the sidebar is rarely needed; its two inner slots cover most cases and keep collapse and the phone drawer working (Tesler's law).",
     ["Use an empty block for pages without navigation, such as a wizard or full-screen editor."],
     "", ["tesler", "jakob"], ["Sidebar"], live=False)
slot("slot-top-bar", "Top bar", "top_bar", APP + ", the marketing and docs layouts",
     "The bar at the top of the page: menu button, brand, top navigation and the user's controls.",
     "A persistent top bar anchors every page (Jakob's law); its inner slots (`brand`, `top_nav`, `top_bar_end`) cover most changes.",
     ["Fill `top_bar_end` for search, notifications and the user menu; replace the whole bar only for a different header."],
     '<div class="orca-row"><a class="orca-icon-button" href="#" aria-label="Notifications">{% icon "notifications" %}</a></div>', ["jakob"], ["Top bar"])
slot("slot-brand", "Brand", "brand", APP + ", auth, error, marketing and docs layouts",
     "The logo or wordmark, from `settings.ORCA['BRAND']`.",
     "The brand in the same place on every page confirms where people are (Jakob's law); it comes from settings so it is never hard-coded.",
     ["Defaults to `orca_logo`; override only to link it elsewhere: `orca_logo href=\"/dashboard/\"`."],
     '{% orca_logo href="#" %}', ["jakob", "C08"], ["Brand"])
slot("slot-sidebar-extra", "Sidebar extra", "sidebar_extra", APP + " and the docs layout",
     "Content under the sidebar navigation: a site switcher, plan meter or help link.",
     "Secondary content stays out of the navigation list so the list stays scannable (Miller's law).",
     ["Keep it short; it is hidden when the sidebar collapses to the rail."],
     '<div class="orca-sidebar__section"><p class="orca-sidebar__label">Site</p><p class="orca-small" style="padding: 0 var(--orca-space-16)">North building</p></div>', ["miller"], ["Sidebar extra"])
slot("slot-sidebar-nav", "Sidebar navigation", "sidebar_nav", APP + " and the docs layout",
     "The navigation sections of the sidebar.",
     "Sections with labels chunk navigation (Miller's law); rendering it from the `nav` context keeps the current page marked correctly on every page.",
     ["Prefer the `nav` context (a list of sections with items); override the block for a nav tree."],
     '<div class="orca-sidebar__section"><ul class="orca-side-nav"><li><a class="orca-side-link" href="#" aria-current="page">{% icon "home" %}<span class="orca-side-link__label">Dashboard</span></a></li></ul></div>',
     ["miller", "jakob"], ["Sidebar navigation"])
slot("slot-filter-panel", "Filter panel", "filter_panel", "the generic list, planning board and simple data page templates",
     "A right drawer for filters, opened by the Filters button in the page actions.",
     "Every page opens its filters from the same place, a Filters button in the page actions, so people never hunt for them (Jakob's law, Practical UI S04).",
     ["Pass a GET `filter_form` and the template renders it; override the block for custom filters."],
     '<form class="orca-filter-panel" method="get" aria-label="Filters" onsubmit="return false"><div class="orca-filter-panel__head"><span class="orca-panel-title">Filters</span></div><fieldset class="orca-filter-panel__group"><legend>Status</legend><label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Online</label></fieldset></form>',
     ["L14", "S04"], ["Filter panel"])
slot("slot-body", "Body", "body", ALL,
     "Everything inside the body element except the skip link, modal and scripts.",
     "Layouts own this slot; a page that replaces it loses the shell (Tesler's law), so only new layouts override it.",
     ["Override it only in your own layout that extends `orca/layouts/base.html`."],
     "<main id=\"main\" tabindex=\"-1\">…</main>", ["tesler"], ["Body"], live=False)
slot("slot-modal", "Modal", "modal", ALL,
     "Dialogs and drawers, placed after the page so they open above it.",
     "Dialogs outside the main content avoid clipping and stacking problems and are found by assistive technology in one place (Practical UI L05).",
     ["Put `<dialog>` elements here and open them with `data-orca-dialog-open`."],
     '<button class="orca-button" type="button" data-orca-dialog-open="slot-dlg">Open the dialog</button><dialog class="orca-dialog" id="slot-dlg" aria-labelledby="slot-dlg-t"><h2 class="orca-dialog-title" id="slot-dlg-t">Dialog title</h2><p class="orca-p">Dialog text.</p><div class="orca-dialog__footer"><button class="orca-button" type="button" data-orca-dialog-close>Close</button></div></dialog>',
     ["L05"], ["Modal"])
slot("slot-footer", "Footer", "footer", APP + ", auth, marketing and docs layouts",
     "Legal and help links on public pages, a version line in applications.",
     "People look for legal and help links at the bottom (Jakob's law).",
     ["The marketing layout fills it from `footer_cols`; in the app shell it sits at the end of the main column."],
     '<p class="orca-small orca-muted">Version 0.4.0 · <a class="orca-link" href="#">Help</a></p>', ["jakob"], ["Footer"])
slot("slot-extra-head", "Extra head", "extra_head", ALL,
     "Page-specific head content: a stylesheet, meta tags, preloads.",
     "Keeping page additions in their own slot means the shared head is never copied (and never drifts) (Practical UI F09).",
     ["Use it for one page's CSS or meta; redefine only the brand tokens."],
     '<meta name="robots" content="noindex">', ["F09"], ["Extra head"], live=False)
slot("slot-extra-scripts", "Extra scripts", "extra_scripts", ALL,
     "One page's scripts, after the site-wide ones.",
     "A page's script loads only where it is needed, keeping other pages fast (Doherty threshold).",
     ["Add `defer`; try ORCA's data attributes before writing script."],
     '<script src="/static/app/reports.js" defer></script>', ["doherty"], ["Extra scripts"], live=False)
slot("slot-theme-bootstrap", "Theme bootstrap", "theme_bootstrap", ALL,
     "The inline script that applies the reader's saved theme before the page paints.",
     "Without it, a reader who chose dark sees a white flash on every page (Aesthetic–usability effect).",
     ["Defaults to `orca_theme_bootstrap`, which outputs nothing when settings fix the theme; empty it if your CSP forbids inline scripts and you fix the theme."],
     "{% templatetag openblock %} orca_theme_bootstrap {% templatetag closeblock %}", ["aesthetic"], ["Theme bootstrap"], live=False)
slot("slot-list-actions", "List actions", "list_actions", "the generic list, parent-child list and simple data page templates",
     "The buttons of a list page: Add first, then exports or bulk tools.",
     "The create button in the same place on every list is found without looking (Jakob's law); one primary keeps it obvious (Practical UI B03).",
     ["Defaults to 'Add <model>' when `create_url` is set."],
     '<a class="orca-button orca-button--primary orca-create" href="#">{% icon "plus" %}Add video</a>', ["jakob", "B03"], ["List actions"])
slot("slot-detail-actions", "Detail actions", "detail_actions", "the generic detail, parent and parent-child detail templates",
     "The buttons of a record: Edit, then other actions, Delete last and quieter.",
     "Edit and Delete in the same place on every record (Jakob's law), Delete apart and outlined so it is not hit by mistake (Practical UI B13).",
     ["Defaults to Edit and Delete when `update_url` and `delete_url` are set."],
     '<div class="orca-row"><a class="orca-button" href="#">{% icon "edit" %}Edit</a><a class="orca-button orca-button--outline-danger" href="#">Delete</a></div>',
     ["jakob", "B13"], ["Detail actions"])
