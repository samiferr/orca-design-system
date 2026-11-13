from .registry import Element, add, category

C = category(
    "charts", "Chart and graphic marks",
    "The small marks that make up charts, legends, zones and heat maps. Every colour mark has a nearby text label.",
)

add(Element(
    "swatch", "Swatch", C,
    "A small colour square that keys a legend entry or shows a chosen colour.",
    why="A legend links a colour to a name; without the name, colour-blind readers lose the chart (Practical UI C03).",
    when=["Chart legends, colour pickers, calendar lists, zone lists."],
    how=["`<span class=\"orca-swatch\" style=\"--orca-swatch: var(--orca-chart-2)\"></span>` followed by the series name.",
         "Line series: `.orca-swatch--line`. Small: `--sm`.", "Use `--orca-chart-1…8` in order for series."],
    classes=[".orca-swatch", ".orca-swatch--sm", ".orca-swatch--line"], tokens=["chart-1", "chart-2", "chart-3"],
    laws=["C03"],
    examples=[("Legend entries", """<ul class="orca-row orca-row--16" style="list-style: none; margin: 0; padding: 0">
  <li class="orca-with-icon"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-1)"></span>Entrance A</li>
  <li class="orca-with-icon"><span class="orca-swatch" style="--orca-swatch: var(--orca-chart-2)"></span>Entrance B</li>
  <li class="orca-with-icon"><span class="orca-swatch orca-swatch--line" style="--orca-swatch: var(--orca-chart-3)"></span>Target</li>
</ul>""")],
    guide=["Swatch"], related=["chart-dot"],
))

add(Element(
    "zone-swatch", "Zone swatch", C,
    "A mark that matches a region drawn on an image or video: coloured outline, light fill, hatched when excluded.",
    why="Using the same mark in lists as on the image or video lets people match a zone to its row without reading (Miller's law); "
        "hatching distinguishes excluded zones without relying on hue (C03).",
    when=["Region lists, region editors, legends over images and videos."],
    how=["`<span class=\"orca-zone-swatch\" style=\"--orca-zone: var(--orca-teal-500)\"></span>` + zone name.",
         "Excluded zone: add `.orca-zone-swatch--exclude`."],
    classes=[".orca-zone-swatch", ".orca-zone-swatch--exclude"], tokens=["chart-1"],
    laws=["miller", "C03"],
    examples=[("Zones", """<div class="orca-stack">
  <span class="orca-with-icon"><span class="orca-zone-swatch" style="--orca-zone: var(--orca-teal-500)"></span>Subject</span>
  <span class="orca-with-icon"><span class="orca-zone-swatch orca-zone-swatch--exclude" style="--orca-zone: var(--orca-orange-500)"></span>Watermark area (excluded)</span>
</div>""")],
    guide=["Zone swatch"], source="ORCA",
))

add(Element(
    "chart-dot", "Dot (chart marker)", C,
    "A data-point marker: round, square, diamond or ring, coloured by series.",
    why="Different marker shapes keep series distinguishable in greyscale and for colour-blind readers (C03).",
    when=["Scatter points, line-chart markers, inline series keys."],
    how=["`<span class=\"orca-mark-dot\" style=\"--orca-swatch: var(--orca-chart-1)\"></span>`; shapes `--square`, `--diamond`, `--ring`.",
         "Give each series a different shape when there are more than three."],
    classes=[".orca-mark-dot", ".orca-mark-dot--square", ".orca-mark-dot--diamond", ".orca-mark-dot--ring"],
    tokens=["chart-1", "chart-2"],
    laws=["C03"],
    examples=[("Shapes", """<div class="orca-row orca-row--16">
  <span class="orca-with-icon"><span class="orca-mark-dot" style="--orca-swatch: var(--orca-chart-1)"></span>Visitors</span>
  <span class="orca-with-icon"><span class="orca-mark-dot orca-mark-dot--square" style="--orca-swatch: var(--orca-chart-2)"></span>Staff</span>
  <span class="orca-with-icon"><span class="orca-mark-dot orca-mark-dot--diamond" style="--orca-swatch: var(--orca-chart-3)"></span>Deliveries</span>
  <span class="orca-with-icon"><span class="orca-mark-dot orca-mark-dot--ring" style="--orca-swatch: var(--orca-chart-4)"></span>Forecast</span>
</div>""")],
    guide=["Dot"],
))

add(Element(
    "heat-cell", "Heat-map cell", C,
    "A cell shaded on a 6-step sequential scale, with its value printed inside.",
    why="Lightness steps show intensity at a glance (pre-attentive), and printing the value keeps it exact and accessible (C03, W11).",
    when=["Capacity by hour and day, occupancy grids, activity calendars."],
    avoid=["Diverging data (above/below a target) on this scale: use two hues (phase 2)."],
    how=["`<td class=\"orca-heat orca-heat--3\">142</td>`; levels `--0`…`--5` mapped by your own thresholds, `--empty` for no data.",
         "Text colour flips automatically on dark levels.", "Show the scale's legend with the same cells and their ranges."],
    a11y=["The value is in the cell; add row and column headers (`<th scope>`) to give screen readers context."],
    classes=[".orca-heat", ".orca-heat--1", ".orca-heat--5", ".orca-heat--empty"], tokens=["heat-0", "heat-5"],
    laws=["C03", "W11"],
    examples=[("Row of cells", """<table style="border-collapse: separate; border-spacing: 2px"><tr>
  <th scope="row" class="orca-small" style="padding-inline-end: var(--orca-space-8)">Mon</th>
  <td class="orca-heat orca-heat--empty">–</td><td class="orca-heat orca-heat--0">4</td><td class="orca-heat orca-heat--1">18</td><td class="orca-heat orca-heat--2">40</td>
  <td class="orca-heat orca-heat--3">96</td><td class="orca-heat orca-heat--4">142</td><td class="orca-heat orca-heat--5">210</td>
</tr></table>""")],
    guide=["Heat-map cell"],
))
