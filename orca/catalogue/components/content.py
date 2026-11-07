from ..registry import add, category
from . import Component

C = category(
    "content-blocks", "Content blocks",
    "Reusable blocks for products, people, posts, heroes and media.",
    level="component",
)

add(Component(
    "product-item", "Product item", C,
    "A product tile: square image, name, price and one action.",
    why="Image, name and price grouped by proximity let people compare products at a glance (Miller's law, Practical UI L01); one action keeps the decision simple (Hick's law).",
    when=["Product grids and lists in shops and catalogues."],
    how=["`<article class=\"orca-product\">` with `.orca-product__image` (square, reserved), `.orca-product__name` (link to the product), `.orca-product__price` (old price in `<s>` with a hidden 'was') and an action.",
         "Long names wrap; never truncate a product name."],
    classes=[".orca-product", ".orca-product__image", ".orca-product__name", ".orca-product__price"],
    laws=["miller", "L01", "hick", "L15"],
    uses=["image", "button"],
    examples=[("Product", """<article class="orca-product" style="max-width: 14rem">
  <div class="orca-product__image"><img src="{% static "orca/img/sample-street.svg" %}" alt=""></div>
  <h3 class="orca-product__name"><a href="#">Dome camera, 4 MP, outdoor</a></h3>
  <p class="orca-product__price" style="margin: 0">€189<s><span class="orca-sr-only">was </span>€229</s></p>
  <button class="orca-button orca-button--dense" type="button">Add to quote</button>
</article>""")],
    guide=["Product item"],
))

add(Component(
    "person-block", "Person block", C,
    "Avatar, name and role, optionally with a contact action.",
    why="Faces and roles help people recognise who someone is before reading the name (Miller's law: recognition).",
    when=["Owners, assignees, contacts, authors."],
    how=["`<div class=\"orca-person\">` with an avatar and `.orca-person__text` (`__name`, `__role`); add a link or icon button for contact.",
         "Use the person's preferred name; never shorten it in a way they did not choose."],
    classes=[".orca-person", ".orca-person__text", ".orca-person__name", ".orca-person__role"],
    laws=["miller", "postel"],
    uses=["avatar"],
    examples=[("Person", """<div class="orca-person"><span class="orca-avatar" aria-hidden="true">AL</span><span class="orca-person__text"><span class="orca-person__name">Ada Lovelace</span><span class="orca-person__role">Site manager, North building</span></span><a class="orca-icon-button" href="#" aria-label="Email Ada Lovelace">{% icon "mail" %}</a></div>""")],
    guide=["Person block"],
))

add(Component(
    "post-block", "Block post", C,
    "An article teaser: kicker, headline, excerpt, meta and a thumbnail.",
    why="Leading with an informative headline and a short excerpt lets people decide whether to read (Practical UI W04, W05).",
    when=["News, release notes, help articles, blog lists."],
    how=["`<article class=\"orca-post\">` with text (kicker, `.orca-post__title` link, `.orca-post__excerpt` clamped to 3 lines, meta) and `.orca-post__thumb` image.",
         "On narrow screens the image moves above the text."],
    classes=[".orca-post", ".orca-post__title", ".orca-post__excerpt", ".orca-post__thumb"],
    laws=["W04", "W05", "W14"],
    uses=["card-kicker", "card-meta", "thumbnail"],
    examples=[("Post", """<article class="orca-post" style="max-width: 36rem"><div>
  <p class="orca-card-kicker">Release notes</p><h3 class="orca-post__title"><a href="#">Counting now ignores staff areas</a></h3>
  <p class="orca-post__excerpt">Mark a zone as excluded and people inside it are no longer counted. Existing zones keep their behaviour until you change them.</p>
  <p class="orca-card-meta">6 November 2026 · 2 min read</p></div>
  <img class="orca-post__thumb" src="{% static "orca/img/sample-floor.svg" %}" alt=""></article>""")],
    guide=["Block post (thumbnail + headline + excerpt)"],
))

add(Component(
    "hero", "Hero", C,
    "The opening block of a marketing or landing page: kicker, headline, lead, actions and an image.",
    why="The first screen must state what the product does and offer one clear next step (Von Restorff, Peak–end rule).",
    when=["Marketing, landing and onboarding pages."],
    avoid=["Application screens."],
    how=["`<section class=\"orca-hero\">` with `.orca-hero__text` (kicker, `h1.orca-hero__title`, `.orca-hero__lead`, actions) and `.orca-hero__media`.",
         "One primary action, one secondary. The headline states the benefit in under 10 words."],
    classes=[".orca-hero", ".orca-hero__text", ".orca-hero__title", ".orca-hero__lead", ".orca-hero__media"],
    laws=["restorff", "peak-end", "B03"],
    uses=["heading", "button", "hero-image"],
    examples=[("Hero", """<section class="orca-hero">
  <div class="orca-hero__text"><p class="orca-card-kicker">People counting</p><h1 class="orca-hero__title">Know how busy every door is, right now.</h1><p class="orca-hero__lead">Count visitors with the cameras you already have.</p>
    <div class="orca-row"><a class="orca-button orca-button--brand" href="#">Start free trial</a><a class="orca-button" href="#">See a demo</a></div></div>
  <div class="orca-hero__media"><img src="{% static "orca/img/sample-street.svg" %}" alt="A shop entrance seen from a ceiling camera"></div>
</section>""")],
    guide=["Hero"],
))

