# Text

Text styles with a fixed role. Choose by what the text is (a page title, a stat value), not by how big you want it.

## Heading (h1–h6)

`id: heading` · level: primitive · source: Tangerine

Document headings from h1 to h6, plus a display style for marketing pages.

### Why

A heading outline lets people scan and lets screen-reader users jump between sections (Miller's law: chunking; Practical UI W08). ORCA's thin h2 is the system's typographic signature.

### When to use

- Structuring long content: docs, settings pages, reports.
- Marketing pages: `.orca-display` for the one hero line.

### When not to use

- Choosing a heading level for its size: keep levels in order and restyle with a class if needed.
- Page and panel titles in applications: use `page-title` and `panel-title`.

### How to use

- Use real `<h1>`–`<h6>` elements with `.orca-h1`…`.orca-h6`.
- One `<h1>` per page. Never skip a level going down.
- h1 and h2 are 42/48 from 1036px and 32/40 below; h4 (light) suits dialog and empty-state titles.
- Write in sentence case, no full stop (W02, W12).

### Accessibility

- The heading level conveys structure; the class only changes looks.

#### Example: Levels

```django
<h1 class="orca-h1">Capacity report</h1>
<h2 class="orca-h2">Weekly overview</h2>
<h3 class="orca-h3">Entrances</h3>
<h4 class="orca-h4">No data for this week</h4>
```

**Classes:** `.orca-h1`, `.orca-h2`, `.orca-h3`, `.orca-h4`, `.orca-h5`, `.orca-h6`, `.orca-display`

**Tokens:** `--orca-type-h1`, `--orca-type-h2`, `--orca-type-h3`, `--orca-type-h4`, `--orca-type-h5`, `--orca-type-h6`, `--orca-type-display`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI W02: Use sentence case; Practical UI T05: Build sizes from a type scale

**Related:** `page-title`, `section-title`

**ORCA guide items covered:** Heading (h1–h6)

---

## Page title

`id: page-title` · level: primitive · source: Tangerine

The single title naming what this page is.

### Why

People confirm they are in the right place from the title first (Jakob's law); one clear title gives the page a single focal point (Von Restorff).

### When to use

- Top of every application page, inside the page head, beside the page actions.

### When not to use

- Repeating the product name or the breadcrumb's last item word for word with extra decoration.
- Long titles: front-load the distinguishing word (W04).

### How to use

- `<h1 class="orca-page-title">` (28/36, weight 700).
- Name the object, not the action: 'Videos', 'Harbour at dusk', 'New album'.
- Long names wrap; they are never cut, so people can always read the full name (L15).
- On application pages it sits in the `page-head` pattern, with the page actions beside it.

### Accessibility

- It is the page's `<h1>`; the document `<title>` should start with the same words.

#### Example: Page title with subtitle

```django
<div>
  <h1 class="orca-page-title">Harbour at dusk</h1>
  <p class="orca-page-subtitle">Added to the library on 3 March 2026.</p>
</div>
```

**Classes:** `.orca-page-title`

**Tokens:** `--orca-type-page-title`

**Principles applied:** Jakob's law: work the way products people already know work; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI W04: Lead with the information people seek; Practical UI L15: Design for long and unusual content

**Related:** `page-subtitle`, `heading`

**ORCA guide items covered:** Page title

---

## Page subtitle

`id: page-subtitle` · level: primitive · source: Tangerine

One sentence under the page title that says what the page is for or about.

### Why

A short orientation sentence answers 'what can I do here' without a manual (Tesler: help in context; paradox of the active user).

### When to use

- Pages whose purpose is not obvious from the title, or that need one key fact (scope, time range).

### When not to use

- Repeating the title.
- Instructions longer than one sentence: put them in help text where they are needed.

### How to use

- `<p class="orca-page-subtitle">` directly after the page title; muted, max 70ch.
- Under 20 words (W01). A full sentence ends with a full stop.

#### Example: Subtitle

```django
<h1 class="orca-page-title">Alert rules</h1>
<p class="orca-page-subtitle">Rules decide who gets an email when a video upload fails or a KPI crosses a limit.</p>
```

**Classes:** `.orca-page-subtitle`

**Tokens:** `--orca-text-muted`, `--orca-measure`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Practical UI W01: Make every word useful

**ORCA guide items covered:** Page subtitle

---

## Section title

`id: section-title` · level: primitive · source: Tangerine

Title of a section inside a page (a group of panels or a long form part).

### Why

Section titles chunk a long page into a few recognisable parts (Miller's law, Practical UI R17).

### When to use

- Splitting a page into two or more regions; grouping fields of a long form.

### When not to use

- A section with a single panel that already has a title: use only the panel title.

### How to use

- `<h2 class="orca-section-title">` (24/32, 550), with `--orca-space-16` below and `--orca-space-32` above.
- Descriptive words people scan for: 'Notifications', not 'Other'.

#### Example: Section title

```django
<h2 class="orca-section-title">Notifications</h2>
```

**Classes:** `.orca-section-title`

**Tokens:** `--orca-type-h3`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI R17: Group fields under headings; Practical UI W08: Structure information for scanning

**ORCA guide items covered:** Section title

---

## Panel title

`id: panel-title` · level: primitive · source: Tangerine

Title at the top of a panel or card group of content.

### Why

Each panel answers one question; its title names that question so it can be found by scanning (Miller's law).

### When to use

- Head of every panel, card group, table card or chart frame.

### When not to use

- Uppercase or coloured titles: they look like labels or links.

### How to use

- `<h2 class="orca-panel-title">` or `<h3>` depending on the outline (18/24, 550).
- Optional muted description under it with `.orca-small.orca-muted`.

#### Example: Panel title

```django
<h2 class="orca-panel-title">People counted today</h2>
<p class="orca-small orca-muted">All entrances, updated every minute.</p>
```

**Classes:** `.orca-panel-title`

**Tokens:** `--orca-type-title`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI L03: Establish an order of importance

**ORCA guide items covered:** Panel title

---

## Alert title

`id: alert-title` · level: primitive · source: Tangerine

Bold first line of an alert, callout or notification that states what happened.

### Why

People read the first words and decide; a bold, specific title is enough on its own to act (Practical UI W15).

### When to use

- Every alert or callout with more than one sentence.

### How to use

- `<p class="orca-alert-title">` (16/24, 550).
- State the fact: 'Video unavailable', 'Report sent'. No 'Error:' prefix, no exclamation marks.

#### Example: Alert title

```django
<p class="orca-alert-title">Video unavailable</p>
<p class="orca-p">The file could not be loaded. Check your connection, then try playing it again.</p>
```

**Classes:** `.orca-alert-title`

**Tokens:** `--orca-type-body-strong`

**Principles applied:** Practical UI W15: Help people recover from errors; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Alert title

---

## Paragraph

`id: paragraph` · level: primitive · source: Tangerine

Running text at 16/24 with a 70-character measure.

### Why

Comfortable line length and line height make reading effortless (Practical UI T07, T09).

### When to use

- Any sentence-level text: descriptions, explanations, dialog bodies.

### When not to use

- Walls of text: split into short paragraphs and lists (W08).

### How to use

- `<p class="orca-p">`. Lead paragraph: `.orca-p--lead` (18/28).
- Front-load the point; one idea per paragraph; under 20 words per sentence where possible.

#### Example: Paragraphs

```django
<p class="orca-p orca-p--lead">Thumbnails are taken from each video at a fixed interval.</p>
<p class="orca-p">Use them to check framing before you draw zones. Shots are kept for 30 days.</p>
```

**Classes:** `.orca-p`, `.orca-p--lead`

**Tokens:** `--orca-type-body`, `--orca-measure`

**Principles applied:** Practical UI T07: Comfortable line spacing; Practical UI T09: Limit reading measure; Practical UI W01: Make every word useful; Practical UI W05: Order explanations as an inverted pyramid

**ORCA guide items covered:** Paragraph

---

## Text link

`id: text-link` · level: primitive · source: Tangerine

An underlined, accent-coloured link inside text.

### Why

Colour plus underline is the convention people recognise without thinking (Jakob's law, Practical UI S03) and it survives colour-blindness (C03).

### When to use

- Navigation to another page or resource from within text.

### When not to use

- Actions that change data: use a button.
- 'Click here' or 'Learn more': name the destination (W14).

### How to use

- `<a class="orca-link" href=…>`. In navigation lists where position already signals a link: `.orca-link--quiet`.
- External links: add `.orca-link--external` (adds ↗) and say so in the text when it matters.
- Visited state uses `--orca-link-visited` except with `.orca-link--plain` (for app navigation).

### Accessibility

- Link text must make sense read alone, as screen-reader users list links.
- Focus shows the 3px ring; hover thickens the underline.

#### Example: Links

```django
<p class="orca-p">Shots are deleted after 30 days. Change this in <a class="orca-link orca-link--plain" href="#">retention settings</a>.</p>
<p class="orca-p"><a class="orca-link orca-link--external" href="https://www.w3.org/WAI/">WCAG overview</a></p>
```

**Classes:** `.orca-link`, `.orca-link--quiet`, `.orca-link--external`, `.orca-link--plain`

**Tokens:** `--orca-accent`, `--orca-accent-hover`, `--orca-link-visited`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI S03: Use link styling with context; Practical UI W14: Give links meaningful destination names; Practical UI C03: Communicate meaning beyond colour

**Related:** `link-action`

**ORCA guide items covered:** Text link

---

## Muted text

`id: muted-text` · level: primitive · source: Tangerine

Secondary text in `--orca-text-muted` (60% ink, still 4.5:1).

### Why

Lowering the weight of secondary information lets the primary information lead (Practical UI L03) while staying readable (T13: never pale grey).

### When to use

- Meta information, descriptions under titles, empty values ('Not set'), counts beside labels.

### When not to use

- Placeholder-like grey for content people must read to finish the task.
- Disabled meaning: use the disabled state.

### How to use

- Add `.orca-muted` to any text element.

#### Example: Muted

```django
<p class="orca-p">Summer 2026 <span class="orca-muted">· 3 videos</span></p>
```

**Classes:** `.orca-muted`

**Tokens:** `--orca-text-muted`

**Principles applied:** Practical UI L03: Establish an order of importance; Practical UI T13: Keep quieter text legible

**ORCA guide items covered:** Muted text

---

## Small text

`id: small-text` · level: primitive · source: Tangerine

14/20 detail text for help, meta and timestamps.

### Why

A clearly smaller detail size separates supporting facts from content (Practical UI L03, T05).

### When to use

- Help text, captions, timestamps, table footnotes.

### When not to use

- Body copy or anything people must read in full: keep it at 16px (T06).

### How to use

- Add `.orca-small`. Combine with `.orca-muted` for supporting meta.

#### Example: Small

```django
<p class="orca-small orca-muted">Updated 2 minutes ago</p>
```

**Classes:** `.orca-small`

**Tokens:** `--orca-type-detail`

**Principles applied:** Practical UI L03: Establish an order of importance; Practical UI T05: Build sizes from a type scale

**ORCA guide items covered:** Small text

---

## Tabular number

`id: tabular-number` · level: primitive · source: Tangerine

Digits of equal width so numbers line up in columns and do not jitter when they update.

### Why

Aligned digits can be compared at a glance; live counters that do not shift are easier to read (Practical UI W11).

### When to use

- Tables, stats, counters, times, durations, prices, percentages.

### How to use

- Add `.orca-num`. Stat values, times and durations already use tabular figures.
- Format with grouping separators and units: '12,480 people', '64%'. Use Django's `intcomma` and `floatformat`.

#### Example: Aligned digits

```django
<div class="orca-num" style="text-align: end; width: 8rem">1,204<br>98<br>12,480</div>
```

**Classes:** `.orca-num`

**Principles applied:** Practical UI W11: Make numbers scannable; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Tabular number

---

## Keyboard key

`id: kbd` · level: primitive · source: Tangerine

A key or shortcut the person presses.

### Why

Showing the key in a key-like shape is a familiar convention (Jakob's law) and separates it from the sentence around it.

### When to use

- Documenting a keyboard shortcut in help text, tooltips or menus.

### How to use

- `<kbd class="orca-kbd">Ctrl</kbd> + <kbd class="orca-kbd">K</kbd>`.
- One `<kbd>` per key; write key names as printed on keyboards.

### Accessibility

- Never make a shortcut the only way to do something.

#### Example: Shortcut

```django
<p class="orca-p">Search with <kbd class="orca-kbd">/</kbd> or <kbd class="orca-kbd">Ctrl</kbd> + <kbd class="orca-kbd">K</kbd>.</p>
```

**Classes:** `.orca-kbd`

**Tokens:** `--orca-font-mono`, `--orca-bg-code`

**Principles applied:** Jakob's law: work the way products people already know work

**ORCA guide items covered:** Keyboard key

---

## Stat label

`id: stat-label` · level: primitive · source: Tangerine

The name of a measured value, shown above it.

### Why

A short, consistent label tells people what the number means before they read it (Miller's law: chunking label with value).

### When to use

- Above every stat value in KPI tiles and summary rows.

### How to use

- `<p class="orca-stat-label">` (14/20, muted). An optional 12px icon may precede it.
- Name the measure and its scope: 'People inside now', 'Average dwell, today'.

#### Example: Stat

```django
<div>
  <p class="orca-stat-label">{% icon "user" size="xs" %} People inside now</p>
  <p class="orca-stat-value">1,204</p>
</div>
```

**Classes:** `.orca-stat-label`

**Tokens:** `--orca-type-detail`, `--orca-text-muted`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI W04: Lead with the information people seek

**Related:** `stat-value`, `delta`

**ORCA guide items covered:** Stat label

---

## Stat value

`id: stat-value` · level: primitive · source: Tangerine

A large, tabular number that is the point of a KPI tile.

### Why

The value is what people come for; size and weight make it the first thing seen (Von Restorff, Practical UI L03).

### When to use

- KPI tiles, summary tiles, dashboard headers.

### When not to use

- More than one large value per tile.

### How to use

- `<p class="orca-stat-value">` (20/28, 550, tabular). Large tiles: `.orca-stat-value--lg` (24/32).
- Include the unit in the text ('64%', '3 h 20 min'); format with separators.

#### Example: Value with delta

```django
<p class="orca-stat-label">Visitors today</p>
<p class="orca-stat-value">12,480 <span class="orca-delta orca-delta--up">{% icon "arrow-up" size="xs" %}<span>+8%</span><span class="orca-sr-only">compared with yesterday</span></span></p>
```

**Classes:** `.orca-stat-value`, `.orca-stat-value--lg`

**Tokens:** `--orca-type-stat`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI W11: Make numbers scannable

**Related:** `stat-label`, `delta`

**ORCA guide items covered:** Stat value

---

## Delta (up, down, flat)

`id: delta` · level: primitive · source: ORCA

Change against a reference: arrow, signed value, colour, and the reference in words.

### Why

Direction must be readable without colour (Practical UI C03): the arrow and the sign carry it, colour only confirms.

### When to use

- Beside a stat value comparing with a previous period or a target.

### When not to use

- Green for 'up' when up is bad (complaints, errors): choose the tone by meaning with `--up`/`--down` classes describing good/bad, not direction.

### How to use

- `.orca-delta--up` (good, positive colour), `--down` (bad, negative colour), `--flat` (muted).
- Content: arrow icon + signed value (+8%, −3) + an `.orca-sr-only` reference ('compared with last week').
- Use the true minus sign (−) for negative numbers.

### Accessibility

- The arrow is decorative; the sign and the hidden reference carry the meaning.

#### Example: Three deltas

```django
<div class="orca-row orca-row--16">
  <span class="orca-delta orca-delta--up">{% icon "arrow-up" size="xs" %}+8%<span class="orca-sr-only"> compared with last week</span></span>
  <span class="orca-delta orca-delta--down">{% icon "arrow-down" size="xs" %}−3%<span class="orca-sr-only"> compared with last week</span></span>
  <span class="orca-delta orca-delta--flat">{% icon "minus" size="xs" %}0%<span class="orca-sr-only"> no change</span></span>
</div>
```

**Classes:** `.orca-delta`, `.orca-delta--up`, `.orca-delta--down`, `.orca-delta--flat`

**Tokens:** `--orca-positive`, `--orca-negative`, `--orca-text-muted`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI C04: Reserve status colours for their meanings

**ORCA guide items covered:** Delta (up, down, flat)

---

## Code text

`id: code-text` · level: primitive · source: Tangerine

Inline code, identifiers, file names and values the person may copy.

### Why

A monospaced face distinguishes literal values from prose and makes characters like 0/O and 1/l distinct (Practical UI T01).

### When to use

- Technical values: IDs, IP addresses, file paths, settings keys, short commands.

### How to use

- `<code class="orca-code">`. Long values wrap anywhere instead of overflowing.
- For multi-line code use the Code block component (phase 2).

#### Example: Inline code

```django
<p class="orca-p">The video server answered at <code class="orca-code">media.example.com:443</code>.</p>
```

**Classes:** `.orca-code`

**Tokens:** `--orca-type-code`, `--orca-font-mono`, `--orca-bg-code`

**Principles applied:** Practical UI T01: One legible sans serif family; Practical UI L15: Design for long and unusual content

**ORCA guide items covered:** Code text

---

## Card kicker

`id: card-kicker` · level: primitive · source: Tangerine

A short uppercase category label above a card title.

### Why

A kicker places the card in a category before the title is read, aiding scanning of mixed card lists (W07: uppercase only for short labels).

### When to use

- Cards in a list that mixes types (image, video, album).

### When not to use

- More than three words.
- Status: use a badge.

### How to use

- `<p class="orca-card-kicker">` (12/16, 550, uppercase, letter-spaced, muted).

#### Example: Card text stack

```django
<div class="orca-stack" style="gap: var(--orca-space-4); max-width: 18rem; padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border)">
  <p class="orca-card-kicker">Video</p>
  <h3 class="orca-card-title">Entrance A, north door</h3>
  <p class="orca-card-meta">MP4 · 1080p · added 3 March</p>
</div>
```

**Classes:** `.orca-card-kicker`

**Tokens:** `--orca-type-label`, `--orca-text-muted`

**Principles applied:** Practical UI W07: Reserve uppercase for short labels; Miller's law: chunk information so working memory is not overloaded

**Related:** `card-title`, `card-meta`

**ORCA guide items covered:** Card kicker

---

## Card title

`id: card-title` · level: primitive · source: Tangerine

The name of the object a card represents.

### Why

The title is the card's identity; it is what people scan for in a grid (Practical UI L03, W04).

### When to use

- Every card.

### How to use

- `<h3 class="orca-card-title">` (18/24, 550). If the whole card is a link, the title holds the link text.
- Wrap long titles; never truncate the distinguishing part (L15).

#### Example: Card title

```django
<h3 class="orca-card-title">Entrance A, north door</h3>
```

**Classes:** `.orca-card-title`

**Tokens:** `--orca-type-title`

**Principles applied:** Practical UI L03: Establish an order of importance; Practical UI L15: Design for long and unusual content

**Related:** `card-kicker`, `card-meta`

**ORCA guide items covered:** Card title

---

## Card meta

`id: card-meta` · level: primitive · source: Tangerine

Secondary facts under a card title, separated by middle dots.

### Why

Grouping the secondary facts on one muted line keeps them available without competing with the title (Miller's law).

### When to use

- Type, source, dates, counts shown under a card title.

### How to use

- `<p class="orca-card-meta">` (14/20, muted). Separate facts with ' · '.
- Three facts at most; move the rest to the detail page.

#### Example: Meta line

```django
<p class="orca-card-meta">3 videos · updated 2 minutes ago</p>
```

**Classes:** `.orca-card-meta`

**Tokens:** `--orca-type-detail`, `--orca-text-muted`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Card meta

---

## Dialog title

`id: dialog-title` · level: primitive · source: Tangerine

The question or statement a dialog or drawer is about.

### Why

A dialog interrupts; its title must say why in a few words so the decision is quick (Hick's law, Practical UI W01).

### When to use

- Top of every dialog and drawer.

### How to use

- `<h2 class="orca-dialog-title">` (24/32, light 275).
- Confirmations ask the question with the object: 'Delete Harbour at dusk?'. The action button repeats the verb: 'Delete image'.

### Accessibility

- Reference it with `aria-labelledby` on the `<dialog>`.

#### Example: Dialog title

```django
<h2 class="orca-dialog-title" id="dlg-title">Cancel this run?</h2>
<p class="orca-p">Shots already taken are kept.</p>
```

**Classes:** `.orca-dialog-title`

**Tokens:** `--orca-type-h4`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI B13: Scale friction to the consequence; Practical UI W01: Make every word useful

**Related:** `dialog-backdrop`

**ORCA guide items covered:** Dialog title

---

## Empty-state title

`id: empty-title` · level: primitive · source: Tangerine

What is missing, said plainly, in an empty region.

### Why

An empty screen is an ending or a beginning; a clear, calm title turns it into a next step instead of a dead end (Peak–end rule).

### When to use

- A list, table, chart or search that has nothing to show.

### How to use

- `<h2 class="orca-empty-title">` (24/32, light). State the fact: 'No images yet', 'No videos match these filters'.

#### Example: Empty state text

```django
<div class="orca-stack" style="align-items: center; text-align: center">
  {% orca_illustration "empty" %}
  <h2 class="orca-empty-title">No images yet</h2>
  <p class="orca-empty-text">Add an image to start your library.</p>
  <button class="orca-button orca-button--primary" type="button">Add image</button>
</div>
```

**Classes:** `.orca-empty-title`

**Tokens:** `--orca-type-h4`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Practical UI W15: Help people recover from errors

**Related:** `empty-text`, `illustration`

**ORCA guide items covered:** Empty-state title

---

## Empty-state text

`id: empty-text` · level: primitive · source: Tangerine

One sentence that says why it is empty and what to do next.

### Why

Saying what to do next prevents a negative peak (Peak–end rule) and moves the person forward (Tesler: guidance in context).

### When to use

- Under every empty-state title.

### When not to use

- Blame ('You have not…'), humour in operational contexts, or more than two sentences.

### How to use

- `<p class="orca-empty-text">` (16/24, muted, max 32rem).
- Filtered-empty: offer to clear filters. First-use empty: offer the create action.

#### Example: Filtered empty

```django
<p class="orca-empty-text">No videos match “harbour” this week. Clear the filters to see all videos.</p>
```

**Classes:** `.orca-empty-text`

**Tokens:** `--orca-text-muted`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Tesler's law: move unavoidable complexity from the user to the system; Practical UI W15: Help people recover from errors

**Related:** `empty-title`

**ORCA guide items covered:** Empty-state text

---
