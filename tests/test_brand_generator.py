"""The docs-site brand generator: the page, the classes it uses and its JavaScript colour maths."""

import json
import random
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from django.test import SimpleTestCase
from django.urls import reverse

from orca import conf, tokens
from orca.conf import compute_brand
from orca.views import BRAND_PRESETS

ROOT = Path(__file__).resolve().parent.parent
JS = ROOT / "orca/static/orca/js/brand-generator.js"
CSS = "".join((ROOT / f"orca/static/orca/css/{n}.css").read_text() for n in ("orca", "components", "patterns", "templates"))
CSS_CLASSES = {m[1:] for m in re.findall(r"\.orca-[a-z0-9_-]+", CSS)}


class BrandGeneratorPageTests(SimpleTestCase):
    def setUp(self):
        self.html = self.client.get(reverse("orca:guide", args=["brand-generator"])).content.decode()

    def test_page_and_script(self):
        self.assertIn("brand-generator.js", self.html)
        self.assertIn("data-brand-generator", self.html)
        self.assertIn('href="/orca/guide/brand-generator/"', self.html)  # in the docs sidebar

    def test_server_data_matches_the_python_settings(self):
        data = json.loads(re.search(r'<script id="brand-generator-data" type="application/json">(.*?)</script>', self.html, re.S).group(1))
        self.assertEqual(data["defaults"], {t.key: t.default for t in tokens.BRAND_TOKENS})
        self.assertEqual(data["grounds"], {"light": list(conf.LIGHT_GROUNDS), "paper": list(conf.PAPER_GROUNDS), "dark": list(conf.DARK_GROUNDS)})

    def test_every_class_exists_and_every_field_is_labelled(self):
        for cls in set(re.findall(r'class="([^"]+)"', self.html)):
            for name in cls.split():
                if name.startswith("orca-"):
                    self.assertIn(name, CSS_CLASSES, f"unknown class {name}")
        for field in re.findall(r'<(?:input|select)\b[^>]*\bid="(bg-[a-z-]+)"', self.html):
            if field.endswith("-pick"):
                continue
            wrapped = re.search(rf'<label[^>]*>\s*<input[^>]*\bid="{field}"', self.html)
            self.assertTrue(f'for="{field}"' in self.html or wrapped, f"{field} has no label")

    def test_presets_are_valid_brand_colours(self):
        for name, hex_ in BRAND_PRESETS:
            with self.subTest(name=name):
                self.assertEqual(compute_brand({"color": hex_}).errors, [])
                self.assertIn(f'data-brand-preset="{hex_}"', self.html)

    def test_initial_code_is_what_the_script_writes_for_the_defaults(self):
        self.assertIn('"name": "Acme",', self.html)
        self.assertIn('"color": "#0f95a1",', self.html)


NODE = shutil.which("node")


class BrandGeneratorParityTests(SimpleTestCase):
    """The page previews the brand with JavaScript; it must equal what ORCA's Python computes from the same settings."""

    def test_javascript_matches_python(self):
        if not NODE:
            self.skipTest("node is not installed")
        rng = random.Random(7)
        cases = [{"color": "#0f95a1"}, {"color": "#ffffff"}, {"color": "#000000"}, {"color": "#7fb2ff", "accent": "#7fb2ff"}]
        for _ in range(250):
            raw = {"color": "#%06x" % rng.randrange(1 << 24)}
            if rng.random() < 0.5:
                raw["accent"] = "#%06x" % rng.randrange(1 << 24)
            if rng.random() < 0.3:
                raw["accent_dark"] = "#%06x" % rng.randrange(1 << 24)
            if rng.random() < 0.3:
                raw["on_color"] = rng.choice(["#ffffff", "#000000"])
            cases.append(raw)
        data = {"defaults": {t.key: t.default for t in tokens.BRAND_TOKENS},
                "grounds": {"light": list(conf.LIGHT_GROUNDS), "paper": list(conf.PAPER_GROUNDS), "dark": list(conf.DARK_GROUNDS)}}
        runner = (
            "const lib = require(process.argv[2]); const input = JSON.parse(require('fs').readFileSync(0, 'utf8'));"
            "lib.setData(input.data);"
            "console.log(JSON.stringify(input.cases.map(c => { const b = lib.computeBrand(c); return {css: b.css, notes: b.notes, style: lib.brandStyle(b.css)}; })));"
        )
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "run.js"
            script.write_text(runner)
            out = subprocess.run([NODE, str(script), str(JS)], input=json.dumps({"data": data, "cases": cases}), capture_output=True, text=True, check=True)
        for raw, js in zip(cases, json.loads(out.stdout)):
            with self.subTest(raw=raw):
                py = compute_brand(raw)
                self.assertEqual(js["css"], py.css)
                self.assertEqual(js["notes"], py.notes)
                self.assertEqual(js["style"], conf.brand_style(py))
