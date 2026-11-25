---
tag: 3VIB
name: Constructed lattice 3VIB
latex: L_{\mathrm{3VIB}}
certifications:
  derive: 1e96637a9e8a75789514a84b52f96815e4b1fef04b8674b32dbc74950e3b6975
  form.integer_valued: 2f7f23d2c27f8de3e783bca325d73cc5cdac6a6a7ee9eea1ae45963aad4d3721
  integral.elementary_primes: 7f9f1af07ee9b9e26755ab4afbca53979b905c601475e2b822e7ae0214e0b7cc
  integral.genus_symbol: 0c300002cc7c90851fad0fec9d73166ecc3f0f09561ae1de55d761410ecd37fe
  integral.genus_class_count: 0b99265c03346991a7457c5dd7f855324b4e2f6c26dd1a0e7b02405a6526dd0d
  integral.overlattice_count: 2c874bcfe2d4a830d41f08f82474ec1f8713f68d789467e534a6fe98573303d5
  integral.spinor_genus_count: 9da380ca92dc94681eae9c91693f023bf4d90ac205eddacf812cb8b17877cd31
  integral.spinor_genera: 79e4f44ea0df743630d5e1184b142df427d5f6e2b27e07ac78ae9b1ffa83f537
  integral.hyperbolic_index: 09efc5c5482f87bcfbdb8959b56f8dbbdd99cddcd2d97d52261477d1073b2e0c
  automorphisms.automorphism_group_order: d6aa82727b257248ef922fac9efd90372a48f098e65d092808852c034d09ceee
  automorphisms.automorphism_group_generator_morphisms: 1f6b83d4e43652ce68756e6c5e882e2d033d0ae66bd3023a8e82f64500b65dc5
  integral.primitive_orbits: 13aa7febbacaaca1e4badaddbfdf34439323c4f027367d1f626c25801be8695a
  integral.modular_scale: 36712500f23e5ff8dceb1821ff964a022eb1e471a908a8a5953bdc0a8a8d7453
  integral.anisotropic_primes: c4e795b775e4c87e9eef5f042cc7920de2136908f720f6d0bde294ed0de2d187
  integral.local_representations: 6441de5baedbf89bc6c0168e84577ad2e421023ae82a112117a989f5b9328cf5
  integral.local_densities: b4090c8c0140c8c2b06f46f417898384fabf76fdb85ae53942c54f8da2cefefb
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 0, 0, 0, -1]
- [0, 0, 0, -1, 0]
signature: [4, 1]
determinant: -2
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 0, 0, 0, -1]
- [0, 0, 0, -1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: false
  discriminant_group: [2]
  overlattice_count: 1
  bad_reduction_primes: [2]
  genus_symbol: 'I_{4,1} (2: [1^4 2^1]_3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
  primitive_orbits:
    O:
      constant: 1
      z: []
      w: []
    O+:
      constant: 1
      z: []
      w: []
    SO:
      constant: 1
      z: []
      w: []
    SO+:
      constant: 1
      z: []
      w: []
    Otilde:
      constant: 1
      z: []
      w: []
    Otilde+:
      constant: 1
      z: []
      w: []
    SOtilde:
      constant: 1
      z: []
      w: []
    SOtilde+:
      constant: 1
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1, 9/8, 1, 9/8, 1, 15/16, 1, 57/64]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7]
indefinite:
  isotropic: true
morphisms:
- target: 3VIB
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3VIB
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 3VIB
  name: O(L) generator 3
  matrix:
  - [0, -1, -2, -1, -1]
  - [-1, 0, -2, -1, -1]
  - [-1, -1, -1, -1, -1]
  - [1, 1, 2, 2, 1]
  - [1, 1, 2, 1, 2]
  scale: 1
- target: 3VIB
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, -1]
  - [0, 0, 2, 1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3VIB
  name: O(L) generator 5
  matrix:
  - [0, -1, 0, 0, 0]
  - [-1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3VIB
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, 0, -2]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [2, 0, 0, 1, 2]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3VIB
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0002, 3ICY.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0002, 3ICY.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0002, 3ICY.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 0002, 3ICY.
