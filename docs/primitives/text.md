# Text

Text styles with a fixed role. Choose by what the text is (a page title, a stat value), not by size.

## Heading (h1–h6)

`id: heading` · level: primitive · source: Tangerine

Headings h1 to h6, plus a display style for marketing pages.

### General description

Headings are titles that label each part of a page, from the main title (h1) down to small sub-sections (h6). They give a page an outline that people and software can scan.

#### Use cases

- Breaking long articles, documentation and reports into scannable sections.
- Letting screen-reader users jump between sections.
- Showing the main topic of a page in one h1.

#### When not to use it

- Making text bigger or bold only for looks: use a style, not a heading level.
- Labelling single items like buttons or form fields: use the proper label element.

#### Best practices

- Use one h1 per page.
- Go down one level at a time and never skip levels.
- Choose the level for the outline, then adjust the look with styling.
- Keep headings short and specific.

### When to use

- Structuring long content: docs, settings pages, reports.
- Marketing pages: `.orca-display` for the one hero line.

### When not to use

- Picking a level for its size: keep levels in order and restyle with a class.
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

The one title that names the page.

### General description

The page title is the main heading of a page. It tells people which page or item they are on.

#### Use cases

- Naming the page at the top of an application screen.
- Naming the record on a detail page.
- Giving every page one clear focal point.

#### When not to use it

- Putting the site name in every title: use a logo or header for the brand.
- Long explanations: use a subtitle or help text.

#### Best practices

- Name the thing, such as 'Orders', not the action.
- Put the distinguishing word first.
- Make it the page's single h1.
- Match the browser tab title.

### When to use

- Top of every application page, in the page head beside the page actions.

### When not to use

- Repeating the product name or the last breadcrumb item.
- Long titles: front-load the distinguishing word (W04).

### How to use

- `<h1 class="orca-page-title">` (28/36, weight 700).
- Name the object, not the action: 'Videos', 'Harbour at dusk', 'New album'.
- Long names wrap and are never cut (L15).
- On application pages it sits in the `page-head` pattern, with the page actions beside it.
- It may start with the icon its page has in the sidebar (`{% icon "name" size="m" %}` as the first child), so the page and its menu entry are recognised together; the icon is decorative.

### Accessibility

- It is the page's `<h1>`. Start the document `<title>` with the same words.
- A leading icon is decorative (`aria-hidden`): the words alone name the page.

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

One sentence under the page title saying what the page is for.

### General description

A page subtitle is one short sentence under the page title. It explains what the page is for or adds one key fact.

#### Use cases

- Clarifying a page whose title alone is vague.
- Showing scope, such as a date range or filter.
- Giving first-time visitors a hint of what to do.

#### When not to use it

- Restating the title in other words: leave it out.
- Long instructions: put help text next to the field that needs it.

#### Best practices

- Keep it to one short sentence.
- Make it add something the title does not.
- Use a quieter colour than the title.
- Keep lines a readable length.

### When to use

- Pages whose purpose is unclear from the title, or that need one key fact (scope, time range).

### When not to use

- Repeating the title.
- Instructions longer than one sentence: put them in help text where needed.

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

Title of a section in a page: a group of panels or part of a long form.

### General description

A section title heads a group of related content on a page, such as a set of panels or part of a long form.

#### Use cases

- Splitting a long page into a few named parts.
- Grouping related fields in a long form.
- Helping people scan to the part they need.

#### When not to use it

- Titling a section that holds only one titled panel: the panel title is enough.
- Naming the whole page: use the page title.

#### Best practices

- Use words people would look for, not 'Other' or 'Misc'.
- Keep the heading level in order.
- Leave more space above than below.
- Keep titles to a few words.

### When to use

- Splitting a page into two or more regions; grouping fields in a long form.

### When not to use

- A section holding one titled panel: use only the panel title.

### How to use

- `<h2 class="orca-section-title">` (24/32, 550), with `--orca-space-16` below and `--orca-space-32` above.
- Use words people scan for: 'Notifications', not 'Other'.

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

Title at the top of a panel or card group.

### General description

A panel title is the heading of a boxed block of content, such as a card, table or chart. It names what that block shows.

#### Use cases

- Naming a chart, table or summary card.
- Heading a settings group in a box.
- Letting people find a block by scanning.

