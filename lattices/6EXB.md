---
tag: 6EXB
name: Constructed lattice 6EXB
latex: L_{\mathrm{6EXB}}
certifications:
  derive: 08831f21afd1c4e5f0d6fa2794cdc4450657c64171441bec3f16f51399068197
  form.integer_valued: 04cf5053d898b675fe9164390e21fe29e3fb788dea86829f86dbabdd6163a10c
  integral.elementary_primes: df7b2c42e29c060399167ec5cca775fca09044b8d2adbc1a8b3ec8564048cbed
  integral.genus_symbol: c44502461af7508dddb9ae58439d7ef314c2045f01e55755d81cbccfb63e6a1c
  integral.genus_class_count: 2558cb53bbcbedf54e7b92eb41229d7e901f30b2c89ffe1c29d7bf911cba7fc9
  integral.overlattice_count: 98f4cac0596a3b027fd9eeaf2cc2ae9d525de4c9ad60e8a102d7a2f43017be21
  integral.spinor_genus_count: f5fa12816ad84cb9bb720c5a9c0c61714a678cec8677e6826145758ddc0601d5
  integral.spinor_genera: 5fe6441d35e3814adc9a5cc365e54aaff868693e8ae642b927c633c4dfb06cf7
  integral.hyperbolic_index: 4858ed13bd5e7fb724bb6ddae75849e23b1bc0f53298945f39161bfc51cb356a
  automorphisms.automorphism_group_generator_morphisms: a1a8b6b7a01de9bf70e57fca0b216ffb67191d0116bd89a405cc3cc53abf13ac
  integral.discriminant_form: fa089b3fba6352fafd743e330ba88da4ba0cbe9f4c732a179b885cac733e6f9e
rank: 4
gram_tensor:
- [0, -2, 0, 0]
- [-2, 0, 0, 0]
- [0, 0, 4, -6]
- [0, 0, -6, 12]
signature: [3, 1]
determinant: -48
definiteness: indefinite
dual_gram_tensor:
- [0, -1/2, 0, 0]
- [-1/2, 0, 0, 0]
- [0, 0, 1, 1/2]
- [0, 0, 1/2, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 6
  discriminant_group: [2, 2, 2, 6]
  overlattice_count: 31
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{3,1} (2: 2^-4; 3: 1^-3 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  discriminant_form:
    orthogonal_group_order: 240
    isotropic_classes: 6
    isotropic_orbits: 2
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 6EXB
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, -1, 1]
  scale: 1
- target: 6EXB
  name: O(L) generator 2
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6EXB
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [1, 1, -1, 3]
  - [-1, 0, 2, -3]
  - [-1, 0, 1, -2]
  scale: 1
- target: 6EXB
  name: O(L) generator 4
  matrix:
  - [1, 1, -1, 3]
  - [1, 1, -2, 3]
  - [-2, -1, 3, -6]
  - [-1, -1, 2, -4]
  scale: 1
- target: 6EXB
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 3ICZ, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 3ICZ, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICZ, 3ID6.
