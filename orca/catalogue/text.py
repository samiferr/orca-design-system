from .registry import Element, add, category

C = category(
    "text", "Text",
    "Text styles with a fixed role. Choose by what the text is (a page title, a stat value), not by how big you want it.",
)

add(Element(
    "heading", "Heading (h1–h6)", C,
    "Document headings from h1 to h6, plus a display style for marketing pages.",
    why="A heading outline lets people scan and lets screen-reader users jump between sections (Miller's law: "
        "chunking; Practical UI W08). Tangerine's thin h2 is the system's typographic signature.",
    when=["Structuring long content: docs, settings pages, reports.",
          "Marketing pages: `.orca-display` for the one hero line."],
    avoid=["Choosing a heading level for its size: keep levels in order and restyle with a class if needed.",
           "Page and panel titles in applications: use `page-title` and `panel-title`."],
    how=["Use real `<h1>`–`<h6>` elements with `.orca-h1`…`.orca-h6`.",
         "One `<h1>` per page. Never skip a level going down.",
         "h1 and h2 are 42/48 from 1036px and 32/40 below; h4 (light) suits dialog and empty-state titles.",
         "Write in sentence case, no full stop (W02, W12)."],
    a11y=["The heading level conveys structure; the class only changes looks."],
    classes=[".orca-h1", ".orca-h2", ".orca-h3", ".orca-h4", ".orca-h5", ".orca-h6", ".orca-display"],
    tokens=["type-h1", "type-h2", "type-h3", "type-h4", "type-h5", "type-h6", "type-display"],
    laws=["miller", "W02", "T05"],
    examples=[("Levels", """<h1 class="orca-h1">Capacity report</h1>
<h2 class="orca-h2">Weekly overview</h2>
<h3 class="orca-h3">Entrances</h3>
<h4 class="orca-h4">No data for this week</h4>""")],
    guide=["Heading (h1–h6)"],
    related=["page-title", "section-title"],
))

add(Element(
    "page-title", "Page title", C,
    "The single title naming what this page is.",
    why="People confirm they are in the right place from the title first (Jakob's law); one clear title gives "
        "the page a single focal point (Von Restorff).",
    when=["Top of every application page, inside the page head, beside the page actions."],
    avoid=["Repeating the product name or the breadcrumb's last item word for word with extra decoration.",
           "Long titles: front-load the distinguishing word (W04)."],
    how=["`<h1 class=\"orca-page-title\">` (28/36, weight 700).",
         "Name the object, not the action: 'Videos', 'Harbour at dusk', 'New album'.",
         "Long names wrap; they are never cut, so people can always read the full name (L15).",
         "On application pages it sits in the `page-head` pattern, with the page actions beside it."],
    a11y=["It is the page's `<h1>`; the document `<title>` should start with the same words."],
    classes=[".orca-page-title"], tokens=["type-page-title"],
    laws=["jakob", "restorff", "W04", "L15"],
    examples=[("Page title with subtitle", """<div>
  <h1 class="orca-page-title">Harbour at dusk</h1>
  <p class="orca-page-subtitle">Added to the library on 3 March 2026.</p>
</div>""")],
    guide=["Page title"],
    related=["page-subtitle", "heading"],
))

add(Element(
    "page-subtitle", "Page subtitle", C,
    "One sentence under the page title that says what the page is for or about.",
    why="A short orientation sentence answers 'what can I do here' without a manual (Tesler: help in context; "
        "paradox of the active user).",
    when=["Pages whose purpose is not obvious from the title, or that need one key fact (scope, time range)."],
    avoid=["Repeating the title.", "Instructions longer than one sentence: put them in help text where they are needed."],
    how=["`<p class=\"orca-page-subtitle\">` directly after the page title; muted, max 70ch.",
         "Under 20 words (W01). A full sentence ends with a full stop."],
    classes=[".orca-page-subtitle"], tokens=["text-muted", "measure"],
    laws=["tesler", "W01"],
    examples=[("Subtitle", """<h1 class="orca-page-title">Alert rules</h1>
<p class="orca-page-subtitle">Rules decide who gets an email when a video upload fails or a KPI crosses a limit.</p>""")],
    guide=["Page subtitle"],
))

