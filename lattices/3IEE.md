---
tag: 3IEE
name: Constructed lattice 3IEE
latex: L_{\mathrm{3IEE}}
certifications:
  derive: fb3b42f45353f78b825a07f7c6c9d824538b31ac11807bcedfc36e09b8a93ca7
  form.integer_valued: 0f902c3552171151816b5ebe63b1a56c4a7ac7664b640d7c08f3fbe17c86549a
  integral.elementary_primes: 72a7e816dedfe30132ed1729f237363f83c9d0088bd9d72315c54b466f55291a
  integral.genus_symbol: f12c6f588ca11611e91d10cedb5ef1ce654d9d63b048120e6ed36c0c748646ad
  integral.genus_class_count: 5fffde8f736dd503a73dd80312526ade9cf82b633a1a29e49f384438fd3e95d1
  integral.overlattice_count: 0e50ed2f8cb751bc598a8dde73a988f8d78d875182abadec1dc9d6b1d5a05a4d
  integral.spinor_genus_count: e244332f98729229b0bef00a40029165afa704cf6916fba09002440e067e49fb
  integral.spinor_genera: 093253c92748a8dfad90e1835a0c8264506b1142c522656a934f8b7c6dd41196
  integral.hyperbolic_index: be648174688a85216a54c34b7cc29a1a71a3f7176c2755345c1aa02672f51704
  automorphisms.automorphism_group_generator_morphisms: dc8fda6b26334d0e37af3a1f6d36452c8fe959e3452a8da4f1476b7fc8817ce1
  integral.discriminant_form: 33bf83da061528ac4d3cd878f44bc9b3c75295693b0e4146c86046700b659122
  integral.primitive_orbits: 5c243bbfd031a91ed7b36b72b26043407efad57abb0f4ef87d367e8510f073c4
  integral.modular_scale: 35e2e9b2fe3b32db5c15068a58da6d28a4e4f9de9542f7ddbf000442d7f6595f
  integral.anisotropic_primes: ca6b66d65484b6ddddaf6200664b786dce3acbcb51bc4ed267cd31c8322bf5d8
  integral.local_representations: 10737b1d483f80b15a5bd7730311b90610d06b95e71d580c20c3e45fd243413a
  integral.local_densities: 6a8f3e8915a55fb7b82f2dbaee432eeb02347f96ec2862a74faba02b3b1d8aca
rank: 3
gram_tensor:
- [2, 0, 0]
- [0, -2, 0]
- [0, 0, -2]
signature: [1, 2]
determinant: 8
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0]
- [0, -1/2, 0]
- [0, 0, -1/2]
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
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 3IEE
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IEE
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3IEE
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IEE
  name: O(L) generator 4
  matrix:
  - [3, 2, 2]
  - [2, 1, 2]
  - [2, 2, 1]
  scale: 1
- target: 3IEE
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ICX, 3ICX.
