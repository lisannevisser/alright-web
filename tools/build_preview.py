#!/usr/bin/env python3
"""Bundle the whole site into one self-contained preview page.

The ten real pages become ten sections of one document, switched by the hash.
The site's own navigation drives it, so the preview clicks like the real thing
without needing a server.
"""
import base64
import pathlib
import posixpath
import re

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(__file__).parent / "preview.html"

PAGES = [
    ("home", "", "en"), ("home-de", "de/", "de"),
    ("about", "about/", "en"), ("about-de", "about/de/", "de"),
    ("next", "whats-next/", "en"), ("next-de", "whats-next/de/", "de"),
    ("support", "support/", "en"), ("support-de", "support/de/", "de"),
    ("privacy", "privacy/", "en"), ("privacy-de", "privacy/de/", "de"),
]
BY_PATH = {path: pid for pid, path, _ in PAGES}


def inline_css():
    css = (REPO / "assets" / "site.css").read_text(encoding="utf-8")
    for name in ("ArchivoBlack-Regular.ttf", "Outfit-Medium.ttf"):
        data = base64.b64encode((REPO / "assets" / "fonts" / name).read_bytes()).decode("ascii")
        css = css.replace(f'url("fonts/{name}") format("truetype")',
                          f'url(data:font/ttf;base64,{data}) format("truetype")')

    # The artifact viewer has its own light/dark toggle: it stamps data-theme on
    # the root, which has to beat the prefers-color-scheme query. The site only
    # varies tokens between the two themes, so the same two blocks do the job.
    light = re.search(r":root \{\n(.*?)\n\}", css, re.S).group(1)
    dark = re.search(r"@media \(prefers-color-scheme: dark\) \{\n  :root \{\n(.*?)\n  \}\n\}",
                     css, re.S).group(1)
    return css + f"""

:root[data-theme="light"] {{
{light}
}}
:root[data-theme="dark"] {{
{dark}
}}
"""


def resolve(href, from_path):
    """A relative href on a real page -> the id of the page it points at."""
    target = posixpath.normpath(posixpath.join("/" + from_path, href)).strip("/")
    target = target + "/" if target else ""
    return BY_PATH.get(target)


def section(pid, path, lang):
    html = (REPO / path / "index.html").read_text(encoding="utf-8")
    body = re.search(r"<body>(.*)</body>", html, re.S).group(1)
    body = re.sub(r'<script src="[^"]*"></script>\s*', "", body)

    # Ten pages in one document means ten of every id. Namespace them.
    body = re.sub(r'(\sid=")([^"]+)(")', lambda m: m.group(1) + pid + "-" + m.group(2) + m.group(3), body)
    for attr in ("aria-controls", "aria-labelledby", "data-screen"):
        body = re.sub(r'(\s%s=")([^"]+)(")' % attr,
                      lambda m: m.group(1) + pid + "-" + m.group(2) + m.group(3), body)

    # Internal links become hash links between the sections.
    def relink(match):
        href = match.group(1)
        if href.startswith(("mailto:", "http", "#")):
            return match.group(0)
        target = resolve(href, path)
        return 'href="#%s"' % target if target else 'href="#%s"' % pid
    body = re.sub(r'href="([^"]*)"', relink, body)

    return (f'<div class="preview-page" id="{pid}" lang="{lang}" hidden>\n'
            f'{body}\n</div>')


sections = "\n\n".join(section(pid, path, lang) for pid, path, lang in PAGES)

preview = f"""<style>
{inline_css()}

/* Preview shell — not part of the site */
.preview-page[hidden] {{ display: none; }}
.preview-bar {{
  position: sticky;
  top: 0;
  z-index: 10;
  background: var(--ink);
  color: var(--bg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  font-size: 0.8rem;
  letter-spacing: 0.02em;
  padding: 0.55rem clamp(1.25rem, 5vw, 3rem);
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.5rem;
  align-items: baseline;
  justify-content: space-between;
}}
.preview-bar strong {{ font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }}
.preview-bar span {{ opacity: 0.75; }}
</style>

<div class="preview-bar">
  <strong>Preview</strong>
  <span>Branch claude/revised-landing-page-700n4k · alle Links funktionieren · Hell/Dunkel folgt deinem System</span>
</div>

{sections}

<script>
(function () {{
  var ids = {[pid for pid, _, _ in PAGES]!r}.map(String);
  function show() {{
    var id = (location.hash || "#home").slice(1);
    if (ids.indexOf(id) === -1) id = "home";
    ids.forEach(function (each) {{
      document.getElementById(each).hidden = each !== id;
    }});
    window.scrollTo(0, 0);
  }}
  window.addEventListener("hashchange", show);
  show();
}})();
</script>

<script>
{(REPO / 'assets' / 'site.js').read_text(encoding='utf-8')}
</script>
"""

OUT.write_text(preview, encoding="utf-8")
print("wrote", OUT, f"{OUT.stat().st_size / 1024:.0f} KB")
