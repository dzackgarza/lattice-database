---
tag: 1UPA
name: nipp tbl.270.html:214
latex: nipp tbl.270.html:214
aliases: []
certifications:
  derive: eed2d976da0f871a87933af3881e7287bc8103dbce997dc0e190e2dcdb0b9b0c
  form.integer_valued: 8dcb734b84a5c7a4e6318552ac1718f645488375f1f653ae3d540bd7f3c3609f
  integral.elementary_primes: b2cac5d8e63bbb6d5d1798549fd0bcf38705b834a0fc4f95c403d23ce2707402
  integral.genus_symbol: 0da9740407115edfdb934a5e21a58f8e58202545740914e58b66f8a764b822ec
  integral.genus_class_count: 3cabd58484f0e106a3e4099366caf26f0e8374598a08bccdf5159fdbcbbebd1c
  integral.overlattice_count: da2032e19cbd734bedcc1c83e9b481251101d4cc923f4042c863a33f4837fbff
  integral.spinor_genus_count: 9fd6f357dbb3e2e8f2c8204c2b275f378a895e76e76a309cb985e3a7f92030d9
  integral.spinor_genera: 9bf20df7e0d8706e5e620a14d6bde75092b4cd362cbdee7c0b33b13dd9b2f0f4
  integral.hyperbolic_index: 7a8a2bc791fab1150d3cf54e4a64d0df820db5363405bf122ec17c1f82a1329f
  definite.automorphism_group_order: cec7bfd0c5efa5bf625847af190198b20cb003585a8b96be90ecbef91387d3ef
  definite.automorphism_group_generator_morphisms: ecb75329d87c76973b6340b82e285c82acb366702c442d03b7d8741ad0502ab4
  integral.discriminant_sequence: 9ea446a8db88f2f8bcb9359e1d251debb7a313b9cca7a4731858069c80db7a1a
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 4, 1, -1, 1]
- [0, 1, 4, 1, 0]
- [0, -1, 1, 4, 1]
- [0, 1, 0, 1, 6]
signature: [5, 0]
determinant: 520
definiteness: positive_definite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 43/130, -3/26, 17/130, -1/13]
- [0, -3/26, 4/13, -3/26, 1/26]
- [0, 17/130, -3/26, 43/130, -1/13]
- [0, -1/13, 1/26, -1/13, 5/26]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 260
  discriminant_group: [2, 2, 130]
  discriminant_sequence:
    discriminant_factors: [2, 2, 130]
    discriminant_basis_lifts:
    - [-1/2, '0', 1/2, '0', -1/2]
    - ['0', 11/2, 9/2, 1/2, '-1']
    - ['0', -14/65, -5/26, -1/65, 1/26]
    discriminant_quadratic_gram:
    - ['1', '0', 1/2]
    - ['0', 3/2, '0']
    - [1/2, '0', 53/130]
    discriminant_group_order: 8
    discriminant_generators:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [1, 0, 1]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [1, 0, 51]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [1, 0, 129]
    image_generators:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 129]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 79]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 129]
    image_order: 4
    kernel_order: 2
    coset_representatives:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [1, 0, 1]
    mm_trivial: false
    image_normal: true
    quotient_generator_cosets: [1, 1, 1]
    quotient_multiplication:
    - [0, 1]
    - [1, 0]
  overlattice_count: 4
  bad_reduction_primes: [2, 5, 13]
  genus_symbol: 'II_{5,0} (2: 1^2 [2^3]_1; 5: 1^-4 5^-1; 13: 1^4 13^1)'
  genus_class_count: 20
  spinor_genus_count: 1
  spinor_genera: [20]
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
  theta_series: [1, 0, 2, 0, 6, 0, 22, 0, 30]
  root_system: [A1]
  roots:
  - type: A1
    scale: 5
    simple_roots:
    - [0, 1, 0, -1, 0]
  - type: A1
    scale: 1
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1]
morphisms:
- target: 1UPA
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 1UPA
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 1UPA
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: G. Nipp, Tables of Quaternary and Quinary Quadratic Forms, tbl.270.html:214.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/tbl.270.html
---

Source entry `nipp:tbl.270.html:214` gives this Gram tensor.
