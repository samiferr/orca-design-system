from .registry import Element, add, category

C = category(
    "identity", "Identity",
    "Who and what: the product's logo and favicon, and people's avatars.",
)

add(Element(
    "logo", "Logo", C,
    "The product's logo image, or its name as a wordmark with a brand bar when no logo is set.",
    why="A consistent mark in a consistent place confirms where people are (Jakob's law). Falling back to plain type keeps "
        "every deployment branded without asking for artwork (Tesler's law).",
    when=["Top bar, sidebar header, login card, email header."],
    avoid=["Recolouring or stretching a logo file.", "More than one logo per screen."],
    how=["`{% orca_logo %}` links to '/'. `{% orca_logo href=\"\" %}` renders it without a link; `size=\"lg\"` for login screens.",
         "Configure `ORCA['BRAND']['logo']` (static path, SVG preferred) and `['name']` (alt text and wordmark)."],
    a11y=["The image alt is the product name; a linked logo's accessible name is the product name (not 'logo')."],
    classes=[".orca-logo", ".orca-logo__img", ".orca-logo__mark", ".orca-logo--lg"],
    tokens=["brand"],
    laws=["jakob", "tesler"],
    examples=[("Logo", """<div class="orca-row orca-row--16">{% orca_logo %}{% orca_logo href="" size="lg" %}</div>""")],
    guide=["Logo"],
    related=["brand-color", "favicon"],
))

add(Element(
    "avatar", "Avatar", C,
    "A person's picture or initials in a circle (or square for organisations and devices).",
    why="Faces and initials let people recognise who did what faster than reading names (Miller's law: recognition "
        "over recall). Initials keep the layout stable when there is no photo (Postel's law).",
    when=["Next to a person's name in lists, comments, activity, the user chip.", "Square: organisations, sites, devices."],
    avoid=["Avatar without the name nearby unless the name is in a tooltip and the list is of known people."],
    how=["Image: `<span class=\"orca-avatar\"><img src=… alt=\"\"></span>` (empty alt when the name is beside it).",
         "Initials: `<span class=\"orca-avatar\" aria-hidden=\"true\">{{ user.get_full_name|orca_initials }}</span>`.",
         "Sizes: `--xs` 24, `--s` 32, default 40, `--l` 48, `--xl` 96. Square: `--square`.",
         "Presence: add `<span class=\"orca-avatar__presence orca-dot--positive\"></span>` and say the presence in text too."],
    a11y=["If the avatar stands alone, give the image `alt` with the person's name, or `role=\"img\" aria-label` on initials."],
    classes=[".orca-avatar", ".orca-avatar--xs", ".orca-avatar--s", ".orca-avatar--l", ".orca-avatar--xl", ".orca-avatar--square", ".orca-avatar__presence"],
    tokens=["avatar-xs", "avatar-s", "avatar-m", "avatar-l", "avatar-xl", "neutral-bg"],
    laws=["miller", "postel"],
    examples=[("Sizes and kinds", """<div class="orca-row orca-row--16">
  <span class="orca-avatar orca-avatar--xs" aria-hidden="true">AL</span>
  <span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span>
  <span class="orca-avatar" aria-hidden="true">{{ "Grace Hopper"|orca_initials }}</span>
  <span class="orca-avatar orca-avatar--l"><img src="{% static "orca/img/sample-person.svg" %}" alt="Ada Lovelace"><span class="orca-avatar__presence orca-dot--positive"></span></span>
  <span class="orca-avatar orca-avatar--xl orca-avatar--square" role="img" aria-label="North building">NB</span>
</div>""")],
    guide=["Avatar (xs, s, l, xl)", "Avatar (square)", "Avatar initials", "Avatar image"],
))

add(Element(
    "favicon", "Favicon set", C,
    "The browser-tab and home-screen icons for the product.",
    why="People find their tab by its icon among many (Von Restorff); a consistent icon also marks installed apps.",
    when=["Every deployment."],
    how=["Set `ORCA['BRAND']['favicon']` to a 32px PNG or an SVG in your static files; `{% orca_head %}` writes the `<link rel=\"icon\">`.",
         "For installable apps also add apple-touch-icon (180px), 192px and 512px icons and a manifest in your base template.",
         "`theme-color` is written from the brand fill automatically."],
    tokens=["brand-strong"],
    laws=["restorff"],
    examples=[("What orca_head writes", """<pre class="orca-code" style="display: block; white-space: pre-wrap">&lt;link rel="icon" href="/static/brand/favicon.svg" type="image/svg+xml"&gt;
&lt;meta name="theme-color" content="{% orca_brand "color" %}"&gt;</pre>""")],
    guide=["Favicon set", "Favicon"],
    related=["logo"],
))
