# AER: Insights submission

Sources for the AER: Insights version of the paper. Edit the `aeri_*.tex` files and `aeri/sections/` directly and
compile. They are a separate copy of the working paper (`main.tex`, `sections/`), so edits to either one do not carry
over to the other. The manuscript cites the Supplemental Appendix by fixed numbers (Table S2, Figure S3, ...); if you
add, drop or reorder exhibits in `aeri/sections/supplement_body.tex`, update those citations, and update the cross-
references to the paper (Table 1, footnote 3, equation (1), ...) inside the supplement.

Compile each file below as the main document (in Overleaf: Menu > Main document) and download the PDF.

| Upload | Source | Notes |
|---|---|---|
| Manuscript | `aeri_manuscript.tex` | Anonymised; title and abstract at the top of page 1; in-paper Appendix A (renewal models) on a new page before the references |
| Title page | `aeri_titlepage.tex` | Label as "title page"; author, affiliation, contact, acknowledgement footnote; fill in `[Acknowledgements.]` |
| Word-count PDF | `aeri_wordcount.tex` | Text, footnotes and Appendix A only; upload to the AEA word-count tool and enter the count it returns |
| Supplemental Appendix | `aeri_supplement.tex` | Anonymised; numbered S1, S2, ...; posted as additional material |
| Disclosure statement | `aeri_disclosure.tex` | Titled "Disclosure Statement"; confirm or edit the red bracketed items |

## Checks against the guidelines (aeaweb.org/journals/aeri/submissions/guidelines)

- **Exhibits:** five in the manuscript (Tables 1--3, Figures 1--2), the maximum; each fits on one page.
- **Words:** limit 7,000 - 5 x 200 = 6,000, counting text, footnotes and in-paper appendices (not the title, abstract,
  exhibits, references or Supplemental Appendix). The word-count PDF has about 5,600 words, page numbers included.
- **Abstract:** 99 words (limit 100).
- **Anonymity:** no author name, affiliation, contact or website in the manuscript or Supplemental Appendix; prior
  work cited by author name.
- **Self-contained:** data sources, variable definitions and the design are in the text; the renewal models are in
  Appendix A; the Supplemental Appendix holds additional results only.
- **AI use:** describe it in the submission form (the title-page footnote also states it).
- **Cover letter:** not required; use the form field only for coeditor conflicts or data-access limits (PATSTAT is
  licensed data: say so if asked about data availability).
- **Fee:** $200 (AEA member) or $300 (non-member), high-income country rate.
- **At acceptance:** replication package under the AEA Data and Code Availability Policy (code in
  `em-patent-value/code`; PATSTAT is licensed, so provide access instructions instead of the raw data).
