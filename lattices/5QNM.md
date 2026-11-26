---
tag: 5QNM
name: Constructed lattice 5QNM
latex: L_{\mathrm{5QNM}}
certifications:
  derive: 0b06cb885317f5c772fcffd5d7bb7a56905d9147bed3807eeca83587fe871ce2
  form.integer_valued: 405ff06f7b134dce0682146b0abd8a3a65f0947c37ed284a1318aa0093a393c7
  integral.elementary_primes: c7d43b71fe834d266d3a05976901835142cc53cb39686c8f62981a47b46817be
  integral.genus_symbol: 287194969ef17c9a25931732084c19770cd7652be1aae118709ee1338246c8c4
  integral.genus_class_count: 71a7690acc3df4571b755d2a16ae13e5354bb1321345c2fc265aa2d44c06c02b
  integral.overlattice_count: 99963d570a67670bdffa406ed3c352787bfa311c30c5ca6bb01d6a2bca5714ed
  integral.spinor_genus_count: 139490ce2d0a6fec4a055fdcad619b6f7c52c70e762c1db24573e3a56cd8d0b9
  integral.spinor_genera: c5c1b1e47759ef13c16e6d46d0f6d2a2e24ce5cc16748c4a146b2086dca1cd5a
  integral.hyperbolic_index: 43bde982c33151eb04a7ff5928a93b7ac8c8a27c4d4520a8a37c851755b0c289
  automorphisms.automorphism_group_order: aac8d4a316615ae8f63e466bd038ea24cb59e1ea2a611d72803c8f23a39d101f
  automorphisms.automorphism_group_generator_morphisms: 4ee11fe9cfe0de23e27144d77ab96dd844793152d2cae08a87b92e72f4842ef7
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, -2, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, -2, 3]
- [0, 0, 0, 3, -6]
signature: [1, 4]
determinant: 24
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, -1/2, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, -2, -1]
- [0, 0, 0, -1, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  discriminant_group: [2, 2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'II_{1,4} (2: 1^-2 [2^3]_7; 3: 1^-4 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7]
indefinite:
  isotropic: true
morphisms:
- target: 5QNM
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5QNM
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5QNM
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5QNM
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5QNM
  name: O(L) generator 5
  matrix:
  - [3, 2, 2, 0, 0]
  - [-2, -1, -2, 0, 0]
  - [-2, -2, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5QNM
  name: O(L) generator 6
  matrix:
  - [3, 0, 2, 1, 0]
  - [0, 1, 0, 0, 0]
  - [-2, 0, -1, -1, 0]
  - [-4, 0, -4, -1, 0]
  - [-2, 0, -2, -1, 1]
  scale: 1
- target: 5QNM
  name: O(L) generator 7
  matrix:
  - [7, 0, 0, 0, 6]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-12, 0, 0, 1, -12]
  - [-8, 0, 0, 0, -7]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ICX, 3ID3.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ICX, 3ID3.
- tag: 3ID3
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ICX, 3ID3.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ICX, 3ICX, 3ID3.
