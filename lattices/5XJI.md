---
tag: 5XJI
name: Constructed lattice 5XJI
latex: L_{\mathrm{5XJI}}
certifications:
  derive: b9fd5a08f4a98913dd60158d0b6614d25b6ca6ae0611b080caccb81f62b26cf4
  form.integer_valued: 6c3bdd5e6737f414ce6824c410aa3222772d15bd685522f984655a8dc9920e50
  integral.elementary_primes: 739f3ca8459395d7548024e6aad992ab730abab52d67a97c066ff591e332a39a
  integral.genus_symbol: 90d3f0b9fa42ef53c54a9598977d9f6ca5485a8bc6962537cf4f18d1d9d01fd7
  integral.genus_class_count: ba56e246d5a8f5e5e7cac85a5434ed9a41aa2cb3987b6e77bc625182ef84da43
  integral.overlattice_count: e7a34c96f90bb790d480cd848158e9d7a9fa1e0df40ce1670996977c7ce4c66b
  integral.spinor_genus_count: edf32d27665f66cdd29ad342ef416191a1cc96f36b9bc1ca452b0fa4dfed75ae
  integral.spinor_genera: c0acc8d540d3961b865b315c4c0258e94f997726d024b511c7853f56d989546a
  integral.hyperbolic_index: 5398d57d98e05c28a972ff2910015413ce4c31323523835a50a52477dcdc8fb3
  automorphisms.automorphism_group_order: 535ecba57a1bb764c6ca9844ca723c050fd6256c586bed701a0be1805eddbb59
  automorphisms.automorphism_group_generator_morphisms: 6557de355288150737e82ef12a882cc3ac648439f3374bde9b40e301496cdf7d
  integral.primitive_orbits: 29ef0bbf6328f265ca4b1530d9a845051f10214e0188893d4dc5621a1d906af2
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, -2, 3, 0, 0]
- [0, 3, -6, 0, 0]
- [0, 0, 0, -4, 6]
- [0, 0, 0, 6, -12]
signature: [1, 4]
determinant: 72
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, -2, -1, 0, 0]
- [0, -1, -2/3, 0, 0]
- [0, 0, 0, -1, -1/2]
- [0, 0, 0, -1/2, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  discriminant_group: [2, 6, 6]
  overlattice_count: 12
  bad_reduction_primes: [2, 3]
  genus_symbol: 'II_{1,4} (2: 1^2 [2^3]_5; 3: 1^3 3^-2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
  primitive_orbits:
    O:
      constant: 2
      z: []
      w: []
    SO:
      constant: 2
      z: []
      w: []
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17]
indefinite:
  isotropic: true
morphisms:
- target: 5XJI
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, -1, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5XJI
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 3, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5XJI
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 2, -3]
  - [0, 0, 0, 1, -2]
  scale: 1
- target: 5XJI
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5XJI
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 2, -3, 0, 0]
  - [0, 1, -2, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5XJI
  name: O(L) generator 6
  matrix:
  - [5, 0, 0, 6, -6]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-6, 0, 0, -8, 9]
  - [-2, 0, 0, -3, 4]
  scale: 1
- target: 5XJI
  name: O(L) generator 7
  matrix:
  - [3, 0, 0, 2, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-4, 0, 0, -3, 0]
  - [-2, 0, 0, -2, 1]
  scale: 1
- target: 5XJI
  name: O(L) generator 8
  matrix:
  - [5, 2, 0, 2, 0]
  - [-8, -3, 0, -4, 0]
  - [-4, -2, 1, -2, 0]
  - [-4, -2, 0, -1, 0]
  - [-2, -1, 0, -1, 1]
  scale: 1
- target: 5XJI
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5XJI
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5XJI
  name: O(L) generator 11
  matrix:
  - [5, 2, 0, -2, 6]
  - [-8, -3, 0, 4, -12]
  - [-4, -2, 1, 2, -6]
  - [-2, -1, 0, 2, -3]
  - [-2, -1, 0, 1, -2]
  scale: 1
- target: 5XJI
  name: O(L) generator 12
  matrix:
  - [5, 0, 0, 6, -6]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-6, 0, 0, -7, 6]
  - [-4, 0, 0, -5, 5]
  scale: 1
- target: 5XJI
  name: O(L) generator 13
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5XJI
  name: O(L) generator 14
  matrix:
  - [7, -2, 6, 4, 0]
  - [-8, 3, -9, -4, 0]
  - [-4, 2, -5, -2, 0]
  - [-8, 2, -6, -5, 0]
  - [-4, 1, -3, -3, 1]
  scale: 1
- target: 5XJI
  name: O(L) generator 15
  matrix:
  - [7, 4, -6, 4, 0]
  - [-8, -6, 9, -4, 0]
  - [-4, -3, 4, -2, 0]
  - [-4, -2, 3, -1, -3]
  - [-4, -2, 3, -2, -1]
  scale: 1
- target: 5XJI
  name: O(L) generator 16
  matrix:
  - [7, 6, -6, 0, 0]
  - [-12, -11, 12, 0, 0]
  - [-4, -4, 5, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5XJI
  name: O(L) generator 17
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID3, 3ID5.
- tag: 3ID3
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID3, 3ID5.
- tag: 3ID5
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID3, 3ID5.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ID3, 3ID5.
