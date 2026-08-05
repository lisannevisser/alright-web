# tools — optional, not a build step

The site is still plain static HTML: GitHub Pages serves the `index.html` files as they are, and
every one of them can be edited by hand. **Nothing here runs on deploy.**

These scripts exist for one reason: header and footer are duplicated in ten files. Changing the
navigation by hand means changing it ten times. The scripts write those ten files from one set of
sources, so a chrome change stays a one-line change.

## Using them

```bash
python3 tools/run.py            # rewrites all ten index.html files
python3 tools/build_preview.py  # bundles the whole site into one preview.html for review
```

`run.py` also refreshes `assets/fonts/` from the app repo when it finds one next door; point
`ALRIGHT_APP_REPO` at it if it lives somewhere else. Without it the fonts already in the repo stay
untouched.

## Files

| File | What it holds |
|---|---|
| `build_site.py` | Header, footer, labels, and the drawn components (lock screen, phone screens, sketches) |
| `content_en.py` | The English page bodies |
| `content_de.py` | The German page bodies |
| `run.py` | Renders every page |
| `build_preview.py` | One self-contained file with all ten pages, for review without a server |

Support and Privacy are a special case: `run.py` lifts their text out of the committed files
(from git HEAD, so a second run does not eat its own output) and only re-wraps it. Their wording is
never touched here — edit those pages directly.

## If they get in the way

Delete the folder. The site keeps working, and the HTML goes back to being hand-maintained, which
is what it was before.
