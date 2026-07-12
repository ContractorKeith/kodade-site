# kodade-site

Static landing page for **ködade**, an Agentic Development Environment (a macOS
terminal app that orchestrates agent CLIs). This repo is the marketing site only —
one page, no build step, no dependencies. Done = kodade.com serving a fast,
brand-correct page with a working macOS download CTA.

## Status
active — last touched 2026-07-11

## Commands
```bash
# preview (no build step — either works):
open index.html
python3 -m http.server 8000   # then http://localhost:8000
```

## Architecture
- `index.html` + `styles.css` — the entire site. Keep it that way.
- `fonts/jetbrains-mono-latin.woff2` — self-hosted JetBrains Mono (latin subset,
  variable weight, ~31 KB). The only binary asset; no external font requests.
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
- Performance is credibility: static HTML, no framework, total page < 200 KB,
  no cookie banner, no analytics scripts that need one.
- No gradients, no glassmorphism, no mascots, never restyle provider logos.

## Out of Scope
- No build tooling, frameworks, or npm — plain HTML/CSS (JS only if trivial and inline).
- No blog, docs section, or multi-page structure — landing page only.
- The product app itself (and PLAN.md) live elsewhere; this repo never grows app code.
