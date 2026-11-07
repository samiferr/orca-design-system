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
  <h3 class="orca-product__name"><a href="#">Dome camera, 4 MP, outdoor</a></h3>
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
  <div class="orca-hero__text"><p class="orca-card-kicker">People counting</p><h1 class="orca-hero__title">Know how busy every door is, right now.</h1><p class="orca-hero__lead">Count visitors with the cameras you already have.</p>
    <div class="orca-row"><a class="orca-button orca-button--brand" href="#">Start free trial</a><a class="orca-button" href="#">See a demo</a></div></div>
  <div class="orca-hero__media"><img src="{% static "orca/img/sample-street.svg" %}" alt="A shop entrance seen from a ceiling camera"></div>
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

## Camera card

`id: camera-card` · level: component · source: Tangerine

A camera's latest snapshot with its status, name, place and actions.

Built from: `linked-card`, `snapshot-image`, `status-light`, `pin-button`

### Why

Operators recognise a camera by its view first (Miller's law); a status flag on the image and a status word below make offline cameras impossible to miss (Von Restorff, C03).

### When to use

- Camera grids on dashboards and camera lists.

### How to use

- A linked card with `.orca-camera-card`: `.orca-ratio--16x9` snapshot (or a removed frame when offline), a badge in `.orca-camera-card__flag`, body with title link and status light, footer with pin and more actions.
- Show the snapshot time; a stale image is labelled as such.

#### Example: Camera cards

```django
<ul class="orca-card-grid">
  <li><article class="orca-card orca-card--link orca-camera-card"><div class="orca-ratio orca-ratio--16x9"><img src="{% static "orca/img/sample-street.svg" %}" alt=""><span class="orca-frame__caption"><span>Snapshot</span><time datetime="2026-11-06T09:14">09:14</time></span></div>
    <div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">Entrance A</a></h3><span class="orca-status orca-small"><span class="orca-dot orca-dot--positive"></span>Online · North building</span></div>
    <div class="orca-card__footer"><span class="orca-small orca-muted orca-num">1,204 today</span><span class="orca-card__footer-end"><button class="orca-icon-button orca-icon-button--sm orca-pin" type="button" aria-pressed="true" aria-label="Unpin Entrance A" data-orca-toggle data-orca-label-on="Unpin Entrance A" data-orca-label-off="Pin Entrance A">{% icon "pin" %}</button></span></div></article></li>
  <li><article class="orca-card orca-card--link orca-camera-card"><div class="orca-ratio orca-ratio--16x9 orca-frame--removed">No image since 08:14</div><span class="orca-badge orca-badge--negative orca-camera-card__flag">Offline</span>
    <div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">Loading dock</a></h3><span class="orca-status orca-small"><span class="orca-dot orca-dot--negative"></span>Offline since 08:14</span></div>
    <div class="orca-card__footer"><span class="orca-small orca-muted">Last count 08:14</span><span class="orca-card__footer-end"><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="More actions for Loading dock">{% icon "more" %}</button></span></div></article></li>
</ul>
```

**Classes:** `.orca-camera-card`, `.orca-camera-card__flag`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Camera card

---
