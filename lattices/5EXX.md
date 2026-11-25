---
tag: 5EXX
name: Constructed lattice 5EXX
latex: L_{\mathrm{5EXX}}
certifications:
  derive: 62bd29c07f263afc6d24df68d8583904fe4a0af43b6c98f655f94dc4c1fd10fb
  form.integer_valued: bb2c18e6620d175a3ba167155f23d1a3fbdc706b72976f6d05c93afc5ff8770a
  integral.elementary_primes: ade7ef55f88e17cc7fde83108fb1bfcbb6cc4bf1de83d86f6c20904213e583ba
  integral.genus_symbol: d6ad615bb89d6214f84070d9e6d79f8ae3aa17b3f28166b15b8466cb350541c5
  integral.genus_class_count: 0e98d2fb69bea5a357d156f347e6f0d505c31c7568f2ac590878314d3fc44191
  integral.overlattice_count: ab1b345f8c6c0378c26a3e015534ae3e9b215e86197007ffb89a7ae74b4d71d7
  integral.spinor_genus_count: 724e8fa01b11c3c3141b5a7399c7585c4daa03f0988a36f89abe02e44641d786
  integral.spinor_genera: 85e96ed8f3a45fa99749e0954565e87567f15906310aead574e7a535cdc8ccad
  integral.hyperbolic_index: 41f3af2e0a1508dd9e1a68bec2b80e6d061fd29b4e148521ca687dbd0d2903ea
  automorphisms.automorphism_group_order: 8ef63b5282edf6cdd39a2f6001c2f7fbc3b6c067c8575e7b713d99388068d30e
  automorphisms.automorphism_group_generator_morphisms: a5e99b05a2a382e09827bf94eafdb433fe310606910069f0d1ad386b7dfb564b
  integral.primitive_orbits: 002c0ec300afd1496240a75f1976d2795b3b15c4f94783ebe119d0e2d56364cf
  integral.modular_scale: 6b8242abff3b9e47bd505d24d22e81d7315bf2f28ff1cdb4422dc8d77662bebc
  integral.anisotropic_primes: 136e12b378569c047af0c2e89133a1509f430ca92de1b347982ca0f7d665e4f9
  integral.local_representations: b1c495dee02d488e1afc00f54b7f7e646551b16531419d4495d0f0d74059a197
  integral.local_densities: 2980c524a3d11280c53a41fe9ae076313383868cc29b57bd448aa990e8f828b3
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 0, -4, 2]
- [0, 0, 0, 2, -4]
signature: [1, 4]
determinant: 12
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 0, -1/3, -1/6]
- [0, 0, 0, -1/6, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{1,4} (2: [1^-3]_3 2^2; 3: 1^-4 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
  primitive_orbits:
    O:
      constant: 2
      z: []
      w: []
    O+:
      constant: 2
      z: []
      w: []
    SO:
      constant: 2
      z: []
      w: []
    SO+:
      constant: 2
      z: []
      w: []
    Otilde:
      constant: 4
      z: []
      w: []
    Otilde+:
      constant: 4
      z: []
      w: []
    SOtilde:
      constant: 4
      z: []
      w: []
    SOtilde+:
      constant: 4
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1/2, 1/2, 7/4, 23/16, 1/2, 1/2, 5/4, 23/16]
  - prime: 3
    densities: [10/9, 10/9, 20/27, 10/9, 10/9, 22/27, 10/9, 10/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13]
indefinite:
  isotropic: true
morphisms:
- target: 5EXX
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5EXX
  name: O(L) generator 2
  matrix:
  - [-1, 2, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [2, -2, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EXX
  name: O(L) generator 3
  matrix:
  - [-3, 2, -2, 0, 0]
  - [-2, 2, -1, 0, 0]
  - [2, -1, 2, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EXX
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 2, -1, -2, -2]
  - [0, -1, 2, 2, 2]
  - [0, 1, -1, -1, -2]
  - [0, 1, -1, -2, -1]
  scale: 1
- target: 5EXX
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, -2, 1, 2, 2]
  - [0, 1, 0, 0, -1]
  - [0, 1, 0, -1, 0]
  scale: 1
- target: 5EXX
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EXX
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 5EXX
  name: O(L) generator 8
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EXX
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, -2, 1, -2, 4]
  - [0, 1, 0, 1, -1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 5EXX
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -2, -2, -2]
  - [0, -2, 3, 6, 0]
  - [0, 1, -2, -3, -1]
  - [0, 1, -1, -2, -1]
  scale: 1
- target: 5EXX
  name: O(L) generator 11
  matrix:
  - [-1, 6, -4, -12, 0]
  - [-4, 13, -8, -24, 0]
  - [6, -18, 13, 36, 0]
  - [-4, 12, -8, -23, 0]
  - [-2, 6, -4, -12, 1]
  scale: 1
- target: 5EXX
  name: O(L) generator 12
  matrix:
  - [-5, 6, -6, -12, 0]
  - [-6, 7, -6, -12, 0]
  - [6, -8, 7, 14, 2]
  - [-4, 5, -4, -8, -1]
  - [-2, 3, -2, -5, 0]
  scale: 1
- target: 5EXX
  name: O(L) generator 13
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICY, 3ID1.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICY, 3ID1.
- tag: 3ID1
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICY, 3ID1.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICY, 3ID1.
