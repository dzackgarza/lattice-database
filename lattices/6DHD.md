---
tag: 6DHD
name: Constructed lattice 6DHD
latex: L_{\mathrm{6DHD}}
certifications:
  derive: eccd2f61b70f2a744fb1592f3d669031bb18a51b500fa493393b3ceb8c4c4f63
  form.integer_valued: b0b16fbf485830672928db9ab67f991cc3881e0bb6487108e69f395fb0e1ac3f
  integral.elementary_primes: 298e7f41ffa27033db7863b3d9fe9f5022e2fa914dddacb600982cbcd0a58a9f
  integral.genus_symbol: 5335ca3279ce24443449f5c10056f5ed36b2c37ee915a4689aa7f45091c490c2
  integral.genus_class_count: 9c7aa4a9e6837e10b8795c7e7133dadd393ff7c76a794bce1bef302e9139f52f
  integral.overlattice_count: f6c6558d037cad1f0cccbfa0e36c851398cde8939b7041eac3cd90d66cff7485
  integral.spinor_genus_count: 5d2e99ea9d0600e6f11fda6e8ca09e9f43653e0cf57e4c7eacf1c88be3c4246f
  integral.spinor_genera: a354ac0bc90bda8c66f9567d12e115a693658eee0990cec783511c47b2a8de9c
  integral.hyperbolic_index: 74ab93ae5f042ea59d0ea919a39e4455ef63d440b9e79681a3715084e12fe444
  automorphisms.automorphism_group_generator_morphisms: 573e6c3601fa2426368c02f451d33d3e9238147040c3981a3f93261bf772a7d7
  integral.discriminant_form: d7eb76a76056fadd6d42d2a05e406e2f0317a009ab5756582382f2c1f7e4f86e
rank: 4
gram_tensor:
- [0, 2, 0, 0]
- [2, 0, 0, 0]
- [0, 0, -4, 6]
- [0, 0, 6, -12]
signature: [1, 3]
determinant: -48
definiteness: indefinite
dual_gram_tensor:
- [0, 1/2, 0, 0]
- [1/2, 0, 0, 0]
- [0, 0, -1, -1/2]
- [0, 0, -1/2, -1/3]
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
  genus_symbol: 'II_{1,3} (2: 2^-4; 3: 1^3 3^-1)'
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
- target: 6DHD
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 2, -3]
  - [0, 0, 1, -2]
  scale: 1
- target: 6DHD
  name: O(L) generator 2
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6DHD
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [1, 1, -1, 0]
  - [2, 0, -1, 0]
  - [1, 0, -1, 1]
  scale: 1
- target: 6DHD
  name: O(L) generator 4
  matrix:
  - [1, 1, -1, 0]
  - [1, 1, -2, 3]
  - [1, 2, -3, 3]
  - [1, 1, -2, 2]
  scale: 1
- target: 6DHD
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0013, 3ID5.
- tag: 3ID5
  relation: This presentation is obtained by orthogonal sum of 0013, 3ID5.
---

The selected Gram tensor is obtained by orthogonal sum of 0013, 3ID5.
