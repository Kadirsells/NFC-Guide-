// Kleine Interaktionen der statischen Seite (ersetzt das React-Bundle von Lovable).
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Kopfzeile bekommt beim Scrollen einen Hintergrund
  var header = document.querySelector("[data-header]");
  if (header) {
    var on = ["border-accent/60", "bg-background/80", "backdrop-blur-md"];
    var off = ["border-transparent", "bg-transparent"];
    var setHeader = function () {
      var s = window.scrollY > 8;
      on.forEach(function (c) { header.classList.toggle(c, s); });
      off.forEach(function (c) { header.classList.toggle(c, !s); });
    };
    window.addEventListener("scroll", setHeader, { passive: true });
    setHeader();
  }

  // Hero: Umschalten zwischen Praxis-Guide und Lieferantenkontakt
  var hero = document.querySelector("[data-hero]");
  if (hero) {
    var data = JSON.parse(hero.getAttribute("data-hero"));
    var current = "guide";
    var fades = hero.querySelectorAll(".ks-fade");
    var show = function (key, instant) {
      if (!data[key] || (key === current && !instant)) return;
      current = key;
      hero.querySelectorAll("[data-stack]").forEach(function (st) {
        st.querySelectorAll("[data-card]").forEach(function (c) {
          var front = c.getAttribute("data-card") === key;
          c.classList.toggle("is-front", front);
          c.classList.toggle("is-back", !front);
          c.tabIndex = front ? -1 : 0;
        });
        st.querySelectorAll("[data-tab]").forEach(function (t) {
          var sel = t.getAttribute("data-tab") === key;
          t.setAttribute("aria-selected", sel ? "true" : "false");
          t.tabIndex = sel ? 0 : -1;
        });
        var counter = st.querySelector("[data-counter]");
        if (counter) counter.textContent = data[key].counter;
      });
      var apply = function () {
        var d = data[key];
        hero.querySelectorAll("[data-f]").forEach(function (el) {
          var f = el.getAttribute("data-f");
          if (d[f] !== undefined) el.textContent = d[f];
        });
        var cta = hero.querySelector("#hero-cta");
        if (cta) cta.setAttribute("href", d.href);
        fades.forEach(function (el) { el.classList.remove("is-fading"); });
      };
      if (instant || reduce) { apply(); return; }
      fades.forEach(function (el) { el.classList.add("is-fading"); });
      window.setTimeout(apply, 200);
      if (history.replaceState) history.replaceState(null, "", "#" + key);
    };
    hero.addEventListener("click", function (e) {
      var el = e.target.closest("[data-card],[data-tab]");
      if (!el) return;
      show(el.getAttribute("data-card") || el.getAttribute("data-tab"));
    });
    hero.addEventListener("keydown", function (e) {
      var t = e.target.closest("[data-tab]");
      if (!t || (e.key !== "ArrowLeft" && e.key !== "ArrowRight")) return;
      var next = current === "guide" ? "lieferant" : "guide";
      show(next);
      var n = t.parentNode.querySelector('[data-tab="' + next + '"]');
      if (n) n.focus();
      e.preventDefault();
    });
    hero.querySelectorAll("[data-stack]").forEach(function (st) {
      st.querySelectorAll("[data-card]").forEach(function (c) {
        if (c.classList.contains("is-front")) c.tabIndex = -1;
      });
      st.querySelectorAll('[data-tab][aria-selected="false"]').forEach(function (t) { t.tabIndex = -1; });
    });
    if (location.hash === "#lieferant") show("lieferant", true);
  }

  // Mobile Kaufleiste unten, sobald der Kauf-Button oben aus dem Bild ist
  var bar = document.querySelector("[data-sticky]");
  var cta = document.getElementById("hero-cta");
  if (bar && cta && "IntersectionObserver" in window) {
    new IntersectionObserver(function (entries) {
      var e = entries[0];
      var visible = !e.isIntersecting && e.boundingClientRect.top < 0;
      bar.classList.toggle("translate-y-full", !visible);
      bar.classList.toggle("translate-y-0", visible);
      bar.setAttribute("aria-hidden", visible ? "false" : "true");
      var link = bar.querySelector("a");
      if (link) link.tabIndex = visible ? 0 : -1;
    }).observe(cta);
  }
})();
