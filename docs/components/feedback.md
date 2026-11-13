# Feedback

How the system tells people what happened and what to do next: alerts, callouts, toasts, dialogs, empty states and progress.

## Alert

`id: alert` · level: component · source: Tangerine

An event message in a white box with a coloured side bar: icon, title, text and optional actions.

Built from: `alert-icon`, `alert-title`, `button`

### When to use

- Results of an action that stay on the page: a failed test, a video offline, a saved setting with a warning.
- Server messages after a redirect (see flash message).

### When not to use

- Permanent guidance: use a callout.
- Short success confirmations: use a toast.

### How to use

- `<div class="orca-alert orca-alert--negative" role="alert">` with `{% status_icon "negative" %}`, `.orca-alert__title`, `.orca-alert__body`, optional `.orca-alert__actions` and a dismiss button `.orca-alert__close` with `data-orca-dismiss`.
- Tones: info (default), positive, caution, negative, neutral. Use `role="alert"` for errors only; `role="status"` otherwise.
- Title states the fact; body says what to do. No 'Error:' prefix.

#### Example: Tones

```django
<div class="orca-stack" style="gap: var(--orca-space-12)">
  <div class="orca-alert orca-alert--negative" role="alert">
    {% status_icon "negative" %}
    <p class="orca-alert__title">Media server unreachable</p>
    <p class="orca-alert__body">Check that the media server is on and connected, then test again.</p>
    <div class="orca-alert__actions">
      <button class="orca-button orca-button--dense" type="button">Test again</button>
    </div>
    <button class="orca-icon-button orca-icon-button--dense orca-alert__close" type="button" aria-label="Dismiss" data-orca-dismiss>
      {% icon "close" %}
    </button>
  </div>
  <div class="orca-alert orca-alert--positive" role="status">
    {% status_icon "positive" %}
    <p class="orca-alert__title">Connection works</p>
    <p class="orca-alert__body">The stream answered in 120 ms.</p>
  </div>
  <div class="orca-alert orca-alert--caution" role="status">
    {% status_icon "caution" %}
    <p class="orca-alert__title">Disk 90% full</p>
    <p class="orca-alert__body">Recordings older than 20 days will be deleted tonight.</p>
  </div>
</div>
```

**Classes:** `.orca-alert`, `.orca-alert--positive`, `.orca-alert--caution`, `.orca-alert--negative`, `.orca-alert--neutral`, `.orca-alert__title`, `.orca-alert__body`, `.orca-alert__actions`, `.orca-alert__close`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI W15: Help people recover from errors; Peak–end rule: people judge an experience by its peak and its end; Practical UI C03: Communicate meaning beyond colour

**Related:** `callout`, `toast`, `flash-message`

**ORCA guide items covered:** Alert

---

## Callout (info, success, warning, danger)

`id: callout` · level: component · source: ORCA

A tinted box of guidance that belongs to the page, not to an event.

Built from: `status-icon`

### When to use

- Explaining a consequence before people act ('Deleting a site deletes its videos').
- Tips and limits on settings pages.

### When not to use

- Events and results: use an alert.
- More than one callout per section (banner blindness).

### How to use

- `<div class="orca-callout orca-callout--caution">{% icon "warning" %}<p class="orca-callout__title">…</p><div class="orca-callout__body">…</div></div>`.
- Tones: info (default), positive (success), caution (warning), negative (danger). Danger only for irreversible consequences.

#### Example: Four tones

```django
<div class="orca-stack" style="gap: var(--orca-space-12)">
  <div class="orca-callout">
    {% icon "info" %}
    <p class="orca-callout__title">Counts update every minute</p>
    <p class="orca-callout__body">Older data is grouped by hour after 30 days.</p>
  </div>
  <div class="orca-callout orca-callout--positive">
    {% icon "success" %}
    <p class="orca-callout__title">All videos are online</p>
  </div>
  <div class="orca-callout orca-callout--caution">
    {% icon "warning" %}
    <p class="orca-callout__title">This changes past reports</p>
    <p class="orca-callout__body">Moving a zone recalculates the last 7 days.</p>
  </div>
  <div class="orca-callout orca-callout--negative">
    {% icon "error" %}
    <p class="orca-callout__title">Deleting a site deletes its videos</p>
    <p class="orca-callout__body">Their counts are kept in reports.</p>
  </div>
</div>
```

