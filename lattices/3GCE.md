---
tag: 3GCE
name: watson 3:489
latex: watson 3:489
aliases: []
certifications:
  derive: b392c2d2cbe009cf6e9069d8ddbaa7b20f38e3dec21c81f8debbab86692a1de5
  form.integer_valued: e1b9c82a08dc169ea8762a25ed2e108d9f0c22012bb83f43ae0bf458fdda0efb
  integral.elementary_primes: 2e46c22b7db086c13d4e3b9ce799fcca207721c5e8fda8295891645c8e1448c7
  integral.genus_symbol: 18b411d5b7d3be02bc64f1dbe57ab99308b38163fa5f5433df3f3ef062ccaa1c
  integral.genus_class_count: d4592ee616bc573a11bf5110fecc37f0139058f15653b4f4f87fd9d48f328f33
  integral.overlattice_count: 87d2412fbb7f94e4cf8cb2aeef677f2079be14d0330d2880b5ff3dc08d9f47a6
  integral.spinor_genus_count: fec0b90bc3a5b0f7ea2365cfd4e4bc2aa8f7161ea27226ef314f33084a66c5f2
  integral.spinor_genera: 4b737daad25304f7afe4f182bbfab0d6f7795cca9e7bea9f61d810a52663b544
  integral.hyperbolic_index: c11175cfb9cc772d92173f88df3b7148997d791bc5b81f223d30f28ee3c66a53
  definite.automorphism_group_order: 71711de84acd4ec2baf56e315d441bd13cbe8c2343bf1cf92c40acf9e5ac9bac
  definite.automorphism_group_generator_morphisms: 1f79a621682a6d25a0ce7c6fcfd9d2641cde1c848311454d508ae8ef990b04ac
  integral.primitive_orbits: e3a980e475e93c268301eeb12ae26695d73c30e2e2d65e1291fecd619b38babe
  integral.modular_scale: 271949d0eb17df4e3a26b8652fe0e5781b68383826f5360db11c04de174508b2
  definite.genus_theta_series: e95f7bc35a53ed62493e71a08d0750e50e46768fca748f44fa82708b6078ed5d
  definite.theta_series_cuspidal_component: ab06bfb6b6ada55e02b01a3108e417f1c34d9223e1dd461dadade9a87b6da3f3
  definite.siegel_eisenstein_coefficients: 5fb482eb5b77dec6037376a364fe1446ebd56bc7f2faa006ed0e483ddd2878e1
  integral.anisotropic_primes: c6fea6a975a8330125f8421b3e959954edc36705b7d41fcd8c50ade7beaf3476
  integral.local_representations: 8cbd795366185845c233032a48d274974dae3e6161163760f539558b3d8d2e5f
  integral.local_densities: 82ad1a6339776e5f699a771f1ab7e885e7d90cfefb74fad536575a9e2ce5eb3c
rank: 3
gram_tensor:
- [3, -1, -1]
- [-1, 3, -1]
- [-1, -1, 7]
signature: [3, 0]
determinant: 48
definiteness: positive_definite
dual_gram_tensor:
- [5/12, 1/6, 1/12]
- [1/6, 5/12, 1/12]
- [1/12, 1/12, 1/6]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 24
  modular_scale: false
  discriminant_group: [4, 12]
  overlattice_count: 5
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{3,0} (2: [1^-1]_3 [4^2]_6; 3: 1^-2 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 1, 1]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 0, 1, 1]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 0, 4, 2]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 0, 4, 2]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 0, 1, 1]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 0, 1, 1]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 0, 4, 2]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 0, 4, 2]
      w: [0, 0, 0, 0]
  anisotropic_primes: [2]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 3
      least_valuation: 0
    - representative: 7
      least_valuation: 0
    - representative: 2
      least_valuation: 3
    - representative: 6
      least_valuation: 3
    - representative: 10
      least_valuation: 3
    - representative: 14
      least_valuation: 3
  local_densities:
  - prime: 2
    densities: [0, 0, 2, 2, 0, 0, 2, 3, 0, 0, 2, 3]
  - prime: 3
    densities: [2/3, 2/3, 4/3, 2/3, 2/3, 2, 2/3, 2/3, 14/9, 2/3, 2/3, 4/3]
definite:
  minimum: 3
  kissing_number: 4
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 1, 0]
  - [1, 0, 0]
  perfect: false
  theta_series: [1, 0, 0, 4, 2, 0, 0, 4, 6, 0, 0, 4, 12]
  genus_theta_series: [1, 0, 0, 4, 2, 0, 0, 4, 6, 0, 0, 4, 12]
  theta_series_cuspidal_component: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  siegel_eisenstein_coefficients: [0, 0, 4, 2, 0, 0, 4, 6, 0, 0, 4, 12]
  root_system: []
  roots:
  - type: A1
    scale: 4
    simple_roots:
    - [1, -1, 0]
  - type: A1
    scale: 2
    simple_roots:
    - [1, 1, 0]
  - type: A1
    scale: 12
    simple_roots:
    - [1, 1, 2]
root_sublattice:
  invariant_factors: [1, 2, 2]
morphisms:
- target: 3GCE
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GCE
  name: O(L) generator 2
  matrix:
  - [0, 1, 0]
  - [1, 0, 0]
  - [0, 0, 1]
  scale: 1
- target: 3GCE
  name: O(L) generator 3
  matrix:
  - [1, 0, -1]
  - [0, 1, -1]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:489.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:3:489` gives this Gram tensor.
