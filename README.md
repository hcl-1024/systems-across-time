# Systems Across Time

The public portfolio site for research, service, leadership, and creative projects. The site is deployed with GitHub Pages at:

<https://hcl-1024.github.io/systems-across-time/>

## Site structure

- `index.html` — home
- `projects/` — project directory and eight individual project pages
- `research/` — Cicero credit-networks overview, methods, findings, and paper status
- `about.html` — purpose and repository organization
- `assets/` — shared visual assets

The research data and reproducible calculations are maintained separately in [cicero-credit-networks](https://github.com/hcl-1024/cicero-credit-networks). The paper page is intentionally a placeholder until the manuscript is ready for public release.

## Local preview

Run a static server from the repository root, then open the local address it prints. For example:

```sh
python3 -m http.server 8000
```

## Checks and deployment

Run the internal-link check before committing:

```sh
python3 scripts/check_links.py
```

Pushes to `main` are validated and deployed automatically through GitHub Actions.
