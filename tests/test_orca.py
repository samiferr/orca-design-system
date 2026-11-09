import html as html_lib
import io
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from django.core import checks
from django.core.management import call_command
from django.template import Context, Template
from django.test import SimpleTestCase, override_settings
from django.urls import reverse

from orca import build, color, icons, tokens
from orca.catalogue import registry
from orca.catalogue.guide import all_items
from orca.conf import compute_brand
from orca.views import render_snippet

ROOT = Path(__file__).resolve().parent.parent
CSS = (ROOT / "orca/static/orca/css/orca.css").read_text() + (ROOT / "orca/static/orca/css/components.css").read_text() + (ROOT / "orca/static/orca/css/patterns.css").read_text() + (ROOT / "orca/static/orca/css/templates.css").read_text()
TOKENS_CSS = (ROOT / "orca/static/orca/css/tokens.css").read_text()
CSS_CLASSES = set(m[1:] for m in re.findall(r"\.orca-[a-z0-9_-]+", CSS))
CSS_TOKENS = set(re.findall(r"--orca-([a-z0-9-]+)\s*:", TOKENS_CSS))


class GuideCoverageTests(SimpleTestCase):
    def test_every_guide_item_of_each_released_level_is_covered_once(self):
        for level in registry.RELEASED_LEVELS:
            with self.subTest(level=level):
                covered = {}
                for el in registry.all_elements(level):
                    for item in el.guide:
                        covered.setdefault(item, []).append(el.id)
                guide = [item for _, item in all_items(level)]
                self.assertEqual([i for i in guide if i not in covered], [], "guide items with no element")
                self.assertEqual({k: v for k, v in covered.items() if len(v) > 1}, {}, "guide items claimed twice")
                self.assertEqual([k for k in covered if k not in guide], [], "element.guide entries not in the guide")

    def test_components_say_what_they_are_built_from(self):
        for el in registry.all_elements("component"):
            self.assertTrue(el.uses, f"{el.id}: a component lists the elements it is built from")


class CatalogueTests(SimpleTestCase):
    def test_every_element_has_why_when_how_and_an_example(self):
        for el in registry.all_elements():
            with self.subTest(el=el.id):
                self.assertTrue(re.fullmatch(r"[a-z0-9-]+", el.id))
                self.assertGreater(len(el.summary), 10)
                self.assertGreater(len(el.why), 40)
                self.assertTrue(el.when and el.how and (el.examples or el.preview))
                self.assertTrue(el.laws, "every element names the principle it applies")
                self.assertIn(el.level, registry.RELEASED_LEVELS)

    def test_principles_are_known(self):
        for el in registry.all_elements():
            for key in el.laws:
                self.assertTrue(key in registry.LAWS or key in registry.PRACTICAL_UI, f"{el.id}: unknown principle {key}")

    def test_related_ids_exist(self):
        for el in registry.all_elements():
            for rid in el.related + el.uses:
                self.assertIsNotNone(registry.get(rid), f"{el.id}: related {rid} missing")

    def test_documented_classes_and_tokens_exist(self):
        for el in registry.all_elements():
            for cls in el.classes:
                name = re.match(r"\.([a-z0-9_-]+)", cls).group(1)
                self.assertTrue(name in CSS_CLASSES, f"{el.id}: class {cls} not in orca.css")
            for tok in el.tokens:
                self.assertIn(tok, CSS_TOKENS, f"{el.id}: token --orca-{tok} not in tokens.css")

    def test_examples_render_and_use_real_classes_and_icons(self):
        for el in registry.all_elements():
            for title, html in el.examples:
                with self.subTest(el=el.id, example=title):
                    out = render_snippet(html)
                    self.assertNotIn("Example failed to render", out)
                    for cls in re.findall(r'class="([^"]*)"', out):
                        for name in re.findall(r"\borca-[a-z0-9_-]+", cls):
                            self.assertTrue(name in CSS_CLASSES, f"{el.id}: example uses unknown class {name}")
                    for btn in re.findall(r"<button\b[^>]*>", out):
                        self.assertIn("type=", btn, f"{el.id}: button without type")
                    for img in re.findall(r"<img\b[^>]*>", out):
                        self.assertIn("alt=", img, f"{el.id}: img without alt")

    def test_css_uses_only_defined_tokens(self):
        used = set(re.findall(r"var\(--orca-([a-z0-9-]+)", CSS))
        local = {"ratio", "value", "swatch", "zone", "event", "days", "cols", "start", "span", "progress",
                 "rows", "at", "planned", "done", "table-max"}  # set inline per element
        self.assertEqual(sorted(used - CSS_TOKENS - local), [])


