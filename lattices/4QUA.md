---
tag: 4QUA
name: Constructed lattice 4QUA
latex: L_{\mathrm{4QUA}}
certifications:
  derive: 2843d88080f85e442700ae340043e6de435680ba7df9ddb005f4e9a1f27827b2
  form.integer_valued: a0c5306d97bee001d5882c68c8f4d8372c55ca133bffdcc59cd6bb94fc5f008f
  integral.elementary_primes: 0b36f4812aef78905d938d18fc8827fdaab7fd7ff9c8450bdac4c8ec6976314d
  integral.genus_symbol: 46e6ee7f7d1d293a8b5f52bfa8c35b600af75e2b11b42adc8cc2706ef8c58b3c
  integral.genus_class_count: 30d92f17e2278dd918d71b6d2ca8a77df2a2fb2337252eb96049ad9b67eea901
  integral.overlattice_count: 3148a8adff031df104a6fc4133c006e7709b38acb822734d8c727bae06d8e400
  integral.spinor_genus_count: 5513d657ae7fa89b9454d4d5a50bd21eaa560bc13857c40e6222079fa8fcaaa3
  integral.spinor_genera: 2483b6cb5c1defabec86bb1c5b97d846786eff92cc3eab478ca86569fab0dbdc
  integral.hyperbolic_index: 2edd014d47c06f0bbbfd18935f3ec0952a438f4f41828b74e60e1f1aba58a19a
  definite.automorphism_group_order: 73e03a430115d98eda6d494aa8ab21dfb7554011dd9c9a9ec3bc4f16959af0ad
  definite.automorphism_group_generator_morphisms: 501d2977ffb7e807975adca40dc461e0c5faf38099c37af7caf2bf00461fd1ce
  integral.discriminant_sequence: 0e45903ea0b9afa00a2aec12a84e986c58e1f78fb7fbf088da2418c1b557741f
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 2, -3, 0, 0]
- [0, -3, 6, 0, 0]
- [0, 0, 0, 2, -3]
- [0, 0, 0, -3, 6]
signature: [5, 0]
determinant: 9
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 2, 1, 0, 0]
- [0, 1, 2/3, 0, 0]
- [0, 0, 0, 2, 1]
- [0, 0, 0, 1, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  discriminant_group: [3, 3]
  discriminant_sequence:
    discriminant_factors: [3, 3]
    discriminant_basis_lifts:
    - ['0', '0', -1/3, '0', '0']
    - ['0', '0', '0', '0', 1/3]
    discriminant_quadratic_gram:
    - [2/3, '0']
    - ['0', 2/3]
    discriminant_group_order: 8
    discriminant_generators:
    - - [0, 1]
      - [2, 0]
    - - [2, 0]
      - [0, 1]
    image_generators:
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 2]
    - - [1, 0]
      - [0, 2]
    - - [0, 1]
      - [1, 0]
    image_order: 8
    kernel_order: 72
    coset_representatives:
    - - [1, 0]
      - [0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0, 0]
    quotient_multiplication:
    - [0]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{5,0} (2: [1^5]_1; 3: 1^3 3^2)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 576
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 12, 24, 38, 72, 36, 24, 156]
  root_system: [A2, A2]
  roots:
  - type: G2
    scale: 1
    simple_roots:
    - [0, 0, 0, 1, 0]
    - [0, 0, 0, 0, 1]
  - type: G2
    scale: 1
    simple_roots:
    - [0, 1, 0, 0, 0]
    - [0, 0, 1, 0, 0]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [1, 2]
morphisms:
- target: 4QUA
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4QUA
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 2, -3]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4QUA
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -3]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4QUA
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, -1, 2]
  - [0, 2, -3, 0, 0]
  - [0, 1, -1, 0, 0]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID4, 3ID4.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID4, 3ID4.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ID4, 3ID4.
