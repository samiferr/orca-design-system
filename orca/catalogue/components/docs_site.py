from ..registry import add, category
from . import Component

C = category(
    "docs-site", "Documentation site",
    "Components for documenting a design system or an API: live examples, code blocks and the navigation tree.",
    level="component",
)

add(Component(
    "live-example", "Live example", C,
    "A rendered example and its source as two tabs.",
    why="Seeing the result and the code side by side lets people copy exactly what they saw (Jakob's law, Tesler's law); tabs keep the code out of the way until wanted.",
    when=["Design-system documentation, component galleries, internal style guides."],
    how=["`<div class=\"orca-live-example\">` with a tab bar (Preview, Code) and two panels; the code panel holds a code block.",
         "Render the preview from the same source string you print, so they can never differ (this site does)."],
    classes=[".orca-live-example"],
    laws=["jakob", "tesler"],
    uses=["tab-bar", "code-block"],
    examples=[("Example", """<div class="orca-live-example">
  <div class="orca-tabs__list" role="tablist" aria-label="Example" data-orca-tabs><button class="orca-tab" role="tab" type="button" id="le-t1" aria-controls="le-p1" aria-selected="true">Preview</button><button class="orca-tab" role="tab" type="button" id="le-t2" aria-controls="le-p2" aria-selected="false">Code</button></div>
  <div class="orca-tabs__panel" role="tabpanel" id="le-p1" aria-labelledby="le-t1"><button class="orca-button orca-button--primary" type="button">Save video</button></div>
  <div class="orca-tabs__panel orca-tabs__panel--code" role="tabpanel" id="le-p2" aria-labelledby="le-t2" hidden><div class="orca-code-block"><pre><code>&lt;button class="orca-button orca-button--primary" type="button"&gt;Save video&lt;/button&gt;</code></pre></div></div>
</div>""")],
    guide=["Live example (preview and code tabs)"],
))

add(Component(
    "code-block", "Code block", C,
    "Multi-line code with its language and a Copy button.",
    why="Copying code by selecting is error-prone; a Copy button with confirmation is exact and fast (Doherty threshold, Tesler's law). A monospaced face keeps similar characters distinct (Practical UI T01).",
    when=["Commands, configuration and code samples in documentation and settings (API keys use the copy button)."],
    how=["`<div class=\"orca-code-block\"><div class=\"orca-code-block__head\"><span>Python</span><button class=\"orca-button orca-button--sm\" type=\"button\" data-orca-copy=\"code-id\"><span data-orca-copy-label>Copy</span></button></div><pre><code id=\"code-id\">…</code></pre></div>`.",
         "The Copy button carries the copy icon and a check icon (`class=\"orca-icon--copy\"` and `\"orca-icon--copied\"`); the check shows while it says Copied.",
         "Code is coloured by `orca.js` (the vendored highlight.js, loaded only on pages with code) in the `--orca-code-*` colours of the theme, "
         "set in the JetBrains Mono font. Name the language with `data-orca-highlight=\"python\"` on the `<code>`, or leave it out to detect it.",
         "Lines scroll sideways instead of wrapping; keep samples short and runnable."],
    classes=[".orca-code-block", ".orca-code-block__head", ".orca-hl-keyword", ".orca-hl-string", ".orca-hl-comment"],
    tokens=["font-mono", "code-keyword", "code-tag", "code-attr", "code-string", "code-number", "code-template", "code-title", "code-comment"],
    laws=["doherty", "tesler", "T01"],
    uses=["copy-button"],
    examples=[("Settings", """<div class="orca-code-block" style="max-width: 32rem"><div class="orca-code-block__head"><span>Python</span><button class="orca-button orca-button--sm" type="button" data-orca-copy="cbk-1">{% icon "copy" class="orca-icon--copy" %}{% icon "check" class="orca-icon--copied" %}<span data-orca-copy-label>Copy</span></button></div><pre><code id="cbk-1" data-orca-highlight="python">ORCA = {
    "BRAND": {"name": "Acme", "color": "#0f95a1"},
}</code></pre></div>""")],
    guide=["Code block"],
))

add(Component(
    "docs-nav-tree", "Docs navigation tree", C,
    "A documentation sidebar: a filter box above a nav tree of sections and pages.",
    why="Documentation has many pages; filtering by name finds one faster than browsing (Hick's law), while the grouped tree teaches the structure (Miller's law).",
    when=["Documentation sites and long help centres (this site uses it)."],
    how=["A search field with `data-orca-filter-list=\"tree-id\"` above a nav tree `<ul id=\"tree-id\">`; matching sections open while filtering, empty ones hide.",
         "Keep the current page highlighted and scrolled into view."],
    classes=[".orca-nav-tree", ".orca-search"],
    laws=["hick", "miller"],
    uses=["nav-tree", "search-field"],
    examples=[("Docs tree", """<nav aria-label="Documentation" style="max-width: 16rem">
  <div class="orca-search" style="margin-bottom: var(--orca-space-8)">{% icon "search" %}<input class="orca-input orca-input--dense" type="search" placeholder="Filter pages" aria-label="Filter pages" data-orca-filter-list="dnt"></div>
  <ul class="orca-nav-tree" id="dnt">
    <li><details open><summary>{% icon "book" %}Get started<span class="orca-chevron">{% icon "chevron-down" size="xs" %}</span></summary><ul><li><a href="#">Installation</a></li><li><a href="#" aria-current="page">Usage</a></li></ul></details></li>
    <li><details><summary>{% icon "grid" %}Forms<span class="orca-chevron">{% icon "chevron-down" size="xs" %}</span></summary><ul><li><a href="#">Form field</a></li><li><a href="#">Combobox</a></li></ul></details></li>
  </ul>
</nav>""")],
    guide=["Docs navigation tree"],
))
