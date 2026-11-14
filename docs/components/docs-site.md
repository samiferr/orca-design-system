# Documentation site

Components for documenting a design system or API: live examples, code blocks and a navigation tree.

## Live example

`id: live-example` · level: component · source: ORCA

A rendered example and its source as two tabs.

Built from: `tab-bar`, `code-block`

### General description

A panel that shows a working example of a piece of interface next to the code that makes it.

#### Use cases

- Design-system and component documentation.
- Style guides and tutorials.
- Showing how an API or widget behaves.

#### When not to use it

- Long code files: link to the source instead.
- Screenshots of static content: use an image.

#### Best practices

- Make sure the preview and code match.
- Show the preview first, code second.
- Let people copy the code easily.
- Keep each example small and focused.

### When to use

- Design-system documentation, component galleries, internal style guides.

### How to use

- `<div class="orca-live-example">` with a tab bar (Preview, Code) and two panels; the code panel holds a code block.
- Render the preview from the same source string you print so they never differ (this site does).

#### Example: Example

```django
<div class="orca-live-example">
  <div class="orca-tabs__list" role="tablist" aria-label="Example" data-orca-tabs>
    <button class="orca-tab" role="tab" type="button" id="le-t1" aria-controls="le-p1" aria-selected="true">Preview</button>
    <button class="orca-tab" role="tab" type="button" id="le-t2" aria-controls="le-p2" aria-selected="false">Code</button>
  </div>
  <div class="orca-tabs__panel" role="tabpanel" id="le-p1" aria-labelledby="le-t1">
    <button class="orca-button orca-button--primary" type="button">Save video</button>
  </div>
  <div class="orca-tabs__panel orca-tabs__panel--code" role="tabpanel" id="le-p2" aria-labelledby="le-t2" hidden>
    <div class="orca-code-block">
      <pre><code>&lt;button class="orca-button orca-button--primary" type="button"&gt;Save video&lt;/button&gt;</code></pre>
    </div>
  </div>
</div>
```

**Classes:** `.orca-live-example`

**Principles applied:** Jakob's law: work the way products people already know work; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Live example (preview and code tabs)

---

## Code block

`id: code-block` · level: component · source: ORCA

Multi-line code with its language and a Copy button.

Built from: `copy-button`

### General description

A formatted area that shows lines of code or commands in an even-width font, usually with a copy button.

#### Use cases

- Documentation with commands and examples.
- Showing settings or configuration.
- Sharing API keys or tokens that people copy.

#### When not to use it

- A single word or short name in a sentence: use inline code.
- Long files: link to the source.

#### Best practices

- Offer a Copy button and confirm it worked.
- Name the language.
- Keep samples short and runnable.
- Scroll sideways instead of wrapping lines.

### When to use

- Commands, configuration and code samples in docs and settings (API keys use the copy button).

### How to use

- `<div class="orca-code-block"><div class="orca-code-block__head"><span>Python</span><button class="orca-button orca-button--sm" type="button" data-orca-copy="code-id"><span data-orca-copy-label>Copy</span></button></div><pre><code id="code-id">…</code></pre></div>`.
- The Copy button holds a copy icon and a check icon (`class="orca-icon--copy"` and `"orca-icon--copied"`); the check shows while it says Copied.
- `orca.js` colours code (using the vendored highlight.js, loaded only on pages with code) in the theme's `--orca-code-*` colours, in the JetBrains Mono font. Name the language with `data-orca-highlight="python"` on the `<code>`, or leave it out to detect it.
- Lines scroll sideways instead of wrapping; keep samples short and runnable.

#### Example: Settings

```django
<div class="orca-code-block" style="max-width: 32rem">
  <div class="orca-code-block__head">
    <span>Python</span>
    <button class="orca-button orca-button--sm" type="button" data-orca-copy="cbk-1">
      {% icon "copy" class="orca-icon--copy" %}
      {% icon "check" class="orca-icon--copied" %}
      <span data-orca-copy-label>Copy</span>
    </button>
  </div>
  <pre><code id="cbk-1" data-orca-highlight="python">ORCA = {
    "BRAND": {"name": "Acme", "color": "#0f95a1"},
}</code></pre>
</div>
```

