---
tag: 3SQE
name: Constructed lattice 3SQE
latex: L_{\mathrm{3SQE}}
certifications:
  derive: 6e1e2379f47e2dbbc2ee0aa07aee53ba2a65938bff7493b53d73773cd738ed8f
  form.integer_valued: d626dc730d639b47eafed5a588e58b9390015fe7e5313998889824ff119f0102
  integral.elementary_primes: e1315ad7fa2b99e12f443aaebb1a4fedf56125b4c10fdeae1d3388344080f896
  integral.genus_symbol: a41fd14aa87a75164042c1069705d29dd0cc7e9cc572116a73a3695d8c1cf9b6
  integral.genus_class_count: b3732c6ea373c754e741f4187ed7aa5a954d366ab178a633f8879f8e036e04c1
  integral.overlattice_count: 465a0399b93500e442b441683276517dc917af11280463611fa4f2dc86f1136c
  integral.spinor_genus_count: 7606e51827c2ce3b72c080fdb75146bb80a1c4dfb1a67534fd5f4968e432c6a2
  integral.spinor_genera: 6666752bf39350dd810827d6c86fded7cfdd65faf2420e02dbdf3a11075cb1a5
  automorphisms.automorphism_group_order: 5f73727d1965807ac045e6c4d373922b9ab1461781751cc0260536a7067a3947
  automorphisms.automorphism_group_generator_morphisms: a5c28d27ff1a97cce69b487b32e97616cce97be62817580f0816a127fe348ad3
  integral.primitive_orbits: 00fb2769f56dc09819775a726b7c52a67a7fecade2fcdd47290b02bedad0763e
  integral.modular_scale: e0b1553e3fc5c698ecb59f0df35ba819b20388131ea1ccc4e593afd4ef5ef936
  integral.anisotropic_primes: 2f0c79bd19ee80a3bff10d1cc717b2df90d15ef97809ee9e6d2e76dc8ca9834d
  integral.local_representations: 681da78e6c3cafecd546ff88774179bc198682f1df450f18c72bdb2e3158aec2
  integral.local_densities: d0a63d31a660a84ffafe1afe7baf707fbd178d97ce689904449e24947f7cce02
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 0, 1]
- [0, 0, 0, 1, 0]
signature: [3, 2]
determinant: 1
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 0, 1]
- [0, 0, 0, 1, 0]
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
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17]
indefinite:
  isotropic: true
morphisms:
- target: 3SQE
  name: O(L) generator 1
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 3SQE
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3SQE
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 1]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 1]
  - [-1, 0, 1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 1]
  - [0, 0, 1, 0, 1]
  - [0, -1, 1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 1, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 1, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 0, 1, 0, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 8
  matrix:
  - [-1, 2, 2, 0, 0]
  - [-2, 1, 2, 0, 0]
  - [-2, 2, 3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 1, 0]
  - [0, 0, 1, 1, 0]
  - [0, 0, 0, 1, 0]
  - [0, -1, 1, 0, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 10
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 1]
  - [0, 0, 1, 0, -1]
  - [0, -1, -1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 1, 0]
  - [0, 0, 1, -1, 0]
  - [0, 0, 0, 1, 0]
  - [0, -1, -1, 0, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 13
  matrix:
  - [-7, -4, 8, 0, 0]
  - [-4, -1, 4, 0, 0]
  - [-8, -4, 9, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 14
  matrix:
  - [0, 1, 0, -1, 0]
  - [1, 0, 0, 1, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 1, 0, -1, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 15
  matrix:
  - [0, 1, 0, 0, 1]
  - [1, 0, 0, 0, -1]
  - [0, 0, 1, 0, 0]
  - [1, -1, 0, 1, -1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SQE
  name: O(L) generator 16
  matrix:
  - [-1, -4, 4, 0, 0]
  - [-4, -7, 8, 0, 0]
  - [-4, -8, 9, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3SQE
  name: O(L) generator 17
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 0016.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 0016.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 0016.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 3ICW, 0016.