class ContrastTests(SimpleTestCase):
    GROUNDS = ("bg", "bg-alt", "bg-input", "bg-page", "bg-panel", "bg-stat")

    def value(self, name, theme):
        tok = next(t for t in tokens.semantic_tokens() if t.name == name)
        return tok.value(theme)

    def test_text_reads_at_4_5_on_every_ground_in_every_theme(self):
        for theme in tokens.THEMES:
            for fg in ("text", "text-muted", "text-inactive"):
                for bg in self.GROUNDS + ("bg-hover", "bg-active", "bg-elevated"):
                    with self.subTest(theme=theme, fg=fg, bg=bg):
                        self.assertGreaterEqual(color.contrast(self.value(fg, theme), self.value(bg, theme)), 4.5)

    def test_control_boundaries_and_focus_hold_3_to_1(self):
        for theme in tokens.THEMES:
            for fg in ("border-strong", "focus"):
                for bg in self.GROUNDS + ("bg-active",):
                    with self.subTest(theme=theme, fg=fg, bg=bg):
                        self.assertGreaterEqual(color.contrast(self.value(fg, theme), self.value(bg, theme)), 3.0)

    def test_code_colours_read_on_every_code_ground(self):
        for theme in tokens.THEMES:
            for tok in [t.name for t in tokens.semantic_tokens() if t.name.startswith("code-")]:
                for bg in ("bg", "bg-alt", "bg-panel", "bg-input"):
                    with self.subTest(theme=theme, fg=tok, bg=bg):
                        self.assertGreaterEqual(color.contrast(self.value(tok, theme), self.value(bg, theme)), 4.5)

    def test_status_text_reads_on_page(self):
        for theme in tokens.THEMES:
            for fg in ("info", "negative", "today"):
                with self.subTest(theme=theme, fg=fg):
                    self.assertGreaterEqual(color.contrast(self.value(fg, theme), self.value("bg", theme)), 4.5)

    def test_text_on_fills(self):
        pairs = [("primary-on", "primary"), ("danger-on", "danger"), ("on-fill", "info-fill"), ("on-fill", "positive-fill"),
                 ("on-fill", "negative-fill"), ("on-fill", "neutral-fill"), ("on-caution", "caution-fill")]
        for theme in tokens.THEMES:
            for fg, bg in pairs:
                with self.subTest(theme=theme, pair=(fg, bg)):
                    self.assertGreaterEqual(color.contrast(self.value(fg, theme), self.value(bg, theme)), 4.5)


class BrandTests(SimpleTestCase):
    def test_defaults_are_readable(self):
        b = compute_brand({})
        self.assertEqual(b.errors, [])
        css = b.css["light"]
        self.assertGreaterEqual(color.contrast(css["--orca-brand-on"], css["--orca-brand-strong"]), 4.5)
        self.assertGreaterEqual(color.contrast(b.css["dark"]["--orca-accent"], "#262626"), 4.5)

    def test_brand_bar_matches_wise_people_analyzer_and_reads(self):
        css = compute_brand({}).css["light"]
        self.assertEqual(css["--orca-brand-bar"], color.mix("#0f95a1", "#000000", 0.30))
        for name in ("--orca-brand-bar", "--orca-brand-bar-hover", "--orca-brand-bar-active"):
            self.assertGreaterEqual(color.contrast("#ffffff", css[name]), 4.5, name)
        pale = compute_brand({"color": "#ffd400"}).css["light"]["--orca-brand-bar"]
        self.assertGreaterEqual(color.contrast("#ffffff", pale), 4.5)

    def test_liberal_input_is_normalised(self):
        b = compute_brand({"color": "7A1FA2", "accent": "#06C"})
        self.assertEqual(b.errors, [])
        self.assertEqual(b.values["color"], "#7a1fa2")
        self.assertEqual(b.css["light"]["--orca-accent"], "#0066cc")

    def test_light_brand_is_darkened_and_reported(self):
        b = compute_brand({"color": "#ffd400", "on_color": "#ffffff"})
        strong = b.css["light"]["--orca-brand-strong"]
        self.assertGreaterEqual(color.contrast("#ffffff", strong), 4.5)
        self.assertTrue(b.notes)

    def test_pale_accent_is_darkened_and_dark_variant_derived(self):
        b = compute_brand({"accent": "#7fb2ff"})
        self.assertGreaterEqual(color.contrast(b.css["light"]["--orca-accent"], "#ebebeb"), 4.5)
        self.assertGreaterEqual(color.contrast(b.css["dark"]["--orca-accent"], "#2c2c2c"), 4.5)
        self.assertTrue(b.notes)

    def test_unknown_keys_and_bad_values_are_errors(self):
        b = compute_brand({"colour": "#fff", "color": "blue-ish", "font_sans": "x; } body { display:none"})
        self.assertEqual(len(b.errors), 3)
        self.assertEqual(b.values["color"], "#0f95a1")

    @override_settings(ORCA={"BRAND": {"color": "#ffd400", "on_color": "#ffffff"}, "SKIN": "x"})
    def test_system_checks(self):
        ids = {m.id for m in checks.run_checks(tags=["orca"])}
        self.assertIn("orca.E001", ids)
        self.assertIn("orca.W001", ids)


