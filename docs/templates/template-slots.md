# Template slots

The named blocks that ORCA's layouts offer. A page fills slots instead of rewriting the layout. Each slot lists the layouts that have it and what goes in it.

## Title

`id: slot-title` · level: template · source: ORCA

The text of the browser tab, before ` · Brand`.

### General description

The page title is the text shown on the browser tab, in history and in bookmarks. It also becomes the headline of a search result.

#### Use cases

- Telling open tabs apart.
- Naming a page in browser history and bookmarks.
- Giving search engines a clear headline for the page.

#### When not to use it

- Do not use it as the visible page heading; use the page's h1 for that.
- Do not repeat the same title on every page.

#### Best practices

- Put the part that is specific to the page first.
- Keep it short enough to avoid being cut off in a tab.
- Add the site name at the end.
- Make every page's title unique.

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block title %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Defaults to `title` from the context; on detail pages, start with the record's name.
- `title_suffix` changes or removes ` · Brand`.

Blocks: `title`

#### Example: {% block title %}

```django
<div class="orca-code-block">
  <pre><code>{% templatetag openblock %} block title {% templatetag closeblock %}Entrance A · Videos{% templatetag openblock %} endblock {% templatetag closeblock %}</code></pre>
</div>
```

**Principles applied:** Practical UI W04: Lead with the information people seek

**ORCA guide items covered:** Title

---

## Page title

`id: slot-page-title` · level: template · source: ORCA

The page's one h1, in the page head.

### General description

The page title is the single main heading at the top of a page. It tells people what the page is and gives screen readers a way to jump to the start.

#### Use cases

- Naming a list, a record or a form.
- Giving screen-reader users a clear starting point.
- Confirming people landed where they meant to.

#### When not to use it

- Do not use several top-level headings on one page; use lower heading levels for sections.
- Do not use it for long sentences; use a subtitle.

#### Best practices

- Use exactly one per page.
- Keep it short and specific.
- Match the label of the link people clicked to get there.
- Use a real heading element, not styled plain text.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates), auth and error layouts.

### How to use

- `{% block page_title %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates), auth and error layouts.
- Defaults to `title`. Keep it short: the record's name or the list's noun.

Blocks: `page_title`

#### Example: {% block page_title %}

```django
{% block page_title %}
  Videos
{% endblock %}
```

**Principles applied:** Practical UI W04: Lead with the information people seek; Practical UI F01: Design for a diverse audience

**ORCA guide items covered:** Page title

---

## Page subtitle

`id: slot-page-subtitle` · level: template · source: ORCA

One sentence under the title: what the page is for or covers.

### General description

A page subtitle is one short line under the main heading. It explains what the page is for or what it covers.

#### Use cases

- Explaining the scope of a list or report.
- Adding context the title is too short to give.
- Reassuring people they are in the right place.

#### When not to use it

- Skip it when the title already says everything.
- Do not use it for instructions that belong next to a form field.

#### Best practices

- Write one sentence, not a paragraph.
- Say something the title does not.
- Use plain words, not jargon.
- Keep the style the same on every page.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates).

### How to use

- `{% block page_subtitle %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates).
- Defaults to `subtitle` from the context; skip it when the title is enough.

Blocks: `page_subtitle`

#### Example: {% block page_subtitle %}

```django
{% block page_subtitle %}
  <p class="orca-page-subtitle">Every video from North building.</p>
{% endblock %}
```

**Principles applied:** Practical UI W05: Order explanations as an inverted pyramid

**ORCA guide items covered:** Page subtitle

---

## Page actions

`id: slot-page-actions` · level: template · source: ORCA

The page's buttons at the end of the page head: one primary action, few others.

### General description

Page actions are the main buttons of a page, placed in a fixed spot near the heading. They hold the things a person can do with the whole page.

#### Use cases

- Adding a new record from a list page.
- Exporting or printing a report.
- Editing the record shown on a detail page.

#### When not to use it

- Do not put actions for a single row there; place them on the row.
- Do not fill it with many equal buttons; group extras in a menu.