**Classes:** `.orca-code-block`, `.orca-code-block__head`, `.orca-hl-keyword`, `.orca-hl-string`, `.orca-hl-comment`

**Tokens:** `--orca-font-mono`, `--orca-code-keyword`, `--orca-code-tag`, `--orca-code-attr`, `--orca-code-string`, `--orca-code-number`, `--orca-code-template`, `--orca-code-title`, `--orca-code-comment`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Tesler's law: move unavoidable complexity from the user to the system; Practical UI T01: One legible sans serif family

**ORCA guide items covered:** Code block

---

## Docs navigation tree

`id: docs-nav-tree` · level: component · source: ORCA

A documentation sidebar: an optional filter box and an optional Collapse all button above a tree of sections and pages.

Built from: `nav-tree`, `search-field`

### General description

A side menu for documentation that groups pages into sections and often has a search box to find a page quickly.

#### Use cases

- Documentation sites with many pages.
- Help centres.
- Design-system guides.

#### When not to use it

- Sites with only a few pages: use a simple menu.
- Main product navigation: use a site menu.

#### Best practices

- Group pages into clear sections.
- Highlight the current page.
- Let people filter by name.
- Keep section names short.

### When to use

- Documentation sites and long help centres (this site uses it).

### How to use

- A search field with `data-orca-filter-list="tree-id"` above a nav tree `<ul id="tree-id">`; while filtering, matching sections open and empty ones hide.
- Both tools are optional. Leave the filter out for a short tree (under about ten pages); add the Collapse all button (`data-orca-tree-toggle aria-controls="tree-id"`, an icon button holding the `collapse` and `expand` icons) for a long one. It collapses every section while any is open, then offers Expand all, and its label follows.
- In the docs layout, pass `sidebar_search=False` to drop the filter (on by default) and `sidebar_collapse_all=True` to add the button (off by default).
- Keep the current page highlighted and scrolled into view.

#### Example: Docs tree

```django
<nav aria-label="Documentation" style="max-width: 16rem">
  <div class="orca-docs-sidebar__tools" style="margin-inline: 0">
    <div class="orca-search">
      {% icon "search" %}
      <input class="orca-input orca-input--dense" type="search" placeholder="Filter pages" aria-label="Filter pages" data-orca-filter-list="dnt">
    </div>
    <button class="orca-icon-button orca-icon-button--dense" type="button" aria-controls="dnt" aria-label="Collapse all sections" title="Collapse all sections" data-orca-tree-toggle>
      {% icon "collapse" class="orca-icon--collapse" %}
      {% icon "expand" class="orca-icon--expand" %}
    </button>
  </div>
  <ul class="orca-nav-tree" id="dnt">
    <li>
      <details open>
        <summary>
          {% icon "book" %}
          Get started
          <span class="orca-chevron">
            {% icon "chevron-down" size="xs" %}
          </span>
        </summary>
        <ul>
          <li>
            <a href="#">Installation</a>
          </li>
          <li>
            <a href="#" aria-current="page">Usage</a>
          </li>
        </ul>
      </details>
    </li>
    <li>
      <details>
        <summary>
          {% icon "grid" %}
          Forms
          <span class="orca-chevron">
            {% icon "chevron-down" size="xs" %}
          </span>
        </summary>
        <ul>
          <li>
            <a href="#">Form field</a>
          </li>
          <li>
            <a href="#">Combobox</a>
          </li>
        </ul>
      </details>
    </li>
  </ul>
</nav>
```

**Classes:** `.orca-nav-tree`, `.orca-search`, `.orca-docs-sidebar__tools`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Docs navigation tree

---
