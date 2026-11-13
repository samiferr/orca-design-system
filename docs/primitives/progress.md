# Progress

Feedback while something takes time. Respond within 400 ms; show progress for longer; describe the step past 10 seconds.

## Progress bar

`id: progress-bar` · level: primitive · source: Tangerine

A 3px (or 8px large) track with a fill: determinate with a value, indeterminate without.

### General description

A progress bar is a horizontal track that fills to show how much of a task is done, or that animates when the time left is unknown.

#### Use cases

- Showing upload, export or import progress.
- Showing storage or quota use.
- Showing steps completed in a task.

#### When not to use it

- Waits under about a second; a spinner is enough.
- Tasks with no measurable progress; use a spinner with a message.

#### Best practices

- Label every bar and show the value as text.
- Say what is happening for long waits.
- Announce completion to screen readers.
- Use color tones only with a text value.

### When to use

- Uploads, exports, imports and any task over about 1 second, whether progress is known (determinate) or not (indeterminate).
- Capacity or quota meters (use the track and fill parts with a status tone).

### When not to use

- Waits under 1 second: a spinner on the button is enough.

### How to use

- Determinate: `<progress class="orca-progress" value="64" max="100" aria-labelledby=…>64%</progress>` with a label and the value in text beside it.
- Indeterminate: omit `value`; it animates (static for reduced motion).
- Large: `.orca-progress--lg`. Tones for meters: `--positive`, `--caution`, `--negative`.
- Custom meter from parts: `<span class="orca-progress-track"><span class="orca-progress-fill" style="--orca-value: 64%"></span></span>` with `role="meter"` and aria values.
- Past 10 seconds, say what is happening and how long is left ('Uploading 3 of 12 files, about 2 minutes left').

### Accessibility

- Label every bar; announce completion in a `role="status"` region.

#### Example: Determinate and indeterminate

```django
<div class="orca-stack" style="max-width: 20rem">
  <div class="orca-row" style="justify-content: space-between">
    <span id="pb1">Video export</span>
    <span class="orca-num orca-muted">64%</span>
  </div>
  <progress class="orca-progress" value="64" max="100" aria-labelledby="pb1">64%</progress>
  <span id="pb2" class="orca-small orca-muted">Preparing the video, this can take up to 15 seconds</span>
  <progress class="orca-progress" aria-labelledby="pb2"></progress>
  <span id="pb3">Disk used</span>
  <span class="orca-progress-track" role="meter" aria-labelledby="pb3" aria-valuenow="91" aria-valuemin="0" aria-valuemax="100" style="height: 0.5rem">
    <span class="orca-progress-fill orca-progress-fill--negative" style="--orca-value: 91%"></span>
  </span>
</div>
```

**Classes:** `.orca-progress`, `.orca-progress--lg`, `.orca-progress-track`, `.orca-progress-fill`

**Tokens:** `--orca-accent`, `--orca-border`, `--orca-bar`, `--orca-radius-bar`, `--orca-duration-brisk`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Peak–end rule: people judge an experience by its peak and its end

**Related:** `progress-ring`, `spinner`

**ORCA guide items covered:** Progress track; Progress fill; Progress bar (default, large)

---

## Progress ring

`id: progress-ring` · level: primitive · source: ORCA

A circular track and indicator with the value in the middle.

### General description

A progress ring is a circular indicator that fills to show a percentage, often with the value in the middle.

#### Use cases

- Showing completion in small tiles.
- Showing a task's percent done.
- Showing quota use in a compact space.

#### When not to use it

- Long operations whose estimate changes; use a bar with text.
- Showing precise comparisons; a bar is easier to read.

#### Best practices

- Put the value in text inside or beside the ring.
- Give it an accessible name.
- Keep it large enough to read.
- Do not rely on color alone.

### When to use

- Compact completion values: a task's percent done, a quota in a tile.

### When not to use

- Long operations with changing estimates: a bar with text is clearer.

### How to use

- `<span class="orca-ring" role="progressbar" aria-valuenow="72" aria-valuemin="0" aria-valuemax="100" aria-label=… style="--orca-value: 72">` containing an svg with `circle.orca-ring__track` and `circle.orca-ring__indicator` (r=15.9155, pathLength 100) and `<span class="orca-ring__label">72%</span>`.
- `.orca-ring--lg` for 64px.

#### Example: Rings

