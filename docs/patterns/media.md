# Media

Video players, live streams, photo posts and image galleries.

## Recording player

`id: recording-player` · level: pattern · source: Tangerine

A recorded clip with the native player, a timeline of event marks and a list of events that jump to their moment.

Built from: `video-player`

### When to use

- Alert details, incident reviews, recorded runs.

### How to use

- `<div class="orca-player">` with a video frame (`<video id=… controls preload="metadata">`), `.orca-player__timeline` of `.orca-player__mark` buttons (`style="--orca-at: 25%"`, `data-orca-seek="seconds"`, `aria-controls`), and `.orca-player__events` buttons with time and description.
- Show 'Loading…' with `role="status"` until metadata arrives; give the clip a caption track when it has speech.

#### Example: Player

```django
<div class="orca-player" style="max-width: 32rem">
  <div class="orca-ratio orca-ratio--16x9">
    <video class="orca-video" id="rp-v" controls preload="none" poster="{% static "orca/img/sample-street.svg" %}" aria-label="Entrance A, 08:10 to 08:20"></video>
  </div>
  <div class="orca-player__timeline" role="group" aria-label="Events in this clip">
    <button class="orca-player__mark" type="button" style="--orca-at: 25%; --orca-event: var(--orca-caution)" aria-label="08:12:30, over capacity" data-orca-seek="150" aria-controls="rp-v"></button>
    <button class="orca-player__mark" type="button" style="--orca-at: 62%; --orca-event: var(--orca-negative)" aria-label="08:16:12, door blocked" data-orca-seek="372" aria-controls="rp-v"></button>
  </div>
  <ul class="orca-player__events">
    <li>
      <button type="button" data-orca-seek="150" aria-controls="rp-v"><time>08:12:30</time>Over capacity, 1,560 inside</button>
    </li>
    <li>
      <button type="button" data-orca-seek="372" aria-controls="rp-v"><time>08:16:12</time>Door blocked for 40 s</button>
    </li>
  </ul>
</div>
```

**Classes:** `.orca-player`, `.orca-player__timeline`, `.orca-player__mark`, `.orca-player__events`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Fitts's law: big, close, well-spaced targets are faster and safer; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Recording player

---

## Live stream panel

`id: live-stream-panel` · level: pattern · source: Tangerine

A live video view with its state, a live flag and the live counts beside it.

Built from: `panel`, `video-player`, `status-light`, `stat-card`

### When to use

- Video detail pages and monitoring walls.

### How to use

- A panel with a panel header (video name, status light, Pause/Full-screen actions), a 16:9 frame with the stream and a `.orca-frame__flag` ('Live'), and `.orca-live-panel__stats` (stat label/value pairs).
- When the stream drops, replace it with the removed frame and a message, never a frozen image without notice.

#### Example: Live

```django
<section class="orca-panel orca-live-panel" aria-labelledby="ls-t" style="max-width: 32rem">
  <div class="orca-panel-header">
    <div class="orca-panel-header__text">
      <h2 class="orca-panel-title" id="ls-t">Entrance A</h2>
      <span class="orca-status orca-small"><span class="orca-dot orca-dot--positive"></span>Online · 25 fps</span>
    </div>
    <div class="orca-panel-header__actions">
      <button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Pause stream">
        {% icon "pause" %}
      </button>
      <button class="orca-icon-button orca-icon-button--dense" type="button" aria-label="Full screen">
        {% icon "expand" %}
      </button>
    </div>
  </div>
  <div class="orca-panel__body">
    <div class="orca-ratio orca-ratio--16x9">
      <img src="{% static "orca/img/sample-street.svg" %}" alt="Live view of Entrance A">
      <span class="orca-frame__flag"><span class="orca-dot orca-dot--sm orca-dot--pulse"></span>Live</span>
    </div>
    <div class="orca-live-panel__stats" style="margin-top: var(--orca-space-12)">
      <div>
        <p class="orca-stat-label">In, last hour</p>
        <p class="orca-stat-value">412</p>
      </div>
      <div>
        <p class="orca-stat-label">Out, last hour</p>
        <p class="orca-stat-value">398</p>
      </div>
      <div>
        <p class="orca-stat-label">Inside now</p>
        <p class="orca-stat-value">1,204</p>
      </div>
    </div>
  </div>
</section>
```

