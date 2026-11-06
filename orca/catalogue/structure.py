from .registry import Element, add, category

C = category(
    "structure", "Structure marks",
    "Marks that organise and connect: rules, separators, focus, markers and backdrops. Plus the accessibility helpers every page needs.",
)

add(Element(
    "divider", "Divider", C,
    "A horizontal or vertical rule: default, muted, medium and large spacing, labelled, highlight and brand.",
    why="A rule separates groups when space alone is not enough (Practical UI L01); used sparingly it chunks content (Miller's law).",
    when=["Between groups in a menu, between sections of a panel, between toolbar groups (vertical).",
          "Labelled: 'or' between alternative sign-in methods."],
    avoid=["Between every item: use spacing or row separators.", "To fake a heading: use a section title."],
    how=["`<hr class=\"orca-divider\">` (16px above and below). `--md` 24px, `--lg` 48px, `--flush` 0, `--muted` lighter line.",
         "Vertical: `<span class=\"orca-divider orca-divider--vertical\" role=\"separator\" aria-orientation=\"vertical\"></span>` inside a flex row.",
         "Labelled: `<div class=\"orca-divider orca-divider--labeled\" role=\"separator\">or</div>`.",
         "Emphasis: `--highlight` (3px text colour) or `--brand` (3px brand)."],
    classes=[".orca-divider", ".orca-divider--muted", ".orca-divider--md", ".orca-divider--lg", ".orca-divider--vertical",
             ".orca-divider--labeled", ".orca-divider--highlight", ".orca-divider--brand"],
    tokens=["border", "border-weak", "hairline", "bar"],
    laws=["L01", "miller"],
    examples=[("Dividers", """<div style="max-width: 24rem">
  <p class="orca-p">Above</p><hr class="orca-divider"><p class="orca-p">Below</p>
  <div class="orca-divider orca-divider--labeled" role="separator">or</div>
  <div class="orca-row"><span>Left</span><span class="orca-divider orca-divider--vertical" role="separator" aria-orientation="vertical"></span><span>Right</span></div>
  <hr class="orca-divider orca-divider--highlight orca-divider--md">
</div>""")],
    guide=["Divider", "Divider (medium, large, vertical, labeled)"],
))

add(Element(
    "chevron-separator", "Chevron separator", C,
    "A small muted chevron between breadcrumb items or path segments.",
    why="The chevron reads as 'inside' by convention (Jakob's law) and is mirrored in right-to-left languages (Postel's law).",
    when=["Breadcrumbs, path displays (Site › Building › Camera)."],
    how=["`<span class=\"orca-sep\" aria-hidden=\"true\">{% icon \"chevron-right\" %}</span>` between items.",
         "In breadcrumbs the list structure carries the meaning; the separator is hidden from screen readers."],
    classes=[".orca-sep"], tokens=["text-muted"],
    laws=["jakob", "postel"],
    examples=[("Path", """<nav aria-label="Breadcrumb" class="orca-small"><a class="orca-link orca-link--plain" href="#">Sites</a><span class="orca-sep" aria-hidden="true">{% icon "chevron-right" %}</span><a class="orca-link orca-link--plain" href="#">North building</a><span class="orca-sep" aria-hidden="true">{% icon "chevron-right" %}</span><span aria-current="page">Entrance A</span></nav>""")],
    guide=["Chevron separator"],
))

add(Element(
    "sr-only", "Screen-reader-only text", C,
    "Text that is read by assistive technology but not shown.",
    why="Some meaning is visual only (an arrow, a position in a grid); hidden text gives screen-reader users the same "
        "information (Postel's law, Practical UI F01).",
    when=["Completing a visual cue: '(opens in a new tab)', 'compared with last week', the name of an icon-only control in a table."],
    avoid=["Hiding text sighted keyboard users also need.", "Duplicating text that is already read."],
    how=["`<span class=\"orca-sr-only\">compared with last week</span>`.",
         "`.orca-sr-only-focusable` shows the element again when it receives focus."],
    classes=[".orca-sr-only", ".orca-sr-only-focusable"],
    laws=["postel", "F01"],
    examples=[("Hidden context", """<span class="orca-delta orca-delta--up">{% icon "arrow-up" size="xs" %}+8%<span class="orca-sr-only"> compared with last week</span></span>""")],
    guide=["Screen-reader-only text"],
))

add(Element(
    "skip-link", "Skip link", C,
    "The first focusable link on every page, jumping past navigation to the main content.",
    why="Keyboard and screen-reader users would otherwise tab through the whole navigation on every page (Fitts's law for "
        "the keyboard: shortest path; WCAG 2.4.1).",
    when=["Every page with navigation before the content."],
    how=["First element in `<body>`: `<a class=\"orca-skip-link\" href=\"#main\">Skip to main content</a>` and `<main id=\"main\" tabindex=\"-1\">`.",
         "It is invisible until focused, then appears top-left above everything."],
    classes=[".orca-skip-link"], tokens=["layer-skip", "bg-elevated"],
    laws=["fitts", "F01"],
    examples=[("Skip link (press Tab inside this example)", """<div style="position: relative; height: 3rem; overflow: hidden">
  <a class="orca-skip-link" href="#main">Skip to main content</a>
  <p class="orca-small orca-muted" style="padding: var(--orca-space-8)">Tab into this box to reveal the link.</p>
</div>""")],
    guide=["Skip link"],
))

