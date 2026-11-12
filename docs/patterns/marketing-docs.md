# Marketing and documentation site

Sections for a product's public pages and its documentation: hero, features, live tokens, code samples and docs navigation.

## Marketing hero

`id: marketing-hero` · level: pattern · source: ORCA

The full-width opening band of a landing page: headline, lead, actions, proof points and an image, edged with the brand bar.

Built from: `hero`

### Why

The first screen decides whether people stay; one headline stating the benefit and one primary action make the next step obvious (Von Restorff, Hick's law). Proof points build trust early (Peak–end rule).

### When to use

- The top of landing and product pages.

### How to use

- `<section class="orca-marketing-hero">` wrapping the hero component; add `<ul class="orca-marketing-hero__proof">` with 2–3 factual proof points.
- Headline under 10 words; one brand or primary button and one secondary.

#### Example: Landing hero

```django
<section class="orca-marketing-hero"><div class="orca-hero">
  <div class="orca-hero__text"><p class="orca-card-kicker">People counting</p><h1 class="orca-hero__title">Know how busy every door is, right now.</h1><p class="orca-hero__lead">Publish the videos you already have. Nothing to install.</p>
    <div class="orca-row"><a class="orca-button orca-button--brand" href="#">Start free trial</a><a class="orca-button" href="#">See a demo</a></div>
    <ul class="orca-marketing-hero__proof"><li>{% icon "success" size="xs" %} 97% average accuracy</li><li>{% icon "success" size="xs" %} Works with ONVIF videos</li></ul></div>
  <div class="orca-hero__media"><img src="{% static "orca/img/sample-street.svg" %}" alt="A shop entrance seen from above"></div></div></section>
```

**Classes:** `.orca-marketing-hero`, `.orca-marketing-hero__proof`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Hick's law: fewer, clearer choices mean faster decisions; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Marketing hero

---

## Feature grid

`id: feature-grid` · level: pattern · source: ORCA

Three to six features, each an icon, a short title and one sentence.

Built from: `feature-item`

### Why

Short, parallel blocks let people scan benefits quickly (Miller's law, Practical UI W08: similar lengths); the title leads with the benefit (W04).

### When to use

- Landing pages, product overviews, release highlights.

### How to use

- `<ul class="orca-feature-grid">` of `<li class="orca-feature">` with a large icon, `.orca-feature__title` and `.orca-feature__text`.
- Keep texts to one sentence of similar length; link a feature title only when there is a page behind it.

#### Example: Features

```django
<ul class="orca-feature-grid">
  <li class="orca-feature">{% icon "statistics" size="l" %}<h3 class="orca-feature__title">Live counts</h3><p class="orca-feature__text">See how many people are inside, updated every minute.</p></li>
  <li class="orca-feature">{% icon "notifications" size="l" %}<h3 class="orca-feature__title">Capacity alerts</h3><p class="orca-feature__text">Get an email before a room or a site is too full.</p></li>
  <li class="orca-feature">{% icon "calendar" size="l" %}<h3 class="orca-feature__title">Reports by schedule</h3><p class="orca-feature__text">Daily and weekly reports land in your inbox at 07:00.</p></li>
</ul>
```

**Classes:** `.orca-feature-grid`, `.orca-feature`, `.orca-feature__title`, `.orca-feature__text`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI W08: Structure information for scanning; Practical UI W04: Lead with the information people seek

**ORCA guide items covered:** Feature grid

---

## Live design-token panel

`id: token-panel` · level: pattern · source: ORCA

Controls for the brand tokens beside a live preview, to try a brand before setting it.

Built from: `form-field`, `live-example`

### Why

Seeing a colour on real components is the only way to judge it (Practical UI C08, C09); changing it live closes the loop instantly (Doherty threshold).

### When to use

- Design-system documentation; an admin 'branding' page that writes settings.

### How to use

- `<div class="orca-token-panel">` with `.orca-token-panel__controls` (colour inputs carrying `data-orca-token="--orca-brand-strong"` and `aria-controls` pointing at the preview) and `.orca-token-panel__preview` (real components).
- The preview only shows the effect; ORCA's contrast adjustment happens when the value is saved in `settings.ORCA['BRAND']`. Show the resulting contrast next to the input.

#### Example: Try a brand colour

```django
<div class="orca-token-panel">
  <div class="orca-token-panel__controls"><div class="orca-field"><label class="orca-label" for="tp-brand">Brand fill</label><div class="orca-color"><input type="color" id="tp-brand" value="#0f95a1" data-orca-token="--orca-brand-strong" aria-controls="tp-preview"></div></div>
    <div class="orca-field"><label class="orca-label" for="tp-accent">Accent</label><div class="orca-color"><input type="color" id="tp-accent" value="#0066cc" data-orca-token="--orca-accent" aria-controls="tp-preview"></div></div></div>
  <div class="orca-token-panel__preview" id="tp-preview"><div class="orca-row"><button class="orca-button orca-button--brand" type="button">Start free trial</button><span class="orca-badge orca-badge--brand">Pro</span></div><p class="orca-p">Read the <a class="orca-link" href="#">retention policy</a>.</p><label class="orca-switch"><input type="checkbox" role="switch" checked><span class="orca-switch__track"></span><span>Email alerts</span></label></div>
</div>
```

**Classes:** `.orca-token-panel`, `.orca-token-panel__controls`, `.orca-token-panel__preview`

**Principles applied:** Practical UI C08: Choose and adapt the brand colour deliberately; Practical UI C09: Give each palette token a role; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Live design-token panel

---

## Code samples block

`id: code-samples` · level: pattern · source: ORCA

The same example in several languages or frameworks as tabs of code blocks.

Built from: `tab-bar`, `code-block`

### Why

People copy the variant for their stack; tabs keep the others out of the way (Hick's law) and Copy buttons make copying exact (Tesler's law).

### When to use

- API documentation, installation instructions for several platforms.

### How to use

- `<div class="orca-live-example">` with a tab bar (one tab per language) and code blocks as panels; remember the last chosen language.

#### Example: Samples

```django
<div class="orca-live-example"><div class="orca-tabs__list" role="tablist" aria-label="Language" data-orca-tabs><button class="orca-tab" role="tab" type="button" id="cs-1" aria-controls="cs-p1" aria-selected="true">Python</button><button class="orca-tab" role="tab" type="button" id="cs-2" aria-controls="cs-p2" aria-selected="false">curl</button></div>
  <div class="orca-tabs__panel orca-tabs__panel--code" role="tabpanel" id="cs-p1" aria-labelledby="cs-1"><div class="orca-code-block"><div class="orca-code-block__head"><span>Python</span><button class="orca-button orca-button--sm" type="button" data-orca-copy="cs-c1">{% icon "copy" class="orca-icon--copy" %}{% icon "check" class="orca-icon--copied" %}<span data-orca-copy-label>Copy</span></button></div><pre><code id="cs-c1">requests.get("https://api.example.com/v1/counts", params={"site": "north"})</code></pre></div></div>
  <div class="orca-tabs__panel orca-tabs__panel--code" role="tabpanel" id="cs-p2" aria-labelledby="cs-2" hidden><div class="orca-code-block"><div class="orca-code-block__head"><span>Shell</span><button class="orca-button orca-button--sm" type="button" data-orca-copy="cs-c2">{% icon "copy" class="orca-icon--copy" %}{% icon "check" class="orca-icon--copied" %}<span data-orca-copy-label>Copy</span></button></div><pre><code id="cs-c2">curl "https://api.example.com/v1/counts?site=north"</code></pre></div></div></div>
```

**Classes:** `.orca-live-example`, `.orca-code-block`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Code samples block

---

## Docs page header

`id: docs-page-header` · level: pattern · source: ORCA

A documentation page's breadcrumb, title, one-paragraph introduction and meta (status, source, version).

Built from: `breadcrumbs`, `page-heading`

### Why

Readers decide in seconds whether a page answers their question; a front-loaded intro (Practical UI W05) and status badges ('Released', 'Beta') answer that.

### When to use

- Every documentation page.

### How to use

- `<header class="orca-docs-head">` with breadcrumbs, the page title, a lead paragraph (max 2 sentences) and `.orca-docs-head__meta` badges.

#### Example: Header

```django
<header class="orca-docs-head"><nav class="orca-breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="#">Components</a></li><li><span aria-current="page">Forms</span></li></ol></nav>
  <h1 class="orca-page-title">Form field</h1><p class="orca-p orca-p--lead">Label, hint, error and one control, wired together. Use it for every single-value field.</p>
  <div class="orca-docs-head__meta"><span class="orca-badge orca-badge--subtle orca-badge--positive">Released</span><span class="orca-badge orca-badge--grey">Since 0.2.0</span></div></header>
```

**Classes:** `.orca-docs-head`, `.orca-docs-head__meta`

**Principles applied:** Practical UI W05: Order explanations as an inverted pyramid; Practical UI W04: Lead with the information people seek

**ORCA guide items covered:** Docs page header (title + intro)

---

## Docs sidebar tree

`id: docs-sidebar` · level: pattern · source: ORCA

The documentation sidebar: a filter box over grouped, collapsible page links, with the current page open and visible.

Built from: `docs-nav-tree`, `drawer`

### Why

Large documentation needs both browsing and finding (Miller's law, Hick's law); a filter finds a page by name while the tree teaches the structure.

### When to use

- Documentation sites. This site puts the same filter and tree inside the sidebar pattern so it can collapse to a rail.

### How to use

- `<nav class="orca-docs-sidebar" aria-label="Documentation">` with a dense search input (`data-orca-filter-list`) and the docs navigation tree; on narrow screens it moves into a left drawer.

#### Example: Sidebar

```django
<nav class="orca-docs-sidebar" aria-label="Documentation"><div class="orca-search">{% icon "search" %}<input class="orca-input orca-input--dense" type="search" placeholder="Filter pages" aria-label="Filter pages" data-orca-filter-list="dsb"></div>
  <ul class="orca-nav-tree" id="dsb"><li><details open><summary>{% icon "book" %}Get started<span class="orca-chevron">{% icon "chevron-down" size="xs" %}</span></summary><ul><li><a href="#">Installation</a></li><li><a href="#" aria-current="page">Usage</a></li></ul></details></li>
    <li><details><summary>{% icon "blueprint" %}Patterns<span class="orca-chevron">{% icon "chevron-down" size="xs" %}</span></summary><ul><li><a href="#">Data table</a></li><li><a href="#">Month calendar</a></li></ul></details></li></ul></nav>
```

**Classes:** `.orca-docs-sidebar`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Docs sidebar tree

---

## Table of contents

`id: table-of-contents` · level: pattern · source: ORCA

An "On this page" list of a long page's sections that marks the section being read.

Built from: `nav-tree`

### Why

On a long page people want to know what it covers and where they are (Miller's law); links to each section let them jump instead of scrolling, and the marked section keeps them oriented (Jakob's law).

### When to use

- Long pages of several sections: documentation, articles, guides, release notes. Put it in the right-hand column of the Blog page.

### When not to use

- Pages with fewer than three sections.
- Navigating between pages: use the nav tree or tabs.

### How to use

- `<nav aria-label="On this page"><details class="orca-toc" open data-orca-toc="body-id">` with a `<summary class="orca-toc__title">` and an `<ol class="orca-toc__list">` of links to the sections' `id`s.
- Leave the list empty and `orca.js` fills it from the `h2` headings of the element named in `data-orca-toc` (adding ids where missing), skipping headings inside live examples, code blocks and dialogs.
- `orca.js` marks the section being read with `aria-current="location"`, keeps the list open on wide screens and closed behind its summary on narrow ones; without script the list stays open.
- Keep labels to the section's name; list `h2` only.

### Accessibility

- A `nav` landmark labelled "On this page"; the current section is exposed with `aria-current="location"`, not by colour alone (bold text and a bar).

#### Example: On this page

```django
<nav aria-label="On this page" style="max-width: 14rem"><details class="orca-toc" open><summary class="orca-toc__title"><span>On this page</span><span class="orca-chevron">{% icon "chevron-down" size="xs" %}</span></summary>
  <ol class="orca-toc__list"><li><a href="#">Install</a></li><li><a href="#" aria-current="location">Configure your brand</a></li><li><a href="#">Load ORCA in a template</a></li><li><a href="#">Check your templates</a></li></ol></details></nav>
```

**Classes:** `.orca-toc`, `.orca-toc__title`, `.orca-toc__list`

**Tokens:** `--orca-brand`, `--orca-text-inactive`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Table of contents (On this page)

---
