JAMMING PHYSICS — English-only site (restructured)
==================================================

WHAT CHANGED
- Site is now English-only. The entire /ko/ tree was removed.
- Homepage (/) restructured into three parts:
    1) Volume-Particle (VP) Theory  (the physics, kept and anchored at #vp-theory)
    2) Deterministic Two-Layer Interpretation of DNA (v3)  (new flagship, #dna)
    3) Other whitepapers  (#whitepapers) + DOI list (#dois)
- The DNA v3 paper is hosted at /en/whitepapers/dna-interpretation/ (self-contained HTML,
  figures embedded, math as MathML, with a top bar linking back to the site).
- Removed the "Deterministic Bio-Physical Applications" whitepaper from the site
  (/en/whitepapers/bio-physical-apps/ deleted; cards/links removed). Its Zenodo record
  (10.5281/zenodo.17979016) is NOT deleted — it remains citable on Zenodo, just not featured here.
- All language toggles / "한국어" links / hreflang="ko" removed across pages.
- papers.js rewritten English-only (DNA v3 added after the VP core; bio removed).
- sitemap.xml regenerated (English URLs only). robots.txt unchanged.

DEPLOY (GitHub Pages)
1) Replace your repository contents with this folder's contents (keep CNAME — included).
2) Commit & push. Pages will serve / from index.html.
3) Verify:
   - https://jamming-physics.org/                              (home, 3 parts)
   - https://jamming-physics.org/en/whitepapers/dna-interpretation/   (DNA v3 paper)
   - https://jamming-physics.org/en/whitepapers/               (hub, no Korean, no bio)
   - https://jamming-physics.org/sitemap.xml

NOTES
- The DNA v3 paper renders math via MathML (native in Firefox/Safari/Chrome 109+); fully offline.
- The big physics whitepaper (/en/whitepaper.html) loads MathJax from jsDelivr CDN (unchanged).
- Author: Young Jae Lee · ORCID 0009-0002-7535-8245.
