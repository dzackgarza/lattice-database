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
  automorphisms.automorphism_group_generator_morphisms: 4430343d2e27d3dbd7287991c5dea70c7fc363dd2dfe622cdba97656a5cd857f
  integral.discriminant_form: fa089b3fba6352fafd743e330ba88da4ba0cbe9f4c732a179b885cac733e6f9e
  automorphisms.automorphism_group_order: 2ed35e78d6fb233b02029773ba727bb99eb0d859e958dfad40045cf4efdd8f89
  integral.discriminant_orbits: e4dc64ba8c45225f1dba62183ae92fceaacaac5632db27a39c7f1eed17f66aa3
  integral.modular_scale: f4ff0174b4c999884452330b73c4df07d4e6bd1cef8875eec4b7b9acf185caa3
  integral.anisotropic_primes: b1ff5ba712b89ddbc3d5c674542ff6486ff2d0c2c656323e1410da3142565eda
  integral.local_representations: 6399eabb4897a015ac227e18fa152903d545496de7e51da1969c71cb96c84aeb
  integral.local_densities: 960b5bb91994007dae9544b19b10b1b4e78d12521a23eb5acc49f8a044ff74a2
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
  modular_scale: false
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
  discriminant_orbits:
    Otilde:
      constant: 6
      z: [0, 1, 0, 11]
      w: [0, 1, 0, 11]
    SOtilde:
      constant: 6
      z: [0, 1, 0, 11]
      w: [0, 1, 0, 11]
    Otilde+:
      constant: 6
      z: [0, 1, 0, 11]
      w: [0, 1, 0, 11]
    SOtilde+:
      constant: 6
      z: [0, 1, 0, 11]
      w: [0, 1, 0, 11]
    O:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    SO:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    O+:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    SO+:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 3
      least_valuation: 2
    - representative: 5
      least_valuation: 2
    - representative: 7
      least_valuation: 2
    - representative: 2
      least_valuation: 3
    - representative: 6
      least_valuation: 3
    - representative: 10
      least_valuation: 3
    - representative: 14
      least_valuation: 3
  local_densities:
  - prime: 2
    densities: [0, 0, 0, 5, 0, 0, 0, 5/2, 0, 0, 0, 5]
  - prime: 3
    densities: [4/3, 2/3, 10/9, 4/3, 2/3, 8/9, 4/3, 2/3, 28/27, 4/3, 2/3, 10/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, 'O(L) generator 3 #2', 'O(L) generator 4 #2', O(L) generator 5]
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
- target: 6EXB
  name: 'O(L) generator 3 #2'
  matrix:
  - [1, 0, 0, 0]
  - [1, 1, 1, -3]
  - [1, 0, 2, -3]
  - [1, 0, 1, -2]
  scale: 1
- target: 6EXB
  name: 'O(L) generator 4 #2'
  matrix:
  - [1, 1, 1, -3]
  - [1, 1, 2, -3]
  - [2, 1, 3, -6]
  - [1, 1, 2, -4]
  scale: 1
related:
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 3ICZ, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 3ICZ, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICZ, 3ID6.
