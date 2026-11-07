---
tag: 3IEH
name: Constructed lattice 3IEH
latex: L_{\mathrm{3IEH}}
certifications:
  derive: 5920575ef7305bc17ca4c93157fd3dc50b51b566aa7db2c2d63991df75c4de93
  form.integer_valued: 577a61e66af36ce25caa64fcaf58d02558007fb50d827225e271a4fb75a17900
  integral.elementary_primes: 223ea0d9e6f762c4c6902dd59600eb36c2adc603cb3a2348b21976a2ef49baa7
  integral.genus_symbol: 9824c0cfe68a3f8ab1cb1e4730a84dec27adc40a135799bc3bda68a690823798
  integral.genus_class_count: f04e0eade8424b6be0155add0965f2cd6209a23e2b424da03f94149dd4e90084
  integral.overlattice_count: eba5815a9cb53366f732230492c3dab9a096125ec167f35eae477fb11bfd73ce
  integral.spinor_genus_count: f47b8665ab03c698e784645453bec5dd0a6b92ee1c8f6ac271be6153ea742eeb
  integral.spinor_genera: 31db9dd68e8b67a8178f2be964cdc6135de96b4ecbbbca61ed4d93e7f5d890ee
  integral.hyperbolic_index: 0b905447b9fe9310a1669f35db91550430a241efe1f4cae41414f0782707d895
  automorphisms.automorphism_group_generator_morphisms: 79ac93894609b69335e1806eec5933d94530e85724602f26e34ab772cf98e20b
  integral.discriminant_form: 234198e5c652815eefa5ab0b798bcf457513b243cf9bbc7e9cd070080e6b080a
  integral.primitive_orbits: a1820d82f7ba8e127e836d673421122e66752e89ea47a455fee13a955a68afdb
  integral.modular_scale: 74ec73f6abb9a43f42f4c518108411a615475cd22321a56126bb71e76b26417e
  integral.anisotropic_primes: fe80fa2ae2d8e5f2b484cf6cba36c0ccf734acf4b0492a90b0c6795cc518c6d1
  integral.local_representations: 7c1e97f21852b32df1659ad6b38c093d5d80be8a9deb4b919b8d406410fab728
  integral.local_densities: 670bbfc11626345ac95bf624d0f4fa41a28942415b83f163a7b45edfa371cced
rank: 3
gram_tensor:
- [2, 0, 0]
- [0, 0, 2]
- [0, 2, 0]
signature: [2, 1]
determinant: -8
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0]
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
  genus_symbol: 'II_{2,1} (2: [2^3]_1)'
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
    densities: [0, 4, 0, 1, 0, 1, 0, 4, 0, 2, 0, 1]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IEH
  name: O(L) generator 1
  matrix:
  - [-1, 2, 0]
  - [0, 1, 0]
  - [2, -2, 1]
  scale: 1
- target: 3IEH
  name: O(L) generator 2
  matrix:
  - [-3, 2, -2]
  - [-2, 2, -1]
  - [2, -1, 2]
  scale: 1
- target: 3IEH
  name: O(L) generator 3
  matrix:
  - [1, 0, 2]
  - [-2, 1, -2]
  - [0, 0, 1]
  scale: 1
- target: 3IEH
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0013.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0002, 0013.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0013.
