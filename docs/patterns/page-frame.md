# Page frame

The parts that surround every page: headers, top bar, sidebar, footer, page head, messages, drawers and filter panels.

## Header

`id: site-header` · level: pattern · source: ORCA

Header of public pages: logo, a few section links and one or two actions, sticky at the top.

Built from: `logo-link`, `primary-navigation`, `call-to-action`

### General description

The bar at the top of a website with the logo, a few main links and one or two actions. It helps visitors know where they are and where to go.

#### Use cases

- Marketing pages and documentation sites.
- Sign-in and sign-up pages.
- Public pages with a few main sections.

#### When not to use it

- Inside an application with many sections, use a top bar and a sidebar.
- Many links are better in a menu or footer.

#### Best practices

- Put the logo at the left and link it to the home page.
- Keep to about 5 links.
- Mark the current page.
- Make one action stand out.
- Let links wrap or collapse on small screens.

### When to use

- Public and marketing pages, documentation sites, sign-in pages.

### When not to use

- Inside the application: use the top bar.

### How to use

- `<header class="orca-site-header">` with the logo, `<nav aria-label="Main"><ul class="orca-site-header__nav">` and `.orca-site-header__actions`.
- At most 5 links; the current one gets `aria-current="page"`. On phones the links wrap under the logo.

#### Example: Header

```django
<header class="orca-site-header" style="position: static">
  {% orca_logo href="#" %}
  <nav aria-label="Main">
    <ul class="orca-site-header__nav">
      <li>
        <a href="#" aria-current="page">Product</a>
      </li>
      <li>
        <a href="#">Pricing</a>
      </li>
      <li>
        <a href="#">Docs</a>
      </li>
    </ul>
  </nav>
  <div class="orca-site-header__actions">
    <a class="orca-button orca-button--ghost" href="#">Sign in</a>
    <a class="orca-button orca-button--brand" href="#">Start free trial</a>
  </div>
</header>
```

**Classes:** `.orca-site-header`, `.orca-site-header__nav`, `.orca-site-header__actions`

**Principles applied:** Jakob's law: work the way products people already know work; Hick's law: fewer, clearer choices mean faster decisions; Practical UI B03: One primary action

**ORCA guide items covered:** Header

---

## Top bar

`id: top-bar` · level: pattern · source: Tangerine

The application's top bar: menu button, logo, main sections, search and user tools.

Built from: `logo-link`, `primary-navigation`, `utility-navigation`, `search-field`

### General description

The bar across the top of a web application. It usually holds the menu, the logo, main sections, search and tools for the signed-in person.

#### Use cases

- Every signed-in page of an application.
- Giving quick access to search and notifications.
- Showing the signed-in person and their menu.

#### When not to use it

- Public marketing pages suit a simple site header.
- Long lists of sections fit better in a sidebar.

#### Best practices

- Keep it the same on every page.
- Keep it low in height so content stays in view.
- Move links into a menu on small screens.
- Label icon-only buttons for screen readers.
- Make sure text stays readable against the bar colour.

### When to use

- Every authenticated page of an application.

### How to use

- `<header class="orca-topbar">` with `.orca-topbar__start` (menu or sidebar toggle, logo, primary navigation) and `.orca-topbar__end` (search, utility navigation).
- It is the wise_people_analyzer bar: `--orca-brand-bar` (the brand colour mixed with 30% black, darkened further if white text would fall below 4.5:1) with `--orca-brand-bar-on` text.
- Below 1036px, navigation and search move into the drawer, opened by the menu button.

#### Example: Top bar

```django
<div class="orca-stack" style="gap: var(--orca-space-16)">
  <header class="orca-topbar" style="position: static">
    <div class="orca-topbar__start">
      <button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Open menu">
        {% icon "menu" %}
      </button>
      {% orca_logo href="#" %}
      <nav aria-label="Main">
        <ul class="orca-topnav">
          <li>
            <a href="#" aria-current="page">Dashboard</a>
          </li>
          <li>
            <a href="#">Videos</a>
          </li>
          <li>
            <a href="#">Reports</a>
          </li>
        </ul>
      </nav>
    </div>
    <div class="orca-topbar__end">
      <div class="orca-search">
        {% icon "search" %}
        <input class="orca-input orca-input--dense" type="search" placeholder="Search" aria-label="Search">
      </div>
      <a class="orca-icon-button orca-has-count" href="#" aria-label="Notifications, 3 unread">
        {% icon "notifications" %}
        <span class="orca-count" aria-hidden="true">3</span>
      </a>
      <button class="orca-user-chip" type="button">
        <span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span>
        <span class="orca-user-chip__text">
          <span class="orca-user-chip__name">Ada Lovelace</span>
        </span>
      </button>
    </div>
  </header>
</div>
```

