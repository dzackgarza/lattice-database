---
tag: 5VFA
name: Constructed lattice 5VFA
latex: L_{\mathrm{5VFA}}
certifications:
  derive: 0a9be0f4cbafe4ded901a1aa01c5098b28386d7ae06c7bd00731d740a9d4294d
  form.integer_valued: 703fe51a0d3606c62d928f504b9d005b85c3f4bd41d35de00683d9b47706a025
  integral.elementary_primes: 978be87a2bed3d010af81ac822f8c1e4c7a2e411e56387146f036f729bd152a1
  integral.genus_symbol: 313791b43e7510487d29fbebab7f380ec33dcc0dd43d95f335e6acc62250e77d
  integral.genus_class_count: 3588dfa53db597b20d29ca146c495249e0ce7564bf8bbf5a939f245af4a2b940
  integral.overlattice_count: a12a3ed87f7bdcddb518d916a0ee6504decf1ff9c9e5f84989f672fff7e7a240
  integral.spinor_genus_count: 06ae3ca246c8cb9b84e16a820397ced70c665104081d5aa4ebded10befdf0b43
  integral.spinor_genera: 202fadce1d8880af4624418835eb2a87c3b74b84ce7e8babbd759041926c8ec5
  integral.hyperbolic_index: 8e6cead1bd4536a49142f23ae12d9bef6615d37a2524534bb1aa242de3c8d04c
  automorphisms.automorphism_group_order: e6f9a20d1bed68e104dd22f7b9fdf0db79dde53430100736fd488db28917c29c
  automorphisms.automorphism_group_generator_morphisms: 60fe508a7865c5a6abdf948198597dc0bd65eb559013239ae0dcf7ad71c9ac7c
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 0, 4, -2]
- [0, 0, 0, -2, 4]
signature: [4, 1]
determinant: -96
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 0, 1/3, 1/6]
- [0, 0, 0, 1/6, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  discriminant_group: [2, 2, 2, 2, 6]
  overlattice_count: 31
  bad_reduction_primes: [2, 3]
  genus_symbol: 'II_{4,1} (2: [2^-5]_1; 3: 1^4 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7]
indefinite:
  isotropic: true
morphisms:
- target: 5VFA
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5VFA
  name: O(L) generator 2
  matrix:
  - [-1, 2, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [2, -2, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5VFA
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5VFA
  name: O(L) generator 4
  matrix:
  - [-3, 2, -4, -2, -2]
  - [-4, 3, -4, -2, -2]
  - [2, -1, 3, 1, 1]
  - [-2, 1, -2, 0, -1]
  - [-2, 1, -2, -1, 0]
  scale: 1
- target: 5VFA
  name: O(L) generator 5
  matrix:
  - [1, -2, 2, 4, -2]
  - [-2, 3, -2, -4, 2]
  - [2, -2, 3, 4, -2]
  - [-2, 2, -2, -3, 2]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5VFA
  name: O(L) generator 6
  matrix:
  - [-1, 2, -2, -4, 2]
  - [-2, 3, -2, -4, 2]
  - [2, -5, 3, 7, -2]
  - [-2, 4, -2, -5, 2]
  - [0, 1, 0, -1, 1]
  scale: 1
- target: 5VFA
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0013, 3ID2.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0002, 0013, 3ID2.
- tag: 3ID2
  relation: This presentation is obtained by orthogonal sum of 0002, 0013, 3ID2.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0013, 3ID2.
