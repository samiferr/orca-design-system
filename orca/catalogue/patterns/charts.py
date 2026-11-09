from ..registry import add, category
from . import Pattern

C = category(
    "pattern-charts", "Charts",
    "Server-rendered SVG charts in a chart frame, in token colours, each with a text summary and its data as a table. No chart library.",
    level="pattern",
)

COMMON = [
    "Every chart: `{% templatetag openblock %} orca_chart kind data title=\"…\" subtitle=\"unit and period\" caption=\"source\" unit=\"%\" {% templatetag closeblock %}`.",
    "`data` is a dict `{\"labels\": […], \"series\": [{\"name\", \"values\"}]}` or a string `\"labels=Mon,Tue | Entrance A=120,180\"`.",
    "The SVG carries a text summary (`aria-label`), each mark has a tooltip, and 'Show data' reveals the table.",
]
A11Y = ["Colour is never the only key: series have a legend; lines change dash; scatter series change shape."]


def chart(eid, name, kind, summary, why, when, avoid, how, data, guide, extra="", laws=("C03", "W11")):
    add(Pattern(eid, name, C, summary, why=why, when=when, avoid=avoid, how=list(how) + COMMON, a11y=A11Y,
                classes=[".orca-chart", ".orca-chart-frame"], laws=list(laws), uses=["chart-frame"],
                examples=[(name, f'{{% orca_chart "{kind}" {data} {extra}%}}')], guide=[guide]))


chart("bar-chart", "Bar chart", "bar",
      "Bars comparing values across categories; grouped, stacked or horizontal.",
      "Lengths from a common baseline are the most accurately compared visual encoding, so bars are the default for comparing categories (Miller's law: one comparison at a glance).",
      ["Comparing quantities across categories or a few periods: visitors per day, alerts per site."],
      ["Many periods (more than about 15): use a line chart.", "Parts of a whole: a stacked bar, or a doughnut for 2–5 parts."],
      ["`stacked=True` stacks series; `horizontal=True` for long category names or many categories.", "Start the value axis at zero; sort categories by value unless they have a natural order (days, hours)."],
      'sample.visitors_week title="Visitors per day" subtitle="This week, people" caption="Source: line counts"', "Bar chart")

chart("line-chart", "Line chart", "line",
      "Lines showing how one or more values change over time.",
      "A line shows trend and change over time better than bars, and comparing with a reference period answers 'is this normal?' (Peak–end rule: context).",
      ["Values over many time points: visitors per hour, accuracy per day."],
      ["Few categories with no order: use bars.", "More than 4 series: split into small multiples."],
      ["Use `\"area\"` as the kind for one series where the volume matters.", "The second series is dashed so it differs without colour; label the reference ('Last Friday')."],
      'sample.visitors_hours title="Visitors per hour" subtitle="Today compared with last Friday"', "Line chart")

chart("pie-chart", "Pie chart", "pie",
      "A circle split into the shares of one total, with a legend giving each value and percentage.",
      "Part-to-whole is understood at a glance when there are few parts; the legend gives exact numbers because angles are hard to compare (Practical UI C03, W11).",
      ["2–5 shares of one total."], ["More than 5 parts or similar shares: use a horizontal bar chart."],
      ["Order slices from largest, clockwise from 12 o'clock; group small ones into 'Other'."],
      'sample.by_entrance title="Visitors by entrance" subtitle="Today"', "Pie chart")

chart("doughnut-chart", "Doughnut chart", "doughnut",
      "A pie with the total in the middle.",
      "The hole leaves room for the total, so one figure answers both 'how many' and 'how split' (Miller's law).",
      ["Shares of a total where the total itself matters: visitors today by entrance."], ["More than 5 parts: use bars."],
      ["Same rules as the pie chart; the centre shows the total."],
      'sample.by_entrance title="Visitors by entrance" subtitle="Today"', "Doughnut chart")

chart("scatter-chart", "Scatter chart", "scatter",
      "Points placed by two values to show a relationship.",
      "Plotting two measures against each other reveals correlation and outliers no table shows (Tesler's law: the chart does the comparison).",
      ["Two numeric measures per item: dwell time against visits per hour."], ["One measure: use bars or a line."],
      ["Each series gets its own marker shape; name both axes in the subtitle with their units."],
      'sample.dwell_vs_visits title="Dwell time and visits" subtitle="x: average dwell (min), y: visits per hour"', "Scatter chart")

chart("bubble-chart", "Bubble chart", "bubble",
      "A scatter chart whose point size shows a third value.",
      "Size adds a third dimension (for example site size) without a second chart; the data table gives exact values because area is hard to compare.",
      ["Three measures per item, where the third is secondary: sites by dwell, visits and number of videos."], ["Exact comparison of the third value: use a table."],
      ["Values are `x:y:size`; size scales by area, not radius."],
      'sample.sites_bubble title="Sites" subtitle="x: average dwell (min), y: visits per hour, size: videos"', "Bubble chart")

chart("radar-chart", "Radar chart", "radar",
      "Scores on several axes drawn as a polygon, comparing one or two items.",
      "A shape shows the profile of an item across many criteria at once and makes weak spots visible (Von Restorff); limit to two items so shapes stay readable.",
      ["Comparing one or two items across 4–8 scored criteria on the same scale."], ["More than two items, or different scales: use a table or bars."],
      ["All axes must share the same scale (for example 0–100)."],
      'sample.site_scores title="Site health" subtitle="Scores out of 100"', "Radar chart", laws=("C03", "restorff"))

chart("polar-area-chart", "Polar area chart", "polar",
      "Equal-angle segments whose radius shows each value.",
      "Equal angles avoid the pie's angle-reading problem while keeping a compact round form; area scales with value.",
      ["Cyclic categories or a compact overview of counts by type: alerts by type, visits by weekday."], ["Precise comparison: use bars."],
      ["Order segments meaningfully (by time or by size)."],
      'sample.alerts_by_type title="Alerts by type" subtitle="Last 30 days"', "Polar area chart")
