---
tag: 3IDK
name: Constructed lattice 3IDK
latex: L_{\mathrm{3IDK}}
certifications:
  derive: ae1e1be84d8d1162aee342381f0f3cc5dc48ebdfcebc502453ec9b4762d1a468
  form.integer_valued: 0b21612e609665531baa9983bd88fde0650873fb44b31ad948cc3e209bdea268
  integral.elementary_primes: 68ce00d2c785504b6f1041220dba84ab756cb3e0c832d1337ca59e0823284231
  integral.genus_symbol: e2ffbde3b6a5415a59632cb4b4d6673ddda8a2f40196b2b7e40974f2b102e1e6
  integral.genus_class_count: f2603b3fcdbc9150389d07b07ab4e341862c07377990a2dfafb7fea3115978ae
  integral.overlattice_count: 95e537dfe2b472fe3a38b012ccd63a0c4556e239586c62976d86f5001c75a53b
  integral.spinor_genus_count: db84a79cea94cb65bcd084ef7f3f3aba0497996815cbcb29a36c18745898df5f
  integral.spinor_genera: 53cfdfa356acd0f06d09669a1e55380b009d13c7bd4c976db201dd4d62059296
  automorphisms.automorphism_group_generator_morphisms: 077667478d768782e19fcccd05c8e43f3ffa4d079bfe91e13d4946303ccb55f9
  integral.primitive_orbits: 31be30a4f7e5397f154a82f902e3993c69f2fd33930d58cf823e6be15e8074d8
  integral.modular_scale: ddaf5a542eafa3f47786a71de8cbcf5bcf0e32f18147a23873edb81a23cb8e87
  integral.anisotropic_primes: f678a1170a839e8d3cccd74329430391ec553ec2ebeb490506ef1704c67f96cb
  integral.local_representations: a2fbd334e96560e5b2388b30c3b17ff16c1ae64e8d23bbf1723e0974c4f7ce69
  integral.local_densities: 2444297e8670048fd2c765a4c683e9b6a692cf143d11d1cf9b7c30a2c2e07226
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, -2, 1]
- [0, 1, -2]
signature: [1, 2]
determinant: 3
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, -2/3, -1/3]
- [0, -1/3, -2/3]
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
  genus_symbol: 'I_{1,2} (2: [1^-3]_1; 3: 1^2 3^1)'
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
    - representative: 3
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
    - representative: 3
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [1, 3/2, 3/2, 1/2, 0, 3/2, 3/2, 3/4, 1, 3/2, 3/2, 3/4]
  - prime: 3
    densities: [4/3, 4/3, 2/3, 4/3, 4/3, 0, 4/3, 4/3, 4/9, 4/3, 4/3, 2/3]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: false
morphisms:
- target: 3IDK
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 1, -1]
  scale: 1
- target: 3IDK
  name: O(L) generator 2
  matrix:
  - [3, 2, 2]
  - [-2, -1, -2]
  - [-2, -2, -1]
  scale: 1
- target: 3IDK
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IDK
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID0.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID0.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ID0.
