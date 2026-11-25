---
tag: 2DES
name: nipp tbl.480.html:2011
latex: nipp tbl.480.html:2011
aliases: []
certifications:
  derive: e11ba6a59d736b4c26eef1432a3c41f3f6928c0697bdf3c0e192b51a4afd8411
  form.integer_valued: 991ab74e4d8ecc1cc95fc42d3c8bd1b22277777af2fb1942bdd7168c628c4ad4
  integral.elementary_primes: 5734af63b99c8268ffa062a0a0b0b353e42ceb7a04ccb82a40a4a43723482a0f
  integral.genus_symbol: 5414f1f25413cfc9294c998c7951f51d2378d0c7c87b96a866a5c887079482f1
  integral.genus_class_count: beb8597bc4b005fcc203b9e438dcdd83e92843b0af8fbc41fd5ae38d69695ec7
  integral.overlattice_count: 25f88917218322d8f4f757c5b3aba6682f57fdd72d47180d9ce78f772ba8abfd
  integral.spinor_genus_count: cb3117742a2842b93df9613954269af37e13e6844cdf65258bb5b070437758bb
  integral.spinor_genera: ded01941cc246ce6fc8d84b8187cda940a1b71808f7316189025c4f8a45b8638
  integral.hyperbolic_index: b9cde6ce6b833d718c0dee449464d51fda8bd76f2749641853fcecfc61c5272e
  definite.automorphism_group_order: 9008ab9809b37fe3435b532b9be9015d5d38f1387eb55e0fcd976aa8f90c9534
  definite.automorphism_group_generator_morphisms: 9bc196d548f8a055d1cbede46e73c1f5b2d618f44e5a2048546bf311ac7c9172
  integral.discriminant_sequence: 37df01b143bfc62f968a07216b57f83eff5c1e5d658fd8cea9598cec8ac2e2a7
rank: 5
gram_tensor:
- [2, 1, 1, 1, 0]
- [1, 2, 0, 0, 0]
- [1, 0, 6, 0, 0]
- [1, 0, 0, 8, 4]
- [0, 0, 0, 4, 10]
signature: [5, 0]
determinant: 904
definiteness: positive_definite
dual_gram_tensor:
- [96/113, -48/113, -16/113, -15/113, 6/113]
- [-48/113, 161/226, 8/113, 15/226, -3/113]
- [-16/113, 8/113, 43/226, 5/226, -1/113]
- [-15/113, 15/226, 5/226, 20/113, -8/113]
- [6/113, -3/113, -1/113, -8/113, 29/226]
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
    - ['0', -1/2, 1/2, '0', '0']
    - ['0', -1/2, '0', 1/2, '0']
    - [-105/113, 105/226, -39/113, -59/226, 1/226]
    discriminant_quadratic_gram:
    - ['0', 1/2, 1/2]
    - [1/2, 1/2, 1/2]
    - [1/2, 1/2, 189/113]
    discriminant_group_order: 4
    discriminant_generators:
    - - [1, 0, 113]
      - [0, 1, 113]
      - [0, 0, 1]
    - - [1, 0, 113]
      - [0, 1, 113]
      - [0, 0, 225]
    image_generators:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 225]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 225]
    image_order: 2
    kernel_order: 6
    coset_representatives:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    - - [1, 0, 113]
      - [0, 1, 113]
      - [0, 0, 1]
    mm_trivial: false
    image_normal: true
    quotient_generator_cosets: [1, 1]
    quotient_multiplication:
    - [0, 1]
    - [1, 0]
  overlattice_count: 4
  bad_reduction_primes: [2, 113]
  genus_symbol: 'II_{5,0} (2: 1^2 [2^3]_1; 113: 1^-4 113^-1)'
  genus_class_count: 67
  spinor_genus_count: 1
  spinor_genera: [67]
  hyperbolic_index: 0
definite:
  minimum: 2
  kissing_number: 6
  automorphism_group_order: 12
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [-1, 1, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [1, -1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 6, 0, 0, 0, 12, 0, 18]
  root_system: [A2]
  roots:
  - type: A2
    scale: 1
    simple_roots:
    - [0, 1, 0, 0, 0]
    - [1, -1, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1]
morphisms:
- target: 2DES
  name: O(L) generator 1
  matrix:
  - [0, -1, 1, 1, 0]
  - [1, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 2DES
  name: O(L) generator 2
  matrix:
  - [1, 1, 1, 1, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: G. Nipp, Tables of Quaternary and Quinary Quadratic Forms, tbl.480.html:2011.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/tbl.480.html
---

Source entry `nipp:tbl.480.html:2011` gives this Gram tensor.
