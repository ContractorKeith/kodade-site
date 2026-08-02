# ködade — DESIGN.md

Brand + product design reference. Companion to PLAN.md. Logo is under exploration
(see `Ködade Brand.dc.html`, options 1a–1d); tokens below are settled unless marked OPEN.

---

## 1. Brand identity

### Name
- **ködade** — "code-ade": simple code + Agentic Development Environment.
- Always lowercase in the wordmark and UI (`ködade`), capitalized only when
  grammar forces it in prose ("Ködade is…").
- Pronounced *code-ah-deh*. The ö is intentional and always written with the
  umlaut in brand contexts. ASCII fallback (package names, domains, CLI):
  `kodade` — never "koedade".

### The ö motif
The umlaut is the brand mark's DNA: **two dots above the o**. Read it as
- two agents attending to your code,
- a cursor's pixel pair,
- the only decoration a terminal needs.

Rule: the dots may be recolored, animated (blink, orbit), or extracted as a
standalone glyph — the o beneath stays quiet. Nothing else in the identity gets
ornamentation.

### Logo — DECIDED: Double dot (exploration 1d → 2a)
- **Mark**: the umlaut alone — two rounded squares, left dot in accent, right dot
  in ink/paper depending on background.
- **Wordmark**: `ködade` in JetBrains Mono Bold, lowercase, -0.02em tracking;
  the ö's dots are the mark's rounded squares, sitting tight above the o's shoulder.
- Mark survives at 16 px (menu bar/favicon), 512 px (DMG icon), 1-color, and on
  any theme background.

### Personality
Sleek & minimal · precise & engineered · premium pro-tool · bring-your-own-model.
If a choice feels clever but heavy, it's wrong. If it feels like a good terminal
emulator made by people with taste, it's right.

---

## 2. Color

The **brand is theme-neutral**: it never borrows from Catppuccin/Tokyo Night/One Dark.
Brand surfaces (site, docs, icon, marketing) use the ink scale + one accent.

### Neutral ink scale (brand)
| Token | Value | Use |
|---|---|---|
| `--ink-950` | `#0F1012` | brand dark bg, icon field |
| `--ink-900` | `#17181B` | raised dark surface |
| `--ink-600` | `#5A5D63` | secondary text on light |
| `--ink-300` | `#C9CBCE` | hairlines, secondary on dark |
| `--paper` | `#F7F6F3` | brand light bg (warm off-white) |
| `--paper-raised` | `#FFFFFF` | cards on light |

### Accent — DECIDED: amber
- `--accent`: `oklch(0.78 0.15 75)` on dark surfaces
- `--accent-on-light`: `oklch(0.66 0.14 75)` (darkened for contrast on `--paper`)

Accent is for: the umlaut dots, primary CTA, active/live indicators. Never for
body text, never as a background wash.

### Product UI color
In-app chrome takes **all** color from the active theme's tokens (PLAN.md § Themes):
one token file maps to UI chrome, xterm palette, and CodeMirror highlight style.
The brand accent appears in-app only where the theme has no opinion
(About window, onboarding, update badge).

---

## 3. Typography

| Role | Face | Notes |
|---|---|---|
| Wordmark / display | JetBrains Mono (Bold for wordmark) | lowercase, -0.02em tracking |
| UI chrome | system stack (`-apple-system, "SF Pro", "Segoe UI", sans-serif`) | native-feeling, zero download |
| Terminal & editor | user/theme-controlled; default `JetBrains Mono` | respect user's font setting |
| Docs & site body | same as display family's text cut, or system stack | max 2 families anywhere |

Scale (site/docs): 15 px body, 1.55 line-height; headings 1.25 ratio; UI chrome
12–13 px labels. Never below 11 px in-app.

---

## 4. Product UI principles

1. **The terminal is the hero.** Chrome recedes: hairline borders, no shadows
   inside the work area, panes separated by 1 px lines in the theme's border token.
2. **Native-feeling, not native-imitating.** Match macOS spacing rhythm and
   traffic-light placement; don't fake Cocoa widgets.
3. **Density is a feature.** 4 px base grid; sidebar rows 28 px; toolbar 38 px.
   Generous space belongs on the landing page, not between panes.
4. **Progressive disclosure.** Defaults work with zero setup (open project →
   terminal ready → "Start Claude"); every power feature is discoverable but
   never in the way. One interface, no modes.
5. **Theme-complete or don't ship it.** Any new surface must render from theme
   tokens only. No hardcoded colors in components — ever.
6. **State is visible, quiet.** Running agent = accent-dot pulse in the session
   row, not a banner. Dirty file = dot on the tab. The umlaut-dot is the house
   status indicator.
7. **Speed is brand.** Sub-second start, instant pane drag, no skeleton screens.
   If something needs a spinner, make it faster instead.

---

## 5. Voice & copy

- **Plain, technical, confident.** "Runs your shell. Your prompt, your PATH."
  — not "Supercharge your workflow ✨".
- Verbs first, lowercase UI labels where macOS allows ("open project", "new session").
- Never overpromise agents: ködade *orchestrates* CLIs; the CLIs do the work.
- No emoji, no exclamation marks, no "blazingly".
- Public tagline: **"your agents. one window"**. It replaces the earlier
  "two döts" headline.

---

## 6. Landing page (kodade.com)

- Single page (PLAN.md: site is a landing page only). **All-dark on `--ink-950`**
  — DECIDED 2026-07-11, supersedes the earlier dark-hero/paper-sections split.
- Visual direction — DECIDED: **pixelation + dithering** (`Ködade Brand.dc.html`
  § 4a, pushed further). Bayer dither fields, halftone ramps as section seams,
  pixel stair ornaments, squared corners, hard offset shadows, pixel-rendered
  headline accent. Build spec lives in SITE-PLAN.md.
- Hero = the product: a real screenshot/screencast of the 4-pane window with a
  live prompt, not abstract 3D blobs.
- Structure: hero + one-line pitch → supported agent CLIs → 3 proof points
  (your real shell / any agent / Apache 2.0) → platform availability.
- CTA: "Download for macOS" in accent, linked to the public GitHub release. One
  primary CTA, repeated at bottom; Windows and Linux remain status labels until
  their releases exist.
- Performance is credibility: static HTML, no framework, < 200 KB, no cookie banner.

---

## 7. Don'ts

- No *smooth* gradients on brand surfaces; no glassmorphism. Dither fields,
  halftone ramps, and pixel patterns (CSS-generated, hard-edged) are the one
  sanctioned texture — they are the brand's texture language, not decoration.
- Never restyle or recolor another provider's logo.
- Never use theme colors in marketing, or brand accent inside themed UI.
- No mascots. The dots are the personality.
