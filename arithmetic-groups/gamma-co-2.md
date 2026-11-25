---
slug: gamma-co-2
name: Gamma_Co,2
latex: \Gamma_{\mathrm{Co},2}
lattice: 6JRR
ambient_lie_group: o-2-9
data:
  index_in_orthogonal_group: 67456
  cardinality: aleph0
  line_orbits: 4
  plane_orbits: 7
  flag_orbits: 13
  abstract_structure: R_{Gamma_En,2}, the image in O(T_Co) of the isometries of T_En that lie in Gamma_En,2 and fix delta, T_Co = delta^perp, delta = e - f; equal to rho^{-1}(P_0) with P_0 = Stab_{O(q)}(A_U(2)), the preimage of the stabilizer of the hyperbolic line A_U(2) of [h/2]^perp; it contains ker rho = Otilde(T_Co)
  reference:
    citation: 'the construction, and not a definition in print: research def:gamma-co-groups(5) defines Gamma_Co,2 = R_{Gamma_En,2}; sage-extensions results/issue286-gamma-co-2-is-the-discriminant-preimage.md proves R_{Gamma_En,2} = rho^{-1}(P_0) from prop:gamma-co-images(3) (the summands A_U(2) and A_E8(2) have orders 4 and 256, so no isometry swaps them). The index is [O(q) : P_0], because rho is onto (Nikulin 1980, Thm. 3.6.3); by the transitivity of O(q) on them, which the program checks, it is the number of hyperbolic lines of [h/2]^perp, 67456, which results/fix-49-gamma-co-2-card.py counts on card 6JRR. The three orbit counts are carried from sage-extensions results/issue607-gamma-co-2-rows-by-the-polar-space.md at commit 47865446a7c37c85d873f91ac9d74cea472e208c, which proves 4 line, 7 plane and 13 flag orbits of this group (GAP log results/issue607-the-levi-candidate.log), in agreement with sage-extensions#391''s image run 43556671111. Nothing here identifies this group with the Coble period group'
---

Its three orbit counts are the ones sage-extensions proves and computes for it, and this database does not recompute them: `latticedb certify` presents a subgroup only through a card's `standard_name`, and $\Gamma_{\mathrm{Co},2}$ is not one of the eight standard subgroups, so the counts are carried from the record with its citation (`data.reference`) rather than minted here.
$\Gamma_{\mathrm{Co},2}$ has $4$ orbits of primitive isotropic lines, of sizes $34560$, $17280$, $15360$ and $256$; $7$ orbits of primitive isotropic planes, of sizes $26880$, $24576$, $8064$, $3360$, $2688$, $1120$ and $768$, over the $67456$ hyperbolic lines of $O(q)$; and $13$ orbits of isotropic flags (sage-extensions `results/issue607-gamma-co-2-rows-by-the-polar-space.md`, commit `47865446a7c37c85d873f91ac9d74cea472e208c`, whose GAP log is `results/issue607-the-levi-candidate.log`).
Those counts agree with the public call's own record of the row — $4$ line cusps, $7$ plane cusps and $13$ edges in sage-extensions#391's image run `43556671111` — which is the agreement that lets the record stand in for a computation of this card's field.
