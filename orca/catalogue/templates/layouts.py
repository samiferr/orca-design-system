"""Level 4: layouts. Real Django templates a project extends; each fills named blocks (the template slots)."""

from ..registry import add, category
from . import Template

C = category(
    "template-layouts", "Layouts",
    "Whole-page Django templates you extend. They place patterns in a fixed structure and leave named blocks for "
    "your content. Every page of an ORCA project starts from one of these.",
    level="template",
)

BASE_BLOCKS = ["title", "title_suffix", "head", "theme_bootstrap", "extra_head", "body_class", "skip_link", "body",
               "modal", "scripts", "extra_scripts"]
APP_BLOCKS = BASE_BLOCKS + ["top_bar", "brand", "top_nav", "top_bar_end", "sidebar", "sidebar_nav", "sidebar_extra",
                            "page_head", "breadcrumbs", "page_title", "page_subtitle", "page_actions", "messages", "content", "footer"]
APP_CONTEXT = [
    "`title`: the page title (also the browser tab, followed by the brand name).",
    "`subtitle`: one sentence under the title.",
    "`breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.",
    "`nav`: sidebar sections, each `{\"label\": …, \"items\": [{\"label\", \"url\", \"icon\", \"count\", \"current\"}]}`.",
    "`user`: when signed in, the top bar shows the user chip.",
    "`messages`: Django messages are shown under the page head automatically.",
]
EXTEND = "Extend it: `{% templatetag openblock %} extends \"TEMPLATE\" {% templatetag closeblock %}`, then fill only the blocks you need."


def extend(template: str) -> str:
    return EXTEND.replace("TEMPLATE", template)


def layout(eid, name, template, summary, why, when, how, laws, uses, guide, avoid=(), blocks=None, context=None,
           classes=(), a11y=(), source="ORCA"):
    add(Template(eid, name, C, summary, why=why, when=list(when), how=[extend(template)] + list(how),
                 avoid=list(avoid), laws=list(laws), uses=list(uses), guide=list(guide), template=template, preview=eid,
                 blocks=list(blocks if blocks is not None else APP_BLOCKS), context=list(context or []),
                 classes=list(classes), a11y=list(a11y), source=source))


add(Template(
    "base-layout", "Base layout", C,
    "The root every ORCA page extends: the html element with language, theme and density, the head with ORCA's "
    "styles and theme bootstrap, the skip link, and slots for body, modal and scripts.",
    why="Every page needs the same document skeleton, and getting it slightly wrong breaks accessibility (no language, no skip link) "
        "or causes a flash of the wrong theme. One base removes that whole class of mistakes (Tesler's law).",
    when=["Directly only for pages with no ORCA chrome (a print view, an embed); otherwise extend the app shell, auth, error, marketing or docs layout."],
    how=[extend("orca/layouts/base.html"),
         "Set `lang` in the context (or override `html_attrs`) for non-English pages.",
         "Put page-specific CSS in `extra_head` and scripts in `extra_scripts`; never replace `head` unless you also call `orca_head`."],
    laws=["tesler", "jakob"], uses=["page-landmarks"], guide=[], template="orca/layouts/base.html", blocks=BASE_BLOCKS + ["html_attrs", "content"],
    context=["`title`", "`lang`: the page language (default \"en\")."],
    examples=[("Usage", """{% templatetag openblock %} extends "orca/layouts/base.html" {% templatetag closeblock %}
{% templatetag openblock %} block title {% templatetag closeblock %}Print view{% templatetag openblock %} endblock {% templatetag closeblock %}
{% templatetag openblock %} block content {% templatetag closeblock %}…{% templatetag openblock %} endblock {% templatetag closeblock %}""")],
))

layout("app-shell", "App shell", "orca/layouts/app.html",
       "The application frame: top bar with brand, sidebar navigation that collapses to a rail (a drawer on phones), "
       "and a main column with breadcrumbs, page title, subtitle, actions, messages and content.",
       "People learn an application's frame once and then only read what changes (Jakob's law). A fixed place for title, actions and "
       "messages makes every page scannable in the same order (Practical UI L03), and the collapsible sidebar gives dense screens their space back.",
       ["Every signed-in page of an application: lists, details, forms, dashboards, calendars."],
       ["Fill `content`; set `title` and `nav` in the context (or override `sidebar_nav`).",
        "Put the page's main button in `page_actions` (one primary, Practical UI B03).",
        "On phones the sidebar opens over the page from the menu button (`data-orca-sidebar-open`); Escape closes it."],
       ["jakob", "L03", "B03", "tesler"], ["top-bar", "sidebar", "page-head", "messages-region"],
       ["App shell"], context=APP_CONTEXT, classes=[".orca-shell__menu"],
       a11y=["One `main` landmark with id `main` for the skip link; the sidebar is a `nav` labelled “Sections”."])

