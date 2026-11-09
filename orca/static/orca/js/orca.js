/* ORCA primitives: progressive enhancement only. Every primitive works without this file.
   Behaviours are opt-in through data attributes, so nothing runs on markup that did not ask for it:
     data-orca-clear           search clear button empties its input and returns focus
     data-orca-step="-1|1"     number stepper buttons
     data-orca-otp             OTP digit boxes: advance, backspace, paste a whole code
     data-orca-toggle          aria-pressed toggle buttons (pin, toggle, tag)
     data-orca-theme-toggle    cycles light / dark / paper and remembers the choice
     data-orca-countdown       live countdown to the ISO time in its datetime attribute
     data-orca-copy            copies the text of the element named by its value (id)
     data-orca-open="id"       opens the <dialog> (dialog or drawer) with that id as a modal; sets aria-expanded
     data-orca-close           closes the dialog it is in; pressing a drawer's backdrop closes it too */
(function () {
  "use strict";
  var THEME_KEY = "orca-theme";

  function closest(el, sel) { return el && el.closest ? el.closest(sel) : null; }

  document.addEventListener("click", function (event) {
    var t = event.target;
    var opener = closest(t, "[data-orca-open]");
    if (opener) {
      var dlg = document.getElementById(opener.getAttribute("data-orca-open"));
      if (dlg && dlg.showModal && !dlg.open) {
        dlg.showModal();
        opener.setAttribute("aria-expanded", "true");
        dlg.addEventListener("close", function () { opener.setAttribute("aria-expanded", "false"); }, { once: true });
      }
      return;
    }
    var closer = closest(t, "[data-orca-close]");
    if (closer) {
      var host = closest(closer, "dialog");
      if (host) host.close();
      return;
    }
    if (t.matches && t.matches("dialog.orca-drawer[open]")) {
      /* A click on the dialog box itself, not on its content, is a click on the backdrop. */
      var box = t.getBoundingClientRect();
      if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) t.close();
      return;
    }
    var clear = closest(t, "[data-orca-clear]");
    if (clear) {
      var input = clear.parentElement.querySelector("input");
      if (input) { input.value = ""; input.dispatchEvent(new Event("input", { bubbles: true })); input.focus(); }
      return;
    }
    var step = closest(t, "[data-orca-step]");
    if (step) {
      var field = step.parentElement.querySelector("input[type=number], input[inputmode=numeric]");
      if (field) {
        var by = parseFloat(step.getAttribute("data-orca-step")) * (parseFloat(field.step) || 1);
        var next = (parseFloat(field.value) || 0) + by;
        if (field.min !== "" && next < parseFloat(field.min)) next = parseFloat(field.min);
        if (field.max !== "" && next > parseFloat(field.max)) next = parseFloat(field.max);
        field.value = next;
        field.dispatchEvent(new Event("change", { bubbles: true }));
      }
      return;
    }
    var toggle = closest(t, "[data-orca-toggle]");
    if (toggle) {
      var on = toggle.getAttribute("aria-pressed") !== "true";
      toggle.setAttribute("aria-pressed", on ? "true" : "false");
      var label = toggle.getAttribute(on ? "data-orca-label-on" : "data-orca-label-off");
      if (label) {
        if (toggle.hasAttribute("aria-label")) toggle.setAttribute("aria-label", label);
        else { var text = toggle.querySelector("[data-orca-toggle-text]"); if (text) text.textContent = label; }
      }
      return;
    }
    var theme = closest(t, "[data-orca-theme-toggle]");
    if (theme) {
      var order = ["light", "dark", "paper"];
      var current = document.documentElement.getAttribute("data-theme") ||
        (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      var nextTheme = order[(order.indexOf(current) + 1) % order.length];
      document.documentElement.setAttribute("data-theme", nextTheme);
      try { localStorage.setItem(THEME_KEY, nextTheme); } catch (e) { /* storage blocked: keep for this page */ }
      theme.setAttribute("aria-label", "Theme: " + nextTheme + ". Change theme");
      return;
    }
    var copy = closest(t, "[data-orca-copy]");
    if (copy && navigator.clipboard) {
      var source = document.getElementById(copy.getAttribute("data-orca-copy"));
      if (source) navigator.clipboard.writeText(source.textContent.trim()).then(function () {
        var old = copy.textContent; copy.textContent = "Copied";
        setTimeout(function () { copy.textContent = old; }, 1500);
      });
    }
  });

  /* OTP: one digit per box, auto-advance, backspace goes back, paste fills every box */
  document.addEventListener("input", function (event) {
    var box = event.target;
    if (!box.matches || !box.matches("[data-orca-otp] input")) return;
    box.value = box.value.replace(/\D/g, "").slice(-1);
    if (box.value) { var next = box.nextElementSibling; while (next && next.tagName !== "INPUT") next = next.nextElementSibling; if (next) next.focus(); }
  });
  document.addEventListener("keydown", function (event) {
    var box = event.target;
    if (event.key !== "Backspace" || !box.matches || !box.matches("[data-orca-otp] input") || box.value) return;
    var prev = box.previousElementSibling; while (prev && prev.tagName !== "INPUT") prev = prev.previousElementSibling;
    if (prev) { prev.focus(); prev.value = ""; event.preventDefault(); }
  });
  document.addEventListener("paste", function (event) {
    var box = event.target;
    if (!box.matches || !box.matches("[data-orca-otp] input")) return;
    var digits = (event.clipboardData || window.clipboardData).getData("text").replace(/\D/g, "");
    if (!digits) return;
    event.preventDefault();
    var boxes = box.closest("[data-orca-otp]").querySelectorAll("input");
    boxes.forEach(function (b, i) { b.value = digits[i] || ""; });
    boxes[Math.min(digits.length, boxes.length) - 1].focus();
  });

  /* Countdowns: update once a second, announce politely only at whole minutes (role=timer is silent by default) */
  function tick() {
    document.querySelectorAll("[data-orca-countdown]").forEach(function (el) {
      var end = Date.parse(el.getAttribute("datetime"));
      if (isNaN(end)) return;
      var s = Math.max(0, Math.round((end - Date.now()) / 1000));
      var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = s % 60;
      el.textContent = (h ? h + ":" + String(m).padStart(2, "0") : m) + ":" + String(sec).padStart(2, "0");
      el.classList.toggle("orca-countdown--urgent", s > 0 && s <= 60);
    });
  }
  if (document.querySelector("[data-orca-countdown]")) { tick(); setInterval(tick, 1000); }
})();
