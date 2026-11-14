/* ORCA: progressive enhancement only. Every element still works, or degrades to a plain form, without this file.
   Behaviours are opt-in through data attributes, so nothing runs on markup that did not ask for it.

   Primitives
     data-orca-clear            search clear button empties its input and returns focus
     data-orca-step="-1|1"      number stepper buttons
     data-orca-otp              OTP digit boxes: advance, backspace, paste a whole code
     data-orca-toggle           aria-pressed toggle buttons (pin, toggle, tag); data-orca-label-on / -off
     data-orca-theme-toggle     cycles light / dark / paper and remembers the choice
     data-orca-countdown        live countdown to the ISO time in its datetime attribute
     data-orca-copy="id"        copies the text of the element with that id; says "Copied" and shows its check icon
     data-orca-highlight="lang" code coloured by the vendored highlight.js (loaded on demand); empty: detect the language
   Components
     data-orca-menu             button that opens the [role=menu] it controls (aria-controls)
     data-orca-listbox          dropdown select: button + [role=listbox] + hidden input
     data-orca-combobox         input[role=combobox] filtering the [role=listbox] it controls
     data-orca-tabs             [role=tablist] container: arrow keys, Home/End, panel switching
     data-orca-dialog-open="id" / data-orca-dialog-close   open and close a <dialog>
     data-orca-confirm="text"   on a form or submit button: ask in a dialog first
     data-orca-dismiss          closes the closest alert, toast or callout
     data-orca-disclose         aria-expanded button that shows/hides the element it controls
     data-orca-set-date="+n"    sets the date input named by aria-controls to today + n days
     data-orca-range            fieldset with two date or time inputs: keeps end >= start, shows duration
     data-orca-detect-tz        button that selects the browser's timezone in the select it controls
     data-orca-add-row="tpl"    clones <template id=tpl> into the list it controls
     data-orca-remove-row       removes its closest [data-orca-row]
     data-orca-weekdays="mon,…" sets the weekday toggles in the fieldset it controls
     data-orca-reveal="id" data-orca-reveal-value="custom"   select that shows an element for one value
     data-orca-filter-list="id" input filtering the <li> of a list
     data-orca-tree-toggle      aria-controls=tree id: button that collapses every section of a nav tree, or expands them when all are closed
     data-orca-carousel         carousel: prev/next, dots, count
     data-orca-file-list="id"   file input listing chosen files in a list
     data-orca-autosubmit       select or input that submits its form on change
     data-orca-theme-choice     radio group choosing auto / light / dark / paper
   Patterns
     data-orca-sidebar-toggle   collapses/expands the sidebar it controls and remembers it
     data-orca-sidebar-open     on phones, shows/hides the sidebar it controls over the page (Escape closes)
     data-orca-light-dismiss    on a <dialog>: a click on the backdrop closes it (drawers)
     data-orca-richtext         rich text editor: toolbar commands, pressed states, syncs to a hidden field
     data-orca-zone-editor      draw a polygon on an image; points saved as JSON in a hidden field
     data-orca-toc="id"         "On this page" <details>: lists the h2 headings of the element with that id (when the list is empty), marks the
                                section being read with aria-current="location", and is closed on narrow screens, open on wide ones
     data-orca-seek="s"         jumps the video it controls to s seconds
     data-orca-gallery          thumbnails swap the stage image
     data-orca-token="--name"   input that sets a CSS custom property on the element it controls (live token preview)
     data-orca-board            drag cards between [data-orca-column] lists; fires "orca:moved"
     data-orca-chart='{spec}'   canvas drawn by Chart.js (loaded on demand) in token colours; redrawn on theme change
   API
     window.ORCA.toast("Report sent", {tone: "positive", action: {label: "Undo", onClick}})            */