```django
<div class="orca-row orca-row--16">
  <span class="orca-ring" role="progressbar" aria-label="Setup" aria-valuenow="72" aria-valuemin="0" aria-valuemax="100" style="--orca-value: 72">
    <svg viewBox="0 0 36 36" aria-hidden="true">
      <circle class="orca-ring__track" cx="18" cy="18" r="15.9155" pathLength="100"/>
      <circle class="orca-ring__indicator" cx="18" cy="18" r="15.9155" pathLength="100"/>
    </svg>
    <span class="orca-ring__label">72%</span>
  </span>
  <span class="orca-ring orca-ring--lg" role="progressbar" aria-label="Quota" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100" style="--orca-value: 30">
    <svg viewBox="0 0 36 36" aria-hidden="true">
      <circle class="orca-ring__track" cx="18" cy="18" r="15.9155" pathLength="100"/>
      <circle class="orca-ring__indicator" cx="18" cy="18" r="15.9155" pathLength="100"/>
    </svg>
    <span class="orca-ring__label">30%</span>
  </span>
</div>
```

**Classes:** `.orca-ring`, `.orca-ring__track`, `.orca-ring__indicator`, `.orca-ring__label`, `.orca-ring--lg`

**Tokens:** `--orca-accent`, `--orca-border`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Progress ring (track, indicator)

---

## Spinner

`id: spinner` · level: primitive · source: Tangerine

A small rotating ring for short, unknown waits.

### General description

A spinner is a small rotating icon showing that something is loading when the wait time is unknown.

#### Use cases

- Showing a busy button.
- Showing a field being checked.
- Showing a small region loading.

#### When not to use it

- Whole page loads or long waits; use a skeleton or progress bar.
- Very short waits; flashing feels worse.

#### Best practices

- Pair it with a short text message.
- Announce it as a status to screen readers.
- Keep it small and calm.
- Replace it with content as soon as ready.

### When to use

- Inside a busy button, beside a field being checked, or in a region that loads in a few seconds.

### When not to use

- Whole pages or waits longer than ~3 seconds: use a skeleton or a progress bar with a message.

### How to use

- `<span class="orca-spinner" role="status" aria-label="Loading"></span>`; sizes `--sm` (12px), default (16px), `--lg` (36px).
- Inherits `color`; inside a filled button set `style="color: inherit"`.
- In a busy button the spinner is decorative and the button gets `aria-busy="true"`.

### Accessibility

- Pair with text ('Searching the library…') in a `role="status"` element.

#### Example: Sizes and with text

```django
<div class="orca-row orca-row--16">
  <span class="orca-spinner orca-spinner--sm" aria-hidden="true"></span>
  <span class="orca-spinner" aria-hidden="true"></span>
  <span class="orca-spinner orca-spinner--lg" aria-hidden="true"></span>
  <span class="orca-with-icon" role="status"><span class="orca-spinner" aria-hidden="true"></span>Searching the library…</span>
</div>
```

**Classes:** `.orca-spinner`, `.orca-spinner--sm`, `.orca-spinner--lg`

**Tokens:** `--orca-text-muted`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Spinner (sm, default, lg); Spinner

---

## Skeleton

`id: skeleton` · level: primitive · source: ORCA

Grey placeholder blocks that hold the shape of content while it loads.

### General description

A skeleton is a grey placeholder shaped like the content that is loading. It shows the page layout early and makes waiting feel shorter.

#### Use cases

- Loading cards, lists and tables.
- Loading image and video grids.
- Loading sections that arrive after the page.

#### When not to use it

- Content that loads almost instantly; the flash is distracting.
- Waits where no layout is known; use a spinner.

#### Best practices

- Match the real layout closely.
- Vary line widths to look like text.
- Mark the region as busy for screen readers.
- Swap in content without moving the layout.

### When to use

- Heavy regions that load after the page: heat maps, image and video grids, comparison tables, htmx `hx-trigger="load"` sections.

### When not to use

- Content that loads in under ~300 ms (the flash is worse than nothing).

### How to use

- Mirror the real layout: `.orca-skeleton--title`, `.orca-skeleton--text` (vary widths with inline `max-width`), `.orca-skeleton--circle`, or a sized `.orca-skeleton` block.
- Wrap the region in `aria-busy="true"` and give it an accessible label such as 'Loading images'; remove both when content arrives.

### Accessibility

- The shimmer stops for reduced motion. Skeleton blocks are `aria-hidden`.

#### Example: Card skeleton

```django
<div aria-busy="true" aria-label="Loading image" style="max-width: 18rem; padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border)">
  <div aria-hidden="true">
    <div class="orca-skeleton orca-aspect-16x9" style="margin-bottom: var(--orca-space-8)"></div>
    <div class="orca-skeleton orca-skeleton--title"></div>
    <div class="orca-skeleton orca-skeleton--text" style="max-width: 80%"></div>
    <div class="orca-skeleton orca-skeleton--text" style="max-width: 50%"></div>
  </div>
</div>
```

**Classes:** `.orca-skeleton`, `.orca-skeleton--text`, `.orca-skeleton--title`, `.orca-skeleton--circle`

**Tokens:** `--orca-bg-hover`, `--orca-bg-active`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower

---
