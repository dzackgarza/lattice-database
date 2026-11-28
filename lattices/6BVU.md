---
tag: 6BVU
name: Constructed lattice 6BVU
latex: L_{\mathrm{6BVU}}
certifications:
  derive: 0f08c17c0d99a8ee04dc04d4a2fc93fc916ea02e35b858813fa48101969dc640
  form.integer_valued: f437125a1c6492dea26b97a481827c9477828779128bf7bf733c030e337659c2
  integral.elementary_primes: 470ecfe8aed1159eda1af3bf8d973a9770cd2cbc975ed12cf64e154f5022bd39
  integral.genus_symbol: d4da6015359b62c8967a9cb53b57323418e7a77445fbcdee677e2c9758f08ce3
  integral.genus_class_count: 1f8597dc8da72d409ca0f2e025687dc750aad96b6122f873b70ce4a81f4818be
  integral.overlattice_count: 1e9b4560ddf1c94c3cad8607b8cfe3671e65305927cc8590619c379bb8e43bdc
  integral.spinor_genus_count: 92d3215a67fcce340e393a18507c4afc048b1c41efda5871920da3fdd9040b24
  integral.spinor_genera: ec3acde7a117b21e420e40459ca3721092913a8bf1d4d15a71795229f7dbdd19
  integral.hyperbolic_index: 8672957cdf22bc0f3b007589020f303d2b34e7ce80dfdf751d0cf94b5bb793f2
  automorphisms.automorphism_group_order: a9e542b46f588bf0a24327ce17fbf8bba3e9a588f16b1f8ccdd5338977adb34a
  automorphisms.automorphism_group_generator_morphisms: 98f6904f144131be1717e7a3a4ad35e3a6d2bb5be1a51639ef2c8203942fd9e7
rank: 5
gram_tensor:
- [0, -1, 0, 0, 0]
- [-1, 0, 0, 0, 0]
- [0, 0, -4, 2, 0]
- [0, 0, 2, -4, 2]
- [0, 0, 0, 2, -4]
signature: [1, 4]
determinant: 32
definiteness: indefinite
dual_gram_tensor:
- [0, -1, 0, 0, 0]
- [-1, 0, 0, 0, 0]
- [0, 0, -3/8, -1/4, -1/8]
- [0, 0, -1/4, -1/2, -1/4]
- [0, 0, -1/8, -1/4, -3/8]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 16
  discriminant_group: [2, 2, 8]
  overlattice_count: 11
  bad_reduction_primes: [2]
  genus_symbol: 'II_{1,4} (2: 1^2:2^-2:[8^-1]_5)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 6BVU
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [-2, 1, -2, 0, -2]
  - [-1, 0, 0, 0, -1]
  - [-1, 0, -1, 1, -1]
  - [-1, 0, -1, 0, 0]
  scale: 1
- target: 6BVU
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 6BVU
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 1, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 6BVU
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  - [0, 0, 1, 0, 0]
  scale: 1
- target: 6BVU
  name: O(L) generator 5
  matrix:
  - [0, -1, 0, 0, 0]
  - [-1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ID8.
- tag: 3ID8
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ID8.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICY, 3ID8.
