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
- `assets/site.js` — two progressive enhancements: the style switcher on the homepage and the
  “another sentence” button on the daily card. Without it every style is simply listed and the
  card shows one sentence. Nothing is loaded, sent or stored.
- `assets/fonts/ArchivoBlack-Regular.ttf` — the typeface the app sets the Bold style in (OFL,
  licence alongside it). Loaded only so the style preview shows the real thing. Everything else
  on the site is system type.

Header and footer are duplicated in each `index.html` on purpose: it keeps the site editable
without a toolchain. Change one, change all ten.

The whole site is `noindex` for now (`robots.txt` plus a meta tag on every page). Worth turning
on at the App Store release, not before.

All content © Lisanne Visser. Not licensed for reuse.
