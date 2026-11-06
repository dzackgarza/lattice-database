---
tag: 6JRR
name: T_Co
latex: T_{\mathrm{Co}}
aliases: [Coble lattice]
rank: 11
gram_tensor:
- [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
- [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [0, 0, 0, -4, 0, 2, 0, 0, 0, 0, 0]
- [0, 0, 0, 0, -4, 0, 2, 0, 0, 0, 0]
- [0, 0, 0, 2, 0, -4, 2, 0, 0, 0, 0]
- [0, 0, 0, 0, 2, 2, -4, 2, 0, 0, 0]
- [0, 0, 0, 0, 0, 0, 2, -4, 2, 0, 0]
- [0, 0, 0, 0, 0, 0, 0, 2, -4, 2, 0]
- [0, 0, 0, 0, 0, 0, 0, 0, 2, -4, 2]
- [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, -4]
signature: [2, 9]
determinant: -2048
definiteness: indefinite
integral:
  parity: even
indefinite:
  isotropic: true
arithmetic_groups: [otilde-t-co, otilde-plus-t-co]
---


The Coble lattice $T_{\mathrm{Co}} = \langle 2 \rangle \oplus U(2) \oplus E_8(-2)$, in the basis $e_{0}$ of the first summand, $e_{1}, f_{1}$ of $U(2)$ with $b(e_{1}, f_{1}) = 2$, and the simple roots of $E_{8}(-2)$: rank $11$, signature $(2, 9)$, determinant $-2048$, even.

$T_{\mathrm{Co}}$ is twice the odd unimodular lattice $I_{2,9} = \langle 1 \rangle \oplus U \oplus E_{8}(-1)$, so $T_{\mathrm{Co}} \cong I_{2,9}(2)$; $b(e_{1}, e_{1}) = 0$, so it is isotropic.
Its discriminant group is $A_{T_{\mathrm{Co}}} = (T_{\mathrm{Co}})^{*}/T_{\mathrm{Co}}$, of order $2048$.
The groups studied with it are the discriminant kernel $\widetilde O(T_{\mathrm{Co}})$ and $\Gamma_{\mathrm{Co}} = \widetilde O^{+}(T_{\mathrm{Co}})$, which have their own arithmetic-group cards `otilde-t-co` and `otilde-plus-t-co`.

No invariant of this card is transcribed from a source: `latticedb certify` computes each from the Gram tensor above and certifies it, so the fields it mints are absent until that computation runs, and `integral.primitive_orbits` is absent in particular.
Its constant term is the number of $\Gamma$-orbits of primitive isotropic lines, the $0$-cusps of the Baily–Borel boundary, and not a count of vectors (`theory/orbits.md`); the preamble operation that returns it for an indefinite lattice does not return it yet.
