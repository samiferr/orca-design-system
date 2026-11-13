# Identity

Who and what: the product's logo and favicon, and people's avatars.

## Logo

`id: logo` · level: primitive · source: Tangerine

The product's logo image, or its name as a wordmark with a brand bar when no logo is set.

### When to use

- Top bar, sidebar header, login card, email header.

### When not to use

- Recolouring or stretching a logo file.
- More than one logo per screen.

### How to use

- `{% orca_logo %}` links to '/'. `{% orca_logo href="" %}` renders it without a link; `size="lg"` for login screens.
- Configure `ORCA['BRAND']['logo']` (static path, SVG preferred) and `['name']` (alt text and wordmark).

### Accessibility

- The image alt is the product name; a linked logo's accessible name is the product name (not 'logo').

#### Example: Logo

```django
<div class="orca-row orca-row--16">
  {% orca_logo %}
  {% orca_logo href="" size="lg" %}
</div>
```

**Classes:** `.orca-logo`, `.orca-logo__img`, `.orca-logo__mark`, `.orca-logo--lg`

**Tokens:** `--orca-brand`

**Principles applied:** Jakob's law: work the way products people already know work; Tesler's law: move unavoidable complexity from the user to the system

**Related:** `brand-color`, `favicon`

**ORCA guide items covered:** Logo

---

## Avatar

`id: avatar` · level: primitive · source: Tangerine

A person's picture or initials in a circle (or square for organisations and devices).

### When to use

- Next to a person's name in lists, comments, activity, the user chip.
- Square: organisations, sites, devices.

### When not to use

- Avatar without the name nearby unless the name is in a tooltip and the list is of known people.

### How to use

- Image: `<span class="orca-avatar"><img src=… alt=""></span>` (empty alt when the name is beside it).
- Initials: `<span class="orca-avatar" aria-hidden="true">{{ user.get_full_name|orca_initials }}</span>`.
- Sizes: `--xs` 24, `--s` 32, default 40, `--l` 48, `--xl` 96. Square: `--square`.
- Presence: add `<span class="orca-avatar__presence orca-dot--positive"></span>` and say the presence in text too.

### Accessibility

- If the avatar stands alone, give the image `alt` with the person's name, or `role="img" aria-label` on initials.

#### Example: Sizes and kinds

```django
<div class="orca-row orca-row--16">
  <span class="orca-avatar orca-avatar--xs" aria-hidden="true">AL</span>
  <span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span>
  <span class="orca-avatar" aria-hidden="true">{{ "Grace Hopper"|orca_initials }}</span>
  <span class="orca-avatar orca-avatar--l">
    <img src="{% static "orca/img/sample-person.svg" %}" alt="Ada Lovelace">
    <span class="orca-avatar__presence orca-dot--positive"></span>
  </span>
  <span class="orca-avatar orca-avatar--xl orca-avatar--square" role="img" aria-label="North building">NB</span>
</div>
```

**Classes:** `.orca-avatar`, `.orca-avatar--xs`, `.orca-avatar--s`, `.orca-avatar--l`, `.orca-avatar--xl`, `.orca-avatar--square`, `.orca-avatar__presence`

**Tokens:** `--orca-avatar-xs`, `--orca-avatar-s`, `--orca-avatar-m`, `--orca-avatar-l`, `--orca-avatar-xl`, `--orca-neutral-bg`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Avatar (xs, s, l, xl); Avatar (square); Avatar initials; Avatar image

---

## Favicon set

`id: favicon` · level: primitive · source: Tangerine

The browser-tab and home-screen icons for the product.

### When to use

- Every deployment.

### How to use

- Set `ORCA['BRAND']['favicon']` to a 32px PNG or an SVG in your static files; `{% orca_head %}` writes the `<link rel="icon">`.
- For installable apps also add apple-touch-icon (180px), 192px and 512px icons and a manifest in your base template.
- `theme-color` is written from the brand fill automatically.

#### Example: What orca_head writes

```django
<pre class="orca-code" style="display: block; white-space: pre-wrap">&lt;link rel="icon" href="/static/brand/favicon.svg" type="image/svg+xml"&gt;
&lt;meta name="theme-color" content="{% orca_brand "color" %}"&gt;</pre>
```

**Tokens:** `--orca-brand-strong`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**Related:** `logo`

**ORCA guide items covered:** Favicon set; Favicon

---
