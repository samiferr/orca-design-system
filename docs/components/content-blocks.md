# Content blocks

Reusable blocks for products, people, posts, heroes and media.

## Product item

`id: product-item` · level: component · source: ORCA

A product tile: square image, name, price and one action.

Built from: `image`, `button`

### Why

Image, name and price grouped by proximity let people compare products at a glance (Miller's law, Practical UI L01); one action keeps the decision simple (Hick's law).

### When to use

- Product grids and lists in shops and catalogues.

### How to use

- `<article class="orca-product">` with `.orca-product__image` (square, reserved), `.orca-product__name` (link to the product), `.orca-product__price` (old price in `<s>` with a hidden 'was') and an action.
- Long names wrap; never truncate a product name.

#### Example: Product

```django
<article class="orca-product" style="max-width: 14rem">
  <div class="orca-product__image"><img src="{% static "orca/img/sample-street.svg" %}" alt=""></div>
  <h3 class="orca-product__name"><a href="#">Dome video, 4 MP, outdoor</a></h3>
  <p class="orca-product__price" style="margin: 0">€189<s><span class="orca-sr-only">was </span>€229</s></p>
  <button class="orca-button orca-button--dense" type="button">Add to quote</button>
</article>
```

**Classes:** `.orca-product`, `.orca-product__image`, `.orca-product__name`, `.orca-product__price`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI L01: Group related information; Hick's law: fewer, clearer choices mean faster decisions; Practical UI L15: Design for long and unusual content

**ORCA guide items covered:** Product item

---

## Person block

`id: person-block` · level: component · source: ORCA

Avatar, name and role, optionally with a contact action.

Built from: `avatar`

### Why

