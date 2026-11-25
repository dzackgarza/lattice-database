---
tag: 6BZB
name: Constructed lattice 6BZB
latex: L_{\mathrm{6BZB}}
certifications:
  derive: a1e8d13798deedbe1e1f78b6f3f2222c0310447a67539224a5e4041f1cd997ff
  form.integer_valued: b61953403c4a8ffff6d4c8712b29dac66506e690a953f84442f1d2a4a406f81f
  integral.elementary_primes: 47882038967850aa2758eafd5b442daf414bfc12141567420adbac70d977b885
  integral.genus_symbol: fc8d91aa37f3b04812b8d452b1041ebae0b07feb4415c8e03942ef883e5e49da
  integral.genus_class_count: 430b8dbffc4f9856e83234b376764354ddee5bc33de405a0a8541ff43350dcbc
  integral.overlattice_count: 750082f739a5e7249b660796ece436be67586594d7b015e9874f47b0e141cdd0
  integral.spinor_genus_count: d177b89331da0a4bc53f7ef674fc7453b5950f180d5ee1b896d56016e6875da9
  integral.spinor_genera: f6ffdb4ecfc7c3871ecb848e505b6ebd5dbb896d61070a61369092c5fb9b6b3e
  integral.hyperbolic_index: b8f27fd48b2d1ab48114716ba55ea5492ea604179b50f4323e49a481aa99b16d
  automorphisms.automorphism_group_generator_morphisms: dc7b3f20e9d82e5b500202facaea19503930a45b0652a03dcb8138ac14f4d2bc
  integral.discriminant_form: 480ff919f24c655866f093109b8cbc7d80ce78e1fe946c406a80351f6849a3a4
  automorphisms.automorphism_group_order: 053d5f7b096daaa80425b7935caccd0bddaa47d739b11b8f63022b1a057b37e4
  integral.discriminant_orbits: 215a91336848a61bf747a42ff4bd95116699e682b5b65c94f60571991e44e089
  integral.modular_scale: a012bd8f98022f80f6510b4c258e9c8d3e38ea2ab01b81b4681b9eca20f700eb
  integral.anisotropic_primes: 725c31c036ee34669756e1fff7516c0deb53921b28640283d34dc06cd66969d3
  integral.local_representations: e3fbaf64aedeb23977577acb7ea4be410cafe6e88f00306849b7e4b8e2833156
  integral.local_densities: 448b10758321645e8f13ba7e4658d15ea2b8ebe01e7edffcfde07f7108404102
rank: 4
gram_tensor:
- [0, 2, 0, 0]
- [2, 0, 0, 0]
- [0, 0, 0, 2]
- [0, 0, 2, 0]
signature: [2, 2]
determinant: 16
definiteness: indefinite
dual_gram_tensor:
- [0, 1/2, 0, 0]
- [1/2, 0, 0, 0]
- [0, 0, 0, 1/2]
- [0, 0, 1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 2
  modular_scale: 4
  discriminant_group: [2, 2, 2, 2]
  overlattice_count: 31
  delta: 0
  bad_reduction_primes: [2]
  quadratic_character: 1
  genus_symbol: 'II_{2,2} (2: 2^4)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  discriminant_form:
    orthogonal_group_order: 72
    isotropic_classes: 10
    isotropic_orbits: 2
  discriminant_orbits:
    Otilde:
      constant: 10
      z: [0, 1, 0, 7]
      w: [0, 1, 0, 7]
    SOtilde:
      constant: 10
      z: [0, 1, 0, 7]
      w: [0, 1, 0, 7]
    Otilde+:
      constant: 10
      z: [0, 1, 0, 7]
      w: [0, 1, 0, 7]
    SOtilde+:
      constant: 10
      z: [0, 1, 0, 7]
      w: [0, 1, 0, 7]
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
    densities: [0, 0, 0, 3, 0, 0, 0, 9/2, 0, 0, 0, 3]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 8, O(L) generator 6, 'O(L) generator 5 #2', O(L) generator 4, 'O(L) generator 7 #2', O(L) generator 3, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, 'O(L) generator 14 #2']
indefinite:
  isotropic: true
morphisms:
- target: 6BZB
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6BZB
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6BZB
  name: O(L) generator 3
  matrix:
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  scale: 1
- target: 6BZB
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 1]
  - [-1, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6BZB
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 1]
  - [0, 1, 0, 0]
  - [0, -1, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6BZB
  name: O(L) generator 6
  matrix:
  - [1, 0, 1, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, -1, 0, 1]
  scale: 1
- target: 6BZB
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 2, 0]
  - [0, 0, 1, 0]
  - [-2, 0, 0, 1]
  scale: 1
- target: 6BZB
  name: O(L) generator 8
  matrix:
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  scale: 1
- target: 6BZB
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 6BZB
  name: O(L) generator 10
  matrix:
  - [0, 1, 0, -1]
  - [1, 0, 0, 1]
  - [1, -1, 1, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 6BZB
  name: O(L) generator 11
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6BZB
  name: O(L) generator 12
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6BZB
  name: O(L) generator 13
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6BZB
  name: O(L) generator 14
  matrix:
  - [1, -1, 1, 1]
  - [0, 0, 1, 0]
  - [0, 1, -1, 0]
  - [1, 0, 1, 0]
  scale: 1
- target: 6BZB
  name: 'O(L) generator 5 #2'
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 1, 0]
  - [0, 0, 1, 0]
  - [-1, 0, 0, 1]
  scale: 1
- target: 6BZB
  name: 'O(L) generator 7 #2'
  matrix:
  - [1, 0, 0, 2]
  - [0, 1, 0, 0]
  - [0, -2, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6BZB
  name: 'O(L) generator 14 #2'
  matrix:
  - [1, -1, 1, 1]
  - [0, 0, 1, 0]
  - [-1, 0, -1, 0]
  - [0, -1, 1, 0]
  scale: 1
related:
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0013, 0013.
---

The selected Gram tensor is obtained by orthogonal sum of 0013, 0013.
