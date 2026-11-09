# Editorial

Blocks for stories and highlighted facts on news, blog and report pages.

## Story feature

`id: story-feature` · level: pattern · source: ORCA

A featured article: large image, kicker, headline, lead and meta, side by side on wide screens.

Built from: `captioned-media`, `post-block`

### Why

One featured story with scale and an image breaks the grid and is noticed first (Von Restorff); a lead paragraph lets people decide quickly (Practical UI W05).

### When to use

- The top story of a news, blog or release-notes page.

### How to use

- `<article class="orca-story">` with `.orca-story__media` (4:3 image with alt text) and the text (kicker, `h2.orca-story__title` linked, `.orca-story__lead`, card meta).

#### Example: Story

```django
<article class="orca-story"><div class="orca-story__media"><img src="{% static "orca/img/sample-street.svg" %}" alt="Shoppers entering the north building"></div>
  <div><p class="orca-card-kicker">Case study</p><h2 class="orca-story__title"><a href="#">How North building cut queues by a third</a></h2><p class="orca-story__lead">Live counts showed the 13:00 peak; two more tills open at 12:45 now.</p><p class="orca-card-meta">6 November 2026 · 4 min read</p></div></article>
```

**Classes:** `.orca-story`, `.orca-story__media`, `.orca-story__title`, `.orca-story__lead`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI W05: Order explanations as an inverted pyramid

**ORCA guide items covered:** Story feature

---

## Factoid

`id: factoid` · level: pattern · source: ORCA

One striking number with a short statement and its source.

Built from: `big-number`

### Why

A single large number is remembered (Von Restorff, Peak–end rule); stating the source keeps it honest.

### When to use

- Reports, case studies and landing pages to highlight one result.

### When not to use

- Several factoids in a row: use a KPI grid or summary tiles.

### How to use

- `<figure class="orca-factoid">` with `.orca-factoid__number`, `<figcaption>` holding `.orca-factoid__text` and `.orca-factoid__source`.

#### Example: Factoid

```django
<figure class="orca-factoid" style="margin: 0"><span class="orca-factoid__number">−34%</span><figcaption><p class="orca-factoid__text">waiting time at the tills after opening two more at peak</p><p class="orca-factoid__source">North building, October 2026</p></figcaption></figure>
```

**Classes:** `.orca-factoid`, `.orca-factoid__number`, `.orca-factoid__text`, `.orca-factoid__source`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Peak–end rule: people judge an experience by its peak and its end; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Factoid

---
