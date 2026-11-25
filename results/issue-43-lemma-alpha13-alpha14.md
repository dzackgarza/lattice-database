# #43, one lemma: at (4.3.9) the symmetry exchanging $\alpha_{13}$ and $\alpha_{14}$ fixes $\delta$

**Lemma.** Of the two symmetries of the chamber diagram at `(4.3.9)` that exchange $\alpha_{13}$ with $\alpha_{14}$,
the one fixing $\alpha_{11}$ and $\alpha_{12}$ sends $\delta = e - f$ to $\delta$ as an isometry of the lattice the walls
span. Every realisation of it therefore preserves $T_{\mathrm{Co}} = \delta^\perp$, so it lies in
$\mathrm{Stab}_{O(T_{\mathrm{En}})}(\delta)$, and the two root classes are one orbit under the $\Gamma_{\mathrm{Co},2}$-cusp stabilizer.
The count at that cusp is therefore **at most 2**.

**Proof.** Card 029J's Gram tensor gives the fourteen walls of the `(4.3.9)` chamber, their squares and their pairings.
Two facts, each a finite computation on that tensor:

1. the walls span a lattice of rank 10 — ten of the fourteen are independent, and
2. $\delta = e - f$ lies in that span: solved on the ten, $\delta$ is reconstructed exactly.

So an isometry whose action on the walls is a given diagram symmetry is determined on the span, and $\delta$'s image is
determined with it. The eight symmetries of the diagram are the permutations of the walls preserving squares and
pairings; exactly two send $\alpha_{13}$ to $\alpha_{14}$, and computing $\delta$'s image under each:

| symmetry | walls it fixes | image of $\delta$ |
| --- | --- | --- |
| $\alpha_{11} \leftrightarrow \alpha_{12}$ among others | $\widetilde\alpha_1$, $\alpha_9$ | neither $\delta$ nor $-\delta$ |
| fixes $\alpha_{11}$, $\alpha_{12}$ | $\widetilde\alpha_1$, $\alpha_6$, $\alpha_9$, $\alpha_{10}$, $\alpha_{11}$, $\alpha_{12}$ | $\delta$ |

The second is the one that preserves the $T_{\mathrm{Co}}$ wall set (the first carries $\alpha_{11}$, which is not a wall
of $T_{\mathrm{Co}}$, onto $\alpha_{12}$, which is), and it fixes $\delta$. Sterk's `(4.3.10)`–`(4.3.12)`, p. 25, realises
such a symmetry by an isometry of $A = H \oplus E_8(-2)$ extending its action on the rank-10 span; that extension agrees
with the symmetry on the span, hence fixes $\delta$, hence preserves $T_{\mathrm{Co}}$. So the realising isometry lies in
$\mathrm{Stab}_{O(T_{\mathrm{En}})}(\delta)$, and with Sterk's statement at `(4.3.9)`, p. 24 — "Symmetries of the graph
can be lifted to $\Gamma_v$" — it is an exhibited isometry carrying $\alpha_{13}$ to $\alpha_{14}$. $\square$

**What this corrects.** The previous turn's lemma said Sterk's argument never mentions $\delta$ and so cannot be
transported. That is true of the argument as written — it is stated for $A = H \oplus E_8(-2)$ — but not of this
symmetry: the symmetry happens to fix $\delta$ on the span, so the transport is available here after all. The two
lemmas compose rather than conflict: the general claim is unavailable, and the specific instance goes through by
computation.

**What is left, and it is one question.** With $\alpha_{13}$ and $\alpha_{14}$ identified, the `(4.3.9)` count is
$1$ if $\alpha_{12}$ joins them and $2$ if it does not. No symmetry of the diagram carries $\alpha_{12}$ to
$\alpha_{13}$ or to $\alpha_{14}$ while preserving $\delta$ — among the eight, the ones that move $\alpha_{12}$ are the
first row above, which does not fix $\delta$ — so the answer needs an element outside the chamber's symmetry group: a
word in $\Gamma_{\mathrm{Co},2}$'s generators that is a product, which is what the earlier walks over the owner's
family looked for and did not find.

**Sources by printed page.** H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*,
Math. Z. 207 (1991), 1–36: `(4.3.9)`, p. 24; `(4.3.10)`, p. 25; `(4.3.12)`, p. 25.