**Classes:** `.orca-topbar`, `.orca-topbar__start`, `.orca-topbar__end`

**Tokens:** `--orca-brand-bar`, `--orca-brand-bar-on`, `--orca-brand-bar-hover`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI F03: Reduce the total effort of a task; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Top bar

---

## Sidebar

`id: sidebar` · level: pattern · source: Tangerine

Side navigation for an application: grouped section links that collapse to an icon rail, remembered per person.

Built from: `sidebar-link`, `nav-tree`, `collapse-toggle`

### General description

A vertical list of links down the side of an application. It shows the main sections at all times and often collapses to icons.

#### Use cases

- Applications with many sections.
- Grouping links by area, such as admin.
- Giving dense screens more room when collapsed.

#### When not to use it

- Sites with only a few sections work with a top bar.
- On phones, show these links in a drawer instead.

#### Best practices

- Group related links under short headings.
- Mark the current page.
- Remember whether the person collapsed it.
- Give icons text labels or tooltips.
- Keep the order stable between visits.

### When to use

- Applications with more than about 5 sections.

### How to use

- `<div class="orca-app">` holds `<nav class="orca-sidebar" id=… aria-label="Sections">` and `<main class="orca-app__main">`.
- Sections: `.orca-sidebar__section` with an optional `.orca-sidebar__label` and side links; `.orca-sidebar__foot` holds the collapse toggle (`data-orca-sidebar-toggle aria-controls=…`).
- Collapsed (`data-collapsed="true"`): labels are hidden visually but still read by screen readers, and the rail keeps icons. Give each link a `title` for tooltips.
- The state is remembered per sidebar in `localStorage` under `orca-sidebar:<id>`, so give the sidebar an `id`.
- Nest a nav tree inside a section for long lists, such as this documentation's navigation; hide it when collapsed.
- Below 620px the sidebar hides; put the same links in a drawer opened from the top bar.

#### Example: Sidebar with collapse

```django
<div class="orca-app" style="min-height: 22rem; border: var(--orca-border-width) solid var(--orca-border)">
  <nav class="orca-sidebar" id="sb-demo" aria-label="Sections" data-collapsed="false">
    <div class="orca-sidebar__section">
      <ul class="orca-side-nav">
        <li>
          <a class="orca-side-link" href="#" aria-current="page">
            {% icon "home" %}
            <span class="orca-side-link__label">Dashboard</span>
          </a>
        </li>
        <li>
          <a class="orca-side-link" href="#">
            {% icon "snapshot" %}
            <span class="orca-side-link__label">Videos</span>
            <span class="orca-count orca-count--neutral">12</span>
          </a>
        </li>
        <li>
          <a class="orca-side-link" href="#">
            {% icon "statistics" %}
            <span class="orca-side-link__label">Reports</span>
          </a>
        </li>
      </ul>
    </div>
    <div class="orca-sidebar__section">
      <p class="orca-sidebar__label">Admin</p>
      <ul class="orca-side-nav">
        <li>
          <a class="orca-side-link" href="#">
            {% icon "user" %}
            <span class="orca-side-link__label">Users</span>
          </a>
        </li>
        <li>
          <a class="orca-side-link" href="#">
            {% icon "settings" %}
            <span class="orca-side-link__label">Settings</span>
          </a>
        </li>
      </ul>
    </div>
    <div class="orca-sidebar__foot">
      <button class="orca-icon-button orca-sidebar__toggle" type="button" aria-controls="sb-demo" aria-expanded="true" aria-label="Collapse navigation" data-orca-sidebar-toggle>
        {% icon "chevron-left" %}
      </button>
    </div>
  </nav>
  <main class="orca-app__main">
    <h1 class="orca-page-title">Dashboard</h1>
  </main>
</div>
```

