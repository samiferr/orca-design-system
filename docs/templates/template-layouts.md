# Layouts

Whole-page Django templates you extend. They place patterns in a fixed structure and leave named blocks for your content. Every page of an ORCA project starts from one of these.

## Base layout

`id: base-layout` · level: template · source: ORCA

The root every ORCA page extends: the html element with language, theme and density, the head with ORCA's styles and theme bootstrap, the skip link, and slots for body, modal and scripts.

Built from: `skip-link`

### Why

Every page needs the same document skeleton, and getting it slightly wrong breaks accessibility (no language, no skip link) or causes a flash of the wrong theme. One base removes that whole class of mistakes (Tesler's law).

### When to use

- Directly only for pages with no ORCA chrome (a print view, an embed); otherwise extend the app shell, auth, error, marketing or docs layout.

### How to use

- Extend it: `{% extends "orca/layouts/base.html" %}`, then fill only the blocks you need.
- Set `lang` in the context (or override `html_attrs`) for non-English pages.
- Put page-specific CSS in `extra_head` and scripts in `extra_scripts`; never replace `head` unless you also call `orca_head`.

Extend: `{% extends "orca/layouts/base.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `html_attrs`, `content`

### Context it reads

- `title`
- `lang`: the page language (default "en").

#### Example: Usage

```django
{% templatetag openblock %} extends "orca/layouts/base.html" {% templatetag closeblock %}
{% templatetag openblock %} block title {% templatetag closeblock %}Print view{% templatetag openblock %} endblock {% templatetag closeblock %}
{% templatetag openblock %} block content {% templatetag closeblock %}…{% templatetag openblock %} endblock {% templatetag closeblock %}
```

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Jakob's law: work the way products people already know work

---

## App shell

`id: app-shell` · level: template · source: ORCA

The application frame: top bar with brand, sidebar navigation that collapses to a rail (a drawer on phones), and a main column with breadcrumbs, page title, subtitle, actions, messages and content.

Built from: `top-bar`, `sidebar`, `page-head`, `messages-region`, `breadcrumbs`

### Why

People learn an application's frame once and then only read what changes (Jakob's law). A fixed place for title, actions and messages makes every page scannable in the same order (Practical UI L03), and the collapsible sidebar gives dense screens their space back.

### When to use

- Every signed-in page of an application: lists, details, forms, dashboards, calendars.

### How to use

- Extend it: `{% extends "orca/layouts/app.html" %}`, then fill only the blocks you need.
- Fill `content`; set `title` and `nav` in the context (or override `sidebar_nav`).
- Put the page's main button in `page_actions` (one primary, Practical UI B03).
- On phones the sidebar opens over the page from the menu button (`data-orca-sidebar-open`); Escape closes it.

### Accessibility

- One `main` landmark with id `main` for the skip link; the sidebar is a `nav` labelled “Sections”.

Extend: `{% extends "orca/layouts/app.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.

#### Example: Child template

```django
{% extends "orca/layouts/app.html" %}{% load orca %}
{% block page_actions %}<button class="orca-button" type="button">Secondary action</button><a class="orca-button orca-button--primary orca-create" href="#">{% icon "plus" %}Main action</a>{% endblock %}
{% block content %}<div class="orca-vstack">
  <section class="orca-panel" aria-label="Section"><div class="orca-skeleton orca-skeleton--title" style="max-width: 16rem"></div><div class="orca-skeleton orca-skeleton--text"></div><div class="orca-skeleton orca-skeleton--text" style="max-width: 70%"></div></section>
  <div class="orca-two-col"><section class="orca-panel" aria-label="Section"><div class="orca-skeleton orca-aspect-16x9"></div></section><section class="orca-panel" aria-label="Section"><div class="orca-skeleton orca-aspect-16x9"></div></section></div>
</div>{% endblock %}
```

**Classes:** `.orca-shell__menu`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI L03: Establish an order of importance; Practical UI B03: One primary action; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** App shell

---

## Auth layout

`id: auth-layout` · level: template · source: ORCA

A centred card on the alternate ground for sign-in, password reset and other pages before an account is open.

Built from: `login-card`, `form-field`

### Why

Before sign-in people should see one task and nothing to wander off to (Hick's law); the brand on the card confirms they are in the right place (Practical UI C08).

### When to use

- Sign in, sign out, password reset and change, locked-out and invitation pages.

### How to use

- Extend it: `{% extends "orca/layouts/auth.html" %}`, then fill only the blocks you need.
- With Django's `LoginView`, `template_name="orca/layouts/auth.html"` works as is: it renders `form` with `orca_field`.
- Override `form_extra` for 'Keep me signed in' and the reset link, `footer` for help text, `submit_label` for the button.

Extend: `{% extends "orca/layouts/auth.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `content`, `brand`, `page_title`, `page_subtitle`, `messages`, `form_extra`, `submit_label`, `footer`

### Context it reads

- `form`: any Django form (fields are rendered in order).
- `title`, `subtitle`, `submit_label`, `form_action`.

#### Example: Child template

```django
{% extends "orca/layouts/auth.html" %}
{% block form_extra %}<div class="orca-login__row"><label class="orca-check"><input type="checkbox" name="remember"><span class="orca-check__box"></span>Keep me signed in</label><a class="orca-link orca-small" href="#">Forgot your password?</a></div>{% endblock %}
{% block footer %}<p class="orca-login__foot">No account? Ask your administrator.</p>{% endblock %}
```

**Classes:** `.orca-auth`, `.orca-auth-page`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI C08: Choose and adapt the brand colour deliberately; Practical UI R01: Keep the main form flow in one column

**ORCA guide items covered:** Auth layout

---

## Email layout

`id: email-layout` · level: template · source: ORCA

The page frame of every transactional email: brand bar, title, paragraphs, one action with its link printed, and footer, with colours written inline.

Built from: `email-frame`

### Why

Email clients ignore stylesheets, so the layout is tables with inline hex colours computed from the brand (Postel's law). One template keeps every email recognisable (Jakob's law).

### When to use

- Every email the project sends.

### How to use

- Extend it: `{% extends "orca/email/base.html" %}`, then fill only the blocks you need.
- Fill `content` (or pass `paragraphs`), set `action_url` and `action_label`, and `footer` with why the reader gets it.
- Send it with `render_to_string` as the HTML alternative of an `EmailMultiAlternatives`; always add the plain-text body.

Extend: `{% extends "orca/email/base.html" %}`

Blocks: `title`, `preheader`, `brand`, `heading`, `content`, `action`, `footer`

### Context it reads

- `title`, `preheader`, `paragraphs`, `action_url`, `action_label`, `footer`, `lang`.

#### Example: Child template

```django
{% extends "orca/email/base.html" %}
{% block footer %}{{ footer }} <a href="#">Email settings</a>{% endblock %}
```

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Jakob's law: work the way products people already know work; Practical UI W05: Order explanations as an inverted pyramid

**ORCA guide items covered:** Email layout

---

## Error layouts

`id: error-layouts` · level: template · source: ORCA

403, 404 and 500 pages: logo, illustration, error code, what happened in plain words and what to do next.

Built from: `empty-state`, `button`

### Why

An error page is the low point of a visit; saying plainly what happened and offering the way out limits the damage (Peak–end rule, Practical UI W15).

### When to use

- Your project's `templates/403.html`, `404.html` and `500.html`.

### How to use

- Extend it: `{% extends "orca/layouts/error.html" %}`, then fill only the blocks you need.
- Create `templates/404.html` containing `{% extends "orca/errors/404.html" %}`; the same for 403 and 500.
- The 500 page renders without a request context: it uses no template tags that need one.
- Override `error_text` and `error_actions` to point to your support or status page.

Extend: `{% extends "orca/layouts/error.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `brand`, `illustration`, `error_code`, `page_title`, `error_text`, `error_actions`

#### Example: Child template

```django
{% extends "orca/errors/404.html" %}
```

**Classes:** `.orca-error-layout`, `.orca-error-layout__body`, `.orca-error-layout__code`, `.orca-error-page`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Practical UI W15: Help people recover from errors; Practical UI W01: Make every word useful

**ORCA guide items covered:** Error layouts (403, 404, 500)

---

## Homepage template

`id: homepage-template` · level: template · source: ORCA

The page people land on after signing in: a greeting, a stat grid, a main column for what changed and an aside with shortcuts.

Built from: `app-shell`, `stat-card`, `activity-feed`

### Why

The first screen should answer 'is everything all right, and what needs me?' (Peak–end rule); stats first and shortcuts to frequent tasks shorten every visit (Fitts's law).

### When to use

- The start page of an application.

### How to use

- Extend it: `{% extends "orca/layouts/home.html" %}`, then fill only the blocks you need.
- Pass `stats` (label, value, foot, url) and `shortcuts` (label, url, icon); fill `home_main` with recent activity or tasks.

Extend: `{% extends "orca/layouts/home.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `home_stats`, `home_main`, `home_aside`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `stats`, `shortcuts`.

#### Example: Child template

```django
{% extends "orca/layouts/home.html" %}
{% block page_subtitle %}<p class="orca-page-subtitle">Here is what changed since yesterday.</p>{% endblock %}
{% block home_main %}<section class="orca-panel" aria-labelledby="h-recent"><h2 class="orca-panel-title" id="h-recent">Recent activity</h2>
  <div class="orca-vstack orca-vstack--tight">{% for i in "123" %}<div class="orca-activity"><span class="orca-avatar orca-avatar--s" aria-hidden="true">PN</span><div class="orca-activity__head"><strong>Person name</strong> changed Record name {{ i }}<time class="orca-activity__time">{{ i }} h ago</time></div></div>{% endfor %}</div></section>{% endblock %}
```

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI L03: Establish an order of importance

**ORCA guide items covered:** Homepage template

---

## Feed skeleton

`id: feed-skeleton` · level: template · source: ORCA

A centred column of posts with skeleton posts while more load, and an empty state when there are none.

Built from: `photo-post`, `skeleton`, `empty-state`

### Why

A narrow column keeps photos and captions at a readable width (Practical UI T09); skeletons that match the post shape make loading feel faster and stop the page jumping (Doherty threshold).

### When to use

- Photo and update feeds, timelines of posts.

### How to use

- Extend it: `{% extends "orca/layouts/feed.html" %}`, then fill only the blocks you need.
- Pass `posts` (author, when, image, alt, text); set `loading` before the first page or `has_more` to show skeleton posts at the end.
- Load the next page with htmx on the skeleton (`hx-trigger="revealed"`) and replace it.

Extend: `{% extends "orca/layouts/feed.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `feed_compose`, `feed`, `feed_loading`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `posts`, `loading`, `has_more`, `empty_title`, `empty_text`.

#### Example: Child template

```django
{% extends "orca/layouts/feed.html" %}
{% block page_head %}{% endblock %}
```

**Classes:** `.orca-feed`, `.orca-feed__skeleton`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI T09: Limit reading measure; Aesthetic–usability effect: consistent, careful visuals earn trust

**ORCA guide items covered:** Feed skeleton

---

## Person-block grid

`id: person-block-grid` · level: template · source: ORCA

A grid of people cards: avatar, name, role and a contact action.

Built from: `person-block`, `card-grid-layout`

### Why

Faces and names in a regular grid are found by recognition rather than reading (Practical UI L11); the same card for everyone keeps it scannable (Jakob's law).

### When to use

- Team pages, members of a site or project, directories.

### How to use

- Extend it: `{% extends "orca/layouts/people.html" %}`, then fill only the blocks you need.
- Pass `people` (name, role, url, email). Use a table instead when people are compared on several attributes.

Extend: `{% extends "orca/layouts/people.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `people`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `people`, `empty_title`.

#### Example: Child template

```django
{% extends "orca/layouts/people.html" %}
{% block page_actions %}<a class="orca-button orca-button--primary" href="#">Invite people</a>{% endblock %}
```

**Classes:** `.orca-person-grid`

**Principles applied:** Practical UI L11: Align the layout with a responsive grid; Jakob's law: work the way products people already know work; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Person-block grid

---

## Marketing page layout

`id: marketing-layout` · level: template · source: ORCA

The public site frame: site header with navigation and actions, full-width sections, and a footer with link columns.

Built from: `site-header`, `marketing-hero`, `feature-grid`, `footer`

### Why

Public pages are scanned, not used: a familiar header, generous sections and a footer of links meet expectations (Jakob's law, Aesthetic–usability effect). One primary call to action per screen (Von Restorff).

### When to use

- Landing, product, pricing and other public pages.

### How to use

- Extend it: `{% extends "orca/layouts/marketing.html" %}`, then fill only the blocks you need.
- Fill `content` with marketing sections (hero, feature grid, story, factoid); wrap non-full-width sections in `.orca-container`.
- Pass `site_nav` and `footer_cols`; put sign-in and the main call to action in `header_actions`.

Extend: `{% extends "orca/layouts/marketing.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `header_actions`, `content`, `footer`, `legal`

### Context it reads

- `site_nav` (label, url, current), `footer_cols` (title, links).
- `title`.

#### Example: Child template

```django
{% extends "orca/layouts/marketing.html" %}{% load orca static %}
{% block header_actions %}<a class="orca-button orca-button--ghost" href="#">Sign in</a><a class="orca-button orca-button--brand" href="#">Main action</a>{% endblock %}
{% block content %}
<section class="orca-marketing-hero"><div class="orca-hero">
  <div class="orca-hero__text"><p class="orca-card-kicker">Kicker</p><h1 class="orca-hero__title">Headline: the benefit in under ten words.</h1><p class="orca-hero__lead">Lead: one or two sentences that explain the headline.</p>
    <div class="orca-row"><a class="orca-button orca-button--brand" href="#">Main action</a><a class="orca-button" href="#">Second action</a></div></div>
  <div class="orca-hero__media"><img src="{% static "orca/img/sample-street.svg" %}" alt="Product picture"></div></div></section>
<div class="orca-container"><ul class="orca-feature-grid">{% for i in "123" %}<li class="orca-feature">{% icon "success" size="l" %}<h2 class="orca-feature__title">Feature title</h2><p class="orca-feature__text">One sentence about the feature and its benefit.</p></li>{% endfor %}</ul></div>
{% endblock %}
```

**Classes:** `.orca-marketing-main`, `.orca-marketing-page`, `.orca-container`

**Principles applied:** Jakob's law: work the way products people already know work; Aesthetic–usability effect: consistent, careful visuals earn trust; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Marketing page layout; Marketing landing page

---

## Docs page layout

`id: docs-layout` · level: template · source: ORCA

Documentation frame: top bar, a sidebar with a filter and a page tree, and a reading column with breadcrumbs, title and introduction.

Built from: `docs-sidebar`, `docs-page-header`, `top-bar`

### Why

Documentation readers both browse and look up (Miller's law, Hick's law): a filterable tree supports both, and a measured reading column keeps long text comfortable (Practical UI T09, W05).

### When to use

- Product documentation, help centres, internal handbooks.

### How to use

- Extend it: `{% extends "orca/layouts/docs.html" %}`, then fill only the blocks you need.
- Pass `docs_nav` (sections with `label`, `open` and `items`: label, url, current), `title`, `subtitle` and `breadcrumbs`; fill `content`.
- This documentation site uses the same structure with the sidebar pattern.

Extend: `{% extends "orca/layouts/docs.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `content`, `footer`

### Context it reads

- `docs_nav`, `title`, `subtitle`, `breadcrumbs`.

#### Example: Child template

```django
{% extends "orca/layouts/docs.html" %}
{% block content %}<p class="orca-p">Body text of the page. Keep paragraphs short and lead with what the reader needs.</p>
<h2 class="orca-section-title">Section heading</h2>
<p class="orca-p">More body text, with <code class="orca-code">inline code</code> and a <a class="orca-link" href="#">link to another page</a>.</p>
<div class="orca-code-block"><div class="orca-code-block__head"><span>Shell</span></div><pre><code>pip install example</code></pre></div>{% endblock %}
```

**Classes:** `.orca-docs-main`, `.orca-docs-article`, `.orca-docs-page`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Hick's law: fewer, clearer choices mean faster decisions; Practical UI T09: Limit reading measure; Practical UI W05: Order explanations as an inverted pyramid

**ORCA guide items covered:** Docs page layout; Docs page

---

## Generic list template

`id: generic-list` · level: template · source: ORCA

A list page from a ListView: title and Add button, optional filter panel, list header with count and search, a table that becomes cards on phones, pagination and the right empty state.

Built from: `app-shell`, `list-header`, `data-table`, `filter-panel`, `pagination`, `empty-state`

### Why

Most screens of a business application are lists; one template that is always right (sortable header, row actions, empty and no-match states, phone cards) removes repeated decisions and keeps every list familiar (Jakob's law, Tesler's law).

### When to use

- Any ListView: records people find, compare and open.

### How to use

- Extend it: `{% extends "orca/generic/list.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Set `template_name = "orca/generic/list.html"`, `list_columns` and `paginate_by`; filter the queryset on `request.GET["q"]` for the search box.
- Pass a `filter_form` (a GET form) to get the filter panel; override `list` to change the rows completely, `list_actions` for the buttons.

Extend: `{% extends "orca/generic/list.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `list_actions`, `filter_panel`, `list_header`, `list`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `object_list`, `page_obj`, `paginator` (from ListView).
- `columns`: `[{"label", "name", "numeric"}]`.
- `create_url`, `detail_url_name`, `update_url_name`, `delete_url_name` (URL names taking the object's pk), `cancel_url`.
- `filter_form`, `empty_title`, `empty_text`.

#### Example: Child template

```django
{% extends "orca/generic/list.html" %}
{% comment %}A ListView with OrcaPageMixin needs no blocks at all; this preview only adds a filter form (filter_form).{% endcomment %}
```

**Classes:** `.orca-list-layout`

**Principles applied:** Jakob's law: work the way products people already know work; Tesler's law: move unavoidable complexity from the user to the system; Miller's law: chunk information so working memory is not overloaded; Practical UI L14: Reduce travel between related actions

**ORCA guide items covered:** Generic list template; List page

---

## Generic detail template

`id: generic-detail` · level: template · source: ORCA

A record page from a DetailView: title, Edit and Delete actions, and the record's fields as a key–value list.

Built from: `app-shell`, `detail-panel`, `key-value-list`, `record-actions`

### Why

Details read top to bottom as label and value pairs (Practical UI L01); Edit and Delete in the same place on every record make them findable without searching (Jakob's law).

### When to use

- Any DetailView: one record with its properties.

### How to use

- Extend it: `{% extends "orca/generic/detail.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Set `detail_fields`; add related lists or history in `detail_extra`, change the buttons in `detail_actions`.

Extend: `{% extends "orca/generic/detail.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `detail_actions`, `detail`, `detail_extra`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `object`, `fields`, `update_url`, `delete_url`.

#### Example: Child template

```django
{% extends "orca/generic/detail.html" %}{% load orca %}
{% block detail_extra %}<section class="orca-panel" aria-labelledby="d-notes"><h2 class="orca-panel-title" id="d-notes">Related section</h2><p class="orca-p orca-muted">Extra panels go in the detail_extra block.</p></section>{% endblock %}
```

**Principles applied:** Practical UI L01: Group related information; Jakob's law: work the way products people already know work; Practical UI B08: Keep action order predictable

**ORCA guide items covered:** Generic detail template; Detail page

---

## Generic form template

`id: generic-form` · level: template · source: ORCA

A create or edit page from a CreateView or UpdateView: one column of ORCA fields with the error summary and Save and Cancel.

Built from: `app-shell`, `form-stack`, `form-field`, `form-actions`, `narrow-form`

### Why

One column is the fastest form to fill (Practical UI R01); the error summary and inline errors from `orca_form_errors` and `orca_field` make every form recover the same way (W15).

### When to use

- Any CreateView or UpdateView; any page whose main job is one form.

### How to use

- Extend it: `{% extends "orca/generic/form.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Add help text on the model or form field: it is shown under the label. Use `form_fields` to group fields in form sections.

Extend: `{% extends "orca/generic/form.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `form_fields`, `form_actions`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `form`, `object` (when editing), `submit_label`, `cancel_url`.

#### Example: Child template

```django
{% extends "orca/generic/form.html" %}
```

**Principles applied:** Practical UI R01: Keep the main form flow in one column; Practical UI W15: Help people recover from errors; Practical UI R09: Persistent labels, not placeholders

**ORCA guide items covered:** Generic form template; Form page

---

## Generic confirm (delete) template

`id: generic-confirm-delete` · level: template · source: ORCA

The delete confirmation from a DeleteView: what will be deleted, what is kept, a danger button and Cancel; or, when other records still use it, why it cannot be deleted yet.

Built from: `app-shell`, `confirm-action-panel`, `delete-blocked-notice`

### Why

Deleting is the most costly mistake, so friction scales with it (Practical UI B13): consequences in words, the danger button named after the action. When related records protect it, saying which ones turns a dead end into a task (W15).

### When to use

- Any DeleteView; any page confirming a destructive action.

### How to use

- Extend it: `{% extends "orca/generic/confirm_delete.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`. On a DeleteView it also fills `blocked_by` from protected and restricted foreign keys.
- Pass `deleted` (a list) and `kept` (a sentence); `confirm_text` adds a required 'I understand' checkbox for severe deletes.

Extend: `{% extends "orca/generic/confirm_delete.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `consequences`, `blocked_actions`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `object`, `deleted`, `kept`, `confirm_text`, `blocked_by`, `submit_label`, `cancel_url`.

#### Example: Child template

```django
{% extends "orca/generic/confirm_delete.html" %}
```

**Principles applied:** Practical UI B13: Scale friction to the consequence; Practical UI W15: Help people recover from errors; Practical UI B10: Name the action clearly

**ORCA guide items covered:** Generic confirm (delete) template; Confirm page

---

## Generic confirm-action template

`id: generic-confirm-action` · level: template · source: ORCA

A confirmation page for any consequential action that is not a delete: archive, send, disable, run.

Built from: `app-shell`, `confirm-action-panel`

### Why

A separate page with the consequences listed gives people a moment to check (Practical UI B13) without the alarm of a danger colour when nothing is lost.

### When to use

- Actions with wide effects that need a second look: send to everyone, disable a site, start a long run.

### How to use

- Extend it: `{% extends "orca/generic/confirm_action.html" %}`, then fill only the blocks you need.
- Pass `title` (a question), `text`, `items` and `submit_label` (the verb); set `danger=True` only when something is lost.
- Add a `form` for an optional reason or choice.

Extend: `{% extends "orca/generic/confirm_action.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `consequences`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `title`, `text`, `items`, `form`, `danger`, `submit_label`, `cancel_url`.

#### Example: Child template

```django
{% extends "orca/generic/confirm_action.html" %}
```

**Principles applied:** Practical UI B13: Scale friction to the consequence; Practical UI B10: Name the action clearly; Practical UI W04: Lead with the information people seek

**ORCA guide items covered:** Generic confirm-action template

---

## Parent base template

`id: parent-base` · level: template · source: ORCA

The frame shared by every page of a parent record: its title and actions, optional summary stats, and tabs for the overview and each child list.

Built from: `parent-child-tabs`, `page-head`, `stat-card`

### Why

Keeping the parent's header and tabs fixed while the tab content changes tells people where they are and what else the record holds (Practical UI L05, Jakob's law).

### When to use

- Records that own other records: a site and its cameras, a project and its tasks.

### How to use

- Extend it: `{% extends "orca/generic/parent_base.html" %}`, then fill only the blocks you need.
- Extend it for each tab and fill `child_content`; mark the current tab in `parent_tabs`.
- Each tab is its own URL (and view), so tabs can be linked, bookmarked and refreshed.

Extend: `{% extends "orca/generic/parent_base.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `parent_summary`, `parent_tabs`, `detail_actions`, `child_content`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `parent`: the parent object (its title heads every tab).
- `parent_tabs`: `[{"label", "url", "count", "current"}]`, Overview first.
- `parent_stats`: optional `[{"label", "value"}]` shown above the tabs; `parent_update_url`.

#### Example: Child template

```django
{% extends "orca/generic/parent_base.html" %}
{% block child_content %}<section class="orca-panel" aria-label="Tab content"><div class="orca-skeleton orca-skeleton--title" style="max-width: 14rem"></div><div class="orca-skeleton orca-skeleton--text"></div><div class="orca-skeleton orca-skeleton--text" style="max-width: 60%"></div></section>{% endblock %}
```

**Classes:** `.orca-parent__panel`

**Principles applied:** Practical UI L05: Use depth to support navigation and priority; Jakob's law: work the way products people already know work; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Parent base template

---

## Parent detail template

`id: parent-detail` · level: template · source: ORCA

The parent's Overview tab: its fields as a key–value list, with room for more overview panels.

Built from: `parent-base`, `detail-panel`

### Why

The overview answers 'what is this record' before any child list (Practical UI W04), so the first tab is always the parent itself.

### When to use

- The first tab of a parent record.

### How to use

- Extend it: `{% extends "orca/generic/parent_detail.html" %}`, then fill only the blocks you need.
- Pass `fields` (or use OrcaPageMixin's `detail_fields`); add panels in `overview_extra`.

Extend: `{% extends "orca/generic/parent_detail.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `parent_summary`, `parent_tabs`, `detail_actions`, `child_content`, `overview`, `overview_extra`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `parent`: the parent object (its title heads every tab).
- `parent_tabs`: `[{"label", "url", "count", "current"}]`, Overview first.
- `parent_stats`: optional `[{"label", "value"}]` shown above the tabs; `parent_update_url`.
- `fields`.

#### Example: Child template

```django
{% extends "orca/generic/parent_detail.html" %}
```

**Principles applied:** Practical UI W04: Lead with the information people seek; Practical UI L01: Group related information

**ORCA guide items covered:** Parent detail template (tabbed); Parent detail page (overview + child tabs)

---

## Parent-child list template

`id: parent-child-list` · level: template · source: ORCA

A child list inside a parent tab: header with count and 'Add … to parent', the table, pagination and an empty state naming the parent.

Built from: `parent-base`, `child-list-tab`, `data-table`, `empty-state`

### Why

Naming the parent in the add button and the empty state ('No cameras for North building') removes any doubt about where a new record goes (Practical UI W04, B10).

### When to use

- Each child tab of a parent record. The four parent-child templates (list, detail, form, confirm) make up its pages.

### How to use

- Extend it: `{% extends "orca/generic/child_list.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Filter the queryset by the parent from the URL; pass `parent` and `parent_tabs` with this tab current.

Extend: `{% extends "orca/generic/child_list.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `parent_summary`, `parent_tabs`, `detail_actions`, `child_content`, `list_actions`, `list`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `parent`: the parent object (its title heads every tab).
- `parent_tabs`: `[{"label", "url", "count", "current"}]`, Overview first.
- `parent_stats`: optional `[{"label", "value"}]` shown above the tabs; `parent_update_url`.
- `object_list`, `page_obj`, `columns`.
- `create_url`, `detail_url_name`, `update_url_name`, `delete_url_name` (URL names taking the object's pk), `cancel_url`.

#### Example: Child template

```django
{% extends "orca/generic/child_list.html" %}
```

**Principles applied:** Practical UI W04: Lead with the information people seek; Practical UI B10: Name the action clearly; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Parent-child list template; Parent-child pages (list, detail, form, confirm)

---

## Parent-child detail template

`id: parent-child-detail` · level: template · source: ORCA

One child record inside its parent's tab: a back link to the list, Edit and Delete, and the record's fields.

Built from: `parent-base`, `top-actions-header`, `detail-panel`

### Why

The back link and the parent's header keep the path home visible (Jakob's law); the child's own actions sit next to its title (Practical UI L14).

### When to use

- Opening a child record without leaving its parent.

### How to use

- Extend it: `{% extends "orca/generic/child_detail.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Pass `list_url` for the back link; `detail` overrides the field list.

Extend: `{% extends "orca/generic/child_detail.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `parent_summary`, `parent_tabs`, `detail_actions`, `child_content`, `detail_actions`, `detail`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `parent`: the parent object (its title heads every tab).
- `parent_tabs`: `[{"label", "url", "count", "current"}]`, Overview first.
- `parent_stats`: optional `[{"label", "value"}]` shown above the tabs; `parent_update_url`.
- `object`, `fields`, `list_url`, `update_url`, `delete_url`.

#### Example: Child template

```django
{% extends "orca/generic/child_detail.html" %}
```

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI L14: Reduce travel between related actions

**ORCA guide items covered:** Parent-child detail template

---

## Parent-child form template

`id: parent-child-form` · level: template · source: ORCA

Create or edit a child inside its parent's tab, with a heading that names the parent.

Built from: `parent-base`, `form-stack`, `form-field`

### Why

A form that says 'Add camera to North building' cannot be misread (Practical UI W04), and the parent's tabs stay one click away.

### When to use

- Adding and editing child records.

### How to use

- Extend it: `{% extends "orca/generic/child_form.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Set the parent on the new object in `form_valid` (do not show the parent as a field).

Extend: `{% extends "orca/generic/child_form.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `parent_summary`, `parent_tabs`, `detail_actions`, `child_content`, `form_fields`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `parent`: the parent object (its title heads every tab).
- `parent_tabs`: `[{"label", "url", "count", "current"}]`, Overview first.
- `parent_stats`: optional `[{"label", "value"}]` shown above the tabs; `parent_update_url`.
- `form`, `object`, `model_name`, `cancel_url`.

#### Example: Child template

```django
{% extends "orca/generic/child_form.html" %}
```

**Principles applied:** Practical UI W04: Lead with the information people seek; Practical UI R01: Keep the main form flow in one column; Practical UI R02: Ask only for useful, necessary information

**ORCA guide items covered:** Parent-child form template

---

## Parent-child confirm template

`id: parent-child-confirm` · level: template · source: ORCA

Confirm removing a child from its parent, or explain what blocks it.

Built from: `parent-base`, `confirm-action-panel`, `delete-blocked-notice`

### Why

The question names both records ('Remove Gate 1 from Warehouse?') so the consequence is clear (Practical UI B13, W04).

### When to use

- Deleting a child record from inside its parent.

### How to use

- Extend it: `{% extends "orca/generic/child_confirm.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Pass `deleted` to list what goes with it; `blocked_by` is filled by the mixin on a DeleteView.

Extend: `{% extends "orca/generic/child_confirm.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `parent_summary`, `parent_tabs`, `detail_actions`, `child_content`, `consequences`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `parent`: the parent object (its title heads every tab).
- `parent_tabs`: `[{"label", "url", "count", "current"}]`, Overview first.
- `parent_stats`: optional `[{"label", "value"}]` shown above the tabs; `parent_update_url`.
- `object`, `deleted`, `blocked_by`, `submit_label`, `cancel_url`.

#### Example: Child template

```django
{% extends "orca/generic/child_confirm.html" %}
```

**Principles applied:** Practical UI B13: Scale friction to the consequence; Practical UI W04: Lead with the information people seek

**ORCA guide items covered:** Parent-child confirm template

---
