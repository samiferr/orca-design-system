# Imagery

Images, frames and graphics. Reserve their space, describe them, and keep text readable over them.

## Image

`id: image` · level: primitive · source: Tangerine

A record's main content image, plain or bordered.

### General description

A picture that carries content, such as a product photo or plan. It needs a text description and reserved space so the page does not shift as it loads.

#### Use cases

- Showing a product, place or person.
- Illustrating a record's main details.
- Showing a plan, diagram or screenshot.

#### When not to use it

- Decoration with no meaning: use a background or leave it out.
- Text content: use real text, not text inside an image.

#### Best practices

- Write alt text that describes what matters, or leave it empty if decorative.
- Set width and height so the layout does not jump.
- Load below-the-fold images lazily.
- Use modern, compressed formats and sensible sizes.

### When to use

- The primary image of a record (product, floor plan, cover image).

### How to use

- `<img class="orca-img" src=… alt=… width=… height=… loading="lazy">`. Always set width and height, or use an `orca-ratio` frame.
- `.orca-img--bordered` when the image edge could blend into the page (white photos, screenshots).
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

### General description

A small cropped preview of an image, used to recognise an item quickly in lists, tables and pickers.

#### Use cases

- Previewing items in lists and tables.
- Choosing between images or files.
- Showing a record's picture in a card.

#### When not to use it

- Viewing details of the image: link to a larger version.
- Images with essential small text: show a bigger one.

#### Best practices

- Use one size and crop consistently.
- Leave alt text empty when the name sits beside it.
- Reserve the space to avoid shifts while loading.
- Make clickable thumbnails large enough to tap.

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

### General description

A large, wide image at the top of a page that sets its mood or subject. It is common on marketing and landing pages.

#### Use cases

- Opening a landing or campaign page.
- Introducing a product, event or story.
- Giving a section a strong visual start.

#### When not to use it

- Task screens and dashboards: it pushes the task down the page.
- Conveying information: use text or a chart.

#### Best practices

- Choose an image that supports the message.
- Make sure text over it stays readable.
- Serve sizes that fit each screen.
- Describe it in alt text if it carries meaning.

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

A fixed-ratio box that holds an image, video, map or chart and reserves its space.

### General description

A box that holds a fixed shape, such as 16:9 or square, for an image, video, map or chart. It reserves space before the content loads.

#### Use cases

- Showing images in galleries and cards.
- Embedding video, maps or charts.
- Keeping a grid of mixed media neat.

#### When not to use it

- Content that must show in full: use a frame that fits without cropping.
- Content with its own size: no frame needed.

#### Best practices

- Pick one ratio per group of items.
- Decide whether to crop or fit the content.
- Set the frame size before the media loads.
- Always give the media a text alternative.

### When to use

- Media whose size is not set in the HTML; galleries and cards with images or video stills.

### How to use

- `<div class="orca-ratio orca-ratio--16x9"><img src=… alt=…></div>`. Ratios: 1x1, 4x3, 3x2, 16x9, 21x9, 3x4, or `style="--orca-ratio: 5 / 4"`.
- Media fills and crops by default; `.orca-ratio--contain` letterboxes instead (floor plans, documents).

#### Example: 4:3 frame

```django
<div class="orca-ratio orca-ratio--4x3" style="max-width: 16rem">
  <img src="{% static "orca/img/sample-street.svg" %}" alt="City street at night">
</div>
```

**Classes:** `.orca-ratio`, `.orca-ratio--16x9`, `.orca-ratio--contain`

**Tokens:** `--orca-bg-alt`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Fitts's law: big, close, well-spaced targets are faster and safer

**Related:** `aspect-ratio`, `snapshot-image`

**ORCA guide items covered:** Aspect-ratio frame

---

## Snapshot image

`id: snapshot-image` · level: primitive · source: ORCA

A video still in a 16:9 frame, with its source and capture time on a solid caption bar.

### General description

A still picture taken from a video or camera, shown with where it came from and when it was captured.

#### Use cases

- Showing key moments from a video.
- Galleries of captured images.
- Evidence or audit images that need a time.

#### When not to use it

- Live or moving content: use a video frame.
- Decorative pictures: use a plain image.

#### Best practices

- Show the source and time on a solid background so text stays readable.
- Put the time in the alt text too.
- Show a clear message when an image has expired or been removed.
- Keep a consistent shape across a gallery.

### When to use

- Video stills and galleries that show when each image was taken.

### How to use

- `<figure class="orca-ratio orca-ratio--16x9"><img …><figcaption class="orca-frame__caption"><span>Harbour timelapse</span><time datetime=…>08:14:03</time></figcaption></figure>`.
- Removed or expired image: replace the img with `<div class="orca-ratio orca-ratio--16x9 orca-frame--removed">Image removed after 30 days</div>`.

### Accessibility

- Alt text says what was captured and when; the visible caption repeats it.

#### Example: Snapshot and removed snapshot

