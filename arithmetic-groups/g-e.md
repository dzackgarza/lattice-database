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

Its generators are absent: no public `sage-extensions` call returns them (`results/evidence-39-ge-card.md` states the call that was tried and where it stops), so they are not stored, and `integral.cusp_chambers['g-e']` on the card of [0125](../tag/0125.html) states the chamber without a generator list.
