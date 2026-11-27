---
tag: 4ZUC
name: Constructed lattice 4ZUC
latex: L_{\mathrm{4ZUC}}
certifications:
  derive: 41aba5e127a32bece794325463c909de15115579bf8ba6a331e56b26cb82899f
  form.integer_valued: 05724ae545ac84208d8d4586ecaa461c5a0ff5751f26c42d047b4b37479f09f2
  integral.elementary_primes: 15c28b1ad4e32a4deee83dc12f6437cb0a03cdd7a35bf362406f90f286d652fa
  integral.genus_symbol: 293a4cdb55837e355cb39d112aeaf5d91aaa6ef35e9420520a34d3e06a13f27c
  integral.genus_class_count: 7bff1a0dd8922ecf7286683d665b11816502aafb0c9413e9bb245a480e1acb89
  integral.overlattice_count: c454e29021a263495b062a3687cd7502ee616b15a37a0527276e8b1248843cec
  integral.spinor_genus_count: 4609ae1b3aa97d9e420412ec51038d011d7a3348caec95aed6f665dc1e449e5a
  integral.spinor_genera: 6614b0c023d887f14d19d3ddb8bffeb5701eba8c4e903a631f66687434b39cdf
  integral.hyperbolic_index: 1197ed20181e1b7e2d7a102b69cd006ecec2c2b44636a7504f4cad69ea43df80
  definite.automorphism_group_order: 275aa4814d78e923abc8c249fcbe0a8d33c77186442223c5eade4d996a59c812
  definite.automorphism_group_generator_morphisms: cb961bd40a610707ee4991a78f8ded6dc32f62c21a3e890d6a67c11d31578b77
  integral.discriminant_sequence: 62b78bbb86a07f08d4c7b75c3f191e153323a99022883ece534a7fff03234cc7
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, -4, 6]
- [0, 0, 0, 6, -12]
signature: [0, 5]
determinant: -24
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, -1, -1/2]
- [0, 0, 0, -1/2, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  discriminant_group: [2, 2, 6]
  discriminant_sequence:
    discriminant_factors: [2, 2, 6]
    discriminant_basis_lifts:
    - ['0', '0', 1/2, '0', '0']
    - ['0', '0', '0', 1/2, '0']
    - ['0', '0', '0', '0', 1/6]
    discriminant_quadratic_gram:
    - [1/2, '0', '0']
    - ['0', '0', 1/2]
    - ['0', 1/2, 2/3]
    discriminant_group_order: 12
    discriminant_generators:
    - - [1, 0, 0]
      - [0, 1, 3]
      - [0, 1, 4]
    - - [1, 0, 0]
      - [0, 1, 3]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 1, 3]
      - [0, 0, 5]
    image_generators:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 0, 3]
      - [0, 1, 5]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 1, 5]
    image_order: 12
    kernel_order: 16
    coset_representatives:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0, 0, 0]
    quotient_multiplication:
    - [0]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{0,5} (2: [1^-2 2^3]_1; 3: 1^-4 3^-1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 4
  automorphism_group_order: 192
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 4, 6, 8, 18, 32, 44, 64, 78]
  root_system: [A1, A1, A1]
  roots:
  - type: B2
    scale: -1/2
    simple_roots:
    - [0, 1, 0, 0, 0]
    - [1, -1, 0, 0, 0]
  - type: G2
    scale: -2
    simple_roots:
    - [0, 0, 0, 1, 0]
    - [0, 0, 0, 0, 1]
  - type: A1
    scale: -1
    simple_roots:
    - [0, 0, 1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [-1, -2, -4]
morphisms:
- target: 4ZUC
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4ZUC
  name: O(L) generator 2
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4ZUC
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4ZUC
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 2, -3]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4ZUC
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -3]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICX, 3ID5.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICX, 3ID5.
- tag: 3ID5
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICX, 3ID5.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICW, 3ICX, 3ID5.
