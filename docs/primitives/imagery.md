# Imagery

Images, frames and graphics. Reserve their space, describe them, and keep text readable over them.

## Image

`id: image` · level: primitive · source: Tangerine

A content image (the primary image of a record), plain or bordered.

### Why

Images are recognised faster than text but must not jump the layout when they load (Doherty threshold: perceived performance) and must be described for people who cannot see them (Postel's law).

### When to use

- The primary image of a record (product, floor plan, cover image).

### How to use

- `<img class="orca-img" src=… alt=… width=… height=… loading="lazy">`. Always set width and height or put it in an `orca-ratio` frame.
- `.orca-img--bordered` when the image's edge could merge with the page (white photos, screenshots).
- `alt` describes what matters in the image for the task; decorative images get `alt=""`.

### Accessibility

- Never put text people must read inside the image.

#### Example: Bordered image

```django
<img class="orca-img orca-img--bordered" src="{% static "orca/img/sample-floor.svg" %}" alt="Floor plan of the north building with two entrances" width="320" height="200" loading="lazy">
```

**Classes:** `.orca-img`, `.orca-img--bordered`, `.orca-img--cover`

**Tokens:** `--orca-bg-alt`, `--orca-border`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Postel's law: accept varied input, output reliable and accessible UI

**Related:** `media-frame`, `thumbnail`

**ORCA guide items covered:** Primary image; Image (bordered)

---

## Thumbnail image

`id: thumbnail` · level: primitive · source: Tangerine

A small square preview (48 or 96px) cropped to fill.

### Why

A consistent small preview lets people spot the right record in a list by sight (Miller's law: recognition).

### When to use

- List rows, table cells, cards, pickers.

### How to use

- `<img class="orca-thumb" src=… alt="" width="48" height="48" loading="lazy">`; `.orca-thumb--lg` for 96px.
- Use `alt=""` when the record's name is next to it.

#### Example: Thumbnails

```django
<div class="orca-row orca-row--16">
  <img class="orca-thumb" src="{% static "orca/img/sample-street.svg" %}" alt="" width="48" height="48">
  <img class="orca-thumb orca-thumb--lg" src="{% static "orca/img/sample-street.svg" %}" alt="" width="96" height="96">
</div>
```

**Classes:** `.orca-thumb`, `.orca-thumb--lg`

**Tokens:** `--orca-thumb`, `--orca-thumb-lg`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Thumbnail image

---

## Hero image

`id: hero-image` · level: primitive · source: Tangerine

A wide image (21:9, 4:3 on phones) heading a marketing or landing page.

### Why

A single strong image sets the context of a landing page at a glance (Aesthetic–usability effect).

### When to use

- Marketing and landing pages only.

### When not to use

- Application screens: it pushes the task below the fold.
- Text over the image without a solid or gradient backing (Practical UI T12).

### How to use

- `<img class="orca-hero-img" src=… alt=…>`; serve responsive sizes with `srcset`.
- Compose with the subject off-centre (rule of thirds).

#### Example: Hero

```django
<img class="orca-hero-img" src="{% static "orca/img/sample-street.svg" %}" alt="Shoppers entering a city-centre store">
```

**Classes:** `.orca-hero-img`

**Tokens:** `--orca-bg-alt`

**Principles applied:** Aesthetic–usability effect: consistent, careful visuals earn trust; Practical UI T12: Make text over photos readable

**ORCA guide items covered:** Hero image

---

## Aspect-ratio frame

`id: media-frame` · level: primitive · source: Tangerine

A box with a fixed aspect ratio that holds an image, video, map or chart and reserves its space.

### Why

Reserved space prevents layout shift while media loads, so nothing moves under the pointer (Doherty threshold, Fitts's law).

### When to use

- Any media whose dimensions are not known in the HTML; image galleries and cards with images or video stills.

### How to use

- `<div class="orca-ratio orca-ratio--16x9"><img src=… alt=…></div>`. Ratios: 1x1, 4x3, 3x2, 16x9, 21x9, 3x4, or `style="--orca-ratio: 5 / 4"`.
- Media fills and crops by default; `.orca-ratio--contain` letterboxes instead (floor plans, documents).

#### Example: 4:3 frame

```django
<div class="orca-ratio orca-ratio--4x3" style="max-width: 16rem"><img src="{% static "orca/img/sample-street.svg" %}" alt="City street at night"></div>
```

**Classes:** `.orca-ratio`, `.orca-ratio--16x9`, `.orca-ratio--contain`

**Tokens:** `--orca-bg-alt`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Fitts's law: big, close, well-spaced targets are faster and safer

**Related:** `aspect-ratio`, `snapshot-image`

**ORCA guide items covered:** Aspect-ratio frame

---

## Snapshot image

`id: snapshot-image` · level: primitive · source: ORCA

A still image taken from a video, in a 16:9 frame with its source and capture time on a solid caption bar.

### Why

A snapshot is a record of a moment; where it comes from and when it was taken must always be visible and readable over any picture (Practical UI T12: solid backing).

### When to use

- Video stills, thumbnails of video moments, image galleries that show when each image was taken.

### How to use

- `<figure class="orca-ratio orca-ratio--16x9"><img …><figcaption class="orca-frame__caption"><span>Harbour timelapse</span><time datetime=…>08:14:03</time></figcaption></figure>`.
- Removed or expired image: replace the img with `<div class="orca-ratio orca-ratio--16x9 orca-frame--removed">Image removed after 30 days</div>`.

### Accessibility

- Alt text says what was captured and when; the caption repeats it visibly.

#### Example: Snapshot and removed snapshot

```django
<div class="orca-row orca-row--16" style="align-items: flex-start">
  <figure class="orca-ratio orca-ratio--16x9" style="max-width: 18rem; margin: 0">
    <img src="{% static "orca/img/sample-street.svg" %}" alt="Still from the harbour timelapse at 08:14: boats leaving the quay">
    <figcaption class="orca-frame__caption"><span>Harbour timelapse</span><time datetime="2026-11-06T08:14:03">08:14:03</time></figcaption>
  </figure>
  <div class="orca-ratio orca-ratio--16x9 orca-frame--removed" style="max-width: 18rem">Image removed after 30 days</div>
</div>
```

**Classes:** `.orca-frame__caption`, `.orca-frame--removed`

**Principles applied:** Practical UI T12: Make text over photos readable; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Snapshot image

---

## Recording frame

`id: recording-frame` · level: primitive · source: ORCA

A video or stream frame marked as recording or live with a red outline and a worded flag.

### Why

Being recorded is a state people must not miss: red outline, pulsing dot and the word 'Recording' together (Von Restorff; C03: never colour alone).

### When to use

- Live streams and recordings in progress.

### How to use

- `<div class="orca-ratio orca-ratio--16x9 orca-frame--recording">…<span class="orca-frame__flag"><span class="orca-dot orca-dot--pulse"></span>Recording</span></div>`.
- Use 'Live' for a stream that is not being stored.

#### Example: Recording

```django
<div class="orca-ratio orca-ratio--16x9 orca-frame--recording" style="max-width: 20rem">
  <img src="{% static "orca/img/sample-street.svg" %}" alt="Live video of the harbour">
  <span class="orca-frame__flag"><span class="orca-dot orca-dot--sm orca-dot--pulse"></span>Recording</span>
</div>
```

**Classes:** `.orca-frame--recording`, `.orca-frame__flag`

**Tokens:** `--orca-negative`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Recording frame

---

## Video frame

`id: video-frame` · level: primitive · source: Tangerine

A native `<video>` with controls inside an aspect-ratio frame.

### Why

Native controls are familiar and keyboard accessible (Jakob's law, Postel's law); the frame reserves space (Doherty).

### When to use

- Recorded clips, tutorials.

### How to use

- `<div class="orca-ratio orca-ratio--16x9"><video class="orca-video" controls preload="metadata" poster=…><source …><track kind="captions" …></video></div>`.
- Never autoplay with sound.

### Accessibility

- Provide captions for speech; describe essential visual content.

#### Example: Video

```django
<div class="orca-ratio orca-ratio--16x9" style="max-width: 20rem"><video class="orca-video" controls preload="none" poster="{% static "orca/img/sample-street.svg" %}" aria-label="Clip from the harbour timelapse, 08:14"></video></div>
```

**Classes:** `.orca-video`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Video frame

---

## Illustration (empty, search, error)

`id: illustration` · level: primitive · source: Tangerine

Simple token-coloured line illustrations for empty, no-result and error states.

### Why

A calm illustration softens an empty or failed moment and signals that the state is expected (Peak–end rule), while staying in the system's colours in every theme.

### When to use

- Empty states and no-result states; error pages.

### When not to use

- Decorating normal content.

### How to use

- `{% orca_illustration "empty" %}`, `"search"` or `"error"`. They are decorative (`aria-hidden`); the title and text carry the meaning.

#### Example: Illustrations

```django
<div class="orca-row orca-row--16">{% orca_illustration "empty" %}{% orca_illustration "search" %}{% orca_illustration "error" %}</div>
```

**Classes:** `.orca-illustration`

**Tokens:** `--orca-brand`, `--orca-accent`, `--orca-border-strong`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Aesthetic–usability effect: consistent, careful visuals earn trust

**Related:** `empty-title`

**ORCA guide items covered:** Illustration (empty, search)

---

## QR code

`id: qr-code` · level: primitive · source: ORCA

A frame for a server-generated QR code: white quiet zone, black modules, and the encoded text below.

### Why

QR codes only scan with enough contrast and quiet zone, so the frame is always black on white whatever the theme; printing the text below gives a fallback (Postel's law).

### When to use

- Pairing a phone, sharing a link to a physical place, two-factor setup.

### How to use

- Generate the SVG on the server (for example with the `segno` package: `segno.make(url).svg_inline(scale=4)`).
- `<figure class="orca-code-frame">{{ qr_svg|safe }}<figcaption class="orca-code-frame__text">ABCD-1234</figcaption></figure>`.
- Keep at least 4 modules of white around the code; never recolour it.

### Accessibility

- Give the code a text alternative: the link or secret written out.

#### Example: QR frame (placeholder image)

```django
<figure class="orca-code-frame" style="margin: 0"><img src="{% static "orca/img/sample-qr.svg" %}" alt="QR code for the setup link"><figcaption class="orca-code-frame__text">ORCA-7Q2K</figcaption></figure>
```

**Classes:** `.orca-code-frame`, `.orca-code-frame__text`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** QR code

---

## Barcode

`id: barcode` · level: primitive · source: ORCA

A frame for a server-generated 1D barcode with its human-readable digits below.

### Why

Same rules as QR: fixed black on white for scanners, digits for people (Postel's law).

### When to use

- Asset labels, tickets, inventory.

### How to use

- Generate the SVG on the server (for example `python-barcode`).
- `<figure class="orca-code-frame orca-code-frame--barcode">{{ svg|safe }}<figcaption class="orca-code-frame__text">4006381333931</figcaption></figure>`.

#### Example: Barcode frame (placeholder)

```django
<figure class="orca-code-frame orca-code-frame--barcode" style="margin: 0"><img src="{% static "orca/img/sample-barcode.svg" %}" alt="Barcode 4006381333931"><figcaption class="orca-code-frame__text">4006381333931</figcaption></figure>
```

**Classes:** `.orca-code-frame--barcode`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Barcode

---