add(Element(
    "section-title", "Section title", C,
    "Title of a section inside a page (a group of panels or a long form part).",
    why="Section titles chunk a long page into a few recognisable parts (Miller's law, Practical UI R17).",
    when=["Splitting a page into two or more regions; grouping fields of a long form."],
    avoid=["A section with a single panel that already has a title: use only the panel title."],
    how=["`<h2 class=\"orca-section-title\">` (24/32, 550), with `--orca-space-16` below and `--orca-space-32` above.",
         "Descriptive words people scan for: 'Notifications', not 'Other'."],
    classes=[".orca-section-title"], tokens=["type-h3"],
    laws=["miller", "R17", "W08"],
    examples=[("Section title", """<h2 class="orca-section-title">Notifications</h2>""")],
    guide=["Section title"],
))

add(Element(
    "panel-title", "Panel title", C,
    "Title at the top of a panel or card group of content.",
    why="Each panel answers one question; its title names that question so it can be found by scanning (Miller's law).",
    when=["Head of every panel, card group, table card or chart frame."],
    avoid=["Uppercase or coloured titles: they look like labels or links."],
    how=["`<h2 class=\"orca-panel-title\">` or `<h3>` depending on the outline (18/24, 550).",
         "Optional muted description under it with `.orca-small.orca-muted`."],
    classes=[".orca-panel-title"], tokens=["type-title"],
    laws=["miller", "L03"],
    examples=[("Panel title", """<h2 class="orca-panel-title">People counted today</h2>
<p class="orca-small orca-muted">All entrances, updated every minute.</p>""")],
    guide=["Panel title"],
))

add(Element(
    "alert-title", "Alert title", C,
    "Bold first line of an alert, callout or notification that states what happened.",
    why="People read the first words and decide; a bold, specific title is enough on its own to act (Practical UI W15).",
    when=["Every alert or callout with more than one sentence."],
    how=["`<p class=\"orca-alert-title\">` (16/24, 550).", "State the fact: 'Video unavailable', 'Report sent'. No 'Error:' prefix, no exclamation marks."],
    classes=[".orca-alert-title"], tokens=["type-body-strong"],
    laws=["W15", "peak-end"],
    examples=[("Alert title", """<p class="orca-alert-title">Video unavailable</p>
<p class="orca-p">The file could not be loaded. Check your connection, then try playing it again.</p>""")],
    guide=["Alert title"],
))

add(Element(
    "paragraph", "Paragraph", C,
    "Running text at 16/24 with a 70-character measure.",
    why="Comfortable line length and line height make reading effortless (Practical UI T07, T09).",
    when=["Any sentence-level text: descriptions, explanations, dialog bodies."],
    avoid=["Walls of text: split into short paragraphs and lists (W08)."],
    how=["`<p class=\"orca-p\">`. Lead paragraph: `.orca-p--lead` (18/28).",
         "Front-load the point; one idea per paragraph; under 20 words per sentence where possible."],
    classes=[".orca-p", ".orca-p--lead"], tokens=["type-body", "measure"],
    laws=["T07", "T09", "W01", "W05"],
    examples=[("Paragraphs", """<p class="orca-p orca-p--lead">Thumbnails are taken from each video at a fixed interval.</p>
<p class="orca-p">Use them to check framing before you draw zones. Shots are kept for 30 days.</p>""")],
    guide=["Paragraph"],
))

add(Element(
    "text-link", "Text link", C,
    "An underlined, accent-coloured link inside text.",
    why="Colour plus underline is the convention people recognise without thinking (Jakob's law, Practical UI S03) "
        "and it survives colour-blindness (C03).",
    when=["Navigation to another page or resource from within text."],
    avoid=["Actions that change data: use a button.", "'Click here' or 'Learn more': name the destination (W14)."],
    how=["`<a class=\"orca-link\" href=…>`. In navigation lists where position already signals a link: `.orca-link--quiet`.",
         "External links: add `.orca-link--external` (adds ↗) and say so in the text when it matters.",
         "Visited state uses `--orca-link-visited` except with `.orca-link--plain` (for app navigation)."],
    a11y=["Link text must make sense read alone, as screen-reader users list links.",
          "Focus shows the 3px ring; hover thickens the underline."],
    classes=[".orca-link", ".orca-link--quiet", ".orca-link--external", ".orca-link--plain"],
    tokens=["accent", "accent-hover", "link-visited"],
    laws=["jakob", "S03", "W14", "C03"],
    examples=[("Links", """<p class="orca-p">Shots are deleted after 30 days. Change this in <a class="orca-link orca-link--plain" href="#">retention settings</a>.</p>
<p class="orca-p"><a class="orca-link orca-link--external" href="https://www.w3.org/WAI/">WCAG overview</a></p>""")],
    guide=["Text link"],
    related=["link-action"],
))

