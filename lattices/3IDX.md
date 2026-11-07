---
tag: 3IDX
name: Constructed lattice 3IDX
latex: L_{\mathrm{3IDX}}
certifications:
  derive: a8f7e5ec57f3ef1cdc2e2d9760495a8963bcdf036eb3351821271e00bc32d30e
  form.integer_valued: b46f2c7aee01172eab1a49d4041757ae24d96984023d13a58af7ce64f8c79882
  integral.elementary_primes: 51282bd8f648b77e6a59cd60abbde1ce19327e5a07991f925604efb1adcf391e
  integral.genus_symbol: 3b38fa78dce085cc182ca065729506e6ec267836816ff0645ef57fbaea6a4c3f
  integral.genus_class_count: 36ad1b4f76386f33bf5051c5edb340a9c69dc6ca930244c149c77aa4e5badba9
  integral.overlattice_count: 83bca211b45577d1a0e0b2a1bc35ee8a6a29c1c17382b0c7d32aebe9ac6d467c
  integral.spinor_genus_count: 7c721330d070c602d6c6550772fff463c5a2d408dbcc3d8504ca2837febca638
  integral.spinor_genera: 90ee3e100da4074550263214fbcf03db87f869eca0036d98e71629dc33937253
  integral.hyperbolic_index: 448f4e7c3c9b19e166e28665ebcc4ffeb340b12fa2fba11525107e11fd574dae
  automorphisms.automorphism_group_generator_morphisms: 358486963e50a8fc202cee8aa96dfcf12ecece7e0dbc5f44cd8d3731217658ed
  integral.primitive_orbits: 3864f47c35218ad91d5c701d62b9a2d5643c47229f1476d7ce0ecee130d7be22
  integral.modular_scale: 3f4d2f98997325b71291a4937b13d8604b2bad3f3c243c769c11fa7031509e12
  integral.anisotropic_primes: 69cf345e9b32349e9b417c6691c7afe1615a5d52c4f4c545412ee6de53559155
  integral.local_representations: 1b36d2c8ee4c519c4a0061922f2ecd86397e31249a35b088a4f0b86f2cb625b9
  integral.local_densities: 7ab2aee133b693e258a507af9ad7e38f1f1f807bece629445bf856bd18ce3d02
rank: 3
gram_tensor:
- [-1, 0, 0]
- [0, 2, 0]
- [0, 0, 2]
signature: [2, 1]
determinant: -4
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0]
- [0, 1/2, 0]
- [0, 0, 1/2]
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
  genus_symbol: 'I_{2,1} (2: [1^1 2^2]_1)'
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
      least_valuation: 0
    - representative: 5
      least_valuation: 2
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
    densities: [2, 1, 1, 2, 0, 1, 1, 1/2, 2, 1, 1, 1/2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IDX
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3IDX
  name: O(L) generator 2
  matrix:
  - [3, 4, 0]
  - [-2, -3, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IDX
  name: O(L) generator 3
  matrix:
  - [3, 4, 0]
  - [0, 0, 1]
  - [2, 3, 0]
  scale: 1
- target: 3IDX
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0002, 0002.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0002, 0002.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 0002, 0002.
