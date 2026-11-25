# #43, one lemma: no source this repository holds prints the $\Gamma_{\mathrm{Co},2}$-cusp root-class orbits

**Lemma.** The row at the 135-orbit $\Gamma_{\mathrm{Co},2}$-cusp cannot be *cited*: none of the printed sources in this
repository's holdings states the orbits of a $\Gamma_{\mathrm{Co},2}$-cusp's root classes, so the value can only be certified by computation.

**Checked, source by source.**

| source | what it treats | $\Gamma_{\mathrm{Co},2}$-cusp orbits? |
| --- | --- | --- |
| H. Sterk, Math. Z. 207 (1991), §4, pp. 16–26 | the five 0-cusps of $\Gamma_{\mathrm{En},2}$ on $T_{\mathrm{En}}$: chambers, diagrams, symmetries | no — every lattice in §4 is $L_- = T_{\mathrm{En}}$ or $H \oplus E_8(-2)$ |
| V. Alexeev, P. Engel, D. Z. Garza, L. Schaffler, Nagoya Math. J. 259 (2025) | $F_{\mathrm{En},2}$: its cusps, folded diagrams (§3.3–3.9, pp. 590–596), stable pairs | no — the word "Coble" appears twice in the paper, both times for Coble *surfaces* arising at torus-fixed points, and the period lattice treated throughout is $T_{\mathrm{En}}$ |
| D. Dutour Sikirić, K. Hulek, J. London Math. Soc. 110 (2024) | polarised Enriques surfaces, the Tits building, line and plane orbits | no — "Coble" does not occur in the paper, and no root class of a $K_I$ is discussed |
| F. Scattone, Mem. AMS 374 (1987) | $\Lambda_2$, $\Lambda_4$, K3 cusps | no |
| V. V. Nikulin, Izv. 1980 / J. Soviet Math. 1983 | integral forms, two-elementary lattices | no |

Each of the first three was searched for "Coble", for "root class" / "root orbit", and read at the pages where its cusp
material sits; the last two are about other lattices entirely.

**Why this is worth recording.** The issue's rule is that a value is "cited from a source that proves it, or certified by
computation", and the corpus's own practice is to leave a field absent rather than guessed. This lemma closes the first
half of that disjunction for the $\Gamma_{\mathrm{Co},2}$-cusps: there is nothing to cite. So the row at the 135-orbit $\Gamma_{\mathrm{Co},2}$-cusp is not waiting on more
reading — it is waiting on the exact orbit computation at a $\Gamma_{\mathrm{Co},2}$-cusp, which is the owner's
`_double_coset_adjustment` returning (`results/probe-43-coble-cusp5-equivalence.py`) or a certified generating family at
that cusp.

It also bounds what the other lemmas can ever be: the structural ones
(`results/issue-43-lemma-alpha13-alpha14.md`, `results/issue-43-lemma-coble-image.md`,
`results/issue-43-lemma-gv-not-stated.md`) reason from Sterk, and Sterk is about $T_{\mathrm{En}}$; none of them can turn
into a citation for the Coble card.

**Sources by printed page.** As tabulated: Sterk, Math. Z. 207 (1991), 1–36, §4, pp. 16–26; Alexeev–Engel–Garza–Schaffler,
Nagoya Math. J. 259 (2025), 581–624, §3.3, p. 590, and §3.7–3.9, pp. 592–596; Dutour Sikirić–Hulek, J. London Math. Soc.
110 (2024), §3.6, p. 22; Scattone, Mem. AMS 374 (1987); Nikulin, Izv. Akad. Nauk SSSR 44 (1980).
