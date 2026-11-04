# Simulated referee report (AER: Insights)

Produced on 2026-11-04 by a Claude Code agent asked to act as an AER: Insights referee on the aeri_* manuscript and
supplement as of that date (commit 7ef3b34). Not a real referee report. Line numbers refer to that version.

---

## 1. Summary

The paper asks whether emerging-market (EM) patents look less valuable because the inventions are worse or because
their owners cannot use them. Using PATSTAT/INPADOC lapse records for ~3 million granted patents filed 2000–2005 at five
EM offices (China, Korea, Russia, Taiwan, Czech Republic) and five advanced-economy (AE) offices (US, Japan, Germany,
UK, France), it compares domestic with foreign owners within each office and asks whether the domestic shortfall in
survival eight years after grant is larger in EM offices. The raw extra shortfall (−10.1 pp) becomes +4.1 pp
conditional on log citations, field and owner group, with mid-sized and large EM firms 8–9 pp "ahead" and small firms
~3 pp ahead. The author concludes the shortfall reflects what is patented. Three constraint tests (home vs. foreign
patents of the same invention, credit-shock years, survival after a sale; plus a fee-change test in the supplement) are
read as showing no binding finance constraints but some owner capacity "at the margin": patents sold by small firms and
Chinese universities survive much longer after sale. Renewal models (Schankerman–Pakes deterministic; Pakes learning)
yield patent-level values, used to price three "policy levers" for China and Korea: fee relief (~$1m per cohort),
markets for technology (up to $1.1bn), improving university patenting ($170–310m).

## 2. Overall assessment

The question is important—EM economies, China above all, now dominate world patenting, and whether their patents are
low-value because of the technology or the owners has real policy content. The assembly of lapse records and fee
schedules for ten offices over 25 years is a genuine data contribution, and the within-office domestic–foreign
comparison is a sensible first step.

However, I do not think the paper currently meets the AER: Insights bar, for three reasons.

(a) **The headline result is fragile and potentially mechanical.** The sign of the key coefficient is produced entirely
by conditioning on citations—a variable whose measurement differs sharply for domestic vs. foreign patents in EM
offices—and by a China-vs-US comparison: excluding China and the US the pooled δ is −1.0, small firms −4.4, and with
richer controls small firms are −0.4 (or −1.7 with family size). Russia and Taiwan go the other way. Several
first-order threats (grant-lag timing, unequal fees within an office, Chinese subsidy/tax incentives to keep patents
alive) are unaddressed and could each generate a positive δ.

(b) **The constraint tests do not discriminate between hypotheses.** Each test outcome is as consistent with
"constrained owners" as with "no constraint," and the sale result that drives the policy conclusion is selection by
construction.

(c) **It is not one point.** The introduction lists four points plus policy counterfactuals in ~6,000 words. The
message ends up "for firms it's the invention, except at the margin, and except for universities, where it's the
inventor." The renewal-value section, by the author's own admission (values.tex l.67–69), "restate[s] the survival
results in money rather than adding an independent test," and the policy table compares a lever that is second-order
by construction (fee relief on marginal patents) with an assumed across-the-board productivity gain. An Insights paper
needs one clear, well-identified fact; the candidate fact here (equal survival at equal observable quality) is the
least robust piece.

## 3. Major concerns

**1. Grant-lag timing mechanically favours domestic owners in EM offices.** Survival is measured eight years after
grant (data.tex l.100–103). Figure S1 shows foreign owners' median grant lags are 2–4 years longer than domestic owners'
in China, Korea, Russia and the Czech Republic, vs. 0–1 year in AE offices. At "eight years after grant," foreign patents
in these offices are therefore 2–4 years older from filing. In offices with fees by year from filing (China, Germany, UK,
Russia), they face higher fees, older technology and shorter remaining term—all of which raise foreign lapses, exactly
where δ is estimated to be positive. The author's justification for grant-based timing (footnote 4) does not address
this. Table S3 col. 2 adds a grant-lag quadratic and already cuts the small-firm estimate from 2.8 to −0.4. I would
want to see: (i) δ at a fixed age from filing (e.g., 10 and 12 years) conditional on grant-lag bins interacted with
office and domestic status; (ii) a discrete-time hazard by age-from-filing with office×fee-year effects; (iii) domestic
and foreign survival curves by office group. A figure of that kind could anchor the paper.