add(Element(
    "focus-ring", "Focus ring", C,
    "The 3px keyboard focus outline, drawn inside controls (outside for ticks and switches).",
    why="Keyboard users must always see where they are (Von Restorff accessibility, Practical UI F10). ORCA darkens Vanilla's "
        "light-theme focus blue so the ring holds 3:1 on every ground.",
    when=["Automatically on `:focus-visible` for every interactive element. Use `.orca-focus-ring` only for custom widgets that manage focus themselves."],
    avoid=["`outline: none` without a replacement. Never remove it."],
    how=["Token: `--orca-focus`, width `--orca-focus-width` (3px), offset inside (−3px).",
         "Filled buttons switch to `--orca-focus-on-fill` or a double ring so it stays visible.",
         "Custom widget: add `.orca-focus-ring` (inside) or `.orca-focus-ring--outside` while it has focus."],
    a11y=["Shown for keyboard focus only (`:focus-visible`), never hidden for mouse focus inside text fields."],
    classes=[".orca-focus-ring", ".orca-focus-ring--outside"], tokens=["focus", "focus-width", "focus-on-fill"],
    laws=["restorff", "F10", "C01"],
    examples=[("Ring shown", """<div class="orca-row orca-row--16">
  <button class="orca-button orca-focus-ring" type="button">Focused button</button>
  <span class="orca-focus-ring--outside orca-focus-ring" style="display: inline-block; width: 1rem; height: 1rem; border: var(--orca-border-width) solid var(--orca-border-strong)"></span>
</div>""")],
    guide=["Focus ring"],
))

add(Element(
    "chevron", "Accordion chevron", C,
    "A chevron that points down when its section is open and sideways when closed.",
    why="The rotating chevron is the familiar cue for 'this expands' (Jakob's law, Practical UI F06), and its motion confirms the change.",
    when=["Disclosure and accordion triggers, collapsible sidebar groups, tree nodes."],
    how=["Inside a `<summary>` or a button with `aria-expanded`: `<span class=\"orca-chevron\">{% icon \"chevron-down\" %}</span>`. It rotates automatically when closed.",
         "Put it at the start of the row (left), in the same place on every row."],
    a11y=["`<details>`/`<summary>` or `aria-expanded` announces the state; the chevron is decorative."],
    classes=[".orca-chevron"], tokens=["duration-fast"],
    laws=["jakob", "F06"],
    examples=[("Disclosure", """<details class="orca-stack" open>
  <summary class="orca-with-icon" style="cursor: pointer; list-style: none"><span class="orca-chevron">{% icon "chevron-down" %}</span>Advanced settings</summary>
  <p class="orca-p" style="margin-inline-start: var(--orca-space-24)">Frame rate, codec and bitrate.</p>
</details>""")],
    guide=["Accordion chevron"],
))

add(Element(
    "step-marker", "Step marker", C,
    "A round marker for one step of a process: to do, current, done or error.",
    why="Showing where people are in a sequence motivates completion (goal-gradient effect, Peak–end rule) and splits long tasks (Hick's law).",
    when=["Steps of a multi-step form or setup, timelines of a process."],
    how=["`<span class=\"orca-step-marker orca-step-marker--done\"></span>` · `--current` · default (to do) · `--error`.",
         "Always next to the step's name, and the current step has `aria-current=\"step\"` on its item."],
    a11y=["The state must also be in text for screen readers: 'Step 2 of 4, current'."],
    classes=[".orca-step-marker", ".orca-step-marker--current", ".orca-step-marker--done", ".orca-step-marker--error"],
    tokens=["accent", "border-strong", "negative"],
    laws=["hick", "peak-end"],
    examples=[("Markers", """<ol class="orca-stack" style="list-style: none; padding: 0; margin: 0">
  <li class="orca-with-icon"><span class="orca-step-marker orca-step-marker--done"></span>Connect recorder<span class="orca-sr-only">, done</span></li>
  <li class="orca-with-icon" aria-current="step"><span class="orca-step-marker orca-step-marker--current"></span><strong>Choose cameras</strong><span class="orca-sr-only">, current step</span></li>
  <li class="orca-with-icon"><span class="orca-step-marker orca-step-marker--error"></span>Test streams<span class="orca-sr-only">, has errors</span></li>
  <li class="orca-with-icon"><span class="orca-step-marker"></span>Draw zones</li>
</ol>""")],
    guide=["Step marker"],
))

