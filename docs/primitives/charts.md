# Chart and graphic marks

The small marks that make up charts, legends, zones and heat maps. Every colour mark has a nearby text label.

## Swatch

`id: swatch` · level: primitive · source: Tangerine

A small colour square that keys a legend entry or shows a chosen colour.

### General description

A small square of colour that stands for a series or a chosen colour. It links a colour on a chart to its name in the legend.

#### Use cases

- Chart legends.
- Colour pickers and calendar lists.
- Labelling series next to a list.

#### When not to use it

- Colour alone does not carry meaning; always add a name.
- Different data types may need different marker shapes.

#### Best practices

- Always place a text label beside the swatch.
- Use colours that are easy to tell apart.
- Use a line style for line series.
- Keep the order the same as in the chart.

### When to use

- Chart legends, colour pickers, calendar lists, zone lists.

### How to use

- `<span class="orca-swatch" style="--orca-swatch: var(--orca-chart-2)"></span>` followed by the series name.
- Line series: `.orca-swatch--line`. Small: `--sm`.
- Use `--orca-chart-1…8` in order for series.

#### Example: Legend entries

```django
<ul class="orca-row orca-row--16" style="list-style: none; margin: 0; padding: 0">
  <li class="orca-with-icon"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-1)"></span>Entrance A</li>
  <li class="orca-with-icon"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-2)"></span>Entrance B</li>
  <li class="orca-with-icon"><span class="orca-swatch orca-swatch--line" style="--orca-swatch: var(--orca-chart-3)"></span>Target</li>
</ul>
```

**Classes:** `.orca-swatch`, `.orca-swatch--sm`, `.orca-swatch--line`

**Tokens:** `--orca-chart-1`, `--orca-chart-2`, `--orca-chart-3`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour

**Related:** `chart-dot`

**ORCA guide items covered:** Swatch

---

## Zone swatch

`id: zone-swatch` · level: primitive · source: ORCA

A mark that matches a region drawn on an image or video: coloured outline, light fill, hatched when excluded.

### General description

A small mark that copies how a region is drawn on an image or video, so a list entry can be matched to its region.

#### Use cases

- Lists of regions on an image or video.
- Region editors.
- Legends laid over images or videos.

#### When not to use it

- Data series in charts need an ordinary legend swatch.
- Hue alone does not carry meaning; always add a name.

#### Best practices

- Match the mark to the region on the image.
- Show excluded regions with a pattern, not only colour.
- Place the region name beside the mark.
- Keep outline and fill the same as on the image.

### When to use

- Region lists, region editors, legends over images and videos.

### How to use

- `<span class="orca-zone-swatch" style="--orca-zone: var(--orca-teal-500)"></span>` + zone name.
- Excluded zone: add `.orca-zone-swatch--exclude`.

#### Example: Zones

```django
<div class="orca-stack">
  <span class="orca-with-icon"><span class="orca-zone-swatch" style="--orca-zone: var(--orca-teal-500)"></span>Subject</span>
  <span class="orca-with-icon"><span class="orca-zone-swatch orca-zone-swatch--exclude" style="--orca-zone: var(--orca-orange-500)"></span>Watermark area (excluded)</span>
</div>
```

**Classes:** `.orca-zone-swatch`, `.orca-zone-swatch--exclude`

**Tokens:** `--orca-chart-1`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Zone swatch

---

## Dot (chart marker)

`id: chart-dot` · level: primitive · source: Tangerine

A data-point marker: round, square, diamond or ring, coloured by series.

### General description

A small shape that marks a data point on a chart or in a legend, such as a circle, square or diamond.

#### Use cases

- Scatter plots.
- Markers on line charts.
- Series keys in a legend.

#### When not to use it

- Many points close together need a different chart or grouping.
- Colour alone fails for colour-blind readers; vary the shape.

#### Best practices

- Use different shapes for different series.
- Keep markers a readable size.
- Label each series beside its marker.
- Use the same marker in the chart and the legend.

### When to use

- Scatter points, line-chart markers, inline series keys.

### How to use

- `<span class="orca-mark-dot" style="--orca-swatch: var(--orca-chart-1)"></span>`; shapes `--square`, `--diamond`, `--ring`.
- Give each series a different shape when there are more than three.

#### Example: Shapes

```django
<div class="orca-row orca-row--16">
  <span class="orca-with-icon"><span class="orca-mark-dot" style="--orca-swatch: var(--orca-chart-1)"></span>Visitors</span>
  <span class="orca-with-icon"><span class="orca-mark-dot orca-mark-dot--square" style="--orca-swatch: var(--orca-chart-2)"></span>Staff</span>
  <span class="orca-with-icon"><span class="orca-mark-dot orca-mark-dot--diamond" style="--orca-swatch: var(--orca-chart-3)"></span>Deliveries</span>
  <span class="orca-with-icon"><span class="orca-mark-dot orca-mark-dot--ring" style="--orca-swatch: var(--orca-chart-4)"></span>Forecast</span>
</div>
```

**Classes:** `.orca-mark-dot`, `.orca-mark-dot--square`, `.orca-mark-dot--diamond`, `.orca-mark-dot--ring`

**Tokens:** `--orca-chart-1`, `--orca-chart-2`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Dot

---

## Heat-map cell

`id: heat-cell` · level: primitive · source: Tangerine

A cell shaded on a 6-step sequential scale, with its value printed inside.

### General description

A table cell shaded from light to dark to show how large a value is. A grid of them makes patterns easy to spot.

#### Use cases

- Activity by hour and day.
- Occupancy or capacity grids.
- Calendars showing busy and quiet days.

#### When not to use it

- Exact comparisons are easier in a table or bar chart.
- Data that goes above and below a target needs a two-colour scale.

#### Best practices

- Print the value inside each cell.
- Show a legend with the ranges.
- Choose clear thresholds for the steps.
- Mark empty cells differently from zero.
- Add row and column headings.

### When to use

- Capacity by hour and day, occupancy grids, activity calendars.

### When not to use

- Diverging data (above/below a target) on this scale: use two hues (phase 2).

### How to use

- `<td class="orca-heat orca-heat--3">142</td>`; levels `--0`…`--5` mapped by your own thresholds, `--empty` for no data.
- Text colour flips automatically on dark levels.
- Show the scale's legend with the same cells and their ranges.

### Accessibility

- The value is in the cell; add row and column headers (`<th scope>`) to give screen readers context.

#### Example: Row of cells

```django
<table style="border-collapse: separate; border-spacing: 2px">
  <tr>
    <th scope="row" class="orca-small" style="padding-inline-end: var(--orca-space-8)">Mon</th>
    <td class="orca-heat orca-heat--empty">–</td>
    <td class="orca-heat orca-heat--0">4</td>
    <td class="orca-heat orca-heat--1">18</td>
    <td class="orca-heat orca-heat--2">40</td>
    <td class="orca-heat orca-heat--3">96</td>
    <td class="orca-heat orca-heat--4">142</td>
    <td class="orca-heat orca-heat--5">210</td>
  </tr>
</table>
```

**Classes:** `.orca-heat`, `.orca-heat--1`, `.orca-heat--5`, `.orca-heat--empty`

**Tokens:** `--orca-heat-0`, `--orca-heat-5`

**Principles applied:** Practical UI C03: Communicate meaning beyond colour; Practical UI W11: Make numbers scannable

**ORCA guide items covered:** Heat-map cell

---