**2. "Same office, same fees" does not hold.** The design assumes domestic and foreign owners in an office face the same
fees, law and enforcement (data.tex l.23, l.92–93). That fails in two of the five EM offices: Russian foreign owners
paid a separate non-resident schedule until 2012 (supplement l.249–251; the explanatory paragraph is commented out at
values.tex l.49–53), and Chinese and Korean fee discounts go only to eligible domestic owners (supplement l.256–260).
The survival regressions (Table 2, S2–S4) ignore these, which bias δ in the direction found. Please model the fee each
patent actually faces in the survival regressions, or restrict to periods/ages when fees are identical, and report
China without the discount-eligible fee-years.

**3. Chinese incentives to keep patents alive regardless of private value.** From 2008 China's High and New Technology
Enterprise (HNTE) programme reduced corporate income tax from 25% to 15% for firms owning qualifying "core" IP; local
governments subsidised patent maintenance; patent counts entered firm, university and official evaluations. Individuals
are excluded for this reason (data.tex l.20–21), but the firm-level schemes are not discussed. These break the
revealed-preference premise of renewal analysis (survival measures private value including the tax/subsidy benefit),
and could produce both a positive δ for Chinese firms and the large post-sale survival (firms buy patents to qualify for
HNTE). The paper should engage with this literature (e.g., Chen, Liu, Suárez Serrato and Xu, AER 2021; Hu, Zhang and
Zhao, JDE 2017; Wei, Xie and Zhang, JEP 2017) and test it—e.g., survival around the 2008 HNTE reform, eligible vs.
non-eligible firms, provinces with and without maintenance subsidies, and whether buyers' post-sale survival is
concentrated in HNTE-relevant fields.

**4. Citations are both mismeasured and potentially a bad control, and they determine the sign.** δ moves from −10.1 to
+4.1 when log citations (with office-specific slopes), field and owner-group effects are added (Table 2 cols 1–2).
Citations are counted at the DOCDB-family level (supplement l.64): foreign patents in China belong to multi-office
families cited by USPTO/EPO examiners, while domestic Chinese patents mostly sit in single-office families cited under
CNIPA practice. The "factor of five" (data.tex l.89–90) is partly a family-structure/citing-office artefact; one linear
slope per office cannot correct a gap of that size. Citations are also partly an outcome of owner capacity
(commercialisation, foreign filing, visibility), so conditioning on them absorbs part of the "inventor" channel the
paper wants to test—the author accepts this logic for family size (Table S3 note) but it applies equally to family
citations. Requested: (i) decompose the col-1→col-2 move into field, citation and owner-group contributions; (ii) use
citations from a common set of citing offices, or within-office citations only; (iii) flexible bins with
common-support evidence, or reweight foreign patents to the domestic citation distribution; (iv) sensitivity to
unobservables (Oster-type bounds). Without this, "at equal quality" is not credible.

**5. The foreign benchmark differs across offices, and inference treats 10 offices as many clusters.** δ compares
domestic–foreign gaps; "foreign" is a different mix in each office. Table S4 shows the AE benchmark ranges from −1.1
(France) to +16.7 (Japan); the text concedes "the benchmark matters" (survival l.17–20; values l.41). Across EM offices
Table S2 ranges from −9.8 (Russia) to +10.1 (Taiwan) for all owners. Clustering by owner gives tiny SEs, but the
treatment varies across only 5 vs. 5 offices; the SEs understate uncertainty about "EM vs. AE." Also, Table 1 lists
30,420 foreign "small" firms in China vs. 5,607 in Korea, suggesting either that Hong Kong/Taiwan/offshore-registered
Chinese applicants count as foreign, or that HAN splits multinationals across translation variants (HAN harmonisation
of Chinese and Korean names is known to be poor). The same splitting would misclassify large domestic Chinese firms as
"small." Requested: a common benchmark (the same multinational, by HAN, observed in both EM and AE offices, with owner
fixed effects), the origin composition of foreign owners by office, office-level inference (wild cluster bootstrap or
randomization inference over offices), and validation of the size classes for Chinese/Korean owners against an
external register.