add(Element(
    "carousel-dot", "Carousel dot", C,
    "A position marker and button for one slide of a carousel or gallery.",
    why="Dots show how many items there are and which is shown (Practical UI S06: show that more exists). The current dot "
        "changes shape, not only colour (C03), and the target is a full 29px/44px button (Fitts's law).",
    when=["Carousels and image galleries with fewer than about 8 items."],
    avoid=["Many items: show a count ('3 of 24') and thumbnails instead."],
    how=["`<button class=\"orca-carousel-dot\" type=\"button\" aria-label=\"Show image 2 of 5\" aria-current=\"true\"></button>`; one per slide in a group with `aria-label`."],
    classes=[".orca-carousel-dot"], tokens=["text", "border-strong"],
    laws=["S06", "C03", "fitts"],
    examples=[("Dots", """<div class="orca-row" role="group" aria-label="Choose image" style="gap: 0">
  <button class="orca-carousel-dot" type="button" aria-label="Show image 1 of 4"></button>
  <button class="orca-carousel-dot" type="button" aria-label="Show image 2 of 4" aria-current="true"></button>
  <button class="orca-carousel-dot" type="button" aria-label="Show image 3 of 4"></button>
  <button class="orca-carousel-dot" type="button" aria-label="Show image 4 of 4"></button>
</div>""")],
    guide=["Carousel dot"], source="ORCA",
))

add(Element(
    "pagination-gap", "Pagination gap (ellipsis)", C,
    "The ellipsis between page numbers that are not shown.",
    why="It tells people pages exist between the shown numbers without listing them all (Hick's law; S06).",
    when=["Pagination with more than 7 pages."],
    how=["`<span class=\"orca-page-gap\" aria-hidden=\"true\">…</span>` between page links. Not focusable."],
    classes=[".orca-page-gap"], tokens=["text-muted", "control-md"],
    laws=["hick", "S06"],
    examples=[("Gap", """<div class="orca-row"><a class="orca-button" href="#">1</a><span class="orca-page-gap" aria-hidden="true">…</span><a class="orca-button" href="#" aria-current="page" style="background: var(--orca-bg-active)">7</a><span class="orca-page-gap" aria-hidden="true">…</span><a class="orca-button" href="#">24</a></div>""")],
    guide=["Pagination gap (ellipsis)"],
))

add(Element(
    "dialog-backdrop", "Dialog backdrop", C,
    "The dimmed layer behind a modal dialog, plus the dialog surface itself.",
    why="Dimming the page focuses attention on the decision (Von Restorff) and signals that the page is paused; the deliberate "
        "pause is useful friction before an irreversible action (Doherty: friction).",
    when=["Modal confirmations and short focused tasks that must finish before going back."],
    avoid=["Information people need to compare with the page behind: use a drawer or inline panel."],
    how=["Use the native element: `<dialog class=\"orca-dialog\" aria-labelledby=…>` opened with `showModal()`; `::backdrop` is styled.",
         "Non-native overlays: `<div class=\"orca-backdrop\"></div>` (`--contained` to stay in a parent).",
         "Body padding 24px; actions at the bottom; Escape and a Cancel button close it."],
    a11y=["`showModal()` traps focus and restores it on close; return focus to the opener."],
    classes=[".orca-dialog", ".orca-backdrop"], tokens=["bg-overlay", "bg-elevated", "shadow-dragged", "layer-dialog"],
    laws=["restorff", "doherty", "B13"],
    examples=[("Dialog", """<button class="orca-button" type="button" onclick="this.nextElementSibling.showModal()">Open dialog</button>
<dialog class="orca-dialog" aria-labelledby="dlg-demo-title">
  <form method="dialog" style="padding: var(--orca-space-24)" class="orca-stack">
    <h2 class="orca-dialog-title" id="dlg-demo-title">Delete Entrance A?</h2>
    <p class="orca-p">Its counts are kept. Its zones and alert rules are deleted.</p>
    <div class="orca-row"><button class="orca-button orca-button--danger" type="submit" value="delete">Delete camera</button><button class="orca-button" type="submit" value="cancel" autofocus>Cancel</button></div>
  </form>
</dialog>""")],
    guide=["Dialog backdrop"],
))

add(Element(
    "drawer-backdrop", "Drawer backdrop", C,
    "The scrim behind a side drawer; pressing it closes the drawer.",
    why="The scrim shows the drawer sits above the page and offers a large, familiar target to dismiss it (Fitts's law, Jakob's law).",
    when=["Behind navigation drawers on phones and filter drawers."],
    how=["`<div class=\"orca-scrim\" data-close></div>` before the drawer; `--contained` keeps it inside a positioned parent.",
         "Clicking the scrim must do the same as the drawer's Close button; Escape too."],
    classes=[".orca-scrim", ".orca-scrim--contained"], tokens=["bg-overlay", "layer-drawer"],
    laws=["fitts", "jakob"],
    examples=[("Contained scrim", """<div style="position: relative; height: 8rem; overflow: hidden; border: var(--orca-border-width) solid var(--orca-border)">
  <p class="orca-p" style="padding: var(--orca-space-16)">Page content</p>
  <div class="orca-scrim orca-scrim--contained"></div>
  <aside class="orca-elevation-2" style="position: absolute; top: 0; bottom: 0; right: 0; width: 60%; padding: var(--orca-space-16); z-index: calc(var(--orca-layer-drawer) + 1)"><p class="orca-dialog-title">Filters</p></aside>
</div>""")],
    guide=["Drawer backdrop"],
))