**Classes:** `.orca-app`, `.orca-app__main`, `.orca-sidebar`, `.orca-sidebar__section`, `.orca-sidebar__label`, `.orca-sidebar__foot`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Tesler's law: move unavoidable complexity from the user to the system; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Sidebar

---

## Footer

`id: footer` · level: pattern · source: ORCA

The bottom of public pages: link columns, legal text and version.

Built from: `logo-link`, `link-column`, `fine-print`

### General description

The area at the bottom of a page with links, legal text and company details. People look there for help, contact and policy links.

#### Use cases

- Contact, help and policy links.
- Legal notices and copyright.
- Secondary links not in the main navigation.

#### When not to use it

- Primary navigation belongs in the header.
- Important actions should not hide in the footer.

#### Best practices

- Group links in columns with short titles.
- Include privacy and terms links.
- Keep it simple and consistent on every page.
- Make links big enough to tap.

### When to use

- Public and documentation sites; a slim version (legal and version only) in applications.

### How to use

- `<footer class="orca-footer">` with `.orca-footer__cols` of `<ul class="orca-footer__col">` (first item `.orca-footer__col-title`) and `.orca-footer__legal`.

#### Example: Footer

```django
<footer class="orca-footer">
  {% orca_logo href="" %}
  <div class="orca-footer__cols">
    <ul class="orca-footer__col">
      <li class="orca-footer__col-title">Product</li>
      <li>
        <a href="#">Features</a>
      </li>
      <li>
        <a href="#">Pricing</a>
      </li>
    </ul>
    <ul class="orca-footer__col">
      <li class="orca-footer__col-title">Help</li>
      <li>
        <a href="#">Documentation</a>
      </li>
      <li>
        <a href="#">Contact support</a>
      </li>
    </ul>
  </div>
  <p class="orca-footer__legal">© 2026 Acme · <a href="#">Privacy</a> · <a href="#">Terms</a> · Version 0.3.0</p>
</footer>
```

**Classes:** `.orca-footer`, `.orca-footer__cols`, `.orca-footer__col`, `.orca-footer__col-title`, `.orca-footer__legal`

**Principles applied:** Jakob's law: work the way products people already know work; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Footer

---

## Page head

`id: page-head` · level: pattern · source: Tangerine

The top of a page's content: breadcrumbs or back link, title, subtitle, meta info and page actions.

Built from: `page-heading`, `breadcrumbs`, `create-button`

### General description

The top part of a page's content. It tells people where they are with a title and breadcrumbs, and offers the main actions for the page.

#### Use cases

- The top of every application page.
- Showing the title with a short description.
- Placing the main actions in a predictable spot.

#### When not to use it

- Marketing pages usually use a hero section instead.
- Actions for a single row belong in that row.

#### Best practices

- Use one clear page title.
- Show breadcrumbs or a back link to say where the page sits.
- Make one action the main one.
- Put the main action in the same place on every page.

### When to use

- The top of every application page.

### How to use

- `<div class="orca-page-head">` with `.orca-page-head__text` (breadcrumbs or back link, `h1.orca-page-title`, `.orca-page-subtitle`, `.orca-page-head__meta`) and `.orca-page-head__actions`.
- Actions: secondary buttons first, then the primary or create button; on phones they stretch full width.

#### Example: Page head

```django
<div class="orca-page-head">
  <div class="orca-page-head__text">
    <nav class="orca-breadcrumbs" aria-label="Breadcrumb">
      <ol>
        <li>
          <a href="#">Sites</a>
        </li>
        <li>
          <span aria-current="page">North building</span>
        </li>
      </ol>
    </nav>
    <h1 class="orca-page-title">Videos</h1>
    <p class="orca-page-subtitle">Every video from North building.</p>
    <p class="orca-page-head__meta">
      <span class="orca-status"><span class="orca-dot orca-dot--positive"></span>11 online</span>
      <span class="orca-status"><span class="orca-dot orca-dot--negative"></span>1 offline</span>
    </p>
  </div>
  <div class="orca-page-head__actions">
    <button class="orca-button" type="button">
      {% icon "upload" %}
      Export
    </button>
    <a class="orca-button orca-button--primary orca-create orca-create--static" href="#">
      {% icon "plus" %}
      Add video
    </a>
  </div>
</div>
```