class TemplateTagTests(SimpleTestCase):
    def render(self, src, **ctx):
        return Template("{% load orca %}" + src).render(Context(ctx))

    def test_icon(self):
        out = self.render('{% icon "search" %}')
        self.assertIn('aria-hidden="true"', out)
        self.assertIn("orca-icon", out)
        self.assertIn('aria-label="Close"', self.render('{% icon "close" label="Close" %}'))
        self.assertIn("<svg", self.render('{% icon "bell" size="l" %}'))

    def test_unknown_icon_raises_with_help(self):
        with self.assertRaisesMessage(KeyError, "python -m orca icons"):
            icons.svg("does-not-exist")

    def test_all_icons_render(self):
        for name in icons.names():
            self.assertIn("<svg", icons.svg(name))

    def test_head(self):
        out = self.render("{% orca_head %}")
        self.assertIn("orca/css/tokens.css", out)
        self.assertIn("--orca-brand-strong", out)

    @override_settings(ORCA={"THEME": "dark"})
    def test_fixed_theme(self):
        self.assertIn('data-theme="dark"', self.render("{% orca_html_attrs %}"))
        self.assertNotIn("localStorage", self.render("{% orca_head %}"))

    def test_density(self):
        self.assertNotIn("data-density", self.render("{% orca_html_attrs %}"))
        self.assertIn('data-density="dense"', self.render('{% orca_html_attrs density="dense" %}'))
        with self.settings(ORCA={"DENSITY": "dense"}):
            self.assertIn('data-density="dense"', self.render("{% orca_html_attrs %}"))
            self.assertNotIn("data-density", self.render('{% orca_html_attrs density="comfortable" %}'))
        with self.settings(ORCA={"DENSITY": "tiny"}):
            self.assertIn("orca.E004", [m.id for m in checks.run_checks(tags=["orca"])])
        css = (ROOT / "orca/static/orca/css/tokens.css").read_text()
        self.assertIn('[data-density="dense"]', css)
        # Dense only overrides tokens that exist, keeps text readable and leaves the touch minimum alone.
        names = {s.name for s in tokens.ALL_SCALES}
        self.assertEqual(sorted(set(tokens.DENSE) - names), [])
        self.assertNotIn("control-lg", tokens.DENSE)
        self.assertIn("0.875rem", tokens.DENSE["type-body"])

    def test_filters(self):
        self.assertEqual(self.render("{{ v|orca_duration }}", v=90), "1 h 30 min")
        self.assertEqual(self.render("{{ v|orca_duration }}", v=45), "45 min")
        self.assertEqual(self.render("{{ v|orca_duration }}", v=1500), "1 d 1 h")
        self.assertEqual(self.render("{{ v|orca_initials }}", v="Ada King Lovelace"), "AL")
        self.assertEqual(self.render("{{ v|orca_initials }}", v=""), "?")

    def test_timezones(self):
        out = self.render('{% orca_timezone_options "Europe/Paris" %}')
        self.assertIn('<option value="Europe/Paris" selected>Paris</option>', out)


class DocsSiteTests(SimpleTestCase):
    def test_pages(self):
        for name in ("home", "index", "components", "patterns", "templates", "tokens", "icons", "catalogue-json"):
            with self.subTest(name=name):
                self.assertEqual(self.client.get(reverse(f"orca:{name}")).status_code, 200)

    def test_every_element_page(self):
        for el in registry.all_elements():
            with self.subTest(el=el.id):
                res = self.client.get(reverse("orca:element", args=[el.id]))
                self.assertEqual(res.status_code, 200)
                self.assertNotContains(res, "Example failed to render")
                self.assertContains(res, "Why")

    def test_every_guide_page(self):
        from orca.views import GUIDE

        for slug, title, _ in GUIDE:
            with self.subTest(slug=slug):
                res = self.client.get(reverse("orca:guide", args=[slug]))
                self.assertEqual(res.status_code, 200)
                self.assertContains(res, f'<h1 class="orca-page-title">{title}</h1>', html=False)
        self.assertEqual(self.client.get("/orca/guide/nope/").status_code, 404)

    def test_principles_index_lists_every_element_once_per_rule(self):
        res = self.client.get(reverse("orca:guide", args=["principles"]))
        for el in registry.all_elements():
            self.assertContains(res, reverse("orca:element", args=[el.id]))

    def test_static_export_has_no_broken_links(self):
        from orca.site import export

        with tempfile.TemporaryDirectory() as d:
            export(d, fragment_index=True)
            root = Path(d)
            index = (root / "index.html").read_text()
            self.assertNotIn("<!doctype", index.lower())
            self.assertIn("<title>", index)
            broken = []
            for page in root.glob("*.html"):
                html = page.read_text()
                self.assertNotIn('href="/orca/', html)
                for target in re.findall(r'(?:href|src)="([^"#?]+)', html):
                    if ":" not in target and not target.startswith("/") and not (root / target).exists():
                        broken.append(f"{page.name} -> {target}")
            self.assertEqual(broken, [])
            self.assertTrue((root / "static/orca/fonts/UbuntuSans-Variable.woff2").exists())

    def test_unknown_element_404(self):
        self.assertEqual(self.client.get("/orca/nope/").status_code, 404)

    @override_settings(ORCA={"DOCS_ENABLED": False})
    def test_disabled(self):
        self.assertEqual(self.client.get(reverse("orca:index")).status_code, 404)


