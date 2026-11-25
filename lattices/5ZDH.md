---
tag: 5ZDH
name: Constructed lattice 5ZDH
latex: L_{\mathrm{5ZDH}}
certifications:
  derive: 42e910d913df38a3340b31f59194b861e5ddbd07ba8422274fed3d72aa703c8c
  form.integer_valued: eebc734ea62f092f368aded86942dea8a5727dab184699d6c5de9b498375710c
  integral.elementary_primes: 3025760f0210d86d32852b0dc4c8e68b64ec0dd3b4491b055988b39076c66f74
  integral.genus_symbol: 6d5bb1f4bc70dd0abaeb8da7e7b270258dddfe1ba210926badb60da866e7e1e0
  integral.genus_class_count: 2b51881f0954e31efdf0e1bdc5099e4e95e4dc1be1b202334ae353df28833257
  integral.overlattice_count: 79117b5459dd6367289f16854556fa4dd8d54bccbe5586150c0416a525927ef6
  integral.spinor_genus_count: 7fb91d81cdf5955311047b36b5820e759c66622fedee57bc0b9b154fe4dd212e
  integral.spinor_genera: 7a660de39f118abddd49d4775db7ac903b2a6914488fa440057e7bd2f1f15016
  integral.hyperbolic_index: 0094ea11c76c80cfe05a37b67e82a7eaaf2e5e226c0a5b51a7a92872a40d842c
  definite.automorphism_group_order: 139e6bda9b138f4378b7b4c306c4a15edb71e5feb4f26adccc38b925f4a2404e
  definite.automorphism_group_generator_morphisms: 0d52c4aa3db95862326ba5c7c27f7b6ee806eb49c02d432cb8be86db48d5aa4b
  integral.discriminant_sequence: f7a4c9dcadab6db9af74b5c5d27f3ee9881910cdcd452dd7f735445932a3d49c
rank: 5
gram_tensor:
- [-2, 0, 0, 0, 0]
- [0, -2, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, -2, 1]
- [0, 0, 0, 1, -2]
signature: [0, 5]
determinant: -24
definiteness: negative_definite
dual_gram_tensor:
- [-1/2, 0, 0, 0, 0]
- [0, -1/2, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, -2/3, -1/3]
- [0, 0, 0, -1/3, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  discriminant_group: [2, 2, 6]
  discriminant_sequence:
    discriminant_factors: [2, 2, 6]
    discriminant_basis_lifts:
    - ['0', '0', 1/2, '0', '0']
    - ['-1', 3/2, '0', '1', '-1']
    - [-1/2, 1/2, '0', 1/3, -1/3]
    discriminant_quadratic_gram:
    - [3/2, '0', '0']
    - ['0', 3/2, 1/2]
    - ['0', 1/2, 1/3]
    discriminant_group_order: 12
    discriminant_generators:
    - - [1, 0, 0]
      - [0, 1, 3]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 1, 3]
      - [0, 0, 5]
    - - [0, 1, 0]
      - [1, 0, 0]
      - [1, 1, 5]
    image_generators:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 5]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 5]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    - - [0, 1, 0]
      - [1, 0, 0]
      - [1, 1, 1]
    - - [0, 1, 3]
      - [0, 1, 0]
      - [1, 1, 4]
    image_order: 12
    kernel_order: 48
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
  genus_symbol: 'II_{0,5} (2: 1^-2 [2^3]_5; 3: 1^4 3^1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 2
  kissing_number: 12
  automorphism_group_order: 576
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, -1]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, 1]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 12, 0, 48, 0, 86, 0, 96]
  root_system: [A2, A1, A1, A1]
  roots:
  - type: B3
    scale: -1
    simple_roots:
    - [1, -1, 0, 0, 0]
    - [0, 1, -1, 0, 0]
    - [0, 0, 1, 0, 0]
  - type: G2
    scale: -1
    simple_roots:
    - [0, 0, 0, 0, 1]
    - [0, 0, 0, 1, -1]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [-2]
morphisms:
- target: 5ZDH
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 5ZDH
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5ZDH
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5ZDH
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5ZDH
  name: O(L) generator 5
  matrix:
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICX, 3ICX, 3ICX, 3ID0.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 3ICX, 3ICX, 3ICX, 3ID0.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICX, 3ICX, 3ICX, 3ID0.