**6. The constraint tests are not diagnostic.**
- *Same invention (Fig. 1A).* A cash-constrained owner drops expensive foreign patents first; for EM owners those are
  US/JP/EP patents with high fees and attorney costs. A larger home-minus-abroad gap is therefore at least as
  consistent with constraints as with their absence. Office fee structures also differ (annual vs. US lump payments at
  3.5/7.5/11.5 years). The pooled EM estimate is driven by Russia and the Czech Republic (~35 pp in Fig. S2A), and
  Chinese firms (all) show a *negative* point estimate (~−8 pp, CI spanning zero), contradicting constraints.tex
  l.25–27 and the conclusion (l.6).
- *Credit shocks (Fig. 1B).* With office×year effects, identification is domestic vs. foreign owners in shock years.
  In 2008–09—the shock years for TW, CZ, KR, RU—foreign owners in these offices were mostly AE multinationals hit by
  the global crisis, so a negative domestic-minus-foreign effect in EM offices is close to mechanical. The China
  (2013, 2017–18), Korea 2003–04 and Russia 2014–15 years are not Laeven–Valencia systemic crises, though LV2018 is the
  only source cited (constraints fn 5). Fig. S2B shows Korean firms lapse ~2 pp more in shock years (significant) and
  Japanese firms ~2.5 pp less—the pooled numbers average over strong heterogeneity. Firm-level financial exposure
  (leverage, bank dependence, listed-firm balance sheets) would be needed where available, rather than aggregate shock
  years; at minimum report baseline lapse rates so power can be judged.
- *Sales (Fig. 1C).* The author states the premium is selection ("buyers pick good patents everywhere") but then
  treats the EM-minus-AE difference as informative. That requires selection to be equally strong across offices,
  which is unlikely when Chinese transfers include HNTE-motivated purchases, intra-group/affiliate and
  university-enterprise transfers, and policy-driven university transfers after 2015; recorded "transfers" may also
  include name changes and mergers. Please separate arm's-length sales from intra-group transfers and name changes,
  use pre-sale survival hazards to match, and ideally exploit sales plausibly exogenous to patent quality (bankruptcies,
  owner exits, portfolio sales).
- *Fees (Table S5).* The design relies on a size proxy (patent counts) for eligibility that is income-based in China
  and employment-based in the US/France; France has a significant wrong sign; the US large-firm "placebo" has
  elasticity 0.05—the same as the Chinese small-firm elasticity—so "large US firms not at all" (constraints l.63) is
  not supported. For a 2000–05 cohort the 2016/2018 Chinese changes affect only late-granted patents.

**7. The counterfactual "levers" are not on a common scale.** Fee relief changes behaviour only for marginal patents
(returns ≈ fees), so in the deterministic model its effect on returns is second-order by construction (envelope
theorem). Markets for technology are modelled as multiplying *every* patent's returns by 1.41/1.39/5.0 (21 in the
learning model), calibrated from the selection-contaminated post-sale survival premium and applied to all patents in
the group. "Two to three orders of magnitude" (stake l.79–81) is built in, not found. The calibration is also
inconsistent: firms are calibrated to EM-minus-AE differences while universities are calibrated to China's own 45-pp
premium, on the grounds that the AE premium is "slightly negative" (fn 8)—which would make the difference larger
(~50 pp), not undefined. The mid-sized (5.0 pp) and large-firm (0) post-sale premia used in the calibration appear
nowhere in the exhibits. And the levels rest on d fixed at 0.85, which is not identified in China or the US (free
estimate 0.47; Table S6). I recommend dropping Table 3 and Section 6, or at most retaining a qualitative statement,
and using the exhibit for survival curves or the identification checks above.

**8. Renewal values add no independent evidence and use scarce space.** By the author's own account (values l.67–69),
patent-level values are a monotone transformation of survival on a fee path. Section 5 and Figure 2 thus spend an
exhibit and ~1,000 words restating Table 2. Moreover several claims are undocumented: the deterministic-model estimates
are not reported, robustness to the decay rate is asserted but not shown, and only 1.37–1.42 million of 2.96 million
patents are valued without describing the sampling ("up to 60,000 per owner group" in the appendix). Russia is dropped
with its explanation commented out. I'd move values to the supplement, or use them only where fee paths differ enough
to add information.

