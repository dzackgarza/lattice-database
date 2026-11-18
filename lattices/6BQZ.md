---
tag: 6BQZ
name: Constructed lattice 6BQZ
latex: L_{\mathrm{6BQZ}}
certifications:
  derive: cf9b7179f3dece4187cc7cef7ab0a04e321697e378835cacd39dd68b982f8fd7
  form.integer_valued: e5938280993ab4c6b164e7bdde41f896d0edf1b70d643096fbacd11ee7aaea5d
  integral.elementary_primes: 90ac1aa69a117bf5507fd48220dbdc3309bb38a48a9c31a7bad5f08a228eaff7
  integral.genus_symbol: ec4bd8bbb7fcc50e9f9675ea414940166a8ee2b9ed3d0aac818dfca13685b23f
  integral.genus_class_count: d78d3c0f8290b09390c276e0bd127b3a3a0fd818be5d02f1c0665864df68d214
  integral.overlattice_count: c9411ccf5069fcf38fea0a7a5d334d69bc7443d3ee56dfe0e2e5301eaa60e56c
  integral.spinor_genus_count: 7153a7a77d51c7805f75dbe713369abeaf46673ba6873ee3827081d98805152d
  integral.spinor_genera: f28168d682207a452099454b3cef4c719103cb8f53b9490f411765376f7e58f6
  integral.hyperbolic_index: ad946236ed119cbb548d047195b942c776bf14921d768ecea50db10cb6c762d0
  automorphisms.automorphism_group_generator_morphisms: d42aa48fd71b000d7a6db7d9046861bfcbba548355f67274d6d4e2a9d56e2870
  integral.discriminant_form: d3c8ec16893a7a3085649b4d7b1482fd03634a5e5ab8907e7fa55990bb630205
rank: 4
gram_tensor:
- [0, -1, 0, 0]
- [-1, 0, 0, 0]
- [0, 0, -4, 6]
- [0, 0, 6, -12]
signature: [1, 3]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [0, -1, 0, 0]
- [-1, 0, 0, 0]
- [0, 0, -1, -1/2]
- [0, 0, -1/2, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 6
  discriminant_group: [2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{1,3} (2: 1^2:2^-2; 3: 1^3 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
  discriminant_form:
    orthogonal_group_order: 12
    isotropic_classes: 1
    isotropic_orbits: 1
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 6BQZ
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, -1, 1]
  scale: 1
- target: 6BQZ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [-2, 1, 2, -6]
  - [-1, 0, 2, -3]
  - [-1, 0, 1, -2]
  scale: 1
- target: 6BQZ
  name: O(L) generator 3
  matrix:
  - [0, -1, 0, 0]
  - [-1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6BQZ
  name: O(L) generator 4
  matrix:
  - [1, -2, -4, 6]
  - [-2, 7, 10, -18]
  - [1, -1, -3, 6]
  - [0, 1, 1, -1]
  scale: 1
- target: 6BQZ
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ID5.
- tag: 3ID5
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ID5.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICY, 3ID5.