**Classes:** `.orca-page-head`, `.orca-page-head__text`, `.orca-page-head__meta`, `.orca-page-head__actions`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI B03: One primary action; Practical UI L03: Establish an order of importance

**ORCA guide items covered:** Page head

---

## Messages region

`id: messages-region` · level: pattern · source: Tangerine

A region under the page head that shows the result of the last action, announced politely.

Built from: `flash-message`

### General description

A fixed spot on a page where messages about the result of an action appear, such as 'Saved' or a warning. Screen readers can announce them.

#### Use cases

- Confirming that a save or delete worked.
- Showing errors that need attention.
- Messages that must stay until read.

#### When not to use it

- Short, passing confirmations suit a toast.
- Errors on one field belong next to that field.

#### Best practices

- Always show messages in the same place.
- Announce them to screen readers.
- Say what happened and what to do next.
- Let people dismiss messages.
- Do not rely on colour alone.

### When to use

- Every page, in the base template, between the page head and the content.

### How to use

- `<div class="orca-messages-region" aria-live="polite">{% orca_messages %}</div>`; errors inside use `role="alert"`.
- Toasts float elsewhere; this region keeps messages until they are read.

#### Example: Region

```django
<div class="orca-messages-region" aria-live="polite">
  <div class="orca-messages">
    <div class="orca-alert orca-alert--positive" role="status">
      {% status_icon "positive" %}
      <p class="orca-alert__body">Video “Gate 1” added. Draw its zones next.</p>
      <button class="orca-icon-button orca-icon-button--dense orca-alert__close" type="button" aria-label="Dismiss message" data-orca-dismiss>
        {% icon "close" %}
      </button>
    </div>
  </div>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# Any view: add a message, then redirect (needs django.contrib.messages)
from django.contrib import messages

messages.success(request, "Report sent to 3 people.")
messages.error(request, "The export failed. Try again in a few minutes.")
# The app shell renders them; in other layouts put {% orca_messages %} at the top of the content.
```

**Classes:** `.orca-messages-region`, `.orca-messages`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Messages region

---

## Drawer

`id: drawer` · level: pattern · source: Tangerine

A panel that slides in over the page from one edge, built on the native dialog.

Built from: `dialog`, `form-actions`

### General description

A panel that slides in from the edge of the screen over the page. People can do a task there while still seeing the page behind it.

#### Use cases

- Navigation on phones.
- Filters and quick settings.
- Details of a selected row.

#### When not to use it

- Long forms need their own page.
- A short yes or no question suits a dialog.

#### Best practices

- Trap focus inside while it is open.
- Close it with Escape, the close button or a click outside.
- Give it a clear title.
- Return focus to the button that opened it.
- Keep its content short.

### When to use

- Navigation on phones, filters, details of a selected row, quick settings.

### When not to use

- Long forms: use a page.

### How to use

- `<dialog class="orca-drawer" id=… aria-labelledby=… data-orca-light-dismiss>` with `.orca-drawer__header` (title + close), `.orca-drawer__body`, `.orca-drawer__footer`.
- Open with `data-orca-dialog-open="id"`; `--left` for navigation. A click on the backdrop closes it.

#### Example: Details drawer

```django
<button class="orca-button" type="button" data-orca-dialog-open="dr-demo">Show video details</button>
<dialog class="orca-drawer" id="dr-demo" aria-labelledby="dr-demo-t" data-orca-light-dismiss>
  <div class="orca-drawer__header">
    <h2 class="orca-dialog-title" id="dr-demo-t">Entrance A</h2>
    <button class="orca-icon-button" type="button" aria-label="Close" data-orca-dialog-close>
      {% icon "close" %}
    </button>
  </div>
  <div class="orca-drawer__body">
    <dl class="orca-kv orca-kv--stacked">
      <div>
        <dt>Status</dt>
        <dd>Online</dd>
      </div>
      <div>
        <dt>Today</dt>
        <dd>4,812 visitors</dd>
      </div>
    </dl>
  </div>
  <div class="orca-drawer__footer">
    <a class="orca-button orca-button--primary" href="#">Open video</a>
    <button class="orca-button" type="button" data-orca-dialog-close>Close</button>
  </div>
</dialog>
```