add(Component(
    "photo-actions-bar", "Photo-actions bar", C,
    "The row under a photo: like, comment and share with counts, and save at the end.",
    why="A familiar row of icon actions under media (Jakob's law) with counts and pressed states shows people's own reaction clearly.",
    when=["Photo posts, galleries, shared snapshots."],
    how=["`<div class=\"orca-photo-actions\">` of icon buttons with `aria-label` and `aria-pressed` for toggles, each followed by `.orca-photo-actions__count`; save goes in `.orca-photo-actions__end`."],
    classes=[".orca-photo-actions", ".orca-photo-actions__count", ".orca-photo-actions__end"],
    laws=["jakob", "fitts"],
    uses=["icon-button", "toggle-button"],
    examples=[("Actions", """<div class="orca-photo-actions" style="max-width: 24rem">
  <button class="orca-icon-button" type="button" aria-pressed="true" aria-label="Like" data-orca-toggle>{% icon "star" %}</button><span class="orca-photo-actions__count">24</span>
  <button class="orca-icon-button" type="button" aria-label="Comment">{% icon "chat" %}</button><span class="orca-photo-actions__count">3</span>
  <button class="orca-icon-button" type="button" aria-label="Share">{% icon "share" %}</button>
  <button class="orca-icon-button orca-photo-actions__end" type="button" aria-pressed="false" aria-label="Save" data-orca-toggle>{% icon "pin" %}</button>
</div>""")],
    guide=["Photo-actions bar"],
))

add(Component(
    "camera-card", "Camera card", C,
    "A camera's latest snapshot with its status, name, place and actions.",
    why="Operators recognise a camera by its view first (Miller's law); a status flag on the image and a status word below make offline cameras impossible to miss (Von Restorff, C03).",
    when=["Camera grids on dashboards and camera lists."],
    how=["A linked card with `.orca-camera-card`: `.orca-ratio--16x9` snapshot (or a removed frame when offline), a badge in `.orca-camera-card__flag`, body with title link and status light, footer with pin and more actions.",
         "Show the snapshot time; a stale image is labelled as such."],
    classes=[".orca-camera-card", ".orca-camera-card__flag"],
    laws=["miller", "restorff", "C03"],
    uses=["linked-card", "snapshot-image", "status-light", "pin-button"],
    examples=[("Camera cards", """<ul class="orca-card-grid">
  <li><article class="orca-card orca-card--link orca-camera-card"><div class="orca-ratio orca-ratio--16x9"><img src="{% static "orca/img/sample-street.svg" %}" alt=""><span class="orca-frame__caption"><span>Snapshot</span><time datetime="2026-11-06T09:14">09:14</time></span></div>
    <div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">Entrance A</a></h3><span class="orca-status orca-small"><span class="orca-dot orca-dot--positive"></span>Online · North building</span></div>
    <div class="orca-card__footer"><span class="orca-small orca-muted orca-num">1,204 today</span><span class="orca-card__footer-end"><button class="orca-icon-button orca-icon-button--sm orca-pin" type="button" aria-pressed="true" aria-label="Unpin Entrance A" data-orca-toggle data-orca-label-on="Unpin Entrance A" data-orca-label-off="Pin Entrance A">{% icon "pin" %}</button></span></div></article></li>
  <li><article class="orca-card orca-card--link orca-camera-card"><div class="orca-ratio orca-ratio--16x9 orca-frame--removed">No image since 08:14</div><span class="orca-badge orca-badge--negative orca-camera-card__flag">Offline</span>
    <div class="orca-card__body"><h3 class="orca-card-title"><a class="orca-card__link" href="#">Loading dock</a></h3><span class="orca-status orca-small"><span class="orca-dot orca-dot--negative"></span>Offline since 08:14</span></div>
    <div class="orca-card__footer"><span class="orca-small orca-muted">Last count 08:14</span><span class="orca-card__footer-end"><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="More actions for Loading dock">{% icon "more" %}</button></span></div></article></li>
</ul>""")],
    guide=["Camera card"], source="Tangerine",
))
