---
tag: 3XSJ
name: Constructed lattice 3XSJ
latex: L_{\mathrm{3XSJ}}
certifications:
  derive: 609eb9b3e8723f15b957e999267717f0309f90da454e4005e215024ba9446959
  form.integer_valued: d24c4debc60b1a0445dfc46ec0c3d75cb66d926916ffc3473d75a4cf71af2413
  integral.elementary_primes: 4276fdc7d8291fe680747791114b5b27b0500cf984d9ef2df76e0c02950a2172
  integral.genus_symbol: e5ff922ec1a45d29fee7d100500694d0a8cebc51ca924880f6f2f49eb7c724b5
  integral.genus_class_count: 578dbb0b0a7c454c1155a2a6efa6c54e8285044ffb013a0ea43afa8223af0ca5
  integral.overlattice_count: ccd1a27b9413dc0139a722547ac197ce35d4e30e8491d6eba761a030a441cc6b
  integral.spinor_genus_count: 13818e254d244d5cd01c3a66f4e262fc98295fe3505525a5774c776676c84814
  integral.spinor_genera: 25573c7b9ce95850635cb972d068f2f8681614ffd9ee9c2807970c09f10cd5bc
  integral.hyperbolic_index: b39bce78ae2c046dce0e44b117500d2f48b081c579c1c367a4aa3fee46306760
  automorphisms.automorphism_group_generator_morphisms: 90a48fdab95c031cd8f339d1fe392ca54aa6a7eab31f4b33f81e28f00e4aeb7c
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, 1, 0, 0]
- [0, 0, 0, 1]
- [0, 0, 1, 0]
signature: [3, 1]
determinant: -1
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, 1, 0, 0]
- [0, 0, 0, 1]
- [0, 0, 1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 2
  discriminant_group: []
  overlattice_count: 1
  bad_reduction_primes: [2]
  quadratic_character: -4
  genus_symbol: I_{3,1}
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 3XSJ
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3XSJ
  name: O(L) generator 2
  matrix:
  - [0, -1, 1, 0]
  - [-1, 0, 1, 0]
  - [0, 0, 1, 0]
  - [1, 1, -1, 1]
  scale: 1
- target: 3XSJ
  name: O(L) generator 3
  matrix:
  - [-3, 0, 2, -2]
  - [0, 1, 0, 0]
  - [-2, 0, 2, -1]
  - [2, 0, -1, 2]
  scale: 1
- target: 3XSJ
  name: O(L) generator 4
  matrix:
  - [0, -1, 0, 0]
  - [-1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3XSJ
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0016.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0016.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 0016.
