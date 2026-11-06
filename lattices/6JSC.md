---
tag: 6JSC
name: U(2) + <-2> + <-2> + <-2> + <-2> + <-2> + <-2>
latex: U(2) \oplus \langle -2 \rangle \oplus \langle -2 \rangle \oplus \langle -2 \rangle \oplus \langle -2 \rangle \oplus \langle -2 \rangle \oplus \langle -2 \rangle
aliases:
- (r, a, delta) = (8, 8, 1)
rank: 8
gram_tensor:
- - 0
  - 2
  - 0
  - 0
  - 0
  - 0
  - 0
  - 0
- - 2
  - 0
  - 0
  - 0
  - 0
  - 0
  - 0
  - 0
- - 0
  - 0
  - -2
  - 0
  - 0
  - 0
  - 0
  - 0
- - 0
  - 0
  - 0
  - -2
  - 0
  - 0
  - 0
  - 0
- - 0
  - 0
  - 0
  - 0
  - -2
  - 0
  - 0
  - 0
- - 0
  - 0
  - 0
  - 0
  - 0
  - -2
  - 0
  - 0
- - 0
  - 0
  - 0
  - 0
  - 0
  - 0
  - -2
  - 0
- - 0
  - 0
  - 0
  - 0
  - 0
  - 0
  - 0
  - -2
signature:
- 1
- 7
determinant: -256
definiteness: indefinite
integral:
  parity: even
  discriminant_group:
  - 2
  - 2
  - 2
  - 2
  - 2
  - 2
  - 2
  - 2
  delta: 1
indefinite:
  isotropic: true
families:
- nikulin-two-elementary
related:
- tag: 028P
  relation: The same lattice as $\langle 2 \rangle \oplus \langle -2 \rangle^{7}$, by Theorem 3.6.2, p. 144.
references:
- citation: Yu. I. Nikulin, "Integral symmetric bilinear forms and some of their applications", Math. USSR Izvestija 14 (1980), Theorem 3.6.2, p. 144 (PDF page 43); the summands' discriminant forms are those of §3.6
---

The even hyperbolic 2-elementary lattice of invariants $(r, a, \delta) = (8, 8, 1)$: rank $8$, signature $(1, 7)$, discriminant group $(\mathbb{Z}/2)^{8}$, $\delta = 1$.

The Gram matrix is the orthogonal sum $U(2) \oplus \langle -2 \rangle^{6}$ in the displayed basis, seven summands: $a = 2 + 6$, and $\delta = 1$ because $\delta(U(2)) = \delta(\langle -2 \rangle) = 1$. The orthogonal sum $\langle 2 \rangle \oplus \langle -2 \rangle^{7}$ has the same invariants, and Nikulin's Theorem 3.6.2, p. 144, states that for $t_+, t_- > 0$ the invariants determine the isomorphism class, so the two presentations are one lattice; the other one is the record [028P](../tag/028P.html).
