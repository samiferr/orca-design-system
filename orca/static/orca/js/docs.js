/* ORCA documentation site only: sidebar filter, phone menu, copy buttons on code blocks. */
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