add(Element(
    "muted-text", "Muted text", C,
    "Secondary text in `--orca-text-muted` (60% ink, still 4.5:1).",
    why="Lowering the weight of secondary information lets the primary information lead (Practical UI L03) while "
        "staying readable (T13: never pale grey).",
    when=["Meta information, descriptions under titles, empty values ('Not set'), counts beside labels."],
    avoid=["Placeholder-like grey for content people must read to finish the task.", "Disabled meaning: use the disabled state."],
    how=["Add `.orca-muted` to any text element."],
    classes=[".orca-muted"], tokens=["text-muted"],
    laws=["L03", "T13"],
    examples=[("Muted", """<p class="orca-p">Summer 2026 <span class="orca-muted">· 3 videos</span></p>""")],
    guide=["Muted text"],
))

add(Element(
    "small-text", "Small text", C,
    "14/20 detail text for help, meta and timestamps.",
    why="A clearly smaller detail size separates supporting facts from content (Practical UI L03, T05).",
    when=["Help text, captions, timestamps, table footnotes."],
    avoid=["Body copy or anything people must read in full: keep it at 16px (T06)."],
    how=["Add `.orca-small`. Combine with `.orca-muted` for supporting meta."],
    classes=[".orca-small"], tokens=["type-detail"],
    laws=["L03", "T05"],
    examples=[("Small", """<p class="orca-small orca-muted">Updated 2 minutes ago</p>""")],
    guide=["Small text"],
))

add(Element(
    "tabular-number", "Tabular number", C,
    "Digits of equal width so numbers line up in columns and do not jitter when they update.",
    why="Aligned digits can be compared at a glance; live counters that do not shift are easier to read (Practical UI W11).",
    when=["Tables, stats, counters, times, durations, prices, percentages."],
    how=["Add `.orca-num`. Stat values, times and durations already use tabular figures.",
         "Format with grouping separators and units: '12,480 people', '64%'. Use Django's `intcomma` and `floatformat`."],
    classes=[".orca-num"],
    laws=["W11", "miller"],
    examples=[("Aligned digits", """<div class="orca-num" style="text-align: end; width: 8rem">1,204<br>98<br>12,480</div>""")],
    guide=["Tabular number"],
))

add(Element(
    "kbd", "Keyboard key", C,
    "A key or shortcut the person presses.",
    why="Showing the key in a key-like shape is a familiar convention (Jakob's law) and separates it from the "
        "sentence around it.",
    when=["Documenting a keyboard shortcut in help text, tooltips or menus."],
    how=["`<kbd class=\"orca-kbd\">Ctrl</kbd> + <kbd class=\"orca-kbd\">K</kbd>`.", "One `<kbd>` per key; write key names as printed on keyboards."],
    a11y=["Never make a shortcut the only way to do something."],
    classes=[".orca-kbd"], tokens=["font-mono", "bg-code"],
    laws=["jakob"],
    examples=[("Shortcut", """<p class="orca-p">Search with <kbd class="orca-kbd">/</kbd> or <kbd class="orca-kbd">Ctrl</kbd> + <kbd class="orca-kbd">K</kbd>.</p>""")],
    guide=["Keyboard key"],
))

add(Element(
    "stat-label", "Stat label", C,
    "The name of a measured value, shown above it.",
    why="A short, consistent label tells people what the number means before they read it (Miller's law: chunking label with value).",
    when=["Above every stat value in KPI tiles and summary rows."],
    how=["`<p class=\"orca-stat-label\">` (14/20, muted). An optional 12px icon may precede it.",
         "Name the measure and its scope: 'People inside now', 'Average dwell, today'."],
    classes=[".orca-stat-label"], tokens=["type-detail", "text-muted"],
    laws=["miller", "W04"],
    examples=[("Stat", """<div>
  <p class="orca-stat-label">{% icon "user" size="xs" %} People inside now</p>
  <p class="orca-stat-value">1,204</p>
</div>""")],
    guide=["Stat label"],
    related=["stat-value", "delta"],
))

