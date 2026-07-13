# kodade-site

Landing page and public documentation for **ködade**, an Agentic Development
Environment (a macOS terminal app that orchestrates agent CLIs). The landing
page stays hand-authored HTML/CSS; MkDocs builds the documentation. Both ship in
one curated Cloudflare Pages artifact.

## Status
active — last touched 2026-07-13

## Commands
```bash
# first-time setup (Python is pinned for Cloudflare Pages v3)
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt

# build and preview the same artifact Cloudflare publishes
./scripts/build.sh
python3 -m http.server --directory dist 8000
```

## Architecture
- `index.html` + `styles.css` — the hand-authored landing page. Do not route it
  through MkDocs or change its output as part of documentation work.
- `fonts/jetbrains-mono-latin.woff2` — self-hosted JetBrains Mono (latin subset,
  variable weight, ~31 KB). The only binary asset; no external font requests.
- `docs/` + `mkdocs.yml` — public documentation source and navigation. MkDocs
  builds it with strict warnings and directory URLs under `dist/docs/`.
- `public/` — Cloudflare Pages control files and the root 404 page. These are
  copied explicitly; it is not a general-purpose static-assets directory.
- `scripts/build.sh` — removes `dist/`, copies only approved landing/Cloudflare
  files, builds the docs, and verifies the artifact boundary.
- `dist/` — generated deploy output. Never edit or commit it.
- `DESIGN.md` — brand + design reference. **Read it before touching copy or CSS**;
  it is the source of truth for tokens, type, voice, and page structure.
- `Ködade Brand.dc.html` — logo exploration archive (decision landed: double-dot
  mark, option 1d → 2a). Reference only, don't edit.
- `favicon.svg` — the umlaut double-dot mark.
- `PLAN.md` is referenced by DESIGN.md but lives with the product repo, not here.

## Conventions & Gotchas
- Wordmark is always lowercase `ködade` (with umlaut); ASCII contexts (domain,
  package, CLI) use `kodade` — never "koedade".
- Brand is theme-neutral: ink scale + one amber accent (`oklch(0.78 0.15 75)` on
  dark, `oklch(0.66 0.14 75)` on light). Accent only for the umlaut dots, primary
  CTA, and live indicators — never body text or background washes.
- Type: JetBrains Mono for wordmark/display, system stack for body. Max 2 families.
- Voice: plain, technical, confident. No emoji, no exclamation marks, no
  "blazingly", no overpromising ("ködade orchestrates CLIs; the CLIs do the work").
  One allowed flourish: umlaut wordplay in headlines.
- Performance is credibility: static output, no frontend framework, landing
  page < 200 KB, no cookie banner, no analytics scripts that need one.
- Run `./scripts/build.sh` before committing documentation or deployment changes.
  Warnings fail the build. Do not loosen strict mode to land content.
- Keep documentation task-oriented and progressively disclosed: one interface
  for new users and experienced engineers, not separate beginner/expert modes.
- Product behavior must come from the current `kodade` app implementation and
  tests. Windows is in development; do not claim availability or parity.
- No gradients, no glassmorphism, no mascots, never restyle provider logos.

## Out of Scope
- No frontend framework or npm. The landing page remains plain HTML/CSS (JS only
  if trivial and inline); MkDocs is the documentation build dependency.
- No app code. The product implementation and PLAN.md live in the `kodade` repo.
- No broad repository copies into `dist/`; every non-MkDocs root artifact must
  be explicitly allowlisted in `scripts/build.sh`.
