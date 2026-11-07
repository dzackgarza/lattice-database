---
tag: 3IEP
name: Constructed lattice 3IEP
latex: L_{\mathrm{3IEP}}
certifications:
  derive: 7766849ef3d594c1da2fccffc1330d8c4a57671ad53b10578243a4f2bfc035e5
  form.integer_valued: 66bd517384df3153560da55c7664dabdb9ba8f072191c63a1dc3f9d2bcfd8dbd
  integral.elementary_primes: 98c9771613707b46f2ae4d800db168eb87b0b10f7beacef6a8c7527fadf861d2
  integral.genus_symbol: 86d02f43dcfb57aebefb99a0c57d84496530261bf7fd408cee44f4eefc55de51
  integral.genus_class_count: e6f5fabf7ce724b55aaf2774410d56742041be9b78df4822a07a7fe6efb927b3
  integral.overlattice_count: 041719e5d7e06ae6852166839661c74f744fac3ec892ea393fa70740348c4425
  integral.spinor_genus_count: a7a5ee97316ce61a012d9fe312cea9fd4e170838a1da335029ea1ffcbd83ae66
  integral.spinor_genera: a4fa92e024c36dc4cb57de885ce2bcfba3ada63d524eb336f6d8bc104b7dcb42
  integral.hyperbolic_index: a3743815a6a7693e61d39dcb8744a99c857dd520ed199355a69f2416eb0bda54
  automorphisms.automorphism_group_generator_morphisms: c2d006dd4e462d4e0b8dff2ddf2b401067ca38a678f305e7cbfcbdab231393ce
  integral.discriminant_form: 31b0370f0d2139a5b6e93576bdca472cf0ede495597e26e5a52c1ff537dd0fae
  integral.primitive_orbits: 004725896754c0b227402b9a4dd7084bff442ebafe79e4bb78dd20ce4d06d630
  integral.modular_scale: 20c5d9ba720bd9c3bbfbf7ecb7d14beff201ea8bec8d450ce85f0c4285473549
  integral.anisotropic_primes: f173f75edc3d06cc2b5a751d967a41fc3d49ca92c18b88b48aa0cf36a439dc02
  integral.local_representations: d4016fe3cb3d9122185e12aa430fec4ab6fc459b54158d6f368a9d61d8668a1f
  integral.local_densities: c42a3abd0a3cc81b39c826ab87e0d6c890ec3bd6c855df360693bdc9b6aec40d
rank: 3
gram_tensor:
- [2, 0, 0]
- [0, -4, 6]
- [0, 6, -12]
signature: [1, 2]
determinant: 24
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0]
- [0, -1, -1/2]
- [0, -1/2, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  modular_scale: false
  discriminant_group: [2, 2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'II_{1,2} (2: [2^-3]_1; 3: 1^2 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: []
      w: []
    SO:
      constant: 0
      z: []
      w: []
    Otilde:
      constant: 0
      z: []
      w: []
    SOtilde:
      constant: 0
      z: []
      w: []
    O+:
      constant: 0
      z: []
      w: []
    SO+:
      constant: 0
      z: []
      w: []
    Otilde+:
      constant: 0
      z: []
      w: []
    SOtilde+:
      constant: 0
      z: []
      w: []
  discriminant_form:
    orthogonal_group_order: 12
    isotropic_classes: 1
    isotropic_orbits: 1
  anisotropic_primes: [2, 3]
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
    - representative: 14
      least_valuation: 1
  - prime: 3
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 2
      least_valuation: 0
    - representative: 6
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [0, 2, 0, 3, 0, 3, 0, 1, 0, 0, 0, 3]
  - prime: 3
    densities: [4/3, 4/3, 0, 4/3, 4/3, 2/3, 4/3, 4/3, 4/9, 4/3, 4/3, 0]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: false
morphisms:
- target: 3IEP
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, -1, 3]
  - [0, 0, 1]
  scale: 1
- target: 3IEP
  name: O(L) generator 2
  matrix:
  - [5, 0, -6]
  - [6, 1, -9]
  - [4, 0, -5]
  scale: 1
- target: 3IEP
  name: O(L) generator 3
  matrix:
  - [3, 2, -6]
  - [2, 3, -6]
  - [2, 2, -5]
  scale: 1
- target: 3IEP
  name: O(L) generator 4
  matrix:
  - [5, 0, -6]
  - [0, 2, -3]
  - [2, 1, -4]
  scale: 1
- target: 3IEP
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID5.
- tag: 3ID5
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID5.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ID5.
