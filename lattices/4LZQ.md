---
tag: 4LZQ
name: Constructed lattice 4LZQ
latex: L_{\mathrm{4LZQ}}
certifications:
  derive: 04e02cd60b3697c95ad8a3e8a78c88046434ccb3946ab47b8684024bd27e3781
  form.integer_valued: 93667ff11f4c01914f332220af2828f835c92d6c9862c3c7119577658c0288d6
  integral.elementary_primes: 06a5b66bef4431a5cf7321224459286b81a3ae67c4f37c3971d21f51005a8a55
  integral.genus_symbol: 568f9dff5091378b44aa14b00909e9aac4d4c28960015511d0e187dfeee96818
  integral.genus_class_count: a8f7c5cc3608b555fe07052a55f4c83fbdab4bcd2c9b1be60fa0c4e53553056f
  integral.overlattice_count: f5f29a6f1ef4483edb1bab28ef7dc3a07e7479e5f82ab61c2d295704ab39e476
  integral.spinor_genus_count: fad1595de872ada9e4c023f38678ecae62c3ed57c279d35d39247e1beb670bba
  integral.spinor_genera: b50d3f4045e3744ea1706679ea02abfe52021e6270ecde651cf98be4e1a387f0
  integral.hyperbolic_index: 3f50d705029d0d37821516d0772378c9ade24ca5708c299cbda67b530a8b1bbb
  automorphisms.automorphism_group_generator_morphisms: 4a3bc37d48a4b2916b1da3b3636c4c5be7ecad8c4a340794d61a6830ff3985d6
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, -4, 2]
- [0, 0, 2, -4]
signature: [1, 3]
determinant: -24
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, -1/3, -1/6]
- [0, 0, -1/6, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  discriminant_group: [2, 2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  quadratic_character: -24
  genus_symbol: 'I_{1,3} (2: [1^-1 2^3]_4; 3: 1^-3 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7]
indefinite:
  isotropic: true
morphisms:
- target: 4LZQ
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, -1]
  scale: 1
- target: 4LZQ
  name: O(L) generator 2
  matrix:
  - [5, 4, 4, 4]
  - [-2, -1, -2, -2]
  - [-2, -2, -1, -2]
  - [-2, -2, -2, -1]
  scale: 1
- target: 4LZQ
  name: O(L) generator 3
  matrix:
  - [3, 4, 0, 0]
  - [-2, -3, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4LZQ
  name: O(L) generator 4
  matrix:
  - [3, 4, 0, 0]
  - [2, 3, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4LZQ
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 4LZQ
  name: O(L) generator 6
  matrix:
  - [7, 0, 12, 0]
  - [0, 1, 0, 0]
  - [-4, 0, -7, 0]
  - [-2, 0, -4, 1]
  scale: 1
- target: 4LZQ
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ID1.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ID1.
- tag: 3ID1
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ID1.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICX, 3ID1.
