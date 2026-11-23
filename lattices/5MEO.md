---
tag: 5MEO
name: Constructed lattice 5MEO
latex: L_{\mathrm{5MEO}}
certifications:
  derive: 9cbdf998a7a6b2900532167af60a45cd8f7a2476abd5e9efec27d93bf3e854a0
  form.integer_valued: 97c1179c8ae10ca5ab349bda6e23d467debd67266ec445bfb6fe819be7ca3495
  integral.elementary_primes: ac7c16ef0a94a1db4d5c12b7fbe4fef45a33e7a4f2c56b42d474d02d9cf4623a
  integral.genus_symbol: 7736273a5bbaf66948c329dce6bd1e9593fcedc87bfdd9431799f8a68d197e14
  integral.genus_class_count: d45811cea6117892c06697a249b6d9da99cc4024fde5295b6f2fa7d7ee8318ff
  integral.overlattice_count: e20816b8eb2522326d6ea05192705fd2542c34df6b7b54881763c6b9572ad450
  integral.spinor_genus_count: ac212c107f7ff8ec48c90989b6053327d0c9222177bfe2b377c3df1b50f2fd69
  integral.spinor_genera: b5919edbd314142fc3eb1d69ceef3ad4fb6f1888157c3cb48e1fbadb163422ce
  integral.hyperbolic_index: 25aa4c311a70e851d3decd7de6e02a4542426d8e895f8d0dccece5e4271d87fd
  automorphisms.automorphism_group_order: f32f1b141eb7f7f44ad697aeb48aa7c7d1bd13e1ce0ea4f2f1b8b2cbf3464000
  automorphisms.automorphism_group_generator_morphisms: 841125bcdd6d8df93d1da695cb2146e9bbe2f28469704c4eb05468bba4b95a7f
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, 4, -2]
- [0, 0, 0, -2, 4]
signature: [4, 1]
determinant: -96
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
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
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8]
indefinite:
  isotropic: true
morphisms:
- target: 5MEO
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MEO
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MEO
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5MEO
  name: O(L) generator 4
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MEO
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 1, 1]
  - [0, -1, 2, 1, 1]
  - [0, 1, -1, 0, -1]
  - [0, 1, -1, -1, 0]
  scale: 1
- target: 5MEO
  name: O(L) generator 6
  matrix:
  - [0, 2, 3, 3, 0]
  - [-1, 0, 0, 0, 0]
  - [0, 3, 4, 3, 0]
  - [0, -2, -2, -1, 0]
  - [0, -1, -1, -1, 1]
  scale: 1
- target: 5MEO
  name: O(L) generator 7
  matrix:
  - [-2, 2, 7, 6, 3]
  - [-2, 1, 6, 4, 4]
  - [-3, 2, 10, 8, 5]
  - [1, 0, -3, -3, -1]
  - [1, 0, -1, -1, 0]
  scale: 1
- target: 5MEO
  name: O(L) generator 8
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX, 3ID2.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX, 3ID2.
- tag: 3ID2
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX, 3ID2.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0002, 3ICX, 3ID2.
