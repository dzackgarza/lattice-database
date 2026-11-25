---
tag: 3SYR
name: Constructed lattice 3SYR
latex: L_{\mathrm{3SYR}}
certifications:
  derive: aebe4b495ad25d6e38f3ee2cb2a48b245d4f323d9e96269c5652e9b6cb3a2332
  form.integer_valued: 094930af4a8cbe31c9b6ed124fb00bd97a252e0c5266b1ea5e79f136b8fb63e1
  integral.elementary_primes: 649509c07647522e5bf7eb7a3d4770c94aed9ca202b1cb90162bfda26c207cf4
  integral.genus_symbol: c8f2960c0074ca75680e563656d7da719d48e37464006d9efcf8fc3c1b6108e8
  integral.genus_class_count: 1e920f9fab4573bbeae18aeb7b34f3ee89fdba6a03aa470c5a5adb10e3e5d31c
  integral.overlattice_count: 524180435f0c2a3eec8695911b96b8d30abef4cffc3e6c30f3ef27372f911d9c
  integral.spinor_genus_count: bc4572d2225736250992abfbfbae66e5ee7377a667cd64b7c20ab0438f649719
  integral.spinor_genera: b96177ac3da500bcc25cb02d2d5cc024b321ebd57d4feca1f1675f12ef4b108c
  automorphisms.automorphism_group_order: e5e113e78fd79c93169624031a18408b858124471c7c312f6fb7f1717e63998b
  automorphisms.automorphism_group_generator_morphisms: b8b13ac9be766da4c85c34b26a2b6497af4581cad3c2959a2f20b7f63c10ae78
  integral.primitive_orbits: 2df33cd718d3d790d0abd3cb067a2b531e7cd5621c73037ae71647f6d854185f
  integral.modular_scale: b9875647896e3e843fabdff388d066de6092bc917543f75c5857335015f4e478
  integral.anisotropic_primes: 4472878e22fa9fbf174b43cc8442e65d8fa1813d882cab9454831c70110f9390
  integral.local_representations: 6b2d8cf3e68188c1a35e81c2115a26185f16c5c707c00b25ba630475e48ce19e
  integral.local_densities: ea1d709055c9d04578116fbbe48d5c3a87d289287c9f863554ab4d558bbc92d8
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 0, 2]
- [0, 0, 0, 2, 0]
signature: [3, 2]
determinant: 4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 0, 1/2]
- [0, 0, 0, 1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 2
  modular_scale: false
  discriminant_group: [2, 2]
  overlattice_count: 4
  bad_reduction_primes: [2]
  genus_symbol: 'I_{3,2} (2: [1^3]_1 2^2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
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
    densities: [7/4, 1/2, 1/2, 51/32, 5/4, 1/2, 1/2, 23/16]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17, O(L) generator 18, O(L) generator 19, O(L) generator 20, O(L) generator 21]
indefinite:
  isotropic: true
morphisms:
- target: 3SYR
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3SYR
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 2, 0]
  - [0, 0, 1, 2, 0]
  - [0, 0, 0, 1, 0]
  - [0, -1, 1, 0, 1]
  scale: 1
- target: 3SYR
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, -2]
  - [0, 0, -1, 0, -2]
  - [0, -1, 1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SYR
  name: O(L) generator 4
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 2, 0]
  - [0, 0, -1, -2, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 0, 1, 0, 1]
  scale: 1
- target: 3SYR
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, -2]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 2]
  - [-1, 0, -1, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3SYR
  name: O(L) generator 6
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3SYR
  name: O(L) generator 7
  matrix:
  - [1, 2, -2, 0, 0]
  - [-2, -1, 2, 0, 0]
  - [-2, -2, 3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SYR
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 2, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, -2, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 0, -1, 0, 1]
  scale: 1
- target: 3SYR
  name: O(L) generator 9
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SYR
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 3SYR
  name: O(L) generator 11
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SYR
  name: O(L) generator 12
  matrix:
  - [2, -1, 0, 2, -2]
  - [-1, 2, 0, -2, 2]
  - [0, 0, 1, 0, 0]
  - [-1, 1, 0, -1, 2]
  - [1, -1, 0, 2, -1]
  scale: 1
- target: 3SYR
  name: O(L) generator 13
  matrix:
  - [4, -1, 0, 4, -4]
  - [-1, -4, 4, 0, 0]
  - [-4, 0, 1, -4, 4]
  - [0, -2, 2, 1, 0]
  - [0, 2, -2, 0, 1]
  scale: 1
- target: 3SYR
  name: O(L) generator 14
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3SYR
  name: O(L) generator 15
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 3SYR
  name: O(L) generator 16
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 3SYR
  name: O(L) generator 17
  matrix:
  - [0, -1, 0, -2, 0]
  - [-1, 0, 0, -2, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [-1, -1, 0, -2, 1]
  scale: 1
- target: 3SYR
  name: O(L) generator 18
  matrix:
  - [-1, -2, 2, 2, 0]
  - [-2, -1, 2, 2, 0]
  - [-2, -2, 3, 2, 0]
  - [0, 0, 0, 1, 0]
  - [1, 1, -1, -1, 1]
  scale: 1
- target: 3SYR
  name: O(L) generator 19
  matrix:
  - [0, 1, 0, 0, 2]
  - [1, 0, 0, 0, -2]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [1, -1, 0, 1, -2]
  scale: 1
- target: 3SYR
  name: O(L) generator 20
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 3, 4, 2]
  - [0, 0, -2, -4, -1]
  - [0, 0, -1, -1, -1]
  scale: 1
- target: 3SYR
  name: O(L) generator 21
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 0013.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 0013.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 0013.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 3ICW, 0013.
