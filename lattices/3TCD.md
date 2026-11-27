---
tag: 3TCD
name: Constructed lattice 3TCD
latex: L_{\mathrm{3TCD}}
certifications:
  derive: 3cf786741e45fb2b2506efda10572412dd7c95bc8ce1bfc36a7be01da24bff24
  form.integer_valued: cf8c3b7330aade396468ac8f729fb2acfce5b335e730297a592f9a3d98ed77d6
  integral.elementary_primes: fd9e5a97a22f7e32d5c9a03d00d7b68bd17e5e978c6b0dd76d4653ee1105a20d
  integral.genus_symbol: 2f5ce3afe85962a1b95e58c724758e827880eee971ab8eba95173e0ac3cb7cf4
  integral.genus_class_count: 61ab0ea995bf29d63d8b32124c2591785b114027620092ee3fbd0ad323bba824
  integral.overlattice_count: 0137c2709e47ecea4c4a0a88c606e9f815b7c711fa4ad925597e2ccce314f751
  integral.spinor_genus_count: bf9aa48095d3a5e2c4d022857b4b2ad20e56876421894573dd08f3d988e818d9
  integral.spinor_genera: 28a9340c587b5522a47fb9dcc1d0e22f0e9d36ac2c4604b06e310b2708e57920
  integral.hyperbolic_index: edef4a90f7f624254247c53821614f6e370466a04f2681021354b5b2d9c411d5
  automorphisms.automorphism_group_order: 0bfbc19b45f1bff6bc25a277af6ca2b4c4335c1d68117671be85bad6305060fb
  automorphisms.automorphism_group_generator_morphisms: dabcb6ad27490bd7fd0e79e7dde5ebad7ed7b2f4cc07d5a2d564f50d5213d5a3
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 4, -2]
- [0, 0, 0, -2, 4]
signature: [4, 1]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 1/3, 1/6]
- [0, 0, 0, 1/6, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  discriminant_group: [2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{4,1} (2: [1^-3]_5 2^2; 3: 1^-4 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7]
indefinite:
  isotropic: true
morphisms:
- target: 3TCD
  name: O(L) generator 1
  matrix:
  - [-1, 0, -2, -2, -2]
  - [0, 1, 0, 0, 0]
  - [2, 0, 3, 2, 2]
  - [-1, 0, -1, 0, -1]
  - [-1, 0, -1, -1, 0]
  scale: 1
- target: 3TCD
  name: O(L) generator 2
  matrix:
  - [-1, -2, -2, 0, 0]
  - [-2, -1, -2, 0, 0]
  - [2, 2, 3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TCD
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 3TCD
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 3TCD
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 7, 12, 0]
  - [0, 0, -4, -7, 0]
  - [0, 0, -2, -4, 1]
  scale: 1
- target: 3TCD
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TCD
  name: O(L) generator 7
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ID2.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ID2.
- tag: 3ID2
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ID2.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ID2.
