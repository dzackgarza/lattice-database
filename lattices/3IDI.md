---
tag: 3IDI
name: Constructed lattice 3IDI
latex: L_{\mathrm{3IDI}}
certifications:
  derive: 42f1afc7c6e7d85d6b695b12639748d28d3914b3737011d8b2748e74980d703b
  form.integer_valued: a1dcc88a7174156e76cc7d5babdfd8262de5ad19b48237ea52ee69c419c68b75
  integral.elementary_primes: 0a2b79f53f27d5f68a2103bca5cb6a0e1b98b0b678d683b905b5c480fd71c7d5
  integral.genus_symbol: 18839cff949061c4b44e4e4c8004ef834af08056513f68aba92c419c386c56a7
  integral.genus_class_count: e1d1e930876730351bce32c4d97fd73866d961111f6260e915729599925b0295
  integral.overlattice_count: 940089a820dd1ca51f0010a51ae887ea5b824785bfcb95e199792cfabd32fdec
  integral.spinor_genus_count: dc43dabd1f67dcaeb1bb19b9a432f03d628517bbe7b257e4e288bec4b53b5f20
  integral.spinor_genera: 8aee44c213e8300b7af8ec5420db0766fa9b78359a8b125f5df928cad5003eff
  integral.hyperbolic_index: b61f9a123c6f0117ec21439700ffc86d9e42c67c782687abfbbd00ace359db04
  automorphisms.automorphism_group_generator_morphisms: 9bfcb586923bb391cf45cc1c22c69d1d067b6112e5ad8c17ebda7f8e6b4c89eb
  integral.primitive_orbits: abf99b0f291d9518e81752e1af985614e2b7629604fcedde26a9f1cfeb510b85
  integral.modular_scale: 6b2ac7fb97ab7918292cdb1dbb0577a7f8f602896471cf76e7515897e3dd7b94
  integral.anisotropic_primes: 61be76f374a777a6d347c7d337d5ed0d300bc6e105860bef2dcd957c9d5a3262
  integral.local_representations: f2bb7901631bc96ae67d31d32b843edcf34b885489f4c6242443b0e32f6c9ada
  integral.local_densities: 77a8f69c096d162fd1aafee5e9c7d0e5ce97266a89ec25cab2183f970613ad08
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, 0, 2]
- [0, 2, 0]
signature: [2, 1]
determinant: -4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, 0, 1/2]
- [0, 1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 2
  modular_scale: false
  discriminant_group: [2, 2]
  overlattice_count: 4
  bad_reduction_primes: [2]
  genus_symbol: 'I_{2,1} (2: [1^1]_1 2^2)'
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
      constant: 3
      z: []
      w: []
    SOtilde:
      constant: 3
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
      constant: 3
      z: []
      w: []
    SOtilde+:
      constant: 3
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
      least_valuation: 2
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
    densities: [3, 0, 0, 3, 1, 0, 0, 3/2, 3, 0, 0, 3/2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IDI
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 0, -1]
  - [0, -1, 0]
  scale: 1
- target: 3IDI
  name: O(L) generator 2
  matrix:
  - [-1, 2, 0]
  - [0, 1, 0]
  - [1, -1, 1]
  scale: 1
- target: 3IDI
  name: O(L) generator 3
  matrix:
  - [1, 0, 2]
  - [0, 0, -1]
  - [1, -1, 1]
  scale: 1
- target: 3IDI
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0013.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0001, 0013.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0013.