**9. Robustness and the university claim.** Universities are called "the one robust weak spot" (intro l.51), but pooled
EM universities are not significantly behind in survival (Table 2 col 6: −5.7, SE 3.6); in value (Fig. 2) the EM
university premium is ~0 and the difference ~−22 log points, not significant; and with family size controlled EM
universities are *ahead* by 9.6** (Table S3 col 3), which the text does not mention. The Chinese university result
rests on the China-specific estimates (−16.9 pp; −0.83 log points) and needs China-specific robustness to the controls
in concerns 1, 3 and 4. Also, owner-group results drop unknown-type owners: 61% of Russian patents (79,126 of
129,038), ~98k in Japan, ~63k in Korea. Korea's records end in 2019 and Russia's in 2022. Please show that missing
applicant data and truncation are unrelated to lapse status, and state how alive-8-years-after-grant is defined for
late-granted KR/RU patents.

**10. Focus and framing for Insights.** The abstract's "keep their patents as long as comparable firms in rich
economies" overstates what is a relative domestic–foreign difference, interpreted as a firm-to-firm comparison only
under a common-foreign-benchmark assumption. The conclusion generalises to "China, Korea and the Czech Republic" and to
"fee cuts" (tested only in China) and "credit shocks" (contradicted for Korea). Missing literature: Akcigit, Celik and
Greenwood (2016, Econometrica) "Buy, keep or sell" is the natural framework for sale-driven reallocation; Serrano
(2018, IER) on gains from trade in patents; Arora, Fosfuri and Gambardella (2001) on markets for technology; Schankerman
(1998, RAND) and Lanjouw, Pakes and Putnam (1998, JIE) on renewal-based values; de Rassenfosse and van Pottelsberghe de
la Potterie on fee elasticities; Hvide and Jones (2018, AER) on university ownership of patents; and the Chinese
incentive literature in concern 3. A paper on one fact—"at matched age and matched observable quality, the EM renewal
shortfall is composition," with the threats above dealt with—has a better chance than the current
four-and-a-half-point structure.

## 4. Minor concerns

1. Table 2: report the mean of the dependent variable by office group and domestic status so pp effects can be scaled.
2. Eq. (1): the pooled spec imposes one domestic coefficient across owner groups; state that col 2 is a
   composition-weighted average.
3. data.tex l.15–17: missing applicant countries are imputed from family and first-filing office. Report the share of
   domestic/foreign labels imputed, by office, and robustness dropping imputed cases.
4. Constraints footnote 5 packs three specifications into one footnote and is hard to parse; each test needs its
   estimating equation in the supplement.
5. "10% lower fee lowers the lapse rate by about 0.5%" (constraints l.61): clarify that this is relative and give the
   baseline lapse rate.
6. Same-invention test: sample sizes by origin–destination office, and the share of "abroad" patents in AE vs. EM
   offices, are needed to read Fig. 1A.
7. Lapse definition: "first cessation" may capture lapses later reversed by restoration (allowed in China and Japan);
   check restoration events.
8. Inclusion rule: the Czech Republic (909 domestic firm patents) is included despite the "about 1,000" threshold
   (Table S1 note) while Hungary (299) is not—fine, but say so in the main text, which says included offices have
   "enough domestic firm patents" (intro l.20–21).
9. Deterministic model (appendix l.8–9): the myopic rule is optimal only if real fees rise; with fixed nominal
   schedules deflated by CPI (Russia especially), real fees fall within a schedule. Discuss.
10. Supplement "Small against large domestic firms" (l.186–191) is useful evidence (3.9 vs 0.6 pp) but has no table,
    SEs or N.
11. Word count: my rough count of the main text excluding exhibits is close to 5,900—at the 6,000 limit. Please report
    the AEA tool count.
12. Figure 1C: the small-firm "All offices" estimate shows no interval; panel B is labelled "All firms" while the text
    says "domestic owners".
13. Abstract: "Owners keep home patents longer than the same inventions' foreign patents" holds in every office, so it
    is not an EM finding and doesn't belong in the headline results.