#### When not to use it

- Naming a whole page section: use a section title.
- Styling that looks like a link or label, such as colour or all capitals.

#### Best practices

- Describe the content in a few words.
- Pick the heading level that fits the page outline.
- Add a short muted description only if needed.
- Keep style the same on every panel.

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

Bold first line of an alert, callout or notification, stating what happened.

### General description

An alert title is the bold first line of a message box. It states plainly what happened so the reader can decide quickly.

#### Use cases

- Naming the result in a success or error message.
- Heading a warning or notice with a longer body.
- Giving screen-reader users the key fact first.

#### When not to use it

- One-line messages: skip the title and write one clear sentence.
- Vague titles like 'Error' or 'Oops': state the problem.

#### Best practices

- State the fact, such as 'Report sent'.
- Keep it to a few words.
- Skip 'Error:' prefixes and exclamation marks.
- Follow it with what to do next.

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

### General description

A paragraph is a block of running text. It carries explanations and descriptions, and its size and line length set how easy a page is to read.

#### Use cases

- Explaining a feature or a result.
- Writing the body of a dialog or message.
- Introducing a section before lists or tables.

#### When not to use it

- Long blocks of dense text: split them or use a list.
- Content that is really a list of steps: use a numbered list.

#### Best practices

- Put the main point first.
- Keep one idea in each paragraph.
- Keep lines around 60 to 75 characters.
- Use short sentences.

### When to use

- Descriptions, explanations, dialog bodies and other running text.

### When not to use

- Walls of text: split into short paragraphs and lists (W08).

### How to use

- `<p class="orca-p">`. Lead paragraph: `.orca-p--lead` (18/28).
- Lead with the point; one idea per paragraph; under 20 words per sentence where possible.

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

An underlined, accent-coloured link in text.

### General description

A text link is clickable text that takes the reader to another page, file or place on the same page.

#### Use cases

- Pointing to related pages from within a sentence.
- Linking to outside sources or documentation.
- Jumping to a section on the same page.

#### When not to use it

- Actions that change data, such as save or delete: use a button.
- Vague text like 'click here': say where the link goes.

#### Best practices

- Make link text meaningful on its own.
- Underline links so colour is not the only cue.
- Show a clear focus outline.
- Say when a link opens another site.

### When to use

- Linking to another page or resource from within text.

### When not to use

- Actions that change data: use a button.
- 'Click here' or 'Learn more': name the destination (W14).

### How to use

- `<a class="orca-link" href=…>`. In navigation lists where position already signals a link: `.orca-link--quiet`.
- External links: add `.orca-link--external` (adds ↗) and say so in the text when it matters.
- Visited state uses `--orca-link-visited` except with `.orca-link--plain` (for app navigation).

### Accessibility

- Link text must make sense on its own: screen-reader users list links.
- Focus shows the 3px ring; hover thickens the underline.

#### Example: Links

