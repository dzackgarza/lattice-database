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
  automorphisms.automorphism_group_generator_morphisms: f2b503dd10a2040dffd043295143a5d74808a87f084f15b1feaf8ab5f2b4859e
  integral.discriminant_form: b7d5a5c406936abc48bd65bb6ce2679546dac9ac4e4ecea2f2f7edd566a0763c
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
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12]
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
related:
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 3ICZ, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICZ, 3ICZ.
