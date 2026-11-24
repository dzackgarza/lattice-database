---
tag: 6DPL
name: Constructed lattice 6DPL
latex: L_{\mathrm{6DPL}}
certifications:
  derive: cf813c8c3e7fd4d9c828331de6a3841c8bc4f3ca8e12d6d8b91b26d27cbb93f0
  form.integer_valued: b30b95d37d7900eb9662c18d70b84987bcf3708d97dcecef191c9e38080d1405
  integral.elementary_primes: eb9f1bb9d2b379da477da3115e4ea9b885ee6ad419ab1999961ce5ee6d31c816
  integral.genus_symbol: 5c9187c45d688a583ceee13ab1ea1ab636c6fb3f052975fb1cd974b4dee8a96e
  integral.genus_class_count: 35b77fd0989ce33457f4c3ba90ab9a85fa561d37614d02af0d496ea35e428066
  integral.overlattice_count: e06fbc666c488d775abc4840564265f3cdfdd7a2112a8e50b456f9298074ed6e
  integral.spinor_genus_count: e7997b2454cfebbf2cbcc45dfa7ebd51767eac8467c7b744cbd8be4fc04e7d6f
  integral.spinor_genera: e0457dd8385cbd9f99f1c1937760526a1caf3a814adbdba4a6f615466000059d
  integral.hyperbolic_index: fea3eff096aa0173a9feb2613a3c2b363b85e6e649ec0a734641b3f1a245ee2c
  automorphisms.automorphism_group_generator_morphisms: 3280b1d30378c5462d67c5f0b98ff24c9690e0bb64635a23b30572c8b71ac672
  integral.discriminant_form: b7d5a5c406936abc48bd65bb6ce2679546dac9ac4e4ecea2f2f7edd566a0763c
  automorphisms.automorphism_group_order: 5f60a52fa901857eaf58df3671eaac06656d71f366ba8345c8eee0144bf58f44
  integral.discriminant_orbits: 6e015a9291539d941ded116f5f5fd05212eacb5abe2e8643f2cdf9dfc037e327
  integral.modular_scale: 536fbc3f85e943c89d9ee9dc8c43b41f8889f1559c5c124c52a2d6f52bc354f5
  integral.anisotropic_primes: 769ad9ccd92aee81766ff746bd18f5fcdb1aa2ae070eace916d03fb756f4e668
  integral.local_representations: 7d482b81b6cbe02ea106a571660e35f7cd6ade70a621e2f2058c52bfa7061eed
  integral.local_densities: f0e29ffba43b9f7c6e89b5457d0886ebd5124a288b7b9e3b9e0502e52f6f3383
rank: 4
gram_tensor:
- [0, -2, 0, 0]
- [-2, 0, 0, 0]
- [0, 0, 0, -2]
- [0, 0, -2, 0]
signature: [2, 2]
determinant: 16
definiteness: indefinite
dual_gram_tensor:
- [0, -1/2, 0, 0]
- [-1/2, 0, 0, 0]
- [0, 0, 0, -1/2]
- [0, 0, -1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 2
  modular_scale: 4
  discriminant_group: [2, 2, 2, 2]
  overlattice_count: 31
  delta: 0
  bad_reduction_primes: [2]
  quadratic_character: 1
  genus_symbol: 'II_{2,2} (2: 2^4)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  discriminant_form:
    orthogonal_group_order: 72
    isotropic_classes: 10
    isotropic_orbits: 2
  discriminant_orbits:
    Otilde:
      constant: 10
      z: [0, 1, 0, 7]
      w: [0, 1, 0, 7]
    SOtilde:
      constant: 10
      z: [0, 1, 0, 7]
      w: [0, 1, 0, 7]
    Otilde+:
      constant: 10
      z: [0, 1, 0, 7]
      w: [0, 1, 0, 7]
    SOtilde+:
      constant: 10
      z: [0, 1, 0, 7]
      w: [0, 1, 0, 7]
    O:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    SO:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    O+:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    SO+:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 3
      least_valuation: 2
    - representative: 5
      least_valuation: 2
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
    densities: [0, 0, 0, 3, 0, 0, 0, 9/2, 0, 0, 0, 3]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 4, 'O(L) generator 2 #2', 'O(L) generator 3 #2', O(L) generator 3, O(L) generator 5, 'O(L) generator 6 #2', O(L) generator 6, 'O(L) generator 8 #2', 'O(L) generator 9 #2', 'O(L) generator 10 #2', O(L) generator 8, 'O(L) generator 12 #2', O(L) generator 11, O(L) generator 14]
indefinite:
  isotropic: true
morphisms:
- target: 6DPL
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6DPL
  name: O(L) generator 2
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 1]
  - [1, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6DPL
  name: O(L) generator 3
  matrix:
  - [1, 0, 1, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, -1, 0, 1]
  scale: 1
- target: 6DPL
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6DPL
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 1, 0]
  - [0, 0, 1, 0]
  - [-1, 0, 0, 1]
  scale: 1
- target: 6DPL
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 2]
  - [0, 1, 0, 0]
  - [0, -2, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6DPL
  name: O(L) generator 7
  matrix:
  - [1, -1, 1, 1]
  - [0, 1, 0, 0]
  - [0, 1, 0, -1]
  - [0, 1, -1, 0]
  scale: 1
- target: 6DPL
  name: O(L) generator 8
  matrix:
  - [0, -1, 0, 0]
  - [-1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6DPL
  name: O(L) generator 9
  matrix:
  - [0, -1, 1, 0]
  - [-2, 0, 0, -1]
  - [-1, 0, 0, -1]
  - [0, 1, -2, 0]
  scale: 1
- target: 6DPL
  name: O(L) generator 10
  matrix:
  - [0, 0, 0, -1]
  - [-1, 0, -1, 0]
  - [0, -1, 0, 1]
  - [-1, 0, 0, 0]
  scale: 1
- target: 6DPL
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6DPL
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, -1]
  - [0, 0, 0, 1]
  - [1, 0, 1, 0]
  scale: 1
- target: 6DPL
  name: 'O(L) generator 2 #2'
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6DPL
  name: 'O(L) generator 3 #2'
  matrix:
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  scale: 1
- target: 6DPL
  name: 'O(L) generator 6 #2'
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 1]
  - [-1, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6DPL
  name: 'O(L) generator 8 #2'
  matrix:
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  scale: 1
- target: 6DPL
  name: 'O(L) generator 9 #2'
  matrix:
  - [0, -1, 0, -1]
  - [-1, 0, 0, -1]
  - [-1, -1, 1, -1]
  - [0, 0, 0, 1]
  scale: 1
- target: 6DPL
  name: 'O(L) generator 10 #2'
  matrix:
  - [0, -1, 1, 0]
  - [-1, 0, 1, 0]
  - [0, 0, 1, 0]
  - [1, 1, -1, 1]
  scale: 1
- target: 6DPL
  name: 'O(L) generator 12 #2'
  matrix:
  - [0, -1, 0, 0]
  - [-1, 0, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6DPL
  name: O(L) generator 14
  matrix:
  - [-1, -1, 1, -1]
  - [0, 0, -1, 0]
  - [-1, 0, 1, 0]
  - [0, -1, 1, 0]
  scale: 1
related:
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 3ICZ, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICZ, 3ICZ.