#### Best practices

- Show one clear primary action.
- Keep the same position on every page.
- Start button labels with a verb.
- Move rarely used actions into an overflow menu.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates).

### How to use

- `{% block page_actions %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates).
- List and detail templates fill it from `list_actions` and `detail_actions`; override those instead.

Blocks: `page_actions`

#### Example: {% block page_actions %}

```django
{% block page_actions %}
  <div class="orca-row">
    <button class="orca-button" type="button">Export</button>
    <a class="orca-button orca-button--primary" href="#">Add video</a>
  </div>
{% endblock %}
```

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI B03: One primary action

**ORCA guide items covered:** Page actions

---

## Breadcrumbs

`id: slot-breadcrumbs` · level: template · source: ORCA

The trail of parent pages above the title.

### General description

Breadcrumbs are a row of links showing the pages above the current one. They show where you are and let you jump back up.

#### Use cases

- Orienting people deep inside a site or app.
- Going back to a parent list in one click.
- Helping visitors who arrive from search on a nested page.

#### When not to use it

- Do not use them on flat sites with only one level; use plain navigation.
- Do not use them as the main way to move around.

#### Best practices

- Show the path from the top level to the current page.
- Make the last item plain text, not a link.
- Keep labels short and match page titles.
- Place them above the page title.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates) and the docs layout.

### How to use

- `{% block breadcrumbs %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates) and the docs layout.
- Defaults to the `breadcrumbs` context list of `(label, url)`; OrcaPageMixin builds it for detail pages.

Blocks: `breadcrumbs`

#### Example: {% block breadcrumbs %}

```django
{% block breadcrumbs %}
  <nav class="orca-breadcrumbs" aria-label="Breadcrumb">
    <ol>
      <li>
        <a href="#">Videos</a>
      </li>
      <li>
        <span aria-current="page">Entrance A</span>
      </li>
    </ol>
  </nav>
{% endblock %}
```

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI L05: Use depth to support navigation and priority

**ORCA guide items covered:** Breadcrumbs

---

## Content

`id: slot-content` · level: template · source: ORCA

The page's own content, inside the main landmark.

### General description

The content region is the main area of a page where its own material goes. Everything around it, such as the header and navigation, stays the same from page to page.

#### Use cases

- Holding the main text, forms or tables of a page.
- Keeping a consistent frame around changing content.
- Letting screen readers skip straight to the main part.

#### When not to use it

- Do not put site-wide navigation or footers inside it.
- Do not make several competing main regions on one page.

#### Best practices

- Use one main region per page.
- Mark it so skip links can reach it.
- Structure it with clear headings and spacing.
- Leave the surrounding frame untouched.

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block content %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Wrap sections in a vertical stack; put two related panels in a two-column grid or split.

Blocks: `content`

#### Example: {% block content %}

```django
{% block content %}
  <div class="orca-vstack orca-vstack--tight">
    <p class="orca-p">Your page content.</p>
  </div>
{% endblock %}
```

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI L09: Set spacing by relationship

**ORCA guide items covered:** Content

---

## Scripts

`id: slot-scripts` · level: template · source: ORCA

Script tags at the end of the body, for scripts loaded on every page.

### General description

A scripts region holds the JavaScript files a page loads, placed at the end of the page. This lets the visible content appear first.

#### Use cases

- Loading site-wide behaviour such as menus.
- Adding analytics or a shared library.
- Keeping all script tags in one predictable place.

#### When not to use it

- Do not load scripts for one page on every page; load them only where needed.
- Do not put code the page needs before it renders at the end.

#### Best practices

- Load scripts at the end or with defer.
- Include only what the page uses.
- Keep scripts in one place.
- Make sure the page still works with scripts that fail to load.

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block scripts %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Set it once in your project's own base template; use `extra_scripts` for one page.

Blocks: `scripts`

#### Example: {% block scripts %}

