---
slug: otilde-t-co
name: Otilde(T_Co)
latex: \widetilde O(T_{\mathrm{Co}})
lattice: 6JRR
ambient_lie_group: o-2-9
standard_name: Otilde
data:
  abstract_structure: the kernel of O(T_Co) -> O(A_T_Co)
  cardinality: aleph0
  index_in_orthogonal_group: 46998591897600
  generator_morphisms: [Otilde(T_Co) generator 1, Otilde(T_Co) generator 2, Otilde(T_Co) generator 3, Otilde(T_Co) generator 4, Otilde(T_Co) generator 5, Otilde(T_Co) generator 6, Otilde(T_Co) generator 7, Otilde(T_Co) generator 8, Otilde(T_Co) generator 9, Otilde(T_Co) generator 10, Otilde(T_Co) generator 11, Otilde(T_Co) generator 12, Otilde(T_Co) generator 13, Otilde(T_Co) generator 14, Otilde(T_Co) generator 15, Otilde(T_Co) generator 16, Otilde(T_Co) generator 17, Otilde(T_Co) generator 18, Otilde(T_Co) generator 19, Otilde(T_Co) generator 20, Otilde(T_Co) generator 21, Otilde(T_Co) generator 22, Otilde(T_Co) generator 23, Otilde(T_Co) generator 24, Otilde(T_Co) generator 25, Otilde(T_Co) generator 26, Otilde(T_Co) generator 27, Otilde(T_Co) generator 28, Otilde(T_Co) generator 29, Otilde(T_Co) generator 30, Otilde(T_Co) generator 31, Otilde(T_Co) generator 32, Otilde(T_Co) generator 33, Otilde(T_Co) generator 34, Otilde(T_Co) generator 35, Otilde(T_Co) generator 36, Otilde(T_Co) generator 37, Otilde(T_Co) generator 38, Otilde(T_Co) generator 39, Otilde(T_Co) generator 40, Otilde(T_Co) generator 41, Otilde(T_Co) generator 42, Otilde(T_Co) generator 43, Otilde(T_Co) generator 44, Otilde(T_Co) generator 45, Otilde(T_Co) generator 46, Otilde(T_Co) generator 47, Otilde(T_Co) generator 48, Otilde(T_Co) generator 49, Otilde(T_Co) generator 50, Otilde(T_Co) generator 51, Otilde(T_Co) generator 52, Otilde(T_Co) generator 53, Otilde(T_Co) generator 54, Otilde(T_Co) generator 55, Otilde(T_Co) generator 56]
  line_orbits: 527
  plane_orbits: 189720
  flag_orbits: 569160
  reference:
    citation: 'sage-extensions `main` 47865446a7c37c85d873f91ac9d74cea472e208c, `results/issue286-the-stage-1-call.md`:372: 569160 edges over 527 line cusps and 189720 plane cusps for `Otilde(T_Co) = ker rho`. The citation covers the three orbit counts only; the index and the generators are computations about the card of 6JRR''s Gram tensor and are certified there.'
---

The discriminant kernel of $O(T_{\mathrm{Co}})$, the kernel of the reduction $\varphi \colon O(L) \to O(A_L)$ of Dolgachev–Kondo, Section 2, (2.1), p. 510, written $\widetilde O(L) = O(L)^{*}$ there; it is a subgroup of $O(L_{\mathbb{R}}) \cong O(2, 9)$ and is countably infinite, being an infinite subgroup of finite index.

`latticedb certify` asks the preamble for its index in $O(T_{\mathrm{Co}})$, the cardinality of $O(L)/\widetilde O(L)$, which is $|O(A_{T_{\mathrm{Co}}}, q)|$, and for the isometries of $T_{\mathrm{Co}}$ that generate it, at `L.stable_orthogonal_group()`.
The index is stored as `data.index_in_orthogonal_group` and the generators as `data.generator_morphisms`; each generator is one `morphisms` entry of the card of [6JRR](../tag/6JRR.html) with `scale: 1`, stored once, and the two values are certified on that card under `arithmetic-group.otilde-t-co.index_in_orthogonal_group` and `arithmetic-group.otilde-t-co.generator_morphisms`.
The index the computation returned is $46998591897600 = |O(A_{T_{\mathrm{Co}}}, q)|$, the order of the finite orthogonal group of the discriminant form — the finite image of $\varphi$ — read from that finite group rather than from its coset space, whose cardinality is the same number.
The **56 ordinary integral generators** are now stored as named self-isometries of [6JRR](../tag/6JRR.html), with `data.generator_morphisms` listing those names. Their exact source-hashed matrix certificate is `research/computations/reports/coble_kernel_fifty_six_congruence_generators.json` (research theorem `thm:coble-fifty-six-ordinary-full-kernel-generation`, commit `99f7680924`); the proof uses the canonical even neighbor, explicit Eichler generators, exact congruence quotients, and the Spin congruence subgroup property. All 56 matrices were independently accepted by the public `NamedLattices.Tco.stable_orthogonal_group()` predicate. The index and generator values are certified separately on the lattice card. Earlier exhaustive Schreier enumeration of 46,998,591,897,600 cosets timed out, but is unnecessary for this explicit finite generating family.

Its three orbit counts are cited, not computed: the record `results/issue286-the-stage-1-call.md` at `47865446a7c37c85d873f91ac9d74cea472e208c`:372 gives this subgroup 527 line cusps, 189720 plane cusps and 569160 incidence edges, and `data.reference` names it. `latticedb certify` can compute the counts for a standard subgroup; the record is what states them here, and a computed value that disagreed with it would be a defect on the record rather than a replacement for it.
