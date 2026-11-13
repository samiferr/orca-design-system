# Template slots

The named blocks of ORCA's layouts. A page fills slots instead of rewriting layouts, so every page keeps the same structure. Each slot below says which layouts have it and what belongs in it.

## Title

`id: slot-title` · level: template · source: ORCA

The text of the browser tab, before ` · Brand`.

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block title %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Defaults to `title` from the context; override for detail pages: the record's name first.
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

One sentence under the title saying what the page is for or its scope.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates).

### How to use

- `{% block page_subtitle %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates).
- Defaults to `subtitle` from the context; leave it out when the title says it all.

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

The page's buttons, at the end of the page head: one primary action and few others.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates).

### How to use

- `{% block page_actions %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates).
- List and detail templates fill it from `list_actions` and `detail_actions`; override those instead when you can.

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

Script tags at the end of the body, for a project-wide script loaded on every page.

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

Classes on the body element, for page-wide styling hooks.

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

The whole sidebar element: navigation, extra content and the collapse toggle.

### When to use

- Pages built on the app shell and every template built on it (generic, parent-child and page-type templates) and the docs layout.

### How to use

- `{% block sidebar %}…{% endblock %}` in a template that extends the app shell and every template built on it (generic, parent-child and page-type templates) and the docs layout.
- Override with an empty block for pages without navigation (a wizard, a full-screen editor).

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

Content under the navigation in the sidebar: a site switcher, a plan meter, a help link.

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

Where filters go: a right drawer, opened by the Filters button the template puts in the page actions.

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

Dialogs and drawers, placed after the page so they open above everything.

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

The end of the page: legal and help links on public pages, a version line in applications.

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

Page-specific additions to the head: a stylesheet, meta tags, preloads.

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block extra_head %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Use it for one page's CSS or meta; never redefine ORCA tokens other than the brand ones.

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

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block extra_scripts %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Add `defer`; prefer ORCA's data attributes before writing script.

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

### When to use

- Pages built on every layout (from orca/layouts/base.html).

### How to use

- `{% block theme_bootstrap %}…{% endblock %}` in a template that extends every layout (from orca/layouts/base.html).
- Defaults to `orca_theme_bootstrap`, which outputs nothing when the theme is fixed in settings; empty it if your CSP forbids inline scripts and you fix the theme.

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
