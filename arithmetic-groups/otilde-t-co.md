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
---

The discriminant kernel of $O(T_{\mathrm{Co}})$, the kernel of the reduction $\varphi \colon O(L) \to O(A_L)$ of Dolgachev–Kondo, Section 2, (2.1), p. 510, written $\widetilde O(L) = O(L)^{*}$ there; it is a subgroup of $O(L_{\mathbb{R}}) \cong O(2, 9)$ and is countably infinite, being an infinite subgroup of finite index.

`latticedb certify` asks the preamble for its index in $O(T_{\mathrm{Co}})$, the cardinality of $O(L)/\widetilde O(L)$, which is $|O(A_{T_{\mathrm{Co}}}, q)|$, and for the isometries of $T_{\mathrm{Co}}$ that generate it, at `L.stable_orthogonal_group()`.
The index is stored as `data.index_in_orthogonal_group` and the generators as `data.generator_morphisms`; each generator is one `morphisms` entry of the card of [6JRR](../tag/6JRR.html) with `scale: 1`, stored once, and the two values are certified on that card under `arithmetic-group.otilde-t-co.index_in_orthogonal_group` and `arithmetic-group.otilde-t-co.generator_morphisms`.
A value that computation has not returned is absent from this card, and no page supplies it.
