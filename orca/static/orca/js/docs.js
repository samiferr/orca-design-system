/* ORCA documentation site only: sidebar page search, page filters in the right drawer, phone menu, copy buttons. */
(function () {
  "use strict";
  var filter = document.querySelector("[data-docs-filter]");
  var nav = document.getElementById("docs-nav");

  if (filter && nav) {
    var empty = nav.querySelector("[data-docs-empty]");
    filter.addEventListener("input", function () {
      var q = filter.value.trim().toLowerCase();
      var shown = 0;
      nav.querySelectorAll(".docs-nav__section").forEach(function (section) {
        var sectionShown = 0;
        section.querySelectorAll("li").forEach(function (li) {
          var hit = !q || li.textContent.toLowerCase().indexOf(q) !== -1;
          li.hidden = !hit;
          if (hit) sectionShown++;
        });
        section.querySelectorAll("details").forEach(function (d) {
          var any = d.querySelector("li:not([hidden])");
          d.hidden = !any;
          if (q && any) d.open = true;
        });
        section.hidden = q && !sectionShown;
        shown += sectionShown;
      });
      if (empty) empty.hidden = shown > 0;
    });
    var current = nav.querySelector("[aria-current=page]");
    if (current && current.scrollIntoView) current.scrollIntoView({ block: "center" });
  }

  /* Page filters (Primitives page): the drawer's form narrows the cards live; applied filters show as tags. */
  var drawer = document.querySelector("[data-docs-filters]");
  if (drawer) {
    var form = drawer.querySelector("form");
    var items = document.querySelectorAll("[data-docs-item]");
    var openButton = document.querySelector("[data-docs-filters-open]");
    var countBadge = document.querySelector("[data-docs-filters-count]");
    var applied = document.querySelector("[data-docs-applied]");
    var tags = document.querySelector("[data-docs-tags]");
    var results = document.querySelector("[data-docs-results]");
    var none = document.querySelector("[data-docs-none]");
    var show = drawer.querySelector("[data-docs-show]");
    var total = items.length;
    var closeIcon = document.querySelector("template[data-docs-close-icon]");

    var state = function () {
      var q = form.elements.q.value.trim().toLowerCase();
      var cats = Array.prototype.filter.call(form.querySelectorAll("input[name=category]"), function (c) { return c.checked; });
      var source = form.querySelector("input[name=source]:checked");
      return { q: q, cats: cats, source: source && source.value ? source : null };
    };

    var tag = function (text, clear) {
      var span = document.createElement("span");
      span.className = "orca-tag";
      var label = document.createElement("span");
      label.className = "orca-tag__text";
      label.textContent = text;
      var remove = document.createElement("button");
      remove.type = "button";
      remove.className = "orca-tag__remove";
      remove.setAttribute("aria-label", "Remove " + text);
      if (closeIcon) remove.appendChild(closeIcon.content.cloneNode(true));
      remove.addEventListener("click", function () { clear(); apply(); });
      span.appendChild(label); span.appendChild(remove);
      return span;
    };

    var apply = function () {
      var s = state();
      var shown = 0;
      items.forEach(function (li) {
        var hit = (!s.q || li.getAttribute("data-text").toLowerCase().indexOf(s.q) !== -1) &&
          (!s.cats.length || s.cats.some(function (c) { return c.value === li.getAttribute("data-category"); })) &&
          (!s.source || s.source.value === li.getAttribute("data-source"));
        li.hidden = !hit;
        if (hit) shown++;
      });
      document.querySelectorAll("[data-docs-group]").forEach(function (g) { g.hidden = !g.querySelector("[data-docs-item]:not([hidden])"); });
      var active = (s.q ? 1 : 0) + s.cats.length + (s.source ? 1 : 0);
      document.querySelectorAll("[data-docs-unfiltered]").forEach(function (el) { el.hidden = active > 0; });
      countBadge.hidden = !active;
      countBadge.textContent = active;
      openButton.setAttribute("aria-label", active ? "Filters, " + active + " applied" : "Filters");
      applied.hidden = !active;
      none.hidden = shown > 0;
      results.textContent = "Showing " + shown + " of " + total + " elements";
      show.textContent = shown === 1 ? "Show 1 element" : "Show " + shown + " elements";
      tags.textContent = "";
      if (s.q) tags.appendChild(tag("“" + form.elements.q.value.trim() + "”", function () { form.elements.q.value = ""; }));
      s.cats.forEach(function (c) { tags.appendChild(tag(c.getAttribute("data-label"), function () { c.checked = false; })); });
      if (s.source) tags.appendChild(tag(s.source.getAttribute("data-label"), function () { form.querySelector("input[name=source][value='']").checked = true; }));
    };

    form.addEventListener("input", apply);
    form.addEventListener("change", apply);
    document.querySelectorAll("[data-docs-clear]").forEach(function (b) {
      b.addEventListener("click", function () { form.reset(); apply(); });
    });
    apply();
  }

  var menu = document.querySelector("[data-docs-menu]");
  if (menu && nav) {
    menu.addEventListener("click", function () {
      var open = menu.getAttribute("aria-expanded") !== "true";
      menu.setAttribute("aria-expanded", open ? "true" : "false");
      menu.setAttribute("aria-label", open ? "Hide navigation" : "Show navigation");
      document.body.classList.toggle("docs--nav-open", open);
      if (open && filter) filter.focus();
    });
  }

  // Template previews: show the page at desktop, tablet or phone width.
  document.querySelectorAll("[data-docs-viewport]").forEach(function (group) {
    var frame = group.closest(".docs-example").querySelector("[data-docs-frame]");
    group.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-width]"); if (!b || !frame) return;
      group.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      frame.style.maxWidth = b.getAttribute("data-width") || "";
    });
  });

  document.querySelectorAll("pre.docs-code").forEach(function (pre) {
    var button = document.createElement("button");
    button.type = "button";
    button.className = "orca-button orca-button--sm docs-code__copy";
    button.textContent = "Copy";
    button.addEventListener("click", function () {
      var text = pre.querySelector("code").textContent;
      var done = function () { button.textContent = "Copied"; setTimeout(function () { button.textContent = "Copy"; }, 1500); };
      if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(done, function () { select(pre); });
      } else { select(pre); }
    });
    pre.appendChild(button);
  });

  function select(el) {
    var range = document.createRange();
    range.selectNodeContents(el.querySelector("code"));
    var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(range);
  }
})();