layout("auth-layout", "Auth layout", "orca/layouts/auth.html",
       "A centred card on the alternate ground for sign-in, password reset and other pages before an account is open.",
       "Before sign-in people should see one task and nothing to wander off to (Hick's law); the brand on the card confirms they are in the right place (Practical UI C08).",
       ["Sign in, sign out, password reset and change, locked-out and invitation pages."],
       ["With Django's `LoginView`, `template_name=\"orca/layouts/auth.html\"` works as is: it renders `form` with `orca_field`.",
        "Override `form_extra` for 'Keep me signed in' and the reset link, `footer` for help text, `submit_label` for the button."],
       ["hick", "C08", "R01"], ["login-card"], ["Auth layout"],
       blocks=BASE_BLOCKS + ["content", "brand", "page_title", "page_subtitle", "messages", "form_extra", "submit_label", "footer"],
       context=["`form`: any Django form (fields are rendered in order).", "`title`, `subtitle`, `submit_label`, `form_action`."],
       classes=[".orca-auth", ".orca-auth-page"])

layout("email-layout", "Email layout", "orca/email/base.html",
       "The page frame of every transactional email: brand bar, title, paragraphs, one action with its link printed, and footer, with colours written inline.",
       "Email clients ignore stylesheets, so the layout is tables with inline hex colours computed from the brand (Postel's law). One template keeps every email recognisable (Jakob's law).",
       ["Every email the project sends."],
       ["Fill `content` (or pass `paragraphs`), set `action_url` and `action_label`, and `footer` with why the reader gets it.",
        "Send it with `render_to_string` as the HTML alternative of an `EmailMultiAlternatives`; always add the plain-text body."],
       ["postel", "jakob", "W05"], ["email-frame"], ["Email layout"],
       blocks=["title", "preheader", "brand", "heading", "content", "action", "footer"],
       context=["`title`, `preheader`, `paragraphs`, `action_url`, `action_label`, `footer`, `lang`."])

layout("error-layouts", "Error layouts", "orca/layouts/error.html",
       "403, 404 and 500 pages: logo, illustration, error code, what happened in plain words and what to do next.",
       "An error page is the low point of a visit; saying plainly what happened and offering the way out limits the damage (Peak–end rule, Practical UI W15).",
       ["Your project's `templates/403.html`, `404.html` and `500.html`."],
       ["Create `templates/404.html` containing `{% templatetag openblock %} extends \"orca/errors/404.html\" {% templatetag closeblock %}`; the same for 403 and 500.",
        "The 500 page renders without a request context: it uses no template tags that need one.",
        "Override `error_text` and `error_actions` to point to your support or status page."],
       ["peak-end", "W15", "W01"], ["error-message"], ["Error layouts (403, 404, 500)"],
       blocks=BASE_BLOCKS + ["brand", "illustration", "error_code", "page_title", "error_text", "error_actions"],
       classes=[".orca-error-layout", ".orca-error-layout__body", ".orca-error-layout__code", ".orca-error-page"])

layout("homepage-template", "Homepage template", "orca/layouts/home.html",
       "The page people land on after signing in: a greeting, a stat grid, a main column for what changed and an aside with shortcuts.",
       "The first screen should answer 'is everything all right, and what needs me?' (Peak–end rule); stats first and shortcuts to frequent tasks shorten every visit (Fitts's law).",
       ["The start page of an application."],
       ["Pass `stats` (label, value, icon, foot, url) and `shortcuts` (label, url, icon); fill `home_main` with recent activity or tasks."],
       ["peak-end", "fitts", "L03"], ["app-shell", "kpi-grid", "activity-feed"], ["Homepage template"],
       blocks=APP_BLOCKS + ["home_stats", "home_main", "home_aside"], context=APP_CONTEXT + ["`stats`, `shortcuts`."])

layout("feed-skeleton", "Feed skeleton", "orca/layouts/feed.html",
       "A centred column of posts with skeleton posts while more load, and an empty state when there are none.",
       "A narrow column keeps photos and captions at a readable width (Practical UI T09); skeletons that match the post shape make loading feel faster and stop the page jumping (Doherty threshold).",
       ["Photo and update feeds, timelines of posts."],
       ["Pass `posts` (author, when, image, alt, text); set `loading` before the first page or `has_more` to show skeleton posts at the end.",
        "Load the next page with htmx on the skeleton (`hx-trigger=\"revealed\"`) and replace it."],
       ["doherty", "T09", "aesthetic"], ["photo-post", "loading-placeholder", "no-results"], ["Feed skeleton"],
       blocks=APP_BLOCKS + ["feed_compose", "feed", "feed_loading"], context=APP_CONTEXT + ["`posts`, `loading`, `has_more`, `empty_title`, `empty_text`."],
       classes=[".orca-feed", ".orca-feed__skeleton"])

layout("person-block-grid", "Person-block grid", "orca/layouts/people.html",
       "A grid of people cards: avatar, name, role and a contact action.",
       "Faces and names in a regular grid are found by recognition rather than reading (Practical UI L11); the same card for everyone keeps it scannable (Jakob's law).",
       ["Team pages, members of a site or project, directories."],
       ["Pass `people` (name, role, url, email). Use a table instead when people are compared on several attributes."],
       ["L11", "jakob", "miller"], ["card-grid-layout"], ["Person-block grid"],
       blocks=APP_BLOCKS + ["people"], context=APP_CONTEXT + ["`people`, `empty_title`."], classes=[".orca-person-grid"])