```django
<div class="orca-code-block">
  <pre><code>{% templatetag openblock %} block scripts {% templatetag closeblock %}&lt;script src=&quot;/static/app/site.js&quot; defer&gt;&lt;/script&gt;{% templatetag openblock %} endblock {% templatetag closeblock %}</code></pre>
</div>
```

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Scripts

---

## Head

`id: slot-head` · level: template · source: ORCA

ORCA's stylesheets, brand values, favicon and script (`orca_head`).

### General description

The head of a page holds information for the browser that is not shown on screen: stylesheets, the icon, the title and meta tags.

#### Use cases

- Linking stylesheets and fonts.
- Setting the page icon and character set.
- Adding meta tags for phones and search engines.

#### When not to use it

- Do not put visible content in it; use the body.
- Do not copy the head into every page by hand; share it.

#### Best practices

- Set the character encoding first.
- Include the viewport meta tag for phones.
- Keep it in one shared place.
- Load only the styles the page needs.

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block head %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Override only to pass options, and keep `orca_head` in it: `orca_head script=False`.

Blocks: `head`

#### Example: {% block head %}

```django
<div class="orca-code-block">
  <pre><code>{% templatetag openblock %} block head {% templatetag closeblock %}{% templatetag openblock %} orca_head theme_restore=False {% templatetag closeblock %}{% templatetag openblock %} endblock {% templatetag closeblock %}</code></pre>
</div>
```

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Head

---

## Body class

`id: slot-body-class` · level: template · source: ORCA

Classes on the body element, for page-wide styling.

### General description

A body class is a name added to the page's body element so styles can target one kind of page. It changes a page's look without touching shared code.

#### Use cases

- Giving a single page its own layout tweak.
- Marking the type of page, such as an app or a report.
- Switching a page to a full-width mode.

#### When not to use it

- Do not use it to restyle individual components; style those directly.
- Do not use it to store state that scripts depend on.

#### Best practices

- Use short, descriptive names.
- Keep the classes the layout already needs.
- Scope styles with the class instead of overriding globally.
- Remove unused classes.

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block body_class %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- The app shell sets `orca-shell`; keep it when overriding: `orca-shell my-page`.

Blocks: `body_class`

#### Example: {% block body_class %}

```django
<div class="orca-code-block">
  <pre><code>{% templatetag openblock %} block body_class {% templatetag closeblock %}orca-shell reports-page{% templatetag openblock %} endblock {% templatetag closeblock %}</code></pre>
</div>
```

**Principles applied:** Practical UI F09: Keep visual and functional behaviour consistent

**ORCA guide items covered:** Body class

---

## Sidebar

`id: slot-sidebar` · level: template · source: ORCA

The whole sidebar: navigation, extra content and the collapse toggle.

### General description

A sidebar is a vertical panel at the side of a page. It usually holds the main navigation and can collapse to save room.

#### Use cases

- Showing the main sections of an application.
- Keeping navigation visible while content scrolls.
- Docs sites with a long list of pages.

#### When not to use it

- Avoid it on short flows such as sign-up or checkout; use a simple page.
- Avoid it for sites with only a few links; use a top bar.

#### Best practices

- Keep the order of items the same everywhere.
- Mark the current page.
- Let it collapse on small screens.
- Limit the number of top-level items.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates) and the docs layout.

### How to use

- `{% block sidebar %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates) and the docs layout.
- Use an empty block for pages without navigation, such as a wizard or full-screen editor.

Blocks: `sidebar`

#### Example: {% block sidebar %}

```django
<div class="orca-code-block">
  <pre><code>{% templatetag openblock %} block sidebar {% templatetag closeblock %}{% templatetag openblock %} endblock {% templatetag closeblock %}</code></pre>
