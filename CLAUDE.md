# Working agreement

Solo project, Lisanne is the only maintainer and does not do code review. Once a
change is correct and complete, commit, merge to `main`, and push directly —
do not stop to ask for permission first. GitHub keeps history, so a bad change
is just a revert away; default to shipping and iterating, not to pre-approval.

This applies to routine content/config changes (copy, links, contact info,
assets). Still pause and ask before anything genuinely destructive or
hard to reverse (force-push, history rewrite, deleting content).

This repo (`alrightapp.github.io`) hosts the marketing homepage plus the Support
and Privacy Policy pages required for App Store submission (Guideline 1.5 /
5.1.1(i)). See `README.md` for the URL layout. It publishes via
GitHub Pages directly from `main` — no build step, no Actions workflow needed.
Changes are live within a minute or two of a push to `main`.
