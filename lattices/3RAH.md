---
tag: 3RAH
name: Constructed lattice 3RAH
latex: L_{\mathrm{3RAH}}
certifications:
  derive: ce8731f69a68ce91ffa00db22840d5e8b03a575e16fc2aea200f817a37e9b025
  form.integer_valued: 59919d4a98fda2d3af6e271f4a2063e9195a866e2a665ad527017cc99dea69c1
  integral.elementary_primes: 58361296e777d65bd80fcfdde4da555dc6b555019316535422eb9e147ad5db99
  integral.genus_symbol: c90e910764dc5c55ec6e6a175e19dcd7cfac0d39e53bfc8522d039713f8e3797
  integral.genus_class_count: 65656766bb8d2c7e72a32bf40155158f8ae0bf5595ae48828b5aa5422f943e36
  integral.overlattice_count: 06be6a6e3124467050806b4df0c6a6be983ef508682d4ec6f1229a99f1fff830
  integral.spinor_genus_count: 97ce79ce50ef1bf95e716c7ba9b3112db68de17c2ab35c0b1baaabb4558c9107
  integral.spinor_genera: b2dd442996269bdd0e3bc0f62dd284c4f4b50dcf06e89aed3b3c75e91eef0fd6
  automorphisms.automorphism_group_order: 4d356200a7154159cab97c3a6f64090c7f37203df333810b6d05734c673c434f
  automorphisms.automorphism_group_generator_morphisms: 2520ca23b0c4bbf28f9ec15a22db3a2ee3e4160360d36386391bb4aaa56bc5f0
  integral.modular_scale: 38c17c06cef72ff34cfb5225fa5776af1b622aa2f57bd0d87e457cb992f5aeef
  integral.anisotropic_primes: bcba35b5523217d20ef7aa018a31d77d14916a990892949f6974e9591c3013b0
  integral.local_representations: cd85835f30148b238133ec0cf33e64e46e80084cfcb67cfb9128e54866ca4e4f
  integral.local_densities: 8eb1f374f787a9a305f1dee6e8d808752895375a03000938a0aef10e2ba65569
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 2, 0]
- [0, 0, 0, 0, -2]
signature: [3, 2]
determinant: 4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 1/2, 0]
- [0, 0, 0, 0, -1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: false
  discriminant_group: [2, 2]
  overlattice_count: 2
  bad_reduction_primes: [2]
  genus_symbol: 'I_{3,2} (2: [1^3 2^2]_1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [5/4, 1, 1, 35/32, 3/4, 1, 1, 15/16]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17, O(L) generator 18, O(L) generator 19, O(L) generator 20, O(L) generator 21, O(L) generator 22, O(L) generator 23, O(L) generator 24, O(L) generator 25, O(L) generator 26, O(L) generator 27, O(L) generator 28, O(L) generator 29, O(L) generator 30, O(L) generator 31, O(L) generator 32, O(L) generator 33, O(L) generator 34, O(L) generator 35, O(L) generator 36]
indefinite:
  isotropic: true
morphisms:
- target: 3RAH
  name: O(L) generator 1
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 2
  matrix:
  - [1, 2, -2, 0, 0]
  - [2, 1, -2, 0, 0]
  - [2, 2, -3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3RAH
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 2, -2]
  - [0, 0, 1, 2, -2]
  - [0, -1, 1, 1, 0]
  - [0, -1, 1, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 2, -2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 2, -2]
  - [-1, 0, 1, 1, 0]
  - [-1, 0, 1, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 8
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 2, -2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, -2, 2]
  - [-1, 0, -1, 1, 0]
  - [-1, 0, -1, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 2, 2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [1, 0, 0, 0, 1]
  - [-1, 0, 0, -1, -2]
  scale: 1
- target: 3RAH
  name: O(L) generator 11
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, -2, -2]
  - [0, 0, -1, -2, -1]
  - [0, 0, 1, 1, 0]
  scale: 1
- target: 3RAH
  name: O(L) generator 12
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, -2, -2]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 1]
  - [0, 1, 0, -1, -2]
  scale: 1
- target: 3RAH
  name: O(L) generator 13
  matrix:
  - [-1, 0, 0, 2, 2]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [1, 0, 0, 0, -1]
  - [-1, 0, 0, 1, 2]
  scale: 1
- target: 3RAH
  name: O(L) generator 14
  matrix:
  - [3, 2, 2, 0, 4]
  - [-2, 1, -2, 0, 0]
  - [-2, -2, -1, 0, -4]
  - [0, 0, 0, -1, 0]
  - [-2, 0, -2, 0, -1]
  scale: 1