class LevelTests(SimpleTestCase):
    def test_each_level_groups_the_level_before_it(self):
        keys = [lv.key for lv in registry.LEVEL_DEFS]
        self.assertEqual(tuple(keys), registry.LEVELS)
        self.assertEqual(registry.LEVEL_DEFS[0].built_from, "")
        for before, level in zip(registry.LEVEL_DEFS, registry.LEVEL_DEFS[1:]):
            self.assertEqual(level.built_from, before.key)

    def test_each_element_is_built_from_the_level_below(self):
        order = {k: i for i, k in enumerate(registry.LEVELS)}
        els = {e.id: e for e in registry.all_elements()}
        skips = [f"{e.id} ({e.level}) uses {u} ({els[u].level})" for e in els.values() for u in e.uses
                 if not 0 <= order[e.level] - order[els[u].level] <= 1]
        self.assertEqual(skips, [], "a component groups primitives, a pattern components, a template patterns")

    def test_built_from_lists_have_no_redundant_parts(self):
        els = {e.id: e for e in registry.all_elements()}

        def parts(eid, seen):
            for u in els[eid].uses:
                if u in els and u not in seen:
                    seen.add(u)
                    parts(u, seen)
            return seen

        redundant = [(e.id, u) for e in els.values() for u in e.uses
                     if any(u in parts(o, set()) for o in e.uses if o != u)]
        self.assertEqual(redundant, [], "a part already contained in another listed element is listed again")

    def test_roadmap_has_no_atomic_design_aliases(self):
        res = self.client.get(reverse("orca:guide", args=["roadmap"]))
        for alias in ("Atoms", "Molecules", "Organisms"):
            self.assertNotContains(res, alias)
        self.assertContains(res, "A group of components that")


class PageFilterTests(SimpleTestCase):
    def test_level_pages_have_filters_in_a_right_drawer_opened_from_the_page_actions(self):
        html = self.client.get(reverse("orca:index")).content.decode()
        actions = html[html.index('class="orca-page-head__actions"'):]
        self.assertIn('data-orca-dialog-open="docs-filters"', actions[:600])
        self.assertIn('<dialog class="orca-drawer" id="docs-filters"', html)

    def test_generic_templates_open_filters_from_the_page_actions(self):
        from django import forms
        from django.template.loader import render_to_string
        from django.test import RequestFactory

        class Filters(forms.Form):
            kind = forms.ChoiceField(choices=[("image", "Image"), ("video", "Video")], required=False)

        ctx = {"filter_form": Filters(), "active_filters": 1, "object_list": [], "model_name": "image",
               "model_name_plural": "images", "request": RequestFactory().get("/")}
        for name in ("orca/generic/list.html", "orca/layouts/simple_data.html", "orca/layouts/board.html"):
            with self.subTest(template=name):
                html = render_to_string(name, ctx)
                actions = html[html.index('class="orca-page-head__actions"'):]
                self.assertIn('data-orca-dialog-open="orca-filters"', actions[:400])
                self.assertIn('<dialog class="orca-drawer" id="orca-filters"', html)
                self.assertNotIn('class="orca-filter-bar" method', html)
                self.assertNotIn('<form class="orca-filter-panel"', html)

    def test_no_camera_terminology(self):
        sources = [ROOT / "AGENTS.md", ROOT / "README.md", *(ROOT / "orca").rglob("*.py"), *(ROOT / "orca/templates").rglob("*.html"),
                   *(ROOT / "orca/static/orca").rglob("*.css")]
        hits = [str(p) for p in sources if re.search(r"camera|rtsp|recorder|\bnvr\b|capture run", p.read_text(), re.I)]
        self.assertEqual(hits, [])


