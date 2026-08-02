# kodade.com/docs — documentation plan

Implementation plan for issue #8. Product behavior is sourced from the current
`Kodade/kodade` implementation and tests, not from stale milestone text
in that repository's README or PLAN.md.

## Outcome

Publish a public, task-oriented MkDocs site at `https://kodade.com/docs/` while
keeping the existing landing page at `https://kodade.com/` visually unchanged.
The two surfaces share one brand system and one Cloudflare Pages deployment.

## Audience and writing rule

The first path is for someone opening an ADE for the first time; deeper reference
stays available in the same navigation for experienced engineers. There are no
separate beginner and expert modes. Copy stays plain, technical, and honest about
availability and security boundaries.

## Information architecture

1. **Start here** — what ködade is, requirements, installation status, first project.
2. **Core workflow** — projects and layout, terminal sessions, agent CLIs.
3. **Workspace tools** — files, editor, previews, GitHub, browser.
4. **Agent workspace** — KödHarness, KödMem, and KödMCP.
5. **Personalize** — Settings, themes, and keyboard shortcuts.
6. **Trust and support** — open-source licensing, local data,
   privacy/security, troubleshooting, and platform status.

## Product truth to preserve

- macOS 13 or newer on Apple silicon is available from the public GitHub
  release. Other Mac architectures must not be implied.
- Adding a project starts a real login-shell terminal in that folder. Users run
  their installed and authenticated agent CLIs manually.
- Projects, layouts, theme, sidebar mode, and tab metadata persist locally.
  Live terminal sessions and unsaved buffers do not survive restart.
- GitHub visibility is read-only and uses the user's authenticated `gh` CLI.
- The embedded browser is currently macOS-only, HTTP(S)-only, and isolated from
  the app's IPC bridge. Downloads and popups are blocked.
- File-manager mutations and document previews are confined to the project, but
  shells and agents keep the user's normal operating-system permissions.
- Windows is targeted for the first week of August 2026. Do not claim it is
  available or has feature parity until its public artifact exists.
- Linux is planned without a committed release date.
- The public release is Apache-2.0 and has no Free/Pro product split.
- KödSSH, KödWhisper, KödLocal, and KödPR are outside the public release and
  remain development lanes. KödWeb is outside the release and is no longer in
  development.

## Build and deployment architecture

- Pin MkDocs 1.6.1 and build a small custom theme instead of adding a third-party
  theme runtime.
- Generate one clean `dist/` artifact. Whitelist the existing public landing
  assets into its root and build MkDocs into `dist/docs/`.
- Configure the existing Git-connected Cloudflare Pages project to publish
  `dist`. No DNS change or second Pages project is required.
- Add explicit 404 pages and `/docs` to `/docs/` routing so missing paths no
  longer fall back to the landing page.
- Treat warnings as errors in local builds and GitHub CI. Assert that design
  notes, repo instructions, screenshots, and local caches never enter `dist/`.

## Design direction

Reuse the shipped ink/amber tokens, self-hosted JetBrains Mono, double-dot mark,
square geometry, and restrained dither texture. Keep article surfaces quiet:
dither belongs in the header and seams, never behind body copy. Desktop uses a
section nav, readable article column, and on-page table of contents; smaller
screens collapse navigation accessibly and remove decorative texture.

## Delivery graph

- #9 — build and curated deployment artifact
- #10 — custom theme, navigation, and landing integration (after #9)
- #11 — overview, installation, projects, and terminal sessions
- #12 — files, editor, previews, GitHub, browser, and shortcuts
- #13 — local data, privacy/security, troubleshooting, and platform status
- #14 — CI, preview review, Cloudflare configuration, and production proof

Independent content tickets can run in parallel. Their branches merge into this
feature branch through reviewed pull requests. The feature branch then receives
a full standards/spec review before its final pull request to `main`.

## Release proof

- `/` serves the unchanged landing page.
- `/docs` redirects to `/docs/`; `/docs/` and nested routes serve the docs.
- Unknown root and docs routes return 404.
- Internal Markdown, screenshots, and repo artifacts return 404 publicly.
- CI passes; Cloudflare preview is reviewed before merge; the production
  deployment source SHA matches the final merge.
