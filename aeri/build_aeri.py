"""Build the AER: Insights submission sources from the working paper's sections.

Run from the repository root:  python aeri/build_aeri.py
Writes aeri/sections/*.tex (anonymised manuscript sections, in-paper Appendix A on the renewal models and the
Supplemental Appendix body). The working paper (main.tex, sections/) is not touched. Rerun after editing sections/.

Cross-references from the manuscript to the Supplemental Appendix, and back, are written as fixed numbers (the two are
compiled as separate PDFs); the asserts below check that every label is accounted for.
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "sections")
OUT = os.path.join(ROOT, "aeri", "sections")
os.makedirs(OUT, exist_ok=True)

# Supplemental Appendix numbering (order of appendix.tex)
SUPP = {
    "app:data": ("Section", "S1"),
    "app:results": ("Section", "S2"),
    "app:constraints": ("Section", "S3"),
    "app:models": ("Section", "S4"),
    "app:leverslearning": ("Section", "S5"),
    "tab:coverage": ("Table", "S1"),
    "fig:lags": ("Figure", "S1"),
    "tab:within": ("Table", "S2"),
    "tab:rich": ("Table", "S3"),
    "fig:country": ("Figure", "S2"),
    "fig:constraints-country": ("Figure", "S3"),
    "tab:fees": ("Table", "S4"),
    "tab:learning": ("Table", "S5"),
    "tab:patentvalues": ("Table", "S6"),
    "tab:levers-learning": ("Table", "S7"),
}
# Manuscript numbering referred to from the Supplemental Appendix
MAIN = {
    "tab:sample": "Table~1",
    "tab:survival": "Table~2",
    "tab:levers": "Table~3",
    "fig:constraints": "Figure~1",
    "fig:valuespooled": "Figure~2",
    "sec:values": "Section~5",
    "fn:specs": "footnote~3",
    "eq:did": "(1)",
}


def read(name):
    return io.open(os.path.join(SRC, name), encoding="utf-8").read().replace("\r\n", "\n")


def write(name, s):
    io.open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n").write(s)


def to_supp(s):
    """Manuscript side: 'Appendix Table~\\ref{tab:within}' -> 'Supplemental Appendix Table~S2'."""
    for key, (kind, num) in SUPP.items():
        if kind == "Section":
            if key == "app:models":
                continue  # the models are Appendix A of the manuscript; handled below
            s = re.sub(r"Appendix~\\ref\{" + re.escape(key) + r"\}", "Supplemental Appendix~" + num, s)
        else:
            s = re.sub(r"Appendix(\s+)" + kind + r"~\\ref\{" + re.escape(key) + r"\}",
                       lambda m: "Supplemental Appendix" + m.group(1) + kind + "~" + num, s)
    return s


# 1. Manuscript sections
for name in ["introduction", "data", "survival", "constraints", "values", "stake", "conclusion"]:
    s = to_supp(read(name + ".tex"))
    if name == "values":
        a = "Appendix~\\ref{app:models} gives the details."
        assert s.count(a) == 1
        s = s.replace(a, "Appendix~\\ref{app:models} sets out both models; Supplemental Appendix~S4 gives the fee "
                         "schedules and estimates.")
    left = [k for k in SUPP if "\\ref{" + k + "}" in s and k != "app:models"]
    assert not left, (name, left)
    assert "Appendix~\\ref" not in s.replace("Appendix~\\ref{app:models}", ""), name
    write(name + ".tex", s)

# 2. Split the working-paper appendix: model set-up -> in-paper Appendix A; the rest -> Supplemental Appendix
app = read("appendix.tex")
i = app.index("\\paragraph{Deterministic model.}")
j = app.index("\\paragraph{Fee discounts.}")
models = app[i:j].rstrip() + "\n"
a = "Table~\\ref{tab:learning} reports the\nestimates."
assert models.count(a) == 1
models = models.replace(a, "Supplemental Appendix\nTable~S5 reports the estimates.")
models = models.replace("\\paragraph{Patent-level values.} The learning model is re-estimated",
                        "\\paragraph{Patent-level values.} For the values of Section~\\ref{sec:values}, the learning "
                        "model is re-estimated")
assert "\\ref{tab:" not in models and "\\ref{fig:" not in models
write("appendix_models.tex",
      "\\section{Renewal models}\\label{app:models}\n\n"
      "Fee schedules, the fee discounts and the estimates are in Supplemental Appendix~S4.\n\n" + models)

supp = app[:i] + app[j:]
supp = supp.replace("\\section{Renewal models and patent values}\\label{app:models}\n",
                    "\\section{Renewal models and patent values}\\label{app:models}\n\n"
                    "The deterministic and learning models are set out in Appendix~A of the paper.\n")
for key, txt in MAIN.items():
    if key == "eq:did":
        supp = supp.replace("equation~\\eqref{eq:did}", "equation~" + txt + " of the paper")
    else:
        supp = re.sub(r"\\ref\{" + re.escape(key) + r"\}\}?", lambda m: "REF" + key, supp)
        word = txt.split("~")[0]
        supp = re.sub(word + r"~REF" + re.escape(key), txt, supp)
        assert "REF" + key not in supp, key
missing = set(re.findall(r"\\(?:eq)?ref\{([^}]*)\}", supp)) - set(SUPP)
assert not missing, missing
write("supplement_body.tex", supp)

# 3. Word count check (approximate; the AEA tool counts the word-count PDF)
def words(s):
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\\begin\{(table|figure)\}.*?\\end\{\1\}", " ", s, flags=re.S)
    s = re.sub(r"\\input\{tables/[^}]*\}", " ", s)
    s = re.sub(r"\\begin\{equation\}.*?\\end\{equation\}|\\\[.*?\\\]", " ", s, flags=re.S)
    s = re.sub(r"\\cite[pt]?(\[[^]]*\])*\{[^}]*\}", " Author (2000) ", s)
    s = re.sub(r"\\(label|ref|eqref)\{[^}]*\}", " 1 ", s)
    s = re.sub(r"\$[^$]*\$", " x ", s)
    s = re.sub(r"\\[a-zA-Z]+\*?", " ", s)
    s = re.sub(r"[{}~\\]", " ", s)
    return len([w for w in s.split() if re.search(r"[A-Za-z0-9]", w)])


n = sum(words(io.open(os.path.join(OUT, f + ".tex"), encoding="utf-8").read())
        for f in ["introduction", "data", "survival", "constraints", "values", "stake", "conclusion",
                  "appendix_models"])
print(f"counted words (text, footnotes, Appendix A): about {n:,}; limit with 5 exhibits: 6,000")