class ComponentTagTests(SimpleTestCase):
    def render(self, src, **ctx):
        return Template("{% load orca %}" + src).render(Context(ctx))

    def form(self, data=None):
        from django import forms

        class F(forms.Form):
            name = forms.CharField(help_text="Shown on dashboards.")
            note = forms.CharField(required=False, widget=forms.Textarea)
            kind = forms.ChoiceField(choices=[("a", "Door"), ("b", "Gate")], widget=forms.RadioSelect)
            on = forms.BooleanField(required=False)
            day = forms.DateField()

        f = F(data)
        if data is not None:
            f.is_valid()
        return f

    def test_field_wires_label_help_and_error(self):
        f = self.form({"name": "", "kind": "a", "day": "2026-11-06"})
        out = self.render("{% orca_field f.name %}", f=f)
        self.assertIn('for="id_name"', out)
        self.assertIn('aria-describedby="id_name-error id_name-help"', out)
        self.assertIn('aria-invalid="true"', out)
        self.assertIn('class="orca-input"', out)
        self.assertLess(out.index("orca-help"), out.index("orca-error"))
        self.assertLess(out.index("orca-error"), out.index("<input"))

    def test_field_kinds(self):
        f = self.form()
        self.assertIn("(optional)", self.render("{% orca_field f.note %}", f=f))
        self.assertIn("orca-textarea", self.render("{% orca_field f.note %}", f=f))
        radios = self.render("{% orca_field f.kind %}", f=f)
        self.assertIn("<fieldset", radios)
        self.assertIn("orca-radio__dot", radios)
        self.assertIn('role="switch"', self.render("{% orca_field f.on switch=True %}", f=f))
        self.assertIn('type="date"', self.render("{% orca_field f.day %}", f=f))

    def test_form_errors_summary(self):
        f = self.form({"kind": "z"})
        out = self.render("{% orca_form_errors f %}", f=f)
        self.assertIn("fields need attention", out)
        self.assertIn('href="#id_name"', out)

    def test_page_window(self):
        from orca.components import page_window

        self.assertEqual(page_window(7, 16), [1, None, 6, 7, 8, None, 16])
        self.assertEqual(page_window(1, 5), [1, 2, 3, 4, 5])
        self.assertEqual(page_window(2, 9), [1, 2, 3, 4, None, 9])
        self.assertEqual(page_window(3, 7), [1, 2, 3, 4, 5, 6, 7])

    def test_pagination_keeps_query(self):
        from django.core.paginator import Paginator
        from django.test import RequestFactory

        request = RequestFactory().get("/videos/", {"site": "north", "page": "3"})
        page = Paginator(list(range(100)), 10).page(3)
        out = self.render('{% orca_pagination page noun="videos" %}', page=page, request=request)
        self.assertIn("site=north&amp;page=4", out)
        self.assertIn('aria-current="page"', out)
        self.assertIn("Showing 21–30 of 100 videos", out)

    def test_mini_calendar(self):
        from django.utils import translation

        src = '{% orca_mini_calendar "2026-11-01" selected="2026-11-12" today="2026-11-06" url="/d/{date}" events="2026-11-04" %}'
        out = self.render(src)
        self.assertIn('href="/d/2026-11-12"', out)
        self.assertIn('aria-current="date"', out)
        self.assertIn("has events", out)
        # Weeks start on the locale's first day: Sunday in English, Monday in French.
        self.assertEqual(re.search(r'href="/d/([\d-]+)"', out).group(1), "2026-11-01")
        with translation.override("fr"):
            self.assertEqual(re.search(r'href="/d/([\d-]+)"', self.render(src)).group(1), "2026-10-26")

    def test_messages(self):
        from django.contrib.messages.storage.base import Message
        from django.contrib.messages import constants

        out = self.render("{% orca_messages %}", messages=[Message(constants.SUCCESS, "Saved"), Message(constants.ERROR, "Failed")])
        self.assertIn("orca-alert--positive", out)
        self.assertIn('role="alert"', out)

    def test_charts(self):
        spark = self.render('{% orca_sparkline "1,3,2,5" %}')
        self.assertIn('role="img"', spark)
        self.assertEqual(json.loads(html_lib.unescape(re.search(r'data-orca-chart="([^"]+)"', spark).group(1)))["values"], [1, 3, 2, 5])
        self.assertEqual(self.render('{% orca_sparkline "4" %}'), "")
        donut = self.render('{% orca_donut "A:3, B:1" total_label="Visitors" %}')
        self.assertIn("A 75%, B 25%", donut)
        self.assertIn("data-orca-chart=", donut)
        self.assertIn(">4<", donut)
        self.assertIn("1,200", self.render('{% orca_donut "A:1200, B:300" %}'))


