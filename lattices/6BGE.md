---
tag: 6BGE
name: Constructed lattice 6BGE
latex: L_{\mathrm{6BGE}}
certifications:
  derive: 51ff4ecd6bd2922ea402a5072abdd38cdaa662ccd56e3cc3ac0dc28336599fec
  form.integer_valued: ea5167abab8e373b1da5bd0fc414021afa0fb4c3a8468b8ccf6abdcb568eb7a9
  integral.elementary_primes: bce11dd65f4e59eb98a384b81c5b4c7cb2d716d9ca7e1c610d2b59479ed4f596
  integral.genus_symbol: e604cdfad8f3351bd655e4a744b83741de1c3c4ab14bf01f04f756a3bba345b0
  integral.genus_class_count: 71e782f099c8f5c32d4475b6748f5519f552df90df3aabe3fc620dff5e4ce6aa
  integral.overlattice_count: b80297e9d36ff910cadef7e1d318cd8a7be45cac739cb9c83c94ae82cbeae2ec
  integral.spinor_genus_count: 28ba2a147427ba5bfca93a725615c7f8643fdb628ecfe770041c41f1125562c1
  integral.spinor_genera: fa38e50ab01b008c3061b98af92adfc3abe6f87c5eaafc01782c7326106f8662
  integral.hyperbolic_index: b8d7d5cb6d6d7941ee3d6ee77816192d80049a7cb99c4a86ca8b8439221c8221
  automorphisms.automorphism_group_order: 07b0ecf7524160bbe5367da8aaf3af82842abcc1202f5fe3a20737614229785f
  automorphisms.automorphism_group_generator_morphisms: 33cfc93b4d9ce9664d20d4376de53ad1d6d0d08f4a8cbdfb05459807364a52f2
rank: 4
gram_tensor:
- [0, -1, 0, 0]
- [-1, 0, 0, 0]
- [0, 0, 4, -2]
- [0, 0, -2, 4]
signature: [3, 1]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [0, -1, 0, 0]
- [-1, 0, 0, 0]
- [0, 0, 1/3, 1/6]
- [0, 0, 1/6, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 6
  discriminant_group: [2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{3,1} (2: 1^2:2^-2; 3: 1^-3 3^1)'
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
- target: 6BGE
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, -1]
  scale: 1
- target: 6BGE
  name: O(L) generator 2
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6BGE
  name: O(L) generator 3
  matrix:
  - [1, 2, 2, 2]
  - [0, 1, 0, 0]
  - [0, -1, 0, -1]
  - [0, -1, -1, 0]
  scale: 1
- target: 6BGE
  name: O(L) generator 4
  matrix:
  - [0, 1, 0, 0]
  - [1, 2, 4, -2]
  - [0, -1, -1, 0]
  - [0, -1, -1, 1]
  scale: 1
- target: 6BGE
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ID2.
- tag: 3ID2
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ID2.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICY, 3ID2.
