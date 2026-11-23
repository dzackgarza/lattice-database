---
tag: 4FQF
name: Constructed lattice 4FQF
latex: L_{\mathrm{4FQF}}
certifications:
  derive: 47ec410fc924ca4772ebaaf11f1e69c621d85fb5cd0cbf145b7ef03b532b9d0d
  form.integer_valued: c6de90a01f93f48b4aff5d8dffb632cc5ee56c0125d523bcdcc82d5d5bc217cb
  integral.elementary_primes: abd7453fdc302616327a661324d18d13cbc5f66a15a3ae900a46c80950707fea
  integral.genus_symbol: 42f1122ca44c5ef22e2f88655af446a46a67101554b648b5cc8b7616f73a3cb1
  integral.genus_class_count: 005bdf4c90f6a6fcde11dbda7092251d1891e19259a05ceb535c340aa999c758
  integral.overlattice_count: 443342a3d18dbbc6563a383fda5532c3140e6a8d81414c4ae96637b2046aa03f
  integral.spinor_genus_count: fc42872a45d64cad503a7cfdf2013d6468f178d9623177b8549acc8cab68b92b
  integral.spinor_genera: 2dcedfb2817e937125f72aa67fda129639a09ea4596798ece02ba18f806de686
  integral.hyperbolic_index: 2767d4af1b396a7e2cfb6b37538cfe9e40a7dbd54319392e15c5f422da038bcb
  automorphisms.automorphism_group_order: 1177e6feeb7a380a942041bfc2bccab0bd55ab8ffeabd9048c1f7abec2b524ea
  automorphisms.automorphism_group_generator_morphisms: b6c9ae355e00b2ddf4cd28c26d1c51d2a44e862c87c16e60f3a812504e6d899c
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, 4, -6]
- [0, 0, 0, -6, 12]
signature: [4, 1]
determinant: -48
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, 1, 1/2]
- [0, 0, 0, 1/2, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  discriminant_group: [2, 2, 2, 6]
  overlattice_count: 11
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{4,1} (2: [1^-1 2^4]_5; 3: 1^-4 3^1)'
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
- target: 4FQF
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4FQF
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, -1, 1]
  scale: 1
- target: 4FQF
  name: O(L) generator 3
  matrix:
  - [-7, -4, -12, -8, 12]
  - [-2, 0, -3, -2, 3]
  - [6, 3, 10, 6, -9]
  - [-2, -1, -3, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4FQF
  name: O(L) generator 4
  matrix:
  - [-17, 0, -24, 0, 0]
  - [0, 1, 0, 0, 0]
  - [12, 0, 17, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4FQF
  name: O(L) generator 5
  matrix:
  - [-7, 2, -10, 0, 0]
  - [5, 0, 7, 0, 0]
  - [7, -1, 10, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4FQF
  name: O(L) generator 6
  matrix:
  - [-31, 0, -48, -24, 48]
  - [0, 1, 0, 0, 0]
  - [24, 0, 37, 18, -36]
  - [-12, 0, -18, -7, 15]
  - [-4, 0, -6, -2, 5]
  scale: 1
- target: 4FQF
  name: O(L) generator 7
  matrix:
  - [-21, 0, -36, -20, 48]
  - [0, 1, 0, 0, 0]
  - [18, 0, 31, 18, -42]
  - [-4, 0, -6, -3, 6]
  - [2, 0, 4, 3, -7]
  scale: 1
- target: 4FQF
  name: O(L) generator 8
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ICX, 3ID6.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ICX, 3ID6.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ICX, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ICX, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0002, 3ICX, 3ID6.
