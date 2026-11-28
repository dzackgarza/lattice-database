---
tag: 3SUT
name: Constructed lattice 3SUT
latex: L_{\mathrm{3SUT}}
certifications:
  derive: 366769a0a48e06e8e6791f4908a60fb5f08ad9f89f4819cc310cadd31a0ee576
  form.integer_valued: 0b84a47ed3b4940b5f71b3ebe9360087fa282571d29b6895c49646807bc216e1
  integral.elementary_primes: 134140d6a26b7de5bf34b31d7bf35634dbd293bdc8a2f4a45f3e5a8c836e50e4
  integral.genus_symbol: de5d313e94618e083312486e572f08cec13c809d74a66f8075d84b8db938d333
  integral.genus_class_count: dfd5362d4609413d0317ed7a20bac7d55aa9cd50efea1324b15073da83bd2db9
  integral.overlattice_count: 9526388c29c9f56a5bb81644b0161aa74f86831a1b8ce602d0c785c724e73929
  integral.spinor_genus_count: c4b59370de4862d7eaebbd26304037bebe0e61ba1bdadbe70af3e6d6eb6d3e00
  integral.spinor_genera: 20ee0ccf860c37342c06584cf2348dcea9b2061ba5e0d066354e258a41ecc437
  integral.hyperbolic_index: 0f8ebba6f15c7fe185016e780a374bfecb33c675daef2e52f058cd78686d5c05
  automorphisms.automorphism_group_order: 187f387b15f010b8393cc516ed2e8881d655836c912a30d20ac871f7bef2c7bb
  automorphisms.automorphism_group_generator_morphisms: 6f8b7712100116a671354cf822b89eb03edbd9e52d5b536a82f63df41a876f09
  integral.primitive_orbits: 34a789f56f7914df930553ee18229e544d5662882576f9611b5d96d808f46ff4
  integral.modular_scale: 4a833764439778af3bfcc47b11e42067e2d7f890913326a08584499f553d7f8f
  integral.anisotropic_primes: ddbff5bfb221000f3c830c6c72b2f1fbdf970f3adece8df1a79c0ba2138ce18c
  integral.local_representations: 3ad9480799c75ce2cc970f3697eb89d09c023d62b4e5ab64505acc0e096f562d
  integral.local_densities: fd5e58bcf662de6e8b9af65f49aae3f7f187b609c019f15d96a20d5d7e864653
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 0, -1]
- [0, 0, 0, -1, 0]
signature: [3, 2]
determinant: 1
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 0, -1]
- [0, 0, 0, -1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 2
  modular_scale: 1
  discriminant_group: []
  overlattice_count: 1
  bad_reduction_primes: [2]
  genus_symbol: I_{3,2}
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 2
  primitive_orbits:
    O:
      constant: 1
      z: []
      w: []
    O+:
      constant: 1
      z: []
      w: []
    SO:
      constant: 1
      z: []
      w: []
    SO+:
      constant: 1
      z: []
      w: []
    Otilde:
      constant: 1
      z: []
      w: []
    Otilde+:
      constant: 1
      z: []
      w: []
    SOtilde:
      constant: 1
      z: []
      w: []
    SOtilde+:
      constant: 1
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [11/8, 3/4, 3/4, 83/64, 9/8, 3/4, 3/4, 39/32]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16]
indefinite:
  isotropic: true
morphisms:
- target: 3SUT
  name: O(L) generator 1
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SUT
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 3SUT
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3SUT
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SUT
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, -1, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, -1, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 0, 1, 0, 1]
  scale: 1
- target: 3SUT
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, -1, 0]
  - [0, 0, 1, -1, 0]
  - [0, 0, 0, 1, 0]
  - [0, -1, 1, 0, 1]
  scale: 1
- target: 3SUT
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, -1]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, -1]
  - [-1, 0, 1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SUT
  name: O(L) generator 8
  matrix:
  - [-1, 2, 2, 0, 0]
  - [-2, 1, 2, 0, 0]
  - [-2, 2, 3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SUT
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, -1]
  - [0, 0, 1, 0, -1]
  - [0, -1, 1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SUT
  name: O(L) generator 10
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SUT
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, -1, 0]
  - [0, 0, 1, 1, 0]
  - [0, 0, 0, 1, 0]
  - [0, -1, -1, 0, 1]
  scale: 1
- target: 3SUT
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, -1]
  - [0, 0, 1, 0, 1]
  - [0, -1, -1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SUT
  name: O(L) generator 13
  matrix:
  - [-7, -4, 8, 0, 0]
  - [-4, -1, 4, 0, 0]
  - [-8, -4, 9, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SUT
  name: O(L) generator 14
  matrix:
  - [0, 1, 0, 1, 0]
  - [1, 0, 0, -1, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 1, 0, 1, 1]
  scale: 1
- target: 3SUT
  name: O(L) generator 15
  matrix:
  - [-1, -4, 4, 0, 0]
  - [-4, -7, 8, 0, 0]
  - [-4, -8, 9, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3SUT
  name: O(L) generator 16
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ICY.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ICY.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ICY.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ICY.
