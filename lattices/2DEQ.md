---
tag: 2DEQ
name: nipp tbl.480.html:2009
latex: nipp tbl.480.html:2009
aliases: []
certifications:
  derive: 925241269a806c03a64fbeeb686d3d6b3f69823212c9bd0df7d876f498d005b6
  form.integer_valued: a4f57b4081b6348cfbe63cc8cdff3148074a9d6c676c95c15a27c4871b0e1e24
  integral.elementary_primes: cbc3ed36197c251d87787ce81afed1cb9a47fcf4cd0e11e7ebf322a19acaba03
  integral.genus_symbol: c78810d34bfec608dd7c5f65c83284f3275a776f69b4eb66ca470538be57e855
  integral.genus_class_count: 6905e96055a8c206a9cba75dc59d4db73f850e9d973a2374173b8c02e7160dcc
  integral.overlattice_count: 91fd39c2f6e8c5b5b65aaa36e169364790509a9c9c682e3ca4a8a45ace801788
  integral.spinor_genus_count: b851653b2c4b01832d38b6db6da15bbb8feda5517e7b08805863d355c5022a64
  integral.spinor_genera: 8c526ebe2a6fee334f93a5683fe678f724aa00779efff61bb70bc4884743ac3c
  integral.hyperbolic_index: d2a3b15fd4219c9ac58571410dcbc72f12406a5ab7cc4bff123c4b8f5dc644c3
  definite.automorphism_group_order: dceeefde378565094f2111141386ecdf3809aa5e74689e653de48ee2e20b9ea6
  definite.automorphism_group_generator_morphisms: d7b50a55bfa3014e4d2499cbdffc996901e793f6b7df3abfd7574c19b0793b91
  integral.discriminant_sequence: 812b789686b22630d0bf915d299d154b19b154e7c9a3c86de0779b13493e0776
rank: 5
gram_tensor:
- [2, 0, 1, 0, 1]
- [0, 2, 1, 0, 1]
- [1, 1, 6, 1, 0]
- [0, 0, 1, 8, -3]
- [1, 1, 0, -3, 8]
signature: [5, 0]
determinant: 904
definiteness: positive_definite
dual_gram_tensor:
- [137/226, 12/113, -13/113, -5/226, -11/113]
- [12/113, 137/226, -13/113, -5/226, -11/113]
- [-13/113, -13/113, 47/226, -2/113, 5/226]
- [-5/226, -5/226, -2/113, 17/113, 7/113]
- [-11/113, -11/113, 5/226, 7/113, 39/226]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 452
  discriminant_group: [2, 2, 226]
  discriminant_sequence:
    discriminant_factors: [2, 2, 226]
    discriminant_basis_lifts:
    - ['60', '36', 1/2, '0', -1/2]
    - [-1/2, '0', '0', 1/2, '0']
    - [-73/226, -73/226, -81/226, -23/113, 1/226]
    discriminant_quadratic_gram:
    - [3/2, '0', 1/2]
    - ['0', 1/2, 1/2]
    - [1/2, 1/2, 29/226]
    discriminant_group_order: 4
    discriminant_generators:
    - - [1, 0, 0]
      - [1, 1, 113]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [1, 1, 113]
      - [0, 0, 225]
    image_generators:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 225]
    - - [1, 0, 0]
      - [1, 1, 113]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 225]
    image_order: 4
    kernel_order: 4
    coset_representatives:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0, 0]
    quotient_multiplication:
    - [0]
  overlattice_count: 4
  bad_reduction_primes: [2, 113]
  genus_symbol: 'II_{5,0} (2: 1^2 [2^3]_1; 113: 1^-4 113^-1)'
  genus_class_count: 67
  spinor_genus_count: 1
  spinor_genera: [67]
  hyperbolic_index: 0
definite:
  minimum: 2
  kissing_number: 4
  automorphism_group_order: 16
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 4, 0, 4, 0, 8, 0, 14]
  root_system: [A1, A1]
  roots:
  - type: B2
    scale: 1
    simple_roots:
    - [0, 1, 0, 0, 0]
    - [1, -1, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1]
morphisms:
- target: 2DEQ
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 2DEQ
  name: O(L) generator 2
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 2DEQ
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, -1, 0, -1]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 2DEQ
  name: O(L) generator 4
  matrix:
  - [1, 0, 1, 0, 1]
  - [0, 1, 1, 0, 1]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: G. Nipp, Tables of Quaternary and Quinary Quadratic Forms, tbl.480.html:2009.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/tbl.480.html
---

Source entry `nipp:tbl.480.html:2009` gives this Gram tensor.
