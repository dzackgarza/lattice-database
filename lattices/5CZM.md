---
tag: 5CZM
name: Constructed lattice 5CZM
latex: L_{\mathrm{5CZM}}
certifications:
  derive: 8d38a03d6ff569e4b84013ecfb8f1fa021d7fce155f670c21e30e68dc9259789
  form.integer_valued: 19e2c709dde1c8a9f03cc1ebb0f10e7db52070d460e09aa79e2ac6168b397ded
  integral.elementary_primes: baa0179d1138f514ddb39ba8fdc400c45a323b7eeccdcbdd90792663d8e60901
  integral.genus_symbol: 442911e786188347356fc416daafa2414caead3000ae2594453e2f04f97ffc77
  integral.genus_class_count: 81ba9014f62b1818c0e2fc66dc780e4a6ebd38a58fca859909881de365de6218
  integral.overlattice_count: bca885e19dcbbbfc893ef3299a43d0999aa34ced1c07e9bdce1d44a7e3998b73
  integral.spinor_genus_count: 504185ff3833382d3e05ff6df7a1e1dd05511764c166e03ebf393192e39fc1c2
  integral.spinor_genera: 384022519b6450365cedbeabb2ccb888722527704b2ab87067031459c0aeedcc
  integral.hyperbolic_index: be309385e72fcf38151c4bc9900fbf95181ebf46279f5faa7df93c713e66a328
  definite.automorphism_group_order: e7f77ad262de5a82c2f8a217ac39b96b131974126a7cd28f6daccaa9d0f2d450
  definite.automorphism_group_generator_morphisms: 9c76d4698586e12b8536e58763bad15e291b8d3b37208d129e63d61ea208bc4e
  integral.primitive_orbits: 5969d4f0e5f320cb85835b7a0d89f787467c74038887e0eb01c27700e82b1090
  integral.modular_scale: 50166b31a69433e2399670650204adaaec3a5e80b05e1c6cff68147f1880d11d
  definite.genus_theta_series: 13e64fe7e4430fa517a87637d51b5857c9b1073569d648705b31dbfc6898ae14
  definite.theta_series_cuspidal_component: c84fa1d2c56b9922c841202f09c0598aa90da6dd2f811bc655ce593ed4b65bf8
rank: 4
gram_tensor:
- [-1, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, -4, 2]
- [0, 0, 2, -4]
signature: [0, 4]
determinant: 24
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, -1/3, -1/6]
- [0, 0, -1/6, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  modular_scale: false
  discriminant_group: [2, 2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  quadratic_character: 24
  genus_symbol: 'I_{0,4} (2: [1^-1 2^3]_2; 3: 1^3 3^-1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 1]
    SO:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 1]
    Otilde:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 6]
    SOtilde:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 2, 6]
    O+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 1]
    SO+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 1]
    Otilde+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 6]
    SOtilde+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 2, 6]
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 48
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 2, 4, 8, 12, 16, 24, 14, 6, 24, 4, 22]
  genus_theta_series: [1, 4/3, 10/3, 10/3, 28/3, 12, 40/3, 24, 34/3, 28/3, 24, 20/3, 70/3]
  theta_series_cuspidal_component: [0, 2/3, -4/3, 2/3, -4/3, 0, 8/3, 0, 8/3, -10/3, 0, -8/3, -4/3]
  root_system: [A1]
  roots:
  - type: G2
    scale: -2
    simple_roots:
    - [0, 0, 0, 1]
    - [0, 0, 1, -1]
  - type: A1
    scale: -1
    simple_roots:
    - [0, 1, 0, 0]
  - type: A1
    scale: -1/2
    simple_roots:
    - [1, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1]
  norms: [-1, -2, -4]
morphisms:
- target: 5CZM
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5CZM
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5CZM
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, -1]
  - [0, 0, 1, 0]
  scale: 1
- target: 5CZM
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, -1]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ID1.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ID1.
- tag: 3ID1
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ID1.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICX, 3ID1.