</div>
```

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Sidebar

---

## Top bar

`id: slot-top-bar` · level: template · source: ORCA

The bar at the top of the page: menu button, brand, top navigation and the user's controls.

### General description

A top bar is a strip across the top of every page. It holds the brand, main links and the person's own controls such as search or account.

#### Use cases

- Showing the logo and a link home.
- Offering search, notifications and the account menu.
- Giving public sites their main navigation.

#### When not to use it

- Do not crowd it with many links; move extras to a sidebar or menu.
- Do not hide it on every scroll when people need quick access.

#### Best practices

- Keep it in the same place on every page.
- Put the logo on the left and personal tools on the right.
- Keep the height small.
- Collapse links into a menu on phones.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates), the marketing and docs layouts.

### How to use

- `{% block top_bar %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates), the marketing and docs layouts.
- Fill `top_bar_end` for search, notifications and the user menu; replace the whole bar only for a different header.

Blocks: `top_bar`

#### Example: {% block top_bar %}

```django
{% block top_bar %}
  <div class="orca-row">
    <a class="orca-icon-button" href="#" aria-label="Notifications">
      {% icon "notifications" %}
    </a>
  </div>
{% endblock %}
```

**Principles applied:** Jakob's law: work the way products people already know work

**ORCA guide items covered:** Top bar

---

## Brand

`id: slot-brand` · level: template · source: ORCA

The logo or wordmark, from `settings.ORCA['BRAND']`.

### General description

The brand area shows the logo or name of a product or company. It usually links back to the home page.

#### Use cases

- Confirming whose site this is.
- Giving a one-click way back home.
- Repeating identity across all pages.

#### When not to use it

- Do not use large logos that push content down; keep them compact.
- Do not make it the only way to reach home on small screens without a label.

#### Best practices

- Place it in the same corner on every page.
- Link it to the home page.
- Give the logo image useful alternative text.
- Use a version that stays readable on small screens.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates), auth, error, marketing and docs layouts.

### How to use

- `{% block brand %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates), auth, error, marketing and docs layouts.
- Defaults to `orca_logo`; override only to link it elsewhere: `orca_logo href="/dashboard/"`.

Blocks: `brand`

#### Example: {% block brand %}

```django
{% block brand %}
  {% orca_logo href="#" %}
{% endblock %}
```

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI C08: Choose and adapt the brand colour deliberately

**ORCA guide items covered:** Brand

---

## Sidebar extra

`id: slot-sidebar-extra` · level: template · source: ORCA

Content under the sidebar navigation: a site switcher, plan meter or help link.

### General description

A sidebar extra area is space under the main navigation for secondary items, such as a site switcher, a usage meter or a help link.

#### Use cases

- Switching between sites or workspaces.
- Showing plan or storage usage.
- Linking to help and support.

#### When not to use it

- Do not put main navigation here; keep it in the navigation list.
- Do not add long content; it crowds the navigation.

#### Best practices

- Keep it short.
- Group related items together.
- Put the most useful item first.
- Make sure it works when the sidebar is narrow.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates) and the docs layout.

### How to use

- `{% block sidebar_extra %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates) and the docs layout.
- Keep it short; it is hidden when the sidebar collapses to the rail.

Blocks: `sidebar_extra`

#### Example: {% block sidebar_extra %}

```django
{% block sidebar_extra %}
  <div class="orca-sidebar__section">
    <p class="orca-sidebar__label">Site</p>
    <p class="orca-small" style="padding: 0 var(--orca-space-16)">North building</p>
  </div>
{% endblock %}
```

**Principles applied:** Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Sidebar extra

---

## Sidebar navigation

`id: slot-sidebar-nav` · level: template · source: ORCA

The navigation sections of the sidebar.

### General description

Sidebar navigation is a list of links to the main sections of an app, usually grouped under short labels. It stays on screen as you move around.

#### Use cases

- Moving between the main areas of an application.
- Showing where you are right now.
- Grouping many pages into clear sections.

#### When not to use it

- Avoid it for a handful of links; use a top bar.
- Avoid deep nesting; use breadcrumbs or tabs for lower levels.

#### Best practices

- Group related links under clear labels.
- Mark the current page.
- Use short, plain item names.
- Keep the order stable between visits.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates) and the docs layout.

### How to use