**Classes:** `.orca-drawer`, `.orca-drawer--left`, `.orca-drawer__header`, `.orca-drawer__body`, `.orca-drawer__footer`

**Principles applied:** Practical UI L14: Reduce travel between related actions; Postel's law: accept varied input, output reliable and accessible UI; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Drawer

---

## Top actions header

`id: top-actions-header` · level: pattern · source: Tangerine

A thin row above a detail or form page with a back link on one side and page actions on the other.

Built from: `back-link`, `record-actions`

### General description

A thin row at the top of a detail or form page with a back link on one side and the page's actions on the other.

#### Use cases

- Detail pages reached from a list.
- Form pages with Save and Cancel actions.
- Tablet and phone layouts that need little height.

#### When not to use it

- Pages needing a title and subtitle need a full page head.
- Navigation between sections belongs in the main navigation.

#### Best practices

- Name the place the back link goes to.
- Keep the actions few.
- Put less common actions in a 'More' menu.
- Label icon-only buttons.

### When to use

- Detail and form pages reached from a list, especially on tablets and phones.

### How to use

- `<div class="orca-top-actions">` with a back link and `.orca-top-actions__end` (record actions).

#### Example: Top actions

```django
<div class="orca-top-actions">
  <a class="orca-back-link" href="#">
    {% icon "chevron-left" size="xs" %}
    Back to videos
  </a>
  <div class="orca-top-actions__end">
    <a class="orca-button orca-button--dense" href="#">
      {% icon "edit" %}
      Edit
    </a>
    <button class="orca-icon-button orca-icon-button--dense orca-icon-button--outlined" type="button" aria-label="More actions">
      {% icon "more" %}
    </button>
  </div>
</div>
```

**Classes:** `.orca-top-actions`, `.orca-top-actions__end`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI B09: Position multi-step navigation carefully

**ORCA guide items covered:** Top actions header (back link + actions)

---

## Settings panel

`id: settings-panel` · level: pattern · source: Tangerine

Grouped display preferences, theme and density, applied live. ORCA has one appearance; the project sets brand colours.

Built from: `theme-toggle`, `toggle-field`, `settings-toggle`

### General description

A panel where people adjust how the interface looks and behaves, such as theme, density or reduced motion. Changes take effect straight away.

#### Use cases

- Theme and density choices.
- Accessibility preferences such as reduced motion.
- Account preferences.

#### When not to use it

- Rarely changed technical settings belong on a settings page.
- Preferences everyone must share are project settings, not personal ones.

#### Best practices

- Group related options under clear headings.
- Apply changes at once and show the result.
- Remember choices for each person.
- Offer sensible defaults.
- Use plain labels for each option.

### When to use

- A drawer or popover opened by the settings toggle; an account preferences page.

### How to use

- `<div class="orca-settings-panel">` of `<fieldset class="orca-settings-panel__group">`: the theme toggle (Auto, Light, Dark, Paper), and switches for personal preferences such as reduced motion or compact tables.
- Apply at once and remember per person. Brand colour, accent and rounding are project settings (brand tokens), not personal: ORCA keeps one shape language.

#### Example: Panel

```django
<div class="orca-settings-panel" style="max-width: 24rem">
  <fieldset class="orca-segmented orca-settings-panel__group" data-orca-theme-choice style="flex-direction: row">
    <legend>Theme</legend>
    <label class="orca-segmented__item"><input type="radio" name="sp-theme" value="auto" checked>Auto</label>
    <label class="orca-segmented__item"><input type="radio" name="sp-theme" value="light">Light</label>
    <label class="orca-segmented__item"><input type="radio" name="sp-theme" value="dark">Dark</label>
    <label class="orca-segmented__item"><input type="radio" name="sp-theme" value="paper">Paper</label>
  </fieldset>
  <fieldset class="orca-settings-panel__group">
    <legend>Tables</legend>
    <label class="orca-switch">
      <input type="checkbox" role="switch">
      <span class="orca-switch__track"></span>
      <span>Compact rows</span>
    </label>
  </fieldset>
</div>
```

