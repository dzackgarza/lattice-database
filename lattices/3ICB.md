---
tag: 3ICB
name: Earnest–Haensch spinor regular ternary form 13
latex: Earnest–Haensch spinor regular ternary form 13
aliases: []
certifications:
  definite.spinor_regular: fe8a17c892b5fd80b5741fcccb93be82ce7d45fba21778a688c282527d361588
  derive: f72134f8a2f59f86b94df390c45b113cfe12f5d092cb32f50e7f99aedf7763e1
  form.integer_valued: 516fae67ee9c52cc800aed6fbae64d18000dd9d384f7ee3f38b44ae07bfce6a1
  integral.elementary_primes: b2f790f7d000a868d8201a9dd98d9e74dbce3de63983bf46cef993998e03594d
  integral.genus_symbol: ce36b44fe0d3fc6a148f46151c03f4b19870cc9f91089d1f01e2153d8d792b7d
  integral.genus_class_count: 4e055d02b93d39b0883fe9a16da723aa431dc3aef080f66ad242db614a4eb287
  integral.overlattice_count: 7a929935eed3d650da82ace7aad4777b8ec90d0e4eca87c75ab619ebb6f04294
  integral.spinor_genus_count: ef6544aba971a11c6c6ae98f04cecfe017f36be31c9dbf18a53d049f5efe13e1
  integral.spinor_genera: 5b4b40b136da7d13089f5ba5ba4150d1f7d63a51479c8907bc9d9f5f8aee997f
  integral.hyperbolic_index: b8c79bdd6723e8ae652de83ad27d797b30e613f81d0f00c3800bb87ee4fefd95
  definite.automorphism_group_order: 6d175867b302362cd545a416e356f0ace2b910180c3cc1cd17bc0f888b402fb3
  definite.automorphism_group_generator_morphisms: d2634f1a43dd2acf6659f9dffbc263307ffaff48f3255abb8afcf57e9cc2f915
  integral.primitive_orbits: 38100e899f26a3076e0ad14cc45f77ac7099c34c36685e41c8acb4889614aa4d
  integral.modular_scale: c1e48d331bb9bdedae93ae58fafd13eacbea959af1e5b5a28d9d7bfe52d79fae
  definite.genus_theta_series: 76fa083c46981da4589b188d6653b2d83f9093207a9f7953c90af55bc715c2c8
  definite.theta_series_cuspidal_component: 401b306aca74e3dba5d334dafd440cffe38f7bd8d2af1b1c1fe5f813b3fc832a
  definite.siegel_eisenstein_coefficients: 9c5c38bb2c2d0a9f2d25ca1d189e183fb1fc0241deb987bccb33eb303cdb42f8
  integral.anisotropic_primes: bdf5f2a90e7a431d78b097eaf49d08d01f863dfde81ee133ede410b8d685aaf9
  integral.local_representations: 10b5ce3e3ac647dc0f08765e6f8b2b76763414850047172d84f4511060e5b61d
  integral.local_densities: cb33209b3325b658452cf45741a6e91a69c122d520cba5a451b00de70da96953
  definite.regular: e877232fc32c24ec3c323fa0e70eee548d9b810eec5e933dfc4ca2852b2afddf
rank: 3
gram_tensor:
- [4, 0, 0]
- [0, 5, 1]
- [0, 1, 13]
signature: [3, 0]
determinant: 256
definiteness: positive_definite
dual_gram_tensor:
- [1/4, 0, 0]
- [0, 13/64, -1/64]
- [0, -1/64, 5/64]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 128
  modular_scale: false
  discriminant_group: [4, 64]
  overlattice_count: 11
  bad_reduction_primes: [2]
  genus_symbol: 'I_{3,0} (2: [1^-1]_5 [4^1]_1:[64^-1]_5)'
  genus_class_count: 3
  spinor_genus_count: 2
  spinor_genera: [1, 2]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 0, 1]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 0, 0, 2]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 0, 0, 2]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 0, 0, 2]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 0, 0, 2]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 0, 0, 2]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 0, 0, 2]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 0, 0, 2]
      w: [0, 0, 0, 0]
  anisotropic_primes: [2]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 6
    - representative: 5
      least_valuation: 0
    - representative: 2
      least_valuation: 5
    - representative: 6
      least_valuation: 3
    - representative: 10
      least_valuation: 5
    - representative: 14
      least_valuation: 3
  local_densities:
  - prime: 2
    densities: [2, 0, 0, 4, 2, 0, 0, 0, 2, 0, 0, 0]
definite:
  minimum: 4
  kissing_number: 2
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: false
  spinor_regular: true
  theta_series: [1, 0, 0, 0, 2, 2, 0, 0, 0, 4, 0, 0, 0]
  genus_theta_series: [1, 1/2, 0, 0, 2, 2, 0, 0, 0, 5/2, 0, 0, 0]
  theta_series_cuspidal_component: [0, -1/2, 0, 0, 0, 0, 0, 0, 0, 3/2, 0, 0, 0]
  siegel_eisenstein_coefficients: [1/2, 0, 0, 2, 2, 0, 0, 0, 5/2, 0, 0, 0]
  root_system: []
  roots:
  - type: A1
    scale: 2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3ICB
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3ICB
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Table 1, row 13; its spinor genus has one class.
  url: https://arxiv.org/abs/1711.05811v2
---

Row 13 of `sources/earnest_haensch/spinor_regular_ternaries.txt` gives the coefficients $(a, b, c, d, e, f) = (4, 5, 13, 2, 0, 0)$ of $Q = ax^2 + by^2 + cz^2 + dyz + ezx + fxy$; the Gram tensor is that of $b(x, x) = Q(x)$.
