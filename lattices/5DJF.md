---
tag: 5DJF
name: Constructed lattice 5DJF
latex: L_{\mathrm{5DJF}}
certifications:
  derive: c7dc8db0f0be58047a59be9082dd026059ad6b118413f226fbe02c68b1d91e47
  form.integer_valued: ffd030a20f55ea72ac8edb980f2c952455d71802310218e3e1c048f60a2945e2
  integral.elementary_primes: 41070f1aac88081fe58187bc5a4a9bc4cc0e3232c6a077fa33df53ede36e30b2
  integral.genus_symbol: 9f55d7910f1ba0f99defa3e2d119f08b36b45ecba5bae52567bb5df679b6583f
  integral.genus_class_count: e704c31a8c89479d3fec074970620e51d9a10630e27508e2798d968ccc6e417f
  integral.overlattice_count: 9fe2fde40f4142668cce0c5b0aa3f15781273f56ff0ad57cf9313ac8f2665d63
  integral.spinor_genus_count: 196a2363219c54ac9e47129fb574efaa23fe7a5a254ed5069a6827e024059fb6
  integral.spinor_genera: 0df3bfcfa55db21f7968b6f0a950ad940c7c497391816bf8dccef56c78475dbf
  integral.hyperbolic_index: 730923b0d4e2206a6270a918c39656381cf130d9a829efff9c9b9eda07e1da12
  definite.automorphism_group_order: d1ca9c78b4b303d33ab3efa5768d4a3bc6ae880e4dead8c0868122978cf3b378
  definite.automorphism_group_generator_morphisms: 0c27f0ce15a3c07813742df4248faf739f6deae24c0942f512cd49205e0bf750
  integral.discriminant_sequence: 9344b5f8860a68b3ad7d9418d5e9c8ec5ebda60c81c275f7dbf35821723e0bc1
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -2, 0, 0, 0]
- [0, 0, -2, 1, 0]
- [0, 0, 1, -2, 1]
- [0, 0, 0, 1, -2]
signature: [0, 5]
determinant: -8
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1/2, 0, 0, 0]
- [0, 0, -3/4, -1/2, -1/4]
- [0, 0, -1/2, -1, -1/2]
- [0, 0, -1/4, -1/2, -3/4]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 8
  discriminant_group: [2, 4]
  discriminant_sequence:
    discriminant_factors: [2, 4]
    discriminant_basis_lifts:
    - ['0', 1/2, -1/2, '0', 1/2]
    - ['0', '0', 1/4, 1/2, -1/4]
    discriminant_quadratic_gram:
    - [1/2, 1/2]
    - [1/2, 1/4]
    discriminant_group_order: 2
    discriminant_generators:
    - - [1, 0]
      - [0, 3]
    image_generators:
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 3]
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 1]
    image_order: 2
    kernel_order: 96
    coset_representatives:
    - - [1, 0]
      - [0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0]
    quotient_multiplication:
    - [0]
  overlattice_count: 2
  bad_reduction_primes: [2]
  genus_symbol: 'I_{0,5} (2: [1^3 2^1 4^1]_3)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 192
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 14, 28, 32, 60, 64, 72, 122]
  root_system: [A3, A1]
  roots:
  - type: C3
    scale: -1
    simple_roots:
    - [0, 0, 0, 1, 0]
    - [0, 0, 0, 0, 1]
    - [0, 0, 1, 0, -1]
  - type: A1
    scale: -1
    simple_roots:
    - [0, 1, 0, 0, 0]
  - type: A1
    scale: -1/2
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [-1, -2]
morphisms:
- target: 5DJF
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5DJF
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 1, -1, 1]
  - [0, 0, 1, -1, 0]
  scale: 1
- target: 5DJF
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, -1, 1]
  - [0, 0, 0, -1, 0]
  - [0, 0, 1, -1, 0]
  scale: 1
- target: 5DJF
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, -1, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, -1, 1]
  scale: 1
- target: 5DJF
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5DJF
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ID7.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ID7.
- tag: 3ID7
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ID7.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICX, 3ID7.