**Classes:** `.orca-settings-panel`, `.orca-settings-panel__group`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI R14: Checkbox or switch according to timing

**ORCA guide items covered:** Settings panel (appearance, theme, accent, rounding, card shadow)

---

## Filter panel

`id: filter-panel` · level: pattern · source: Tangerine

Labelled groups of filters with a result count and Clear all: the content of the filter drawer.

Built from: `choice-group`, `panel-header`, `search-field`

### General description

A set of filters in labelled groups with the number of matching results. People use it to narrow a long list or table to what they want.

#### Use cases

- Narrowing lists, tables and galleries.
- Combining several filters at once.
- Showing how many results match.

#### When not to use it

- A few simple options can be a dropdown or tabs.
- Free text search alone needs only a search field.

#### Best practices

- Group filters under clear headings.
- Show a live result count.
- Offer one 'Clear all' action.
- Put a search field first for long lists.
- Use checkboxes for choosing several values.

### When to use

- Inside the filter drawer of every page with filters.

### When not to use

- A side column of filters beside the list: page filters always open in the right drawer.

### How to use

- `<div class="orca-drawer__body orca-filter-panel">` inside the filter drawer's form (`method="get"`).
- One `<fieldset class="orca-filter-panel__group">` per dimension with checkbox lists; a search field that narrows the list goes first.
- Announce the number of results; the drawer footer's primary button repeats it ('Show 11 videos').

#### Example: Panel

```django
<form class="orca-filter-panel" method="get" aria-label="Filters" style="max-width: 15rem" onsubmit="return false">
  <div class="orca-filter-panel__head">
    <span class="orca-panel-title">Filters</span>
    <button class="orca-button orca-button--link" type="reset">Clear all</button>
  </div>
  <fieldset class="orca-filter-panel__group">
    <legend>Status</legend>
    <div class="orca-choice-group__items">
      <label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Online <span class="orca-muted">11</span></label>
      <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Offline <span class="orca-muted">1</span></label>
    </div>
  </fieldset>
  <fieldset class="orca-filter-panel__group">
    <legend>Site</legend>
    <div class="orca-choice-group__items">
      <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>North building</label>
      <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Warehouse</label>
    </div>
  </fieldset>
  <p class="orca-small orca-muted" role="status">11 videos match</p>
</form>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Filter form and list view

```python
# videos/forms.py
from django import forms

from .models import Album, Video


class VideoFilterForm(forms.Form):
    q = forms.CharField(label="Title contains", required=False)
    album = forms.ModelChoiceField(Album.objects.all(), required=False, empty_label="Any album")
    status = forms.MultipleChoiceField(choices=Video.Status.choices, required=False,
                                       widget=forms.CheckboxSelectMultiple)


# videos/views.py
from django.views.generic import ListView

from orca.mixins import OrcaPageMixin

from .forms import VideoFilterForm
from .models import Video


class VideoList(OrcaPageMixin, ListView):
    model = Video
    paginate_by = 25
    template_name = "orca/generic/list.html"   # or "orca/layouts/simple_data.html"
    list_columns = ["title", "album", "status", ("Views today", "views_today")]
    detail_url_name, create_url_name = "video-detail", "video-create"

    def get_queryset(self):
        qs = super().get_queryset()
        self.filter_form = VideoFilterForm(self.request.GET or None)
        if self.filter_form.is_valid():
            data = self.filter_form.cleaned_data
            if data["q"]:
                qs = qs.filter(title__icontains=data["q"])
            if data["album"]:
                qs = qs.filter(album=data["album"])
            if data["status"]:
                qs = qs.filter(status__in=data["status"])
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # The template puts the Filters button in the page actions and the form in the right drawer.
        ctx["filter_form"] = self.filter_form
        data = self.filter_form.cleaned_data if self.filter_form.is_valid() else {}
        ctx["active_filters"] = sum(1 for value in data.values() if value)
        return ctx
