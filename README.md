# The Invention, Not the Inventor: Patent Value in Emerging Markets

Discussion-paper draft: main text under 10 pages, at most 20 pages with references and appendices. LaTeX source,
compiled with pdfLaTeX + BibTeX (Overleaf default).

- `main.tex`: preamble, title page, abstract; includes the sections.
- `sections/`: one file per section and the appendix (A data and office choice, B renewal models, C additional
  results).
- `figures/`: PNG figures, produced by `code/25_paper_figures.py` in the companion project `em-patent-value`.
- `references.bib`: bibliography (entries still to be checked against published versions).

Numbers in the tables come from the outputs of `em-patent-value` (`output/*.csv`, `notes/01_first_results.md`);
each table names its source in a comment. `\tbd{}` (red) marks numbers still to be filled from running analyses.

## Overleaf

New Project > Import from GitHub > `em-patent-renewal-paper`. Compiler: pdfLaTeX. Main document: `main.tex`.

## Open items

- Fill the `\tbd{}` placeholders (step 24 of `em-patent-value`: richer quality controls, matched comparison, same
  invention, credit shocks, sale premium on the 5 + 5 office set; figure 2).
- Value models for Russia, Taiwan, the Czech Republic and France once their fee schedules are compiled.
- Literature review; check the bibliography.
- Acknowledgements.