- `{% block sidebar_nav %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates) and the docs layout.
- Prefer the `nav` context (a list of sections with items); override the block for a nav tree.

Blocks: `sidebar_nav`

#### Example: {% block sidebar_nav %}

```django
{% block sidebar_nav %}
  <div class="orca-sidebar__section">
    <ul class="orca-side-nav">
      <li>
        <a class="orca-side-link" href="#" aria-current="page">
          {% icon "home" %}
          <span class="orca-side-link__label">Dashboard</span>
        </a>
      </li>
    </ul>
  </div>
{% endblock %}
```

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Sidebar navigation

---

## Filter panel

`id: slot-filter-panel` · level: template · source: ORCA

A right drawer for filters, opened by the Filters button in the page actions.

### General description

A filter panel is a set of controls for narrowing a list, often in a drawer or side panel. People pick values and the list updates.

#### Use cases

- Narrowing a long list by status, date or owner.
- Combining several filters at once.
- Keeping the list visible while filters stay out of the way.

#### When not to use it

- Avoid it for one or two simple filters; show them above the list.
- Avoid it for finding by name; use a search box.

#### Best practices

- Open it from a clearly labelled Filters button.
- Show which filters are active.
- Offer a way to clear all filters.
- Apply filters without losing the person's place.

### When to use

- Pages built on the generic list, planning board and simple data page templates.

### How to use

- `{% block filter_panel %}…{% endblock %}` in a template that extends the generic list, planning board and simple data page templates.
- Pass a GET `filter_form` and the template renders it; override the block for custom filters.

Blocks: `filter_panel`

#### Example: {% block filter_panel %}

```django
{% block filter_panel %}
  <form class="orca-filter-panel" method="get" aria-label="Filters" onsubmit="return false">
    <div class="orca-filter-panel__head">
      <span class="orca-panel-title">Filters</span>
    </div>
    <fieldset class="orca-filter-panel__group">
      <legend>Status</legend>
      <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Online</label>
    </fieldset>
  </form>
{% endblock %}
```

**Principles applied:** Practical UI L14: Reduce travel between related actions; Practical UI S04: Reveal secondary information when needed

**ORCA guide items covered:** Filter panel

---

## Body

`id: slot-body` · level: template · source: ORCA

Everything inside the body element except the skip link, modal and scripts.

### General description

The body of a page is everything people see in the browser window. A layout fills it with the frame around the page's own content.

#### Use cases

- Defining the overall structure of a page type.
- Building a new kind of layout.
- Placing the skip link, main area and dialogs.

#### When not to use it

- Do not replace it on ordinary pages; fill the content area instead.
- Do not put hidden tracking content in it.

#### Best practices

- Use proper landmark regions such as header, main and footer.
- Keep one main region.
- Place a skip link first.
- Keep structure the same across pages.

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block body %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Override it only in your own layout that extends `orca/layouts/base.html`.

Blocks: `body`

#### Example: {% block body %}

```django
<div class="orca-code-block">
  <pre><code>{% templatetag openblock %} block body {% templatetag closeblock %}&lt;main id=&quot;main&quot; tabindex=&quot;-1&quot;&gt;…&lt;/main&gt;{% templatetag openblock %} endblock {% templatetag closeblock %}</code></pre>
