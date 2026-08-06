#!/usr/bin/env python3
"""Render every page of the site."""
import os
import re
import shutil
import subprocess
import pathlib

import build_site
from build_site import REPO, render
import content_en as en
import content_de as de

# Path to the app repo, only needed to refresh the bundled fonts.
APP = pathlib.Path(os.environ.get("ALRIGHT_APP_REPO", "../alrightapp")).expanduser()

# ---------------------------------------------------------------- carry-over
# Support and Privacy keep their text exactly as it is; only the surrounding
# chrome changes. Pull the content out of the pages as they stand today.


def carry(path):
    # From git HEAD, not from disk: the file on disk may already be a rendered
    # result of an earlier run of this script, and re-wrapping a wrapped page
    # loses its subline. Falls back to the working copy outside a checkout.
    done = subprocess.run(["git", "-C", str(REPO), "show", "HEAD:" + path],
                          capture_output=True, text=True)
    src = done.stdout if done.returncode == 0 else (REPO / path).read_text(encoding="utf-8")
    head = re.search(r"<h1>(.*?)</h1>", src, re.S).group(1)
    sub = re.search(r'<p class="(?:tagline|meta)">(.*?)</p>', src, re.S)
    sections = re.findall(r"  <section>.*?</section>", src, re.S)
    return head, (sub.group(1).strip() if sub else None), sections


def prose_page(eyebrow, head, sub, sections, sub_class="lede"):
    subline = f'    <p class="{sub_class}">{sub}</p>\n' if sub else ""
    body = "\n\n".join(s.replace("\n  ", "\n  ") for s in sections)
    return f"""<section class="page-head">
  <div class="wrap wrap-narrow">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{head}</h1>
{subline}  </div>
</section>

<div class="wrap wrap-narrow">
<div class="prose">
{body}
</div>
</div>"""


# Links inside the carried-over text were written for the old file layout.
FIXUPS = {
    "support/index.html": [('href="../../privacy/"', 'href="%%PRIVACY%%"'),
                           ('href="../privacy/"', 'href="%%PRIVACY%%"')],
    "support/de/index.html": [('href="../../privacy/de/"', 'href="%%PRIVACY%%"')],
    "privacy/index.html": [],
    "privacy/de/index.html": [],
}

# ------------------------------------------------------------------- render

PAGES = []

PAGES.append(dict(
    page="", lang="en",
    title="alright — one affirmation a day",
    description="alright shows you one affirmation a day: one quiet notification, "
                "no account, no tracking. Coming to the App Store.",
    body=en.HOME))
PAGES.append(dict(
    page="", lang="de",
    title="alright — ein Satz am Tag",
    description="alright zeigt dir jeden Tag eine Affirmation: eine leise Mitteilung, "
                "kein Account, kein Tracking. Bald im App Store.",
    body=de.HOME))

PAGES.append(dict(
    page="about/", lang="en",
    title="About — alright",
    description="Made by one person: Lisanne Visser, designer, builder and yoga "
                "teacher. Why alright exists and how it is built.",
    body=en.ABOUT))
PAGES.append(dict(
    page="about/", lang="de",
    title="Über — alright",
    description="Gemacht von einer Person: Lisanne Visser, Designerin, Builderin und "
                "Yogalehrerin. Warum es alright gibt und wie es gebaut ist.",
    body=de.ABOUT))

PAGES.append(dict(
    page="whats-next/", lang="en",
    title="What&#8217;s next — alright",
    description="What comes after version one, what is being weighed, and what alright "
                "will never do. No dates.",
    body=en.NEXT))
PAGES.append(dict(
    page="whats-next/", lang="de",
    title="Was als Nächstes kommt — alright",
    description="Was nach Version eins kommt, was abgewogen wird und was alright nie "
                "tun wird. Ohne Termin.",
    body=de.NEXT))

for page, lang, path, eyebrow in (
    ("support/", "en", "support/index.html", "Support"),
    ("support/", "de", "support/de/index.html", "Support"),
    ("privacy/", "en", "privacy/index.html", "Legal"),
    ("privacy/", "de", "privacy/de/index.html", "Rechtliches"),
):
    head, sub, sections = carry(path)
    body = prose_page(eyebrow, head, sub, sections,
                      sub_class="lede" if page == "support/" else "meta")
    for old, new in FIXUPS[path]:
        body = body.replace(old, new)
    titles = {
        ("support/", "en"): ("Support — alright", "How to reach the person who builds alright, and answers to the usual questions."),
        ("support/", "de"): ("Support — alright", "Kontakt zur Entwicklerin von alright und Antworten auf die häufigsten Fragen."),
        ("privacy/", "en"): ("Privacy Policy — alright", "alright collects no data: no account, no analytics, no network calls."),
        ("privacy/", "de"): ("Datenschutzerklärung — alright", "alright erhebt keine Daten: kein Konto, keine Analyse, keine Netzwerkaufrufe."),
    }
    title, description = titles[(page, lang)]
    PAGES.append(dict(page=page, lang=lang, title=title, description=description, body=body))

for spec in PAGES:
    out = render(**spec)
    print("wrote", out.relative_to(REPO))

# ---------------------------------------------------------------- font asset

fonts = REPO / "assets" / "fonts"
if (APP / "Alright" / "Fonts").is_dir():
    fonts.mkdir(parents=True, exist_ok=True)
    for name in ("ArchivoBlack-Regular.ttf", "OFL-ArchivoBlack.txt",
                 "Outfit-Medium.ttf", "OFL-Outfit.txt"):
        shutil.copy(APP / "Alright" / "Fonts" / name, fonts / name)
        print("copied", name)
else:
    print("app repo not found, leaving assets/fonts as it is "
          "(set ALRIGHT_APP_REPO to refresh them)")
