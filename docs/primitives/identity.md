# Identity

The product's logo and favicon, and people's avatars.

## Logo

`id: logo` · level: primitive · source: Tangerine

The product's logo image, or its name as a wordmark with a brand bar when no logo is set.

### General description

The symbol or wordmark that identifies a product or brand. It usually sits in a top bar or header and links to the home page.

#### Use cases

- Showing the brand in the header or top bar.
- Branding login and sign-up screens.
- Branding emails and documents.

#### When not to use it

- Repeating it many times on one screen.
- Using it as decoration.

#### Best practices

- Keep it in the same place on every page.
- Link it to the home page.
- Never stretch or recolour the file.
- Give it the product name as alt text.

### When to use

- Top bar, sidebar header, login card, email header.

### When not to use

- Recolouring or stretching a logo file.
- More than one logo per screen.

### How to use

- `{% orca_logo %}` links to '/'. `{% orca_logo href="" %}` renders it without a link; `size="lg"` for login screens.
- Configure `ORCA['BRAND']['logo']` (static path, SVG preferred) and `['name']` (alt text and wordmark).

### Accessibility

- The image alt is the product name, also for a linked logo (not 'logo').

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

### General description

A small picture or set of initials that stands for a person, team or account.

#### Use cases

- Showing who wrote a comment or made a change.
- Listing people and team members.
- Showing the signed-in user in a menu.

#### When not to use it

- Decoration with no meaning.
- Showing a company brand: use a logo.

#### Best practices

- Show initials when there is no photo.
- Keep the name nearby or in a tooltip.
- Offer a few consistent sizes.
- Give a text alternative when it stands alone.

### When to use

- Next to a person's name in lists, comments, activity, the user chip.
- Square: organisations, sites, devices.

### When not to use

- An avatar with no name nearby, unless the name is in a tooltip and the people are well known.

### How to use

- Image: `<span class="orca-avatar"><img src=… alt=""></span>` (empty alt when the name is beside it).
- Initials: `<span class="orca-avatar" aria-hidden="true">{{ user.get_full_name|orca_initials }}</span>`.
- Sizes: `--xs` 24, `--s` 32, default 40, `--l` 48, `--xl` 96. Square: `--square`.
- Presence: add `<span class="orca-avatar__presence orca-dot--positive"></span>` and say the presence in text too.

### Accessibility

- A standalone avatar needs the person's name: `alt` on the image, or `role="img" aria-label` on initials.

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

### General description

The small icon that appears in browser tabs, bookmarks and on home screens to represent a site.

#### Use cases

- Helping people find a tab among many.
- Identifying a site in bookmarks and history.
- Showing the app icon when saved to a home screen.

#### When not to use it

- Showing the full brand: use a logo.
- Detailed images that become unreadable when tiny.

#### Best practices

- Keep it simple so it reads at 16px.
- Provide an SVG or PNG and larger sizes for phones.
- Make it clear on light and dark tabs.
- Match it to the brand.

### When to use

- Every deployment.

### How to use

- Set `ORCA['BRAND']['favicon']` to a 32px PNG or an SVG in your static files; `{% orca_head %}` writes the `<link rel="icon">`.
- Installable apps also need apple-touch-icon (180px), 192px and 512px icons and a manifest in the base template.
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