</div>
```

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Body

---

## Modal

`id: slot-modal` · level: template · source: ORCA

Dialogs and drawers, placed after the page so they open above it.

### General description

A modal region is the place in a page where dialogs and drawers are kept. They appear above everything else when opened.

#### Use cases

- Holding confirmation dialogs.
- Holding side drawers with forms or details.
- Keeping overlays out of the page's normal flow.

#### When not to use it

- Do not use a dialog for content people need to compare with the page; use a panel.
- Do not open dialogs automatically on load.

#### Best practices

- Give each dialog a title.
- Move focus into it when it opens.
- Let Escape close it.
- Return focus to the button that opened it.

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block modal %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Put `<dialog>` elements here and open them with `data-orca-dialog-open`.

Blocks: `modal`

#### Example: {% block modal %}

```django
{% block modal %}
  <button class="orca-button" type="button" data-orca-dialog-open="slot-dlg">Open the dialog</button>
  <dialog class="orca-dialog" id="slot-dlg" aria-labelledby="slot-dlg-t">
    <h2 class="orca-dialog-title" id="slot-dlg-t">Dialog title</h2>
    <p class="orca-p">Dialog text.</p>
    <div class="orca-dialog__footer">
      <button class="orca-button" type="button" data-orca-dialog-close>Close</button>
    </div>
  </dialog>
{% endblock %}
```

**Principles applied:** Practical UI L05: Use depth to support navigation and priority

**ORCA guide items covered:** Modal

---

## Footer

`id: slot-footer` · level: template · source: ORCA

Legal and help links on public pages, a version line in applications.

### General description

A footer is the area at the end of a page. It holds links people expect to find last, such as legal notices, contact details and help.

#### Use cases

- Linking to terms, privacy and contact pages.
- Showing the app version or copyright.
- Repeating key links for people who reach the bottom.

#### When not to use it

- Do not hide essential actions there; people may never scroll that far.
- Do not overload it with every site link.

#### Best practices

- Keep it the same on every page.
- Group links under short headings.
- Keep text small but readable.
- Include only links people need.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates), auth, marketing and docs layouts.

### How to use

- `{% block footer %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates), auth, marketing and docs layouts.
- The marketing layout fills it from `footer_cols`; in the app shell it sits at the end of the main column.

Blocks: `footer`

#### Example: {% block footer %}

```django
{% block footer %}
  <p class="orca-small orca-muted">Version 0.4.0 · <a class="orca-link" href="#">Help</a></p>
{% endblock %}
```

**Principles applied:** Jakob's law: work the way products people already know work

**ORCA guide items covered:** Footer

---

## Extra head

`id: slot-extra-head` · level: template · source: ORCA

Page-specific head content: a stylesheet, meta tags, preloads.

### General description

An extra head area lets one page add its own items to the head: a stylesheet, meta tags or preloaded files, without copying the shared head.

#### Use cases

- Adding a page-specific stylesheet.
- Setting a page's social sharing tags.
- Telling search engines not to index one page.

#### When not to use it

- Do not use it for content every page needs; add that to the shared head.
- Do not use it to restyle the whole site.

#### Best practices

- Add only what this page needs.
- Keep additions small.
- Do not repeat tags the shared head already sets.
- Test that the page still loads fast.

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block extra_head %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Use it for one page's CSS or meta; redefine only the brand tokens.

Blocks: `extra_head`

#### Example: {% block extra_head %}

```django
<div class="orca-code-block">
  <pre><code>{% templatetag openblock %} block extra_head {% templatetag closeblock %}&lt;meta name=&quot;robots&quot; content=&quot;noindex&quot;&gt;{% templatetag openblock %} endblock {% templatetag closeblock %}</code></pre>
</div>
```

**Principles applied:** Practical UI F09: Keep visual and functional behaviour consistent

**ORCA guide items covered:** Extra head

---

## Extra scripts

`id: slot-extra-scripts` · level: template · source: ORCA

One page's scripts, after the site-wide ones.

### General description

An extra scripts area lets one page load its own JavaScript after the site-wide scripts. Other pages stay lighter because they skip it.

#### Use cases

- Loading a chart library on a report page.
- Adding behaviour for one form.
- Running a small page-specific script.

#### When not to use it

- Do not use it for scripts every page needs; load those site-wide.
- Do not use it for behaviour a plain HTML feature already gives.

#### Best practices

- Load with defer.
- Include only what the page uses.
- Keep files small.
- Make sure the page still works if the script fails.

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block extra_scripts %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Add `defer`; try ORCA's data attributes before writing script.

Blocks: `extra_scripts`

#### Example: {% block extra_scripts %}

```django
<div class="orca-code-block">
  <pre><code>{% templatetag openblock %} block extra_scripts {% templatetag closeblock %}&lt;script src=&quot;/static/app/reports.js&quot; defer&gt;&lt;/script&gt;{% templatetag openblock %} endblock {% templatetag closeblock %}</code></pre>
</div>
```

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Extra scripts

