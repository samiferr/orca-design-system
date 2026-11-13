from .registry import Element, add, category

C = category(
    "progress", "Progress",
    "Feedback while something takes time. Respond within 400 ms; show progress for longer; describe the step past 10 seconds.",
)

add(Element(
    "progress-bar", "Progress bar", C,
    "A 3px (or 8px large) track with a fill: determinate with a value, indeterminate without.",
    why="A progress bar makes a wait tolerable and shows the system is working (Doherty threshold); a visible end point "
        "motivates finishing (goal-gradient). Native `<progress>` is announced by screen readers.",
    when=["Uploads, exports, imports and any task over about 1 second, whether progress is known (determinate) or not (indeterminate).",
          "Capacity or quota meters (use the track and fill parts with a status tone)."],
    avoid=["Waits under 1 second: a spinner on the button is enough."],
    how=["Determinate: `<progress class=\"orca-progress\" value=\"64\" max=\"100\" aria-labelledby=…>64%</progress>` with a label and the value in text beside it.",
         "Indeterminate: omit `value`; it animates (static for reduced motion).",
         "Large: `.orca-progress--lg`. Tones for meters: `--positive`, `--caution`, `--negative`.",
         "Custom meter from parts: `<span class=\"orca-progress-track\"><span class=\"orca-progress-fill\" style=\"--orca-value: 64%\"></span></span>` with `role=\"meter\"` and aria values.",
         "Past 10 seconds, say what is happening and how long is left ('Uploading 3 of 12 files, about 2 minutes left')."],
    a11y=["Label every bar; announce completion in a `role=\"status\"` region."],
    classes=[".orca-progress", ".orca-progress--lg", ".orca-progress-track", ".orca-progress-fill"],
    tokens=["accent", "border", "bar", "radius-bar", "duration-brisk"],
    laws=["doherty", "peak-end"],
    examples=[("Determinate and indeterminate", """<div class="orca-stack" style="max-width: 20rem">
  <div class="orca-row" style="justify-content: space-between"><span id="pb1">Video export</span><span class="orca-num orca-muted">64%</span></div>
  <progress class="orca-progress" value="64" max="100" aria-labelledby="pb1">64%</progress>
  <span id="pb2" class="orca-small orca-muted">Preparing the video, this can take up to 15 seconds</span>
  <progress class="orca-progress" aria-labelledby="pb2"></progress>
  <span id="pb3">Disk used</span>
  <span class="orca-progress-track" role="meter" aria-labelledby="pb3" aria-valuenow="91" aria-valuemin="0" aria-valuemax="100" style="height: 0.5rem"><span class="orca-progress-fill orca-progress-fill--negative" style="--orca-value: 91%"></span></span>
</div>""")],
    guide=["Progress track", "Progress fill", "Progress bar (default, large)"],
    related=["progress-ring", "spinner"],
))

add(Element(
    "progress-ring", "Progress ring", C,
    "A circular track and indicator with the value in the middle.",
    why="A ring fits a percentage into a small square (KPI tiles, avatars of tasks) while keeping the value readable in text (Doherty; C03).",
    when=["Compact completion values: a task's percent done, a quota in a tile."],
    avoid=["Long operations with changing estimates: a bar with text is clearer."],
    how=["`<span class=\"orca-ring\" role=\"progressbar\" aria-valuenow=\"72\" aria-valuemin=\"0\" aria-valuemax=\"100\" aria-label=… style=\"--orca-value: 72\">` containing an svg with `circle.orca-ring__track` and `circle.orca-ring__indicator` (r=15.9155, pathLength 100) and `<span class=\"orca-ring__label\">72%</span>`.",
         "`.orca-ring--lg` for 64px."],
    classes=[".orca-ring", ".orca-ring__track", ".orca-ring__indicator", ".orca-ring__label", ".orca-ring--lg"],
    tokens=["accent", "border"],
    laws=["doherty", "C03"],
    examples=[("Rings", """<div class="orca-row orca-row--16">
  <span class="orca-ring" role="progressbar" aria-label="Setup" aria-valuenow="72" aria-valuemin="0" aria-valuemax="100" style="--orca-value: 72"><svg viewBox="0 0 36 36" aria-hidden="true"><circle class="orca-ring__track" cx="18" cy="18" r="15.9155" pathLength="100"/><circle class="orca-ring__indicator" cx="18" cy="18" r="15.9155" pathLength="100"/></svg><span class="orca-ring__label">72%</span></span>
  <span class="orca-ring orca-ring--lg" role="progressbar" aria-label="Quota" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100" style="--orca-value: 30"><svg viewBox="0 0 36 36" aria-hidden="true"><circle class="orca-ring__track" cx="18" cy="18" r="15.9155" pathLength="100"/><circle class="orca-ring__indicator" cx="18" cy="18" r="15.9155" pathLength="100"/></svg><span class="orca-ring__label">30%</span></span>
</div>""")],
    guide=["Progress ring (track, indicator)"], source="ORCA",
))

