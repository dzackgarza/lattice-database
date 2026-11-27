---
tag: 4DWK
name: Constructed lattice 4DWK
latex: L_{\mathrm{4DWK}}
certifications:
  derive: 77924baf180dcb22ba40ea3a577e2e935c545f2019d5ec841f40cce99d123f10
  form.integer_valued: 207c617e4cc62257b79525fa620964cc612e47bd952c0f6d1db447acbf32f5ca
  integral.elementary_primes: 1ffa07bd2adb8c84e2194a8aa30dcd94f484021933fab65ceaec76fce29138b7
  integral.genus_symbol: 6e010ecfcd9bde137d663416f3fcadf353aefe15b693e51c8151bed9c96fa06f
  integral.genus_class_count: 062ccc9c2f097127f6d911a1f59c4250d0ca8735ef346874328c448861a5a0e8
  integral.overlattice_count: 0b2b9a635b7bc2640d9fc40a485851748d52f06b2f560dc5011677c0f3ad2fbd
  integral.spinor_genus_count: 74f6c65cbd3f3ac99176c1f133adfb65415566920105a7430d23899847888e67
  integral.spinor_genera: cc2a17ffd89c6396fdd39dfe4276bff7d6ab2d36e7998bc040808407d7b1a709
  integral.hyperbolic_index: 8cb2c9aa3c609d89f9e6a729e01b749184086b8a255e821502538f46c98bb543
  definite.automorphism_group_order: 5a610e5c7e63ff77fcacae4c86b8ddfc02fe9b1431991be0ce7a6ec3035b0a5a
  definite.automorphism_group_generator_morphisms: 1cf1ac2178b2d677bcaf74478796a24d261fc561df0f59fd7e6d711b5f053163
  integral.discriminant_sequence: 8a733859d05b4ae642ef24388fb0efb27016d4fc000f3426c7ff48d2d733b6f2
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 0, 0, 2, -1]
- [0, 0, 0, -1, 2]
signature: [5, 0]
determinant: 12
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 0, 0, 2/3, 1/3]
- [0, 0, 0, 1/3, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  discriminant_group: [2, 6]
  discriminant_sequence:
    discriminant_factors: [2, 6]
    discriminant_basis_lifts:
    - ['0', '-1', 3/2, '1', '-1']
    - ['0', -1/2, 1/2, 1/3, -1/3]
    discriminant_quadratic_gram:
    - [1/2, 1/2]
    - [1/2, 2/3]
    discriminant_group_order: 4
    discriminant_generators:
    - - [1, 3]
      - [0, 1]
    - - [1, 3]
      - [0, 5]
    image_generators:
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 5]
    - - [1, 0]
      - [0, 5]
    - - [1, 0]
      - [0, 1]
    - - [1, 3]
      - [0, 1]
    image_order: 4
    kernel_order: 48
    coset_representatives:
    - - [1, 0]
      - [0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0, 0]
    quotient_multiplication:
    - [0]
  overlattice_count: 2
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{5,0} (2: [1^-3 2^2]_3; 3: 1^-4 3^-1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 192
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 10, 20, 30, 56, 50, 60, 90]
  root_system: [A2, A1, A1]
  roots:
  - type: B2
    scale: 1
    simple_roots:
    - [0, 0, 1, 0, 0]
    - [0, 1, -1, 0, 0]
  - type: G2
    scale: 1
    simple_roots:
    - [0, 0, 0, 0, 1]
    - [0, 0, 0, 1, -1]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [1, 2]
morphisms:
- target: 4DWK
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DWK
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 4DWK
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4DWK
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DWK
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 0012.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 0012.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 0012.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0002, 0002, 0012.
