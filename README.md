# kodade-site

Landing page and public documentation for ködade, the Agentic Development
Environment. The site deploys as one static Cloudflare Pages artifact:

- `https://kodade.com/` — hand-authored landing page
- `https://kodade.com/docs/` — MkDocs documentation

## Local preview

Python 3.13.3 and MkDocs 1.6.1 are pinned to match the Cloudflare Pages v3 build
environment.

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
./scripts/build.sh
python3 -m http.server --directory dist 8000
```

Open `http://localhost:8000/` for the landing page and
`http://localhost:8000/docs/` for documentation. Cloudflare Pages runs
`./scripts/build.sh` and publishes `dist`.

The build starts from an empty `dist/`, copies an explicit allowlist of landing
and Cloudflare control files, then runs MkDocs in strict mode. Generated output
is ignored by Git and must not be committed.

## Project notes

- Brand and product direction lives in `DESIGN.md`.
- Documentation scope and product-truth rules live in `DOCS-PLAN.md`.
- The design exploration source is kept in `Ködade Brand.dc.html`.
- Keep the landing page static and lightweight. Documentation styling should
  reuse the settled brand system without coupling the landing page to MkDocs.
