---
tag: 3IDY
name: Constructed lattice 3IDY
latex: L_{\mathrm{3IDY}}
certifications:
  derive: 8f95996fd866bd79e871f68a6b77067f7e1b01f5dab3f3258131f06fdfa30c00
  form.integer_valued: 391cbce2f97fea839905d3a84730aacc08c6a516ba5ca2a38b0e3741eee25c47
  integral.elementary_primes: 9268112bf9080d9b9a08375e9cdb3c9e508c2d61aed87ed07119b09c098a7258
  integral.genus_symbol: dfe6b62296bc1f4ed38ceb635358027b1e9518a75533269f56962577f114ff80
  integral.genus_class_count: 1ff468c719c9b07fc2f08735cdea8d904bfeb1e4cf0d283e0560f793f5fd7abf
  integral.overlattice_count: 7cc8855901254fc3f9d43924786ef51af37793d4f6c8b2d8d4619d36dff7dd1b
  integral.spinor_genus_count: 203ee141115ecdecbf921a55bedac435c564abd0d0e6053e2138137aff6c1c92
  integral.spinor_genera: 7a8a2cd969cadccab9e0da8a3b6f9d6e0428b93479e8cdf6acb0e3a4f0fadbe0
  integral.hyperbolic_index: 01d73ce308087fba50f0d83e5862e8c783c71e52a22d8dfa29c0f4352d36b28c
  automorphisms.automorphism_group_generator_morphisms: aa366503879218a74275043fef4d974936b5cf27f8671dad91879f9cd8e83afd
  integral.primitive_orbits: cdc55ad6dad050d5156e2deaea51e43e35b8698ec445d5b1815c26e3f49797b2
  integral.modular_scale: f5a7ed5d46aeb82e2166d6341649ee59a5df3e33b84e710525e0f49deac7d8f2
  integral.anisotropic_primes: 09a9c17080fcab153e0caca93b69846ed3fb2addafb5500361c5f1bb12e94c26
  integral.local_representations: 6919f5e78ab2e6de600d1973420a5cee1f2b38c9317b22b1fa752d7f4de29195
  integral.local_densities: 0352fb67bc2b62c831b2102816a4abf995bcc892bb7942041beabca0ea8de27a
rank: 3
gram_tensor:
- [-1, 0, 0]
- [0, 2, 0]
- [0, 0, -2]
signature: [1, 2]
determinant: 4
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0]
- [0, 1/2, 0]
- [0, 0, -1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: false
  discriminant_group: [2, 2]
  overlattice_count: 2
  bad_reduction_primes: [2]
  genus_symbol: 'I_{1,2} (2: [1^1 2^2]_7)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 1
      z: []
      w: []
    SO:
      constant: 1
      z: []
      w: []
    Otilde:
      constant: 1
      z: []
      w: []
    SOtilde:
      constant: 1
      z: []
      w: []
    O+:
      constant: 1
      z: []
      w: []
    SO+:
      constant: 1
      z: []
      w: []
    Otilde+:
      constant: 1
      z: []
      w: []
    SOtilde+:
      constant: 1
      z: []
      w: []
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 2
    - representative: 5
      least_valuation: 0
    - representative: 7
      least_valuation: 0
    - representative: 2
      least_valuation: 1
    - representative: 6
      least_valuation: 1
    - representative: 10
      least_valuation: 1
    - representative: 14
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [1, 1, 0, 1/2, 1, 1, 2, 1/2, 1, 1, 0, 1]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IDY
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3IDY
  name: O(L) generator 2
  matrix:
  - [-17, -24, 0]
  - [12, 17, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IDY
  name: O(L) generator 3
  matrix:
  - [-1, -2, 2]
  - [1, 2, -1]
  - [-1, -1, 0]
  scale: 1
- target: 3IDY
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0002, 3ICX.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0002, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0002, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 0002, 3ICX.
