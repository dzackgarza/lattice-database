---
tag: 4LSW
name: Constructed lattice 4LSW
latex: L_{\mathrm{4LSW}}
certifications:
  derive: eb0243a030ff7d005ab482df59a8939edc5d8e24f0ba8d7b116d6a0d9e2e71fe
  form.integer_valued: 968bb46607f9d2ca520bc0b64980f201e44ac4c426ee8d84c73af35c8741ebe4
  integral.elementary_primes: 230d8a8be44e5bfd6706630da1013bbede8eac90ba22c8d03dd066229fc7c67f
  integral.genus_symbol: 75f54e2ecb068ee9f1cdbc7248c98aee89ab45937413e2b3b570334da3a7e3bc
  integral.genus_class_count: aa77a78c5d7e4dabb089d6a55636597dfdb7c4b20b41eda0e16dd87587d81aba
  integral.overlattice_count: 2df7ee1083d0cb989f33fd90780f171becb640207bdd7e376eca0c27a8524800
  integral.spinor_genus_count: 68c82252b72fe0eb87164589d31c25e1bcd4591fa8d9aba47e46fec23aee0493
  integral.spinor_genera: 25b727bcf2d1ecb9189bbb6d72177e4844817504d8d4efce344b2674d8e0a8a9
  integral.hyperbolic_index: 2f66ef4cb640e18286c7f159d2bb1fa72b24bd46b2646f049d93241f427dd5d5
  automorphisms.automorphism_group_generator_morphisms: 725b1b29420062490d8e876bfc48e046b56499dc57a780c36dfd3dfceeb69436
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, 2, -1]
- [0, 0, -1, 2]
signature: [3, 1]
determinant: -6
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, 2/3, 1/3]
- [0, 0, 1/3, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  discriminant_group: [6]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  quadratic_character: -24
  genus_symbol: 'I_{3,1} (2: [1^-3 2^1]_0; 3: 1^-3 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11]
indefinite:
  isotropic: true
morphisms:
- target: 4LSW
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 4LSW
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, -1]
  scale: 1
- target: 4LSW
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 4LSW
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 4LSW
  name: O(L) generator 5
  matrix:
  - [-17, -24, 0, 0]
  - [12, 17, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4LSW
  name: O(L) generator 6
  matrix:
  - [-1, -4, 2, 2]
  - [2, 5, -2, -2]
  - [2, 4, -1, -2]
  - [2, 4, -2, -1]
  scale: 1
- target: 4LSW
  name: O(L) generator 7
  matrix:
  - [-3, -4, 0, 0]
  - [2, 3, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4LSW
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4LSW
  name: O(L) generator 9
  matrix:
  - [-1, -4, 2, 2]
  - [2, 5, -2, -2]
  - [0, 0, 1, -1]
  - [-2, -4, 2, 1]
  scale: 1
- target: 4LSW
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0]
  - [0, 7, -6, 0]
  - [0, 8, -7, 0]
  - [0, 4, -3, -1]
  scale: 1
- target: 4LSW
  name: O(L) generator 11
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 0012.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 0012.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 0012.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICX, 0012.
