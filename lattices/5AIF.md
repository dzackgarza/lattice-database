---
tag: 5AIF
name: Constructed lattice 5AIF
latex: L_{\mathrm{5AIF}}
certifications:
  derive: afdf7552c55c6925b11c4265df3fabc386a1d4f0cd9f17d0bbb33000078a4db9
  form.integer_valued: c11e3051f7e549401640fd475ae0291ac4ef4d20cdd8700cbc070eecad6b2b5f
  integral.elementary_primes: cb3aa8f481d1ef65dd627d650e5d3011b74dac7b50e5e11a79cce321786dce69
  integral.genus_symbol: de6d998ab67b24392dae62dc5fa7440888bb6ffd1b2d2354a5bae57271e0d687
  integral.genus_class_count: 938dcffa2aacd2468e068388144f7f2c512b0336636cac08a904e1071081bbae
  integral.overlattice_count: da7a31aeeb075f5b69930978eec0b7df685e345ecf028e6854fbc4e67f62bb46
  integral.spinor_genus_count: d75cf657a419b91c29577416241186e68e472253f48520880c13a4aaa36370cb
  integral.spinor_genera: c5cbebfde69c7b4341d4bd2078d6cb1f6f371d40c62b433ace85e390201da979
  integral.hyperbolic_index: 113be6a9ae594fbfa65bf4f5c84e4ab2141ae48212143e1111bd726eda085cca
  automorphisms.automorphism_group_order: 2d2c2905591b45962f545bf5e494e766aa5bc8d61461be716b2f6e7f994a508f
  automorphisms.automorphism_group_generator_morphisms: 8a3864166eb0be58fd5cd119c33aab2e15fcce9b7cc5773a3f243bbbae5171ed
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -2, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, 0, -2]
- [0, 0, 0, -2, 0]
signature: [1, 4]
determinant: 16
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1/2, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, 0, -1/2]
- [0, 0, 0, -1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  discriminant_group: [2, 2, 2, 2]
  overlattice_count: 11
  bad_reduction_primes: [2]
  genus_symbol: 'I_{1,4} (2: [1^1 2^4]_5)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11]
indefinite:
  isotropic: true
morphisms:
- target: 5AIF
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5AIF
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, -1]
  - [0, 1, 0, 0, 1]
  - [0, -1, 1, 1, -1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5AIF
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -3, 0, 2, -2]
  - [0, 0, 1, 0, 0]
  - [0, -2, 0, 2, -1]
  - [0, 2, 0, -1, 2]
  scale: 1
- target: 5AIF
  name: O(L) generator 4
  matrix:
  - [-17, -24, 0, 24, -24]
  - [-12, -15, 0, 16, -16]
  - [0, 0, 1, 0, 0]
  - [-12, -16, 0, 17, -16]
  - [12, 16, 0, -16, 17]
  scale: 1
- target: 5AIF
  name: O(L) generator 5
  matrix:
  - [-1, -4, 0, 4, -2]
  - [-2, -3, 0, 4, -2]
  - [0, 0, 1, 0, 0]
  - [-1, -2, 0, 3, -1]
  - [2, 4, 0, -4, 3]
  scale: 1
- target: 5AIF
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 1, 0]
  - [0, 1, 0, -1, 0]
  - [0, 0, 0, 1, 0]
  - [0, 1, -1, -1, 1]
  scale: 1
- target: 5AIF
  name: O(L) generator 7
  matrix:
  - [-7, -4, 4, 8, -8]
  - [-2, 0, 1, 2, -2]
  - [2, 1, 0, -2, 2]
  - [-4, -2, 2, 5, -4]
  - [4, 2, -2, -4, 5]
  scale: 1
- target: 5AIF
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5AIF
  name: O(L) generator 9
  matrix:
  - [-1, -2, 2, 2, -2]
  - [0, -1, 0, 1, 0]
  - [2, 2, -1, -3, 2]
  - [-1, -1, 1, 2, -1]
  - [2, 3, -1, -3, 3]
  scale: 1
- target: 5AIF
  name: O(L) generator 10
  matrix:
  - [-7, -8, 0, 10, -8]
  - [-2, -1, 0, 2, -2]
  - [0, 0, 1, 0, 0]
  - [-2, -2, 0, 3, -2]
  - [7, 8, 0, -9, 9]
  scale: 1
- target: 5AIF
  name: O(L) generator 11
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ICX, 3ICZ.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ICX, 3ICZ.
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ICX, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICX, 3ICX, 3ICZ.
