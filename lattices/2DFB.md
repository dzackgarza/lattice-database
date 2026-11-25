---
tag: 2DFB
name: nipp tbl.480.html:2030
latex: nipp tbl.480.html:2030
aliases: []
certifications:
  derive: 07a301f2e58bb9db949592671bc102bd3bd96795a5fcf5a5a6622ee49dffc716
  form.integer_valued: d1c4264177300aabfef1ce3fde313c12ea5b9f8d214bb355a548fe6d9ce66998
  integral.elementary_primes: 39c0a237769fc375ac5f31dfd28f523f070bf0cc65f277aed5298be37a312504
  integral.genus_symbol: b239378b3fd7088b3b956db26f213e5dba81673fcf8f29df2501dac0f98f2a57
  integral.genus_class_count: 5849690cd71a02b6cda0e9b6b40c4b5332217002b772dbe6ba5cb81dc7690f0c
  integral.overlattice_count: 5838f91bc23846e00f2faf5acbc5c2ec1787d0d62cccbb55fabc7f6ee44702be
  integral.spinor_genus_count: 18994756dffbc3e63a4ba91e033ce4c14ee402eee217f890cd3c9b032e28458c
  integral.spinor_genera: 51ff20ad277c14070c40ef9991498cab5fdadc92d8724926498e01e34e1497c6
  integral.hyperbolic_index: 873a7ecf637fe73929cee4c4ad8e6a47d11817b7a501d4313bd5d64159b16b18
  definite.automorphism_group_order: 57bfad45ad1df2a7c4a99844f6ac50a54ae00b07587ea120515fbf29d7234289
  definite.automorphism_group_generator_morphisms: 9db056c97b2618a1a37a5752640ae1104be03bcd5b310b548f6ea6e11571746e
  integral.discriminant_sequence: e17a524d85ff711d29a5ad0447cfc99487bdcfc9e02356bab09c0bf85a1b6f07
rank: 5
gram_tensor:
- [2, 0, 0, 1, 1]
- [0, 4, 0, 0, 2]
- [0, 0, 6, 0, 2]
- [1, 0, 0, 6, 2]
- [1, 2, 2, 2, 6]
signature: [5, 0]
determinant: 904
definiteness: positive_definite
dual_gram_tensor:
- [66/113, 6/113, 4/113, -7/113, -12/113]
- [6/113, 73/226, 11/226, 9/226, -33/226]
- [4/113, 11/226, 45/226, 3/113, -11/113]
- [-7/113, 9/226, 3/113, 23/113, -9/113]
- [-12/113, -33/226, -11/113, -9/113, 33/113]
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
    - ['31', '28', '0', 1/2, -1/2]
    - [-31/113, -57/226, -19/113, -103/226, 1/226]
    discriminant_quadratic_gram:
    - [3/2, 1/2, 1/2]
    - [1/2, '0', 1/2]
    - [1/2, 1/2, 6/113]
    discriminant_group_order: 4
    discriminant_generators:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 225]
    - - [1, 0, 0]
      - [0, 0, 113]
      - [0, 1, 114]
    image_generators:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 225]
    - - [1, 0, 0]
      - [0, 0, 113]
      - [0, 1, 114]
    - - [1, 0, 0]
      - [0, 0, 113]
      - [0, 1, 112]
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
  theta_series: [1, 0, 2, 0, 2, 0, 18, 0, 18]
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
- target: 2DFB
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 2DFB
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, -1]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 2DFB
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 1, 1]
  - [0, 1, 0, 0, 1]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: G. Nipp, Tables of Quaternary and Quinary Quadratic Forms, tbl.480.html:2030.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/tbl.480.html
---

Source entry `nipp:tbl.480.html:2030` gives this Gram tensor.
