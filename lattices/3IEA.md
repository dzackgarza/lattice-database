---
tag: 3IEA
name: Constructed lattice 3IEA
latex: L_{\mathrm{3IEA}}
certifications:
  derive: 3333021ad5825f4281ee43bc4a9b7b6ac8b8b57f5fdd5e7532868214d25705f1
  form.integer_valued: 949aed2991e65f5465df68377702313c386bdd09ec431011a4fddc409805b172
  integral.elementary_primes: b4cd4a04992a29a55b118baceb39a7a60f551df77d183787d01cd9b590046a84
  integral.genus_symbol: aecfcc36a61e263ac8d3c6e90127b1f2418a8d6ce92560f54b0f115cb1d7f7b5
  integral.genus_class_count: e32eb13c7f5d37e64d01c1f71039c098ee0f7ec7b33b113e57f77aec383c9a95
  integral.overlattice_count: 46b3f4109e383c7c9db7c3a0fb4e60af87a8c18dfa9f59c8335faa9d99bf4fb0
  integral.spinor_genus_count: 0962fc12fee47acd7a3a087a51813aafd5eb328cb1eb841f908b4a841f0c46f0
  integral.spinor_genera: 977b35dbc8785513a92ff2bd7f6600e8992f197d0f812c22c0417d6c82207d23
  automorphisms.automorphism_group_generator_morphisms: f0d33c39905bebc22ee1b5ba1ba427db5bfda98cac0a5b30bba9f7b3e491b7cc
  integral.primitive_orbits: 7716924b48a50c2a83c0bf13ddc3b8a8e7560a1804f33c0b9c564f8ffec37f06
  integral.modular_scale: 1f76878a8ef3d983c81f92b4c1dba6c63283441da0219c647da28af78082d356
  integral.anisotropic_primes: 784776d9993b6aec2e269a760db724617c4342124a6e2b740cc2ec8ca035bd47
  integral.local_representations: 264b3e2b4cf37b3b621860ca8cadfbf77a045f306787e9d9dc9c02aa3c96f5cf
  integral.local_densities: 969193704a6955da33bf6afd4cd71dfe07ac6874b0e6f5c6e9595a24af8e0f88
rank: 3
gram_tensor:
- [-1, 0, 0]
- [0, 2, -3]
- [0, -3, 6]
signature: [2, 1]
determinant: -3
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0]
- [0, 2, 1]
- [0, 1, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [3]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{2,1} (2: [1^-3]_7; 3: 1^2 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
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
  anisotropic_primes: [2, 3]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
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
    densities: [3/2, 3/2, 0, 3/4, 3/2, 3/2, 1, 3/4, 3/2, 3/2, 0, 0]
  - prime: 3
    densities: [4/3, 4/3, 0, 4/3, 4/3, 2/3, 4/3, 4/3, 4/9, 4/3, 4/3, 0]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: false
morphisms:
- target: 3IEA
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 2, -3]
  - [0, 1, -2]
  scale: 1
- target: 3IEA
  name: O(L) generator 2
  matrix:
  - [5, 6, -6]
  - [-6, -8, 9]
  - [-2, -3, 4]
  scale: 1
- target: 3IEA
  name: O(L) generator 3
  matrix:
  - [3, 4, -6]
  - [-2, -3, 6]
  - [0, 0, 1]
  scale: 1
- target: 3IEA
  name: O(L) generator 4
  matrix:
  - [5, 6, -6]
  - [0, -1, 3]
  - [2, 2, -1]
  scale: 1
- target: 3IEA
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID4.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID4.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ID4.