class PatternTagTests(SimpleTestCase):
    def render(self, src, **ctx):
        return Template("{% load orca %}" + src).render(Context(ctx))

    def test_chart_kinds_render_a_chartjs_canvas_legend_and_data_table(self):
        from orca.samples import SAMPLE

        data = {"bar": "visitors_week", "line": "visitors_hours", "area": "visitors_hours", "pie": "by_entrance",
                "doughnut": "by_entrance", "scatter": "dwell_vs_visits", "bubble": "sites_bubble",
                "radar": "site_scores", "polar": "alerts_by_type"}
        for kind, key in data.items():
            with self.subTest(kind=kind):
                html = self.render(f'{{% orca_chart "{kind}" d title="T" %}}', d=SAMPLE[key])
                self.assertIn(f"orca-chart-frame--{kind}", html)
                spec = json.loads(html_lib.unescape(re.search(r'data-orca-chart="([^"]+)"', html).group(1)))
                self.assertEqual(spec["kind"], kind)
                self.assertTrue(spec["series"] and all(s_["values"] for s_ in spec["series"]))
                self.assertIn('<canvas class="orca-chart" role="img" aria-label="T: ', html)
                self.assertIn("<table", html)
                self.assertNotIn("nan", html.lower().replace("nant", ""))

    def test_chart_accepts_string_data_and_stacking(self):
        html = self.render('{% orca_chart "bar" "labels=Mon,Tue | A=1,2 | B=3,4" stacked=True %}')
        self.assertIn("Mon", html)
        spec = json.loads(html_lib.unescape(re.search(r'data-orca-chart="([^"]+)"', html).group(1)))
        self.assertTrue(spec["stacked"])
        self.assertEqual([s_["values"] for s_ in spec["series"]], [[1, 2], [3, 4]])

    def test_code_font_and_highlighter_are_vendored(self):
        self.assertTrue((ROOT / "orca/static/orca/fonts/JetBrainsMono-Latin-Variable.woff2").exists())
        self.assertIn('font-family: "JetBrains Mono"', CSS)
        self.assertTrue(compute_brand({}).css["light"]["--orca-font-mono"].startswith('"JetBrains Mono"'))
        hl = (ROOT / "orca/static/orca/vendor/highlight.min.js").read_text()
        self.assertIn("Highlight.js v11", hl)
        self.assertIn('registerLanguage("django"', hl)
        self.assertIn("vendor/highlight.min.js", (ROOT / "orca/static/orca/js/orca.js").read_text())

    def test_chartjs_is_vendored_and_loaded_on_demand(self):
        self.assertTrue((ROOT / "orca/static/orca/vendor/chart.umd.js").read_text().startswith("/*!\n * Chart.js v4"))
        js = (ROOT / "orca/static/orca/js/orca.js").read_text()
        self.assertIn('vendor/chart.umd.js', js)
        self.assertIn('canvas[data-orca-chart]', js)

    def test_month_calendar_places_events_and_holidays(self):
        from orca.samples import SAMPLE

        html = self.render('{% orca_month_calendar e month="2026-11" today="2026-11-06" holidays=h %}', e=SAMPLE["events"], h=SAMPLE["holidays"])
        self.assertIn("Weekly review", html)
        self.assertIn("Armistice Day", html)
        self.assertIn("orca-month-view", html)

    def test_week_view_positions_overlaps_side_by_side(self):
        events = [{"title": "A", "start": "2026-11-06T10:00", "end": "2026-11-06T11:30"},
                  {"title": "B", "start": "2026-11-06T10:30", "end": "2026-11-06T11:00"}]
        html = self.render('{% orca_week_view e start="2026-11-06" days=1 today="2026-11-06" now="2026-11-06T10:40" start_hour=8 end_hour=18 %}', e=events)
        widths = re.findall(r"width: ([0-9.]+)%", html)
        self.assertTrue(widths and all(abs(float(w) - 50) < 0.01 for w in widths), widths)
        self.assertIn("orca-timegrid__now", html)

    def test_agenda_and_year_views(self):
        from orca.samples import SAMPLE

        agenda = self.render('{% orca_agenda e start="2026-11-02" days=7 today="2026-11-06" %}', e=SAMPLE["events"])
        self.assertIn("Delivery window", agenda)
        self.assertNotIn("Go-live rehearsal", agenda)  # outside the 7 days
        year = self.render('{% orca_year_view year=2026 events=e today="2026-11-06" %}', e=SAMPLE["events"])
        self.assertEqual(year.count("orca-mini-calendar\""), 12)

    def test_email_frame_inlines_hex_colours(self):
        from django.template.loader import render_to_string

        html = render_to_string("orca/email/base.html", {"title": "Hello", "paragraphs": ["One."], "action_url": "https://x.test/", "action_label": "Open"})
        self.assertNotIn("var(--", html)
        self.assertRegex(html, r"background:#[0-9a-f]{6}")
        self.assertIn("https://x.test/", html)
        preview = self.render('{% orca_email_preview title="Hi" %}')
        self.assertIn("<iframe", preview)
        self.assertIn("sandbox", preview)


