---
tag: 5TDE
name: Constructed lattice 5TDE
latex: L_{\mathrm{5TDE}}
certifications:
  derive: 5b76dff11ef39ad0237f91e658eb90c266114f6e9f1ef2c38549beadef8ebfe6
  form.integer_valued: 42db1702f43bc66831f5fc50448b117964fd1e9c8b745daa39515428b46d95f9
  integral.elementary_primes: 1dd813d0d5230d8c742a44c0a3a693e5398afe93dadd7b10b74c5dcd49cfd655
  integral.genus_symbol: 1e45f76878474ad2b4e6fd8a18c6ef2ff6ac5fc354bf449ad768d41132038364
  integral.genus_class_count: 67712cbc980a1a3ccb40a670864ee78068e0b1ac62cc2dbb531c8834618d22ec
  integral.overlattice_count: 3d3fd6b838ec508239f8fac1c9ee90e3dc0ce9acfe85ecbea4d3bb4f75e45b11
  integral.spinor_genus_count: b9b5c204cbe472f4096bb39e09dee1dc5559e54478529c64965c601a93b32e90
  integral.spinor_genera: a86cb9ec7023b5bc9794b3cbfa6614574de3571c67a20ff485ef045861428631
  integral.hyperbolic_index: 5e1f6502716e0de9c0bf49fc36fd0228b84d3bab922bf46e09f823cedd5a6bc8
  automorphisms.automorphism_group_order: d82f7f56f17b6635eba89c76b315c734ebd8ca1b27ced77284fca394da7a91a7
  automorphisms.automorphism_group_generator_morphisms: b4d8451de314f22eb647204badcc220028e6e79d374990890e73fc39a2b22eb5
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, -2, 0, 0, 0]
- [0, 0, 2, -1, 0]
- [0, 0, -1, 2, -1]
- [0, 0, 0, -1, 2]
signature: [4, 1]
determinant: -16
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, -1/2, 0, 0, 0]
- [0, 0, 3/4, 1/2, 1/4]
- [0, 0, 1/2, 1, 1/2]
- [0, 0, 1/4, 1/2, 3/4]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 8
  discriminant_group: [2, 2, 4]
  overlattice_count: 5
  bad_reduction_primes: [2]
  genus_symbol: 'II_{4,1} (2: 1^2 [2^2 4^1]_3)'
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
- target: 5TDE
  name: O(L) generator 1
  matrix:
  - [-1, -2, 1, -1, -1]
  - [2, 3, -1, 1, 1]
  - [0, 0, 1, 0, 0]
  - [-2, -2, 1, 0, -1]
  - [-2, -2, 1, -1, 0]
  scale: 1
- target: 5TDE
  name: O(L) generator 2
  matrix:
  - [-1, -4, 4, -2, 0]
  - [4, 9, -8, 4, 0]
  - [4, 8, -7, 4, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TDE
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5TDE
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, -1, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, -1, 1]
  scale: 1
- target: 5TDE
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 5, -4, 4, 0]
  - [0, 2, -1, 2, 0]
  - [0, -4, 4, -3, 0]
  - [0, -2, 2, -2, 1]
  scale: 1
- target: 5TDE
  name: O(L) generator 6
  matrix:
  - [0, -1, 1, -1, 1]
  - [1, 2, -1, 1, -1]
  - [1, 1, 0, 1, -1]
  - [0, 0, 0, 1, 0]
  - [1, 1, -1, 1, 0]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 0023.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 0023.
- tag: '0023'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 0023.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ICX, 0023.
