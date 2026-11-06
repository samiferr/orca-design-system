import io
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
CSS = (ROOT / "orca/static/orca/css/orca.css").read_text()
TOKENS_CSS = (ROOT / "orca/static/orca/css/tokens.css").read_text()
CSS_CLASSES = set(m[1:] for m in re.findall(r"\.orca-[a-z0-9_-]+", CSS))
CSS_TOKENS = set(re.findall(r"--orca-([a-z0-9-]+)\s*:", TOKENS_CSS))


class GuideCoverageTests(SimpleTestCase):
    def test_every_primitive_of_the_guide_is_covered_once(self):
        covered = {}
        for el in registry.all_elements():
            for item in el.guide:
                covered.setdefault(item, []).append(el.id)
        guide = [item for _, item in all_items()]
        self.assertEqual([i for i in guide if i not in covered], [], "guide items with no element")
        self.assertEqual({k: v for k, v in covered.items() if len(v) > 1}, {}, "guide items claimed twice")
        self.assertEqual([k for k in covered if k not in guide], [], "element.guide entries not in the guide")


class CatalogueTests(SimpleTestCase):
    def test_every_element_has_why_when_how_and_an_example(self):
        for el in registry.all_elements():
            with self.subTest(el=el.id):
                self.assertTrue(re.fullmatch(r"[a-z0-9-]+", el.id))
                self.assertGreater(len(el.summary), 10)
                self.assertGreater(len(el.why), 40)
                self.assertTrue(el.when and el.how and el.examples)
                self.assertTrue(el.laws, "every element names the principle it applies")
                self.assertEqual(el.level, "primitive")

    def test_principles_are_known(self):
        for el in registry.all_elements():
            for key in el.laws:
                self.assertTrue(key in registry.LAWS or key in registry.PRACTICAL_UI, f"{el.id}: unknown principle {key}")

    def test_related_ids_exist(self):
        for el in registry.all_elements():
            for rid in el.related:
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
        local = {"ratio", "value", "swatch", "zone", "event"}  # per-element custom properties set inline
        self.assertEqual(sorted(used - CSS_TOKENS - local), [])


class ContrastTests(SimpleTestCase):
    GROUNDS = ("bg", "bg-alt", "bg-input")

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
        for name in ("index", "tokens", "icons", "catalogue-json"):
            with self.subTest(name=name):
                self.assertEqual(self.client.get(reverse(f"orca:{name}")).status_code, 200)

    def test_every_element_page(self):
        for el in registry.all_elements():
            with self.subTest(el=el.id):
                res = self.client.get(reverse("orca:element", args=[el.id]))
                self.assertEqual(res.status_code, 200)
                self.assertNotContains(res, "Example failed to render")
                self.assertContains(res, "Why")

    def test_unknown_element_404(self):
        self.assertEqual(self.client.get("/orca/nope/").status_code, 404)

    @override_settings(ORCA={"DOCS_ENABLED": False})
    def test_disabled(self):
        self.assertEqual(self.client.get(reverse("orca:index")).status_code, 404)


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
            good.write_text('<button class="orca-button orca-button--primary" type="submit">Save camera</button>\n')
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
