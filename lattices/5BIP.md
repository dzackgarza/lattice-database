---
tag: 5BIP
name: Constructed lattice 5BIP
latex: L_{\mathrm{5BIP}}
certifications:
  derive: 1d176335825841e0edb22d8e0831923eb57187a8e04938a23592b2e4d95f7574
  form.integer_valued: 07eeeaa650a605c0b35aa8ebee114ac8c2916635856449a5d8f3aaba8f64fca8
  integral.elementary_primes: c8fd96b7ecfb74837fe383687987aaf93b27e1335e019d5ae286f3d2e1cd2769
  integral.genus_symbol: 37a5f9171744a7ba13a886809646ec383be4f86a5b35b1f8d8856ac2b67d7967
  integral.genus_class_count: 0d0ba8fde837d18931d823a3d9a6ace3622e308d7ad65dcb5a338339ef41d56f
  integral.overlattice_count: 2224aa33e097e8569201d47d160c8679464b547ba65ac181662795597aabb2c0
  integral.spinor_genus_count: c1ff93ed327a17b1b14d1d2b48aa79801c8a0c55f9bb89e2f88479a9ff929209
  integral.spinor_genera: a234479367de9b936605c54b13531c61e602a1c73ca22bc2560dd44b61bb308f
  integral.hyperbolic_index: 239d6426f5805990ca63e18212b37d8af2b5b415bfac1e4444b85abc37b0c01c
  automorphisms.automorphism_group_generator_morphisms: f5e7781ecdea6f930acd7e33bf9c5753f3f3ec761d9b5d2182b7ece097775eed
rank: 4
gram_tensor:
- [-1, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, 0, -1]
- [0, 0, -1, 0]
signature: [1, 3]
determinant: -2
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, 0, -1]
- [0, 0, -1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  discriminant_group: [2]
  overlattice_count: 1
  bad_reduction_primes: [2]
  quadratic_character: -8
  genus_symbol: 'I_{1,3} (2: [1^3 2^1]_6)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
indefinite:
  isotropic: true
morphisms:
- target: 5BIP
  name: O(L) generator 1
  matrix:
  - [-1, -4, 2, -2]
  - [-2, -3, 2, -2]
  - [-2, -4, 3, -2]
  - [2, 4, -2, 3]
  scale: 1
- target: 5BIP
  name: O(L) generator 2
  matrix:
  - [-3, -4, 4, -2]
  - [-2, -1, 2, -1]
  - [-2, -2, 3, -1]
  - [4, 4, -4, 3]
  scale: 1
- target: 5BIP
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, -1]
  - [0, 0, -1, 0]
  scale: 1
- target: 5BIP
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 2]
  - [0, 1, 0, 0]
  - [-2, 0, 1, -2]
  - [0, 0, 0, 1]
  scale: 1
- target: 5BIP
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, -2]
  - [0, -1, 0, 0]
  - [-2, 0, 1, -2]
  - [0, 0, 0, 1]
  scale: 1
- target: 5BIP
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ICY.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ICY.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ICY.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICX, 3ICY.
