---
tag: 4DQS
name: Constructed lattice 4DQS
latex: L_{\mathrm{4DQS}}
certifications:
  derive: 3310cfd1d9236adf651aa4e76cb499c6bc42d6263085c5f4ae6b74edf6eab743
  form.integer_valued: 23d57403ec6b07506f2c47a44be0745fa07139f4ba4c03994c37251be3672ef8
  integral.elementary_primes: 4e1a24cea5b83a2ff235c6c92cd11901fee948ee8d5d7fa60e85cf68e97c3ffe
  integral.genus_symbol: d915b327f0fc6dde81d02c06be19457db95527399122f01c429098f5aeafd109
  integral.genus_class_count: c0f3592d2eef4b3edde2f1bd98592e519a7343aebd54088667081a1f4289382b
  integral.overlattice_count: dee49aaeb8e5b3a6e712b8effc86a1ff46222d5935c0f35bed1a0ba7409b6304
  integral.spinor_genus_count: 422b5d3ff48fcb515cd386c1af6803896c70471f6acd7465b0100bcec05bf81c
  integral.spinor_genera: 2d019c16f760ae2608582f80125c150a815bfa8e7d7b1ab52e1178be78b0e620
  integral.hyperbolic_index: 68b75f7c1e7e8b5efe97b6824c043defb4c4e711a8800bc398f290ef3609d0cd
  automorphisms.automorphism_group_order: 363422a9b52251be91d7ddca0a914581da5f94ebb3908e9d2e0a39bf79c34dbe
  automorphisms.automorphism_group_generator_morphisms: 48d0d047930c29244075331793f382778e2a2c998e6f83b576a6b2b06e93c2de
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 0, 0, 0, -2]
- [0, 0, 0, -2, 0]
signature: [4, 1]
determinant: -16
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 0, 0, 0, -1/2]
- [0, 0, 0, -1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  discriminant_group: [2, 2, 2, 2]
  overlattice_count: 11
  bad_reduction_primes: [2]
  genus_symbol: 'I_{4,1} (2: [1^1 2^4]_3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10]
indefinite:
  isotropic: true
morphisms:
- target: 4DQS
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DQS
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 4DQS
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, -1]
  - [0, 1, 0, 0, 1]
  - [0, 1, -1, 1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DQS
  name: O(L) generator 4
  matrix:
  - [-17, -24, 0, -24, -24]
  - [-12, -15, 0, -16, -16]
  - [0, 0, 1, 0, 0]
  - [12, 16, 0, 17, 16]
  - [12, 16, 0, 16, 17]
  scale: 1
- target: 4DQS
  name: O(L) generator 5
  matrix:
  - [-1, -4, 0, -4, -2]
  - [-2, -3, 0, -4, -2]
  - [0, 0, 1, 0, 0]
  - [1, 2, 0, 3, 1]
  - [2, 4, 0, 4, 3]
  scale: 1
- target: 4DQS
  name: O(L) generator 6
  matrix:
  - [-7, -4, 4, -8, -8]
  - [-2, 0, 1, -2, -2]
  - [2, 1, 0, 2, 2]
  - [4, 2, -2, 5, 4]
  - [4, 2, -2, 4, 5]
  scale: 1
- target: 4DQS
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DQS
  name: O(L) generator 8
  matrix:
  - [-3, -4, 0, -4, -4]
  - [0, -1, 0, 0, -1]
  - [2, 2, -1, 2, 3]
  - [2, 3, -1, 3, 3]
  - [2, 2, 0, 2, 3]
  scale: 1
- target: 4DQS
  name: O(L) generator 9
  matrix:
  - [-1, -4, 0, -2, -4]
  - [-2, -3, 0, -2, -4]
  - [0, 0, 1, 0, 0]
  - [1, 2, 0, 1, 3]
  - [2, 4, 0, 3, 4]
  scale: 1
- target: 4DQS
  name: O(L) generator 10
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 3ICZ.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 3ICZ.
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0002, 0002, 3ICZ.
