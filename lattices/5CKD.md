---
tag: 5CKD
name: Constructed lattice 5CKD
latex: L_{\mathrm{5CKD}}
certifications:
  derive: 149ab86ab75c3d51de1b9ef7fd5a7e6a9d85dbdcbeb30d61c01dc414253d9727
  form.integer_valued: 0232c63941927f4d1116e5c151f352edf0b41d3902c6af266d21a5c1db272e99
  integral.elementary_primes: fd51b03e3bec68146845e2b09003cb94558b10cf08f3c2af58dae794ac4745d8
  integral.genus_symbol: 14fbb8cfc55b6c61905d088ba29891085f2a3142332728f30ae8e76a3906e159
  integral.genus_class_count: 43697b2c0071298fe88e2ec5ac9aef842c35e30d44659975352193c7a19d3482
  integral.overlattice_count: 12ed45e82f565347f652883c3904766798fcdcea911c368e831c804f21883a54
  integral.spinor_genus_count: 9c3e9fa87a62fc7b18c4f4c355a7d82cc2029b11f91b8cdc491f9135f378648c
  integral.spinor_genera: c73103ef97bf5f1aab5768bb4e8880149818a029b28ba470c897893e19651953
  integral.hyperbolic_index: d0249029e6efdd4e04b0fa82e1e2a91176a97cc798703e8d1b8e49d71e19a71f
  definite.automorphism_group_order: fafe2ddaad0301b924217866b51138aa2e68ef367dc0fcab91ff99579090f650
  definite.automorphism_group_generator_morphisms: b849f83088101b6300f435647172762d4849b7aa3cd0a9ad44b2dd06047600dc
  integral.primitive_orbits: 6ff5096c882f5a2e240b17b9ffa42e615de221c1fb4d4ac5be259aadee36c214
  integral.modular_scale: d71fc6bc7ea89817a3c5aaeada90dbe8645956ab7ce742146485df2c47779c81
  definite.genus_theta_series: 95176ca45c2bb6bf7c70dc8cc81ba4adee042156925123c4dd2b7ebcde5feae2
  definite.theta_series_cuspidal_component: cb767b826da1d6fea326e9bce69715ccae023d1000265202cd08c70a78475de5
rank: 4
gram_tensor:
- [-1, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, -2, 1]
- [0, 0, 1, -2]
signature: [0, 4]
determinant: 6
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, -2/3, -1/3]
- [0, 0, -1/3, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  modular_scale: false
  discriminant_group: [6]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  quadratic_character: 24
  genus_symbol: 'I_{0,4} (2: [1^-3 2^1]_6; 3: 1^-3 3^1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 2, 2, 1]
    SO:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 2, 2, 1]
    Otilde:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 2, 2, 1]
    SOtilde:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 2, 2, 1]
    O+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 2, 2, 1]
    SO+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 2, 2, 1]
    Otilde+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 2, 2, 1]
    SOtilde+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 2, 2, 1]
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 48
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 8, 16, 14, 24, 22, 12, 44, 42, 36, 64, 40]
  genus_theta_series: [1, 10/3, 28/3, 40/3, 34/3, 24, 70/3, 12, 124/3, 130/3, 36, 200/3, 136/3]
  theta_series_cuspidal_component: [0, -4/3, -4/3, 8/3, 8/3, 0, -4/3, 0, 8/3, -4/3, 0, -8/3, -16/3]
  root_system: [A2, A1]
  roots:
  - type: G2
    scale: -1
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
  norms: [-1, -2]
morphisms:
- target: 5CKD
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5CKD
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, -1]
  - [0, 0, 1, 0]
  scale: 1
- target: 5CKD
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, -1]
  - [0, 0, 0, -1]
  scale: 1
- target: 5CKD
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ID0.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ID0.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ID0.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICX, 3ID0.
