---
slug: gamma-en-2
name: Gamma_En,2
latex: \Gamma_{\mathrm{En},2}
lattice: 029J
ambient_lie_group: o-2-10
parent_group: o-t-en
data:
  index_in_orthogonal_group: 67456
  abstract_structure: the image in O(T_En) of the isometries of the K3 lattice that
    commute with I_En and fix h
  reference:
    citation: 'V. Alexeev, P. Engel, D. Z. Garza, L. Schaffler, "Compact moduli of Enriques surfaces of degree 2", Nagoya Math. J. 259 (2025), 581–624, Definitions 2.6 and 2.7: the group; Section 3.3, p. 590: "There are five 0-cusps for which we use Sterk''s numbering 1, 2, 3, 4, 5. There are also 9 distinct 1-cusps."; the five orbits of primitive isotropic lines are H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207 (1991), 1-36, Proposition 4.2.3 with Remark 4.2.4, p. 16.'
  cardinality: aleph0
  line_orbits: 5
  plane_orbits: 9
---

The five orbits of primitive isotropic lines of $\Gamma_{\mathrm{En},2}$ are its 0-cusps, and the nine of primitive isotropic planes its 1-cusps: Sterk's Proposition 4.2.3 with Remark 4.2.4, p. 16, counts the lines, and Alexeev–Engel–Garza–Schaffler, Section 3.3, p. 590, states both numbers.

The five $0$-cusps of $\Gamma_{\mathrm{En},2}$ are Sterk's five primitive isotropic vectors, and the chambers of the reflection subgroups $\Gamma_{\mathrm{En},2,v}$ at three of them are stored in `integral.cusp_chambers['gamma-en-2']` on the card of [029J](../tag/029J.html#cusp-chambers): (4.3.5), p. 19 with Fig. 4, at the cusp $e$, with $12$ walls; (4.3.6), p. 21 with Fig. 6, at $e'$, with $10$ walls; and (4.3.8), p. 23 with Fig. 10, at $2e' + f' + \bar\alpha_1$, with $11$ walls (H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*, Math. Z. 207 (1991), 1–36, Section 4.3).
Statement (4.3.7), pp. 21–22 with Fig. 8, at $e' + f' + \bar\alpha_8$, and statement (4.3.9), pp. 23–24 with Fig. 12, at $2e + 2f + \bar\alpha_1$, print their chambers only in figures that the scan of the paper does not resolve into vectors, so those two cusps have no stored chamber: their rows stop at the statement, and the card of [029J](../tag/029J.html#cusp-chambers) says so.
The three stored diagrams are Sterk's; the wall counts, Gram matrices and Coxeter diagrams are what the lattice's Gram tensor says about his walls, computed once and certified, and no Vinberg search was run for them.
