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
  generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 10]
---

$H_e$ is the subgroup of $G_e$ that the nine members of the greedy subfamily generate: `L.Aut().discriminant_point_stabilizer_image_generators(A_{U(2)})` returns them, the subfamily of the Schreier family of the orbit of $A_{U(2)}$ whose images generate $P = \mathrm{Stab}_{O(A_L)}(A_{U(2)})$ (sage-extensions#354; the lazy family that makes the call return is sage-extensions#459), and each of the nine is an isometry the card of [0125](../tag/0125.html) already stores as `O(L) generator 1`, `O(L) generator 2`, `O(L) generator 3`, `O(L) generator 4`, `O(L) generator 5`, `O(L) generator 6`, `O(L) generator 7`, `O(L) generator 8` and `O(L) generator 10`, so each is stored once and named there.

The map $\rho_L \colon O(L) \to O(A_L)$ is onto, and $G_e = \rho_L^{-1}(P)$ for $P$ the stabilizer in $O(A_L)$ of the two-class form group $A_{U(2)}$ of the first summand (H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*, Math. Z. 207 (1991), 1–36, (4.3.5), p. 19; the same $P$ is the discriminant part of Sterk's $G_e$).
Each stored member induces an element of $P$, by construction, and $\rho_L(H_e) = P$: the images generate a subgroup of $O(A_L)$ of order $696729600$, which is the engine's own order of $P$, and also $|O(A_L)| / |\mathrm{orbit}(A_{U(2)})| = 46998591897600 / 67456$ by the index–stabilizer identity, and $2 \cdot 348364800$, the product of the isometry groups of the two summands $A_{U(2)}$ and $A_{E_8(-2)}$. The row's certificate on the card of [0125](../tag/0125.html), `arithmetic-group.h-e.generator_morphisms`, commits to the stored matrices and names the owner revision that returned them.

These are **not** generators of $G_e$, and this card does not name them as such.
$G_e = \widetilde O(L) \cdot H_e$, and no generating set of the discriminant kernel $\widetilde O(L) = \ker \rho_L$ exists: Kneser's theorem needs $\mathrm{rank}_2 \ge 6$ against $\mathrm{rank}_2(L) = 0$, Gritsenko–Hulek–Sankaran's Proposition 3.4 needs two hyperbolic planes, Allcock's family is stated for $\Lambda(2)$ rather than for this lattice, and the Schreier family over a transversal of the finite image has $46998591897600$ cosets (sage-extensions#597).
The other route to a generating set of $G_e$ is the whole Schreier family of the orbit of $A_{U(2)}$ (Seress, *Permutation Group Algorithms*, Lemma 4.2.1, p. 57), which `L.Aut().discriminant_point_stabilizer(A_{U(2)}).group_generators()` returns and which has $15 \cdot 67456 - 67455 = 944385$ members (sage-extensions#354); no card holds it.
They are the greedy subfamily the issue names, and the call that returns them is the repaired one: at sage-extensions `2fb37d5a717` it did not return on the machine this was computed on (seven runs, recorded in `results/evidence-40-ge-generators.md`), and at `b501886b`, where sage-extensions#459 closed, it returns the nine in $93$ s.