```

**Classes:** `.orca-filter-panel`, `.orca-filter-panel__head`, `.orca-filter-panel__group`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI S04: Reveal secondary information when needed

**ORCA guide items covered:** Filter panel

---

## Filter drawer

`id: filter-drawer` · level: pattern · source: Tangerine

Page filters in a right drawer opened by a Filters button in the page actions, with Show results and Clear all.

Built from: `filter-button`, `dialog`, `filter-panel`

### General description

A drawer that holds a page's filters. A button opens it, people choose filters, and the results update behind it.

#### Use cases

- Filtering lists, tables and galleries.
- Pages with many filters.
- Reports and boards.

#### When not to use it

- One or two simple filters can sit above the results.
- Quick sorting is better as a dropdown.

#### Best practices

- Show the number of applied filters on the button.
- Use a clear 'Show results' button with the count.
- List applied filters above the results so they can be removed.
- Offer 'Clear all'.
- Open it from the same place on every page.

### When to use

- Every page with filters, at every screen width: lists, tables, galleries, boards and reports.

### When not to use

- A row of filter fields above the results or a side column of filters: both move here.
- The Filters button in the list header or toolbar: it belongs to the page actions.

### How to use

- The Filters button (filter icon, number of applied filters) is in the page actions: `{% block page_actions %}`, `.orca-page-head__actions`. It has `data-orca-dialog-open="filters"`; put it before the primary action.
- `<dialog class="orca-drawer" id="filters" data-orca-light-dismiss>` (right side) holding a GET form: header with title and Close, `.orca-drawer__body.orca-filter-panel`, footer with 'Show 11 videos' (primary, the count updates live) and 'Clear all'.
- Above the results, the `filter-bar` lists the applied filters as removable tags.

#### Example: Filters from the page actions

```django
<div class="orca-page-head">
  <div class="orca-page-head__text">
    <h1 class="orca-page-title">Videos</h1>
    <p class="orca-page-subtitle">128 videos in the library.</p>
  </div>
  <div class="orca-page-head__actions">
    <button class="orca-button" type="button" data-orca-dialog-open="fd-demo">
      {% icon "filter" %}
      Filters
      <span class="orca-count orca-count--accent" aria-hidden="true">1</span>
      <span class="orca-sr-only">, 1 active</span>
    </button>
    <a class="orca-button orca-button--primary" href="#">
      {% icon "plus" %}
      Add video
    </a>
  </div>
</div>
<dialog class="orca-drawer" id="fd-demo" aria-labelledby="fd-demo-t" data-orca-light-dismiss>
  <form method="dialog" style="display: contents">
    <div class="orca-drawer__header">
      <h2 class="orca-dialog-title" id="fd-demo-t">Filters</h2>
      <button class="orca-icon-button" type="button" aria-label="Close" data-orca-dialog-close>
        {% icon "close" %}
      </button>
    </div>
    <div class="orca-drawer__body orca-filter-panel">
      <fieldset class="orca-filter-panel__group">
        <legend>Status</legend>
        <div class="orca-choice-group__items">
          <label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Published</label>
          <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Draft</label>
        </div>
      </fieldset>
    </div>
    <div class="orca-drawer__footer">
      <button class="orca-button orca-button--primary" type="submit" value="apply">Show 11 videos</button>
      <button class="orca-button orca-button--ghost" type="reset">Clear all</button>
    </div>
  </form>
</dialog>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Filter form and list view

```python
# videos/forms.py
from django import forms

from .models import Album, Video


class VideoFilterForm(forms.Form):
    q = forms.CharField(label="Title contains", required=False)
    album = forms.ModelChoiceField(Album.objects.all(), required=False, empty_label="Any album")
    status = forms.MultipleChoiceField(choices=Video.Status.choices, required=False,
                                       widget=forms.CheckboxSelectMultiple)


# videos/views.py
from django.views.generic import ListView

from orca.mixins import OrcaPageMixin

from .forms import VideoFilterForm
from .models import Video


class VideoList(OrcaPageMixin, ListView):
    model = Video
    paginate_by = 25
    template_name = "orca/generic/list.html"   # or "orca/layouts/simple_data.html"
    list_columns = ["title", "album", "status", ("Views today", "views_today")]
    detail_url_name, create_url_name = "video-detail", "video-create"

    def get_queryset(self):
        qs = super().get_queryset()
        self.filter_form = VideoFilterForm(self.request.GET or None)
        if self.filter_form.is_valid():
            data = self.filter_form.cleaned_data
            if data["q"]:
                qs = qs.filter(title__icontains=data["q"])
            if data["album"]:
                qs = qs.filter(album=data["album"])
            if data["status"]:
                qs = qs.filter(status__in=data["status"])
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # The template puts the Filters button in the page actions and the form in the right drawer.
        ctx["filter_form"] = self.filter_form
        data = self.filter_form.cleaned_data if self.filter_form.is_valid() else {}
        ctx["active_filters"] = sum(1 for value in data.values() if value)
        return ctx
```

