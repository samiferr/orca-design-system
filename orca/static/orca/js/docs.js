/* ORCA documentation site only: behaviour, no styling. Everything it touches is ORCA markup
   (the docs sidebar tree, the filter drawer, applied filters and the empty state).
   - opens the sidebar scrolled to the current page;
   - narrows the element cards live from the filter drawer, because the exported site has no server to filter on. */
(function () {
  "use strict";
  var nav = document.getElementById("orca-sidebar");
  var current = nav && nav.querySelector("[aria-current=page]");
  if (current && nav.scrollHeight > nav.clientHeight) nav.scrollTop = Math.max(0, current.offsetTop - nav.clientHeight / 2);

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

})();