(function () {
  "use strict";
  var THEME_KEY = "orca-theme";
  var doc = document;

  function closest(el, sel) { return el && el.closest ? el.closest(sel) : null; }
  function byId(id) { return id ? doc.getElementById(id) : null; }
  /* Where this file was loaded from: the vendored Chart.js sits next to it (static/orca/vendor/). */
  var SELF_SRC = (document.currentScript && document.currentScript.src) || "";
  function controlled(el) { return byId(el.getAttribute("aria-controls")); }
  function fire(el, type) { el.dispatchEvent(new Event(type, { bubbles: true })); }
  function today(offset) {
    var d = new Date(); d.setDate(d.getDate() + (offset || 0));
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }
  var liveRegion;
  function announce(text) {
    if (!liveRegion) {
      liveRegion = doc.createElement("div");
      liveRegion.className = "orca-sr-only"; liveRegion.setAttribute("role", "status");
      doc.body.appendChild(liveRegion);
    }
    liveRegion.textContent = ""; setTimeout(function () { liveRegion.textContent = text; }, 50);
  }

  /* ---------------------------------------------------------------- popovers (menu, listbox) */
  var openPopover = null;
  function closePopover(focusTrigger) {
    if (!openPopover) return;
    openPopover.list.hidden = true;
    openPopover.trigger.setAttribute("aria-expanded", "false");
    if (focusTrigger) openPopover.trigger.focus();
    openPopover = null;
  }
  function openList(trigger, list, focusFirst) {
    closePopover(false);
    list.hidden = false; trigger.setAttribute("aria-expanded", "true");
    openPopover = { trigger: trigger, list: list };
    var items = items_(list);
    var target = list.querySelector('[aria-selected="true"]') || (focusFirst === "last" ? items[items.length - 1] : items[0]);
    if (target) focusItem(list, target);
  }
  function items_(list) {
    return Array.prototype.filter.call(list.querySelectorAll('[role=menuitem],[role=option],[role=menuitemradio],[role=menuitemcheckbox]'),
      function (i) { return !i.hidden && i.getAttribute("aria-disabled") !== "true" && !i.disabled && !closest(i, "[hidden]"); });
  }
  function focusItem(list, item) { item.focus(); }
  function moveIn(list, current, delta) {
    var items = items_(list); if (!items.length) return null;
    var i = items.indexOf(current);
    var next = delta === "first" ? items[0] : delta === "last" ? items[items.length - 1] : items[(i + delta + items.length) % items.length];
    focusItem(list, next); return next;
  }
  function activeOption(list) { return list.contains(doc.activeElement) ? doc.activeElement : null; }
  function chooseOption(wrap, option) {
    var button = wrap.querySelector("[data-orca-listbox]");
    var list = controlled(button);
    list.querySelectorAll("[role=option]").forEach(function (o) { o.setAttribute("aria-selected", o === option ? "true" : "false"); });
    var value = button.querySelector(".orca-picker-btn__value");
    if (value) { value.textContent = option.getAttribute("data-label") || option.textContent.trim(); value.classList.remove("orca-picker-btn__value--placeholder"); }
    var input = wrap.querySelector("input[type=hidden]");
    if (input) { input.value = option.getAttribute("data-value"); fire(input, "change"); }
    closePopover(true);
  }

  /* ---------------------------------------------------------------- dialogs */
  function openDialog(dialog, opener) {
    if (!dialog || dialog.open) return;
    dialog._orcaOpener = opener || doc.activeElement;
    if (dialog.showModal) dialog.showModal(); else dialog.setAttribute("open", "");
  }
  doc.addEventListener("close", function (e) {
    var d = e.target;
    if (d && d._orcaOpener && d._orcaOpener.focus) d._orcaOpener.focus();
  }, true);

  var confirmDialog;
  function confirmFirst(text, title, action, onYes) {
    if (!confirmDialog) {
      confirmDialog = doc.createElement("dialog");
      confirmDialog.className = "orca-dialog";
      confirmDialog.setAttribute("aria-labelledby", "orca-confirm-title");
      confirmDialog.innerHTML = '<form method="dialog"><div class="orca-dialog__header"><h2 class="orca-dialog-title" id="orca-confirm-title"></h2></div>' +
        '<div class="orca-dialog__body"><p class="orca-p" data-text></p></div><div class="orca-dialog__footer">' +
        '<button class="orca-button orca-button--danger" type="submit" value="yes" data-action></button>' +
        '<button class="orca-button" type="submit" value="no" autofocus>Cancel</button></div></form>';
      doc.body.appendChild(confirmDialog);
    }
    confirmDialog.querySelector("#orca-confirm-title").textContent = title || "Are you sure?";
    confirmDialog.querySelector("[data-text]").textContent = text;
    confirmDialog.querySelector("[data-action]").textContent = action || "Continue";
    confirmDialog.returnValue = "";
    confirmDialog.onclose = function () { if (confirmDialog.returnValue === "yes") onYes(); };
    openDialog(confirmDialog);
  }
  doc.addEventListener("submit", function (e) {
    var form = e.target;
    var submitter = e.submitter;
    var source = (submitter && submitter.hasAttribute("data-orca-confirm")) ? submitter : (form.hasAttribute("data-orca-confirm") ? form : null);
    if (!source || form._orcaConfirmed) return;
    e.preventDefault();
    confirmFirst(source.getAttribute("data-orca-confirm"), source.getAttribute("data-orca-confirm-title"),
      source.getAttribute("data-orca-confirm-action") || (submitter && submitter.textContent.trim()), function () {
        form._orcaConfirmed = true;
        if (form.requestSubmit) form.requestSubmit(submitter || undefined); else form.submit();
        form._orcaConfirmed = false;
      });
  }, true);

  /* ---------------------------------------------------------------- toasts */
  function toastStack() {
    var stack = doc.querySelector(".orca-toast-stack:not(.orca-toast-stack--static)");
    if (!stack) {
      stack = doc.createElement("ol");
      stack.className = "orca-toast-stack"; stack.setAttribute("aria-live", "polite"); stack.setAttribute("aria-label", "Notifications");
      doc.body.appendChild(stack);
    }
    return stack;
  }
  var ICONS = { positive: "success", negative: "error", caution: "warning", info: "info" };
  function toast(text, opts) {
    opts = opts || {};
    var tone = opts.tone || "info";
    var li = doc.createElement("li");
    li.className = "orca-toast orca-toast--" + tone;
    var iconTpl = doc.querySelector('template[data-orca-icon="' + (ICONS[tone] || "info") + '"]');
    if (iconTpl) li.appendChild(iconTpl.content.cloneNode(true)); else li.appendChild(doc.createElement("span"));
    var p = doc.createElement("p"); p.className = "orca-toast__text"; p.textContent = text; li.appendChild(p);
    var actions = doc.createElement("div"); actions.className = "orca-toast__actions";
    if (opts.action) {
      var b = doc.createElement("button"); b.type = "button"; b.className = "orca-button orca-button--link"; b.textContent = opts.action.label;
      b.addEventListener("click", function () { opts.action.onClick && opts.action.onClick(); dismiss(li); });
      actions.appendChild(b);
    }
    var close = doc.createElement("button"); close.type = "button"; close.className = "orca-icon-button"; close.setAttribute("aria-label", "Dismiss");
    close.innerHTML = '<span aria-hidden="true">×</span>'; close.addEventListener("click", function () { dismiss(li); });
    actions.appendChild(close); li.appendChild(actions);
    toastStack().appendChild(li);
    var timeout = opts.timeout === undefined ? (tone === "negative" ? 0 : 6000) : opts.timeout;
    if (timeout) {
      var timer = setTimeout(function () { dismiss(li); }, timeout);
      li.addEventListener("mouseenter", function () { clearTimeout(timer); });
      li.addEventListener("focusin", function () { clearTimeout(timer); });
    }
    return li;
  }
  function dismiss(el) { if (el && el.parentNode) el.parentNode.removeChild(el); }
  window.ORCA = window.ORCA || {};
  window.ORCA.toast = toast;
  window.ORCA.confirm = confirmFirst;

  /* ---------------------------------------------------------------- click */
  doc.addEventListener("click", function (event) {
    var t = event.target;
    if (openPopover && !closest(t, ".orca-anchor") && !openPopover.list.contains(t)) closePopover(false);

    var el;
    if ((el = closest(t, "[data-orca-clear]"))) {
      var input = el.parentElement.querySelector("input");
      if (input) { input.value = ""; fire(input, "input"); input.focus(); }
      return;
    }
    if ((el = closest(t, "[data-orca-step]"))) {
      var field = el.parentElement.querySelector("input[type=number], input[inputmode=numeric]");
      if (field) {
        var by = parseFloat(el.getAttribute("data-orca-step")) * (parseFloat(field.step) || 1);
        var next = (parseFloat(field.value) || 0) + by;
        if (field.min !== "" && next < parseFloat(field.min)) next = parseFloat(field.min);
        if (field.max !== "" && next > parseFloat(field.max)) next = parseFloat(field.max);
        field.value = next; fire(field, "change");
      }
      return;
    }
    if ((el = closest(t, "[data-orca-toggle]"))) {
      var on = el.getAttribute("aria-pressed") !== "true";
      el.setAttribute("aria-pressed", on ? "true" : "false");
      var label = el.getAttribute(on ? "data-orca-label-on" : "data-orca-label-off");
      if (label) {
        if (el.hasAttribute("aria-label")) el.setAttribute("aria-label", label);
        var txt = el.querySelector("[data-orca-toggle-text]") || (el.id && doc.querySelector('[data-orca-state-for="' + el.id + '"]'));
        if (txt) txt.textContent = el.getAttribute(on ? "data-orca-state-on" : "data-orca-state-off") || label;
        if (el.hasAttribute("data-orca-announce")) announce(label);
      }
      var state = el.id && doc.querySelector('[data-orca-state-for="' + el.id + '"]');
      if (state && el.hasAttribute("data-orca-state-on")) { state.textContent = el.getAttribute(on ? "data-orca-state-on" : "data-orca-state-off"); announce(state.textContent); }
      return;
    }
    if ((el = closest(t, "[data-orca-theme-toggle]"))) {
      var order = ["light", "dark", "paper"];
      var current = doc.documentElement.getAttribute("data-theme") ||
        (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      setTheme(order[(order.indexOf(current) + 1) % order.length]);
      el.setAttribute("aria-label", "Theme: " + doc.documentElement.getAttribute("data-theme") + ". Change theme");
      return;
    }
    if ((el = closest(t, "[data-orca-copy]"))) {
      var source = byId(el.getAttribute("data-orca-copy"));
      if (!source) return;
      var text = (source.value !== undefined && source.tagName !== "DIV" ? source.value : source.textContent).trim();
      var done = function () {
        var label = el.querySelector("[data-orca-copy-label]") || el;
        var old = label.textContent; label.textContent = "Copied"; announce("Copied to clipboard");
        el.setAttribute("data-copied", "");
        setTimeout(function () { label.textContent = old; el.removeAttribute("data-copied"); }, 1500);
      };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () { selectText(source); });
      else selectText(source);
      return;
    }
    if ((el = closest(t, "[data-orca-menu]"))) {
      var menu = controlled(el);
      if (!menu) return;
      if (el.getAttribute("aria-expanded") === "true") closePopover(false); else openList(el, menu);
      return;
    }
    if ((el = closest(t, "[data-orca-listbox]"))) {
      var lb = controlled(el);
      if (el.getAttribute("aria-expanded") === "true") closePopover(false); else openList(el, lb);
      return;
    }
    if ((el = closest(t, '[role=option]')) && closest(el, "[data-orca-listbox-wrap]")) {
      chooseOption(closest(el, "[data-orca-listbox-wrap]"), el); return;
    }
    if ((el = closest(t, '[role=option]')) && closest(el, "[data-orca-combobox-wrap]")) {
      pickCombo(closest(el, "[data-orca-combobox-wrap]"), el); return;
    }
    if ((el = closest(t, "[role=menuitem]")) && openPopover && openPopover.list.contains(el)) {
      if (el.tagName !== "A") closePopover(true);
      return;
    }
    if ((el = closest(t, "[role=tab]")) && closest(el, "[data-orca-tabs]")) { selectTab(el, true); return; }
    if ((el = closest(t, "[data-orca-dialog-open]"))) { openDialog(byId(el.getAttribute("data-orca-dialog-open")), el); return; }
    if ((el = closest(t, "[data-orca-dialog-close]"))) { var dlg = closest(el, "dialog"); if (dlg) dlg.close(el.value || ""); return; }
    if ((el = closest(t, "[data-orca-toast]"))) {
      toast(el.getAttribute("data-orca-toast"), { tone: el.getAttribute("data-orca-toast-tone") || "positive" }); return;
    }
    if ((el = closest(t, "[data-orca-dismiss]"))) { dismiss(closest(el, ".orca-alert, .orca-toast, .orca-callout")); return; }
    if ((el = closest(t, "[data-orca-disclose]"))) {
      var target = controlled(el); if (!target) return;
      var open = el.getAttribute("aria-expanded") !== "true";
      el.setAttribute("aria-expanded", open ? "true" : "false"); target.hidden = !open;
      if (open) { var first = target.querySelector("input, select, textarea, button, a[href]"); if (first) first.focus(); }
      return;
    }
    if ((el = closest(t, "[data-orca-set-date]"))) {
      var dateInput = controlled(el);
      if (dateInput) {
        dateInput.value = today(parseInt(el.getAttribute("data-orca-set-date"), 10) || 0); fire(dateInput, "change");
        var group = closest(el, ".orca-shortcuts");
        if (group) group.querySelectorAll("[data-orca-set-date]").forEach(function (b) { b.setAttribute("aria-pressed", b === el ? "true" : "false"); });
      }
      return;
    }
    if ((el = closest(t, "[data-orca-detect-tz]"))) {
      var sel = controlled(el); var zone = "";
      try { zone = Intl.DateTimeFormat().resolvedOptions().timeZone; } catch (e) { /* unavailable */ }
      if (sel && zone && sel.querySelector('option[value="' + zone + '"]')) { sel.value = zone; fire(sel, "change"); announce("Timezone set to " + zone); }
      return;
    }
    if ((el = closest(t, "[data-orca-add-row]"))) {
      var tpl = byId(el.getAttribute("data-orca-add-row")); var list = controlled(el);
      if (tpl && list) {
        var count = list.querySelectorAll("[data-orca-row]").length;
        var html = tpl.innerHTML.replace(/__prefix__/g, String(count));
        list.insertAdjacentHTML("beforeend", html);
        var rows = list.querySelectorAll("[data-orca-row]"); var row = rows[rows.length - 1];
        var f = row && row.querySelector("input, select"); if (f) f.focus();
        var total = byId(el.getAttribute("data-orca-total")); if (total) total.value = rows.length;
      }
      return;
    }
    if ((el = closest(t, "[data-orca-remove-row]"))) {
      var r = closest(el, "[data-orca-row]"); if (!r) return;
      var container = r.parentElement; var label2 = el.getAttribute("aria-label") || "Row";
      var del = r.querySelector('input[name$="-DELETE"]');
      if (del) { del.checked = true; r.hidden = true; } else r.parentNode.removeChild(r);
      announce(label2.replace(/^Remove /, "") + " removed");
      var focusNext = container && container.querySelector("[data-orca-row]:not([hidden]) input, [data-orca-row]:not([hidden]) select");
      if (focusNext) focusNext.focus();
      return;
    }
    if ((el = closest(t, "[data-orca-weekdays]"))) {
      var set = el.getAttribute("data-orca-weekdays").split(",");
      var fs = controlled(el);
      if (fs) fs.querySelectorAll('input[type=checkbox]').forEach(function (c) { c.checked = set.indexOf(c.value) !== -1; fire(c, "change"); });
      var presetGroup = closest(el, ".orca-presets");
      if (presetGroup) presetGroup.querySelectorAll("[data-orca-weekdays]").forEach(function (b) { b.setAttribute("aria-pressed", b === el ? "true" : "false"); });
      return;
    }
    if ((el = closest(t, "[data-orca-carousel] [data-orca-prev], [data-orca-carousel] [data-orca-next], [data-orca-carousel] [data-orca-slide]"))) {
      var car = closest(el, "[data-orca-carousel]");
      var index = el.hasAttribute("data-orca-slide") ? parseInt(el.getAttribute("data-orca-slide"), 10) : carouselIndex(car) + (el.hasAttribute("data-orca-next") ? 1 : -1);
      goSlide(car, index); return;
    }
  });

  function selectText(el) {
    if (el.select) { el.select(); return; }
    var range = doc.createRange(); range.selectNodeContents(el);
    var s = window.getSelection(); s.removeAllRanges(); s.addRange(range);
  }
  function setTheme(theme) {
    if (theme === "auto") doc.documentElement.removeAttribute("data-theme");
    else doc.documentElement.setAttribute("data-theme", theme);
    try { if (theme === "auto") localStorage.removeItem(THEME_KEY); else localStorage.setItem(THEME_KEY, theme); } catch (e) { /* storage blocked */ }
  }

  /* ---------------------------------------------------------------- keyboard */
  doc.addEventListener("keydown", function (e) {
    var t = e.target;
    if (e.key === "Escape") {
      if (openPopover) { closePopover(true); e.preventDefault(); return; }
      var tip = closest(t, ".orca-tooltip-wrap"); if (tip) tip.classList.add("is-dismissed");
      var openSide = doc.querySelector('.orca-sidebar[data-open="true"]');
      if (openSide) {
        openSide.setAttribute("data-open", "false");
        var opener = doc.querySelector('[data-orca-sidebar-open][aria-controls="' + openSide.id + '"]');
        if (opener) { opener.setAttribute("aria-expanded", "false"); opener.setAttribute("aria-label", "Show navigation"); opener.focus(); }
      }
    }
    // Menus and listboxes
    if (openPopover && (openPopover.list.contains(t) || t === openPopover.trigger)) {
      var list = openPopover.list; var cur = activeOption(list);
      if (e.key === "ArrowDown") { moveIn(list, cur, 1); e.preventDefault(); }
      else if (e.key === "ArrowUp") { moveIn(list, cur, -1); e.preventDefault(); }
      else if (e.key === "Home") { moveIn(list, cur, "first"); e.preventDefault(); }
      else if (e.key === "End") { moveIn(list, cur, "last"); e.preventDefault(); }
      else if (e.key === "Tab") { closePopover(false); }
      else if ((e.key === "Enter" || e.key === " ") && cur && cur.getAttribute("role") === "option") {
        var w = closest(cur, "[data-orca-listbox-wrap]"); if (w) { chooseOption(w, cur); e.preventDefault(); }
      }
      return;
    }
    var trig = closest(t, "[data-orca-menu], [data-orca-listbox]");
    if (trig && (e.key === "ArrowDown" || e.key === "ArrowUp")) { openList(trig, controlled(trig), e.key === "ArrowUp" ? "last" : "first"); e.preventDefault(); return; }
    // Combobox
    var combo = closest(t, "[data-orca-combobox]");
    if (combo) { comboKey(combo, e); return; }
    // Tabs
    var tab = closest(t, "[role=tab]");
    if (tab && closest(tab, "[data-orca-tabs]")) {
      var tabs = Array.prototype.slice.call(closest(tab, "[role=tablist]").querySelectorAll("[role=tab]"));
      var i = tabs.indexOf(tab), n = null;
      var rtl = getComputedStyle(tab).direction === "rtl";
      if (e.key === (rtl ? "ArrowLeft" : "ArrowRight")) n = tabs[(i + 1) % tabs.length];
      if (e.key === (rtl ? "ArrowRight" : "ArrowLeft")) n = tabs[(i - 1 + tabs.length) % tabs.length];
      if (e.key === "Home") n = tabs[0];
      if (e.key === "End") n = tabs[tabs.length - 1];
      if (n) { selectTab(n, true); e.preventDefault(); }
      return;
    }
    // OTP backspace
    if (e.key === "Backspace" && t.matches && t.matches("[data-orca-otp] input") && !t.value) {
      var prev = t.previousElementSibling; while (prev && prev.tagName !== "INPUT") prev = prev.previousElementSibling;
      if (prev) { prev.focus(); prev.value = ""; e.preventDefault(); }
    }
  });
  doc.addEventListener("focusout", function (e) {
    var tip = closest(e.target, ".orca-tooltip-wrap"); if (tip) tip.classList.remove("is-dismissed");
  });

  /* ---------------------------------------------------------------- tabs */
  function selectTab(tab, focus) {
    var list = closest(tab, "[role=tablist]");
    list.querySelectorAll("[role=tab]").forEach(function (t) {
      var on = t === tab;
      t.setAttribute("aria-selected", on ? "true" : "false");
      t.tabIndex = on ? 0 : -1;
      var panel = controlled(t); if (panel) panel.hidden = !on;
    });
    if (focus) tab.focus();
  }

  /* ---------------------------------------------------------------- combobox */
  function comboList(input) { return controlled(input); }
  function comboFilter(input) {
    var list = comboList(input); if (!list) return;
    var q = input.value.trim().toLowerCase(); var shown = 0;
    list.querySelectorAll("[role=option]").forEach(function (o) {
      var label = (o.getAttribute("data-label") || o.textContent).trim();
      var hit = !q || label.toLowerCase().indexOf(q) !== -1;
      o.hidden = !hit || shown >= 10;
      if (hit && shown < 10) {
        shown++;
        var i = label.toLowerCase().indexOf(q);
        if (q && i !== -1 && !o.querySelector(".orca-option__desc")) {
          o.innerHTML = ""; o.append(label.slice(0, i));
          var m = doc.createElement("mark"); m.textContent = label.slice(i, i + q.length); o.append(m, label.slice(i + q.length));
        } else if (!o.querySelector(".orca-option__desc")) { o.textContent = label; }
      }
      o.classList.remove("is-active");
    });
    var empty = list.querySelector(".orca-popover__empty"); if (empty) empty.hidden = shown > 0;
    list.hidden = false; input.setAttribute("aria-expanded", "true");
    var status = byId(input.getAttribute("data-orca-status"));
    if (status) status.textContent = shown ? shown + " suggestion" + (shown === 1 ? "" : "s") : "No matches";
  }
  function comboMove(input, delta) {
    var list = comboList(input); if (!list) return;
    var opts = Array.prototype.filter.call(list.querySelectorAll("[role=option]"), function (o) { return !o.hidden; });
    if (!opts.length) return;
    var cur = list.querySelector(".is-active"); var i = opts.indexOf(cur);
    var next = opts[(i + delta + opts.length) % opts.length];
    if (cur) cur.classList.remove("is-active");
    next.classList.add("is-active"); input.setAttribute("aria-activedescendant", next.id);
    if (next.scrollIntoView) next.scrollIntoView({ block: "nearest" });
  }
  function pickCombo(wrap, option) {
    var input = wrap.querySelector("[data-orca-combobox]");
    input.value = option.getAttribute("data-label") || option.textContent.trim();
    var hidden = wrap.querySelector("input[type=hidden]"); if (hidden) { hidden.value = option.getAttribute("data-value") || input.value; fire(hidden, "change"); }
    var list = comboList(input); list.hidden = true; input.setAttribute("aria-expanded", "false"); input.removeAttribute("aria-activedescendant");
    input.focus();
  }
  function comboKey(input, e) {
    var list = comboList(input); if (!list) return;
    if (e.key === "ArrowDown") { if (list.hidden) comboFilter(input); comboMove(input, 1); e.preventDefault(); }
    else if (e.key === "ArrowUp") { comboMove(input, -1); e.preventDefault(); }
    else if (e.key === "Enter" && !list.hidden) { var a = list.querySelector(".is-active"); if (a) { pickCombo(closest(input, "[data-orca-combobox-wrap]"), a); e.preventDefault(); } }
    else if (e.key === "Escape") { if (!list.hidden) { list.hidden = true; input.setAttribute("aria-expanded", "false"); } else { input.value = ""; } e.preventDefault(); }
  }
  doc.addEventListener("focusout", function (e) {
    var wrap = closest(e.target, "[data-orca-combobox-wrap]");
    if (!wrap) return;
    setTimeout(function () {
      if (!wrap.contains(doc.activeElement)) {
        var input = wrap.querySelector("[data-orca-combobox]"); var list = input && comboList(input);
        if (list) { list.hidden = true; input.setAttribute("aria-expanded", "false"); }
      }
    }, 120);
  });

  /* ---------------------------------------------------------------- input and change */
  doc.addEventListener("input", function (e) {
    var t = e.target;
    if (t.matches && t.matches("[data-orca-otp] input")) {
      t.value = t.value.replace(/\D/g, "").slice(-1);
      if (t.value) { var n = t.nextElementSibling; while (n && n.tagName !== "INPUT") n = n.nextElementSibling; if (n) n.focus(); }
      return;
    }
    if (t.hasAttribute && t.hasAttribute("data-orca-combobox")) { comboFilter(t); return; }
    if (t.hasAttribute && t.hasAttribute("data-orca-filter-list")) {
      var list = byId(t.getAttribute("data-orca-filter-list")); if (!list) return;
      var q = t.value.trim().toLowerCase(); var shown = 0;
      list.querySelectorAll("li").forEach(function (li) { var hit = !q || li.textContent.toLowerCase().indexOf(q) !== -1; li.hidden = !hit; if (hit) shown++; });
      list.querySelectorAll("details").forEach(function (d) { var any = d.querySelector("li:not([hidden])"); d.hidden = !any; if (q && any) d.open = true; });
      var status = byId(t.getAttribute("data-orca-status")); if (status) status.textContent = shown + " shown";
    }
  });
  doc.addEventListener("change", function (e) {
    var t = e.target;
    if (t.hasAttribute && t.hasAttribute("data-orca-autosubmit") && t.form) { if (t.form.requestSubmit) t.form.requestSubmit(); else t.form.submit(); return; }
    if (t.hasAttribute && t.hasAttribute("data-orca-reveal")) {
      var target = byId(t.getAttribute("data-orca-reveal"));
      if (target) target.hidden = t.value !== t.getAttribute("data-orca-reveal-value");
      return;
    }
    if (t.name && closest(t, "[data-orca-theme-choice]") && t.checked) { setTheme(t.value); return; }
    var range = closest(t, "[data-orca-range]");
    if (range) { checkRange(range); return; }
    if (t.hasAttribute && t.hasAttribute("data-orca-file-list")) {
      var out = byId(t.getAttribute("data-orca-file-list")); if (!out) return;
      out.innerHTML = "";
      Array.prototype.forEach.call(t.files || [], function (f) {
        var li = doc.createElement("li");
        li.textContent = f.name + " · " + (f.size > 1048576 ? (f.size / 1048576).toFixed(1) + " MB" : Math.max(1, Math.round(f.size / 1024)) + " KB");
        out.appendChild(li);
      });
      announce((t.files ? t.files.length : 0) + " file(s) chosen");
    }
  });
  doc.addEventListener("dragover", function (e) { var z = closest(e.target, ".orca-dropzone"); if (z) z.classList.add("is-over"); });
  doc.addEventListener("dragleave", function (e) { var z = closest(e.target, ".orca-dropzone"); if (z) z.classList.remove("is-over"); });
  doc.addEventListener("drop", function (e) { var z = closest(e.target, ".orca-dropzone"); if (z) z.classList.remove("is-over"); });

  /* ---------------------------------------------------------------- ranges */
  function minutes(v) { var p = (v || "").split(":"); return p.length < 2 ? null : parseInt(p[0], 10) * 60 + parseInt(p[1], 10); }
  function checkRange(range) {
    var inputs = range.querySelectorAll("input"); if (inputs.length < 2) return;
    var start = inputs[0], end = inputs[1];
    var out = range.querySelector("[data-orca-range-output]");
    if (start.type === "date") {
      if (start.value) end.min = start.value;
      if (start.value && end.value && end.value < start.value) { end.value = start.value; }
      if (out && start.value && end.value) {
        var days = Math.round((Date.parse(end.value) - Date.parse(start.value)) / 86400000) + 1;
        out.textContent = days + " day" + (days === 1 ? "" : "s");
      }
    } else if (start.type === "time") {
      var a = minutes(start.value), b = minutes(end.value);
      if (out && a !== null && b !== null) {
        var d = b - a; var overnight = d <= 0; if (overnight) d += 1440;
        var h = Math.floor(d / 60), m = d % 60;
        out.textContent = (h ? h + " h" : "") + (h && m ? " " : "") + (m ? m + " min" : "") + (overnight ? ", ends the next day" : "");
      }
    }
  }

  /* ---------------------------------------------------------------- carousel */
  function carouselIndex(car) {
    var track = car.querySelector(".orca-carousel__track");
    return Math.round(track.scrollLeft / Math.max(1, track.clientWidth)) * (getComputedStyle(track).direction === "rtl" ? -1 : 1);
  }
  function goSlide(car, index) {
    var track = car.querySelector(".orca-carousel__track"); var slides = track.children.length;
    index = Math.max(0, Math.min(slides - 1, index));
    var rtl = getComputedStyle(track).direction === "rtl";
    track.scrollTo({ left: (rtl ? -1 : 1) * index * track.clientWidth });
    updateCarousel(car, index);
  }
  function updateCarousel(car, index) {
    var track = car.querySelector(".orca-carousel__track"); var slides = track.children.length;
    car.querySelectorAll("[data-orca-slide]").forEach(function (d, i) { if (i === index) d.setAttribute("aria-current", "true"); else d.removeAttribute("aria-current"); });
    var count = car.querySelector(".orca-carousel__count"); if (count) count.textContent = (index + 1) + " of " + slides;
    var prev = car.querySelector("[data-orca-prev]"), next = car.querySelector("[data-orca-next]");
    if (prev) prev.disabled = index === 0; if (next) next.disabled = index === slides - 1;
    Array.prototype.forEach.call(track.children, function (s, i) { s.setAttribute("aria-hidden", i === index ? "false" : "true"); });
  }
  doc.querySelectorAll("[data-orca-carousel]").forEach(function (car) {
    var track = car.querySelector(".orca-carousel__track"); var t;
    updateCarousel(car, 0);
    track.addEventListener("scroll", function () { clearTimeout(t); t = setTimeout(function () { updateCarousel(car, Math.abs(carouselIndex(car))); }, 100); });
  });

  /* Collapse all / Expand all: the button offers whichever is useful now (collapse while any section is open) */
  function syncTreeToggles() {
    doc.querySelectorAll("[data-orca-tree-toggle]").forEach(function (b) {
      var tree = controlled(b); if (!tree) return;
      var anyOpen = Array.prototype.some.call(tree.querySelectorAll("details"), function (d) { return d.open; });
      var label = anyOpen ? "Collapse all sections" : "Expand all sections";
      if (anyOpen) b.removeAttribute("data-all-closed"); else b.setAttribute("data-all-closed", "");
      b.setAttribute("aria-label", label); b.setAttribute("title", label);
    });
  }
  doc.addEventListener("toggle", function (e) { if (closest(e.target, ".orca-nav-tree")) syncTreeToggles(); }, true);
  syncTreeToggles();

  /* ---------------------------------------------------------------- patterns */
  doc.addEventListener("click", function (e) {
    var t = e.target, el;
    if (t.tagName === "DIALOG" && t.hasAttribute("data-orca-light-dismiss")) {
      var r = t.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) t.close("dismiss");
      return;
    }
    if ((el = closest(t, "[data-orca-sidebar-open]"))) {
      var side = controlled(el); if (!side) return;
      var open = side.getAttribute("data-open") !== "true";
      side.setAttribute("data-open", open ? "true" : "false");
      el.setAttribute("aria-expanded", open ? "true" : "false");
      el.setAttribute("aria-label", open ? "Hide navigation" : "Show navigation");
      if (open) { var first = side.querySelector("a, button, input"); if (first) first.focus(); }
      return;
    }
    if ((el = closest(t, "[data-orca-tree-toggle]"))) {
      var tree = controlled(el); if (!tree) return;
      var sections = tree.querySelectorAll("details");
      var anyOpen = Array.prototype.some.call(sections, function (d) { return d.open; });
      sections.forEach(function (d) { d.open = !anyOpen; });
      syncTreeToggles();
      return;
    }
    if ((el = closest(t, "[data-orca-sidebar-toggle]"))) {
      var bar = controlled(el); if (!bar) return;
      var collapsed = bar.getAttribute("data-collapsed") !== "true";
      bar.setAttribute("data-collapsed", collapsed ? "true" : "false");
      el.setAttribute("aria-expanded", collapsed ? "false" : "true");
      el.setAttribute("aria-label", collapsed ? "Expand navigation" : "Collapse navigation");
      try { localStorage.setItem(sidebarKey(bar), collapsed ? "collapsed" : "expanded"); } catch (x) { /* storage blocked */ }
      return;
    }
    if ((el = closest(t, "[data-orca-rt]"))) {
      var cmd = el.getAttribute("data-orca-rt");
      var area = closest(el, "[data-orca-richtext]").querySelector("[contenteditable]");
      area.focus();
      if (cmd === "createLink") { var url = window.prompt ? window.prompt("Link address") : ""; if (url) doc.execCommand("createLink", false, url); }
      else doc.execCommand(cmd, false, null);
      syncRichtext(closest(el, "[data-orca-richtext]"));
      return;
    }
    if ((el = closest(t, "[data-orca-seek]"))) {
      var video = controlled(el); if (!video) return;
      video.currentTime = parseFloat(el.getAttribute("data-orca-seek")) || 0;
      if (video.play) { var pr = video.play(); if (pr && pr.catch) pr.catch(function () {}); }
      announce("Jumped to " + (el.getAttribute("aria-label") || el.textContent.trim()));
      return;
    }
    if ((el = closest(t, "[data-orca-gallery] [data-orca-gallery-src]"))) {
      var gal = closest(el, "[data-orca-gallery]"); var stage = gal.querySelector("[data-orca-gallery-stage]");
      stage.src = el.getAttribute("data-orca-gallery-src"); stage.alt = el.getAttribute("data-orca-gallery-alt") || "";
      gal.querySelectorAll("[data-orca-gallery-src]").forEach(function (b) { if (b === el) b.setAttribute("aria-current", "true"); else b.removeAttribute("aria-current"); });
      var cnt = gal.querySelector("[data-orca-gallery-count]"); var all = gal.querySelectorAll("[data-orca-gallery-src]");
      if (cnt) cnt.textContent = (Array.prototype.indexOf.call(all, el) + 1) + " of " + all.length;
      return;
    }
    if ((el = closest(t, "[data-orca-zone-editor] [data-orca-zone-action]"))) {
      var ed = closest(el, "[data-orca-zone-editor]"); var act = el.getAttribute("data-orca-zone-action");
      var st = zoneState(ed);
      if (act === "undo") st.points.pop();
      if (act === "clear") st.points = [];
      if (act === "close" && st.points.length >= 3) st.closed = true;
      if (act !== "close") st.closed = false;
      drawZone(ed); return;
    }
    if ((el = closest(t, "[data-orca-zone-editor] .orca-zone-editor__stage"))) {
      var ed2 = closest(el, "[data-orca-zone-editor]"); var s2 = zoneState(ed2);
      if (s2.closed) return;
      var rect = el.getBoundingClientRect();
      s2.points.push([Math.round((e.clientX - rect.left) / rect.width * 1000) / 10, Math.round((e.clientY - rect.top) / rect.height * 1000) / 10]);
      drawZone(ed2); return;
    }
  });
  function syncRichtext(wrap) {
    var area = wrap.querySelector("[contenteditable]"); var field = wrap.querySelector("textarea, input[type=hidden]");
    if (field) field.value = area.innerHTML;
    wrap.querySelectorAll("[data-orca-rt]").forEach(function (b) {
      var c = b.getAttribute("data-orca-rt");
      if (c === "createLink" || c === "removeFormat") return;
      try { b.setAttribute("aria-pressed", doc.queryCommandState(c) ? "true" : "false"); } catch (x) { /* unsupported */ }
    });
  }
  doc.addEventListener("input", function (e) {
    var wrap = closest(e.target, "[data-orca-richtext]"); if (wrap) syncRichtext(wrap);
    var tok = closest(e.target, "[data-orca-token]");
    if (tok) { var target = controlled(tok); if (target) target.style.setProperty(tok.getAttribute("data-orca-token"), tok.value); }
  });
  doc.addEventListener("selectionchange", function () {
    var a = doc.activeElement; var wrap = a && closest(a, "[data-orca-richtext]"); if (wrap) syncRichtext(wrap);
  });
  function zoneState(ed) {
    if (!ed._zone) {
      var field = ed.querySelector("input[type=hidden]"); var pts = [];
      try { pts = JSON.parse(field && field.value || "[]"); } catch (x) { pts = []; }
      ed._zone = { points: pts, closed: pts.length >= 3 };
    }
    return ed._zone;
  }
  function drawZone(ed) {
    var st = zoneState(ed); var svg = ed.querySelector("svg");
    var pts = st.points.map(function (p) { return p[0] + "," + p[1]; }).join(" ");
    var shape = st.closed ? '<polygon points="' + pts + '"/>' : '<polyline points="' + pts + '"/>';
    svg.innerHTML = shape + st.points.map(function (p) { return '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="0.9"/>'; }).join("");
    var field = ed.querySelector("input[type=hidden]"); if (field) field.value = st.closed ? JSON.stringify(st.points) : "";
    var status = ed.querySelector("[data-orca-zone-status]");
    if (status) status.textContent = st.closed ? "Zone closed with " + st.points.length + " points." : st.points.length + " point" + (st.points.length === 1 ? "" : "s") + ". " + (st.points.length >= 3 ? "Close the shape when done." : "Add at least 3.");
  }
  doc.querySelectorAll("[data-orca-zone-editor]").forEach(drawZone);
  /* Each sidebar remembers its own state (key "orca-sidebar:<id>"), so a demo never collapses the real navigation */
  function sidebarKey(bar) { return "orca-sidebar" + (bar.id ? ":" + bar.id : ""); }
  doc.querySelectorAll("[data-orca-sidebar-toggle]").forEach(function (b) {
    var bar = controlled(b); if (!bar) return;
    var pref = null; try { pref = localStorage.getItem(sidebarKey(bar)); } catch (x) { /* storage blocked */ }
    if (!pref) return;
    var collapsed = pref === "collapsed";
    bar.setAttribute("data-collapsed", collapsed ? "true" : "false");
    b.setAttribute("aria-expanded", collapsed ? "false" : "true");
    b.setAttribute("aria-label", collapsed ? "Expand navigation" : "Collapse navigation");
  });

  /* Kanban drag and drop (the "Move to" menu on each card is the keyboard and touch alternative) */
  var dragged = null;
  doc.addEventListener("dragstart", function (e) {
    var card = closest(e.target, "[data-orca-board] [draggable=true]"); if (!card) return;
    dragged = card; card.classList.add("orca-is-dragging");
    if (e.dataTransfer) { e.dataTransfer.effectAllowed = "move"; e.dataTransfer.setData("text/plain", card.id || ""); }
  });
  doc.addEventListener("dragend", function () {
    if (dragged) dragged.classList.remove("orca-is-dragging"); dragged = null;
    doc.querySelectorAll(".orca-board__cards.is-target").forEach(function (l) { l.classList.remove("is-target"); });
  });
  doc.addEventListener("dragover", function (e) {
    var list = closest(e.target, "[data-orca-column]"); if (!list || !dragged) return;
    e.preventDefault(); list.classList.add("is-target");
  });
  doc.addEventListener("drop", function (e) {
    var list = closest(e.target, "[data-orca-column]"); if (!list || !dragged) return;
    e.preventDefault(); list.classList.remove("is-target");
    var from = closest(dragged, "[data-orca-column]"); list.appendChild(dragged);
    var col = closest(list, ".orca-board__col"); var name = col && col.querySelector(".orca-board__head") ? col.querySelector(".orca-board__head").firstChild.textContent.trim() : list.getAttribute("data-orca-column");
    announce("Moved to " + name);
    list.dispatchEvent(new CustomEvent("orca:moved", { bubbles: true, detail: { id: dragged.id, from: from && from.getAttribute("data-orca-column"), to: list.getAttribute("data-orca-column") } }));
    [from, list].forEach(updateCount);
  });
  function updateCount(list) {
    if (!list) return; var col = closest(list, ".orca-board__col"); if (!col) return;
    var c = col.querySelector("[data-orca-count]"); if (c) c.textContent = list.children.length;
  }

  /* ---------------------------------------------------------------- paste into OTP */
  doc.addEventListener("paste", function (e) {
    var box = e.target;
    if (!box.matches || !box.matches("[data-orca-otp] input")) return;
    var digits = (e.clipboardData || window.clipboardData).getData("text").replace(/\D/g, "");
    if (!digits) return;
    e.preventDefault();
    var boxes = box.closest("[data-orca-otp]").querySelectorAll("input");
    boxes.forEach(function (b, i) { b.value = digits[i] || ""; });
    boxes[Math.min(digits.length, boxes.length) - 1].focus();
  });

  /* ---------------------------------------------------------------- initial state */
  doc.querySelectorAll("[data-orca-tabs]").forEach(function (list) {
    var sel = list.querySelector('[role=tab][aria-selected="true"]') || list.querySelector("[role=tab]");
    if (sel) selectTab(sel, false);
  });
  doc.querySelectorAll("[data-orca-theme-choice]").forEach(function (group) {
    var cur = "auto"; try { cur = localStorage.getItem(THEME_KEY) || "auto"; } catch (e) { /* storage blocked */ }
    var radio = group.querySelector('input[value="' + cur + '"]'); if (radio) radio.checked = true;
  });
  doc.querySelectorAll("[data-orca-range]").forEach(checkRange);

  function tick() {
    doc.querySelectorAll("[data-orca-countdown]").forEach(function (el) {
      var end = Date.parse(el.getAttribute("datetime"));
      if (isNaN(end)) return;
      var s = Math.max(0, Math.round((end - Date.now()) / 1000));
      var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = s % 60;
      el.textContent = (h ? h + ":" + String(m).padStart(2, "0") : m) + ":" + String(sec).padStart(2, "0");
      el.classList.toggle("orca-countdown--urgent", s > 0 && s <= 60);
    });
  }
  if (doc.querySelector("[data-orca-countdown]")) { tick(); setInterval(tick, 1000); }

  /* ---------------------------------------------------------------- charts (Chart.js) */
  /* The server writes a spec {kind, labels, series:[{name, values}], unit, stacked, horizontal} on each canvas.
     Chart.js is loaded once, only when a page has a chart. Colours, font and grid come from the ORCA tokens, so a
     theme change redraws every chart. ORCA writes its own legend and data table; Chart.js draws the plot only. */
  var charts = [];
  function token(el, name) { return getComputedStyle(el).getPropertyValue(name).trim(); }
  function alpha(color, a) {
    var m = /^#([0-9a-f]{6})$/i.exec(color);
    if (m) { var n = parseInt(m[1], 16); return "rgba(" + (n >> 16) + "," + ((n >> 8) & 255) + "," + (n & 255) + "," + a + ")"; }
    m = /^rgba?\(([^)]+)\)$/.exec(color);
    if (m) { var p = m[1].split(",").slice(0, 3).join(","); return "rgba(" + p + "," + a + ")"; }
    return color;
  }
  function chartConfig(canvas, spec) {
    var t = function (n) { return token(canvas, n); };
    var palette = [1, 2, 3, 4, 5, 6, 7, 8].map(function (i) { return t("--orca-chart-" + i); });
    var col = function (i) { return palette[i % palette.length]; };
    var text = t("--orca-text-muted"), grid = t("--orca-gridline") || t("--orca-border-weak"), ground = t("--orca-bg-panel") || t("--orca-bg");
    var font = { family: t("--orca-font-sans"), size: 11 };
    var lang = doc.documentElement.lang || undefined;
    var unit = spec.unit || "";
    var num = function (v) { return Number(v).toLocaleString(lang) + unit; };
    var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
    var series = spec.series || [];
    var opts = {
      responsive: true, maintainAspectRatio: false, animation: reduce ? false : { duration: 300 },
      plugins: { legend: { display: false }, tooltip: { titleFont: font, bodyFont: font, callbacks: {} } },
      font: font, layout: { padding: 8 }
    };
    var axis = function (stacked) {
      return { stacked: !!stacked, grid: { color: grid }, border: { color: t("--orca-border-strong") },
               ticks: { color: text, font: font, callback: function (v) { return typeof v === "number" ? num(v) : this.getLabelForValue(v); } } };
    };
    var kind = spec.kind, type = kind, data = { labels: spec.labels || [] };
    if (kind === "sparkline") {
      var accent = t("--orca-accent");
      var lo = Math.min.apply(null, spec.values), hi = Math.max.apply(null, spec.values), pad = (hi - lo || 1) * 0.1;
      return { type: "line", data: { labels: spec.values.map(function (_, i) { return i; }),
        datasets: [{ data: spec.values, borderColor: accent, backgroundColor: alpha(accent, 0.12), fill: "start", borderWidth: 1.5,
                     tension: 0.3, pointRadius: spec.values.map(function (_, i) { return i === spec.values.length - 1 ? 2.5 : 0; }),
                     pointBackgroundColor: accent }] },
        options: { responsive: true, maintainAspectRatio: false, animation: false, events: [],
                   plugins: { legend: { display: false }, tooltip: { enabled: false } },
                   scales: { x: { display: false }, y: { display: false, min: lo - pad, max: hi + pad } }, layout: { padding: 3 } } };
    }
    if (kind === "pie" || kind === "doughnut" || kind === "polar") {
      type = kind === "polar" ? "polarArea" : kind;
      data.datasets = [{ data: series.length ? series[0].values : [], label: series.length ? series[0].name : "",
                         backgroundColor: data.labels.map(function (_, i) { return kind === "polar" ? alpha(col(i), 0.85) : col(i); }),
                         borderColor: ground, borderWidth: 2 }];
      if (kind === "doughnut") opts.cutout = spec.donut ? "72%" : "58%";
      if (kind === "polar") opts.scales = { r: { grid: { color: grid }, ticks: { color: text, font: font, backdropColor: "transparent" } } };
      opts.plugins.tooltip.callbacks.label = function (c) { return " " + c.label + ": " + num(c.raw); };
    } else if (kind === "scatter" || kind === "bubble") {
      data = { datasets: series.map(function (s, i) {
        return { label: s.name, backgroundColor: alpha(col(i), kind === "bubble" ? 0.55 : 1), borderColor: col(i), borderWidth: 1.5,
                 pointStyle: ["circle", "rect", "triangle", "rectRot", "star", "crossRot"][i % 6], pointRadius: 4,
                 data: s.values.map(function (v) { return kind === "bubble" ? { x: v[0], y: v[1], r: v[2] || 4 } : { x: v[0], y: v[1] }; }) };
      }) };
      opts.scales = { x: axis(false), y: axis(false) };
      opts.scales.x.grace = opts.scales.y.grace = "8%";
      opts.scales.x.ticks.callback = opts.scales.y.ticks.callback = function (v) { return Number(v).toLocaleString(lang); };
    } else if (kind === "radar") {
      data.datasets = series.map(function (s, i) {
        return { label: s.name, data: s.values, borderColor: col(i), backgroundColor: alpha(col(i), 0.15), pointBackgroundColor: col(i), borderWidth: 2 };
      });
      opts.scales = { r: { grid: { color: grid }, angleLines: { color: grid }, pointLabels: { color: text, font: font },
                           ticks: { color: text, font: font, backdropColor: "transparent" } } };
    } else {
      type = kind === "area" ? "line" : kind;
      data.datasets = series.map(function (s, i) {
        var d = { label: s.name, data: s.values, borderColor: col(i), backgroundColor: kind === "bar" ? col(i) : alpha(col(i), 0.12) };
        if (type === "line") { d.fill = kind === "area" ? "origin" : false; d.tension = 0.3; d.borderWidth = 2.5; d.pointRadius = 2.5; d.pointBackgroundColor = col(i);
          if (i % 2) d.borderDash = [6, 4]; /* every other series is dashed: colour is never the only key */ }
        return d;
      });
      opts.indexAxis = spec.horizontal ? "y" : "x";
      opts.scales = { x: axis(spec.stacked), y: axis(spec.stacked) };
      var catAxis = spec.horizontal ? "y" : "x";
      opts.scales[catAxis].grid = { display: false };
      opts.scales[catAxis].ticks.callback = function (v) { return this.getLabelForValue(v); };
    }
    if (!opts.plugins.tooltip.callbacks.label) {
      opts.plugins.tooltip.callbacks.label = function (c) {
        var v = c.raw && typeof c.raw === "object" ? "(" + [c.raw.x, c.raw.y].map(function (x) { return Number(x).toLocaleString(lang); }).join(", ") + ")" : num(c.raw);
        return " " + (c.dataset.label ? c.dataset.label + ": " : "") + v;
      };
    }
    return { type: type, data: data, options: opts };
  }
  function drawCharts() {
    charts.forEach(function (c) { c.destroy(); }); charts = [];
    doc.querySelectorAll("canvas[data-orca-chart]").forEach(function (canvas) {
      var spec; try { spec = JSON.parse(canvas.getAttribute("data-orca-chart")); } catch (e) { return; }
      charts.push(new window.Chart(canvas, chartConfig(canvas, spec)));
    });
  }
  function loadChartJs(done) {
    if (window.Chart) { done(); return; }
    var src = doc.documentElement.getAttribute("data-orca-chartjs") || SELF_SRC.replace(/js\/orca\.js(\?.*)?$/, "vendor/chart.umd.js");
    var s = doc.createElement("script"); s.src = src; s.onload = done;
    var nonce = doc.querySelector("script[nonce]"); if (nonce) s.nonce = nonce.nonce || nonce.getAttribute("nonce");
    doc.head.appendChild(s);
  }
  if (doc.querySelector("canvas[data-orca-chart]")) {
    loadChartJs(function () {
      drawCharts();
      new MutationObserver(drawCharts).observe(doc.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
      if (window.matchMedia) matchMedia("(prefers-color-scheme: dark)").addEventListener("change", drawCharts);
    });
  }
  window.ORCA.drawCharts = function () { loadChartJs(drawCharts); };

  /* ---------------------------------------------------------------- table of contents ("On this page") */
  function slug(text) { return text.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || "section"; }
  function initToc(toc) {
    var body = byId(toc.getAttribute("data-orca-toc")); var list = toc.querySelector(".orca-toc__list");
    if (!body || !list) return;
    if (!list.children.length) {
      var used = {};
      Array.prototype.forEach.call(body.querySelectorAll("h2"), function (h) {
        if (closest(h, ".orca-live-example, .orca-code-block, dialog, template, [hidden], .orca-sr-only") || h.classList.contains("orca-sr-only")) return;
        if (!h.id) { var base = slug(h.textContent), id = base, n = 2; while (byId(id) || used[id]) id = base + "-" + n++; h.id = id; }
        used[h.id] = true;
        var li = doc.createElement("li"), a = doc.createElement("a");
        a.href = "#" + h.id; a.textContent = h.textContent.trim(); li.appendChild(a); list.appendChild(li);
      });
    }
    toc.hidden = !list.children.length;
    if (toc.hidden) return;
    var links = Array.prototype.slice.call(list.querySelectorAll("a"));
    var targets = links.map(function (a) { return byId(decodeURIComponent(a.getAttribute("href").slice(1))); });
    var queued = false;
    function spy() {
      queued = false;
      var at = -1;
      targets.forEach(function (t, i) { if (t && t.getBoundingClientRect().top <= 120) at = i; });
      if (window.innerHeight + window.pageYOffset >= doc.documentElement.scrollHeight - 2) at = links.length - 1;
      links.forEach(function (a, i) { if (i === at) a.setAttribute("aria-current", "location"); else a.removeAttribute("aria-current"); });
    }
    window.addEventListener("scroll", function () { if (!queued) { queued = true; window.requestAnimationFrame(spy); } }, { passive: true });
    window.addEventListener("resize", spy);
    spy();
    if (window.matchMedia) {
      var narrow = window.matchMedia("(max-width: 1099px)");
      var fit = function () { toc.open = !narrow.matches; };
      fit();
      if (narrow.addEventListener) narrow.addEventListener("change", fit);
    }
  }
  doc.querySelectorAll("[data-orca-toc]").forEach(initToc);

  /* ---------------------------------------------------------------- code colouring (highlight.js) */
  /* Code in [data-orca-highlight] and in code blocks is coloured by the vendored highlight.js, loaded only on pages that
     have code. Classes are prefixed orca-hl- and read the --orca-code-* tokens, so colours follow the theme. */
  var CODE = "code[data-orca-highlight], .orca-code-block pre > code";
  function highlightAll() {
    window.hljs.configure({ classPrefix: "orca-hl-", ignoreUnescapedHTML: true,
                            languages: ["django", "xml", "python", "bash", "css", "javascript", "json"] });
    doc.querySelectorAll(CODE).forEach(function (code) {
      if (code.hasAttribute("data-highlighted")) return;
      var lang = code.getAttribute("data-orca-highlight");
      if (lang) code.classList.add("language-" + lang);
      window.hljs.highlightElement(code);
    });
  }
  if (doc.querySelector(CODE)) {
    if (window.hljs) highlightAll();
    else {
      var hl = doc.createElement("script");
      hl.src = SELF_SRC.replace(/js\/orca\.js(\?.*)?$/, "vendor/highlight.min.js"); hl.onload = highlightAll;
      var hlNonce = doc.querySelector("script[nonce]"); if (hlNonce) hl.nonce = hlNonce.nonce || hlNonce.getAttribute("nonce");
      doc.head.appendChild(hl);
    }
  }
})();
