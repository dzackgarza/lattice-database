---
tag: 3TFH
name: Constructed lattice 3TFH
latex: L_{\mathrm{3TFH}}
certifications:
  derive: ef4780163c8360850182aa7e78b09252114c8e92d677d3600e311ddbf055307b
  form.integer_valued: 59bd053acacf4cc4ca21e5cf484fac836cb9ef86b99cc61ab6419c27e0c2f9f1
  integral.elementary_primes: 85b78e5a6f4efcc66f490f3547e4d7e78cac0265cc5d36f7548d71a157addc0b
  integral.genus_symbol: cd18cf16e23824567c91e26882a36766ac476de64f5b486408c62f3d60627c33
  integral.genus_class_count: c93f229c1bbd82426824265e2651d2c3968b7b68d239d428d386d4538662d8cd
  integral.overlattice_count: 2c597b09beacc14a118006351a0a6c3995841d0e08ac3a540351304fa58ee9f3
  integral.spinor_genus_count: f9ae95150da1174f040f4088d58a83f777b0f0de7191752c7c3e4137f07c015f
  integral.spinor_genera: 43da635c658d974677e7da15866d9405ea69fb33000dfc4494daabfa019cd1e1
  integral.hyperbolic_index: df9be445a0876539fad365b1a5e45231ff5956837c85fdc038caa9153ea1812f
  automorphisms.automorphism_group_order: e3f8d17630243066388eeec7f74540b519151758a7a52f62b96611084e6e7d79
  automorphisms.automorphism_group_generator_morphisms: 42dac7601cbce806ebf1c26237f2b9dbe94319f3d83bb6dccca83eec1f440282
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 2, -3]
- [0, 0, 0, -3, 6]
signature: [4, 1]
determinant: -3
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 2, 1]
- [0, 0, 0, 1, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  discriminant_group: [3]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{4,1} (2: [1^-5]_1; 3: 1^4 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
indefinite:
  isotropic: true
morphisms:
- target: 3TFH
  name: O(L) generator 1
  matrix:
  - [-1, -2, -2, 0, 0]
  - [-2, -1, -2, 0, 0]
  - [2, 2, 3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TFH
  name: O(L) generator 2
  matrix:
  - [0, 0, -1, -1, 0]
  - [0, 1, 0, 0, 0]
  - [1, 0, 2, 1, 0]
  - [-2, 0, -2, -1, 0]
  - [-1, 0, -1, -1, 1]
  scale: 1
- target: 3TFH
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 3TFH
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TFH
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TFH
  name: O(L) generator 6
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ID4.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ID4.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ID4.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ID4.
