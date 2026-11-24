---
tag: 5LSP
name: Constructed lattice 5LSP
latex: L_{\mathrm{5LSP}}
certifications:
  derive: 82bb02c304cfe1c46e4cfc89c8e0cef6b9ff546f57ff0b548e64e6c9a37345f0
  form.integer_valued: 4091434bddacbb8dca1da159075de1e766fbcc58e69acace6c8694789325230d
  integral.elementary_primes: a2109fa74b9bb574e5b79a5dd598a71c20304af0cda93f6615513a9cdb1994d0
  integral.genus_symbol: 53d9ff90f4761591889178d9565f0f09f1ef4da0adfb877f771d9421fd6c51fd
  integral.genus_class_count: 47fab31f9ed238bec04623231bf82139cb2f22ecbf51bebe985c4bd0ae17bfa9
  integral.overlattice_count: 3d9768ebe356bf034c3e1ecd230ad8bbe74fc28c3b0e0601e37aa9e2b2dd8ece
  integral.spinor_genus_count: a36a11a59b912cca642d9ab64550f17f9d8a11d4efce870c25855d182e7a22a9
  integral.spinor_genera: 852a04faf30ddeae274f9abb85ad5deb4da39974701f87dd642282c1fd887606
  integral.hyperbolic_index: 0322f7fcdd28fb326dad530dadcb003b25fc373d5fa47db2724d217dd85644e0
  automorphisms.automorphism_group_order: a1f005ba14a1d08f71e84493456db867686190a4e1e6588bae6bd8b8d77ad563
  automorphisms.automorphism_group_generator_morphisms: c818f5262f7bcae5016365fb5f8338d2ccc80e83ec5d1a61d6b975300c0e28be
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, 0, 1]
- [0, 0, 0, 1, 0]
signature: [3, 2]
determinant: 8
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, 0, 1]
- [0, 0, 0, 1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  discriminant_group: [2, 2, 2]
  overlattice_count: 4
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{3,2} (2: 1^2 [2^3]_1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17, O(L) generator 18, O(L) generator 19, O(L) generator 20, O(L) generator 21, O(L) generator 22, O(L) generator 23, O(L) generator 24, O(L) generator 25, O(L) generator 26, O(L) generator 27, O(L) generator 28, O(L) generator 29]
indefinite:
  isotropic: true
morphisms:
- target: 5LSP
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5LSP
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, -1, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, -2, 0, -1, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 1]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-2, 0, 0, 1, -1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, -1]
  - [0, 0, -2, 1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 1]
  - [0, 0, 1, 0, 0]
  - [0, -2, 0, 1, -1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, 1, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, -1, 0]
  - [0, 0, 0, -1, 0]
  - [-2, 0, -2, 0, -1]
  scale: 1
- target: 5LSP
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 5LSP
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5LSP
  name: O(L) generator 9
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 10
  matrix:
  - [-1, 2, -2, 0, 0]
  - [-2, 1, -2, 0, 0]
  - [2, -2, 3, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5LSP
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 13
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 5LSP
  name: O(L) generator 14
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 5LSP
  name: O(L) generator 15
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, -2]
  - [0, 0, -1, 0, -2]
  - [0, -4, -4, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5LSP
  name: O(L) generator 16
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5LSP
  name: O(L) generator 17
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 2]
  - [0, 0, 1, 0, -2]
  - [0, 0, 0, 0, 1]
  - [0, -4, -4, 1, 0]
  scale: 1
- target: 5LSP
  name: O(L) generator 18
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 5LSP
  name: O(L) generator 19
  matrix:
  - [-1, 0, 0, 1, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, 0, -1, 0]
  - [-2, 0, 2, 0, -1]
  scale: 1
- target: 5LSP
  name: O(L) generator 20
  matrix:
  - [-1, 0, 0, -1, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [-2, 0, 0, -1, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 21
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 22
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, -2, 1, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 23
  matrix:
  - [-1, 0, 0, 0, 2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [4, 0, 0, 1, -4]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 24
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 2]
  - [0, 0, 1, 0, 0]
  - [0, 4, 0, 1, -4]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 25
  matrix:
  - [1, 2, 2, 0, 0]
  - [2, 1, 2, 0, 0]
  - [-2, -2, -3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 26
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, -2]
  - [0, 0, 4, 1, 4]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 27
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5LSP
  name: O(L) generator 28
  matrix:
  - [2, 1, 2, 0, -1]
  - [-1, 0, 0, -1, 0]
  - [4, 4, 5, 1, -2]
  - [2, 2, 2, 1, -1]
  - [6, 8, 10, 0, -3]
  scale: 1
- target: 5LSP
  name: O(L) generator 29
  matrix:
  - [2, 1, 2, 0, -1]
  - [-1, -2, -2, 0, 4]
  - [2, 2, 3, 0, 0]
  - [12, 18, 20, 1, -17]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX, 0016.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX, 0016.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX, 0016.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0002, 3ICX, 0016.
