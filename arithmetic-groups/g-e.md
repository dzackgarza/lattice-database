---
slug: g-e
name: G_e
latex: G_e
lattice: '0125'
ambient_lie_group: o-1-9
parent_group: o-u2-e8
data:
  cardinality: aleph0
  abstract_structure: the stabilizer in O(U(2) + E8(-2)) of the decomposition of
    the discriminant group, the image of the stabilizer of the isotropic vector e
  reference:
    citation: 'H. Sterk, "Compactifications of the period space of Enriques surfaces,
      Part I", Math. Z. 207 (1991), 1-36, (4.3.5), p. 19: "It is easy to see that
      G_e = {g in O(M(2)) : the induced map on M(2)*/M(2) respects the decomposition}",
      where G_e is the image of the stabilizer Gamma_e of the isotropic vector e in
      O(M(2)) = O(U(2) + E8(-2)); and (4.3.5) again: "G_e = {+-1} W_e semidirect S_e"
      with S_e = Z/2 x Z/2.'
---

The image of the stabilizer $\Gamma_e$ of the isotropic vector $e$ in $O(M(2)) = O(U(2) \oplus E_8(-2))$, which Sterk identifies with the subgroup of $O(M(2))$ whose induced map on the discriminant group $M(2)^*/M(2)$ respects its decomposition (H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*, Math. Z. 207 (1991), 1–36, (4.3.5), p. 19).
That decomposition is $A_{U(2)} \oplus A_{E_8(-2)}$, of the two orthogonal summands, and the condition cuts $O(L)$ down to a subgroup of finite index: Sterk writes $G_e \cong \{\pm 1\} W_e \rtimes S_e$ with $S_e \cong \mathbb{Z}/2 \times \mathbb{Z}/2$, so the chamber of $W_e$ is not the chamber of $O(L)$ and has twelve walls where the lattice's own reflection group has ten.

A generating set of $G_e$ itself is absent, and no public `sage-extensions` call returns one.
$G_e = \widetilde O(L) \cdot H_e$ with $\widetilde O(L) = \ker \rho_L$: Sterk's group is the full preimage of $P$ under $\rho_L$, the family that generates it is the Schreier family of the orbit of $A_{U(2)}$ with $15 \cdot 67456 - 67455 = 944385$ members (sage-extensions#354, Lemma 4.2.1 of Seress, *Permutation Group Algorithms*, p. 57), and no generating set of $\widetilde O(L)$ exists (sage-extensions#597).
What is stored is the other factor: three self-isometries of $L$ — `H_e generator 1`, `H_e generator 2` and `O(L) generator 8`, the last one an isometry of $O(L)$'s own generator list, so stored once — which are the lifts along $\rho_L$ of the three generators of $P = \mathrm{Stab}_{O(A_L)}(A_{U(2)})$ and generate a subgroup $H_e \le G_e$ with $\rho_L(H_e) = P$.
The card of [H_e](h-e.html) names them and states that relation; they are `morphisms` entries with `scale: 1` of the card of [0125](../tag/0125.html), and the certificate `arithmetic-group.h-e.generator_morphisms` on that card commits to their matrices at the owner revision that returned them.
They are **not** generators of $G_e$ and this card claims none: it states no `data.generator_morphisms` and no `data.index_in_orthogonal_group`, whose value $[O(L) : G_e] = 67456$ is known only for $G_e$ itself, not for $H_e$.
`integral.cusp_chambers['g-e']` on the card of [0125](../tag/0125.html) states the chamber of $W_e$ without a generator list.
