Jamming-Physics.org site package (Unified Whitepapers Hub)

What this package contains
- Unified home pages: /index.html, /en/index.html, /ko/index.html
- Unified whitepapers hub: /en/whitepapers/ , /ko/whitepapers/
- Full HTML builds (with MathJax + TOC):
  - DNA/mm39 v1.2 (EN/KO)
  - Deterministic Bio-Physical Applications v1.2 (EN/KO)
- Stub pages (DOI links only; HTML body not included here):
  - Fluid Dynamics from VP (DOI: 10.5281/zenodo.17972570)
  - VP Cosmology & Lattice Optics (DOI: 10.5281/zenodo.18012058)
- New site assets:
  - /assets/whitepapers.css
  - /assets/whitepapers.js
  - /assets/papers.js

Important notes
1) Applications whitepaper appendices are referenced via \input{...} in the LaTeX sources,
   but the appendix .tex files were not provided in this build.
   The HTML includes explicit [MISSING APPENDIX] placeholders where those inputs were expected.
   To include them, add these files next to the main tex and rebuild:
   EN: appendix_BIO_EM_DYNAMICS_EN.tex, appendix_OMEGALEARNSIM_IR_PAM_EN.tex, appendix_DNA_DICTIONARY_EN.tex
   KO: appendix_DNA_FULL.tex, appendix_BIO_EM_DYNAMICS.tex, appendix_OMEGALEARNSIM_IR_PAM.tex, appendix_DNA_DICTIONARY.tex

2) Personal contact email was removed from generated HTML pages.

How to deploy (GitHub Pages repo)
- Upload/merge the folders:
  assets/
  en/
  ko/
  index.html
  robots.txt
  sitemap.xml

No other repo files are required for this addon, but keep your existing CNAME and workflow files intact.
