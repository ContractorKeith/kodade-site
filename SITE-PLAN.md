# kodade.com — Site Plan: the 4a overhaul

Implementation plan for rebuilding the landing page around the **pixelation +
dithering** direction (`Ködade Brand.dc.html` § 4a), pushed further than the
mock. Companion to DESIGN.md (tokens, voice) — this file is the build spec.
Named SITE-PLAN.md because PLAN.md belongs to the product repo.

Decisions locked 2026-07-11:

1. **Full commitment** — the whole page speaks 1-bit. Pixel-rendered headline
   treatment, denser dither fields, pixel seams between sections. Not
   hero-only decoration.
2. **All-dark** — the entire page lives on `--ink-950`. No paper sections.
   (DESIGN.md § 6 amended to match.)
3. **Subtle CSS motion** — blinking block cursor, accent-dot pulse, slow
   dither shimmer. All behind `prefers-reduced-motion`.
4. **Public tagline** — the headline is "your agents. one window".

---

## 1. Design language — the dither vocabulary

Everything below is pure CSS (gradients + masks + grids). Zero image bytes.

| Element | Recipe | Source |
|---|---|---|
| **Bayer dither field** | `conic-gradient` checker (2×2) at 3–6 px cell size, amber `rgba(230,160,60,α)` or paper `rgba(247,246,243,α)`, shaped by a `radial-gradient` mask | 4a mock, lines 40–45 |
| **Halftone ramp** | stacked 8 px rows of `radial-gradient` dots, shrinking radius + alpha per row; used as section seams | 4a mock, lines 172–178 |
| **Pixel stair ornament** | CSS grid of 13–14 px cells, scattered diagonal fills in amber/paper at varying opacity | 4a mock, lines 47–70 |
| **Hard geometry** | `border-radius: 0` everywhere; window mock shadow is `8px 8px 0 rgba(0,0,0,.55)` — offset, never blurred | 4a mock |
| **Pixel umlaut wordmark** | JetBrains Mono `kodade` with the ö built from positioned 3 px squares (left amber, right paper) | 4a mock, lines 79–88 |

**Pushing further than the mock (the "full commitment" additions):**

- **Pixel-rendered headline accent** — the accent word in the H1 is drawn as
  actual pixel-grid letterforms or dither-masked type, not
  just recolored. Constraint: NO third font family — achieve it with CSS
  grids, inline SVG, `clip-path: polygon()` stair-stepping, or dither-pattern
  `background-clip: text`. Implementer prototypes, we pick.
- **Denser fields** — hero dither raised above mock opacity; add a coarse
  8 px field layer so the texture reads at arm's length.
- **Dithered section seams everywhere** — every section boundary is a
  halftone ramp or pixel-stair row. No plain 1 px rules between sections
  (inside component grids 1 px hairlines stay).
- **Pixel-clipped edges** — CTA buttons and the window mock get subtle
  stair-stepped corners via `clip-path` instead of square-but-smooth.
- **Dither on hover** — nav links and CTA hover states use dither texture,
  not smooth color transitions.

## 2. Page structure (top → bottom, all on ink-950)

1. **Nav** — pixel-umlaut wordmark left; docs / GitHub / 𝕏 / amber CTA
   right. The public social profile is `@kodadeapp`.
2. **Hero** — dither field halo behind centered headline; pixel stairs top-right
   and mid-left; H1 "your agents. one window"; lede; amber macOS download CTA.
3. **Product window mock** — the existing 4-pane mock restyled: squared,
   hard offset shadow, double dither glow behind it, blinking cursor,
   pulsing session dot.
4. **Halftone ramp seam.**
5. **Proof points** — 3-up grid on ink-950, 1 px `#24262A` gutters, mono
   headings (your real shell / any agent / Apache 2.0).
6. **Agent strip** — supported CLI names as plain
   text rows (never restyled logos).
7. **Pixel-stair seam.**
8. **Download** — repeated macOS release CTA, Windows first-week-of-August 2026
   status, and Linux planned status.
9. **Footer** — minimal: wordmark dots, copyright, nothing else.

## 3. Motion spec (CSS only)

| Animation | Where | Behavior |
|---|---|---|
| Block cursor blink | terminal mock | 1 s step blink, amber block |
| Session dot pulse | sidebar "claude · main" row | slow opacity pulse, the house status indicator |
| Dither shimmer | hero field only | very slow `background-position` drift on ONE layer; imperceptible-until-noticed |

All wrapped in `@media (prefers-reduced-motion: no-preference)`. Nothing
moves for reduced-motion users; the page is fully legible static.

## 4. Hard constraints

- Static HTML + CSS; JS only if trivial and inline. No build step, no deps.
- Total page < 200 KB including the JetBrains Mono subset.
- Textures are CSS-generated — no PNG/GIF dither assets.
- `mask-image` needs `-webkit-` prefixes; page must degrade gracefully
  (plain dark hero) where masks are unsupported.
- Contrast: body text stays ≥ 4.5:1 on ink-950; dither fields never sit
  behind body copy at legibility-hurting opacity.
- Mobile: dither fields scale down, stair ornaments hide below ~700 px,
  window mock simplifies to 2 panes.

## 5. Tickets

| # | Ticket | Depends on |
|---|---|---|
| 1 | Dither/pixel CSS foundation (utility classes + tokens) | — |
| 2 | Hero rebuild: nav, pixel wordmark, pixel headline, dither fields | 1 |
| 3 | Product window mock restyle: squared, glow, hard shadow | 1 |
| 4 | Below-the-fold: proof, agents, download, footer, dithered seams | 1 |
| 5 | Motion pass: cursor, pulse, shimmer + reduced-motion | 2, 3 |
| 6 | Copywriting: headline line two, lede, section copy | — (non-blocking) |
| 7 | QA: budget, responsive, a11y, mask fallbacks, meta/OG | 2, 3, 4, 5 |

## 6. Open items

- Headline second line ("every agent." is out). Candidates to hash out in #6.
- Whether the pixel-headline treatment applies to H2s or H1 only — decide
  after seeing the #2 prototype.
