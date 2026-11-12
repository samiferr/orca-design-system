# Layouts

Whole-page Django templates you extend. They place patterns in a fixed structure and leave named blocks for your content. Every page of an ORCA project starts from one of these.

## Base layout

`id: base-layout` · level: template · source: ORCA

The root every ORCA page extends: the html element with language, theme and density, the head with ORCA's styles and theme bootstrap, the skip link, and slots for body, modal and scripts.

Built from: `page-landmarks`

### Why

Every page needs the same document skeleton, and getting it slightly wrong breaks accessibility (no language, no skip link) or causes a flash of the wrong theme. One base removes that whole class of mistakes (Tesler's law).

### When to use

- Directly only for pages with no ORCA chrome (a print view, an embed); otherwise extend the app shell, auth, error, marketing or docs layout.

### How to use

- Extend it: `{% extends "orca/layouts/base.html" %}`, then fill only the blocks you need.
- Set `lang` in the context (or override `html_attrs`) for non-English pages.
- Put page-specific CSS in `extra_head` and scripts in `extra_scripts`; never replace `head` unless you also call `orca_head`.

Extend: `{% extends "orca/layouts/base.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `html_attrs`, `content`

### Context it reads

- `title`
- `lang`: the page language (default "en").

#### Example: Usage

```django
{% templatetag openblock %} extends "orca/layouts/base.html" {% templatetag closeblock %}
{% templatetag openblock %} block title {% templatetag closeblock %}Print view{% templatetag openblock %} endblock {% templatetag closeblock %}
{% templatetag openblock %} block content {% templatetag closeblock %}…{% templatetag openblock %} endblock {% templatetag closeblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
from django.utils.translation import get_language
from django.views.generic import TemplateView


class Landing(TemplateView):
    template_name = "videos/landing.html"   # {% extends "orca/layouts/base.html" %}

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(title="Welcome", lang=get_language())   # <html lang="…"> and the <title>
        return ctx
```

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Jakob's law: work the way products people already know work

---

## App shell

`id: app-shell` · level: template · source: ORCA

The application frame: top bar with brand, sidebar navigation that collapses to a rail (a drawer on phones), and a main column with breadcrumbs, page title, subtitle, actions, messages and content.

Built from: `top-bar`, `sidebar`, `page-head`, `messages-region`

### Why

People learn an application's frame once and then only read what changes (Jakob's law). A fixed place for title, actions and messages makes every page scannable in the same order (Practical UI L03), and the collapsible sidebar gives dense screens their space back.

### When to use

- Every signed-in page of an application: lists, details, forms, dashboards, calendars.

### How to use

- Extend it: `{% extends "orca/layouts/app.html" %}`, then fill only the blocks you need.
- Fill `content`; set `title` and `nav` in the context (or override `sidebar_nav`).
- Put the page's main button in `page_actions` (one primary, Practical UI B03).
- On phones the sidebar opens over the page from the menu button (`data-orca-sidebar-open`); Escape closes it.

### Accessibility

- One `main` landmark with id `main` for the skip link; the sidebar is a `nav` labelled “Sections”.

Extend: `{% extends "orca/layouts/app.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.

#### Example: Child template

```django
{% extends "orca/layouts/app.html" %}{% load orca %}
{% block page_actions %}<button class="orca-button" type="button">Secondary action</button><a class="orca-button orca-button--primary orca-create" href="#">{% icon "plus" %}Main action</a>{% endblock %}
{% block content %}<div class="orca-vstack">
  <section class="orca-panel" aria-label="Section"><div class="orca-skeleton orca-skeleton--title" style="max-width: 16rem"></div><div class="orca-skeleton orca-skeleton--text"></div><div class="orca-skeleton orca-skeleton--text" style="max-width: 70%"></div></section>
  <div class="orca-two-col"><section class="orca-panel" aria-label="Section"><div class="orca-skeleton orca-aspect-16x9"></div></section><section class="orca-panel" aria-label="Section"><div class="orca-skeleton orca-aspect-16x9"></div></section></div>
</div>{% endblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Context processor and view

```python
# videos/context_processors.py — add "videos.context_processors.orca" to TEMPLATES["OPTIONS"]["context_processors"]
from django.urls import reverse


def orca(request):
    """The sidebar of the app shell, on every page."""
    path = request.path

    def item(label, name, icon, count=None):
        url = reverse(name)
        return {"label": label, "url": url, "icon": icon, "count": count, "current": path.startswith(url)}

    return {"nav": [
        {"label": "Library", "items": [item("Videos", "video-list", "play"), item("Albums", "album-list", "folder")]},
        {"label": "Admin", "items": [item("Users", "user-list", "user"), item("Settings", "settings", "settings")]},
    ]}


# videos/views.py — any view that renders a template extending orca/layouts/app.html
from django.views.generic import TemplateView


class Overview(TemplateView):
    template_name = "videos/overview.html"   # {% extends "orca/layouts/app.html" %}
    extra_context = {
        "title": "Overview",
        "subtitle": "Everything that happened in your library today.",
        "breadcrumbs": [("Library", "/videos/"), ("Overview", "")],
    }
    # `messages` and `user` come from Django's context processors; ORCA shows them in the shell.
```

**Classes:** `.orca-shell__menu`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI L03: Establish an order of importance; Practical UI B03: One primary action; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** App shell

---

## Auth layout

`id: auth-layout` · level: template · source: ORCA

A centred card on the alternate ground for sign-in, password reset and other pages before an account is open.

Built from: `login-card`

### Why

Before sign-in people should see one task and nothing to wander off to (Hick's law); the brand on the card confirms they are in the right place (Practical UI C08).

### When to use

- Sign in, sign out, password reset and change, locked-out and invitation pages.

### How to use

- Extend it: `{% extends "orca/layouts/auth.html" %}`, then fill only the blocks you need.
- With Django's `LoginView`, `template_name="orca/layouts/auth.html"` works as is: it renders `form` with `orca_field`.
- Override `form_extra` for 'Keep me signed in' and the reset link, `footer` for help text, `submit_label` for the button.

Extend: `{% extends "orca/layouts/auth.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `content`, `brand`, `page_title`, `page_subtitle`, `messages`, `form_extra`, `submit_label`, `footer`

### Context it reads

- `form`: any Django form (fields are rendered in order).
- `title`, `subtitle`, `submit_label`, `form_action`.

#### Example: Child template

```django
{% extends "orca/layouts/auth.html" %}
{% block form_extra %}<div class="orca-login__row"><label class="orca-check"><input type="checkbox" name="remember"><span class="orca-check__box"></span>Keep me signed in</label><a class="orca-link orca-small" href="#">Forgot your password?</a></div>{% endblock %}
{% block footer %}<p class="orca-login__foot">No account? Ask your administrator.</p>{% endblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### URLs

```python
# accounts/urls.py — Django's auth views with the ORCA layout
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="orca/layouts/auth.html",
        extra_context={"title": "Sign in", "subtitle": "Use your work email.", "submit_label": "Sign in"},
    ), name="login"),
    path("password-reset/", auth_views.PasswordResetView.as_view(
        template_name="orca/layouts/auth.html",
        extra_context={"title": "Reset your password", "submit_label": "Send the reset link"},
    ), name="password_reset"),
]
```

**Classes:** `.orca-auth`, `.orca-auth-page`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Practical UI C08: Choose and adapt the brand colour deliberately; Practical UI R01: Keep the main form flow in one column

**ORCA guide items covered:** Auth layout

---

## Email layout

`id: email-layout` · level: template · source: ORCA

The page frame of every transactional email: brand bar, title, paragraphs, one action with its link printed, and footer, with colours written inline.

Built from: `email-frame`

### Why

Email clients ignore stylesheets, so the layout is tables with inline hex colours computed from the brand (Postel's law). One template keeps every email recognisable (Jakob's law).

### When to use

- Every email the project sends.

### How to use

- Extend it: `{% extends "orca/email/base.html" %}`, then fill only the blocks you need.
- Fill `content` (or pass `paragraphs`), set `action_url` and `action_label`, and `footer` with why the reader gets it.
- Send it with `render_to_string` as the HTML alternative of an `EmailMultiAlternatives`; always add the plain-text body.

Extend: `{% extends "orca/email/base.html" %}`

Blocks: `title`, `preheader`, `brand`, `heading`, `content`, `action`, `footer`

### Context it reads

- `title`, `preheader`, `paragraphs`, `action_url`, `action_label`, `footer`, `lang`.

#### Example: Child template

```django
{% extends "orca/email/base.html" %}
{% block footer %}{{ footer }} <a href="#">Email settings</a>{% endblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Sending the email

```python
# videos/notifications.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_offline_alert(video, recipients):
    context = {
        "title": f"{video} is offline",
        "preheader": f"No video since {video.last_seen:%H:%M}",
        "paragraphs": [f"{video} has sent nothing since {video.last_seen:%H:%M} today.",
                       "Check the network connection; playback restarts on its own."],
        "action_url": f"https://example.com{video.get_absolute_url()}",
        "action_label": "Open the video",
        "footer": "You get this email because you are on the alert list.",
    }
    html = render_to_string("orca/email/base.html", context)   # colours are inlined: no CSS needed
    message = EmailMultiAlternatives(context["title"], strip_tags(html), to=recipients)
    message.attach_alternative(html, "text/html")
    message.send()
```

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Jakob's law: work the way products people already know work; Practical UI W05: Order explanations as an inverted pyramid

**ORCA guide items covered:** Email layout

---

## Error layouts

`id: error-layouts` · level: template · source: ORCA

403, 404 and 500 pages: logo, illustration, error code, what happened in plain words and what to do next.

Built from: `error-message`

### Why

An error page is the low point of a visit; saying plainly what happened and offering the way out limits the damage (Peak–end rule, Practical UI W15).

### When to use

- Your project's `templates/403.html`, `404.html` and `500.html`.

### How to use

- Extend it: `{% extends "orca/layouts/error.html" %}`, then fill only the blocks you need.
- Create `templates/404.html` containing `{% extends "orca/errors/404.html" %}`; the same for 403 and 500.
- The 500 page renders without a request context: it uses no template tags that need one.
- Override `error_text` and `error_actions` to point to your support or status page.

Extend: `{% extends "orca/layouts/error.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `brand`, `illustration`, `error_code`, `page_title`, `error_text`, `error_actions`

#### Example: Child template

```django
{% extends "orca/errors/404.html" %}
```

**Classes:** `.orca-error-layout`, `.orca-error-layout__body`, `.orca-error-layout__code`, `.orca-error-page`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Practical UI W15: Help people recover from errors; Practical UI W01: Make every word useful

**ORCA guide items covered:** Error layouts (403, 404, 500)

---

## Homepage template

`id: homepage-template` · level: template · source: ORCA

The page people land on after signing in: a greeting, a stat grid, a main column for what changed and an aside with shortcuts.

Built from: `app-shell`, `kpi-grid`, `activity-feed`

### Why

The first screen should answer 'is everything all right, and what needs me?' (Peak–end rule); stats first and shortcuts to frequent tasks shorten every visit (Fitts's law).

### When to use

- The start page of an application.

### How to use

- Extend it: `{% extends "orca/layouts/home.html" %}`, then fill only the blocks you need.
- Pass `stats` (label, value, icon, foot, url) and `shortcuts` (label, url, icon); fill `home_main` with recent activity or tasks.

Extend: `{% extends "orca/layouts/home.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `home_stats`, `home_main`, `home_aside`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `stats`, `shortcuts`.

#### Example: Child template

```django
{% extends "orca/layouts/home.html" %}
{% block page_subtitle %}<p class="orca-page-subtitle">Here is what changed since yesterday.</p>{% endblock %}
{% block home_main %}<section class="orca-panel" aria-labelledby="h-recent"><h2 class="orca-panel-title" id="h-recent">Recent activity</h2>
  <div class="orca-vstack orca-vstack--tight">{% for i in "123" %}<div class="orca-activity"><span class="orca-avatar orca-avatar--s" aria-hidden="true">PN</span><div class="orca-activity__head"><strong>Person name</strong> changed Record name {{ i }}<time class="orca-activity__time">{{ i }} h ago</time></div></div>{% endfor %}</div></section>{% endblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "orca/layouts/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        ctx["title"] = f"Good morning, {user.first_name}"
        ctx["stats"] = [
            {"label": "Views today", "value": f"{views_today():,}", "icon": "show", "url": "/reports/"},
            {"label": "Videos", "value": Video.objects.count(), "icon": "play", "foot": "3 processing"},
        ]
        ctx["shortcuts"] = [{"label": "Add a video", "url": "/videos/new/", "icon": "plus"},
                            {"label": "Open reports", "url": "/reports/", "icon": "statistics"}]
        return ctx
```

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI L03: Establish an order of importance

**ORCA guide items covered:** Homepage template

---

## Feed skeleton

`id: feed-skeleton` · level: template · source: ORCA

A centred column of posts with skeleton posts while more load, and an empty state when there are none.

Built from: `photo-post`, `loading-placeholder`, `no-results`

### Why

A narrow column keeps photos and captions at a readable width (Practical UI T09); skeletons that match the post shape make loading feel faster and stop the page jumping (Doherty threshold).

### When to use

- Photo and update feeds, timelines of posts.

### How to use

- Extend it: `{% extends "orca/layouts/feed.html" %}`, then fill only the blocks you need.
- Pass `posts` (author, when, image, alt, text); set `loading` before the first page or `has_more` to show skeleton posts at the end.
- Load the next page with htmx on the skeleton (`hx-trigger="revealed"`) and replace it.

Extend: `{% extends "orca/layouts/feed.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `feed_compose`, `feed`, `feed_loading`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `posts`, `loading`, `has_more`, `empty_title`, `empty_text`.

#### Example: Child template

```django
{% extends "orca/layouts/feed.html" %}
{% block page_head %}{% endblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
from django.views.generic import TemplateView


class Feed(TemplateView):
    template_name = "orca/layouts/feed.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        posts = Post.objects.select_related("author").order_by("-created_at")[:20]
        ctx["posts"] = [{"author": p.author.get_full_name(), "when": p.created_at, "text": p.text,
                         "image": p.image.url if p.image else "", "alt": p.image_alt} for p in posts]
        ctx.update(title="Feed", has_more=Post.objects.count() > 20,
                   empty_title="No posts yet", empty_text="Share the first clip with your team.")
        return ctx
```

**Classes:** `.orca-feed`, `.orca-feed__skeleton`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Practical UI T09: Limit reading measure; Aesthetic–usability effect: consistent, careful visuals earn trust

**ORCA guide items covered:** Feed skeleton

---

## Person-block grid

`id: person-block-grid` · level: template · source: ORCA

A grid of people cards: avatar, name, role and a contact action.

Built from: `card-grid-layout`

### Why

Faces and names in a regular grid are found by recognition rather than reading (Practical UI L11); the same card for everyone keeps it scannable (Jakob's law).

### When to use

- Team pages, members of a site or project, directories.

### How to use

- Extend it: `{% extends "orca/layouts/people.html" %}`, then fill only the blocks you need.
- Pass `people` (name, role, url, email). Use a table instead when people are compared on several attributes.

Extend: `{% extends "orca/layouts/people.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `people`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `people`, `empty_title`.

#### Example: Child template

```django
{% extends "orca/layouts/people.html" %}
{% block page_actions %}<a class="orca-button orca-button--primary" href="#">Invite people</a>{% endblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# people/views.py
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView


class Team(TemplateView):
    template_name = "orca/layouts/people.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        users = get_user_model().objects.filter(is_active=True).order_by("first_name")
        ctx["people"] = [{"name": u.get_full_name(), "role": u.profile.role, "email": u.email,
                          "url": f"/people/{u.pk}/"} for u in users]
        ctx.update(title="Team", empty_title="No one here yet")
        return ctx
```

**Classes:** `.orca-person-grid`

**Principles applied:** Practical UI L11: Align the layout with a responsive grid; Jakob's law: work the way products people already know work; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Person-block grid

---

## Marketing page layout

`id: marketing-layout` · level: template · source: ORCA

The public site frame: site header with navigation and actions, full-width sections, and a footer with link columns.

Built from: `site-header`, `marketing-hero`, `feature-grid`, `footer`

### Why

Public pages are scanned, not used: a familiar header, generous sections and a footer of links meet expectations (Jakob's law, Aesthetic–usability effect). One primary call to action per screen (Von Restorff).

### When to use

- Landing, product, pricing and other public pages.

### How to use

- Extend it: `{% extends "orca/layouts/marketing.html" %}`, then fill only the blocks you need.
- Fill `content` with marketing sections (hero, feature grid, story, factoid); wrap non-full-width sections in `.orca-container`.
- Pass `site_nav` and `footer_cols`; put sign-in and the main call to action in `header_actions`.

Extend: `{% extends "orca/layouts/marketing.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `header_actions`, `content`, `footer`, `legal`

### Context it reads

- `site_nav` (label, url, current), `footer_cols` (title, links).
- `title`.

#### Example: Child template

```django
{% extends "orca/layouts/marketing.html" %}{% load orca static %}
{% block header_actions %}<a class="orca-button orca-button--ghost" href="#">Sign in</a><a class="orca-button orca-button--brand" href="#">Main action</a>{% endblock %}
{% block content %}
<section class="orca-marketing-hero"><div class="orca-hero">
  <div class="orca-hero__text"><p class="orca-card-kicker">Kicker</p><h1 class="orca-hero__title">Headline: the benefit in under ten words.</h1><p class="orca-hero__lead">Lead: one or two sentences that explain the headline.</p>
    <div class="orca-row"><a class="orca-button orca-button--brand" href="#">Main action</a><a class="orca-button" href="#">Second action</a></div></div>
  <div class="orca-hero__media"><img src="{% static "orca/img/sample-street.svg" %}" alt="Product picture"></div></div></section>
<div class="orca-container"><ul class="orca-feature-grid">{% for i in "123" %}<li class="orca-feature">{% icon "success" size="l" %}<h2 class="orca-feature__title">Feature title</h2><p class="orca-feature__text">One sentence about the feature and its benefit.</p></li>{% endfor %}</ul></div>
{% endblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# site/views.py
from django.views.generic import TemplateView


class Pricing(TemplateView):
    template_name = "site/pricing.html"   # {% extends "orca/layouts/marketing.html" %}
    extra_context = {
        "title": "Pricing",
        "site_nav": [{"label": "Product", "url": "/"}, {"label": "Pricing", "url": "/pricing/", "current": True},
                     {"label": "Docs", "url": "/docs/"}],
        "footer_cols": [{"title": "Product", "links": [{"label": "Features", "url": "/"}, {"label": "Pricing", "url": "/pricing/"}]},
                        {"title": "Help", "links": [{"label": "Documentation", "url": "/docs/"}]}],
    }
```

**Classes:** `.orca-marketing-main`, `.orca-marketing-page`, `.orca-container`

**Principles applied:** Jakob's law: work the way products people already know work; Aesthetic–usability effect: consistent, careful visuals earn trust; Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly

**ORCA guide items covered:** Marketing page layout; Marketing landing page

---

## Blog page layout

`id: blog-layout` · level: template · source: ORCA

A long-form page that reads well: breadcrumbs, title, introduction, version and last update, sections in a measured reading column, and an "On this page" column on the right.

Built from: `docs-page-header`, `table-of-contents`, `top-bar`

### Why

Long text is read, not scanned: a front-loaded introduction (Practical UI W05), a line length near 70 characters (T09) and a contents column that shows where you are (Miller's law) let people read comfortably on any screen, and a centred column never stretches across a large window. Version and last update tell the reader whether to trust the page.

### When to use

- Articles, guides, documentation pages, release notes, case studies and policies: any page that is mostly sections of text.

### How to use

- Extend it: `{% extends "orca/layouts/blog.html" %}`, then fill only the blocks you need.
- Pass `title`, `subtitle` (the introduction: one or two sentences), `version` and `updated` (a date); optional `kicker`, `author`, `reading_time` (minutes), `breadcrumbs`.
- Fill `blog_body` with sections: each `<section>` has an `h2.orca-section-title` with an `id`. The contents column is built from those `h2` headings, or pass `toc` (`[{"id", "label"}]`) to write it yourself.
- Indexes, tables and galleries that need the full width: add `{% block blog_modifier %} orca-blog--wide{% endblock %}`; the head keeps its reading width.
- The page has the app shell's top bar and sidebar (`nav`, or your own `sidebar` block); the Docs page layout is this layout with a documentation sidebar.

Extend: `{% extends "orca/layouts/blog.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `messages`, `blog_modifier`, `breadcrumbs`, `blog_kicker`, `page_title`, `page_subtitle`, `blog_meta`, `page_actions`, `blog_body`, `blog_footer`, `blog_aside`, `blog_toc`, `content`, `footer`

### Context it reads

- `title`, `subtitle` (introduction), `kicker`, `breadcrumbs`.
- `version`, `updated` (a date), `author`, `reading_time`: shown as the meta line when present.
- `toc`: optional contents `[{"id", "label"}]`; without it the `h2` headings of the body are listed.

#### Example: Child template

```django
{% extends "orca/layouts/blog.html" %}
{% block blog_body %}<section class="orca-vstack orca-vstack--tight" aria-labelledby="section-one">
  <h2 class="orca-section-title" id="section-one">Section one</h2>
  <p class="orca-p">Body text of the page. Keep paragraphs short and lead with what the reader needs; the column stays about 70 characters wide, however large the window.</p>
  <p class="orca-p">More body text, with <code class="orca-code">inline code</code> and a <a class="orca-link" href="#">link to another page</a>.</p>
</section>
<section class="orca-vstack orca-vstack--tight" aria-labelledby="section-two">
  <h2 class="orca-section-title" id="section-two">Section two</h2>
  <p class="orca-p">Each section starts with an <code class="orca-code">h2</code> that has an <code class="orca-code">id</code>, so the contents column can link to it.</p>
  <div class="orca-code-block"><div class="orca-code-block__head"><span>Shell</span></div><pre><code>pip install example</code></pre></div>
</section>
<section class="orca-vstack orca-vstack--tight" aria-labelledby="section-three">
  <h2 class="orca-section-title" id="section-three">Section three</h2>
  <p class="orca-p">Close with what to do next.</p>
</section>{% endblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# blog/views.py
from datetime import date

from django.views.generic import TemplateView


class PostDetail(TemplateView):
    template_name = "blog/post.html"   # {% extends "orca/layouts/blog.html" %}, sections in {% block blog_body %}

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(title="How we count visitors", kicker="Case study",
                   subtitle="Two sentences that say what this page covers and who it is for.",
                   version="1.2.0", updated=date(2026, 11, 6), author="Person name", reading_time=4,
                   breadcrumbs=[("Blog", "/blog/"), ("How we count visitors", "")])
        return ctx
```

**Classes:** `.orca-blog`, `.orca-blog--wide`, `.orca-blog__article`, `.orca-blog__head`, `.orca-blog__intro`, `.orca-blog__meta`, `.orca-blog__body`, `.orca-blog__aside`, `.orca-blog-page`

**Principles applied:** Practical UI W05: Order explanations as an inverted pyramid; Practical UI T09: Limit reading measure; Miller's law: chunk information so working memory is not overloaded; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Blog page layout; Blog page

---

## Docs page layout

`id: docs-layout` · level: template · source: ORCA

The Blog page with a documentation sidebar: a filter and a page tree on the left, the reading column and "On this page" on the right.

Built from: `docs-sidebar`, `docs-page-header`, `top-bar`

### Why

Documentation readers both browse and look up (Miller's law, Hick's law): a filterable tree supports both, and the Blog page's measured reading column keeps long text comfortable (Practical UI T09, W05).

### When to use

- Product documentation, help centres, internal handbooks.

### How to use

- Extend it: `{% extends "orca/layouts/docs.html" %}`, then fill only the blocks you need.
- Pass `docs_nav` (sections with `label`, `icon`, `open` and `items`: label, url, current), `title`, `subtitle`, `version`, `updated` and `breadcrumbs`; fill `blog_body`.
- First-level sections lead with an `icon` and end with a small chevron that shows open or closed.
- This documentation site uses the same structure with the sidebar pattern.

Extend: `{% extends "orca/layouts/docs.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `messages`, `blog_modifier`, `breadcrumbs`, `blog_kicker`, `page_title`, `page_subtitle`, `blog_meta`, `page_actions`, `blog_body`, `blog_footer`, `blog_aside`, `blog_toc`, `content`, `footer`

### Context it reads

- `docs_nav`, `title`, `subtitle`, `version`, `updated`, `breadcrumbs`.

#### Example: Child template

```django
{% extends "orca/layouts/docs.html" %}
{% block blog_body %}<section class="orca-vstack orca-vstack--tight" aria-labelledby="s-one">
  <h2 class="orca-section-title" id="s-one">Section heading</h2>
  <p class="orca-p">Body text of the page. Keep paragraphs short and lead with what the reader needs.</p>
  <p class="orca-p">More body text, with <code class="orca-code">inline code</code> and a <a class="orca-link" href="#">link to another page</a>.</p>
</section>
<section class="orca-vstack orca-vstack--tight" aria-labelledby="s-two">
  <h2 class="orca-section-title" id="s-two">Another section</h2>
  <div class="orca-code-block"><div class="orca-code-block__head"><span>Shell</span></div><pre><code>pip install example</code></pre></div>
</section>{% endblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# docs/views.py
from datetime import date

from django.views.generic import TemplateView


class DocsPage(TemplateView):
    template_name = "docs/page.html"   # {% extends "orca/layouts/docs.html" %}, sections in {% block blog_body %}

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        here = self.request.path
        sections = {"Get started": ("book", [("Installation", "/docs/install/"), ("Usage", "/docs/usage/")]),
                    "Guides": ("repository", [("Uploads", "/docs/uploads/"), ("Sharing", "/docs/sharing/")])}
        ctx["docs_nav"] = [{"label": label, "icon": icon, "open": any(url == here for _, url in items),
                            "items": [{"label": t, "url": url, "current": url == here} for t, url in items]}
                           for label, (icon, items) in sections.items()]
        ctx.update(title="Uploads", subtitle="Add videos one by one or in bulk.", version="1.2.0", updated=date(2026, 11, 6),
                   breadcrumbs=[("Docs", "/docs/"), ("Uploads", "")])
        return ctx
```

**Classes:** `.orca-docs-sidebar`, `.orca-docs-page`, `.orca-blog`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Hick's law: fewer, clearer choices mean faster decisions; Practical UI T09: Limit reading measure; Practical UI W05: Order explanations as an inverted pyramid

**ORCA guide items covered:** Docs page layout; Docs page

---

## Generic list template

`id: generic-list` · level: template · source: ORCA

A list page from a ListView: title and Add button, optional filter panel, list header with count and search, a table that becomes cards on phones, pagination and the right empty state.

Built from: `app-shell`, `list-header`, `data-table`, `filter-drawer`, `no-results`

### Why

Most screens of a business application are lists; one template that is always right (sortable header, row actions, empty and no-match states, phone cards) removes repeated decisions and keeps every list familiar (Jakob's law, Tesler's law).

### When to use

- Any ListView: records people find, compare and open.

### How to use

- Extend it: `{% extends "orca/generic/list.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Set `template_name = "orca/generic/list.html"`, `list_columns` and `paginate_by`; filter the queryset on `request.GET["q"]` for the search box.
- Pass a `filter_form` (a GET form) to get the filter panel; override `list` to change the rows completely, `list_actions` for the buttons.

Extend: `{% extends "orca/generic/list.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `list_actions`, `filter_panel`, `list_header`, `list`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `object_list`, `page_obj`, `paginator` (from ListView).
- `columns`: `[{"label", "name", "numeric"}]`.
- `create_url`, `detail_url_name`, `update_url_name`, `delete_url_name` (URL names taking the object's pk), `cancel_url`.
- `filter_form`, `empty_title`, `empty_text`.

#### Example: Child template

```django
{% extends "orca/generic/list.html" %}
{% comment %}A ListView with OrcaPageMixin needs no blocks at all; this preview only adds a filter form (filter_form).{% endcomment %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Views

```python
# videos/views.py
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from orca.mixins import OrcaPageMixin

from .models import Video


class VideoPages(OrcaPageMixin):
    """What every video page shares: the model and the URL names the templates link to."""

    model = Video
    list_url_name, detail_url_name, create_url_name = "video-list", "video-detail", "video-create"
    update_url_name, delete_url_name = "video-update", "video-delete"


class VideoList(VideoPages, ListView):
    template_name = "orca/generic/list.html"
    paginate_by = 25
    list_columns = ["title", "album", "status", ("Views today", "views_today")]
    extra_context = {"empty_title": "No videos yet", "empty_text": "Add your first video to start your library."}


class VideoDetail(VideoPages, DetailView):
    template_name = "orca/generic/detail.html"
    detail_fields = ["title", "album", "status", "recorded_on", ("Length", "duration_text")]

    def get_title(self, obj=None):
        return str(obj)


class VideoCreate(VideoPages, SuccessMessageMixin, CreateView):
    template_name = "orca/generic/form.html"
    fields = ["title", "album", "recorded_on"]
    title = "New video"
    success_message = "Video “%(title)s” added."
    extra_context = {"submit_label": "Add video"}


class VideoUpdate(VideoPages, SuccessMessageMixin, UpdateView):
    template_name = "orca/generic/form.html"
    fields = ["title", "album", "recorded_on"]
    success_message = "Video “%(title)s” saved."
    extra_context = {"submit_label": "Save video"}

    def get_title(self, obj=None):
        return f"Edit {obj}"


class VideoDelete(VideoPages, DeleteView):
    template_name = "orca/generic/confirm_delete.html"
    success_url = reverse_lazy("video-list")
    # `blocked_by` (protected or restricted related objects) is filled by the mixin.
    extra_context = {"deleted": ["its chapters", "its share links"], "kept": ["the album"], "submit_label": "Delete video"}

    def get_title(self, obj=None):
        return f"Delete {obj}?"

    def form_valid(self, form):
        messages.success(self.request, f"Video “{self.object}” deleted.")
        return super().form_valid(form)
```

#### URLs

```python
# videos/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("videos/", views.VideoList.as_view(), name="video-list"),
    path("videos/new/", views.VideoCreate.as_view(), name="video-create"),
    path("videos/<int:pk>/", views.VideoDetail.as_view(), name="video-detail"),
    path("videos/<int:pk>/edit/", views.VideoUpdate.as_view(), name="video-update"),
    path("videos/<int:pk>/delete/", views.VideoDelete.as_view(), name="video-delete"),
]
```

#### Filters (optional)

```python
# videos/forms.py
from django import forms

from .models import Album, Video


class VideoFilterForm(forms.Form):
    q = forms.CharField(label="Title contains", required=False)
    album = forms.ModelChoiceField(Album.objects.all(), required=False, empty_label="Any album")
    status = forms.MultipleChoiceField(choices=Video.Status.choices, required=False,
                                       widget=forms.CheckboxSelectMultiple)


# videos/views.py
from django.views.generic import ListView

from orca.mixins import OrcaPageMixin

from .forms import VideoFilterForm
from .models import Video


class VideoList(OrcaPageMixin, ListView):
    model = Video
    paginate_by = 25
    template_name = "orca/generic/list.html"   # or "orca/layouts/simple_data.html"
    list_columns = ["title", "album", "status", ("Views today", "views_today")]
    detail_url_name, create_url_name = "video-detail", "video-create"

    def get_queryset(self):
        qs = super().get_queryset()
        self.filter_form = VideoFilterForm(self.request.GET or None)
        if self.filter_form.is_valid():
            data = self.filter_form.cleaned_data
            if data["q"]:
                qs = qs.filter(title__icontains=data["q"])
            if data["album"]:
                qs = qs.filter(album=data["album"])
            if data["status"]:
                qs = qs.filter(status__in=data["status"])
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # The template puts the Filters button in the page actions and the form in the right drawer.
        ctx["filter_form"] = self.filter_form
        data = self.filter_form.cleaned_data if self.filter_form.is_valid() else {}
        ctx["active_filters"] = sum(1 for value in data.values() if value)
        return ctx
```

**Classes:** `.orca-list-layout`

**Principles applied:** Jakob's law: work the way products people already know work; Tesler's law: move unavoidable complexity from the user to the system; Miller's law: chunk information so working memory is not overloaded; Practical UI L14: Reduce travel between related actions

**ORCA guide items covered:** Generic list template; List page

---

## Generic detail template

`id: generic-detail` · level: template · source: ORCA

A record page from a DetailView: title, Edit and Delete actions, and the record's fields as a key–value list.

Built from: `app-shell`, `detail-panel`

### Why

Details read top to bottom as label and value pairs (Practical UI L01); Edit and Delete in the same place on every record make them findable without searching (Jakob's law).

### When to use

- Any DetailView: one record with its properties.

### How to use

- Extend it: `{% extends "orca/generic/detail.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Set `detail_fields`; add related lists or history in `detail_extra`, change the buttons in `detail_actions`.

Extend: `{% extends "orca/generic/detail.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `detail_actions`, `detail`, `detail_extra`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `object`, `fields`, `update_url`, `delete_url`.

#### Example: Child template

```django
{% extends "orca/generic/detail.html" %}{% load orca %}
{% block detail_extra %}<section class="orca-panel" aria-labelledby="d-notes"><h2 class="orca-panel-title" id="d-notes">Related section</h2><p class="orca-p orca-muted">Extra panels go in the detail_extra block.</p></section>{% endblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Views

```python
# videos/views.py
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from orca.mixins import OrcaPageMixin

from .models import Video


class VideoPages(OrcaPageMixin):
    """What every video page shares: the model and the URL names the templates link to."""

    model = Video
    list_url_name, detail_url_name, create_url_name = "video-list", "video-detail", "video-create"
    update_url_name, delete_url_name = "video-update", "video-delete"


class VideoList(VideoPages, ListView):
    template_name = "orca/generic/list.html"
    paginate_by = 25
    list_columns = ["title", "album", "status", ("Views today", "views_today")]
    extra_context = {"empty_title": "No videos yet", "empty_text": "Add your first video to start your library."}


class VideoDetail(VideoPages, DetailView):
    template_name = "orca/generic/detail.html"
    detail_fields = ["title", "album", "status", "recorded_on", ("Length", "duration_text")]

    def get_title(self, obj=None):
        return str(obj)


class VideoCreate(VideoPages, SuccessMessageMixin, CreateView):
    template_name = "orca/generic/form.html"
    fields = ["title", "album", "recorded_on"]
    title = "New video"
    success_message = "Video “%(title)s” added."
    extra_context = {"submit_label": "Add video"}


class VideoUpdate(VideoPages, SuccessMessageMixin, UpdateView):
    template_name = "orca/generic/form.html"
    fields = ["title", "album", "recorded_on"]
    success_message = "Video “%(title)s” saved."
    extra_context = {"submit_label": "Save video"}

    def get_title(self, obj=None):
        return f"Edit {obj}"


class VideoDelete(VideoPages, DeleteView):
    template_name = "orca/generic/confirm_delete.html"
    success_url = reverse_lazy("video-list")
    # `blocked_by` (protected or restricted related objects) is filled by the mixin.
    extra_context = {"deleted": ["its chapters", "its share links"], "kept": ["the album"], "submit_label": "Delete video"}

    def get_title(self, obj=None):
        return f"Delete {obj}?"

    def form_valid(self, form):
        messages.success(self.request, f"Video “{self.object}” deleted.")
        return super().form_valid(form)
```

#### URLs

```python
# videos/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("videos/", views.VideoList.as_view(), name="video-list"),
    path("videos/new/", views.VideoCreate.as_view(), name="video-create"),
    path("videos/<int:pk>/", views.VideoDetail.as_view(), name="video-detail"),
    path("videos/<int:pk>/edit/", views.VideoUpdate.as_view(), name="video-update"),
    path("videos/<int:pk>/delete/", views.VideoDelete.as_view(), name="video-delete"),
]
```

**Principles applied:** Practical UI L01: Group related information; Jakob's law: work the way products people already know work; Practical UI B08: Keep action order predictable

**ORCA guide items covered:** Generic detail template; Detail page

---

## Generic form template

`id: generic-form` · level: template · source: ORCA

A create or edit page from a CreateView or UpdateView: one column of ORCA fields with the error summary and Save and Cancel.

Built from: `app-shell`, `narrow-form`

### Why

One column is the fastest form to fill (Practical UI R01); the error summary and inline errors from `orca_form_errors` and `orca_field` make every form recover the same way (W15).

### When to use

- Any CreateView or UpdateView; any page whose main job is one form.

### How to use

- Extend it: `{% extends "orca/generic/form.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Add help text on the model or form field: it is shown under the label. Use `form_fields` to group fields in form sections.

Extend: `{% extends "orca/generic/form.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `form_fields`, `form_actions`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `form`, `object` (when editing), `submit_label`, `cancel_url`.

#### Example: Child template

```django
{% extends "orca/generic/form.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Views

```python
# videos/views.py
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from orca.mixins import OrcaPageMixin

from .models import Video


class VideoPages(OrcaPageMixin):
    """What every video page shares: the model and the URL names the templates link to."""

    model = Video
    list_url_name, detail_url_name, create_url_name = "video-list", "video-detail", "video-create"
    update_url_name, delete_url_name = "video-update", "video-delete"


class VideoList(VideoPages, ListView):
    template_name = "orca/generic/list.html"
    paginate_by = 25
    list_columns = ["title", "album", "status", ("Views today", "views_today")]
    extra_context = {"empty_title": "No videos yet", "empty_text": "Add your first video to start your library."}


class VideoDetail(VideoPages, DetailView):
    template_name = "orca/generic/detail.html"
    detail_fields = ["title", "album", "status", "recorded_on", ("Length", "duration_text")]

    def get_title(self, obj=None):
        return str(obj)


class VideoCreate(VideoPages, SuccessMessageMixin, CreateView):
    template_name = "orca/generic/form.html"
    fields = ["title", "album", "recorded_on"]
    title = "New video"
    success_message = "Video “%(title)s” added."
    extra_context = {"submit_label": "Add video"}


class VideoUpdate(VideoPages, SuccessMessageMixin, UpdateView):
    template_name = "orca/generic/form.html"
    fields = ["title", "album", "recorded_on"]
    success_message = "Video “%(title)s” saved."
    extra_context = {"submit_label": "Save video"}

    def get_title(self, obj=None):
        return f"Edit {obj}"


class VideoDelete(VideoPages, DeleteView):
    template_name = "orca/generic/confirm_delete.html"
    success_url = reverse_lazy("video-list")
    # `blocked_by` (protected or restricted related objects) is filled by the mixin.
    extra_context = {"deleted": ["its chapters", "its share links"], "kept": ["the album"], "submit_label": "Delete video"}

    def get_title(self, obj=None):
        return f"Delete {obj}?"

    def form_valid(self, form):
        messages.success(self.request, f"Video “{self.object}” deleted.")
        return super().form_valid(form)
```

#### URLs

```python
# videos/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("videos/", views.VideoList.as_view(), name="video-list"),
    path("videos/new/", views.VideoCreate.as_view(), name="video-create"),
    path("videos/<int:pk>/", views.VideoDetail.as_view(), name="video-detail"),
    path("videos/<int:pk>/edit/", views.VideoUpdate.as_view(), name="video-update"),
    path("videos/<int:pk>/delete/", views.VideoDelete.as_view(), name="video-delete"),
]
```

**Principles applied:** Practical UI R01: Keep the main form flow in one column; Practical UI W15: Help people recover from errors; Practical UI R09: Persistent labels, not placeholders

**ORCA guide items covered:** Generic form template; Form page

---

## Generic confirm (delete) template

`id: generic-confirm-delete` · level: template · source: ORCA

The delete confirmation from a DeleteView: what will be deleted, what is kept, a danger button and Cancel; or, when other records still use it, why it cannot be deleted yet.

Built from: `app-shell`, `confirm-action-panel`, `delete-blocked-notice`

### Why

Deleting is the most costly mistake, so friction scales with it (Practical UI B13): consequences in words, the danger button named after the action. When related records protect it, saying which ones turns a dead end into a task (W15).

### When to use

- Any DeleteView; any page confirming a destructive action.

### How to use

- Extend it: `{% extends "orca/generic/confirm_delete.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`. On a DeleteView it also fills `blocked_by` from protected and restricted foreign keys.
- Pass `deleted` (a list) and `kept` (a sentence); `confirm_text` adds a required 'I understand' checkbox for severe deletes.

Extend: `{% extends "orca/generic/confirm_delete.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `consequences`, `blocked_actions`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `object`, `deleted`, `kept`, `confirm_text`, `blocked_by`, `submit_label`, `cancel_url`.

#### Example: Child template

```django
{% extends "orca/generic/confirm_delete.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Views

```python
# videos/views.py
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from orca.mixins import OrcaPageMixin

from .models import Video


class VideoPages(OrcaPageMixin):
    """What every video page shares: the model and the URL names the templates link to."""

    model = Video
    list_url_name, detail_url_name, create_url_name = "video-list", "video-detail", "video-create"
    update_url_name, delete_url_name = "video-update", "video-delete"


class VideoList(VideoPages, ListView):
    template_name = "orca/generic/list.html"
    paginate_by = 25
    list_columns = ["title", "album", "status", ("Views today", "views_today")]
    extra_context = {"empty_title": "No videos yet", "empty_text": "Add your first video to start your library."}


class VideoDetail(VideoPages, DetailView):
    template_name = "orca/generic/detail.html"
    detail_fields = ["title", "album", "status", "recorded_on", ("Length", "duration_text")]

    def get_title(self, obj=None):
        return str(obj)


class VideoCreate(VideoPages, SuccessMessageMixin, CreateView):
    template_name = "orca/generic/form.html"
    fields = ["title", "album", "recorded_on"]
    title = "New video"
    success_message = "Video “%(title)s” added."
    extra_context = {"submit_label": "Add video"}


class VideoUpdate(VideoPages, SuccessMessageMixin, UpdateView):
    template_name = "orca/generic/form.html"
    fields = ["title", "album", "recorded_on"]
    success_message = "Video “%(title)s” saved."
    extra_context = {"submit_label": "Save video"}

    def get_title(self, obj=None):
        return f"Edit {obj}"


class VideoDelete(VideoPages, DeleteView):
    template_name = "orca/generic/confirm_delete.html"
    success_url = reverse_lazy("video-list")
    # `blocked_by` (protected or restricted related objects) is filled by the mixin.
    extra_context = {"deleted": ["its chapters", "its share links"], "kept": ["the album"], "submit_label": "Delete video"}

    def get_title(self, obj=None):
        return f"Delete {obj}?"

    def form_valid(self, form):
        messages.success(self.request, f"Video “{self.object}” deleted.")
        return super().form_valid(form)
```

#### URLs

```python
# videos/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("videos/", views.VideoList.as_view(), name="video-list"),
    path("videos/new/", views.VideoCreate.as_view(), name="video-create"),
    path("videos/<int:pk>/", views.VideoDetail.as_view(), name="video-detail"),
    path("videos/<int:pk>/edit/", views.VideoUpdate.as_view(), name="video-update"),
    path("videos/<int:pk>/delete/", views.VideoDelete.as_view(), name="video-delete"),
]
```

**Principles applied:** Practical UI B13: Scale friction to the consequence; Practical UI W15: Help people recover from errors; Practical UI B10: Name the action clearly

**ORCA guide items covered:** Generic confirm (delete) template; Confirm page

---

## Generic confirm-action template

`id: generic-confirm-action` · level: template · source: ORCA

A confirmation page for any consequential action that is not a delete: archive, send, disable, run.

Built from: `app-shell`, `confirm-action-panel`

### Why

A separate page with the consequences listed gives people a moment to check (Practical UI B13) without the alarm of a danger colour when nothing is lost.

### When to use

- Actions with wide effects that need a second look: send to everyone, disable a site, start a long run.

### How to use

- Extend it: `{% extends "orca/generic/confirm_action.html" %}`, then fill only the blocks you need.
- Pass `title` (a question), `text`, `items` and `submit_label` (the verb); set `danger=True` only when something is lost.
- Add a `form` for an optional reason or choice.

Extend: `{% extends "orca/generic/confirm_action.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `consequences`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `title`, `text`, `items`, `form`, `danger`, `submit_label`, `cancel_url`.

#### Example: Child template

```django
{% extends "orca/generic/confirm_action.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### View

```python
# videos/views.py
from django import forms
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import FormView

from .models import Album


class ArchiveForm(forms.Form):
    reason = forms.CharField(required=False, label="Reason (optional)")


class ArchiveAlbum(FormView):
    template_name = "orca/generic/confirm_action.html"
    form_class = ArchiveForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        album = get_object_or_404(Album, pk=self.kwargs["pk"])
        ctx.update(title=f"Archive {album}?", text="Its videos stay available by link but leave the library.",
                   items=[str(v) for v in album.videos.all()[:10]], danger=False,
                   submit_label="Archive album", cancel_url=album.get_absolute_url())
        return ctx

    def form_valid(self, form):
        album = get_object_or_404(Album, pk=self.kwargs["pk"])
        album.archive(reason=form.cleaned_data["reason"])
        messages.success(self.request, f"Album “{album}” archived.")
        return redirect("album-list")
```

**Principles applied:** Practical UI B13: Scale friction to the consequence; Practical UI B10: Name the action clearly; Practical UI W04: Lead with the information people seek

**ORCA guide items covered:** Generic confirm-action template

---

## Parent base template

`id: parent-base` · level: template · source: ORCA

The frame shared by every page of a parent record: its title and actions, optional summary stats, and tabs for the overview and each child list.

Built from: `parent-child-tabs`

### Why

Keeping the parent's header and tabs fixed while the tab content changes tells people where they are and what else the record holds (Practical UI L05, Jakob's law).

### When to use

- Records that own other records: a site and its videos, a project and its tasks.

### How to use

- Extend it: `{% extends "orca/generic/parent_base.html" %}`, then fill only the blocks you need.
- Extend it for each tab and fill `child_content`; mark the current tab in `parent_tabs`.
- Each tab is its own URL (and view), so tabs can be linked, bookmarked and refreshed.

Extend: `{% extends "orca/generic/parent_base.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `parent_summary`, `parent_tabs`, `detail_actions`, `child_content`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `parent`: the parent object (its title heads every tab).
- `parent_tabs`: `[{"label", "url", "count", "current"}]`, Overview first.
- `parent_stats`: optional `[{"label", "value"}]` shown above the tabs; `parent_update_url`.

#### Example: Child template

```django
{% extends "orca/generic/parent_base.html" %}
{% block child_content %}<section class="orca-panel" aria-label="Tab content"><div class="orca-skeleton orca-skeleton--title" style="max-width: 14rem"></div><div class="orca-skeleton orca-skeleton--text"></div><div class="orca-skeleton orca-skeleton--text" style="max-width: 60%"></div></section>{% endblock %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Parent mixin and views

```python
# videos/views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView

from orca.mixins import OrcaPageMixin

from .models import Album, Video


class AlbumTabs(OrcaPageMixin):
    """The parent (an album) and its tabs, for every page under /albums/<album_pk>/."""

    def get_parent(self):
        return get_object_or_404(Album, pk=self.kwargs["album_pk"])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        album = ctx["parent"] = self.get_parent()
        here = self.request.path
        tabs = [("Overview", reverse("album-detail", args=[album.pk]), None),
                ("Videos", reverse("album-videos", args=[album.pk]), album.videos.count())]
        ctx["parent_tabs"] = [{"label": label, "url": url, "count": count, "current": here == url} for label, url, count in tabs]
        ctx["parent_stats"] = [{"label": "Videos", "value": album.videos.count(), "icon": "play"},
                               {"label": "Last change", "value": album.updated_at.strftime("%-d %b"), "icon": "history"}]
        ctx["parent_update_url"] = reverse("album-update", args=[album.pk])
        return ctx


class AlbumDetail(AlbumTabs, DetailView):
    model = Album
    pk_url_kwarg = "album_pk"
    template_name = "orca/generic/parent_detail.html"
    detail_fields = ["title", "owner", "created_at"]


class AlbumVideos(AlbumTabs, ListView):
    model = Video
    template_name = "orca/generic/child_list.html"
    paginate_by = 25
    list_columns = ["title", "status", "recorded_on"]
    detail_url_name, create_url_name = "video-detail", "album-video-create"

    def get_queryset(self):
        return super().get_queryset().filter(album_id=self.kwargs["album_pk"])
```

**Classes:** `.orca-parent__panel`

**Principles applied:** Practical UI L05: Use depth to support navigation and priority; Jakob's law: work the way products people already know work; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Parent base template

---

## Parent detail template

`id: parent-detail` · level: template · source: ORCA

The parent's Overview tab: its fields as a key–value list, with room for more overview panels.

Built from: `parent-base`, `detail-panel`

### Why

The overview answers 'what is this record' before any child list (Practical UI W04), so the first tab is always the parent itself.

### When to use

- The first tab of a parent record.

### How to use

- Extend it: `{% extends "orca/generic/parent_detail.html" %}`, then fill only the blocks you need.
- Pass `fields` (or use OrcaPageMixin's `detail_fields`); add panels in `overview_extra`.

Extend: `{% extends "orca/generic/parent_detail.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `parent_summary`, `parent_tabs`, `detail_actions`, `child_content`, `overview`, `overview_extra`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `parent`: the parent object (its title heads every tab).
- `parent_tabs`: `[{"label", "url", "count", "current"}]`, Overview first.
- `parent_stats`: optional `[{"label", "value"}]` shown above the tabs; `parent_update_url`.
- `fields`.

#### Example: Child template

```django
{% extends "orca/generic/parent_detail.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Parent mixin and views

```python
# videos/views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView

from orca.mixins import OrcaPageMixin

from .models import Album, Video


class AlbumTabs(OrcaPageMixin):
    """The parent (an album) and its tabs, for every page under /albums/<album_pk>/."""

    def get_parent(self):
        return get_object_or_404(Album, pk=self.kwargs["album_pk"])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        album = ctx["parent"] = self.get_parent()
        here = self.request.path
        tabs = [("Overview", reverse("album-detail", args=[album.pk]), None),
                ("Videos", reverse("album-videos", args=[album.pk]), album.videos.count())]
        ctx["parent_tabs"] = [{"label": label, "url": url, "count": count, "current": here == url} for label, url, count in tabs]
        ctx["parent_stats"] = [{"label": "Videos", "value": album.videos.count(), "icon": "play"},
                               {"label": "Last change", "value": album.updated_at.strftime("%-d %b"), "icon": "history"}]
        ctx["parent_update_url"] = reverse("album-update", args=[album.pk])
        return ctx


class AlbumDetail(AlbumTabs, DetailView):
    model = Album
    pk_url_kwarg = "album_pk"
    template_name = "orca/generic/parent_detail.html"
    detail_fields = ["title", "owner", "created_at"]


class AlbumVideos(AlbumTabs, ListView):
    model = Video
    template_name = "orca/generic/child_list.html"
    paginate_by = 25
    list_columns = ["title", "status", "recorded_on"]
    detail_url_name, create_url_name = "video-detail", "album-video-create"

    def get_queryset(self):
        return super().get_queryset().filter(album_id=self.kwargs["album_pk"])
```

**Principles applied:** Practical UI W04: Lead with the information people seek; Practical UI L01: Group related information

**ORCA guide items covered:** Parent detail template (tabbed); Parent detail page (overview + child tabs)

---

## Parent-child list template

`id: parent-child-list` · level: template · source: ORCA

A child list inside a parent tab: header with count and 'Add … to parent', the table, pagination and an empty state naming the parent.

Built from: `parent-base`, `child-list-tab`

### Why

Naming the parent in the add button and the empty state ('No videos for North building') removes any doubt about where a new record goes (Practical UI W04, B10).

### When to use

- Each child tab of a parent record. The four parent-child templates (list, detail, form, confirm) make up its pages.

### How to use

- Extend it: `{% extends "orca/generic/child_list.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Filter the queryset by the parent from the URL; pass `parent` and `parent_tabs` with this tab current.

Extend: `{% extends "orca/generic/child_list.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `parent_summary`, `parent_tabs`, `detail_actions`, `child_content`, `list_actions`, `list`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `parent`: the parent object (its title heads every tab).
- `parent_tabs`: `[{"label", "url", "count", "current"}]`, Overview first.
- `parent_stats`: optional `[{"label", "value"}]` shown above the tabs; `parent_update_url`.
- `object_list`, `page_obj`, `columns`.
- `create_url`, `detail_url_name`, `update_url_name`, `delete_url_name` (URL names taking the object's pk), `cancel_url`.

#### Example: Child template

```django
{% extends "orca/generic/child_list.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Parent mixin and views

```python
# videos/views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView

from orca.mixins import OrcaPageMixin

from .models import Album, Video


class AlbumTabs(OrcaPageMixin):
    """The parent (an album) and its tabs, for every page under /albums/<album_pk>/."""

    def get_parent(self):
        return get_object_or_404(Album, pk=self.kwargs["album_pk"])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        album = ctx["parent"] = self.get_parent()
        here = self.request.path
        tabs = [("Overview", reverse("album-detail", args=[album.pk]), None),
                ("Videos", reverse("album-videos", args=[album.pk]), album.videos.count())]
        ctx["parent_tabs"] = [{"label": label, "url": url, "count": count, "current": here == url} for label, url, count in tabs]
        ctx["parent_stats"] = [{"label": "Videos", "value": album.videos.count(), "icon": "play"},
                               {"label": "Last change", "value": album.updated_at.strftime("%-d %b"), "icon": "history"}]
        ctx["parent_update_url"] = reverse("album-update", args=[album.pk])
        return ctx


class AlbumDetail(AlbumTabs, DetailView):
    model = Album
    pk_url_kwarg = "album_pk"
    template_name = "orca/generic/parent_detail.html"
    detail_fields = ["title", "owner", "created_at"]


class AlbumVideos(AlbumTabs, ListView):
    model = Video
    template_name = "orca/generic/child_list.html"
    paginate_by = 25
    list_columns = ["title", "status", "recorded_on"]
    detail_url_name, create_url_name = "video-detail", "album-video-create"

    def get_queryset(self):
        return super().get_queryset().filter(album_id=self.kwargs["album_pk"])
```

**Principles applied:** Practical UI W04: Lead with the information people seek; Practical UI B10: Name the action clearly; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Parent-child list template; Parent-child pages (list, detail, form, confirm)

---

## Parent-child detail template

`id: parent-child-detail` · level: template · source: ORCA

One child record inside its parent's tab: a back link to the list, Edit and Delete, and the record's fields.

Built from: `parent-base`, `top-actions-header`, `detail-panel`

### Why

The back link and the parent's header keep the path home visible (Jakob's law); the child's own actions sit next to its title (Practical UI L14).

### When to use

- Opening a child record without leaving its parent.

### How to use

- Extend it: `{% extends "orca/generic/child_detail.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Pass `list_url` for the back link; `detail` overrides the field list.

Extend: `{% extends "orca/generic/child_detail.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `parent_summary`, `parent_tabs`, `detail_actions`, `child_content`, `detail_actions`, `detail`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `parent`: the parent object (its title heads every tab).
- `parent_tabs`: `[{"label", "url", "count", "current"}]`, Overview first.
- `parent_stats`: optional `[{"label", "value"}]` shown above the tabs; `parent_update_url`.
- `object`, `fields`, `list_url`, `update_url`, `delete_url`.

#### Example: Child template

```django
{% extends "orca/generic/child_detail.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Parent mixin and views

```python
# videos/views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView

from orca.mixins import OrcaPageMixin

from .models import Album, Video


class AlbumTabs(OrcaPageMixin):
    """The parent (an album) and its tabs, for every page under /albums/<album_pk>/."""

    def get_parent(self):
        return get_object_or_404(Album, pk=self.kwargs["album_pk"])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        album = ctx["parent"] = self.get_parent()
        here = self.request.path
        tabs = [("Overview", reverse("album-detail", args=[album.pk]), None),
                ("Videos", reverse("album-videos", args=[album.pk]), album.videos.count())]
        ctx["parent_tabs"] = [{"label": label, "url": url, "count": count, "current": here == url} for label, url, count in tabs]
        ctx["parent_stats"] = [{"label": "Videos", "value": album.videos.count(), "icon": "play"},
                               {"label": "Last change", "value": album.updated_at.strftime("%-d %b"), "icon": "history"}]
        ctx["parent_update_url"] = reverse("album-update", args=[album.pk])
        return ctx


class AlbumDetail(AlbumTabs, DetailView):
    model = Album
    pk_url_kwarg = "album_pk"
    template_name = "orca/generic/parent_detail.html"
    detail_fields = ["title", "owner", "created_at"]


class AlbumVideos(AlbumTabs, ListView):
    model = Video
    template_name = "orca/generic/child_list.html"
    paginate_by = 25
    list_columns = ["title", "status", "recorded_on"]
    detail_url_name, create_url_name = "video-detail", "album-video-create"

    def get_queryset(self):
        return super().get_queryset().filter(album_id=self.kwargs["album_pk"])
```

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI L14: Reduce travel between related actions

**ORCA guide items covered:** Parent-child detail template

---

## Parent-child form template

`id: parent-child-form` · level: template · source: ORCA

Create or edit a child inside its parent's tab, with a heading that names the parent.

Built from: `parent-base`, `form-stack`

### Why

A form that says 'Add video to North building' cannot be misread (Practical UI W04), and the parent's tabs stay one click away.

### When to use

- Adding and editing child records.

### How to use

- Extend it: `{% extends "orca/generic/child_form.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Set the parent on the new object in `form_valid` (do not show the parent as a field).

Extend: `{% extends "orca/generic/child_form.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `parent_summary`, `parent_tabs`, `detail_actions`, `child_content`, `form_fields`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `parent`: the parent object (its title heads every tab).
- `parent_tabs`: `[{"label", "url", "count", "current"}]`, Overview first.
- `parent_stats`: optional `[{"label", "value"}]` shown above the tabs; `parent_update_url`.
- `form`, `object`, `model_name`, `cancel_url`.

#### Example: Child template

```django
{% extends "orca/generic/child_form.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Parent mixin and views

```python
# videos/views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView

from orca.mixins import OrcaPageMixin

from .models import Album, Video


class AlbumTabs(OrcaPageMixin):
    """The parent (an album) and its tabs, for every page under /albums/<album_pk>/."""

    def get_parent(self):
        return get_object_or_404(Album, pk=self.kwargs["album_pk"])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        album = ctx["parent"] = self.get_parent()
        here = self.request.path
        tabs = [("Overview", reverse("album-detail", args=[album.pk]), None),
                ("Videos", reverse("album-videos", args=[album.pk]), album.videos.count())]
        ctx["parent_tabs"] = [{"label": label, "url": url, "count": count, "current": here == url} for label, url, count in tabs]
        ctx["parent_stats"] = [{"label": "Videos", "value": album.videos.count(), "icon": "play"},
                               {"label": "Last change", "value": album.updated_at.strftime("%-d %b"), "icon": "history"}]
        ctx["parent_update_url"] = reverse("album-update", args=[album.pk])
        return ctx


class AlbumDetail(AlbumTabs, DetailView):
    model = Album
    pk_url_kwarg = "album_pk"
    template_name = "orca/generic/parent_detail.html"
    detail_fields = ["title", "owner", "created_at"]


class AlbumVideos(AlbumTabs, ListView):
    model = Video
    template_name = "orca/generic/child_list.html"
    paginate_by = 25
    list_columns = ["title", "status", "recorded_on"]
    detail_url_name, create_url_name = "video-detail", "album-video-create"

    def get_queryset(self):
        return super().get_queryset().filter(album_id=self.kwargs["album_pk"])
```

**Principles applied:** Practical UI W04: Lead with the information people seek; Practical UI R01: Keep the main form flow in one column; Practical UI R02: Ask only for useful, necessary information

**ORCA guide items covered:** Parent-child form template

---

## Parent-child confirm template

`id: parent-child-confirm` · level: template · source: ORCA

Confirm removing a child from its parent, or explain what blocks it.

Built from: `parent-base`, `confirm-action-panel`, `delete-blocked-notice`

### Why

The question names both records ('Remove Gate 1 from Warehouse?') so the consequence is clear (Practical UI B13, W04).

### When to use

- Deleting a child record from inside its parent.

### How to use

- Extend it: `{% extends "orca/generic/child_confirm.html" %}`, then fill only the blocks you need.
- Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` (from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.
- Pass `deleted` to list what goes with it; `blocked_by` is filled by the mixin on a DeleteView.

Extend: `{% extends "orca/generic/child_confirm.html" %}`

Blocks: `title`, `title_suffix`, `head`, `theme_bootstrap`, `extra_head`, `body_class`, `skip_link`, `body`, `modal`, `scripts`, `extra_scripts`, `top_bar`, `brand`, `top_nav`, `top_bar_end`, `sidebar`, `sidebar_nav`, `sidebar_extra`, `page_head`, `breadcrumbs`, `page_title`, `page_subtitle`, `page_actions`, `messages`, `content`, `footer`, `parent_summary`, `parent_tabs`, `detail_actions`, `child_content`, `consequences`

### Context it reads

- `title`: the page title (also the browser tab, followed by the brand name).
- `subtitle`: one sentence under the title.
- `breadcrumbs`: a list of `(label, url)`; the current page comes last with an empty url.
- `nav`: sidebar sections, each `{"label": …, "items": [{"label", "url", "icon", "count", "current"}]}`.
- `user`: when signed in, the top bar shows the user chip.
- `messages`: Django messages are shown under the page head automatically.
- `parent`: the parent object (its title heads every tab).
- `parent_tabs`: `[{"label", "url", "count", "current"}]`, Overview first.
- `parent_stats`: optional `[{"label", "value"}]` shown above the tabs; `parent_update_url`.
- `object`, `deleted`, `blocked_by`, `submit_label`, `cancel_url`.

#### Example: Child template

```django
{% extends "orca/generic/child_confirm.html" %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Parent mixin and views

```python
# videos/views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView

from orca.mixins import OrcaPageMixin

from .models import Album, Video


class AlbumTabs(OrcaPageMixin):
    """The parent (an album) and its tabs, for every page under /albums/<album_pk>/."""

    def get_parent(self):
        return get_object_or_404(Album, pk=self.kwargs["album_pk"])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        album = ctx["parent"] = self.get_parent()
        here = self.request.path
        tabs = [("Overview", reverse("album-detail", args=[album.pk]), None),
                ("Videos", reverse("album-videos", args=[album.pk]), album.videos.count())]
        ctx["parent_tabs"] = [{"label": label, "url": url, "count": count, "current": here == url} for label, url, count in tabs]
        ctx["parent_stats"] = [{"label": "Videos", "value": album.videos.count(), "icon": "play"},
                               {"label": "Last change", "value": album.updated_at.strftime("%-d %b"), "icon": "history"}]
        ctx["parent_update_url"] = reverse("album-update", args=[album.pk])
        return ctx


class AlbumDetail(AlbumTabs, DetailView):
    model = Album
    pk_url_kwarg = "album_pk"
    template_name = "orca/generic/parent_detail.html"
    detail_fields = ["title", "owner", "created_at"]


class AlbumVideos(AlbumTabs, ListView):
    model = Video
    template_name = "orca/generic/child_list.html"
    paginate_by = 25
    list_columns = ["title", "status", "recorded_on"]
    detail_url_name, create_url_name = "video-detail", "album-video-create"

    def get_queryset(self):
        return super().get_queryset().filter(album_id=self.kwargs["album_pk"])
```

**Principles applied:** Practical UI B13: Scale friction to the consequence; Practical UI W04: Lead with the information people seek

**ORCA guide items covered:** Parent-child confirm template

---
