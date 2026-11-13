# Editorial

Blocks for stories and highlighted facts on news, blog and report pages.

## Story feature

`id: story-feature` · level: pattern · source: ORCA

A featured article: large image, kicker, headline, lead and meta, side by side on wide screens.

Built from: `captioned-media`, `post-block`

### General description

A large featured article block with a big image, headline, intro text and details. It highlights the top story on a page.

#### Use cases

- Showing the lead story on a news or blog page.
- Featuring a case study or announcement.
- Highlighting the newest release notes.

#### When not to use it

- For lists of many stories, use smaller teaser blocks.
- Do not feature several stories at once; the highlight is lost.

#### Best practices

- Use one strong image with a helpful description.
- Write a headline that tells the story.
- Keep the intro to a few lines.
- Show the date and reading time.
- Stack image and text on small screens.

### When to use

- The top story of a news, blog or release-notes page.

### How to use

- `<article class="orca-story">` with `.orca-story__media` (4:3 image with alt text) and the text (kicker, `h2.orca-story__title` linked, `.orca-story__lead`, card meta).

#### Example: Story

```django
<article class="orca-story">
  <div class="orca-story__media">
    <img src="{% static "orca/img/sample-street.svg" %}" alt="Shoppers entering the north building">
  </div>
  <div>
    <p class="orca-card-kicker">Case study</p>
    <h2 class="orca-story__title">
      <a href="#">How North building cut queues by a third</a>
    </h2>
    <p class="orca-story__lead">Live counts showed the 13:00 peak; two more tills open at 12:45 now.</p>
    <p class="orca-card-meta">6 November 2026 · 4 min read</p>
  </div>
</article>
```

**Classes:** `.orca-story`, `.orca-story__media`, `.orca-story__title`, `.orca-story__lead`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Practical UI W05: Order explanations as an inverted pyramid

**ORCA guide items covered:** Story feature

---

## Factoid

`id: factoid` · level: pattern · source: ORCA

One striking number with a short statement and its source.

Built from: `big-number`

### General description

A single large number or fact with a short sentence and its source. It makes one result easy to remember.

#### Use cases

- Highlighting a key result in a report or case study.
- Adding a striking statistic to a landing page.
- Summarizing one finding in a story.

#### When not to use it

- For several figures together, use a grid of summary tiles.
- For data that needs context over time, use a chart.

#### Best practices

- Show one number only and make it large.
- Explain in a sentence what the number means.
- Always give the source and date.
- Use a number you can back up.
- Keep text readable against the background.

### When to use

- Reports, case studies and landing pages to highlight one result.

### When not to use

- Several factoids in a row: use a KPI grid or summary tiles.

### How to use

- `<figure class="orca-factoid">` with `.orca-factoid__number`, `<figcaption>` holding `.orca-factoid__text` and `.orca-factoid__source`.

#### Example: Factoid

```django
<figure class="orca-factoid" style="margin: 0">
  <span class="orca-factoid__number">−34%</span>
  <figcaption>
    <p class="orca-factoid__text">waiting time at the tills after opening two more at peak</p>
    <p class="orca-factoid__source">North building, October 2026</p>
  </figcaption>
</figure>
```

**Classes:** `.orca-factoid`, `.orca-factoid__number`, `.orca-factoid__text`, `.orca-factoid__source`

**Principles applied:** Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly; Peak–end rule: people judge an experience by its peak and its end; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Factoid

---
