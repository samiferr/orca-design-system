from ..registry import add, category
from . import Pattern

C = category(
    "process", "Process and status",
    "Following a long-running job: what is done, what is happening, what failed and what to do next.",
    level="pattern",
)

add(Pattern(
    "capture-run-progress", "Video export progress", C,
    "A running job's progress: overall bar with counts and time left, the steps, and each video's state.",
    why="Long waits feel shorter and trustworthy when people see progress, the current step and an estimate (Doherty threshold); per-item status shows exactly what failed so it can be retried (Peak–end rule).",
    when=["Video exports, imports, bulk updates: anything running longer than ~10 seconds."],
    how=["`<section class=\"orca-run-progress\" aria-live=\"polite\">` with progress-with-counts, steps (done, current), and `<ul class=\"orca-run-progress__cams\">` with each item's status light.",
         "Offer 'Cancel run' (confirmed) while it runs and 'Retry failed' at the end; refresh with htmx polling every few seconds, not every frame.",
         "End with an alert stating what was done and what failed."],
    classes=[".orca-run-progress", ".orca-run-progress__cams"],
    laws=["doherty", "peak-end", "miller"],
    uses=["progress-with-counts", "steps", "status-light", "confirm-dialog"],
    examples=[("Run", """<section class="orca-run-progress" aria-live="polite" aria-labelledby="crp-t" style="max-width: 40rem">
  <div class="orca-panel-header"><div class="orca-panel-header__text"><h2 class="orca-panel-title" id="crp-t">Morning video export</h2><p class="orca-panel-header__desc">Started 08:00 by Ada Lovelace</p></div><div class="orca-panel-header__actions"><button class="orca-button orca-button--outline-danger orca-button--dense" type="button">Cancel run</button></div></div>
  <div class="orca-progress-counts" style="max-width: none"><div class="orca-progress-counts__head"><span>Taking snapshots</span><span class="orca-progress-counts__value">64%</span></div><progress class="orca-progress orca-progress--lg" value="77" max="120" aria-label="77 of 120 shots"></progress><div class="orca-progress-counts__meta"><span>77 of 120 shots</span><span>About 4 minutes left</span></div></div>
  <ol class="orca-steps"><li class="orca-steps__item orca-steps__item--done"><span class="orca-step-marker orca-step-marker--done" aria-hidden="true"></span><span class="orca-steps__title">Connect</span></li><li class="orca-steps__item" aria-current="step"><span class="orca-step-marker orca-step-marker--current" aria-hidden="true"></span><span class="orca-steps__title">Capture</span></li><li class="orca-steps__item"><span class="orca-step-marker" aria-hidden="true"></span><span class="orca-steps__title">Count</span></li></ol>
  <ul class="orca-run-progress__cams"><li>Entrance A <span class="orca-status"><span class="orca-dot orca-dot--positive"></span>Done</span></li><li>Gate 1 <span class="orca-status"><span class="orca-spinner orca-spinner--sm" aria-hidden="true"></span>Capturing</span></li><li>Loading dock <span class="orca-status"><span class="orca-dot orca-dot--negative"></span>Failed</span></li></ul>
</section>""")],
    guide=["Video export progress"], source="Tangerine",
))