**Classes:** `.orca-callout`, `.orca-callout--positive`, `.orca-callout--caution`, `.orca-callout--negative`, `.orca-callout__title`, `.orca-callout__body`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI C04: Reserve status colours for their meanings; Practical UI B13: Scale friction to the consequence

**ORCA guide items covered:** Callout (info, success, warning, danger)

---

## Empty state

`id: empty-state` · level: component · source: Tangerine

Illustration, title, explanation and the next action, where a list or page has nothing yet.

Built from: `illustration`, `empty-title`, `empty-text`, `button`

### When to use

- First use (no records yet); filters that match nothing; a cleared inbox.

### When not to use

- Small regions like a chart or a table cell: use the no-data state.

### How to use

- `<div class="orca-empty">{% orca_illustration "empty" %}<h2 class="orca-empty-title">…</h2><p class="orca-empty-text">…</p><div class="orca-empty__actions">…</div></div>`.
- First use: the create action. Filtered: 'Clear filters'. Search: the 'search' illustration and the query in the title.

#### Example: First use and no results

```django
<div class="orca-row" style="align-items: flex-start; gap: var(--orca-space-32)">
  <div class="orca-empty">
    {% orca_illustration "empty" %}
    <h2 class="orca-empty-title">No videos yet</h2>
    <p class="orca-empty-text">Add a video to start counting people at an entrance.</p>
    <div class="orca-empty__actions">
      <a class="orca-button orca-button--primary" href="#">
        {% icon "plus" %}
        Add video
      </a>
    </div>
  </div>
  <div class="orca-empty">
    {% orca_illustration "search" %}
    <h2 class="orca-empty-title">No events match “dock”</h2>
    <p class="orca-empty-text">Check the spelling or clear the filters.</p>
    <div class="orca-empty__actions">
      <button class="orca-button" type="button">Clear filters</button>
    </div>
  </div>
</div>
```

**Classes:** `.orca-empty`, `.orca-empty__actions`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Empty state

---

## No-data state

`id: no-data-state` · level: component · source: ORCA

A compact message inside a chart, table or tile that has no data for the chosen period.

Built from: `muted-text`

### When to use

- Charts, KPI tiles and table bodies with no data for the current filters or period.

### How to use

- `<div class="orca-no-data" role="status"><strong>No data for this period</strong>Counting started on 3 March.</div>` sized like the content it replaces.
- In a table, put it in one cell spanning all columns.

#### Example: In a chart area

```django
<div class="orca-no-data" role="status" style="max-width: 24rem"><strong>No data for this period</strong>Counting started on 3 March 2026.</div>
```

**Classes:** `.orca-no-data`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** No-data state

---

## Status light

`id: status-light` · level: component · source: Tangerine

A dot, a status word and an optional time: 'Offline since 08:14'.

Built from: `status-dot`, `time-label`

### When to use

- Device, service or job state in lists, cards and headers.

### How to use

- `<span class="orca-status"><span class="orca-dot orca-dot--negative"></span>Offline <span class="orca-status__meta">since 08:14</span></span>`.
- Use the same words everywhere: Online, Offline, Degraded, Disabled.

#### Example: Status lights

```django
<div class="orca-stack">
  <span class="orca-status"><span class="orca-dot orca-dot--positive"></span>Online <span class="orca-status__meta">for 12 days</span></span>
  <span class="orca-status"><span class="orca-dot orca-dot--negative"></span>Offline <span class="orca-status__meta">since <time datetime="2026-11-06T08:14">08:14</time></span></span>
  <span class="orca-status"><span class="orca-dot orca-dot--caution"></span>Degraded <span class="orca-status__meta">2 of 4 streams</span></span>
</div>
```

**Classes:** `.orca-status`, `.orca-status__meta`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Status light

---

## Dialog

`id: dialog` · level: component · source: ORCA