---

## Theme bootstrap

`id: slot-theme-bootstrap` · level: template · source: ORCA

The inline script that applies the reader's saved theme before the page paints.

### General description

A theme bootstrap is a tiny script that runs early and applies the reader's saved light or dark choice before the page is drawn, so there is no flash of the wrong colours.

#### Use cases

- Remembering a dark theme between visits.
- Avoiding a white flash on page load.
- Applying a theme set by the system.

#### When not to use it

- Do not use it if the site has only one theme; it is not needed.
- Do not make it large; slow code defeats the purpose.

#### Best practices

- Run it before the page is drawn.
- Keep it very small.
- Fall back to the system preference.
- Save the choice in a place the script can read.

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block theme_bootstrap %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Defaults to `orca_theme_bootstrap`, which outputs nothing when settings fix the theme; empty it if your CSP forbids inline scripts and you fix the theme.

Blocks: `theme_bootstrap`

#### Example: {% block theme_bootstrap %}

```django
<div class="orca-code-block">
  <pre><code>{% templatetag openblock %} block theme_bootstrap {% templatetag closeblock %}{% templatetag openblock %} orca_theme_bootstrap {% templatetag closeblock %}{% templatetag openblock %} endblock {% templatetag closeblock %}</code></pre>
</div>
```

**Principles applied:** Aesthetic–usability effect: consistent, careful visuals earn trust

**ORCA guide items covered:** Theme bootstrap

---

## List actions

`id: slot-list-actions` · level: template · source: ORCA

The buttons of a list page: Add first, then exports or bulk tools.

### General description

List actions are the buttons at the top of a list page, such as adding a record, exporting or running bulk tools.

#### Use cases

- Adding a new item to a list.
- Exporting the list to a file.
- Starting actions on many selected rows.

#### When not to use it

- Do not put actions for one row here; keep them on that row.
- Do not show many equal buttons; keep one primary action.

#### Best practices

- Put the main add button first.
- Start labels with a verb and name the item.
- Keep the position the same on every list.
- Group less common actions in a menu.

### When to use

- Pages built on the generic list, parent-child list and simple data page templates.

### How to use

- `{% block list_actions %}…{% endblock %}` in a template that extends the generic list, parent-child list and simple data page templates.
- Defaults to 'Add <model>' when `create_url` is set.

Blocks: `list_actions`

#### Example: {% block list_actions %}

```django
{% block list_actions %}
  <a class="orca-button orca-button--primary orca-create" href="#">
    {% icon "plus" %}
    Add video
  </a>
{% endblock %}
```

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI B03: One primary action

**ORCA guide items covered:** List actions

---

## Detail actions

`id: slot-detail-actions` · level: template · source: ORCA

The buttons of a record: Edit, then other actions, Delete last and quieter.

### General description

Detail actions are the buttons on the page of a single record, such as edit, duplicate or delete. They sit together near the record's title.

#### Use cases

- Editing the record being viewed.
- Deleting or archiving the record.
- Running other one-off actions such as export.

#### When not to use it

- Do not place delete beside the main action without separation; set it apart.
- Do not hide Edit in a menu on a detail page.

#### Best practices

- Put Edit first and Delete last.
- Make Delete look quieter and ask for confirmation.
- Use clear verb labels.
- Keep the same positions on every record.

### When to use

- Pages built on the generic detail, parent and parent-child detail templates.

### How to use

- `{% block detail_actions %}…{% endblock %}` in a template that extends the generic detail, parent and parent-child detail templates.
- Defaults to Edit and Delete when `update_url` and `delete_url` are set.

Blocks: `detail_actions`

#### Example: {% block detail_actions %}

```django
{% block detail_actions %}
  <div class="orca-row">
    <a class="orca-button" href="#">
      {% icon "edit" %}
      Edit
    </a>
    <a class="orca-button orca-button--outline-danger" href="#">Delete</a>
  </div>
{% endblock %}
```

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI B13: Scale friction to the consequence

**ORCA guide items covered:** Detail actions

---