```django
<p class="orca-p">Shots are deleted after 30 days. Change this in <a class="orca-link orca-link--plain" href="#">retention settings</a>.</p>
<p class="orca-p">
  <a class="orca-link orca-link--external" href="https://www.w3.org/WAI/">WCAG overview</a>
</p>
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

### General description

Muted text is secondary text shown in a softer colour so the main content stands out. It must still be easy to read.

#### Use cases

- Showing descriptions under titles.
- Showing meta details such as counts or dates.
- Showing empty values like 'Not set'.

#### When not to use it

- Text people must read to finish a task: use normal colour.
- Showing that something is disabled: use a real disabled state.

#### Best practices

- Keep enough contrast: at least 4.5 to 1 against the background.
- Do not rely on pale grey.
- Use it only for secondary information.

### When to use

- Meta information, descriptions under titles, empty values ('Not set'), counts beside labels.

### When not to use

- Pale grey for content people must read to finish the task.
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

### General description

Small text is a smaller type size for supporting information such as help, captions and timestamps.

#### Use cases

- Writing help text under a field.
- Showing captions, timestamps or footnotes.
- Adding meta details next to a title.

#### When not to use it

- Body copy or anything essential to read in full: use normal text size.
- Legal or critical warnings: keep them at normal size.

#### Best practices

- Do not go below about 14px.
- Keep contrast high.
- Keep it short.
- Pair it with a quieter colour for meta details.

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

Equal-width digits that line up in columns and do not shift when numbers update.

### General description

Tabular numbers use digits of equal width, so figures line up in columns and do not shift when values change.

#### Use cases

- Showing prices and totals in tables.
- Showing live counters and timers.
- Showing times, durations and percentages.

#### When not to use it

- Running text and headings: normal digits read more naturally there.
- Codes with letters and digits, such as IDs: use a monospace code style.

#### Best practices

- Right-align numbers in columns.
- Add thousand separators and units.
- Use the same decimal places in a column.
- Use it for values that update.

### When to use

- Tables, stats, counters, times, durations, prices, percentages.

### How to use

- Add `.orca-num`. Stat values, times and durations already use tabular figures.
- Add separators and units: '12,480 people', '64%', using Django's `intcomma` and `floatformat`.

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

### General description

A keyboard key element shows a key or key combination in a key-like shape, so readers can tell it from the surrounding sentence.

#### Use cases

- Documenting shortcuts in help text.
- Showing shortcuts next to menu items.
- Writing instructions that name specific keys.

#### When not to use it

- Showing code or commands: use a code style.
- Making a shortcut the only way to do something: always offer a visible option.

#### Best practices

- Use one element per key.
- Write key names as printed, such as Ctrl or Esc.
- Join combinations with a plus sign.
- Consider Mac and Windows differences.

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

### General description

A stat label is the short name of a measured value, shown with the number so readers know what it means.

#### Use cases

- Naming a number on a dashboard tile.
- Labelling a figure in a summary row.
- Telling apart several similar numbers.

#### When not to use it

- Long explanations: use a tooltip or help text.
- Labels that repeat the whole tile title.

#### Best practices

- Name the measure and its scope, such as 'Visitors today'.
- Keep it to a few words.
- Place it consistently above or beside the value.
- Use sentence case.

### When to use

- Above every stat value in KPI tiles and summary rows.

### How to use

- `<p class="orca-stat-label">` (14/20, muted). An optional 12px icon may precede it.
- Name the measure and its scope: 'People inside now', 'Average dwell, today'.

#### Example: Stat

```django
<div>
  <p class="orca-stat-label">
    {% icon "user" size="xs" %}
    People inside now
  </p>
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

The large tabular number a KPI tile exists to show.

### General description

A stat value is a large number that shows one key measurement. It is the main thing a summary tile is there to show.

#### Use cases

- Showing key figures on a dashboard.
- Opening a report with headline numbers.
- Showing a live count.

#### When not to use it

- Many figures in one tile: use a table or chart.
- Numbers without context: add a label, unit or comparison.

#### Best practices

- Show one main value per tile.
- Include the unit, such as % or h.
- Format with thousand separators.
- Use equal-width digits.

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
<p class="orca-stat-value">
  12,480
  <span class="orca-delta orca-delta--up">
    {% icon "arrow-up" size="xs" %}
    <span>+8%</span>
    <span class="orca-sr-only">compared with yesterday</span>
  </span>
</p>
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

### General description

A delta shows how a value changed compared with an earlier period or a target, using an arrow, a signed number and a colour.

#### Use cases

- Comparing today with yesterday on a KPI tile.
- Showing growth or decline over a period.
- Showing distance from a target.

#### When not to use it

- Showing a total on its own: use a stat value.
- Using red and green alone: add an arrow and a sign.

#### Best practices

- Show direction with an arrow and sign, not colour alone.
- Say what it is compared with.
- Colour by good or bad, not up or down.
- Use a true minus sign.

### When to use

- Beside a stat value comparing with a previous period or a target.

### When not to use

- Green for 'up' when up is bad (complaints, errors): the `--up`/`--down` classes mean good/bad, not direction.

### How to use

- `.orca-delta--up` (good, positive colour), `--down` (bad, negative colour), `--flat` (muted).
- Content: arrow icon + signed value (+8%, −3) + an `.orca-sr-only` reference ('compared with last week').
- Use the true minus sign (−) for negative numbers.

### Accessibility

- The arrow is decorative; the sign and the hidden reference carry the meaning.

#### Example: Three deltas

