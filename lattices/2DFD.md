---
tag: 2DFD
name: nipp tbl.480.html:2032
latex: nipp tbl.480.html:2032
aliases: []
certifications:
  derive: 0a5ec240385c7c16003a1f647d50b7fdd9bfcee01f4a1dbb9f7c7950d73b1dee
  form.integer_valued: 3cf780163b6a0e1202ae11697540170edf0d5553c8c17daa89f289eaaa7f7d43
  integral.elementary_primes: 2cf158db2391ab5d9493f03e22de0c09af768589e551bf3e56b7b0d4f848ce16
  integral.genus_symbol: 44178dc745cf1a4f901b1a31b4e4ba34eaba247499dd751745e3751f6df07522
  integral.genus_class_count: 8e9858b8b6def76850785e285fa79558525c70f5e7b3af15ea572230f5b43fde
  integral.overlattice_count: d617a0b6b2c1db9fd280f0371fbb9f8e9179825d950b33f2761bf4a955009548
  integral.spinor_genus_count: 94ee54afda1b3a48d91d95d08c79832c8488f98a277decb76f0fa541aaa903c1
  integral.spinor_genera: 74c9e9b3b5723d10f65deb181b3c3db24c20128516a2865b8394390d333679ae
  integral.hyperbolic_index: 1e6f97fb31af1df3246796ff021759e9f985401f7e9814f0dfe1ba9c9d69b0d4
  definite.automorphism_group_order: db650403eb3e00379d79764f8907cde43600c82a32dd5f8d876e52227dcbbd64
  definite.automorphism_group_generator_morphisms: e688debce8772bd8b6269f73359a9766c919663c449b6a6893ddc3a9746d96db
  integral.discriminant_sequence: eae1da0d106c734533ba13533c350789c5e6551ec154bfecb846d4d946d79979
rank: 5
gram_tensor:
- [2, 0, 1, 1, 0]
- [0, 4, 0, 2, 2]
- [1, 0, 6, 2, 3]
- [1, 2, 2, 6, 3]
- [0, 2, 3, 3, 8]
signature: [5, 0]
determinant: 904
definiteness: positive_definite
dual_gram_tensor:
- [137/226, 2/113, -23/226, -25/226, 17/226]
- [2/113, 38/113, 15/226, -23/226, -8/113]
- [-23/226, 15/226, 55/226, -9/226, -21/226]
- [-25/226, -23/226, -9/226, 59/226, -13/226]
- [17/226, -8/113, -21/226, -13/226, 45/226]
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
    - ['0', 1/2, -1/2, 1/2, '0']
    - ['0', '0', -1/2, 1/2, '0']
    - [-85/226, -33/226, -4/113, -24/113, 1/226]
    discriminant_quadratic_gram:
    - ['0', 1/2, '0']
    - [1/2, '0', 1/2]
    - ['0', 1/2, 221/226]
    discriminant_group_order: 4
    discriminant_generators:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 225]
    - - [0, 1, 0]
      - [1, 0, 0]
      - [1, 1, 225]
    image_generators:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 225]
    - - [0, 1, 0]
      - [1, 0, 0]
      - [1, 1, 1]
    - - [0, 1, 0]
      - [1, 0, 0]
      - [1, 1, 225]
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
  theta_series: [1, 0, 2, 0, 2, 0, 16, 0, 22]
  root_system: [A1]
  roots:
  - type: A1
    scale: 2
    simple_roots:
    - [0, 1, 0, 0, 0]
  - type: A1
    scale: 1
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1]
morphisms:
- target: 2DFD
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 2DFD
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, -1, -1]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 2DFD
  name: O(L) generator 3
  matrix:
  - [1, 0, 1, 1, 0]
  - [0, 1, 0, 1, 1]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: G. Nipp, Tables of Quaternary and Quinary Quadratic Forms, tbl.480.html:2032.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/tbl.480.html
---

Source entry `nipp:tbl.480.html:2032` gives this Gram tensor.