add(Element(
    "stat-value", "Stat value", C,
    "A large, tabular number that is the point of a KPI tile.",
    why="The value is what people come for; size and weight make it the first thing seen (Von Restorff, Practical UI L03).",
    when=["KPI tiles, summary tiles, dashboard headers."],
    avoid=["More than one large value per tile."],
    how=["`<p class=\"orca-stat-value\">` (20/28, 550, tabular). Large tiles: `.orca-stat-value--lg` (24/32).",
         "Include the unit in the text ('64%', '3 h 20 min'); format with separators."],
    classes=[".orca-stat-value", ".orca-stat-value--lg"], tokens=["type-stat"],
    laws=["restorff", "W11"],
    examples=[("Value with delta", """<p class="orca-stat-label">Visitors today</p>
<p class="orca-stat-value">12,480 <span class="orca-delta orca-delta--up">{% icon "arrow-up" size="xs" %}<span>+8%</span><span class="orca-sr-only">compared with yesterday</span></span></p>""")],
    guide=["Stat value"],
    related=["stat-label", "delta"],
))

add(Element(
    "delta", "Delta (up, down, flat)", C,
    "Change against a reference: arrow, signed value, colour, and the reference in words.",
    why="Direction must be readable without colour (Practical UI C03): the arrow and the sign carry it, colour only confirms.",
    when=["Beside a stat value comparing with a previous period or a target."],
    avoid=["Green for 'up' when up is bad (complaints, errors): choose the tone by meaning with `--up`/`--down` classes "
           "describing good/bad, not direction."],
    how=["`.orca-delta--up` (good, positive colour), `--down` (bad, negative colour), `--flat` (muted).",
         "Content: arrow icon + signed value (+8%, −3) + an `.orca-sr-only` reference ('compared with last week').",
         "Use the true minus sign (−) for negative numbers."],
    a11y=["The arrow is decorative; the sign and the hidden reference carry the meaning."],
    classes=[".orca-delta", ".orca-delta--up", ".orca-delta--down", ".orca-delta--flat"],
    tokens=["positive", "negative", "text-muted"],
    laws=["C03", "C04"],
    examples=[("Three deltas", """<div class="orca-row orca-row--16">
  <span class="orca-delta orca-delta--up">{% icon "arrow-up" size="xs" %}+8%<span class="orca-sr-only"> compared with last week</span></span>
  <span class="orca-delta orca-delta--down">{% icon "arrow-down" size="xs" %}−3%<span class="orca-sr-only"> compared with last week</span></span>
  <span class="orca-delta orca-delta--flat">{% icon "minus" size="xs" %}0%<span class="orca-sr-only"> no change</span></span>
</div>""")],
    guide=["Delta (up, down, flat)"],
    source="ORCA",
))

add(Element(
    "code-text", "Code text", C,
    "Inline code, identifiers, file names and values the person may copy.",
    why="A monospaced face distinguishes literal values from prose and makes characters like 0/O and 1/l distinct (Practical UI T01).",
    when=["Technical values: IDs, IP addresses, file paths, settings keys, short commands."],
    how=["`<code class=\"orca-code\">`. Long values wrap anywhere instead of overflowing.", "For multi-line code use the Code block component (phase 2)."],
    classes=[".orca-code"], tokens=["type-code", "font-mono", "bg-code"],
    laws=["T01", "L15"],
    examples=[("Inline code", """<p class="orca-p">The video server answered at <code class="orca-code">media.example.com:443</code>.</p>""")],
    guide=["Code text"],
))

add(Element(
    "card-kicker", "Card kicker", C,
    "A short uppercase category label above a card title.",
    why="A kicker places the card in a category before the title is read, aiding scanning of mixed card lists (W07: uppercase only for short labels).",
    when=["Cards in a list that mixes types (image, video, album)."],
    avoid=["More than three words.", "Status: use a badge."],
    how=["`<p class=\"orca-card-kicker\">` (12/16, 550, uppercase, letter-spaced, muted)."],
    classes=[".orca-card-kicker"], tokens=["type-label", "text-muted"],
    laws=["W07", "miller"],
    examples=[("Card text stack", """<div class="orca-stack" style="gap: var(--orca-space-4); max-width: 18rem; padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border)">
  <p class="orca-card-kicker">Video</p>
  <h3 class="orca-card-title">Entrance A, north door</h3>
  <p class="orca-card-meta">MP4 · 1080p · added 3 March</p>
</div>""")],
    guide=["Card kicker"],
    related=["card-title", "card-meta"],
))

