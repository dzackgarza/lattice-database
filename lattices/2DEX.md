---
tag: 2DEX
name: nipp tbl.480.html:2016
latex: nipp tbl.480.html:2016
aliases: []
certifications:
  derive: 8eb90e98723b73b3fda07751c23e6603021c8f469fc37ea77ef80007f2d26a90
  form.integer_valued: 5ae6419be11e21aa66af7fc8d377be3fa1b9d56500cf5f079a728dc096a9ccab
  integral.elementary_primes: 326549f63da4b09c19b0b7eef541115c5d61e606ec2e0ea02dcf4a28f1ed5a7d
  integral.genus_symbol: 83f7a9651215585c115da391a09446c50a7f5cdc8992174b37bd67d0576c0039
  integral.genus_class_count: 26d20d342e246a28d305239d8d1e05a606d7e7695a27eae23a2ca18271df27ee
  integral.overlattice_count: 635b79bb740e7dfa0f36f07fe4ce94aa464dbc596609439d077d410a9737e01d
  integral.spinor_genus_count: d96a962ce0f102075cb6bd640dca0f5c020d0d70244f306f500bce6588e0e99b
  integral.spinor_genera: b44ce5cc036bcc8379202eb7dcabfb54e8c2ff02de09295b7a9414ca6bf9f242
  integral.hyperbolic_index: 038b1aa41af03261732657dce8393b8b3e4eeaee5f35aa77a6983decb38024bc
  definite.automorphism_group_order: 37e2d0e52ebc3077621473735967dfe3694e220b7b89bbbba8e56e991b3f51d0
  definite.automorphism_group_generator_morphisms: 68b5578f28c47be8545965faa2865554015eeccad67033997e00a80fe50dfaa0
  integral.discriminant_sequence: 8271d1faf929427645e66d42d341505955c6010bd32cb5633529afe54b849d85
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 4, 0, 1, 2]
- [0, 0, 4, 0, 2]
- [0, 1, 0, 6, 3]
- [0, 2, 2, 3, 8]
signature: [5, 0]
determinant: 904
definiteness: positive_definite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 33/113, 9/226, -1/113, -9/113]
- [0, 9/226, 34/113, 5/113, -23/226]
- [0, -1/113, 5/113, 24/113, -10/113]
- [0, -9/113, -23/226, -10/113, 23/113]
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
    - ['0', '0', 1/2, '0', '0']
    - [-1/2, 1/2, '0', '0', -1/2]
    - ['0', 79/226, 57/226, 69/113, -1/226]
    discriminant_quadratic_gram:
    - ['1', 1/2, 1/2]
    - [1/2, 1/2, 1/2]
    - [1/2, 1/2, 156/113]
    discriminant_group_order: 4
    discriminant_generators:
    - - [1, 0, 0]
      - [1, 1, 0]
      - [1, 0, 1]
    - - [1, 0, 0]
      - [1, 1, 0]
      - [1, 0, 225]
    image_generators:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 225]
    - - [1, 0, 0]
      - [1, 1, 0]
      - [1, 0, 225]
    - - [1, 0, 0]
      - [1, 1, 0]
      - [1, 0, 1]
    image_order: 4
    kernel_order: 2
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
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 2, 0, 4, 0, 10, 0, 24]
  root_system: [A1]
  roots:
  - type: A1
    scale: 2
    simple_roots:
    - [0, 0, 1, 0, 0]
  - type: A1
    scale: 1
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1]
morphisms:
- target: 2DEX
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 2DEX
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 1]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 2DEX
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, -1]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
families: []
related: []
references:
- citation: G. Nipp, Tables of Quaternary and Quinary Quadratic Forms, tbl.480.html:2016.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/tbl.480.html
---

Source entry `nipp:tbl.480.html:2016` gives this Gram tensor.
