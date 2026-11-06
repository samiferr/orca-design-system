from .registry import Element, add, category

C = category(
    "imagery", "Imagery",
    "Images, frames and graphics. Reserve their space, describe them, and keep text readable over them.",
)

add(Element(
    "image", "Image", C,
    "A content image (the primary image of a record), plain or bordered.",
    why="Images are recognised faster than text but must not jump the layout when they load (Doherty threshold: perceived "
        "performance) and must be described for people who cannot see them (Postel's law).",
    when=["The primary image of a record (product, floor plan, camera view)."],
    how=["`<img class=\"orca-img\" src=… alt=… width=… height=… loading=\"lazy\">`. Always set width and height or put it in an `orca-ratio` frame.",
         "`.orca-img--bordered` when the image's edge could merge with the page (white photos, screenshots).",
         "`alt` describes what matters in the image for the task; decorative images get `alt=\"\"`."],
    a11y=["Never put text people must read inside the image."],
    classes=[".orca-img", ".orca-img--bordered", ".orca-img--cover"], tokens=["bg-alt", "border"],
    laws=["doherty", "postel"],
    examples=[("Bordered image", """<img class="orca-img orca-img--bordered" src="{% static "orca/img/sample-floor.svg" %}" alt="Floor plan of the north building with two entrances" width="320" height="200" loading="lazy">""")],
    guide=["Primary image", "Image (bordered)"],
    related=["media-frame", "thumbnail"],
))

add(Element(
    "thumbnail", "Thumbnail image", C,
    "A small square preview (48 or 96px) cropped to fill.",
    why="A consistent small preview lets people spot the right record in a list by sight (Miller's law: recognition).",
    when=["List rows, table cells, cards, pickers."],
    how=["`<img class=\"orca-thumb\" src=… alt=\"\" width=\"48\" height=\"48\" loading=\"lazy\">`; `.orca-thumb--lg` for 96px.",
         "Use `alt=\"\"` when the record's name is next to it."],
    classes=[".orca-thumb", ".orca-thumb--lg"], tokens=["thumb", "thumb-lg"],
    laws=["miller"],
    examples=[("Thumbnails", """<div class="orca-row orca-row--16">
  <img class="orca-thumb" src="{% static "orca/img/sample-street.svg" %}" alt="" width="48" height="48">
  <img class="orca-thumb orca-thumb--lg" src="{% static "orca/img/sample-street.svg" %}" alt="" width="96" height="96">
</div>""")],
    guide=["Thumbnail image"],
))

add(Element(
    "hero-image", "Hero image", C,
    "A wide image (21:9, 4:3 on phones) heading a marketing or landing page.",
    why="A single strong image sets the context of a landing page at a glance (Aesthetic–usability effect).",
    when=["Marketing and landing pages only."],
    avoid=["Application screens: it pushes the task below the fold.", "Text over the image without a solid or gradient backing (Practical UI T12)."],
    how=["`<img class=\"orca-hero-img\" src=… alt=…>`; serve responsive sizes with `srcset`.", "Compose with the subject off-centre (rule of thirds)."],
    classes=[".orca-hero-img"], tokens=["bg-alt"],
    laws=["aesthetic", "T12"],
    examples=[("Hero", """<img class="orca-hero-img" src="{% static "orca/img/sample-street.svg" %}" alt="Shoppers entering a city-centre store">""")],
    guide=["Hero image"],
))

add(Element(
    "media-frame", "Aspect-ratio frame", C,
    "A box with a fixed aspect ratio that holds an image, video, map or chart and reserves its space.",
    why="Reserved space prevents layout shift while media loads, so nothing moves under the pointer (Doherty threshold, Fitts's law).",
    when=["Any media whose dimensions are not known in the HTML; grids of snapshots or cards with images."],
    how=["`<div class=\"orca-ratio orca-ratio--16x9\"><img src=… alt=…></div>`. Ratios: 1x1, 4x3, 3x2, 16x9, 21x9, 3x4, or `style=\"--orca-ratio: 5 / 4\"`.",
         "Media fills and crops by default; `.orca-ratio--contain` letterboxes instead (floor plans, documents)."],
    classes=[".orca-ratio", ".orca-ratio--16x9", ".orca-ratio--contain"], tokens=["bg-alt"],
    laws=["doherty", "fitts"],
    examples=[("4:3 frame", """<div class="orca-ratio orca-ratio--4x3" style="max-width: 16rem"><img src="{% static "orca/img/sample-street.svg" %}" alt="Street outside entrance A"></div>""")],
    guide=["Aspect-ratio frame"],
    related=["aspect-ratio", "snapshot-image"],
))

add(Element(
    "snapshot-image", "Snapshot image", C,
    "A camera snapshot in a 16:9 frame with its camera and capture time on a solid caption bar.",
    why="A snapshot is evidence; its source and time must always be visible and readable over any picture (Practical UI T12: solid backing).",
    when=["Alert details, capture runs, camera cards."],
    how=["`<figure class=\"orca-ratio orca-ratio--16x9\"><img …><figcaption class=\"orca-frame__caption\"><span>Entrance A</span><time datetime=…>08:14:03</time></figcaption></figure>`.",
         "Removed or expired image: replace the img with `<div class=\"orca-ratio orca-ratio--16x9 orca-frame--removed\">Image removed after 30 days</div>`."],
    a11y=["Alt text says what was captured and when; the caption repeats it visibly."],
    classes=[".orca-frame__caption", ".orca-frame--removed"],
    laws=["T12", "postel"],
    examples=[("Snapshot and removed snapshot", """<div class="orca-row orca-row--16" style="align-items: flex-start">
  <figure class="orca-ratio orca-ratio--16x9" style="max-width: 18rem; margin: 0">
    <img src="{% static "orca/img/sample-street.svg" %}" alt="Entrance A at 08:14, two people at the door">
    <figcaption class="orca-frame__caption"><span>Entrance A</span><time datetime="2026-11-06T08:14:03">08:14:03</time></figcaption>
  </figure>
  <div class="orca-ratio orca-ratio--16x9 orca-frame--removed" style="max-width: 18rem">Image removed after 30 days</div>
</div>""")],
    guide=["Snapshot image"], source="ORCA",
))

