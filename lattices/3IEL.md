---
tag: 3IEL
name: Constructed lattice 3IEL
latex: L_{\mathrm{3IEL}}
certifications:
  derive: ce8e1ffa8322a12f0082fd90dd0f4840d7387a5d89a0c5663d2976c38975de8e
  form.integer_valued: f6efd76e6a36678fe02de59e721a1ca7c2335fdcd0cd714eaaa765cccdd55edc
  integral.elementary_primes: 3ef7e879d965504da3deccddb231f240849ef30efcc17be637e2df5f074a35f0
  integral.genus_symbol: 601210d836ea4b38d5532d8a031d41c755944ddc02a173b33520fa7c1f61f34c
  integral.genus_class_count: f175a99efc5ccb23885b4649fc7074dd5275b57de412ae5e240f11b86b09c8d4
  integral.overlattice_count: c2b2e461d6ae060abc0eaf4aa57c4793bdc6ec1e7e48ea35da2582e98533edaa
  integral.spinor_genus_count: ac50eb3c0e3381e027df94db1289eb6a5b5645f61b31a1accbc5a51266ed5f92
  integral.spinor_genera: 63cdd6d47584cf263a2b9fdb0c8deb7ecbe957e464b7a6170b0405a32456608e
  integral.hyperbolic_index: cdedcdad0c0efa796940ab3ec5ca549b04bb1c9418b05873c724337165578861
  automorphisms.automorphism_group_generator_morphisms: a7add08972e0892a1ab98d378e198e57f0a5d46af719d34203afab79d207d467
  integral.discriminant_form: 82745fa7e15882dd9ef6108492406e31d75d27fc7377f3aa2e7861721c9827b5
  integral.primitive_orbits: 1fd975f8e2c6081ab2961ea5799804dfc1e13bf4fff53ed03edfcf79855ef17b
  integral.modular_scale: 1133826ba5c0328d1655a82903935c934bae30a8f067967ad416a1ad58a0d965
  integral.anisotropic_primes: e1ec3030322825fa642d365d9abd45b89834556db6f29e03cba712beb70f4138
  integral.local_representations: fe647f3e1b35a5107819ed57d0515095393755c17d1ccc9afbdffac2b67523bc
  integral.local_densities: 40221d7e36c28942222d403aa43c483bcbfee69955c740bf2b461ebce2e0fbd4
rank: 3
gram_tensor:
- [2, 0, 0]
- [0, -4, 2]
- [0, 2, -4]
signature: [1, 2]
determinant: 24
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0]
- [0, -1/3, -1/6]
- [0, -1/6, -1/3]
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
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: false
morphisms:
- target: 3IEL
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 1, -1]
  scale: 1
- target: 3IEL
  name: O(L) generator 2
  matrix:
  - [3, 2, 2]
  - [-2, -1, -2]
  - [-2, -2, -1]
  scale: 1
- target: 3IEL
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IEL
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID1.
- tag: 3ID1
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID1.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ID1.
