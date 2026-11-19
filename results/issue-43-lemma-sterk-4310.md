# #43, one lemma: Sterk's (4.3.10) does not lift a Coble symmetry

**Lemma.** Sterk's reduction of the symmetry-lifting question (`(4.3.10)`–`(4.3.13)`, pp. 25–26) is a statement about
$A = H \oplus E_8(-2)$, the perpendicular of an Enriques cusp, and about the sublattice
$K' = \mathbb{Z}\{e+f, e-f\} \oplus E_8(-2) \subset A$. It says nothing about the Coble lattice
$T_{\mathrm{Co}} = \delta^\perp = \langle 2\rangle \oplus U(2) \oplus E_8(-2)$, $\delta = e - f$, and therefore it cannot
be transported to $\Gamma_{\mathrm{Co},2}$.

**Proof, from the printed page.** `(4.3.10)`, p. 25: "To check whether a symmetry of a diagram lifts to the stabilizer
group of the corresponding isotropic vector, one can proceed as follows. Note that in the last cases ((4.3.7), (4.3.8),
(4.3.9)) the span of the roots occurring in the diagram is of the form
$\mathbb{Z}\{e-f,\ e+f\} \oplus E_8(-2)$ ($e$, $f$ standard basis for $H$)." The paragraph then sets
$A = H \oplus E_8(-2)$ and $K' = \mathbb{Z}\{e+f, e-f\} \oplus E_8(-2) \subset A$, a sublattice of index 2 whose form is
$K(2)$, and `(4.3.12)`, p. 25 — "Every $g \in O(K(2))$ extends to an isometry of $A$" — is what makes a symmetry of the
diagram, which lives on $K'$, act on $A$: the proof extends $g$ through the dual lattices
$A^*(2) \cong K(4) = H(2) \oplus \{E_8(-4)\}$ and $g(A^*(2)) = A^*(2)$. Every object in that argument is built from
$H \oplus E_8(-2)$: no step mentions $T_{\mathrm{Co}}$, $\delta$, or a condition fixing $e - f$.

The Coble side needs the opposite: an isometry of $A$ that preserves $T_{\mathrm{Co}} = \delta^\perp$, i.e. one carrying
$\delta$ to $\pm\delta$. `(4.3.12)` gives an isometry of $A$ from one of $K'$ and says nothing about where it sends
$\delta = e - f$: extending is not the same as fixing, and nothing on pp. 25–26 controls the sign or the vector.
So the lemma holds: Sterk's lifting statement is an Enriques statement.

**What it refutes.** The earlier turns read "the symmetry of the diagram comes from an element in $\Gamma_v$" ((4.3.7),
p. 22), "the symmetry is induced by an element of $\Gamma_v$" ((4.3.8), p. 23) and "Symmetries of the graph can be lifted
to $\Gamma_v$" ((4.3.9), p. 24) as a statement that also settles the $T_{\mathrm{Co}}$ rows. It settles the $T_{En}$
rows, which are stored; it does not settle the Coble ones. That is consistent with the measurement: of the owner's
family at the Coble cusp, 22 of 27 members preserve $T_{\mathrm{Co}}$ and none of the 22 carries one root class to
another (`results/probe-43-coble-classes.py`), and the exact equivalence does not return there
(`results/probe-43-coble-cusp5-equivalence.py`, killed in `_double_coset_adjustment`, `orthogonal_quotients.py:234`).

**A second lemma, computed from the card, that narrows the row.** The chamber at `(4.3.9)` has fourteen walls and
eight symmetries of its Coxeter diagram, read off card 029J's Gram tensor (the wall squares and their pairings). Exactly
two of the eight carry the $T_{\mathrm{Co}}$ wall set $\{\alpha_{12}, \alpha_{13}, \alpha_{14}\}$ to itself — the
identity and the one exchanging $\alpha_{13}$ with $\alpha_{14}$ while fixing $\alpha_{12}$ and $\alpha_{11}$. So the
only diagram symmetry that could join two of the three Coble classes joins $\alpha_{13}$ and $\alpha_{14}$, and the row's
count is $1$ or $2$, never $3$, as soon as that symmetry is realised inside $\Gamma_{\mathrm{Co},2}$; if it is not,
nothing on pp. 22–26 says what the count is. That is a strictly sharper question than "is the count 1, 2 or 3", and it
is the one the row now waits on.

Careful with what the computation states: a symmetry preserves the *wall set* of $T_{\mathrm{Co}}$, which is necessary
for the isometry realising it to preserve $T_{\mathrm{Co}}$ and not sufficient; the graph does not determine the
isometry.

**Consequence for the issue.** Cusp 5 of the $T_{\mathrm{Co}}$ side cannot be decided from Sterk, and it is not decided
by anything the owner's library returns today. The row stays empty; the two cusps whose family is one class stay
stored, because their count needs no symmetry at all.

**Sources by printed page.** H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*,
Math. Z. 207 (1991), 1–36: `(4.3.7)`, p. 22; `(4.3.8)`, p. 23; `(4.3.9)`, p. 24; `(4.3.10)`, p. 25; `(4.3.12)`, p. 25;
`(4.3.13)`, p. 26. Read from the PDF's text layer and, for pp. 22, 24 and 25, as page images where the text layer's
rendering of the formulas was ambiguous.
