# Self-Assembly Lab

Nextra documentation site for **self-assembly education** — molecular/DNA nanotech, swarm robotics, and programmable matter — aimed at young scientists and engineers.

**Repo:** https://github.com/caretak3r/self-assembly-lab  
**Live:** https://silent.engineer/self-assembly-lab/

## Honest framing

Engineered self-assembly applications are mostly **lab-scale / undeveloped**. Nature already self-assembles; engineers program interactions; landmark demos prove principles; products remain limited. Kinetics, errors, energy, and manufacturing still constrain useful devices. Manufacturing and supply-chain pages teach **starter paths** (kits, makerspaces, university labs, small CNC/3D print, electronics BOMs) — not mass-market programmable-matter factories.

## Stack

- [Nextra](https://nextra.site/) 4 + Docs theme
- Next.js 15 (App Router) + React 19
- TypeScript + MDX
- Static export (`output: 'export'`) suitable for GitHub Pages (`basePath` `/self-assembly-lab` in production)

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

Static files land in `out/`. In production / GitHub Actions, `basePath` is `/self-assembly-lab`.

## Deploy (GitHub Pages)

1. Enable Pages on the repo (GitHub Actions or deploy `out/` from `main`).
2. Project site base path `/self-assembly-lab` (also mirrored at https://silent.engineer/self-assembly-lab/).

## Content sources

Educational pages are adapted from the curated corpus (not invented):

- `papers.md` — bibliography
- `latest-finds.md` — recent reviews/preprints
- `experiments.md` — 10 safe labs
- `how-to-start.md` — 2–4 week path
- `media.md` — lectures & demos
- `summary.md` — IA & framing
- `beginners-manufacturing-notes.md` — verified videos & manufacturing research scratch

## Site map

| Route | Content |
|-------|---------|
| `/` | Frontier framing + homepage sources + media strip |
| `/beginners` | Beginner track index |
| `/beginners/chapter-1` | What self-assembly looks like |
| `/beginners/chapter-2` | Local rules, energy, order |
| `/beginners/chapter-3` | DNA origami intuition (no wet lab) |
| `/beginners/chapter-4` | Robot swarms & modular robots |
| `/beginners/chapter-5` | First safe experiments |
| `/concepts` | Vocabulary / foundations |
| `/dna` | Molecular / DNA track |
| `/robots` | Swarm + modular / programmable matter |
| `/experiments` | All 10 starter experiments |
| `/manufacturing` | Starter hardware paths (print, PCB, MCU, DNA-as-service) |
| `/supply-chain` | BOM thinking, distributors, cores, hard-to-buy items |
| `/learn` | 2–4 week learning path |
| `/papers` | Full bibliography + latest finds |
| `/media` | Lectures, demos, open PDFs |
| `/latest` | Digest index |
| `/latest/2026-09-15` | Example daily digest |

## Media

YouTube embeds use the `YouTube` MDX component (`components/YouTube.tsx`). Open-license images live in `public/images/` with attribution in `public/images/CREDITS.md`.

## Contributing digests

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

Educational content curated for public teaching use. Individual papers remain under their publishers’ copyrights — link, don’t republish paywalled PDFs. Images retain their upstream licenses (see CREDITS).