```django
<div class="orca-row orca-row--16">
  <span class="orca-delta orca-delta--up">
    {% icon "arrow-up" size="xs" %}
    +8%
    <span class="orca-sr-only"> compared with last week</span>
  </span>
  <span class="orca-delta orca-delta--down">
    {% icon "arrow-down" size="xs" %}
    −3%
    <span class="orca-sr-only"> compared with last week</span>
  </span>
  <span class="orca-delta orca-delta--flat">
    {% icon "minus" size="xs" %}
    0%
    <span class="orca-sr-only"> no change</span>
  </span>
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

### General description

Code text shows short technical values in a monospace font, so they stand out from sentences and characters are easy to tell apart.

#### Use cases

- Showing file names, paths and IDs.
- Showing short commands or settings keys.
- Showing values people may copy.

#### When not to use it

- Many lines of code: use a code block.
- Emphasising ordinary words: use bold or italic.

#### Best practices

- Use it only for literal values.
- Let long values wrap.
- Offer a copy button for values people copy.
- Keep contrast high.

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

### General description

A card kicker is a short label above a card title that names the card's category, such as 'Video' or 'Guide'.

#### Use cases

- Telling types apart in a mixed list of cards.
- Adding a category to news or article cards.
- Helping people scan a grid.

#### When not to use it

- Showing status such as 'Draft' or 'Failed': use a badge.
- Long labels: keep kickers to one to three words.

#### Best practices

- Use one to three words.
- Use the same wording across cards.
- Keep it quieter than the title.
- Use capitals only for short labels.

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

### General description

A card title is the name of the item a card stands for. It is the first thing people read in a grid of cards.

#### Use cases

- Naming a record, product or article card.
- Giving a clickable card its link text.
- Helping people choose between cards.

#### When not to use it

- Decorative or vague titles: use the real name of the item.
- Cutting off long names: let them wrap.

#### Best practices

- Use the item's real name.
- Keep the distinguishing words visible.
- Use the same heading level on every card.
- Make link text clear if the card is a link.

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

### General description

Card meta is a line of small secondary facts under a card title, such as type, date or count.

#### Use cases

- Showing dates, sizes or counts on a card.
- Showing the source or author of an item.
- Giving extra detail without crowding the title.

#### When not to use it

- Key facts people need to decide: put them in the title or body.
- Long lists of facts: link to a detail page.

#### Best practices

- Show three facts at most.
- Separate facts with a dot or space.
- Use a quieter style than the title.
- Keep the order the same on every card.

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

### General description

A dialog title is the heading of a pop-up window. It says in a few words what the person is being asked or told.

#### Use cases

- Naming a confirmation, such as 'Delete this file?'.
- Titling a form shown in a dialog.
- Naming a side panel or drawer.

#### When not to use it

- Vague titles like 'Warning' or 'Are you sure?': name the action and object.
- Long text: put detail in the body.

#### Best practices

- Ask the question or name the task.
- Mention the object affected.
- Repeat the verb on the main button.
- Link the title to the dialog for screen readers.

### When to use

- Top of every dialog and drawer.

### How to use

- `<h2 class="orca-dialog-title">` (24/32, light 275).
- Confirmations name the object: 'Delete Harbour at dusk?'. The action button repeats the verb: 'Delete image'.

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

### General description

An empty-state title is the short heading shown when a list, table or search has nothing to display. It says plainly what is missing.

#### Use cases

- Showing a new, empty list.
- Showing a search or filter with no matches.
- Showing a chart with no data yet.

#### When not to use it

- Content that is still loading: show a loading state instead.
- Errors: use an error message that says what went wrong.

#### Best practices

- State what is missing in plain words.
- Keep it calm and short.
- Avoid blaming the person.
- Pair it with a next step.

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

### General description

Empty-state text is a short sentence under the empty-state title. It explains why nothing is shown and what to do next.

#### Use cases

- Inviting people to create their first item.
- Suggesting they clear filters after no results.
- Explaining why data is not there yet.

#### When not to use it

- Long help articles: link to documentation.
- Jokes or blame in work tools: stay neutral and useful.

#### Best practices

- Say what to do next.
- Keep it to one or two sentences.
- Offer the action as a button.
- Fit the text to the cause, new or filtered.

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
