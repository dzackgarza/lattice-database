---
tag: 5UMA
name: Constructed lattice 5UMA
latex: L_{\mathrm{5UMA}}
certifications:
  derive: a69cd081d08288612126cf40e0b70108ba5f4e5d39a29c8b9f0fea830d8709d8
  form.integer_valued: 0e9966c5ad55b73b1b0f53480931bc5ea96e64460d54629eaaad1439c968c6e8
  integral.elementary_primes: 72bbb5ddc078812a0df69594d18da1a08b85ffcff6af1b1abcec4226bff79fd2
  integral.genus_symbol: 01a4cc7050af1db0a8f9873cd8b623ad19d33cbc4babe20f33072eac11f33a3b
  integral.genus_class_count: b5547b28e46b204cf819c4e381e74796d768f747d88288ce7c694083ec48e903
  integral.overlattice_count: e5f6c87eab5e47b40e95e8d641f7fec24cefd77d3ef77f9eef33e3e6617c65a2
  integral.spinor_genus_count: 22d4c9f0d7c89088765891943c1adbc0bb7973bda1d7a54bdf05fd53198e3732
  integral.spinor_genera: 05d546874622efc206460f11d7694ff8db7a78f5917da85bffb84bc897a40cf8
  integral.hyperbolic_index: 3d9eb81467ca3ffdd493c5ce3a7b1b24c31f4a669b48242aa0735d39a7a917d0
  automorphisms.automorphism_group_order: ebbab8424a912731138bb8d0ac5cefcd62bc4831585e6ef7e64c22b428242b61
  automorphisms.automorphism_group_generator_morphisms: 120019c800e5b1926c3cd0c85f16ab48798baa8fafb59c0ada44d1fae45e3c83
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 0, -2, 1]
- [0, 0, 0, 1, -2]
signature: [2, 3]
determinant: -6
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 0, -2/3, -1/3]
- [0, 0, 0, -1/3, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  discriminant_group: [6]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'II_{2,3} (2: 1^-4 [2^1]_1; 3: 1^4 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 2
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17, O(L) generator 18, O(L) generator 19, O(L) generator 20, O(L) generator 21, O(L) generator 22, O(L) generator 23, O(L) generator 24, O(L) generator 25, O(L) generator 26, O(L) generator 27, O(L) generator 28]
indefinite:
  isotropic: true
morphisms:
- target: 5UMA
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 5UMA
  name: O(L) generator 4
  matrix:
  - [-7, 0, 0, -6, 6]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [4, 0, 0, 3, -4]
  - [-4, 0, 0, -4, 3]
  scale: 1
- target: 5UMA
  name: O(L) generator 5
  matrix:
  - [7, 0, 0, 6, -6]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-4, 0, 0, -3, 4]
  - [4, 0, 0, 4, -3]
  scale: 1
- target: 5UMA
  name: O(L) generator 6
  matrix:
  - [-3, -1, 1, -3, 3]
  - [-2, 0, 0, -2, 1]
  - [2, 0, 0, 1, -2]
  - [2, 0, -1, 2, -2]
  - [-2, -1, 0, -2, 2]
  scale: 1
- target: 5UMA
  name: O(L) generator 7
  matrix:
  - [-3, -1, 1, -3, 3]
  - [2, 0, 0, 1, -2]
  - [-2, 0, 0, -2, 1]
  - [2, 1, 0, 2, -2]
  - [-2, 0, 1, -2, 2]
  scale: 1
- target: 5UMA
  name: O(L) generator 8
  matrix:
  - [1, -1, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [-2, 0, 1, -2, 1]
  - [0, 1, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 9
  matrix:
  - [-3, 1, -1, -3, 3]
  - [-2, 0, 0, -2, 1]
  - [2, 0, 0, 1, -2]
  - [2, 0, 1, 2, -2]
  - [-2, 1, 0, -2, 2]
  scale: 1
- target: 5UMA
  name: O(L) generator 10
  matrix:
  - [1, 0, -1, 0, 0]
  - [-2, 1, 0, -2, 1]
  - [0, 0, 1, 0, 0]
  - [0, 0, 1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 11
  matrix:
  - [1, 1, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [2, 0, 1, 2, -1]
  - [0, -1, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 12
  matrix:
  - [1, 1, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [2, 0, 1, 1, -2]
  - [0, 0, 0, 1, 0]
  - [0, 1, 0, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 13
  matrix:
  - [1, -3, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [-6, -3, 1, -6, 6]
  - [0, 2, 0, 1, 0]
  - [0, -2, 0, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 14
  matrix:
  - [1, 0, -1, 0, 0]
  - [-2, 1, 0, -1, 2]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, -1, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 15
  matrix:
  - [1, 0, 3, 0, 0]
  - [6, 1, -3, 6, -6]
  - [0, 0, 1, 0, 0]
  - [0, 0, -2, 1, 0]
  - [0, 0, 2, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 16
  matrix:
  - [1, 0, 1, 0, 0]
  - [2, 1, 0, 2, -1]
  - [0, 0, 1, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 17
  matrix:
  - [7, 0, 0, 6, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-4, 0, 0, -3, -1]
  - [4, 0, 0, 4, -1]
  scale: 1
- target: 5UMA
  name: O(L) generator 18
  matrix:
  - [1, -1, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [-2, 0, 1, -1, 2]
  - [0, 0, 0, 1, 0]
  - [0, -1, 0, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 19
  matrix:
  - [1, 0, 1, 0, 0]
  - [2, 1, 0, 1, -2]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 1, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 20
  matrix:
  - [7, 0, 0, 0, -6]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-4, 0, 0, -1, 4]
  - [4, 0, 0, -1, -3]
  scale: 1
- target: 5UMA
  name: O(L) generator 21
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 22
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5UMA
  name: O(L) generator 23
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5UMA
  name: O(L) generator 24
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 5UMA
  name: O(L) generator 25
  matrix:
  - [3, -1, -1, -1, -1]
  - [2, 0, -1, -1, -1]
  - [2, -1, 0, -1, -1]
  - [-2, 1, 1, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5UMA
  name: O(L) generator 26
  matrix:
  - [7, 0, 0, -6, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-4, 0, 0, 3, 1]
  - [4, 0, 0, -4, 1]
  scale: 1
- target: 5UMA
  name: O(L) generator 27
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5UMA
  name: O(L) generator 28
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICY, 3ID0.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICY, 3ID0.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICY, 3ID0.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ICY, 3ID0.