add(Element(
    "card-title", "Card title", C,
    "The name of the object a card represents.",
    why="The title is the card's identity; it is what people scan for in a grid (Practical UI L03, W04).",
    when=["Every card."],
    how=["`<h3 class=\"orca-card-title\">` (18/24, 550). If the whole card is a link, the title holds the link text.",
         "Wrap long titles; never truncate the distinguishing part (L15)."],
    classes=[".orca-card-title"], tokens=["type-title"],
    laws=["L03", "L15"],
    examples=[("Card title", """<h3 class="orca-card-title">Entrance A, north door</h3>""")],
    guide=["Card title"],
    related=["card-kicker", "card-meta"],
))

add(Element(
    "card-meta", "Card meta", C,
    "Secondary facts under a card title, separated by middle dots.",
    why="Grouping the secondary facts on one muted line keeps them available without competing with the title (Miller's law).",
    when=["Type, source, dates, counts shown under a card title."],
    how=["`<p class=\"orca-card-meta\">` (14/20, muted). Separate facts with ' · '.", "Three facts at most; move the rest to the detail page."],
    classes=[".orca-card-meta"], tokens=["type-detail", "text-muted"],
    laws=["miller", "hick"],
    examples=[("Meta line", """<p class="orca-card-meta">3 videos · updated 2 minutes ago</p>""")],
    guide=["Card meta"],
))

add(Element(
    "dialog-title", "Dialog title", C,
    "The question or statement a dialog or drawer is about.",
    why="A dialog interrupts; its title must say why in a few words so the decision is quick (Hick's law, Practical UI W01).",
    when=["Top of every dialog and drawer."],
    how=["`<h2 class=\"orca-dialog-title\">` (24/32, light 275).",
         "Confirmations ask the question with the object: 'Delete Harbour at dusk?'. The action button repeats the verb: 'Delete image'."],
    a11y=["Reference it with `aria-labelledby` on the `<dialog>`."],
    classes=[".orca-dialog-title"], tokens=["type-h4"],
    laws=["hick", "B13", "W01"],
    examples=[("Dialog title", """<h2 class="orca-dialog-title" id="dlg-title">Cancel this run?</h2>
<p class="orca-p">Shots already taken are kept.</p>""")],
    guide=["Dialog title"],
    related=["dialog-backdrop"],
))

add(Element(
    "empty-title", "Empty-state title", C,
    "What is missing, said plainly, in an empty region.",
    why="An empty screen is an ending or a beginning; a clear, calm title turns it into a next step instead of a dead end (Peak–end rule).",
    when=["A list, table, chart or search that has nothing to show."],
    how=["`<h2 class=\"orca-empty-title\">` (24/32, light). State the fact: 'No images yet', 'No videos match these filters'."],
    classes=[".orca-empty-title"], tokens=["type-h4"],
    laws=["peak-end", "W15"],
    examples=[("Empty state text", """<div class="orca-stack" style="align-items: center; text-align: center">
  {% orca_illustration "empty" %}
  <h2 class="orca-empty-title">No images yet</h2>
  <p class="orca-empty-text">Add an image to start your library.</p>
  <button class="orca-button orca-button--primary" type="button">Add image</button>
</div>""")],
    guide=["Empty-state title"],
    related=["empty-text", "illustration"],
))

add(Element(
    "empty-text", "Empty-state text", C,
    "One sentence that says why it is empty and what to do next.",
    why="Saying what to do next prevents a negative peak (Peak–end rule) and moves the person forward (Tesler: guidance in context).",
    when=["Under every empty-state title."],
    avoid=["Blame ('You have not…'), humour in operational contexts, or more than two sentences."],
    how=["`<p class=\"orca-empty-text\">` (16/24, muted, max 32rem).",
         "Filtered-empty: offer to clear filters. First-use empty: offer the create action."],
    classes=[".orca-empty-text"], tokens=["text-muted"],
    laws=["peak-end", "tesler", "W15"],
    examples=[("Filtered empty", """<p class="orca-empty-text">No videos match “harbour” this week. Clear the filters to see all videos.</p>""")],
    guide=["Empty-state text"],
    related=["empty-title"],
))