A modal window with a title, a body and actions, built on the native <dialog>.

Built from: `dialog-backdrop`, `dialog-title`, `button`, `icon-button`

### When to use

- Short focused tasks: rename, confirm, pick an option.

### When not to use

- Long forms or content people compare with the page: use a page or a drawer.

### How to use

- `<dialog class="orca-dialog" id=… aria-labelledby=…>` with `.orca-dialog__header` (title + close icon button with `data-orca-dialog-close`), `.orca-dialog__body` and `.orca-dialog__footer`.
- Open with a button carrying `data-orca-dialog-open="id"`; forms inside use `method="dialog"` or post normally.
- `--lg` for wider content. Primary action first in the footer.

### Accessibility

- Focus moves into the dialog and returns to the opener when it closes.

#### Example: Rename dialog

```django
<button class="orca-button" type="button" data-orca-dialog-open="dl-rename">Rename video</button>
<dialog class="orca-dialog" id="dl-rename" aria-labelledby="dl-rename-t">
  <form method="dialog">
    <div class="orca-dialog__header">
      <h2 class="orca-dialog-title" id="dl-rename-t">Rename video</h2>
      <button class="orca-icon-button" type="button" aria-label="Close" data-orca-dialog-close>
        {% icon "close" %}
      </button>
    </div>
    <div class="orca-dialog__body">
      <div class="orca-field">
        <label class="orca-label" for="dl-name">Name</label>
        <input class="orca-input" id="dl-name" value="Entrance A">
      </div>
    </div>
    <div class="orca-dialog__footer">
      <button class="orca-button orca-button--primary" type="submit" value="save">Save name</button>
      <button class="orca-button" type="submit" value="cancel">Cancel</button>
    </div>
  </form>
</dialog>
```

**Classes:** `.orca-dialog`, `.orca-dialog__header`, `.orca-dialog__body`, `.orca-dialog__footer`, `.orca-dialog--lg`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Postel's law: accept varied input, output reliable and accessible UI; Practical UI B08: Keep action order predictable

**Related:** `confirm-dialog`

**ORCA guide items covered:** Dialog

---

## Confirm dialog

`id: confirm-dialog` · level: component · source: Tangerine

A dialog that names the consequence and the action before something irreversible happens.

Built from: `dialog-title`, `button`, `checkbox`

### When to use

- Deleting, cancelling a run, revoking access: anything that cannot be undone.

### When not to use

- Reversible actions: do them and offer Undo in a toast.

### How to use

- Markup: a dialog with a question title ('Delete Entrance A?'), one sentence of consequence, a `--danger` button repeating the verb and object, and Cancel (focused first).
- Shortcut: add `data-orca-confirm="Its zones and alert rules are deleted." data-orca-confirm-title="Delete Entrance A?" data-orca-confirm-action="Delete video"` to the form or submit button.
- Very serious consequences: add a required acknowledgement checkbox in `.orca-dialog__ack`.

#### Example: Shortcut attribute

```django
<form method="post" action="#" onsubmit="return false" data-orca-confirm="Shots already taken are kept." data-orca-confirm-title="Cancel this run?" data-orca-confirm-action="Cancel run">
  <button class="orca-button orca-button--outline-danger" type="submit">Cancel run</button>
</form>
```

#### Example: With acknowledgement

```django
<button class="orca-button orca-button--outline-danger" type="button" data-orca-dialog-open="cd-site">Delete site</button>
<dialog class="orca-dialog" id="cd-site" aria-labelledby="cd-site-t">
  <form method="dialog">
    <div class="orca-dialog__header">
      <h2 class="orca-dialog-title" id="cd-site-t">Delete North building?</h2>
    </div>
    <div class="orca-dialog__body">
      <p class="orca-p">Its 12 videos, 5 zones and alert rules are deleted. Reports keep their counts.</p>
      <label class="orca-check orca-dialog__ack"><input type="checkbox" required><span class="orca-check__box"></span>I understand this cannot be undone</label>
    </div>
    <div class="orca-dialog__footer">
      <button class="orca-button orca-button--danger" type="submit" value="delete">Delete site</button>
      <button class="orca-button" type="submit" value="cancel" formnovalidate autofocus>Cancel</button>
    </div>
  </form>
</dialog>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py — the dialog only confirms; the delete is a POST the server checks
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import Video


@require_POST
def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk, owner=request.user)
    video.delete()
    messages.success(request, f"Video “{video}” deleted.")
    return redirect("video-list")
```

