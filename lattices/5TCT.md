---
tag: 5TCT
name: Constructed lattice 5TCT
latex: L_{\mathrm{5TCT}}
certifications:
  derive: f1c6d4cd5cc2a439bb1cea6242c65981202d232479a70ad79a6e35f34d7c7f63
  form.integer_valued: 499107faa7f39dc5e20d6f6e3f755d90120f451ead095670c4ca565a6359e9a8
  integral.elementary_primes: b16cd7b5a7e5cbcd681af5ad2a0093f69d94a0ed8f7a063784c48d1448c63c96
  integral.genus_symbol: 379e80ee6edd232e46eefef6ee2fa2172b67d0da65e1e8c6a3dbb6c8bc4414ca
  integral.genus_class_count: c77b21c3bc49e94f01fb735bd14e31ae3caa63a090f1ad30e30c711d99ecacbc
  integral.overlattice_count: 79ee3d0e7445ae0caa9400909bc826d891e96cfa528ddf7dc8206487ed14a877
  integral.spinor_genus_count: 17b8a60a03ebddef801be1f8ac42a914a6bd7ab475b1afa9ab5ac585c9cf0d2c
  integral.spinor_genera: f397963eb78fbdfa1f6800673124b3ea839606efcb988ad520c56ab297c56cd0
  integral.hyperbolic_index: 0126736005d9405a180a3cfd52e4d58a3751eb368db2d4fccb908ef9a1adade6
  automorphisms.automorphism_group_order: 1eaa33296b17c2a74ae603f4568ddb299f16d1ae19de7d914db66cb85a0e06c4
  automorphisms.automorphism_group_generator_morphisms: 7ed83a153f28c270b43113343b02e9353d1c0102e1031642bd3bdaf88567dcca
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, -2, 0, 0, 0]
- [0, 0, -2, 1, 0]
- [0, 0, 1, -2, 1]
- [0, 0, 0, 1, -2]
signature: [1, 4]
determinant: 16
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, -1/2, 0, 0, 0]
- [0, 0, -3/4, -1/2, -1/4]
- [0, 0, -1/2, -1, -1/2]
- [0, 0, -1/4, -1/2, -3/4]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 8
  discriminant_group: [2, 2, 4]
  overlattice_count: 5
  bad_reduction_primes: [2]
  genus_symbol: 'II_{1,4} (2: 1^2 [2^2 4^1]_5)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11]
indefinite:
  isotropic: true
morphisms:
- target: 5TCT
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TCT
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TCT
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 1, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TCT
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5TCT
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5TCT
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  - [0, 0, 1, 0, 0]
  scale: 1
- target: 5TCT
  name: O(L) generator 7
  matrix:
  - [2, -1, -1, 1, -1]
  - [1, 0, -1, 1, -1]
  - [1, -1, 0, 1, -1]
  - [0, 0, 0, 1, 0]
  - [1, -1, -1, 1, 0]
  scale: 1
- target: 5TCT
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TCT
  name: O(L) generator 9
  matrix:
  - [2, 1, -1, 0, 1]
  - [1, 0, -1, 0, 1]
  - [1, 1, -1, 1, 0]
  - [0, 0, 0, 1, 0]
  - [-1, -1, 0, 1, -1]
  scale: 1
- target: 5TCT
  name: O(L) generator 10
  matrix:
  - [7, -2, -6, 1, 0]
  - [2, -1, -2, 1, 0]
  - [8, -2, -7, 1, 0]
  - [4, 0, -4, 1, 0]
  - [2, 0, -2, 1, -1]
  scale: 1
- target: 5TCT
  name: O(L) generator 11
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ID7.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ID7.
- tag: 3ID7
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ID7.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ICX, 3ID7.