```django
<div class="orca-row orca-row--16" style="align-items: flex-start">
  <figure class="orca-ratio orca-ratio--16x9" style="max-width: 18rem; margin: 0">
    <img src="{% static "orca/img/sample-street.svg" %}" alt="Still from the harbour timelapse at 08:14: boats leaving the quay">
    <figcaption class="orca-frame__caption">
      <span>Harbour timelapse</span>
      <time datetime="2026-11-06T08:14:03">08:14:03</time>
    </figcaption>
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

A video or stream frame marked recording or live with a red outline and a worded flag.

### General description

A video or stream frame that clearly shows it is being recorded or is live. It uses an outline and a word label so the state is hard to miss.

#### Use cases

- Live camera feeds.
- Screen or meeting recordings in progress.
- Streams that are being stored.

#### When not to use it

- Recorded clips that are not live: use a normal video frame.
- General status of a thing: use a status indicator.

#### Best practices

- Use a word such as 'Recording' or 'Live', not only colour.
- Keep any motion subtle and respect reduced-motion settings.
- Place the label where people will see it.
- Remove the marker as soon as recording stops.

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

### General description

A video player with standard controls inside a fixed-shape box. It plays recorded clips on the page.

#### Use cases

- Tutorials and product demos.
- Recorded meetings or clips.
- Short explainers within an article.

#### When not to use it

- Short looping graphics: use an animated image or an animation.
- Live streams: use a live frame.

#### Best practices

- Add captions for speech.
- Never start playing with sound automatically.
- Set a poster image and reserve the space.
- Keep the browser's own controls so they work with a keyboard.

### When to use

- Recorded clips, tutorials.

### How to use

- `<div class="orca-ratio orca-ratio--16x9"><video class="orca-video" controls preload="metadata" poster=…><source …><track kind="captions" …></video></div>`.
- Never autoplay with sound.

### Accessibility

- Provide captions for speech; describe essential visual content.

#### Example: Video

```django
<div class="orca-ratio orca-ratio--16x9" style="max-width: 20rem">
  <video class="orca-video" controls preload="none" poster="{% static "orca/img/sample-street.svg" %}" aria-label="Clip from the harbour timelapse, 08:14"></video>
</div>
```

**Classes:** `.orca-video`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI; Doherty threshold: respond within 400 ms; show progress for anything slower

**ORCA guide items covered:** Video frame

---

## Illustration (empty, search, error)

`id: illustration` · level: primitive · source: Tangerine

Simple token-coloured line illustrations for empty, no-result and error states.

### General description

A simple drawing used to add friendliness to a page, usually for an empty, no-results or error state.

#### Use cases

- Empty lists and first-use screens.
- No search results.
- Error and not-found pages.

#### When not to use it

- Decorating pages that already have content.
- Explaining steps in detail: use text or a diagram.

#### Best practices

- Pair it with a clear title and a next action.
- Keep it simple and consistent in style.
- Treat it as decoration with no alt text.
- Make sure it works in light and dark themes.

### When to use

- Empty states and no-result states; error pages.

### When not to use

- Decorating normal content.

### How to use

- `{% orca_illustration "empty" %}`, `"search"` or `"error"`. They are decorative (`aria-hidden`); the title and text carry the meaning.

#### Example: Illustrations

```django
<div class="orca-row orca-row--16">
  {% orca_illustration "empty" %}
  {% orca_illustration "search" %}
  {% orca_illustration "error" %}
</div>
```

**Classes:** `.orca-illustration`

**Tokens:** `--orca-brand`, `--orca-accent`, `--orca-border-strong`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Aesthetic–usability effect: consistent, careful visuals earn trust

**Related:** `empty-title`

**ORCA guide items covered:** Illustration (empty, search)

---

## QR code

`id: qr-code` · level: primitive · source: ORCA

A frame for a server-generated QR code: white quiet zone, black modules, encoded text below.

### General description

A square barcode that a phone camera can scan to open a link or read a code. It is shown with the same text written out.

#### Use cases

- Pairing a phone or device.
- Linking to a web page from a printed item.
- Setting up two-factor sign-in.

#### When not to use it

- Links people can simply click: use a normal link.
- Long text: use a short link, because dense codes scan poorly.

#### Best practices

- Keep dark modules on a light background with a quiet border.
- Print the text or link below as a fallback.
- Make it large enough to scan.
- Test it with a real phone.

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
<figure class="orca-code-frame" style="margin: 0">
  <img src="{% static "orca/img/sample-qr.svg" %}" alt="QR code for the setup link">
  <figcaption class="orca-code-frame__text">ORCA-7Q2K</figcaption>
</figure>
```

**Classes:** `.orca-code-frame`, `.orca-code-frame__text`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** QR code

---

## Barcode

`id: barcode` · level: primitive · source: ORCA

A frame for a server-generated 1D barcode with its human-readable digits below.

### General description

A row of lines that a scanner reads to identify an item, with its number printed underneath.

#### Use cases

- Labelling assets or inventory.
- Printing tickets and passes.
- Looking up items at a counter or warehouse.

#### When not to use it

- Phone scanning from a screen: a QR code is easier to read.
- Showing a number only: use plain text.

#### Best practices

- Keep dark bars on a plain light background.
- Print the digits below for people.
- Leave empty space at both ends.
- Test with a real scanner at the printed size.

### When to use

- Asset labels, tickets, inventory.

### How to use

- Generate the SVG on the server (for example `python-barcode`).
- `<figure class="orca-code-frame orca-code-frame--barcode">{{ svg|safe }}<figcaption class="orca-code-frame__text">4006381333931</figcaption></figure>`.

#### Example: Barcode frame (placeholder)

```django
<figure class="orca-code-frame orca-code-frame--barcode" style="margin: 0">
  <img src="{% static "orca/img/sample-barcode.svg" %}" alt="Barcode 4006381333931">
  <figcaption class="orca-code-frame__text">4006381333931</figcaption>
</figure>
```

**Classes:** `.orca-code-frame--barcode`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Barcode

---
