# Documentation site

Components for documenting a design system or an API: live examples, code blocks and the navigation tree.

## Live example

`id: live-example` · level: component · source: ORCA

A rendered example and its source as two tabs.

Built from: `tab-bar`, `code-block`

### Why

Seeing the result and the code side by side lets people copy exactly what they saw (Jakob's law, Tesler's law); tabs keep the code out of the way until wanted.

### When to use

- Design-system documentation, component galleries, internal style guides.

### How to use

- `<div class="orca-live-example">` with a tab bar (Preview, Code) and two panels; the code panel holds a code block.
- Render the preview from the same source string you print, so they can never differ (this site does).

#### Example: Example

```django
<div class="orca-live-example">
  <div class="orca-tabs__list" role="tablist" aria-label="Example" data-orca-tabs><button class="orca-tab" role="tab" type="button" id="le-t1" aria-controls="le-p1" aria-selected="true">Preview</button><button class="orca-tab" role="tab" type="button" id="le-t2" aria-controls="le-p2" aria-selected="false">Code</button></div>
  <div class="orca-tabs__panel" role="tabpanel" id="le-p1" aria-labelledby="le-t1"><button class="orca-button orca-button--primary" type="button">Save video</button></div>
  <div class="orca-tabs__panel orca-tabs__panel--code" role="tabpanel" id="le-p2" aria-labelledby="le-t2" hidden><div class="orca-code-block"><pre><code>&lt;button class="orca-button orca-button--primary" type="button"&gt;Save video&lt;/button&gt;</code></pre></div></div>
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

### Why

Copying code by selecting is error-prone; a Copy button with confirmation is exact and fast (Doherty threshold, Tesler's law). A monospaced face keeps similar characters distinct (Practical UI T01).

### When to use

- Commands, configuration and code samples in documentation and settings (API keys use the copy button).

### How to use

- `<div class="orca-code-block"><div class="orca-code-block__head"><span>Python</span><button class="orca-button orca-button--sm" type="button" data-orca-copy="code-id"><span data-orca-copy-label>Copy</span></button></div><pre><code id="code-id">…</code></pre></div>`.
- The Copy button carries the copy icon and a check icon (`class="orca-icon--copy"` and `"orca-icon--copied"`); the check shows while it says Copied.
- Code is coloured by `orca.js` (the vendored highlight.js, loaded only on pages with code) in the `--orca-code-*` colours of the theme, set in the JetBrains Mono font. Name the language with `data-orca-highlight="python"` on the `<code>`, or leave it out to detect it.
- Lines scroll sideways instead of wrapping; keep samples short and runnable.

#### Example: Settings

```django
<div class="orca-code-block" style="max-width: 32rem"><div class="orca-code-block__head"><span>Python</span><button class="orca-button orca-button--sm" type="button" data-orca-copy="cbk-1">{% icon "copy" class="orca-icon--copy" %}{% icon "check" class="orca-icon--copied" %}<span data-orca-copy-label>Copy</span></button></div><pre><code id="cbk-1" data-orca-highlight="python">ORCA = {
    "BRAND": {"name": "Acme", "color": "#0f95a1"},
}</code></pre></div>
```

**Classes:** `.orca-code-block`, `.orca-code-block__head`, `.orca-hl-keyword`, `.orca-hl-string`, `.orca-hl-comment`

**Tokens:** `--orca-font-mono`, `--orca-code-keyword`, `--orca-code-tag`, `--orca-code-attr`, `--orca-code-string`, `--orca-code-number`, `--orca-code-template`, `--orca-code-title`, `--orca-code-comment`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Tesler's law: move unavoidable complexity from the user to the system; Practical UI T01: One legible sans serif family

**ORCA guide items covered:** Code block

---

## Docs navigation tree

`id: docs-nav-tree` · level: component · source: ORCA

A documentation sidebar: a filter box above a nav tree of sections and pages.

Built from: `nav-tree`, `search-field`

### Why

Documentation has many pages; filtering by name finds one faster than browsing (Hick's law), while the grouped tree teaches the structure (Miller's law).

### When to use

- Documentation sites and long help centres (this site uses it).

### How to use

- A search field with `data-orca-filter-list="tree-id"` above a nav tree `<ul id="tree-id">`; matching sections open while filtering, empty ones hide.
- Keep the current page highlighted and scrolled into view.

#### Example: Docs tree

```django
<nav aria-label="Documentation" style="max-width: 16rem">
  <div class="orca-search" style="margin-bottom: var(--orca-space-8)">{% icon "search" %}<input class="orca-input orca-input--dense" type="search" placeholder="Filter pages" aria-label="Filter pages" data-orca-filter-list="dnt"></div>
  <ul class="orca-nav-tree" id="dnt">
    <li><details open><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>Get started</summary><ul><li><a href="#">Installation</a></li><li><a href="#" aria-current="page">Usage</a></li></ul></details></li>
    <li><details><summary><span class="orca-chevron">{% icon "chevron-down" %}</span>Forms</summary><ul><li><a href="#">Form field</a></li><li><a href="#">Combobox</a></li></ul></details></li>
  </ul>
</nav>
```

**Classes:** `.orca-nav-tree`, `.orca-search`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Docs navigation tree

---