- target: 3RAH
  name: O(L) generator 15
  matrix:
  - [0, -1, 0, 0, 0]
  - [-1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 16
  matrix:
  - [3, 2, 2, 0, -4]
  - [-2, 1, -2, 0, 0]
  - [-2, -2, -1, 0, 4]
  - [0, 0, 0, -1, 0]
  - [2, 0, 2, 0, -1]
  scale: 1
- target: 3RAH
  name: O(L) generator 17
  matrix:
  - [1, 2, -2, 0, 0]
  - [-2, 3, -2, 0, -4]
  - [-2, 2, -1, 0, -4]
  - [0, 0, 0, 1, 0]
  - [0, -2, 2, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 18
  matrix:
  - [1, -2, 2, 0, 0]
  - [-2, 1, -2, 0, 0]
  - [-2, 2, -3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 19
  matrix:
  - [0, 1, 0, 0, 0]
  - [-1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3RAH
  name: O(L) generator 20
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 3, 0, 0, -4]
  - [0, 0, 3, -4, 0]
  - [0, 0, -2, 3, 0]
  - [0, -2, 0, 0, 3]
  scale: 1
- target: 3RAH
  name: O(L) generator 21
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 2, -2]
  - [0, 0, -1, -2, 2]
  - [0, -1, -1, -1, 0]
  - [0, -1, -1, 0, -1]
  scale: 1
- target: 3RAH
  name: O(L) generator 22
  matrix:
  - [1, 2, -2, 0, 0]
  - [-2, 3, -2, 0, 4]
  - [-2, 2, -1, 0, 4]
  - [0, 0, 0, 1, 0]
  - [0, 2, -2, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 23
  matrix:
  - [3, 0, 0, 0, -4]
  - [0, 1, 0, 0, 0]
  - [0, 0, 3, -4, 0]
  - [0, 0, -2, 3, 0]
  - [-2, 0, 0, 0, 3]
  scale: 1
- target: 3RAH
  name: O(L) generator 24
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 2, 2]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 1]
  - [0, -1, 0, -1, -2]
  scale: 1
- target: 3RAH
  name: O(L) generator 25
  matrix:
  - [1, 2, 2, 0, 0]
  - [-2, -1, -2, 0, 0]
  - [2, 2, 3, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3RAH
  name: O(L) generator 26
  matrix:
  - [1, 2, 2, 0, 0]
  - [-2, 3, 2, 0, -4]
  - [2, -2, -1, 0, 4]
  - [0, 0, 0, 1, 0]
  - [0, -2, -2, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 27
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3RAH
  name: O(L) generator 28
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3RAH
  name: O(L) generator 29
  matrix:
  - [3, 2, -2, 0, 4]
  - [-2, 1, 2, 0, 0]
  - [2, 2, -1, 0, 4]
  - [0, 0, 0, 1, 0]
  - [2, 0, -2, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 30
  matrix:
  - [1, 4, 0, 2, -6]
  - [-4, 1, 4, 0, 0]
  - [0, 4, 1, 2, -6]
  - [-1, 0, 1, 1, 0]
  - [-3, 0, 3, 0, 1]
  scale: 1
- target: 3RAH
  name: O(L) generator 31
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -3, 0, 0, -4]
  - [0, 0, -3, 4, 0]
  - [0, 0, 2, -3, 0]
  - [0, -2, 0, 0, -3]
  scale: 1
- target: 3RAH
  name: O(L) generator 32
  matrix:
  - [-1, 0, 0, -2, 2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-1, 0, 0, 0, 1]
  - [-1, 0, 0, -1, 2]
  scale: 1
- target: 3RAH
  name: O(L) generator 33
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, -2, 2]
  - [0, 0, 1, 0, 0]
  - [0, -1, 0, 0, 1]
  - [0, -1, 0, -1, 2]
  scale: 1
- target: 3RAH
  name: O(L) generator 34
  matrix:
  - [0, 0, 1, 2, 0]
  - [0, 1, 0, 0, 0]
  - [-1, 0, 0, 0, 2]
  - [1, 0, 0, 0, -1]
  - [0, 0, 1, 1, 0]
  scale: 1
- target: 3RAH
  name: O(L) generator 35
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 2, 0]
  - [0, -1, 0, 0, 2]
  - [0, -1, 0, 0, 1]
  - [0, 0, 1, 1, 0]
  scale: 1
- target: 3RAH
  name: O(L) generator 36
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 0002, 3ICX.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 0002, 3ICX.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 0002, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 0002, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 3ICW, 0002, 3ICX.
