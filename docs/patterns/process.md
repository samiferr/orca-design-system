# Process and status

Following a long-running job: what is done, what is happening, what failed and what to do next.

## Video export progress

`id: capture-run-progress` · level: pattern · source: Tangerine

A running job's progress: overall bar with counts and time left, the steps, and each video's state.

Built from: `progress-with-counts`, `steps`, `status-light`, `confirm-dialog`

### General description

A view of a long-running job, such as an export, that shows overall progress, the current step, time left and the result for each item.

#### Use cases

- Following exports, imports and bulk updates.
- Showing which items finished or failed.
- Letting people cancel or retry a job.

#### When not to use it

- Quick actions under about 10 seconds: a simple spinner is enough.
- Jobs that run in the background for hours: send a notification when done.

#### Best practices

- Show progress, the current step and an estimate.
- Tell screen readers about updates politely.
- Update at a calm pace, not every frame.
- End with a clear summary and a way to retry failures.

### When to use

- Video exports, imports, bulk updates: anything running longer than ~10 seconds.

### How to use

- `<section class="orca-run-progress" aria-live="polite">` with progress-with-counts, steps (done, current), and `<ul class="orca-run-progress__cams">` with each item's status light.
- Offer 'Cancel run' (confirmed) while it runs and 'Retry failed' at the end; refresh with htmx polling every few seconds, not every frame.
- End with an alert stating what was done and what failed.

#### Example: Run

```django
<section class="orca-run-progress" aria-live="polite" aria-labelledby="crp-t" style="max-width: 40rem">
  <div class="orca-panel-header">
    <div class="orca-panel-header__text">
      <h2 class="orca-panel-title" id="crp-t">Morning video export</h2>
      <p class="orca-panel-header__desc">Started 08:00 by Ada Lovelace</p>
    </div>
    <div class="orca-panel-header__actions">
      <button class="orca-button orca-button--outline-danger orca-button--dense" type="button">Cancel run</button>
    </div>
  </div>
  <div class="orca-progress-counts" style="max-width: none">
    <div class="orca-progress-counts__head">
      <span>Taking snapshots</span>
      <span class="orca-progress-counts__value">64%</span>
    </div>
    <progress class="orca-progress orca-progress--lg" value="77" max="120" aria-label="77 of 120 shots"></progress>
    <div class="orca-progress-counts__meta">
      <span>77 of 120 shots</span>
      <span>About 4 minutes left</span>
    </div>
  </div>
  <ol class="orca-steps">
    <li class="orca-steps__item orca-steps__item--done">
      <span class="orca-step-marker orca-step-marker--done" aria-hidden="true"></span>
      <span class="orca-steps__title">Connect</span>
    </li>
    <li class="orca-steps__item" aria-current="step">
      <span class="orca-step-marker orca-step-marker--current" aria-hidden="true"></span>
      <span class="orca-steps__title">Capture</span>
    </li>
    <li class="orca-steps__item">
      <span class="orca-step-marker" aria-hidden="true"></span>
      <span class="orca-steps__title">Count</span>
    </li>
  </ol>
  <ul class="orca-run-progress__cams">
    <li>Entrance A <span class="orca-status"><span class="orca-dot orca-dot--positive"></span>Done</span></li>
    <li>Gate 1 <span class="orca-status"><span class="orca-spinner orca-spinner--sm" aria-hidden="true"></span>Capturing</span></li>
    <li>Loading dock <span class="orca-status"><span class="orca-dot orca-dot--negative"></span>Failed</span></li>
  </ul>
</section>
```

**Classes:** `.orca-run-progress`, `.orca-run-progress__cams`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Peak–end rule: people judge an experience by its peak and its end; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Video export progress

---