add(Element(
    "spinner", "Spinner", C,
    "A small rotating ring for short, unknown waits.",
    why="Acknowledges an action immediately when the result takes more than a moment (Doherty threshold).",
    when=["Inside a busy button, beside a field being checked, or in a region that loads in a few seconds."],
    avoid=["Whole pages or waits longer than ~3 seconds: use a skeleton or a progress bar with a message."],
    how=["`<span class=\"orca-spinner\" role=\"status\" aria-label=\"Loading\"></span>`; sizes `--sm` (12px), default (16px), `--lg` (36px).",
         "Inherits `color`; inside a filled button set `style=\"color: inherit\"`.",
         "In a busy button the spinner is decorative and the button gets `aria-busy=\"true\"`."],
    a11y=["Pair with text ('Searching the library…') in a `role=\"status\"` element."],
    classes=[".orca-spinner", ".orca-spinner--sm", ".orca-spinner--lg"], tokens=["text-muted"],
    laws=["doherty"],
    examples=[("Sizes and with text", """<div class="orca-row orca-row--16">
  <span class="orca-spinner orca-spinner--sm" aria-hidden="true"></span>
  <span class="orca-spinner" aria-hidden="true"></span>
  <span class="orca-spinner orca-spinner--lg" aria-hidden="true"></span>
  <span class="orca-with-icon" role="status"><span class="orca-spinner" aria-hidden="true"></span>Searching the library…</span>
</div>""")],
    guide=["Spinner (sm, default, lg)", "Spinner"],
))

add(Element(
    "skeleton", "Skeleton", C,
    "Grey placeholder blocks that hold the shape of content while it loads.",
    why="Showing the layout immediately and filling it in feels faster than a spinner and prevents layout jumps "
        "(Doherty threshold: perceived performance). Added to ORCA because the Laws of UX review found no skeleton pattern.",
    when=["Heavy regions that load after the page: heat maps, image and video grids, comparison tables, htmx `hx-trigger=\"load\"` sections."],
    avoid=["Content that loads in under ~300 ms (the flash is worse than nothing)."],
    how=["Mirror the real layout: `.orca-skeleton--title`, `.orca-skeleton--text` (vary widths with inline `max-width`), `.orca-skeleton--circle`, or a sized `.orca-skeleton` block.",
         "Wrap the region in `aria-busy=\"true\"` and give it an accessible label such as 'Loading images'; remove both when content arrives."],
    a11y=["The shimmer stops for reduced motion. Skeleton blocks are `aria-hidden`."],
    classes=[".orca-skeleton", ".orca-skeleton--text", ".orca-skeleton--title", ".orca-skeleton--circle"],
    tokens=["bg-hover", "bg-active"],
    laws=["doherty"],
    examples=[("Card skeleton", """<div aria-busy="true" aria-label="Loading image" style="max-width: 18rem; padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border)">
  <div aria-hidden="true">
    <div class="orca-skeleton orca-aspect-16x9" style="margin-bottom: var(--orca-space-8)"></div>
    <div class="orca-skeleton orca-skeleton--title"></div>
    <div class="orca-skeleton orca-skeleton--text" style="max-width: 80%"></div>
    <div class="orca-skeleton orca-skeleton--text" style="max-width: 50%"></div>
  </div>
</div>""")],
    guide=[], source="ORCA",
))
