# alright — website

Marketing site, Support and Privacy Policy pages for the [alright](https://apps.apple.com) app (al/right).
Support and Privacy exist because Apple requires a working Support URL and Privacy Policy URL for
every app (Guideline 1.5 and 5.1.1(i)); the rest is marketing.

Plain static HTML, no build step. Served via GitHub Pages.

## Pages

Every page exists in English and German. German lives under a `de/` subfolder of the English URL.

| Page | English | German |
|---|---|---|
| Home | `/` | `/de/` |
| Design — how the app is made | `/design/` | `/design/de/` |
| What's next — roadmap, no dates | `/whats-next/` | `/whats-next/de/` |
| Support | `/support/` | `/support/de/` |
| Privacy Policy | `/privacy/` | `/privacy/de/` |

Note: Support used to live at `/`. The Support URL in App Store Connect has to point at
`/support/`, otherwise people coming from the App Store land on the marketing page.

## Shared assets

- `assets/site.css` — the whole design system, linked by every page. Tokens at the top; the
  three app styles (Clean, Editorial, Bold) are reproduced from the colours in the app's
  `Brand.swift` and `ThemeStyle.swift`.
- `assets/site.js` — three progressive enhancements: the menu button on phones, the phone on the
  homepage that changes style by itself every few seconds, and today's date in the mockups. Without it the navigation stays open on a phone, all three
  styles simply stand next to each other, and the written-out date stays. The rotation stops while the
  section is off screen and never starts for anyone who asked their system for reduced motion.
  Nothing is loaded, sent or stored.
- `assets/fonts/` — Archivo Black, the typeface the app sets the Bold style in, and Outfit,
  the brand mark face, which sets the single “a” on the app icon in the lock screen mockup
  (both OFL, licences alongside them). Everything else on the site is system type.

Header and footer are duplicated in each `index.html` on purpose: it keeps the site editable
without a toolchain. Change one, change all ten.

The whole site is `noindex` for now (`robots.txt` plus a meta tag on every page). Worth turning
on at the App Store release, not before.

All content © Lisanne Visser. Not licensed for reuse.
