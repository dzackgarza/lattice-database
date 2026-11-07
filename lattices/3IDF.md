---
tag: 3IDF
name: Constructed lattice 3IDF
latex: L_{\mathrm{3IDF}}
certifications:
  derive: 259b7fa105d23f1bf68ddc62ab684a8b47ffb11ed13a2e597b539c5f80478e28
  form.integer_valued: 03c6c376c919ecc4d0783cb26867b98fc0030d977859f93e0ae89958bfee094e
  integral.elementary_primes: a45b60e3e29fd54bfff8a36ca0a224b6c0852a36ceec38972f1dddb1bbf9e03a
  integral.genus_symbol: 36bc87bebd1eb32e363d3fa54380bd4eeba2e34316db689ae5ced456e5142c72
  integral.genus_class_count: 0937cf2b2b1cec776e998384a1474a0be0032d290b62a0de6b67a64c4dc3e294
  integral.overlattice_count: e3e29dfbbc7ce25d4754b4614c6557a887c5ab1bbb17dd739ebe5319e7eb165d
  integral.spinor_genus_count: 0f31092dfef96e9b8e03b3da4771766409c2845d87017e5db636b5b67a571dd4
  integral.spinor_genera: a667d4125ca19f2788f179869cd08e4f2c4e0c0362aa0783963e538c4750d839
  integral.hyperbolic_index: aa4102fceb1ebdf01b45aa677b17cf6a8ea7a5b0694a484305d72266a24df588
  automorphisms.automorphism_group_generator_morphisms: c0044b05b79d911206a5a2dfc03a9cfa5cdcdcc2907cd4b8a315fd8cb694aac3
  integral.primitive_orbits: b23a22248c0a6c58d5865c73e028b8eb1211212183abc83a5f9135da1e6bc39a
  integral.modular_scale: c6a03d521d60f766601f6242c90bfe7270cd7d0fbd1e5e83b804409ef74e5e76
  integral.anisotropic_primes: eb954ca60d9f1d48c589134c95978fc332db5d27c2928ab9e40ff73c9bb37553
  integral.local_representations: bab299f6cfd190b33f6acf4a9931befe68b5340759e300793312dace8009e045
  integral.local_densities: 7c92f0908480bb158fe92a6b7f42d7df1f997d35477ba76172f767b190ba4284
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, -2, 0]
- [0, 0, -2]
signature: [1, 2]
determinant: 4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, -1/2, 0]
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
- target: 3IDF
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3IDF
  name: O(L) generator 2
  matrix:
  - [3, 4, 0]
  - [-2, -3, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IDF
  name: O(L) generator 3
  matrix:
  - [3, 4, 0]
  - [0, 0, 1]
  - [2, 3, 0]
  scale: 1
- target: 3IDF
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICX, 3ICX.