**Classes:** `.orca-drawer`, `.orca-filter-panel`

**Principles applied:** Practical UI S04: Reveal secondary information when needed; Hick's law: fewer, clearer choices mean faster decisions; Jakob's law: work the way products people already know work; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Filter drawer

---

## Page landmarks

`id: page-landmarks` · level: pattern · source: ORCA

The regions every page has: skip navigation, the main landmark and a place for dialogs.

Built from: `skip-navigation`, `dialog`

### General description

Page landmarks are the main regions every page has, such as a skip link, the main content and navigation. They let assistive technology jump straight to the content.

#### Use cases

- Letting keyboard users skip repeated navigation.
- Helping screen-reader users move between regions.
- Giving dialogs one place to open.

#### When not to use it

- Dividing content for looks only: use plain containers.
- Multiple main areas: use only one per page.

#### Best practices

- Use one main region per page.
- Make the skip link the first thing to tab to.
- Label regions that appear more than once.
- Use real landmark elements.

### When to use

- Every page: the base layout writes them, so pages never do.

### How to use

- `<body>` starts with the skip navigation; `<main id="main" tabindex="-1">` holds the content; dialogs and drawers go in `{% block modal %}` after `</main>`.

### Accessibility

- One `<main>` per page; dialogs outside it are opened with `showModal()` so the page behind is inert.

#### Example: Landmarks (press Tab inside this example)

```django
<div style="position: relative; overflow: hidden; border: var(--orca-border-width) solid var(--orca-border)">
  <a class="orca-skip-link" href="#pl-main">Skip to main content</a>
  <div id="pl-main" tabindex="-1" style="padding: var(--orca-space-16)">
    <p class="orca-p">Main content.</p>
  </div>
</div>
```

**Classes:** `.orca-skip-link`

**Principles applied:** Jakob's law: work the way products people already know work; Tesler's law: move unavoidable complexity from the user to the system; Practical UI F01: Design for a diverse audience

**Related:** `base-layout`

---

## Error message

`id: error-message` · level: pattern · source: ORCA

What an error page says: the code, what happened in plain words, what to do, and a way back.

Built from: `empty-state`, `logo-link`, `back-link`

### General description

An error page tells people that something went wrong, such as a missing page or a server problem, in plain words and offers a way forward.

#### Use cases

- Showing a page not found (404).
- Showing no access (403) or server error (500).
- Replacing a section that cannot load.

#### When not to use it

- Mistakes in a form: show inline field errors.
- Short-lived issues: show a banner or toast.

#### Best practices

- Say what happened in plain words.
- Offer a clear next step.
- Do not blame the person.
- Never show technical traces.

### When to use

- 403, 404 and 500 pages; a section that cannot load at all.

### How to use

- `<div class="orca-error-layout">` with the logo link, an illustration, `.orca-error-layout__code`, the empty-state title and text, and one action (Go to the dashboard) plus a back link.
- Never blame the person; never show a stack trace.

#### Example: Not found

```django
<div class="orca-error-layout" style="min-height: 0">
  {% orca_logo href="#" %}
  <div class="orca-error-layout__body">
    {% orca_illustration "search" %}
    <p class="orca-error-layout__code">404</p>
    <h1 class="orca-empty-title">This page does not exist</h1>
    <p class="orca-empty-text">The link may be old, or the page was moved.</p>
    <a class="orca-button orca-button--primary" href="#">Go to the dashboard</a>
  </div>
</div>
```

**Classes:** `.orca-error-layout`, `.orca-error-layout__body`, `.orca-error-layout__code`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Practical UI W15: Help people recover from errors; Jakob's law: work the way products people already know work

**Related:** `error-layouts`

---
