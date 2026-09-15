# Contributing

Thanks for helping grow the Self-Assembly Lab docs. This site stays honest about the frontier and only cites **real** papers.

## Adding a daily digest under `/latest`

1. **Create** `content/latest/YYYY-MM-DD.mdx` (use the calendar date in America/New_York).
2. **Register** the page in `content/latest/_meta.js`:
   ```js
   export default {
     index: 'About digests',
     '2026-09-15': '2026-09-15 digest',
     'YYYY-MM-DD': 'YYYY-MM-DD digest'  // add here
   }
   ```
3. **Update** the table on `content/latest/index.mdx` with a link to the new digest.
4. **Structure** (copy from `2026-09-15.mdx`):
   - Title + date + timezone note
   - Frontier/honesty callout
   - Numbered finds with: authors (when known), link (DOI or arXiv), why newsworthy, beginner hook, caveats/open problems
5. **Cite only real sources.** Verify DOI redirects or arXiv abs pages. Never invent papers, DOIs, or titles.
6. **Prefer** open PDFs / arXiv / HTML for student access; note paywalls when linking publisher pages.
7. **Tone:** lab-scale progress, not product claims. Flag wet-lab impracticality for classroom settings.

## Pull request checklist

- [ ] `npm run build` exits 0
- [ ] New digest registered in `_meta.js` and index table
- [ ] All links resolvable (spot-check DOIs)
- [ ] No invented citations
- [ ] Frontier honesty callout present

## Content edits elsewhere

- Keep vocabulary consistent with `/concepts`.
- Experiments must stay **safe** (no hazardous chemistry, no unsupervised DNA wet labs for young students).
- Prefer adapting corpus language over marketing hype.

## Questions

Open an issue on https://github.com/caretak3r/self-assembly-lab.
