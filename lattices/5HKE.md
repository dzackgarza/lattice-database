---
tag: 5HKE
name: Constructed lattice 5HKE
latex: L_{\mathrm{5HKE}}
certifications:
  derive: 65e0a4f110b979d01936be09162730e9fe16c1cf9cf077b9bb3091395e764f45
  form.integer_valued: 11d2e1d4af232b16d8706517196e994e759c392db1d4e8b2603bae5c6567a1df
  integral.elementary_primes: 58bc375be92506840a01b0111786aa1c76d660e477456ce2c577e5470ab96e79
  integral.genus_symbol: a545324b5f96c38912ed51862e8c0ebaabe4a75da4d40139e1fd1b1a188ea554
  integral.genus_class_count: 35500a62bddf81c771e46beb55f03940c77e234978c853ef9c6655f1b3dfcf76
  integral.overlattice_count: 0d6d2ec04afc3e035df8c8cbe6dda78b8cd26008d6a04bc9679c80bfedcb8ec8
  integral.spinor_genus_count: 2438f6e76e59b992f85befd2bee735dcb47bb0ba9fe7a1b07a603e717ebd8303
  integral.spinor_genera: 1cbe8197611c420a520b319aae943da320ed4b3b98157e360270cf97c56377f6
  integral.hyperbolic_index: 044b90007e18a8d573e99867ade9fb97b73a06e807c85b7c8cfda4affe34679f
  automorphisms.automorphism_group_order: 3ad84b61507d26c8c110f8703b7b3c922682ebc82d3cc8773a534e189b6b3411
  automorphisms.automorphism_group_generator_morphisms: 8b03918dafc2c0327d5135b8eba7ec0c74acaf20b950088295d3ee7fde33b813
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 4, -2, 0, 0]
- [0, -2, 4, 0, 0]
- [0, 0, 0, 4, -6]
- [0, 0, 0, -6, 12]
signature: [4, 1]
determinant: -144
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 1/3, 1/6, 0, 0]
- [0, 1/6, 1/3, 0, 0]
- [0, 0, 0, 1, 1/2]
- [0, 0, 0, 1/2, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  discriminant_group: [2, 2, 6, 6]
  overlattice_count: 31
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{4,1} (2: [1^1]_7 2^4; 3: 1^-3 3^2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8]
indefinite:
  isotropic: true
morphisms:
- target: 5HKE
  name: O(L) generator 1
  matrix:
  - [7, -12, 0, 0, 0]
  - [4, -7, 0, 0, 0]
  - [2, -4, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5HKE
  name: O(L) generator 2
  matrix:
  - [7, 0, 0, 12, -24]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [2, 0, 0, 4, -7]
  scale: 1
- target: 5HKE
  name: O(L) generator 3
  matrix:
  - [3, -2, -2, 4, -6]
  - [1, 0, -1, 2, -3]
  - [1, -1, 0, 2, -3]
  - [-1, 1, 1, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5HKE
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, -1, 1]
  scale: 1
- target: 5HKE
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -3]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5HKE
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5HKE
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5HKE
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, -1, 2]
  - [0, 0, 0, -1, 1]
  - [0, 1, -2, 0, 0]
  - [0, 1, -1, 0, 0]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID2, 3ID6.
- tag: 3ID2
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID2, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID2, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ID2, 3ID6.
