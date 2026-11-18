---
slug: h-e
name: H_e
latex: H_e
lattice: '0125'
ambient_lie_group: o-1-9
parent_group: g-e
data:
  cardinality: aleph0
  abstract_structure: the subgroup of G_e that the stored lifts of the discriminant stabilizer P generate
  generator_morphisms: [H_e generator 1, H_e generator 2, O(L) generator 8]
---

$H_e$ is the subgroup of $G_e$ that the stored lifts of the stabilizer $P$ generate: `L.Aut().discriminant_lift` applied to the three generators of $P = \mathrm{Stab}_{O(A_L)}(A_{U(2)})$ that `O(A_L).stabilizer_of_classes` returns, each lift an isometry of $U(2) \oplus E_8(-2)$ inducing that element of $P$ on $A_L$. Each is stored as a scale-$1$ `morphisms` entry of the card of [0125](../tag/0125.html) and named in `data.generator_morphisms` here: `H_e generator 1`, `H_e generator 2` and `O(L) generator 8`, the last being an isometry of $O(L)$'s own generator list, which is stored once and named there.

The map $\rho_L \colon O(L) \to O(A_L)$ is onto, and $G_e = \rho_L^{-1}(P)$ for $P$ the stabilizer in $O(A_L)$ of the two-class form group $A_{U(2)}$ of the first summand (H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*, Math. Z. 207 (1991), 1–36, (4.3.5), p. 19; the same $P$ is the discriminant part of Sterk's $G_e$).
Each stored lift induces an element of $P$, by construction, and $\rho_L(H_e) = P$: the images generate a subgroup of $O(A_L)$ of order $696729600$, which is the engine's own order of $P$, and also $|O(A_L)| / |\mathrm{orbit}(A_{U(2)})| = 46998591897600 / 67456$ by the index–stabilizer identity, and $2 \cdot 348364800$, the product of the isometry groups of the two summands $A_{U(2)}$ and $A_{E_8(-2)}$. The row's certificate on the card of [0125](../tag/0125.html), `arithmetic-group.h-e.generator_morphisms`, commits to the stored matrices and names the owner revision that returned them.

These are **not** generators of $G_e$, and this card does not name them as such.
$G_e = \widetilde O(L) \cdot H_e$, and no generating set of the discriminant kernel $\widetilde O(L) = \ker \rho_L$ exists: Kneser's theorem needs $\mathrm{rank}_2 \ge 6$ against $\mathrm{rank}_2(L) = 0$, Gritsenko–Hulek–Sankaran's Proposition 3.4 needs two hyperbolic planes, Allcock's family is stated for $\Lambda(2)$ rather than for this lattice, and the Schreier family over a transversal of the finite image has $46998591897600$ cosets (sage-extensions#597).
The other route to a generating set of $G_e$ is the whole Schreier family of the orbit of $A_{U(2)}$ (Seress, *Permutation Group Algorithms*, Lemma 4.2.1, p. 57), which `L.Aut().discriminant_point_stabilizer(A_{U(2)}).group_generators()` returns and which has $15 \cdot 67456 - 67455 = 944385$ members (sage-extensions#354); no card holds it.
The lifts are also not the greedy subfamily that `L.Aut().discriminant_point_stabilizer_image_generators(A_{U(2)})` selects: that call returns no value on the machine this was computed on, ending inside its selection loop without a value or a traceback in three runs (measured in `results/evidence-40-ge-generators.md`), so the stored generators are the lifts of $P$'s own three generators, and $H_e$ is a chosen subgroup of $G_e$ whose only claimed property is $\rho_L(H_e) = P$.