Faces and roles help people recognise who someone is before reading the name (Miller's law: recognition).

### When to use

- Owners, assignees, contacts, authors.

### How to use

- `<div class="orca-person">` with an avatar and `.orca-person__text` (`__name`, `__role`); add a link or icon button for contact.
- Use the person's preferred name; never shorten it in a way they did not choose.

#### Example: Person

```django
<div class="orca-person"><span class="orca-avatar" aria-hidden="true">AL</span><span class="orca-person__text"><span class="orca-person__name">Ada Lovelace</span><span class="orca-person__role">Site manager, North building</span></span><a class="orca-icon-button" href="#" aria-label="Email Ada Lovelace">{% icon "mail" %}</a></div>
```

**Classes:** `.orca-person`, `.orca-person__text`, `.orca-person__name`, `.orca-person__role`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Person block

---

## Block post

`id: post-block` · level: component · source: ORCA

An article teaser: kicker, headline, excerpt, meta and a thumbnail.

Built from: `card-kicker`, `card-meta`, `thumbnail`

### Why

Leading with an informative headline and a short excerpt lets people decide whether to read (Practical UI W04, W05).

### When to use

- News, release notes, help articles, blog lists.

### How to use

- `<article class="orca-post">` with text (kicker, `.orca-post__title` link, `.orca-post__excerpt` clamped to 3 lines, meta) and `.orca-post__thumb` image.
- On narrow screens the image moves above the text.

#### Example: Post

```django
<article class="orca-post" style="max-width: 36rem"><div>
  <p class="orca-card-kicker">Release notes</p><h3 class="orca-post__title"><a href="#">Counting now ignores staff areas</a></h3>
  <p class="orca-post__excerpt">Mark a zone as excluded and people inside it are no longer counted. Existing zones keep their behaviour until you change them.</p>
  <p class="orca-card-meta">6 November 2026 · 2 min read</p></div>
  <img class="orca-post__thumb" src="{% static "orca/img/sample-floor.svg" %}" alt=""></article>
```

**Classes:** `.orca-post`, `.orca-post__title`, `.orca-post__excerpt`, `.orca-post__thumb`

**Principles applied:** Practical UI W04: Lead with the information people seek; Practical UI W05: Order explanations as an inverted pyramid; Practical UI W14: Give links meaningful destination names

**ORCA guide items covered:** Block post (thumbnail + headline + excerpt)

---

## Hero

`id: hero` · level: component · source: ORCA

The opening block of a marketing or landing page: kicker, headline, lead, actions and an image.

Built from: `heading`, `button`, `hero-image`

### Why

The first screen must state what the product does and offer one clear next step (Von Restorff, Peak–end rule).

### When to use

- Marketing, landing and onboarding pages.

### When not to use

- Application screens.

### How to use

- `<section class="orca-hero">` with `.orca-hero__text` (kicker, `h1.orca-hero__title`, `.orca-hero__lead`, actions) and `.orca-hero__media`.
- One primary action, one secondary. The headline states the benefit in under 10 words.

#### Example: Hero

```django
<section class="orca-hero">
  <div class="orca-hero__text"><p class="orca-card-kicker">People counting</p><h1 class="orca-hero__title">Know how busy every door is, right now.</h1><p class="orca-hero__lead">Publish the videos you already have.</p>
    <div class="orca-row"><a class="orca-button orca-button--brand" href="#">Start free trial</a><a class="orca-button" href="#">See a demo</a></div></div>
  <div class="orca-hero__media"><img src="{% static "orca/img/sample-street.svg" %}" alt="A shop entrance seen from above"></div>
</section>
```

**Classes:** `.orca-hero`, `.orca-hero__text`, `.orca-hero__title`, `.orca-hero__lead`, `.orca-hero__media`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Peak–end rule: people judge an experience by its peak and its end; Practical UI B03: One primary action

**ORCA guide items covered:** Hero

---

## Photo-actions bar

`id: photo-actions-bar` · level: component · source: ORCA

The row under a photo: like, comment and share with counts, and save at the end.

Built from: `icon-button`, `toggle-button`

### Why

A familiar row of icon actions under media (Jakob's law) with counts and pressed states shows people's own reaction clearly.

### When to use

- Photo posts, galleries, shared snapshots.

### How to use

- `<div class="orca-photo-actions">` of icon buttons with `aria-label` and `aria-pressed` for toggles, each followed by `.orca-photo-actions__count`; save goes in `.orca-photo-actions__end`.

#### Example: Actions

```django
<div class="orca-photo-actions" style="max-width: 24rem">
  <button class="orca-icon-button" type="button" aria-pressed="true" aria-label="Like" data-orca-toggle>{% icon "star" %}</button><span class="orca-photo-actions__count">24</span>
  <button class="orca-icon-button" type="button" aria-label="Comment">{% icon "chat" %}</button><span class="orca-photo-actions__count">3</span>
  <button class="orca-icon-button" type="button" aria-label="Share">{% icon "share" %}</button>
  <button class="orca-icon-button orca-photo-actions__end" type="button" aria-pressed="false" aria-label="Save" data-orca-toggle>{% icon "pin" %}</button>
</div>
```

**Classes:** `.orca-photo-actions`, `.orca-photo-actions__count`, `.orca-photo-actions__end`

**Principles applied:** Jakob's law: work the way products people already know work; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Photo-actions bar

---

## Video card

`id: video-card` · level: component · source: Tangerine

A video's latest snapshot with its status, name, place and actions.

Built from: `linked-card`, `snapshot-image`, `status-light`, `pin-button`

### Why

Operators recognise a video by its view first (Miller's law); a status flag on the image and a status word below make offline videos impossible to miss (Von Restorff, C03).

### When to use

- Video grids on dashboards and video lists.

### How to use

- A linked card with `.orca-video-card`: `.orca-ratio--16x9` snapshot (or a removed frame when offline), a badge in `.orca-video-card__flag`, body with title link and status light, footer with pin and more actions.
- Show the snapshot time; a stale image is labelled as such.

#### Example: Video cards

```django
<ul class="orca-card-grid">
  <li><article class="orca-card orca-card--link orca-video-card"><div class="orca-ratio orca-ratio--16x9"><img src="{% static "orca/img/sample-street.svg" %}" alt=""><span class="orca-frame__caption"><span>Snapshot</span><time datetime="2026-11-06T09:14">09:14</time></span></div>
    <div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">Entrance A</a></h3><span class="orca-status orca-small"><span class="orca-dot orca-dot--positive"></span>Online · North building</span></div>
    <div class="orca-card__footer"><span class="orca-small orca-muted orca-num">1,204 today</span><span class="orca-card__footer-end"><button class="orca-icon-button orca-icon-button--sm orca-pin" type="button" aria-pressed="true" aria-label="Unpin Entrance A" data-orca-toggle data-orca-label-on="Unpin Entrance A" data-orca-label-off="Pin Entrance A">{% icon "pin" %}</button></span></div></article></li>
  <li><article class="orca-card orca-card--link orca-video-card"><div class="orca-ratio orca-ratio--16x9 orca-frame--removed">No image since 08:14</div><span class="orca-badge orca-badge--negative orca-video-card__flag">Offline</span>
    <div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">Loading dock</a></h3><span class="orca-status orca-small"><span class="orca-dot orca-dot--negative"></span>Offline since 08:14</span></div>
    <div class="orca-card__footer"><span class="orca-small orca-muted">Last count 08:14</span><span class="orca-card__footer-end"><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="More actions for Loading dock">{% icon "more" %}</button></span></div></article></li>
</ul>
```

**Classes:** `.orca-video-card`, `.orca-video-card__flag`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Video card

---

## Page heading

`id: page-heading` · level: component · source: ORCA

The page title, the one-sentence subtitle and an optional meta line with status badges.

Built from: `page-title`, `page-subtitle`, `small-text`, `badge`

### Why

People confirm where they are from the title first and what the page is for from the subtitle (Jakob's law, Practical UI W04); keeping the three together keeps their spacing and order the same on every page.

### When to use

- Inside the page head of application pages and documentation pages.

### How to use

- `<div class="orca-page-head__text">` with `h1.orca-page-title`, `p.orca-page-subtitle` and `p.orca-page-head__meta` (facts in small text, status as badges with a word).

### Accessibility

- The title is the page's only `<h1>`.

#### Example: Page heading

```django
<div class="orca-page-head__text">
  <h1 class="orca-page-title">Videos</h1>
  <p class="orca-page-subtitle">Every video from North building.</p>
  <p class="orca-page-head__meta"><span class="orca-badge orca-badge--subtle orca-badge--positive">{% icon "success" %}Published</span><span>Updated 2 minutes ago</span></p>
</div>
```

**Classes:** `.orca-page-head__text`, `.orca-page-head__meta`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI W04: Lead with the information people seek; Practical UI L03: Establish an order of importance

**Related:** `page-head`, `docs-page-header`

---

## Section heading

`id: section-heading` · level: component · source: ORCA

A section title with an optional one-paragraph introduction.

Built from: `section-title`, `paragraph`

### Why

A title and one sentence of why let people decide whether a section concerns them before reading it (Practical UI W05: inverted pyramid, L01: grouping).

### When to use

- Form sections, settings groups, documentation sections.

### How to use

- `<h2 class="orca-section-title">` then `<p class="orca-p">` of one or two sentences.
- Keep heading levels in order on the page.

#### Example: Section heading

```django
<h2 class="orca-section-title">Thumbnails</h2>
<p class="orca-p orca-muted">How often thumbnails are taken and how long videos are kept.</p>
```

**Classes:** `.orca-section-title`

**Principles applied:** Practical UI W05: Order explanations as an inverted pyramid; Practical UI L01: Group related information

**Related:** `form-section`

---

## Feature item

`id: feature-item` · level: component · source: ORCA

One feature: an icon, a short title and one sentence.

Built from: `icon`, `heading`, `paragraph`

### Why

An icon and a title are recognised before the sentence is read (Miller's law); one sentence per feature keeps the list scannable (Practical UI W01).

### When to use

- Feature grids on marketing pages; 'What you can do' lists on empty dashboards.

### How to use

- `<li class="orca-feature">{% icon "statistics" size="l" %}<h3 class="orca-feature__title">…</h3><p class="orca-feature__text">…</p></li>`.
- The title says the benefit in two to four words.

### Accessibility

- The icon is decorative; the title carries the meaning.

#### Example: Feature item

```django
<ul style="list-style: none; margin: 0; padding: 0; max-width: 18rem"><li class="orca-feature">{% icon "notifications" size="l" %}<h3 class="orca-feature__title">Upload alerts</h3><p class="orca-feature__text">Get an email when a video fails to process.</p></li></ul>
```

**Classes:** `.orca-feature`, `.orca-feature__title`, `.orca-feature__text`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI W01: Make every word useful

**Related:** `feature-grid`

---

## Captioned media

`id: captioned-media` · level: component · source: ORCA

An image or video in its aspect-ratio frame, with a caption or a flag over a solid bar.

Built from: `media-frame`, `snapshot-image`

### Why

The frame reserves the space so nothing jumps while the media loads (Doherty threshold); a caption on a solid bar stays readable over any picture (Practical UI T12).

### When to use

- Photo posts, gallery stages, story images, editors that draw over an image.

### How to use

- `<figure class="orca-ratio orca-ratio--16x9"><img …><figcaption class="orca-frame__caption">…</figcaption></figure>`.
- Without a caption, the frame alone: `<div class="orca-ratio orca-ratio--4x3"><img …></div>`.

### Accessibility

- Alt text says what matters in the image; the caption repeats source and time visibly.

#### Example: Captioned image

```django
<figure class="orca-ratio orca-ratio--16x9" style="max-width: 20rem; margin: 0">
  <img src="{% static "orca/img/sample-street.svg" %}" alt="City street at night">
  <figcaption class="orca-frame__caption"><span>Harbour timelapse</span><time datetime="2026-11-06T08:14:03">08:14:03</time></figcaption>
</figure>
```

**Classes:** `.orca-ratio`, `.orca-frame__caption`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI T12: Make text over photos readable

**Related:** `photo-post`, `image-gallery`, `story-feature`

---

## Thumbnail strip

`id: thumbnail-strip` · level: component · source: ORCA

A row of thumbnail buttons that choose the image shown, the current one marked.

Built from: `thumbnail`

### Why

Thumbnails show what is there and let people jump straight to an image (Miller's law: recognition over recall); the current one changes shape, not only colour (C03).

### When to use

- Image galleries and media pickers with up to about twenty items.

### How to use

- `<ul class="orca-gallery__thumbs"><li><button class="orca-gallery__thumb" type="button" aria-current="true" aria-label="Image 1, 08:14"><img src=… alt=""></button></li>…</ul>`.

### Accessibility

- Each button is named after the image it shows; `aria-current` marks the one on stage.

#### Example: Thumbnails

```django
<ul class="orca-gallery__thumbs"><li><button class="orca-gallery__thumb" type="button" aria-current="true" aria-label="Image 1, street"><img src="{% static "orca/img/sample-street.svg" %}" alt=""></button></li><li><button class="orca-gallery__thumb" type="button" aria-label="Image 2, floor plan"><img src="{% static "orca/img/sample-floor.svg" %}" alt=""></button></li></ul>
```

**Classes:** `.orca-gallery__thumbs`, `.orca-gallery__thumb`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI C03: Communicate meaning beyond colour

**Related:** `image-gallery`

---

## Video player

`id: video-player` · level: component · source: ORCA

A native video in its frame, with a live or recording flag and the current time.

Built from: `video-frame`, `recording-frame`, `time-label`

### Why

Native controls are familiar and keyboard accessible (Jakob's law, Postel's law); a worded flag makes 'live' or 'recording' impossible to miss (Von Restorff, C03).

### When to use

- Recorded clips, live streams, tutorials.

### How to use

- `<div class="orca-ratio orca-ratio--16x9"><video class="orca-video" controls preload="metadata" poster=…></video></div>`.
- Live or recording: add `.orca-frame--recording` and `<span class="orca-frame__flag">` with a pulsing dot and the word.
- Never autoplay with sound.

### Accessibility

- Provide captions for speech; name the video with `aria-label` when no visible title is next to it.

#### Example: Live video

```django
<div class="orca-ratio orca-ratio--16x9 orca-frame--recording" style="max-width: 20rem">
  <video class="orca-video" controls preload="none" poster="{% static "orca/img/sample-street.svg" %}" aria-label="Harbour, live"></video>
  <span class="orca-frame__flag"><span class="orca-dot orca-dot--sm orca-dot--pulse"></span>Live · <time datetime="2026-11-06T08:14">08:14</time></span>
</div>
```

**Classes:** `.orca-video`, `.orca-frame--recording`, `.orca-frame__flag`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI C03: Communicate meaning beyond colour

**Related:** `recording-player`, `live-stream-panel`

---

## Call to action

`id: call-to-action` · level: component · source: ORCA

The one or two actions a section asks for: the primary button and an optional quieter alternative.

Built from: `button`, `text-link`

### Why

One clear primary action per section (Practical UI B03, Hick's law) with the alternative visibly quieter (B05).

### When to use

- Site headers, heroes, email frames, empty pages.

### When not to use

- Three or more actions: keep one, move the rest to a menu or a link.

### How to use

- `<div class="orca-site-header__actions"><a class="orca-button orca-button--ghost" href=…>Sign in</a><a class="orca-button orca-button--brand" href=…>Start free trial</a></div>`.
- In emails the button is a table-based link with the address written below it.

#### Example: Call to action

```django
<div class="orca-site-header__actions"><a class="orca-button orca-button--ghost" href="#">Sign in</a><a class="orca-button orca-button--brand" href="#">Start free trial</a></div>
```

**Classes:** `.orca-site-header__actions`

**Principles applied:** Practical UI B03: One primary action; Practical UI B05: Keep low-priority actions quieter; Hick's law: fewer, clearer choices mean faster decisions

**Related:** `site-header`, `email-frame`, `hero`

---

## Fine print

`id: fine-print` · level: component · source: ORCA

Small legal and version text on one line, with its policy links.

Built from: `small-text`, `text-link`

### Why

Legal text must be there but must not compete (Practical UI S02); small, muted and on one line it stays findable without taking attention (T13: quieter text stays legible).

### When to use

- Footers, email footers, sign-in pages.

### How to use

- `<p class="orca-footer__legal">© 2026 Acme · <a href=…>Privacy</a> · <a href=…>Terms</a> · Version 0.4.0</p>`.

#### Example: Fine print

```django
<p class="orca-footer__legal">© 2026 Acme · <a href="#">Privacy</a> · <a href="#">Terms</a> · Version 0.4.0</p>
```

**Classes:** `.orca-footer__legal`

**Principles applied:** Practical UI S02: Remove styles that compete without communicating; Practical UI T13: Keep quieter text legible

**Related:** `footer`, `email-frame`

---
