---
slug: gamma-co-2
name: Gamma_Co,2
latex: \Gamma_{\mathrm{Co},2}
lattice: 6JRR
ambient_lie_group: o-2-9
parent_group: otilde-plus-t-co
data:
  index_in_orthogonal_group: 4417735280714304737771520000
  cardinality: aleph0
  line_orbits: 4
  plane_orbits: 7
  flag_orbits: 13
  abstract_structure: the image in O(T_Co) of the isometries of T_En that lie in Gamma_En,2 and preserve T_Co = delta^perp, delta = e - f; equivalently the kernel of the T_En-side discriminant character on Otilde+(T_Co), which is the restriction R_{Gamma_En} of the Enriques group to this lattice
  reference:
    citation: 'the construction, and not a definition in print: sage-extensions'' own record `results/issue359-tco-restricted-stabilizers.md`, rows 1 and 2, identifies the restricted stabilizers on T_Co = delta^perp as R_{Gamma_En} = Otilde+(T_Co) of index 93997183795200 = 2|O(A_T_Co, q)| in O(T_Co) and R_{Gamma^K_En} = O(T_Co) of index 1, both computed from the images of the constructed generators, and sage-extensions#286 item 1 is the issue that builds them. The index stored here is the product of that index with the order of the T_En-side discriminant character''s image on the family, 46998591897600, computed by results/probe-43-co2-family.py from 290 generators of Stab_{O(T_En)}(delta) restricted to T_Co. Nothing here asserts the identification of this group with the Coble period group, which the corpus records as conjectural for Otilde+(T_Co) itself (arithmetic-groups/otilde-plus-t-co.md:23-24). The three orbit counts are carried from sage-extensions'' proof and its computation, not from this database: `results/issue607-gamma-co-2-rows-by-the-polar-space.md` at commit 47865446a7c37c85d873f91ac9d74cea472e208c proves 4 line, 7 plane and 13 flag orbits, with 4 = 34560 + 17280 + 15360 + 256 lines, 7 = 26880 + 24576 + 8064 + 3360 + 2688 + 1120 + 768 planes and 13 flags, computed in GAP (`results/issue607-the-levi-candidate.log`, 3 s a row after 335 s of group construction), and its 4, 7, 13 agree with the public call''s own run record (sage-extensions#391, image run 43556671111: 4 line cusps, 7 plane cusps, 13 edges)'
---

Its three orbit counts are the ones sage-extensions proves and computes for it, and this database does not recompute them: `latticedb certify` presents a subgroup only through a card's `standard_name`, and $\Gamma_{\mathrm{Co},2}$ is not one of the eight standard subgroups, so the counts are carried from the record with its citation (`data.reference`) rather than minted here.
$\Gamma_{\mathrm{Co},2}$ has $4$ orbits of primitive isotropic lines, of sizes $34560$, $17280$, $15360$ and $256$; $7$ orbits of primitive isotropic planes, of sizes $26880$, $24576$, $8064$, $3360$, $2688$, $1120$ and $768$, over the $67456$ hyperbolic lines of $O(q)$; and $13$ orbits of isotropic flags (sage-extensions `results/issue607-gamma-co-2-rows-by-the-polar-space.md`, commit `47865446a7c37c85d873f91ac9d74cea472e208c`, whose GAP log is `results/issue607-the-levi-candidate.log`).
Those counts agree with the public call's own record of the row — $4$ line cusps, $7$ plane cusps and $13$ edges in sage-extensions#391's image run `43556671111` — which is the agreement that lets the record stand in for a computation of this card's field.
