---
tag: 6JRU
name: L_4
latex: L_{4}
aliases: [U + U + <-8>]
rank: 5
gram_tensor:
- [0, 1, 0, 0, 0]
- [1, 0, 0, 0, 0]
- [0, 0, 0, 1, 0]
- [0, 0, 1, 0, 0]
- [0, 0, 0, 0, -8]
signature: [2, 3]
determinant: -8
definiteness: indefinite
integral:
  parity: even
indefinite:
  isotropic: true
---

The lattice $L_{4} = U \oplus U \oplus \langle -8 \rangle$, in the basis $e_{1}, f_{1}, e_{2}, f_{2}$ of the two hyperbolic planes and $g$ of the last summand, with $b(e_{i}, f_{i}) = 1$ and $b(g, g) = -8$: rank $5$, signature $(2, 3)$, determinant $-8$, even.

No source states its counts of orbits of primitive isotropic lines or planes, so this card states none, and `latticedb certify` mints what the preamble returns for it: the Gram tensor above is the defining input, and every value it carries is a certificate's subject (`theory/orbits.md`).
