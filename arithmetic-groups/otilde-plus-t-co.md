---
slug: otilde-plus-t-co
name: Otilde+(T_Co)
latex: \widetilde O^{+}(T_{\mathrm{Co}})
lattice: 6JRR
ambient_lie_group: o-2-9
standard_name: Otilde+
parent_group: otilde-t-co
data:
  abstract_structure: Otilde(T_Co) intersect O+(T_Co)
  cardinality: aleph0
---

$\widetilde O^{+}(T_{\mathrm{Co}}) = \widetilde O(T_{\mathrm{Co}}) \cap O^{+}(T_{\mathrm{Co}})$, the subgroup of the discriminant kernel that also lies in the kernel of the real spinor norm (`theory/orbits.md`); the determinant-one subgroup is $SO(T_{\mathrm{Co}})$, which is a different subgroup, and the two are not interchanged here.
It is countably infinite and of finite index in $O(T_{\mathrm{Co}})$; whether its index in $\widetilde O(T_{\mathrm{Co}})$ is $2$ is a value the computation below states when it returns, not an assumption of this card.

`latticedb certify` asks the preamble for its index in $O(T_{\mathrm{Co}})$ and for the isometries of $T_{\mathrm{Co}}$ that generate it, at `L.stable_orthogonal_group().intersection(L.O_plus())`, and stores them as `data.index_in_orthogonal_group` and `data.generator_morphisms`, the generators as scale-$1$ `morphisms` entries of the card of [6JRR](../tag/6JRR.html).
The two values are certified on that card under `arithmetic-group.otilde-plus-t-co.index_in_orthogonal_group` and `arithmetic-group.otilde-plus-t-co.generator_morphisms`; a value that computation has not returned is absent.

That this subgroup is the group $\Gamma_{\mathrm{Co}}$ acting on the Coble period domain is **conjectural**.
Dolgachev–Kondo, Proposition 3.2, p. 513, identifies the moduli space of Coble surfaces with an open subset of $\mathcal{D}(N)/O(N)$ and does not name the subgroup of $O(N)$ that acts; the identification $\Gamma_{\mathrm{Co}} = \widetilde O^{+}(T_{\mathrm{Co}})$ belongs to the family group of the research project, not to this database, and no count on the card of 6JRR rests on it.
