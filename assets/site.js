/* alright — website behaviour

   Three small things, all progressive enhancements: without this file the
   navigation stays open on a phone instead of hiding behind a button, the
   three styles simply stand next to each other, and the date on a mockup is
   the one written into the HTML. Nothing here loads, sends or stores
   anything.
*/
(function () {
  "use strict";

  document.documentElement.classList.add("js");

  var each = function (list, fn) { Array.prototype.forEach.call(list, fn); };

  /* The page language, taken from the nearest element that declares one. */
  var languageOf = function (node) {
    var owner = node.closest ? node.closest("[lang]") : null;
    return (owner && owner.lang) || document.documentElement.lang || "en";
  };

  var stillness = window.matchMedia
    ? window.matchMedia("(prefers-reduced-motion: reduce)")
    : { matches: false };

  /* --------------------------------------------------- the menu, on a phone */

  /* The nav is found through the button's own aria-controls rather than a
     fixed id, so a page carrying more than one header still wires each button
     to its own menu. */
  each(document.querySelectorAll(".nav-toggle"), function (toggle) {
    var nav = document.getElementById(toggle.getAttribute("aria-controls"));
    if (!nav) return;

    var setMenu = function (open) {
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      nav.classList.toggle("is-open", open);
      /* The sheet covers the page, so the page underneath must not scroll. */
      document.documentElement.classList.toggle("menu-open", open);
    };

    toggle.addEventListener("click", function () {
      setMenu(toggle.getAttribute("aria-expanded") !== "true");
    });

    /* Escape closes it, and so does following a link — the page navigates
       anyway, but the menu should not flash open on the way out. */
    document.addEventListener("keydown", function (event) {
      if (event.key !== "Escape") return;
      if (toggle.getAttribute("aria-expanded") !== "true") return;
      setMenu(false);
      toggle.focus();
    });

    each(nav.querySelectorAll("a"), function (link) {
      link.addEventListener("click", function () { setMenu(false); });
    });
  });

  /* ------------------------------------------- the three styles, on their own

     The phone wears one style at a time and changes by itself. Anyone who has
     asked their system for less motion keeps all three side by side instead:
     the same information, without something moving in the corner of the eye.
     The rotation also stops while the section is off screen, so it isn't
     running through a page nobody is looking at. */

  each(document.querySelectorAll("[data-style-stage]"), function (stage) {
    if (stillness.matches) return;

    var shots = Array.prototype.slice.call(stage.querySelectorAll(".style-shot"));
    if (shots.length < 2) return;

    var interval = parseInt(stage.dataset.interval, 10) || 4500;
    var at = 0;
    var timer = null;

    var show = function (index) {
      shots.forEach(function (shot, i) { shot.hidden = i !== index; });
    };

    var advance = function () {
      at = (at + 1) % shots.length;
      show(at);
    };

    var start = function () {
      if (timer === null) timer = window.setInterval(advance, interval);
    };
    var stop = function () {
      window.clearInterval(timer);
      timer = null;
    };

    var onScreen = true;
    var settle = function () {
      if (onScreen && !document.hidden) start(); else stop();
    };

    show(0);

    if (window.IntersectionObserver) {
      new IntersectionObserver(function (entries) {
        onScreen = entries[0].isIntersecting;
        settle();
      }, { threshold: 0.2 }).observe(stage);
    } else {
      start();
    }

    document.addEventListener("visibilitychange", settle);
  });

  /* --------------------------------------------------------- today's date */

  /* The mockups carry a written-out date so they read correctly without
     JavaScript; if JavaScript is there, it may as well be today's. */
  each(document.querySelectorAll("[data-today]"), function (node) {
    try {
      node.textContent = new Date().toLocaleDateString(languageOf(node), {
        weekday: "long", month: "long", day: "numeric"
      });
    } catch (error) {
      /* Leave the written-out date in place. */
    }
  });
})();
