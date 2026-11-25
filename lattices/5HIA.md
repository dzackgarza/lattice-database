---
tag: 5HIA
name: Constructed lattice 5HIA
latex: L_{\mathrm{5HIA}}
certifications:
  derive: 66c0c506ed73edb1b2df1e7429b5963b077d0fb9d0086b397ee8b0cbdf422a79
  form.integer_valued: 520c6fdbe6b2311e8345b69a51fa2c3a3d945e622c9bdf94709246c5bd4b4604
  integral.elementary_primes: 1675ab866c9b46079dc226fd1f2fb8d577e652c56d48d665d13178cf354b9f78
  integral.genus_symbol: 8bfa2d0fcb3c9cc950da2f20da6e893f27cd9574e70eadf3bc2b91e080fa5c4b
  integral.genus_class_count: 6a198ab0b3bd88843518678032d4885219c1fe7b5c87c8b7dc3a7443bfd5f99a
  integral.overlattice_count: f0264e57b384d9cbf3c3104769790c4df4cff99b0b5f4bc95dbe9d37abce9906
  integral.spinor_genus_count: 257ecd88942b73835936db51b5e737aa3fd50dacfe539972d3dd400674484ff5
  integral.spinor_genera: 7835260f0eaee92cbbbd0fe7e04e9b66a7942ef064a6b9f7e7220354eeae8aa1
  automorphisms.automorphism_group_order: 20541e697edff9c8d9b8cfb9078285037db74ee7e26694d231dde610865ec8d1
  automorphisms.automorphism_group_generator_morphisms: 8ee015a1f1f16171ab82e8e89bd94136e9c8d4d2dc72063d0a698e5ccc4d31bb
  integral.primitive_orbits: 5fe3c14ab31f390ca9e25fcf81ed7970aeb96653df48bb4f84b2c03c8337dab9
  integral.modular_scale: e8c413985afa34d8486840d78066320fadeae20ae2c96fc90b1e4dc0cd5c2cb9
  integral.anisotropic_primes: 9f0fb823167838bf7aeb7cc741e9be09474d4375f2f5b4e537c61aec2c1fbf98
  integral.local_representations: b017ca61b8eb25c3db97d01c209af49d2378e30eccefabff6b40f20c17bed57c
  integral.local_densities: 2ef243cba0f2f1c3a892d0a81161a1565eaab222ac0ff5bc0e08b8c855356390
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 4, -2, 0, 0]
- [0, -2, 4, 0, 0]
- [0, 0, 0, 2, -3]
- [0, 0, 0, -3, 6]
signature: [4, 1]
determinant: -36
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 1/3, 1/6, 0, 0]
- [0, 1/6, 1/3, 0, 0]
- [0, 0, 0, 2, 1]
- [0, 0, 0, 1, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [6, 6]
  overlattice_count: 12
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{4,1} (2: [1^3]_3 2^2; 3: 1^3 3^-2)'
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
      constant: 9
      z: []
      w: []
    SOtilde:
      constant: 9
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [3/2, 3/2, 3/4, 9/16, 3/2, 3/2, 1/4, 9/16]
  - prime: 3
    densities: [2/3, 4/3, 26/27, 2/3, 4/3, 26/27, 2/3, 4/3]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15]
indefinite:
  isotropic: true
morphisms:
- target: 5HIA
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5HIA
  name: O(L) generator 2
  matrix:
  - [9, 12, 0, 8, -12]
  - [-4, -5, 0, -4, 6]
  - [-2, -3, 1, -2, 3]
  - [-4, -6, 0, -3, 6]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5HIA
  name: O(L) generator 3
  matrix:
  - [5, 4, 4, 4, -6]
  - [-2, -1, -2, -2, 3]
  - [-2, -2, -1, -2, 3]
  - [-2, -2, -2, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5HIA
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -3]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5HIA
  name: O(L) generator 5
  matrix:
  - [3, 0, 0, 4, -6]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-2, 0, 0, -3, 6]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5HIA
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5HIA
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, -1, 1]
  scale: 1
- target: 5HIA
  name: O(L) generator 8
  matrix:
  - [5, 4, 4, 2, -6]
  - [-2, -1, -2, -1, 3]
  - [-2, -2, -1, -1, 3]
  - [2, 2, 2, 2, -3]
  - [2, 2, 2, 1, -2]
  scale: 1
- target: 5HIA
  name: O(L) generator 9
  matrix:
  - [5, 0, 0, 6, -12]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [2, 0, 0, 3, -5]
  scale: 1
- target: 5HIA
  name: O(L) generator 10
  matrix:
  - [3, 0, 0, 2, -6]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [2, 0, 0, 3, -6]
  - [2, 0, 0, 2, -5]
  scale: 1
- target: 5HIA
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5HIA
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, -1, 2]
  scale: 1
- target: 5HIA
  name: O(L) generator 13
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 1, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5HIA
  name: O(L) generator 14
  matrix:
  - [19, 28, 4, 10, -18]
  - [-10, -15, -2, -5, 9]
  - [-4, -6, -1, -2, 3]
  - [2, 4, -2, 2, -3]
  - [4, 6, 0, 3, -5]
  scale: 1
- target: 5HIA
  name: O(L) generator 15
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID2, 3ID4.
- tag: 3ID2
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID2, 3ID4.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID2, 3ID4.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ID2, 3ID4.
