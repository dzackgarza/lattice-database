---
tag: 5XPP
name: Constructed lattice 5XPP
latex: L_{\mathrm{5XPP}}
certifications:
  derive: d05559dc4f6125f9049f342b7a61b9d7f10c08366e2784a5d5c04ca857a54baf
  form.integer_valued: 7182f7cb9af0cb4667401f3d54bc19137576d2fbd0ccb4e24e734c49882df40a
  integral.elementary_primes: f58a32964caa63d1479657f8d045d9c51eb9a530ecd39e97edab5e36ba10f8c2
  integral.genus_symbol: f083ad53ba1d8d751e4be9209a4db9751df61e9c725ef93ff5e7d2d0b0def1dd
  integral.genus_class_count: be3120a63ab4eb4b077df12238f4a64fa0611563e275863bec9359dce2ab93d3
  integral.overlattice_count: e646c7c90684d2944e1917ce3573bdb105916abcd8f5e8a9fb63468c7bda7d5d
  integral.spinor_genus_count: 2eace29aeec3fc2580e59ed81b7e1ce7781b8fcf9d550321e5f5aa46f683cdf0
  integral.spinor_genera: e8508e687d8f183081d6cb3aed5a1c93cb8c988f14a93883459cd3c99682e80d
  integral.hyperbolic_index: 0e7d8222d1afdc71581c9d82086e6011b94ce792ce4bbc223dd284adb04df404
  definite.automorphism_group_order: e1bd0d7c849449458c4dea123fd002fa60a17c9abe4e6ff6d9ebc5d129b9581e
  definite.automorphism_group_generator_morphisms: 6722a818b50698b252ce4e7d95290791c6cc32f924ab97ef40cd8e37381d7e18
  integral.discriminant_sequence: ae847c7667fd448a9a48e981c7298d6a2d3d6103365622833f8f2763580e8653
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 2, -3, 0, 0]
- [0, -3, 6, 0, 0]
- [0, 0, 0, 4, -6]
- [0, 0, 0, -6, 12]
signature: [5, 0]
determinant: 72
definiteness: positive_definite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 2, 1, 0, 0]
- [0, 1, 2/3, 0, 0]
- [0, 0, 0, 1, 1/2]
- [0, 0, 0, 1/2, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  discriminant_group: [2, 6, 6]
  discriminant_sequence:
    discriminant_factors: [2, 6, 6]
    discriminant_basis_lifts:
    - [-3/2, '0', '-1', 1/2, '0']
    - [1/2, '0', 1/3, '0', '0']
    - ['0', '0', '0', '0', 1/6]
    discriminant_quadratic_gram:
    - [3/2, 1/2, 1/2]
    - [1/2, 7/6, '0']
    - [1/2, '0', 1/3]
    discriminant_group_order: 24
    discriminant_generators:
    - - [1, 0, 3]
      - [0, 5, 0]
      - [1, 3, 4]
    - - [1, 0, 3]
      - [0, 5, 0]
      - [1, 3, 2]
    - - [1, 0, 3]
      - [0, 5, 0]
      - [0, 0, 1]
    image_generators:
    - - [1, 0, 0]
      - [0, 5, 0]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 5, 0]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    - - [0, 3, 3]
      - [0, 1, 0]
      - [1, 3, 5]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [1, 3, 5]
    image_order: 24
    kernel_order: 12
    coset_representatives:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0, 0, 0]
    quotient_multiplication:
    - [0]
  overlattice_count: 12
  bad_reduction_primes: [2, 3]
  genus_symbol: 'II_{5,0} (2: 1^2 [2^3]_5; 3: 1^3 3^-2)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 2
  kissing_number: 8
  automorphism_group_order: 288
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [0, -2, -1, 0, 0]
  - [0, -1, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 1, 1, 0, 0]
  - [0, 2, 1, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 8, 0, 18, 0, 54, 0, 92]
  root_system: [A2, A1]
  roots:
  - type: G2
    scale: 2
    simple_roots:
    - [0, 0, 0, 1, 0]
    - [0, 0, 0, 0, 1]
  - type: G2
    scale: 1
    simple_roots:
    - [0, 1, 0, 0, 0]
    - [0, 0, 1, 0, 0]
  - type: A1
    scale: 1
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [2, 4]
morphisms:
- target: 5XPP
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 2, -3, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5XPP
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -3, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5XPP
  name: O(L) generator 3
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5XPP
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 2, -3]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5XPP
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -3]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID4, 3ID6.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID4, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID4, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ID4, 3ID6.
