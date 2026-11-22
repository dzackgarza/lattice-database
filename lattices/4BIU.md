---
tag: 4BIU
name: Constructed lattice 4BIU
latex: L_{\mathrm{4BIU}}
certifications:
  derive: 6576267843932d2ab46f458cdb47afa7f9e735e818b05abdeafc2d48ff3b9590
  form.integer_valued: 99786cfe134a83437071564533371f23f12cc3ae13ca0e6a46dbd16c27b776ab
  integral.elementary_primes: f9b4d80120942680043e5151692236a278a88551b045ea5d33ab5202fab7d7d8
  integral.genus_symbol: 84d85823ffee8c8395d49b37b8ffb969c00fbfb2076ee26d4214e5d38147f242
  integral.genus_class_count: 4ecd6afbb9aea5221e9073f26a9d97dea5b3f8c663d0c32ee763164c54e99487
  integral.overlattice_count: fe96d2fc4a2ec3ec5491fb7396f4eb5fdd4ae39a6a3e8135ace78fc6a9606a76
  integral.spinor_genus_count: f7c9c99797fe1abc3cd485498cac5df1998fd2c37313864f447a0c655324bafc
  integral.spinor_genera: 8a29865f902b8060f7a09c1337b1fd52b98689ef21dc4ea3edcf7402f48cb177
  automorphisms.automorphism_group_order: 00f2e491d7b4238f14d0c25f72a4826b6cf002d12eb7a219929f02fe721fa97f
  automorphisms.automorphism_group_generator_morphisms: 3ed5c4c02216ffd240e2b3e8bf5fb424f99d9a27df1700f54c4e13a49098d423
  integral.primitive_orbits: fec587bbf17b993fe64ba2fdc8706cb895d024ddb0b76c0e8125c71a93c9aa22
  integral.modular_scale: 89ed44b278d36559ec4d5a785d735350fceeb3c2c0af39fceca7c327eaed4637
  integral.anisotropic_primes: 2a3f03508e7c1d1801ff9faaf6c12fe17f755cb2951bcd8e37943624c8074545
  integral.local_representations: 058cad20adf9d3203d2693f9ccd38856a883dbd9be07acddcee0aac45589f108
  integral.local_densities: 7631802495dbb1adb2fa1df9d48ac6f9c0b47dd21429d20ba61d14f2150c4397
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 4, -2, 0]
- [0, 0, -2, 4, -2]
- [0, 0, 0, -2, 4]
signature: [4, 1]
determinant: -32
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 3/8, 1/4, 1/8]
- [0, 0, 1/4, 1/2, 1/4]
- [0, 0, 1/8, 1/4, 3/8]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 16
  modular_scale: false
  discriminant_group: [2, 2, 8]
  overlattice_count: 11
  bad_reduction_primes: [2]
  genus_symbol: 'I_{4,1} (2: [1^-2]_4 2^2:[8^-1]_3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  primitive_orbits:
    O:
      constant: 2
      z: []
      w: []
    O+:
      constant: 2
      z: []
      w: []
    SO:
      constant: 2
      z: []
      w: []
    SO+:
      constant: 2
      z: []
      w: []
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 0
    - representative: 5
      least_valuation: 0
    - representative: 7
      least_valuation: 0
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
    densities: [1, 0, 1, 5/2, 1, 0, 1, 25/16]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16]
indefinite:
  isotropic: true
morphisms:
- target: 4BIU
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4BIU
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 1, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4BIU
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4BIU
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 5, 8, 0, 0]
  - [0, -3, -5, 0, 0]
  - [0, -2, -4, 1, 0]
  - [0, -1, -2, 0, 1]
  scale: 1
- target: 4BIU
  name: O(L) generator 5
  matrix:
  - [-1, 2, 4, -2, 0]
  - [-2, 3, 4, -2, 0]
  - [1, -1, -1, 1, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4BIU
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4BIU
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  - [0, 0, 1, 0, 0]
  scale: 1
- target: 4BIU
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 3, 0, 4, 0]
  - [0, -1, 1, -2, 0]
  - [0, -2, 0, -3, 0]
  - [0, -1, 0, -2, 1]
  scale: 1
- target: 4BIU
  name: O(L) generator 9
  matrix:
  - [-7, 12, 16, 0, 0]
  - [-12, 19, 24, 0, 0]
  - [6, -9, -11, 0, 0]
  - [4, -6, -8, 1, 0]
  - [2, -3, -4, 0, 1]
  scale: 1
- target: 4BIU
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4BIU
  name: O(L) generator 11
  matrix:
  - [-1, 2, 2, 2, -2]
  - [-2, 3, 2, 2, -2]
  - [1, -1, 0, -1, 1]
  - [1, -1, 0, -1, 0]
  - [1, -1, -1, 0, 0]
  scale: 1
- target: 4BIU
  name: O(L) generator 12
  matrix:
  - [-1, 6, 4, 6, 0]
  - [-2, 9, 4, 10, 0]
  - [1, -4, -1, -5, 0]
  - [1, -3, -1, -4, 1]
  - [1, -2, -1, -2, 0]
  scale: 1
- target: 4BIU
  name: O(L) generator 13
  matrix:
  - [-1, 6, 10, -6, 6]
  - [-2, 13, 22, -10, 10]
  - [1, -7, -12, 5, -5]
  - [0, -4, -7, 3, -3]
  - [0, -2, -3, 1, -2]
  scale: 1
- target: 4BIU
  name: O(L) generator 14
  matrix:
  - [-1, 2, 2, 0, 2]
  - [-2, 3, 2, 0, 2]
  - [-1, 1, 1, 0, 0]
  - [0, 0, 1, 0, -1]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4BIU
  name: O(L) generator 15
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 1, 0, -1]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4BIU
  name: O(L) generator 16
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID9.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID9.
- tag: 3ID9
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID9.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICW, 3ID9.
