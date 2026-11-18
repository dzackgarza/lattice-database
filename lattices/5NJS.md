---
tag: 5NJS
name: Constructed lattice 5NJS
latex: L_{\mathrm{5NJS}}
certifications:
  derive: 031393fed268ff92c52f038c23d6c6f56bdee2b3256edb58e7c150c0881e1721
  form.integer_valued: 62cff998b15a8b693164547b473d8f39709ab857021606e5c1d0980161e9cfbc
  integral.elementary_primes: 609bd5b315b4cb3806ffff34677f33df9ebb133b80066cd1dd17f1d574d7f272
  integral.genus_symbol: 987aeacdf8e76cb4eeefedcdfd80b59a8445958aaa14414fadde2d6805692b10
  integral.genus_class_count: 2bb47f4ce57a77b45b3d101324e38c781b72489e71299ea212e91dab56dba191
  integral.overlattice_count: 64ef84da91c78665bf40e002e30d22bfa64dc5f035bae5e5aba78d1552968298
  integral.spinor_genus_count: fe1750cd48cefca58efd06a923fb0c2911f19d1eab128805d31dc7f415314035
  integral.spinor_genera: 5cea719a89bc66be9749c03c4982a1449eb23841a4cd786381d5fc1c1d28849c
  integral.hyperbolic_index: a9ee78511cf3877fba5a29a0cc16e885142c4fe4616999755b7f295060288921
  automorphisms.automorphism_group_generator_morphisms: 1c10a00b9ec90e78464e5540d3160a84890d5960a7a654efba8c5bc85c60c5b2
  integral.discriminant_form: dc8a70d23ba0481785375cb9546459ba03bff4b5525953992d971069fc633888
rank: 4
gram_tensor:
- [2, 0, 0, 0]
- [0, 2, 0, 0]
- [0, 0, 0, 2]
- [0, 0, 2, 0]
signature: [3, 1]
determinant: -16
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0]
- [0, 1/2, 0, 0]
- [0, 0, 0, 1/2]
- [0, 0, 1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  discriminant_group: [2, 2, 2, 2]
  overlattice_count: 11
  delta: 1
  bad_reduction_primes: [2]
  quadratic_character: -4
  genus_symbol: 'II_{3,1} (2: [2^4]_2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  discriminant_form:
    orthogonal_group_order: 12
    isotropic_classes: 4
    isotropic_orbits: 2
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 5NJS
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5NJS
  name: O(L) generator 2
  matrix:
  - [0, -1, 1, 0]
  - [-1, 0, 1, 0]
  - [0, 0, 1, 0]
  - [1, 1, -1, 1]
  scale: 1
- target: 5NJS
  name: O(L) generator 3
  matrix:
  - [-3, 0, 2, -2]
  - [0, 1, 0, 0]
  - [-2, 0, 2, -1]
  - [2, 0, -1, 2]
  scale: 1
- target: 5NJS
  name: O(L) generator 4
  matrix:
  - [0, -1, 0, 0]
  - [-1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5NJS
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 0013.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 0013.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0002, 0013.
