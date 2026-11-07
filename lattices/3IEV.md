---
tag: 3IEV
name: Constructed lattice 3IEV
latex: L_{\mathrm{3IEV}}
certifications:
  derive: dc260f6d4abccc9b3e202d085ec7897b9cd548c9dfe18a82f1c6db6fa6db02b8
  form.integer_valued: 95073901abae511210330dae2716d95b79e66a210ff0bfcc1f7e6bd38dfae5d6
  integral.elementary_primes: 7122f3a335ca2a73d928c168ee207d3e4646f8daefebc5f38027547a2d45f265
  integral.genus_symbol: 9840cdd04b90fc0d89ab25fc3b7ed8c91579ad6d0565ab2a24d8ff89bbfc0e9f
  integral.genus_class_count: b90bfaf7d8d84050a3d96bf76d34cbe0ac2c3888af509b64fe68a0bb6213cc0a
  integral.overlattice_count: 84968fd8d40dfb933e3271609201f2466e838529b974bac05b362fd0ebb9134f
  integral.spinor_genus_count: f66d3656f9fe3e6e6fd57583c42d19dde372e543df62bb7cd6fcb4c6959ce4fc
  integral.spinor_genera: d53e989de2002c5cc30d84833bf5992550f5828224aa5e1778678fa4af3ed5d9
  integral.hyperbolic_index: 1cf1f5475757f93be8e07b885f1f26d6cb1dc71285c4bf99dd8c8858c3dc9050
  automorphisms.automorphism_group_generator_morphisms: 40eb3c7d095e40b0c732fead9ffdab183b80670e22ea9eef73954a779d5f4a7b
  integral.discriminant_form: cfc0956ffc3c69a8f84d32d93560946fac8c230976a4c091c0652e0627206f12
  integral.primitive_orbits: b2ecd652ccb613929f178db3de5a4e6d9fa214716d74c581052d5d2385aa08ae
  integral.modular_scale: 7b7cf8d7997bc860b95372f04025ad518ab9759c0e50823e69a4ec0492fd05f0
  integral.anisotropic_primes: df7a9c1aa8ea91bc827f58567f6b9e4acf4fc529a4593358617b1aa6378dd898
  integral.local_representations: 24b26e90535dc4e4ecef99eebb8253e2dac39f740c0488790ea4c632f56c3192
  integral.local_densities: 75d4440c530ed5a77742bb8d6f38252930a8b6c7d36fe56bccb716b43f8cd0d0
rank: 3
gram_tensor:
- [-2, 0, 0]
- [0, 0, 2]
- [0, 2, 0]
signature: [1, 2]
determinant: 8
definiteness: indefinite
dual_gram_tensor:
- [-1/2, 0, 0]
- [0, 0, 1/2]
- [0, 1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  modular_scale: 4
  discriminant_group: [2, 2, 2]
  overlattice_count: 4
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{1,2} (2: [2^3]_7)'
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
      constant: 2
      z: []
      w: []
    SOtilde:
      constant: 2
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
      constant: 2
      z: []
      w: []
    SOtilde+:
      constant: 2
      z: []
      w: []
  discriminant_form:
    orthogonal_group_order: 2
    isotropic_classes: 3
    isotropic_orbits: 2
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
      least_valuation: 1
    - representative: 6
      least_valuation: 1
    - representative: 10
      least_valuation: 1
    - representative: 14
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [0, 1, 0, 1, 0, 2, 0, 5/2, 0, 1, 0, 1]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IEV
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IEV
  name: O(L) generator 2
  matrix:
  - [-1, -2, 0]
  - [0, 1, 0]
  - [2, 2, 1]
  scale: 1
- target: 3IEV
  name: O(L) generator 3
  matrix:
  - [1, 0, 2]
  - [2, 1, 2]
  - [0, 0, 1]
  scale: 1
- target: 3IEV
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICX, 0013.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 3ICX, 0013.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICX, 0013.
