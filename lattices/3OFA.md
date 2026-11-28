---
tag: 3OFA
name: Constructed lattice 3OFA
latex: L_{\mathrm{3OFA}}
certifications:
  derive: 51ee8662c7c84cd44eb0a0c758f9b4cd06f7bc7479781ac6a6915479d5cfb4b4
  form.integer_valued: 15b24c9863dc8056913bfc3a541c0ab96b29986881b49f675fbe3ba358643930
  integral.elementary_primes: 95de3d3eec23ae986e83054dc31c7062a120fb126d037a49ae58c1fc45e6e017
  integral.genus_symbol: a8879bbb9bc2f4808d21014c623246112a49ab48a0cbc90023983565712a03b3
  integral.genus_class_count: d431ce2497eac67edb97ccda39cb325f99068e1bec1bece2b170c33c1b864768
  integral.overlattice_count: a77c096524e282919ab3443f8ef0993e217b11362af09e868ce1447bbb344f24
  integral.spinor_genus_count: 75474ef31e0c1bf3c4c13d1447a349f9d5e299b3961d06216f5e7d23556265e0
  integral.spinor_genera: 984e0a1b95156b1c4062e11fcf6bb2bcf25d8b926c1b0eea671c2e3a6b0acb0e
  integral.hyperbolic_index: 6949fea9eb6f2969a2452811e321d44c601fa7f537f3a5ed64d8e0c2b10589ae
  automorphisms.automorphism_group_order: 6761dd12a18441ab87c59652dc631446f84fc2a33025a1968d64aabffc775675
  automorphisms.automorphism_group_generator_morphisms: b4c6981a4d65130c5679be70feae646f30561a412ca6366e6e1fd55376e8eb89
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 0, 0, 0, 1]
- [0, 0, 0, 1, 0]
signature: [4, 1]
determinant: -1
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 0, 0, 0, 1]
- [0, 0, 0, 1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 2
  discriminant_group: []
  overlattice_count: 1
  bad_reduction_primes: [2]
  genus_symbol: I_{4,1}
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
- target: 3OFA
  name: O(L) generator 1
  matrix:
  - [0, -1, 0, 0, 1]
  - [-1, 0, 0, 0, 1]
  - [0, 0, 1, 0, 0]
  - [1, 1, 0, 1, -1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3OFA
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 3OFA
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3OFA
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3OFA
  name: O(L) generator 5
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0001, 0016.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0001, 0016.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 0001, 0016.
