/* ORCA documentation site only: the brand settings generator (guide page "Brand generator").
   It reads the controls inside [data-brand-generator], derives the brand exactly as orca/conf.py does (the colour
   maths below is a port of orca/color.py; tests/test_brand_generator.py compares the two), previews the result on
   this page and writes the ORCA = {...} settings to copy into settings.py.
   Defaults and grounds come from the server as JSON (#brand-generator-data), so nothing is duplicated here.
   Nothing is saved or sent anywhere: reload the page to get the site's own look back. */
(function () {
  "use strict";
  var inBrowser = typeof document !== "undefined";
  var root = inBrowser ? document.querySelector("[data-brand-generator]") : null;
  var dataEl = inBrowser ? document.getElementById("brand-generator-data") : null;
  var DATA = dataEl ? JSON.parse(dataEl.textContent) : null;
  var D = DATA ? DATA.defaults : null;

  /* ------------------------------------------------------------ colour maths (port of orca/color.py) */
  var HEX = /^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$/;
  var RGBA = /^rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*(?:,\s*([\d.]+)\s*)?\)$/;

  function parse(value) {
    var text = String(value).trim(), m = HEX.exec(text);
    if (m) {
      var h = m[1];
      if (h.length === 3) h = h.replace(/./g, function (c) { return c + c; });
      return { rgb: [parseInt(h.slice(0, 2), 16) / 255, parseInt(h.slice(2, 4), 16) / 255, parseInt(h.slice(4, 6), 16) / 255], alpha: 1 };
    }
    m = RGBA.exec(text);
    if (m) return { rgb: [parseFloat(m[1]) / 255, parseFloat(m[2]) / 255, parseFloat(m[3]) / 255], alpha: m[4] !== undefined ? parseFloat(m[4]) : 1 };
    throw new Error("Enter a hex value such as #0f95a1, or rgb(15, 149, 161).");
  }
  // Python's round() sends ties to the even number; Math.round sends them up. Match Python so both always agree.
  function pyRound(x) { var f = Math.floor(x), d = x - f; return d < 0.5 ? f : d > 0.5 ? f + 1 : (f % 2 === 0 ? f : f + 1); }
  function toHex(rgb) {
    return "#" + rgb.map(function (c) { return ("0" + pyRound(Math.max(0, Math.min(1, c)) * 255).toString(16)).slice(-2); }).join("");
  }
  function normalize(value) {
    var p = parse(value);
    if (p.alpha < 1) throw new Error("Use an opaque colour: this one is transparent.");
    return toHex(p.rgb);
  }
  function lin(c) { return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); }
  function luminance(rgb) { return 0.2126 * lin(rgb[0]) + 0.7152 * lin(rgb[1]) + 0.0722 * lin(rgb[2]); }
  function contrast(fg, bg) {
    var f = parse(fg), b = parse(bg).rgb;
    var shown = [0, 1, 2].map(function (i) { return f.rgb[i] * f.alpha + b[i] * (1 - f.alpha); });
    var l1 = luminance(shown), l2 = luminance(b);
    return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
  }
  function mix(a, b, amount) {
    var ra = parse(a).rgb, rb = parse(b).rgb;
    return toHex([0, 1, 2].map(function (i) { return ra[i] * (1 - amount) + rb[i] * amount; }));
  }
  function toward(color, target, bg, ratio) {
    var amount = 0, current = normalize(color);
    while (contrast(current, bg) < ratio && amount < 1) {
      amount = Math.min(1, amount + 0.02);
      current = mix(color, target, amount);
    }
    return current;
  }
  function bestOn(fill) { return contrast("#ffffff", fill) >= contrast("#000000", fill) ? "#ffffff" : "#000000"; }

  /* ------------------------------------------------------------ brand derivation (port of orca/conf.py compute_brand) */
  function has(raw, key) { return Object.prototype.hasOwnProperty.call(raw, key) && raw[key] !== "" && raw[key] != null; }

  function computeBrand(raw) {
    var values = {}, k;
    for (k in D) values[k] = D[k];
    for (k in raw) if (has(raw, k)) values[k] = String(raw[k]).trim();
    ["color", "accent", "accent_dark", "on_color"].forEach(function (key) { if (values[key]) values[key] = normalize(values[key]); });

    var brand = values.color;
    var on = values.on_color || bestOn(brand);
    var strong = toward(brand, on === "#ffffff" ? "#000000" : "#ffffff", on, 4.5);
    var notes = [];
    if (strong !== brand) notes.push("Brand fills use " + strong + " (derived from " + brand + ") so " + on + " text on them reads at 4.5:1.");
    var step = on === "#ffffff" ? "#000000" : "#ffffff";
    var hover = mix(strong, step, 0.12), active = mix(strong, step, 0.2);
    var bar = toward(mix(brand, "#000000", 0.30), "#000000", "#ffffff", 4.5);

    var accent = values.accent, accentOk = accent;
    DATA.grounds.light.concat(DATA.grounds.paper).forEach(function (g) { accentOk = toward(accentOk, "#000000", g, 4.5); });
    if (accentOk !== accent) notes.push("The accent " + accent + " was darkened to " + accentOk + " to read at 4.5:1 on the light and paper grounds.");

    var accentDark;
    if (has(raw, "accent_dark")) accentDark = values.accent_dark;
    else if (has(raw, "accent")) {
      accentDark = accent;
      DATA.grounds.dark.forEach(function (g) { accentDark = toward(accentDark, "#ffffff", g, 4.5); });
    } else accentDark = values.accent_dark;
    var darkOk = accentDark;
    DATA.grounds.dark.forEach(function (g) { darkOk = toward(darkOk, "#ffffff", g, 4.5); });
    if (darkOk !== accentDark && has(raw, "accent_dark")) notes.push("The dark accent " + accentDark + " was lightened to " + darkOk + " to read at 4.5:1 on the dark grounds.");

    var common = {
      "--orca-brand": brand, "--orca-brand-strong": strong, "--orca-brand-strong-hover": hover, "--orca-brand-strong-active": active,
      "--orca-brand-on": on, "--orca-brand-bar": bar,
      "--orca-brand-bar-hover": toward(mix(bar, "#ffffff", 0.14), "#000000", "#ffffff", 4.5),
      "--orca-brand-bar-active": toward(mix(bar, "#ffffff", 0.22), "#000000", "#ffffff", 4.5),
      "--orca-brand-bar-on": "#ffffff", "--orca-font-sans": values.font_sans, "--orca-font-mono": values.font_mono
    };
    function extend(extra) { var o = {}, key; for (key in common) o[key] = common[key]; for (key in extra) o[key] = extra[key]; return o; }
    return {
      values: { color: brand, strong: strong, on: on, bar: bar, accent: accentOk, accentDark: darkOk },
      notes: notes,
      css: {
        light: extend({ "--orca-accent": accentOk, "--orca-accent-hover": mix(accentOk, "#000000", 0.15) }),
        dark: extend({ "--orca-accent": darkOk, "--orca-accent-hover": mix(darkOk, "#ffffff", 0.15) })
      }
    };
  }

  function brandStyle(css) {
    function block(sel, decls) { return sel + " { " + Object.keys(decls).map(function (k) { return k + ": " + decls[k] + ";"; }).join(" ") + " }"; }
    return [
      block(":root", css.light),
      "@media (prefers-color-scheme: dark) { " + block(':root:not([data-theme="light"]):not([data-theme="paper"])', css.dark) + " }",
      block(':root[data-theme="dark"]', css.dark)
    ].join("\n");
  }

  /* Node (the parity test) gets the maths only: it sets the server data itself, then calls computeBrand. */
  if (!root || !DATA) {
    if (typeof module !== "undefined") module.exports = { computeBrand: computeBrand, brandStyle: brandStyle, normalize: normalize, setData: function (d) { DATA = d; D = d.defaults; } };
    return;
  }
  var doc = document, html = doc.documentElement;

  /* ------------------------------------------------------------ the form */
  function $(sel) { return root.querySelector(sel); }
  function $$(sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  var FONT = /^[\p{L}\p{N}_\s",\-.]+$/u;

  var colorFields = ["color", "accent", "accent_dark"].map(function (key) {
    var id = "bg-" + key.replace("_", "-");
    return { key: key, text: $("#" + id), pick: $("#" + id + "-pick"), error: $("#" + id + "-error") };
  });
  var fontFields = [
    { key: "font_sans", input: $("#bg-font-sans"), error: $("#bg-font-sans-error") },
    { key: "font_mono", input: $("#bg-font-mono"), error: $("#bg-font-mono-error") }
  ];
  var els = {
    name: $("#bg-name"), on: $("#bg-on"), darkCustom: $("#bg-dark-custom"), darkRow: $("#bg-dark-row"),
    logo: $("#bg-logo"), favicon: $("#bg-favicon"), docs: $("#bg-docs"),
    code: $("#bg-code"), copy: $("#bg-copy"), status: $("#bg-status"), notes: $("#bg-notes"), notesList: $("#bg-notes-list"),
    previewName: $("#bg-preview-name"), table: $("#bg-derived")
  };
  var initial = { theme: html.getAttribute("data-theme"), density: html.getAttribute("data-density") };
  var styleEl = null;

  function radio(name) { var r = root.querySelector('input[name="' + name + '"]:checked'); return r ? r.value : ""; }
  function setRadio(name, value) { $$('input[name="' + name + '"]').forEach(function (r) { r.checked = r.value === value; }); }

  function showError(field, input, message) {
    var bad = !!message;
    field.error.hidden = !bad;
    field.error.querySelector("span").textContent = message || "";
    input.setAttribute("aria-invalid", bad ? "true" : "false");
    var ids = (input.getAttribute("data-help") || "").split(" ").filter(Boolean);
    if (bad) ids.unshift(field.error.id);
    if (ids.length) input.setAttribute("aria-describedby", ids.join(" ")); else input.removeAttribute("aria-describedby");
  }

  /* Reads every control. Returns the BRAND settings that will be written, and whether all values are valid. */
  function read() {
    var raw = {}, valid = true;
    var name = els.name.value.trim();
    if (name) raw.name = name;
    colorFields.forEach(function (f) {
      var skip = f.key === "accent_dark" && !els.darkCustom.checked;
      var message = "";
      if (!skip) {
        try {
          var hex = normalize(f.text.value);
          if (f.key === "color" || hex !== D[f.key]) raw[f.key] = hex;
        } catch (e) { message = e.message; valid = false; }
      }
      showError(f, f.text, message);
    });
    if (els.on.value) raw.on_color = els.on.value;
    if (els.logo.value.trim()) raw.logo = els.logo.value.trim();
    if (els.favicon.value.trim()) raw.favicon = els.favicon.value.trim();
    fontFields.forEach(function (f) {
      var v = f.input.value.trim(), message = "";
      if (v && v !== D[f.key]) {
        if (FONT.test(v)) raw[f.key] = v;
        else { message = "Use a CSS font stack such as \"Inter\", sans-serif: letters, digits, spaces, quotes, commas and hyphens only."; valid = false; }
      }
      showError(f, f.input, message);
    });
    return { raw: raw, valid: valid };
  }

  /* ------------------------------------------------------------ the settings text */
  function py(s) { return s.indexOf('"') !== -1 && s.indexOf("'") === -1 ? "'" + s + "'" : JSON.stringify(s); }

  function lines(entries, indent) {
    var width = 0;
    entries.forEach(function (e) { if (e.comment) width = Math.max(width, e.text.length); });
    return entries.map(function (e) {
      return indent + (e.comment ? e.text + new Array(width - e.text.length + 3).join(" ") + "# " + e.comment : e.text);
    });
  }

  function settingsText(raw) {
    var order = ["name", "color", "logo", "favicon", "on_color", "accent", "accent_dark", "font_sans", "font_mono"];
    var comments = { logo: "in your STATICFILES" };
    var brand = order.filter(function (k) { return has(raw, k); })
      .map(function (k) { return { text: '"' + k + '": ' + py(raw[k]) + ",", comment: comments[k] }; });
    var theme = radio("bg-theme") || "auto", density = radio("bg-density") || "comfortable";
    var outer = [
      { text: '"THEME": ' + py(theme) + ",", comment: "auto, light, dark or paper" },
      { text: '"DENSITY": ' + py(density) + ",", comment: density === "dense" ? 'or "comfortable"' : 'or "dense"' },
      { text: '"DOCS_ENABLED": ' + (els.docs.checked ? "True" : "False") + ",", comment: "serve this documentation in your project" }
    ];
    return ["ORCA = {", '    "BRAND": {'].concat(lines(brand, "        "), ["    },"], lines(outer, "    "), ["}"]).join("\n");
  }

  /* ------------------------------------------------------------ preview and read-outs */
  function ratio(fg, bg) { return contrast(fg, bg).toFixed(1) + ":1"; }

  function rows(b, raw) {
    var v = b.values;
    var minAccent = Math.min.apply(null, DATA.grounds.light.concat(DATA.grounds.paper).map(function (g) { return contrast(v.accent, g); }));
    var minDark = Math.min.apply(null, DATA.grounds.dark.map(function (g) { return contrast(v.accentDark, g); }));
    return [
      { name: "Brand colour", hex: v.color, note: "Used as given on decorative marks and bars.", ratio: "", adjusted: false },
      { name: "Brand fill", hex: v.strong, note: "Buttons and badges, with " + v.on + " text.", ratio: ratio(v.on, v.strong), adjusted: v.strong !== v.color },
      { name: "Top bar", hex: v.bar, note: "The brand mixed with 30% black, white text.", ratio: ratio("#ffffff", v.bar), adjusted: false },
      { name: "Accent, light and paper", hex: v.accent, note: "Links, checked controls, progress.", ratio: minAccent.toFixed(1) + ":1", adjusted: raw.accent ? v.accent !== raw.accent : v.accent !== D.accent },
      { name: "Accent, dark", hex: v.accentDark, note: "The same, on the dark grounds.", ratio: minDark.toFixed(1) + ":1", adjusted: raw.accent_dark ? v.accentDark !== raw.accent_dark : false }
    ];
  }

  function renderRows(list) {
    var body = els.table.querySelector("tbody");
    body.textContent = "";
    list.forEach(function (r) {
      var tr = doc.createElement("tr");
      var th = doc.createElement("th"); th.scope = "row"; th.className = "orca-table__name";
      var wrap = doc.createElement("span"); wrap.className = "orca-with-icon";
      var sw = doc.createElement("span"); sw.className = "orca-swatch"; sw.setAttribute("aria-hidden", "true"); sw.style.setProperty("--orca-swatch", r.hex);
      wrap.appendChild(sw); wrap.appendChild(doc.createTextNode(r.name)); th.appendChild(wrap);
      var code = doc.createElement("td"); var c = doc.createElement("code"); c.className = "orca-code"; c.textContent = r.hex; code.appendChild(c);
      var ratioCell = doc.createElement("td"); ratioCell.textContent = r.ratio || "Not text";
      var note = doc.createElement("td"); note.className = "orca-small"; note.textContent = r.note;
      if (r.adjusted) { var badge = doc.createElement("span"); badge.className = "orca-badge orca-badge--caution"; badge.textContent = "Adjusted"; note.appendChild(doc.createTextNode(" ")); note.appendChild(badge); }
      [th, code, ratioCell, note].forEach(function (td) { tr.appendChild(td); });
      body.appendChild(tr);
    });
  }

  function applyPage(b) {
    if (!styleEl) { styleEl = doc.createElement("style"); styleEl.id = "brand-generator-style"; doc.head.appendChild(styleEl); }
    styleEl.textContent = brandStyle(b.css);
    var theme = radio("bg-theme");
    if (theme && theme !== "auto") html.setAttribute("data-theme", theme);
    else if (theme === "auto" && root.hasAttribute("data-touched-theme")) { if (initial.theme) html.setAttribute("data-theme", initial.theme); else html.removeAttribute("data-theme"); }
    if (root.hasAttribute("data-touched-density")) html.setAttribute("data-density", radio("bg-density"));
  }

  var lastValid = "";
  function update() {
    var s = read();
    els.status.textContent = "";
    if (!s.valid) {
      els.copy.disabled = true;
      els.code.closest(".orca-code-block").setAttribute("data-invalid", "");
      els.status.textContent = "Fix the highlighted fields to update the settings.";
      return;
    }
    els.copy.disabled = false;
    els.code.closest(".orca-code-block").removeAttribute("data-invalid");
    var b = computeBrand(s.raw);
    applyPage(b);
    renderRows(rows(b, s.raw));
    els.notes.hidden = !b.notes.length;
    els.notesList.textContent = "";
    b.notes.forEach(function (n) { var li = doc.createElement("li"); li.textContent = n; els.notesList.appendChild(li); });
    els.previewName.textContent = els.name.value.trim() || D.name;
    var text = settingsText(s.raw);
    if (text !== lastValid) {
      lastValid = text;
      els.code.textContent = text;
      els.code.removeAttribute("data-highlighted");
      if (window.hljs) try { window.hljs.highlightElement(els.code); } catch (e) { /* plain text stays */ }
    }
  }

  /* ------------------------------------------------------------ wiring */
  colorFields.forEach(function (f) {
    f.pick.addEventListener("input", function () { f.text.value = f.pick.value; update(); });
    f.text.addEventListener("input", function () { try { f.pick.value = normalize(f.text.value); } catch (e) { /* the error shows from update() */ } update(); });
  });
  els.darkCustom.addEventListener("change", function () { els.darkRow.hidden = !els.darkCustom.checked; update(); });
  root.addEventListener("change", function (e) {
    var n = e.target.name;
    if (n === "bg-theme") root.setAttribute("data-touched-theme", "");
    if (n === "bg-density") root.setAttribute("data-touched-density", "");
    update();
  });
  root.addEventListener("input", function (e) { if (e.target.type !== "radio") update(); });

  $$("[data-brand-preset]").forEach(function (b) {
    var c = b.getAttribute("data-brand-preset");
    b.querySelector(".orca-swatch").style.setProperty("--orca-swatch", c);
    b.addEventListener("click", function () {
      var f = colorFields[0]; f.text.value = c; f.pick.value = c;
      $$("[data-brand-preset]").forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
      update();
    });
  });
  colorFields[0].text.addEventListener("input", function () {
    $$("[data-brand-preset]").forEach(function (o) { o.setAttribute("aria-pressed", "false"); });
  });

  var reset = $("[data-brand-reset]");
  reset.addEventListener("click", function () {
    var f = root.querySelector("form"); f.reset();
    colorFields.forEach(function (c) { c.pick.value = c.text.value; });
    els.darkRow.hidden = true;
    $$("[data-brand-preset]").forEach(function (o) { o.setAttribute("aria-pressed", "false"); });
    if (styleEl) { styleEl.remove(); styleEl = null; }
    if (initial.theme) html.setAttribute("data-theme", initial.theme); else html.removeAttribute("data-theme");
    if (initial.density) html.setAttribute("data-density", initial.density); else html.removeAttribute("data-density");
    root.removeAttribute("data-touched-theme"); root.removeAttribute("data-touched-density");
    lastValid = "";
    update();
    els.status.textContent = "Reset to the ORCA defaults.";
  });
  root.querySelector("form").addEventListener("submit", function (e) { e.preventDefault(); });

  update();
  window.addEventListener("load", function () { lastValid = ""; update(); });
})();
