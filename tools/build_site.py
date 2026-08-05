#!/usr/bin/env python3
"""One-off generator for the alright website.

Writes plain, hand-editable HTML into the repo. The repo itself keeps its
"no build step" property: this script exists so the shared header/footer are
written once instead of twelve times, and is not part of the site.
"""
import re
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent

# The wordmark, lifted verbatim from the page it already lives on.
SRC = (REPO / "index.html").read_text(encoding="utf-8")
LOGO = re.search(r'<svg class="logo".*?</svg>', SRC, re.S).group(0)


def logo(indent):
    pad = " " * indent
    return "\n".join(pad + line.strip() if i else line
                     for i, line in enumerate(LOGO.splitlines()))


PAGES = ["", "about/", "whats-next/", "support/", "privacy/"]

NAV = {
    "en": [("about/", "About"), ("whats-next/", "What&#8217;s next"),
           ("support/", "Support")],
    "de": [("about/", "Über"), ("whats-next/", "Was kommt"),
           ("support/", "Support")],
}

LABELS = {
    "en": {
        "lang_other": "Deutsch",
        "tagline": "Everything&#8217;s alright.",
        "col_app": "The app",
        "col_legal": "Legal",
        "home": "Home",
        "privacy": "Privacy Policy",
        "support": "Support",
        "about": "About",
        "next": "What&#8217;s next",
        "contact": "Contact",
        "contact_hint": "Opens your mail app",
        "rights": "© 2026 Lisanne Visser",
        "skip": "Skip to content",
        "menu": "Menu",
    },
    "de": {
        "lang_other": "English",
        "tagline": "Everything&#8217;s alright.",
        "col_app": "Die App",
        "col_legal": "Rechtliches",
        "home": "Startseite",
        "privacy": "Datenschutzerklärung",
        "support": "Support",
        "about": "Über",
        "next": "Was kommt",
        "contact": "Kontakt",
        "contact_hint": "Öffnet dein Mailprogramm",
        "rights": "© 2026 Lisanne Visser",
        "skip": "Zum Inhalt springen",
        "menu": "Menü",
    },
}


def path_for(page, lang):
    """Directory of a page in a language, relative to the site root."""
    if lang == "en":
        return page
    return page + "de/"


def href(page, lang, current):
    """Link from `current` (a site-root-relative dir) to `page` in `lang`."""
    depth = len([p for p in current.split("/") if p])
    return "../" * depth + path_for(page, lang) or "./"


def chrome_header(page, lang, current):
    items = []
    for target, label in NAV[lang]:
        aria = ' aria-current="page"' if target == page else ""
        items.append(f'        <a href="{href(target, lang, current)}"{aria}>{label}</a>')
    other = "de" if lang == "en" else "en"
    items.append(f'        <a class="nav-lang" href="{href(page, other, current)}">'
                 f'{LABELS[lang]["lang_other"]}</a>')
    home = href("", lang, current)
    return f"""<a class="skip-link" href="#content">{LABELS[lang]['skip']}</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{home}" aria-label="alright">
      {logo(6)}
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false"
            aria-controls="site-nav" aria-label="{LABELS[lang]['menu']}">
      <span class="nav-icon" aria-hidden="true"></span>
    </button>
    <nav class="site-nav" id="site-nav" aria-label="{'Hauptnavigation' if lang == 'de' else 'Main'}">
{chr(10).join(items)}
    </nav>
  </div>
</header>"""


def chrome_footer(lang, current):
    t = LABELS[lang]
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <p class="footer-mark">
          {logo(10)}
        </p>
        <p class="footer-tagline">{t['tagline']}</p>
      </div>
      <div class="footer-col">
        <h2>{t['col_app']}</h2>
        <ul>
          <li><a href="{href('', lang, current)}">{t['home']}</a></li>
          <li><a href="{href('about/', lang, current)}">{t['about']}</a></li>
          <li><a href="{href('whats-next/', lang, current)}">{t['next']}</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h2>{t['col_legal']}</h2>
        <ul>
          <li><a href="{href('support/', lang, current)}">{t['support']}</a></li>
          <li><a href="{href('privacy/', lang, current)}">{t['privacy']}</a></li>
          <li><a href="mailto:alrightapp@icloud.com" title="alrightapp@icloud.com">{t['contact']}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>{t['rights']}</p>
      <p><a href="{href(CURRENT_PAGE, 'de' if lang == 'en' else 'en', current)}">{t['lang_other']}</a></p>
    </div>
  </div>
</footer>"""


CURRENT_PAGE = ""


def render(page, lang, title, description, body):
    global CURRENT_PAGE
    CURRENT_PAGE = page
    current = path_for(page, lang)
    depth = len([p for p in current.split("/") if p])
    root = "../" * depth
    head_extra = f"""<link rel="stylesheet" href="{root}assets/site.css">