**Classes:** `.orca-dialog`, `.orca-dialog__ack`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI B13: Scale friction to the consequence; Peak–end rule: people judge an experience by its peak and its end; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Confirm dialog

---

## Progress bar with counts

`id: progress-with-counts` · level: component · source: ORCA

A labelled progress bar with the value in words and the counts behind it.

Built from: `progress-bar`, `tabular-number`

### When to use

- Video exports, imports, uploads, batch operations.

### How to use

- `<div class="orca-progress-counts">` with `__head` (label and `__value` '64%'), a `<progress class="orca-progress">`, and `__meta` ('77 of 120 shots · about 4 minutes left · 2 failed').
- Update at most once a second; announce completion with a toast or alert.

#### Example: Video export

```django
<div class="orca-progress-counts">
  <div class="orca-progress-counts__head">
    <span id="pc-l">Morning video export</span>
    <span class="orca-progress-counts__value">64%</span>
  </div>
  <progress class="orca-progress orca-progress--lg" value="77" max="120" aria-labelledby="pc-l">77 of 120</progress>
  <div class="orca-progress-counts__meta">
    <span>77 of 120 shots</span>
    <span>About 4 minutes left</span>
    <span class="orca-with-icon">
      {% status_icon "negative" size="xs" %}
      2 failed
    </span>
  </div>
</div>
```

**Classes:** `.orca-progress-counts`, `.orca-progress-counts__head`, `.orca-progress-counts__value`, `.orca-progress-counts__meta`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Progress bar with counts

---

## Toast

`id: toast` · level: component · source: ORCA

A short message that appears at the bottom corner after an action and goes away by itself; several stack.

Built from: `status-icon`, `button`

### When to use

- Confirmations of completed, low-risk actions: 'Report sent', 'Video disabled. Undo'.

### When not to use

- Errors that need action: use an alert (toasts with errors do not auto-dismiss).
- Anything people must read later.

### How to use

- Script: `ORCA.toast("Report sent", {tone: "positive"})`; with an action: `{action: {label: "Undo", onClick: fn}}`.
- Server-rendered: an `<ol class="orca-toast-stack" aria-live="polite">` of `.orca-toast` items (icon, `.orca-toast__text`, `.orca-toast__actions`).
- Auto-dismiss after 6 s, paused on hover and focus; negative toasts stay until dismissed. One sentence, no title.

### Accessibility

- The stack is a polite live region; never move focus to a toast.

#### Example: Static stack and a trigger

```django
<ol class="orca-toast-stack orca-toast-stack--static" aria-label="Notifications">
  <li class="orca-toast orca-toast--positive">
    {% icon "success" %}
    <p class="orca-toast__text">Video disabled</p>
    <div class="orca-toast__actions">
      <button class="orca-button orca-button--link" type="button">Undo</button>
      <button class="orca-icon-button" type="button" aria-label="Dismiss" data-orca-dismiss>
        {% icon "close" %}
      </button>
    </div>
  </li>
  <li class="orca-toast orca-toast--info">
    {% icon "info" %}
    <p class="orca-toast__text">Report scheduled for 07:00</p>
    <div class="orca-toast__actions">
      <button class="orca-icon-button" type="button" aria-label="Dismiss" data-orca-dismiss>
        {% icon "close" %}
      </button>
    </div>
  </li>
</ol>
<button class="orca-button" type="button" data-orca-toast="Report sent" data-orca-toast-tone="positive" style="margin-top: var(--orca-space-16)">Show a toast</button>
```

**Classes:** `.orca-toast-stack`, `.orca-toast`, `.orca-toast__text`, `.orca-toast__actions`, `.orca-toast-stack--static`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Toast; Toast stack

---

## Flash message

`id: flash-message` · level: component · source: ORCA

