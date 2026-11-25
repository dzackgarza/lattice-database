---
tag: 5SYI
name: Constructed lattice 5SYI
latex: L_{\mathrm{5SYI}}
certifications:
  derive: f4b41e9a7a37158c0154390d5e71734dfc5941672001d9325ca9cb0b362f5377
  form.integer_valued: 6ece7a9cef224b8b448ba371cc0f5113c7b985214a4c9fd9a17cc08e9404487a
  integral.elementary_primes: 933eed66278615113df9b1e46634bf74d04d8c7b252bbc0c04d934d9cba9b149
  integral.genus_symbol: d0844f27487705f76e05a99408404aa093c698798520d12fbb5087a31a79eed6
  integral.genus_class_count: 1cd9b4bfcdd9ac2c496dafc14bbe19b334b0bdb13cfdd0be2b01e38417ad9647
  integral.overlattice_count: b184bae662a76c2a11a801876a69369072e16924b06fe8f53bee2b7db4f721c9
  integral.spinor_genus_count: f9fba254722e357fd3fbf85fbf716b59337e1e2e4878fd769516cb473e65bab4
  integral.spinor_genera: 00686d5d56b33db66244aa4f5847ef10aa2bc8e002eb3b843b54dcd4dce1d3b7
  integral.hyperbolic_index: 95638665fc53f1b048d179a5c3ca13a275825bd7c28a152702aba1c252db2495
  automorphisms.automorphism_group_generator_morphisms: 7e1b9c2cef3dd5c9a34c6bb6f0aa40b4480d0ff76a4f2739ed47a7bd27b6debb
  integral.discriminant_form: cd23c2734903b34a1b27783984d1df6d039fa005c04001e28783c62592d3b25f
  automorphisms.automorphism_group_order: 9af6b872b7ac050ba29ac99e646befb2685be17d5c45afa8ea0540b1083f4724
  integral.discriminant_orbits: c9ecd775b28df2bba3ae3c8a74cb6cbc5161fee3f55ebce771baecce8c395e15
  integral.modular_scale: e5dd7f2c9a2d09cba085b29ef1c566d34d89226c9eee4cb3a69824c131336bba
  integral.anisotropic_primes: e93cd0b4465e23cd407677925daf3eb8c86b304b11063c1b2aae1ddf05af6b9c
  integral.local_representations: 2ec63ee113928dcd280efb4d527bb05009344dbced0a0c2aa06cd577b55f23f4
  integral.local_densities: 94bab8265d7cd795e1f33dba6888757eb31f8c560eeb319411e1f2d0d669a30f
rank: 4
gram_tensor:
- [2, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, 4, -2]
- [0, 0, -2, 4]
signature: [3, 1]
determinant: -48
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, 1/3, 1/6]
- [0, 0, 1/6, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  modular_scale: false
  discriminant_group: [2, 2, 2, 6]
  overlattice_count: 11
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{3,1} (2: [2^-4]_0; 3: 1^-3 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  discriminant_form:
    orthogonal_group_order: 48
    isotropic_classes: 2
    isotropic_orbits: 2
  discriminant_orbits:
    Otilde:
      constant: 2
      z: [0, 5, 0, 7]
      w: [0, 5, 0, 7]
    SOtilde:
      constant: 2
      z: [0, 5, 0, 7]
      w: [0, 5, 0, 7]
    Otilde+:
      constant: 2
      z: [0, 5, 0, 7]
      w: [0, 5, 0, 7]
    SOtilde+:
      constant: 2
      z: [0, 5, 0, 7]
      w: [0, 5, 0, 7]
    O:
      constant: 2
      z: [0, 2, 0, 2]
      w: [0, 2, 0, 2]
    SO:
      constant: 2
      z: [0, 2, 0, 2]
      w: [0, 2, 0, 2]
    O+:
      constant: 2
      z: [0, 2, 0, 2]
      w: [0, 2, 0, 2]
    SO+:
      constant: 2
      z: [0, 2, 0, 2]
      w: [0, 2, 0, 2]
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
      least_valuation: 1
    - representative: 6
      least_valuation: 1
    - representative: 10
      least_valuation: 1
    - representative: 14
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [0, 2, 0, 3, 0, 2, 0, 1/2, 0, 2, 0, 3]
  - prime: 3
    densities: [4/3, 2/3, 10/9, 4/3, 2/3, 8/9, 4/3, 2/3, 28/27, 4/3, 2/3, 10/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 5SYI
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5SYI
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, -1]
  scale: 1
- target: 5SYI
  name: O(L) generator 3
  matrix:
  - [0, 1, 1, 1]
  - [-1, 2, 1, 1]
  - [1, -1, 0, -1]
  - [1, -1, -1, 0]
  scale: 1
- target: 5SYI
  name: O(L) generator 4
  matrix:
  - [-2, 3, 3, 0]
  - [-3, 4, 3, 0]
  - [2, -2, -1, 0]
  - [1, -1, -1, 1]
  scale: 1
- target: 5SYI
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ID2.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ID2.
- tag: 3ID2
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ID2.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ICX, 3ID2.