<link rel="icon" type="image/svg+xml" href="{root}favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="{root}favicon.png">
<link rel="icon" type="image/png" sizes="16x16" href="{root}favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="{root}apple-touch-icon.png">"""
    body = body.replace("%%ROOT%%", root or "./")
    for token, target in (("%%HOME%%", ""), ("%%ABOUT%%", "about/"),
                          ("%%NEXT%%", "whats-next/"), ("%%SUPPORT%%", "support/"),
                          ("%%PRIVACY%%", "privacy/")):
        body = body.replace(token, href(target, lang, current))
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="noindex, nofollow">
{head_extra}
</head>
<body>
{chrome_header(page, lang, current)}

<main id="content">
{body}
</main>

{chrome_footer(lang, current)}
<script src="{root}assets/site.js"></script>
</body>
</html>
"""
    out = REPO / current / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


# --------------------------------------------------------------- components

def lockscreen(sentence, date, time, when, label):
    """A locked phone with the day's notification on it: the product itself."""
    return f"""<div class="device">
      <div class="device-screen screen-lock" role="img" aria-label="{label}">
        <p class="lock-date" data-today>{date}</p>
        <p class="lock-time">{time}</p>
        <div class="lock-notification">
          <p class="lock-meta">
            <span class="lock-icon" aria-hidden="true">a</span>
            <span class="lock-app">alright</span>
            <span class="lock-when">{when}</span>
          </p>
          <p class="lock-sentence">{sentence}</p>
        </div>
        <div class="lock-bar" aria-hidden="true"></div>
      </div>
    </div>"""


def screen(kind, sentence, date, initial=None, screen_id=None, hidden=False):
    """One phone screen in one of the app's three styles."""
    idattr = f' id="{screen_id}"' if screen_id else ""
    hid = " hidden" if hidden else ""
    if kind == "editorial":
        rest = sentence[len(initial):] if initial else sentence
        body = (f'<p class="screen-sentence">'
                f'<span class="initial" aria-hidden="true">{initial}</span>'
                f'<span class="visually-hidden">{initial}</span>{rest}</p>')
    elif kind == "bold":
        body = (f'<div class="slab"><p class="screen-sentence">'
                f'{sentence}</p></div>')
    else:
        body = f'<p class="screen-sentence">{sentence}</p>'
    return f"""<div class="device"{idattr}{hid}>
      <div class="device-screen screen-{kind}">
        <div class="screen-body">
          {body}
          <p class="screen-date" data-today>{date}</p>
        </div>
      </div>
    </div>"""


# ------------------------------------------------------- sketches, not shots

# Nothing on the what's-next page exists yet, so nothing there can be a
# screenshot. These are drawn diagrams of the idea, labelled as such.

def sketch(kind, label, body):
    return f"""<figure class="sketch sketch-{kind}">
        <div class="sketch-frame" role="img" aria-label="{label}">
{body}
        </div>
      </figure>"""


def sketch_widget(sentence, label):
    """The daily sentence as a home screen widget, set in the Bold style."""
    body = """          <div class="widget-wall">
            <div class="widget-tile">
              <p class="widget-sentence">%s</p>
            </div>
            <div class="widget-dock" aria-hidden="true">
              <span></span><span></span><span></span><span></span>
            </div>
          </div>""" % sentence
    return sketch("widget", label, body)


def sketch_keep(sentences, label):
    """A short list of kept sentences, one of them just added."""
    rows = "\n".join(
        '              <li%s><span class="keep-mark" aria-hidden="true"></span>%s</li>'
        % (' class="is-new"' if i == 0 else "", text)
        for i, text in enumerate(sentences))
    return sketch("keep", label, f"""          <ul class="keep-list">
{rows}
          </ul>""")


def sketch_year(have, total, label, caption):
    """One square per day of the year: filled where a sentence already exists."""
    cells = "".join('<i class="%s"></i>' % ("on" if i < have else "off")
                    for i in range(total))
    return sketch("year", label, f"""          <div class="year-grid" aria-hidden="true">{cells}</div>
          <p class="year-caption">{caption}</p>""")


def sketch_colours(label, swatches):
    """A row of accent colours, one of them picked."""
    dots = "\n".join(
        '            <span class="swatch%s" style="--swatch: %s"></span>'
        % (" is-picked" if i == 1 else "", colour)
        for i, colour in enumerate(swatches))
    return sketch("colours", label, f"""          <div class="swatch-row" aria-hidden="true">
{dots}
          </div>""")


def scheme_matrix(sentence, initial, date, light, dark, caption):
    """The three styles in both schemes, six phones, no controls.

    The page follows the reader's system and therefore shows one of the two.
    This figure pins both, because "drawn twice rather than inverted" is a
    claim that has to be visible to be worth making.
    """
    def row(cls, label):
        return f"""        <p class="scheme-label">{label}</p>
        <div class="scheme-row {cls}">
          {screen("clean", sentence, date)}
          {screen("editorial", sentence, date, initial=initial)}
          {screen("bold", sentence, date)}
        </div>"""

    return f"""<figure class="scheme-figure">
      <div>
{row("scheme-light", light)}
      </div>
      <div style="margin-top: 1.75rem">
{row("scheme-dark", dark)}
      </div>
      <figcaption>{caption}</figcaption>
    </figure>"""