Django messages shown as dismissible alerts at the top of the next page.

Built from: `alert`

### When to use

- Results of form posts that redirect: created, saved, deleted, failed.

### How to use

- Put `{% orca_messages %}` at the top of the main content in the base template.
- In views: `messages.success(request, "Video saved")`, `messages.error(…)`, `messages.warning(…)`, `messages.info(…)`.
- Errors render with `role="alert"`, others with `role="status"`.

#### Example: Rendered messages

```django
<div class="orca-messages">
  <div class="orca-alert orca-alert--positive" role="status">
    {% status_icon "positive" %}
    <p class="orca-alert__body">Video “Entrance A” saved.</p>
    <button class="orca-icon-button orca-icon-button--dense orca-alert__close" type="button" aria-label="Dismiss message" data-orca-dismiss>
      {% icon "close" %}
    </button>
  </div>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py — needs django.contrib.messages in INSTALLED_APPS and its middleware
from django.contrib import messages
from django.shortcuts import redirect


def publish(request, pk):
    video = publish_video(pk)
    messages.success(request, f"Video “{video}” published.")      # positive
    # messages.info / warning / error give the information, caution and negative tones.
    return redirect("video-detail", pk=pk)
    # The app shell shows messages under the page head; elsewhere use {% orca_messages %}.
```

**Classes:** `.orca-messages`, `.orca-alert`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Flash message

---

## Tooltip

`id: tooltip` · level: component · source: ORCA

A short label that appears on hover and keyboard focus, naming an icon-only control.

Built from: `icon-button`

### When to use

- Icon-only buttons in toolbars; truncated labels.

### When not to use

- Essential information or anything interactive inside the tip (Practical UI R08, B07).
- Touch-first screens: show the label instead.

### How to use

- `<span class="orca-tooltip-wrap"><button class="orca-icon-button" aria-label="Refresh" aria-describedby="tt-1">…</button><span class="orca-tooltip" role="tooltip" id="tt-1">Refresh</span></span>`.
- Appears after 0.3 s on hover, at once on focus; Escape hides it. `--below` places it under the trigger.
- Text of a few words, sentence case, no full stop.

#### Example: Tooltip

```django
<div style="padding-top: var(--orca-space-32)">
  <span class="orca-tooltip-wrap">
    <button class="orca-icon-button orca-icon-button--outlined" type="button" aria-label="Refresh counts">
      {% icon "restart" %}
    </button>
    <span class="orca-tooltip" role="tooltip">Refresh counts</span>
  </span>
</div>
```

**Classes:** `.orca-tooltip-wrap`, `.orca-tooltip`, `.orca-tooltip--below`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI B07: Explain necessary disabled states; Practical UI R08: Put essential help before the input

**ORCA guide items covered:** Tooltip

---

## Card skeleton

`id: card-skeleton` · level: component · source: ORCA

The grey shape of a card (image, title, two lines) while the real card loads.

Built from: `skeleton`

### When to use

- Grids and feeds that load cards after the page.

### When not to use

- Content that arrives in under a second: show nothing.

### How to use

- `<div aria-hidden="true"><div class="orca-skeleton orca-aspect-16x9"></div><div class="orca-skeleton orca-skeleton--title"></div><div class="orca-skeleton orca-skeleton--text"></div></div>`; the region around the placeholders has `aria-busy="true"` and a label.

### Accessibility

- Placeholders are hidden from assistive technology; the region's label says what is loading.

#### Example: Card skeleton

```django
<div aria-busy="true" aria-label="Loading video" style="max-width: 16rem; padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border)">
  <div aria-hidden="true">
    <div class="orca-skeleton orca-aspect-16x9" style="margin-bottom: var(--orca-space-8)"></div>
    <div class="orca-skeleton orca-skeleton--title"></div>
    <div class="orca-skeleton orca-skeleton--text" style="max-width: 70%"></div>
  </div>
</div>
```

**Classes:** `.orca-skeleton`, `.orca-skeleton--title`, `.orca-skeleton--text`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower

**Related:** `video-grid`, `loading-placeholder`

---