class TemplateLevelTests(SimpleTestCase):
    """Level 4: layouts, generic and page-type templates, structural layouts and slots."""

    def blocks_of(self, name, seen=None):
        """Every block name a template offers, following its extends chain."""
        from django.template.loader import get_template

        src = get_template(name).template.source
        found = set(re.findall(r"{%\s*block\s+([a-z_]+)", src))
        parent = re.search(r'{%\s*extends\s+"([^"]+)"', src)
        return found | (self.blocks_of(parent.group(1)) if parent else set())

    def test_every_preview_renders_a_whole_page_with_real_classes(self):
        for el in registry.all_elements("template"):
            if not el.preview:
                continue
            with self.subTest(el=el.id):
                res = self.client.get(reverse("orca:preview", args=[el.id]))
                self.assertEqual(res.status_code, 200)
                html = res.content.decode()
                self.assertIn("<!doctype html>", html.lower())
                for cls in re.findall(r'class="([^"]*)"', html):
                    for name in re.findall(r"\borca-[a-z0-9_-]+", cls):
                        self.assertTrue(name in CSS_CLASSES, f"{el.id}: preview uses unknown class {name}")
                for btn in re.findall(r"<button\b[^>]*>", html):
                    self.assertIn("type=", btn, f"{el.id}: button without type")
                for img in re.findall(r"<img\b[^>]*>", html):
                    self.assertIn("alt=", img, f"{el.id}: img without alt")
                self.assertEqual(html.count('id="main"'), 1 if el.id != "email-layout" else 0, f"{el.id}: one main landmark")

    def test_documented_blocks_exist_in_the_template(self):
        for el in registry.all_elements("template"):
            if el.template:
                with self.subTest(el=el.id):
                    missing = set(el.blocks) - self.blocks_of(el.template)
                    self.assertEqual(missing, set(), f"{el.id}: blocks not in {el.template}")

    def test_every_slot_exists_in_the_layouts(self):
        offered = set()
        for name in ("orca/layouts/app.html", "orca/layouts/marketing.html", "orca/layouts/docs.html", "orca/generic/list.html",
                     "orca/generic/detail.html", "orca/layouts/simple_data.html"):
            offered |= self.blocks_of(name)
        for el in registry.all_elements("template"):
            if el.category == "template-slots":
                self.assertIn(el.blocks[0], offered, f"{el.id}: no layout offers block {el.blocks[0]}")

    def test_error_500_renders_without_a_request(self):
        from django.template.loader import render_to_string

        html = render_to_string("orca/errors/500.html")
        self.assertIn("Something went wrong", html)
        self.assertIn("orca-error-layout", html)

    def test_orca_value_filter(self):
        from orca.templatetags.orca import orca_object_url, orca_value

        class Obj:
            name = "Gate 1"
            active = False
            note = None

            def get_status_display(self):
                return "Online"

        self.assertEqual(orca_value(Obj(), "name"), "Gate 1")
        self.assertEqual(orca_value(Obj(), "status"), "Online")
        self.assertEqual(orca_value(Obj(), "active"), "No")
        self.assertEqual(orca_value(Obj(), "note"), "\u2014")
        self.assertEqual(orca_value({"a": True}, "a"), "Yes")
        self.assertEqual(orca_object_url({"pk": 1}, "#"), "#")
        self.assertEqual(orca_object_url({"pk": 1}, "no-such-url"), "")

    def test_scheduler_and_gantt_positions(self):
        from orca import calendar_views as cv

        sched = cv.scheduler_context([{"name": "Ada Lovelace", "bookings": [{"title": "A", "start": "2026-11-06T10:00", "end": "2026-11-06T11:00"}]}], 8, 18)
        b = sched["rows"][0]["bookings"][0]
        self.assertEqual((b["left"], b["width"]), (20.0, 10.0))
        self.assertEqual(sched["rows"][0]["initials"], "AL")
        g = cv.gantt_context([{"label": "T", "start": "2026-11-02", "end": "2026-11-03"}], start="2026-11-02", days=7, today="2026-11-06")
        self.assertAlmostEqual(g["rows"][0]["width"], 2 / 7 * 100, places=2)
        self.assertIsNotNone(g["today_at"])

    def test_mixin_fills_generic_context(self):
        from types import SimpleNamespace

        from django.views.generic.base import ContextMixin

        from orca.mixins import OrcaPageMixin

        class Field:
            verbose_name = "video name"
            choices = None

        class Meta:
            verbose_name, verbose_name_plural = "video", "videos"

            def get_field(self, name):
                if name == "name":
                    return Field()
                raise LookupError(name)

        class V(OrcaPageMixin, ContextMixin):
            model = SimpleNamespace(_meta=Meta())
            list_columns = ["name", ("Counted today", "today"), "last_seen"]
            create_url_name = "orca:home"

        ctx = V().get_context_data()
        self.assertEqual(ctx["model_name_plural"], "videos")
        self.assertEqual([c["label"] for c in ctx["columns"]], ["Video name", "Counted today", "Last seen"])
        self.assertEqual(ctx["create_url"], reverse("orca:home"))