layout("marketing-layout", "Marketing page layout", "orca/layouts/marketing.html",
       "The public site frame: site header with navigation and actions, full-width sections, and a footer with link columns.",
       "Public pages are scanned, not used: a familiar header, generous sections and a footer of links meet expectations (Jakob's law, Aesthetic–usability effect). One primary call to action per screen (Von Restorff).",
       ["Landing, product, pricing and other public pages."],
       ["Fill `content` with marketing sections (hero, feature grid, story, factoid); wrap non-full-width sections in `.orca-container`.",
        "Pass `site_nav` and `footer_cols`; put sign-in and the main call to action in `header_actions`."],
       ["jakob", "aesthetic", "restorff"], ["site-header", "marketing-hero", "feature-grid", "footer"],
       ["Marketing page layout", "Marketing landing page"],
       blocks=BASE_BLOCKS + ["top_bar", "brand", "header_actions", "content", "footer", "legal"],
       context=["`site_nav` (label, url, current), `footer_cols` (title, links).", "`title`."],
       classes=[".orca-marketing-main", ".orca-marketing-page", ".orca-container"])

BLOG_BLOCKS = BASE_BLOCKS + ["top_bar", "brand", "top_nav", "top_bar_end", "sidebar", "sidebar_nav", "sidebar_extra", "messages", "blog_modifier",
                             "breadcrumbs", "blog_kicker", "page_title", "page_subtitle", "blog_meta", "page_actions", "blog_body", "blog_footer",
                             "blog_aside", "blog_toc", "content", "footer"]

layout("blog-layout", "Blog page layout", "orca/layouts/blog.html",
       "A long-form page that reads well: breadcrumbs, title, introduction, version and last update, sections in a measured reading column, "
       "and an \"On this page\" column on the right.",
       "Long text is read, not scanned: a front-loaded introduction (Practical UI W05), a line length near 70 characters (T09) and a contents column "
       "that shows where you are (Miller's law) let people read comfortably on any screen, and a centred column never stretches across a large window. "
       "Version and last update tell the reader whether to trust the page.",
       ["Articles, guides, documentation pages, release notes, case studies and policies: any page that is mostly sections of text."],
       ["Pass `title`, `subtitle` (the introduction: one or two sentences), `version` and `updated` (a date); optional `kicker`, `author`, `reading_time` (minutes), `breadcrumbs`.",
        "Fill `blog_body` with sections: each `<section>` has an `h2.orca-section-title` with an `id`. The contents column is built from those `h2` headings, "
        "or pass `toc` (`[{\"id\", \"label\"}]`) to write it yourself.",
        "Indexes, tables and galleries that need the full width: add `{% templatetag openblock %} block blog_modifier {% templatetag closeblock %} orca-blog--wide{% templatetag openblock %} endblock {% templatetag closeblock %}`; the head keeps its reading width.",
        "The page has the app shell's top bar and sidebar (`nav`, or your own `sidebar` block); the Docs page layout is this layout with a documentation sidebar."],
       ["W05", "T09", "miller", "jakob"], ["docs-page-header", "table-of-contents", "top-bar"], ["Blog page layout", "Blog page"],
       blocks=BLOG_BLOCKS,
       context=["`title`, `subtitle` (introduction), `kicker`, `breadcrumbs`.", "`version`, `updated` (a date), `author`, `reading_time`: shown as the meta line when present.",
                "`toc`: optional contents `[{\"id\", \"label\"}]`; without it the `h2` headings of the body are listed."],
       classes=[".orca-blog", ".orca-blog--wide", ".orca-blog__article", ".orca-blog__head", ".orca-blog__intro", ".orca-blog__meta", ".orca-blog__body", ".orca-blog__aside", ".orca-blog-page"])

layout("docs-layout", "Docs page layout", "orca/layouts/docs.html",
       "The Blog page with a documentation sidebar: a filter and a page tree on the left, the reading column and \"On this page\" on the right.",
       "Documentation readers both browse and look up (Miller's law, Hick's law): a filterable tree supports both, and the Blog page's measured reading column keeps long text comfortable (Practical UI T09, W05).",
       ["Product documentation, help centres, internal handbooks."],
       ["Pass `docs_nav` (sections with `label`, `icon`, `open` and `items`: label, url, current), `title`, `subtitle`, `version`, `updated` and `breadcrumbs`; fill `blog_body`.",
        "First-level sections lead with an `icon` and end with a small chevron that shows open or closed.",
        "This documentation site uses the same structure with the sidebar pattern."],
       ["miller", "hick", "T09", "W05"], ["docs-sidebar", "docs-page-header", "top-bar"], ["Docs page layout", "Docs page"],
       blocks=BLOG_BLOCKS,
       context=["`docs_nav`, `title`, `subtitle`, `version`, `updated`, `breadcrumbs`."],
       classes=[".orca-docs-sidebar", ".orca-docs-page", ".orca-blog"])
