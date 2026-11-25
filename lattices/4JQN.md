---
tag: 4JQN
name: Constructed lattice 4JQN
latex: L_{\mathrm{4JQN}}
certifications:
  derive: 81c0f8002e78825b4e1fb507a8f0f16091867af38764081069782c00e7116953
  form.integer_valued: 33cc6d7c04000493fa2d44d3c1e71aa535721909c636242875af4d37beb5e460
  integral.elementary_primes: 764bb076512278b4b82e69c0bcf7590c7d8ad70eb9939859ea26b588b8ed724e
  integral.genus_symbol: cc5c19d2b41b784bc955b9f92af94cca4394a9411008dacf3e1791f38f811eab
  integral.genus_class_count: 48de128d07ff0e671f4559ae7f863fcae2d4458e18d94f8994dc31a09e932afd
  integral.overlattice_count: f4fc47beeb93a4e751794c70fe4b340360e74bb8a2a14cfbaa49fef0052e1eb8
  integral.spinor_genus_count: 0b59f02095803f1e82f03034b691cacbdca7c7ddcfc03a5cc457210eb3e9f826
  integral.spinor_genera: a525a056cd4e2da2c113adb2168bb5e27a0a49c613f0af49fa038b111f0fc492
  integral.hyperbolic_index: d3737682da082c454a1d806a8a2d1c3fd3510c45ee9210fda7cd0d464d02f48a
  automorphisms.automorphism_group_order: bcedafd497e0892e3fdd562861e4c4a58bfbaa389250b8dfebb3a87f03b2a53e
  automorphisms.automorphism_group_generator_morphisms: 3fa30cdd974ee48b419688f9be20b781836a7d593b205861bdcace927d35b3f4
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -2, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, -4, 2]
- [0, 0, 0, 2, -4]
signature: [1, 4]
determinant: 48
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -1/2, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, -1/3, -1/6]
- [0, 0, 0, -1/6, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  discriminant_group: [2, 2, 2, 6]
  overlattice_count: 11
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{1,4} (2: [1^-1 2^4]_3; 3: 1^-4 3^-1)'
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
- target: 4JQN
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4JQN
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4JQN
  name: O(L) generator 3
  matrix:
  - [3, 2, -2, 2, 2]
  - [-1, 0, 1, -1, -1]
  - [1, 1, 0, 1, 1]
  - [-1, -1, 1, 0, -1]
  - [-1, -1, 1, -1, 0]
  scale: 1
- target: 4JQN
  name: O(L) generator 4
  matrix:
  - [3, 4, 0, 0, 0]
  - [-2, -3, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4JQN
  name: O(L) generator 5
  matrix:
  - [3, 4, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [2, 3, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4JQN
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 4JQN
  name: O(L) generator 7
  matrix:
  - [7, 0, 0, 12, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-4, 0, 0, -7, 0]
  - [-2, 0, 0, -4, 1]
  scale: 1
- target: 4JQN
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
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ICX, 3ID1.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ICX, 3ID1.
- tag: 3ID1
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ICX, 3ID1.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICX, 3ICX, 3ID1.