## 5. Internal-consistency errors

1. **Wrong footnote reference.** supplement_body.tex l.199 (Figure S2 note) says estimates are "specified as in
   footnote 4." The specification footnote is footnote 5 (constraints.tex l.5); footnote 4 is the grant-lag footnote
   (data.tex l.100). Intro has fns 1–2, data fns 3–4. Use \ref.
2. **China fee discount described inconsistently.** constraints.tex l.59–60 and Table S5 row 1 (supplement l.212):
   "85% fee reduction ... window extended from three to six fee-years in 2016." But values.tex l.57–58 and supplement
   l.257–258: owners paid 30% of the fee (70% reduction) until Aug 2016, and 15% only afterwards. So the 2016 reform
   both deepened and extended the discount.
3. **Korea discount described inconsistently.** Table S5 (supplement l.213): "30%/50% discounts for years 4+ (2014,
   2016, 2018)." supplement l.259–260 and values.tex l.58–59: 70% of the fee in years 4–6 from 2014, 50% in years 4+
   from 2018—no 2016 change.
4. **US large-firm fee response.** constraints.tex l.63 "large US firms not at all," but Table S5 placebo elasticity is
   0.05, identical to China's small-firm elasticity (coef 0.009, SE 0.048).
5. **China vs US small-firm premium.** introduction.tex l.48: small firms' premium in China and Korea "is at least as
   large as in the United States and Germany." Table S7: China 0.20 < US 0.23 (equal to Germany 0.20).
6. **Number of valued patents.** values.tex fn 6 (l.24): 1.37 million patents; Table S7 note (supplement l.328): 1.42
   million. Neither is reconciled with the 2.96 million in Table 1.
7. **Figure 2 vs Table S7.** Figure 2's pooled EM small-firm premium (~17) lies below both China (20) and Korea (49),
   which hold ~90% of EM domestic small-firm patents (Table 1); a weighted average of Table S7 gives ~32. The AE "all
   owners" premium (~42) is well below a patent-weighted average of US (34) and Japan (114) (~63). Explain the
   specification/weighting difference.
8. **Russia contradiction.** Table S7 note a (supplement l.330–331) says domestic ownership is collinear with the fee
   path, yet Russian small/mid/large estimates are reported (mid 1.75**). Figure 2's note says Russia is left out.
9. **Russia cross-references point at commented-out text.** The explanation of Russian non-identification is commented
   out (values.tex l.49–53), but stake.tex fn 7 (l.11) and the S7 note send the reader to Section 5 for it.
10. **Claimed supplement content missing.** values.tex l.16 and appendix_models.tex l.3 say Supplemental Appendix S4
    gives "the fee schedules ... and the estimates." S4 contains no fee-schedule tables and no deterministic-model
    estimates (Table S6 is learning model only). "The deterministic model gives the same pattern" (values l.47) and
    stability "across ... decay rates" (values l.67–68) are not shown.
11. **Discount value ratios.** values.tex l.59–60: "values fall by a few percent" and ratios 1.88/2.41 (deterministic)
    and 1.66/1.97 (learning); no standard-fee baseline is reported, and the implied 63–88 log points are hard to square
    with Table S7 (0.20 and 0.49).
12. **Unreported calibration inputs.** stake.tex l.32–34 and fn 8 (l.17–19) use a mid-sized post-sale premium of 5.0 pp
    and zero for large firms; neither appears in Figure 1 or Figure S2 (which show only all firms, small firms,
    universities).
13. **Conclusion vs figures.** conclusion.tex l.5–6: credit shocks "barely move" EM firms' decisions and owners "do not
    drop the home patents." Fig. S2B: Korean firms +~2 pp/yr (significant); Fig. S2A: Chinese firms (all) negative
    home-minus-abroad point estimate. conclusion l.20–21: survival result is "weaker without" Korea and Taiwan—but
    Taiwan's small firms are behind (Table S2: −2.4*), so dropping Taiwan should strengthen the small-firm result.
14. **Table 2 possible transcription error.** Column 1 "Domestic owner" (4.08, SE 0.75) is identical to column 2
    "Domestic × EM" (4.08, SE 1.44). Please verify.
