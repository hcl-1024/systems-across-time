# Systems Across Time

The public portfolio site for research, service, leadership, and creative projects. The site is deployed with GitHub Pages at:

<https://hcl-1024.github.io/systems-across-time/>

## Site structure

- `index.html` — home
- `projects/` — project directory and eight individual project pages
- `research/` — Cicero credit-networks overview, methods, findings, and working paper
- `about.html` — purpose and repository organization
- `assets/` — shared visual assets

The research data, reproducible calculations, and public version 1.0 working paper are maintained in [cicero-credit-networks](https://github.com/hcl-1024/cicero-credit-networks). The website provides a stable public landing page for the paper and links to the versioned PDF on GitHub.

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
