# Self-Assembly Lab

Nextra documentation site for **self-assembly education** — molecular/DNA nanotech, swarm robotics, and programmable matter — aimed at young scientists and engineers.

**Repo:** https://github.com/caretak3r/self-assembly-lab

## Honest framing

Engineered self-assembly applications are mostly **lab-scale / undeveloped**. Nature already self-assembles; engineers program interactions; landmark demos prove principles; products remain limited. Kinetics, errors, energy, and manufacturing still constrain useful devices.

## Stack

- [Nextra](https://nextra.site/) 4 + Docs theme
- Next.js 15 (App Router) + React 19
- TypeScript + MDX
- Static export (`output: 'export'`) suitable for GitHub Pages

## Local development

```bash
npm install
npm run dev
```

Open http://localhost:3000

## Production build

```bash
npm install
npm run build
```

Static files land in `out/`. In production / GitHub Actions, `basePath` is `/self-assembly-lab` for GitHub Pages project sites.

## Deploy (GitHub Pages)

1. Enable Pages on the repo (GitHub Actions or deploy `out/` from `main`).
2. Site will be at `https://caretak3r.github.io/self-assembly-lab/` when Pages is configured with the `/self-assembly-lab` base path.

Example Actions workflow idea: build with `NODE_ENV=production`, upload `out/` as Pages artifact.

## Content sources

Educational pages are adapted from the curated corpus (not invented):

- `papers.md` — bibliography
- `latest-finds.md` — recent reviews/preprints
- `experiments.md` — 10 safe labs
- `how-to-start.md` — 2–4 week path
- `media.md` — lectures & demos
- `summary.md` — IA & framing

## Site map

| Route | Content |
|-------|---------|
| `/` | Frontier framing + 5 homepage sources + media strip |
| `/concepts` | Vocabulary / foundations |
| `/dna` | Molecular / DNA track |
| `/robots` | Swarm + modular / programmable matter |
| `/experiments` | All 10 starter experiments |
| `/learn` | 2–4 week learning path |
| `/papers` | Full bibliography + latest finds |
| `/media` | Lectures, demos, open PDFs |
| `/latest` | Digest index |
| `/latest/2026-09-15` | Example daily digest |

## Contributing digests

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

Educational content curated for public teaching use. Individual papers remain under their publishers’ copyrights — link, don’t republish paywalled PDFs.
