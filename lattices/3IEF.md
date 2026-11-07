---
tag: 3IEF
name: Constructed lattice 3IEF
latex: L_{\mathrm{3IEF}}
certifications:
  derive: e110c0664f338f455edde9705d6bdf9d3259803c9789aceca3681e3de59ed746
  form.integer_valued: 90d3cb41eb145431f32b1705293398684785038c84655f796f2812e3cbd1ead2
  integral.elementary_primes: 025af87c2dd138c6b0b35e5c6ca38cff2dd4232cc3954727f79f3a84c1f9bb33
  integral.genus_symbol: dc9e157cdf4feeeb409dfc6b8f7f225bc1ec3604f3f804b46b98d1a7b5fd6dcb
  integral.genus_class_count: da433522853272a32e0fafb88268edc3e2bed45af1ebc53bb4622be03415e03d
  integral.overlattice_count: 55258be869f24d8d1a683d2a14d7b3cbb94eebe78ba66cacbdb6c1e5ffc03d2b
  integral.spinor_genus_count: a88ef8383d12e3019102f75145487a48c43df93174850f8e5026426cc05309fb
  integral.spinor_genera: f99e6a33565b89ea03449432ebfd32260c17fdd3181f3767fd965d6d8475b79d
  integral.hyperbolic_index: 347b48486b6c35269ea49cc95467cad857e6b35f43364123c9d7b43648b37c27
  automorphisms.automorphism_group_generator_morphisms: 0208c785cd8273aa6979fb99e915f60166431cf33649ad1e198d543b9f999055
  integral.discriminant_form: 7f4eec8fa6e069fd1ffdb4847c3490b54edf46557d3a3a54b47b0a9877d7f9e7
  integral.primitive_orbits: 7ace5ebf4d366a41d94339556a3cb93cd62133e4e7f48bdd3778db5ba312ac96
  integral.modular_scale: 4569ff6f7b6239542f0124672c33e1f7a6898f9da0ffd44d3644054b45104dc0
  integral.anisotropic_primes: bc5c403638441b6d7fbf1161d1c9d5453f7ae80423201c1025db9d8f322dab07
  integral.local_representations: 347cd351cdbdf45bf6c0ce5fa93b2961699617337d323b90b707b9cef80c640d
  integral.local_densities: 911b9d5176d6cfd07181d0f731569f4826fd716b0731fabb20c4c7802546aebb
rank: 3
gram_tensor:
- [2, 0, 0]
- [0, 0, 1]
- [0, 1, 0]
signature: [2, 1]
determinant: -2
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0]
- [0, 0, 1]
- [0, 1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  modular_scale: false
  discriminant_group: [2]
  overlattice_count: 1
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{2,1} (2: 1^2 [2^1]_1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
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
  discriminant_form:
    orthogonal_group_order: 1
    isotropic_classes: 1
    isotropic_orbits: 1
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
    densities: [0, 3, 0, 3/2, 0, 3/2, 0, 3, 0, 2, 0, 3/2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IEF
  name: O(L) generator 1
  matrix:
  - [-1, 0, -1]
  - [-2, 1, -1]
  - [0, 0, 1]
  scale: 1
- target: 3IEF
  name: O(L) generator 2
  matrix:
  - [-1, 1, 0]
  - [0, 1, 0]
  - [2, -1, 1]
  scale: 1
- target: 3IEF
  name: O(L) generator 3
  matrix:
  - [1, 0, 1]
  - [-2, 1, -1]
  - [0, 0, 1]
  scale: 1
- target: 3IEF
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0016.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0002, 0016.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0016.