add(Element(
    "recording-frame", "Recording frame", C,
    "A video or stream frame marked as recording or live with a red outline and a worded flag.",
    why="Being recorded is a state people must not miss: red outline, pulsing dot and the word 'Recording' together "
        "(Von Restorff; C03: never colour alone).",
    when=["Live streams and recordings in progress."],
    how=["`<div class=\"orca-ratio orca-ratio--16x9 orca-frame--recording\">…<span class=\"orca-frame__flag\"><span class=\"orca-dot orca-dot--pulse\"></span>Recording</span></div>`.",
         "Use 'Live' for a stream that is not being stored."],
    classes=[".orca-frame--recording", ".orca-frame__flag"], tokens=["negative"],
    laws=["restorff", "C03"],
    examples=[("Recording", """<div class="orca-ratio orca-ratio--16x9 orca-frame--recording" style="max-width: 20rem">
  <img src="{% static "orca/img/sample-street.svg" %}" alt="Live view of entrance A">
  <span class="orca-frame__flag"><span class="orca-dot orca-dot--sm orca-dot--pulse"></span>Recording</span>
</div>""")],
    guide=["Recording frame"], source="ORCA",
))

add(Element(
    "video-frame", "Video frame", C,
    "A native `<video>` with controls inside an aspect-ratio frame.",
    why="Native controls are familiar and keyboard accessible (Jakob's law, Postel's law); the frame reserves space (Doherty).",
    when=["Recorded clips, tutorials."],
    how=["`<div class=\"orca-ratio orca-ratio--16x9\"><video class=\"orca-video\" controls preload=\"metadata\" poster=…><source …><track kind=\"captions\" …></video></div>`.",
         "Never autoplay with sound."],
    a11y=["Provide captions for speech; describe essential visual content."],
    classes=[".orca-video"],
    laws=["jakob", "postel", "doherty"],
    examples=[("Video", """<div class="orca-ratio orca-ratio--16x9" style="max-width: 20rem"><video class="orca-video" controls preload="none" poster="{% static "orca/img/sample-street.svg" %}" aria-label="Clip from entrance A, 08:14"></video></div>""")],
    guide=["Video frame"],
))

add(Element(
    "illustration", "Illustration (empty, search, error)", C,
    "Simple token-coloured line illustrations for empty, no-result and error states.",
    why="A calm illustration softens an empty or failed moment and signals that the state is expected (Peak–end rule), "
        "while staying in the system's colours in every theme.",
    when=["Empty states and no-result states; error pages."],
    avoid=["Decorating normal content."],
    how=["`{% orca_illustration \"empty\" %}`, `\"search\"` or `\"error\"`. They are decorative (`aria-hidden`); the title and text carry the meaning."],
    classes=[".orca-illustration"], tokens=["brand", "accent", "border-strong"],
    laws=["peak-end", "aesthetic"],
    examples=[("Illustrations", """<div class="orca-row orca-row--16">{% orca_illustration "empty" %}{% orca_illustration "search" %}{% orca_illustration "error" %}</div>""")],
    guide=["Illustration (empty, search)"],
    related=["empty-title"],
))

add(Element(
    "qr-code", "QR code", C,
    "A frame for a server-generated QR code: white quiet zone, black modules, and the encoded text below.",
    why="QR codes only scan with enough contrast and quiet zone, so the frame is always black on white whatever the theme; "
        "printing the text below gives a fallback (Postel's law).",
    when=["Pairing a phone, sharing a link to a physical place, two-factor setup."],
    how=["Generate the SVG on the server (for example with the `segno` package: `segno.make(url).svg_inline(scale=4)`).",
         "`<figure class=\"orca-code-frame\">{{ qr_svg|safe }}<figcaption class=\"orca-code-frame__text\">ABCD-1234</figcaption></figure>`.",
         "Keep at least 4 modules of white around the code; never recolour it."],
    a11y=["Give the code a text alternative: the link or secret written out."],
    classes=[".orca-code-frame", ".orca-code-frame__text"],
    laws=["postel"],
    examples=[("QR frame (placeholder image)", """<figure class="orca-code-frame" style="margin: 0"><img src="{% static "orca/img/sample-qr.svg" %}" alt="QR code for the setup link"><figcaption class="orca-code-frame__text">ORCA-7Q2K</figcaption></figure>""")],
    guide=["QR code"], source="ORCA",
))

add(Element(
    "barcode", "Barcode", C,
    "A frame for a server-generated 1D barcode with its human-readable digits below.",
    why="Same rules as QR: fixed black on white for scanners, digits for people (Postel's law).",
    when=["Asset labels, tickets, inventory."],
    how=["Generate the SVG on the server (for example `python-barcode`).",
         "`<figure class=\"orca-code-frame orca-code-frame--barcode\">{{ svg|safe }}<figcaption class=\"orca-code-frame__text\">4006381333931</figcaption></figure>`."],
    classes=[".orca-code-frame--barcode"],
    laws=["postel"],
    examples=[("Barcode frame (placeholder)", """<figure class="orca-code-frame orca-code-frame--barcode" style="margin: 0"><img src="{% static "orca/img/sample-barcode.svg" %}" alt="Barcode 4006381333931"><figcaption class="orca-code-frame__text">4006381333931</figcaption></figure>""")],
    guide=["Barcode"], source="ORCA",
))
