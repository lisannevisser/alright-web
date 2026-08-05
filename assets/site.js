/* alright — website behaviour

   Three small things, all progressive enhancements: without this file every
   style is simply listed one after another, the daily card shows one sentence,
   and the date on the card is the one written into the HTML. Nothing here
   loads, sends or stores anything.
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

  /* ---------------------------------------------- the three styles as tabs */

  each(document.querySelectorAll("[data-style-tabs]"), function (tablist) {
    var tabs = Array.prototype.slice.call(tablist.querySelectorAll(".style-tab"));
    var panels = tabs.map(function (tab) {
      return document.getElementById(tab.getAttribute("aria-controls"));
    });
    var screens = tabs.map(function (tab) {
      return document.getElementById(tab.dataset.screen);
    });

    var select = function (index, focus) {
      tabs.forEach(function (tab, i) {
        var on = i === index;
        tab.setAttribute("aria-selected", on ? "true" : "false");
        tab.tabIndex = on ? 0 : -1;
        if (panels[i]) panels[i].hidden = !on;
        if (screens[i]) screens[i].hidden = !on;
      });
      if (focus) tabs[index].focus();
    };

    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () { select(i, false); });
      tab.addEventListener("keydown", function (event) {
        var next = null;
        if (event.key === "ArrowRight" || event.key === "ArrowDown") next = (i + 1) % tabs.length;
        if (event.key === "ArrowLeft" || event.key === "ArrowUp") next = (i - 1 + tabs.length) % tabs.length;
        if (event.key === "Home") next = 0;
        if (event.key === "End") next = tabs.length - 1;
        if (next === null) return;
        event.preventDefault();
        select(next, true);
      });
    });

    select(0, false);
  });

  /* ------------------------------------------------ one card, then the next */

  each(document.querySelectorAll("[data-card]"), function (card) {
    if (!card.dataset.sentences) return;
    var sentences = JSON.parse(card.dataset.sentences);
    var target = card.querySelector("[data-card-sentence]");
    if (sentences.length < 2 || !target) return;

    var at = 0;
    var button = document.createElement("button");
    button.type = "button";
    button.className = "card-nudge";
    button.textContent = card.dataset.nudgeLabel || "Another sentence";
    /* The card is decorative next to the copy; announcing every flip would
       interrupt a screen reader mid-page for no gain. */
    target.setAttribute("aria-live", "off");

    button.addEventListener("click", function () {
      at = (at + 1) % sentences.length;
      target.textContent = sentences[at];
    });

    card.appendChild(button);
  });

  /* --------------------------------------------------------- today's date */

  /* The card carries a written-out date so it reads correctly without
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