**Classes:** `.orca-live-panel`, `.orca-live-panel__stats`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI C03: Communicate meaning beyond colour; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Live stream panel

---

## Photo post

`id: photo-post` · level: pattern · source: ORCA

A shared photo with who posted it and when, the photo, actions and caption.

Built from: `person-block`, `captioned-media`, `photo-actions-bar`

### When to use

- Shared snapshots, community or team feeds.

### How to use

- `<article class="orca-photo-post">` with `.orca-photo-post__head` (person block + relative time), the photo in a 4:3 frame with alt text, `.orca-photo-post__foot` (photo-actions bar + `.orca-photo-post__caption`).

#### Example: Post

```django
<article class="orca-photo-post">
  <div class="orca-photo-post__head">
    <div class="orca-person">
      <span class="orca-avatar orca-avatar--s" aria-hidden="true">GH</span>
      <span class="orca-person__text">
        <span class="orca-person__name">Grace Hopper</span>
        <time class="orca-person__role" datetime="2026-11-06T08:30">2 hours ago</time>
      </span>
    </div>
  </div>
  <div class="orca-ratio orca-ratio--4x3">
    <img src="{% static "orca/img/sample-street.svg" %}" alt="Still from the new warehouse gate video">
  </div>
  <div class="orca-photo-post__foot">
    <div class="orca-photo-actions">
      <button class="orca-icon-button" type="button" aria-pressed="false" aria-label="Like" data-orca-toggle>
        {% icon "star" %}
      </button>
      <span class="orca-photo-actions__count">8</span>
      <button class="orca-icon-button" type="button" aria-label="Comment">
        {% icon "chat" %}
      </button>
      <span class="orca-photo-actions__count">2</span>
    </div>
    <p class="orca-photo-post__caption"><strong>Grace Hopper</strong> Gate 1 video is up. It goes live tomorrow.</p>
  </div>
</article>
```

**Classes:** `.orca-photo-post`, `.orca-photo-post__head`, `.orca-photo-post__foot`, `.orca-photo-post__caption`

**Principles applied:** Jakob's law: work the way products people already know work

**ORCA guide items covered:** Photo post (user info + photo + actions + caption)

---

## Image gallery

`id: image-gallery` · level: pattern · source: ORCA

A large stage image with a row of thumbnails and a count; thumbnails swap the stage.

Built from: `captioned-media`, `thumbnail-strip`

### When to use

- Several snapshots of one event; product photos; before/after views.

### How to use

- `<div class="orca-gallery" data-orca-gallery>` with a frame holding `<img data-orca-gallery-stage>`, a count (`data-orca-gallery-count`, polite), and `<ul class="orca-gallery__thumbs">` of `<button class="orca-gallery__thumb" data-orca-gallery-src=… data-orca-gallery-alt=…>`.
- The current thumb has `aria-current="true"`; each thumb's button is named after its image.

#### Example: Gallery

```django
<div class="orca-gallery" data-orca-gallery style="max-width: 28rem">
  <div class="orca-ratio orca-ratio--4x3">
    <img src="{% static "orca/img/sample-street.svg" %}" alt="08:14, two people at the door" data-orca-gallery-stage>
  </div>
  <p class="orca-small orca-muted" data-orca-gallery-count aria-live="polite">1 of 2</p>
  <ul class="orca-gallery__thumbs">
    <li>
      <button class="orca-gallery__thumb" type="button" aria-current="true" aria-label="Image 1, 08:14" data-orca-gallery-src="{% static "orca/img/sample-street.svg" %}" data-orca-gallery-alt="08:14, two people at the door">
        <img src="{% static "orca/img/sample-street.svg" %}" alt="">
      </button>
    </li>
    <li>
      <button class="orca-gallery__thumb" type="button" aria-label="Image 2, floor plan" data-orca-gallery-src="{% static "orca/img/sample-floor.svg" %}" data-orca-gallery-alt="Floor plan with the door marked">
        <img src="{% static "orca/img/sample-floor.svg" %}" alt="">
      </button>
    </li>
  </ul>
</div>
```

**Classes:** `.orca-gallery`, `.orca-gallery__thumbs`, `.orca-gallery__thumb`

**Principles applied:** Practical UI S06: Make essential content visible or discoverable; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Image gallery (stage, thumbnails, dots)

---