15. **Table 2 vs Table 1 observation counts.** Table 2 cols 3–6: 332,608 / 384,430 / 1,769,598 / 159,298; Table 1
    totals: 332,609 / 384,434 / 1,769,599 / 159,305. The China/US and non-China/US subsamples sum exactly within Table
    2, so the gaps are in the non-China/US offices (presumably singletons)—state this.
16. **Table 1 Panel B.** "All offices" domestic counts (123,285; 19,258; 3,365; 13,410) are below the column sums across
    offices (123,289; 19,274; 3,400; 13,419), implying owners "domestic" in more than one office. Explain.
17. **Sample description.** introduction.tex l.23: "approximately three million granted patents held by firms and
    universities." Table 1's 2,961,829 includes 315,882 patents of owners of unknown type (including 61% of Russian
    patents).
18. **Follow-up period.** data.tex l.4: patents "followed for close to twenty years," but Korean lapse records end in
    2019 (Table S5 note l.223) and Russian in 2022 (supplement l.254). Table S1 ("candidate emerging-market offices")
    omits China and Korea, the two main offices, and Brazil, which is mentioned in its note and in intro fn 2.
19. **Robustness omitted from text.** survival.tex l.26 and introduction l.33 report the richer-control small-firm
    estimate as "level," omitting Table S3 col 3 (−1.7**) and the universities' switch to +9.6**.
20. **"Bounds" mislabel.** supplement_body.tex l.256: "For the bounds in Section 5"—Section 5 presents no bounds; the
    fee-relief counterfactual is in Section 6.
21. **Credit-shock source.** Constraints fn 5 cites Laeven–Valencia (2018) for shock years that LV does not classify as
    systemic crises (China 2013/2017–18, Korea 2003–04, Russia 2014–15, Taiwan and Czech Republic 2008–09).
22. **Typos/layout.** data.tex footnote at l.12–13 lacks a final period; introduction.tex l.21 "South-East Asia
    countries"; constraints.tex l.32 "( $-0.9$"; values.tex l.46 "foreign universities' patent" → "patents"; manual
    \clearpage\newpage mid-section at survival.tex l.29–30 and supplement l.336–337; commented-out sentence at
    introduction.tex l.49.

Numbers that do check out: Table 2 subsample observation counts, Table 1 Panel A totals, fn 8 patents per year (Table 1
/ 6), Table 3 row sums and % of R&D, Table S8 ratios ("about ten," "five times"), text figures quoted from Tables 2, S2,
S3, S4 and Figures 1–2 except where listed above, 1−e^(−0.83) = 56%, abstract = 100 words.

## 6. Confidential note to the editor

**Recommendation: Reject.**

The question is important and the multi-office lapse-and-fee dataset is a real asset. But the headline claim—equal
survival at equal quality—is not robust: it depends on citation controls that are poorly measured for exactly the
comparison at issue, is driven by China vs. the US, and flips sign for small firms under richer controls or outside
China/US. Several first-order threats (a 2–4 year grant-lag gap between domestic and foreign owners in EM offices,
unequal fees within the "same office" from Russian non-resident schedules and domestic-only discounts, Chinese tax and
subsidy incentives to maintain patents) could each generate the result and are not addressed. The constraint tests do
not discriminate between hypotheses; the sale result that drives the policy message is selection; and the policy
counterfactuals compare a lever that is second-order by construction with an assumed productivity multiplier. For
Insights, the paper also lacks a single clear point—it makes four or five, and the renewal-value section restates the
survival results. I counted more than 20 internal inconsistencies (fee-discount descriptions, cross-references to
missing or commented-out material, unreported calibration inputs), suggesting it is not ready. A tightly focused
version—one fact, survival matched on age-from-filing and fees, with credible quality measurement and office-level
inference—could become a good field-journal paper or perhaps a later Insights submission, but that requires
substantial new analysis rather than revision.

---

## Author's triage notes (2026-11-04)

- §5 item 14 is a false alarm: the two 4.08s are different coefficients with different standard errors (0.75, 1.44).
- Credit-shock years outside Laeven–Valencia are documented credit crunches; cite sources rather than drop.
- Section 6 is kept (author's decision).