class ServerCodeTests(SimpleTestCase):
    DATA_TAGS = ("orca_chart", "orca_month_calendar", "orca_week_view", "orca_agenda", "orca_year_view", "orca_scheduler",
                 "orca_gantt", "orca_field", "orca_form_errors", "orca_messages", "orca_pagination", "orca_mini_calendar",
                 "orca_sparkline", "orca_donut", "orca_email_preview")
    POSTS_BACK = ("data-orca-board", "data-orca-zone-editor", "data-orca-richtext", "data-orca-add-row", "data-orca-file-list",
                  "data-orca-autosubmit")

    def test_every_element_that_needs_the_server_documents_it(self):
        missing = []
        for el in registry.all_elements():
            text = " ".join(h for _, h in el.example_list()) + " ".join(el.how)
            needs = any(t in text for t in self.DATA_TAGS + self.POSTS_BACK) or el.context
            if needs and not el.server:
                missing.append(el.id)
        self.assertEqual(missing, [], "elements that read data or post back need server code")

    def test_server_code_compiles_and_its_django_and_orca_imports_exist(self):
        import ast

        for el in registry.all_elements():
            for title, code in el.server:
                with self.subTest(el=el.id, snippet=title):
                    tree = ast.parse(code)
                    imports = [n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))
                               and (getattr(n, "module", "") or n.names[0].name).split(".")[0] in ("django", "orca")]
                    for node in imports:
                        try:
                            exec(compile(ast.Module(body=[node], type_ignores=[]), f"<{el.id}>", "exec"), {})
                        except RuntimeError as exc:  # a contrib app the test settings do not install
                            import importlib.util

                            self.assertIn("INSTALLED_APPS", str(exc))
                            self.assertIsNotNone(importlib.util.find_spec(node.module), node.module)

    def test_element_page_and_markdown_show_it(self):
        res = self.client.get(reverse("orca:element", args=["generic-list"]))
        self.assertContains(res, "Server code")
        self.assertContains(res, 'data-orca-highlight="python"')
        self.assertContains(res, "class VideoList(VideoPages, ListView):")
        from orca.catalogue.render import element_markdown

        md = element_markdown(registry.get("bar-chart"))
        self.assertIn("### Server code", md)
        self.assertIn("```python", md)


class StatCardTests(SimpleTestCase):
    def test_templates_render_the_descriptive_icon_of_each_stat(self):
        from django.template.loader import render_to_string

        stats = [{"label": "Visitors today", "value": "12,480", "icon": "user"}, {"label": "Inside now", "value": "1,204"}]
        for name, key in (("orca/layouts/dashboard.html", "stats"), ("orca/layouts/home.html", "stats"),
                          ("orca/generic/parent_base.html", "parent_stats")):
            with self.subTest(template=name):
                html = render_to_string(name, {key: stats, "title": "T"})
                self.assertEqual(html.count('class="orca-stat-card__icon" aria-hidden="true"'), 1)


class LintTests(SimpleTestCase):
    def test_lint_finds_problems(self):
        with tempfile.TemporaryDirectory() as d:
            bad = Path(d, "bad.html")
            bad.write_text(
                '<div style="color: #ff0000"><button class="orca-icon-button">x</button><img src="a.png">'
                '<span class="orca-buton"></span></div>\n<style>:root { --orca-text: red; --orca-brand: #123456; }</style>\n'
            )
            out = io.StringIO()
            with self.assertRaises(SystemExit):
                call_command("orca_lint", str(bad), stdout=out, stderr=io.StringIO())
            text = out.getvalue()
            for needle in ("hard-coded colour", "without type", "without aria-label", "without alt", "orca-buton", "--orca-text is not a brand token"):
                self.assertIn(needle, text)
            self.assertNotIn("--orca-brand is not", text)

    def test_lint_passes_clean_file(self):
        with tempfile.TemporaryDirectory() as d:
            good = Path(d, "good.html")
            good.write_text('<button class="orca-button orca-button--primary" type="submit">Save image</button>\n')
            out = io.StringIO()
            call_command("orca_lint", str(good), stdout=out)
            self.assertIn("No ORCA problems", out.getvalue())


class BuildAndCliTests(SimpleTestCase):
    def test_generated_files_are_up_to_date(self):
        stale = [str(p) for p, text in build.outputs().items() if not p.exists() or p.read_text(encoding="utf-8") != text]
        self.assertEqual(stale, [], "run `python -m orca build`")

    def test_cli_show(self):
        res = subprocess.run([sys.executable, "-m", "orca", "show", "button"], capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(res.returncode, 0)
        self.assertIn("### Why", res.stdout)
        self.assertIn("### How to use", res.stdout)
