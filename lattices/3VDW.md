---
tag: 3VDW
name: Constructed lattice 3VDW
latex: L_{\mathrm{3VDW}}
certifications:
  derive: 6d1572d0df0833c2fa16c52aea461f42b3ef3f7e0c5d5b4033569053cf07e709
  form.integer_valued: 233814e5e5c1765d8bd68d7f4c91d5742c81041f856cdcfc2a5198e071746ce4
  integral.elementary_primes: bc9f59d4c796baf2d7ce5a4536960c2181c5d151543e099f8758053bed8d6e46
  integral.genus_symbol: debf30d2f121fdf2009f40a171bed09036a05457c7510c1cc9ea80ceea5ffa54
  integral.genus_class_count: 3eb5fb5ebadae947ee5650b2e5675a80b0dd7a3f45a191493e2566342218ad5f
  integral.overlattice_count: c8f8fe26ca413706ff17bcf77a09d8d6c453e97631c0a52acdaa151d4fc0f1f2
  integral.spinor_genus_count: f38d69a49dce364699bb57510d03921dca945f8a49f1c47dc1c240bae7599092
  integral.spinor_genera: ff43e40f8c94066e15ba9f4f4ef2e3c204d7daa1bde676d3662271ce941cfbde
  integral.hyperbolic_index: 24a67b8bf5f72565e2046490ebbaea1729ee885b2be0b0e1c67511be6f279433
  automorphisms.automorphism_group_order: bc5ffa8c258138eb42379858dbf60552a7e89aae454704b61a922fc8464e8f4f
  automorphisms.automorphism_group_generator_morphisms: 23cc0410f10ee5bf0379ea0446f05b6938c6de001fa6d927a9d344a85ab0d668
  integral.primitive_orbits: efdc3acc31dae32efa6733d64e4147d26a756c0f7a5817db6bfcb162e7e66e35
  integral.modular_scale: 7a2634225b5e6675d319ebc4d1729deab4afe5c461b23a75fd12d69403c451c4
  integral.anisotropic_primes: fb25bc127e7307ed02b10aed802223a0f3cec3b5949a94904b89b24699373085
  integral.local_representations: 43543e29a29522aac89ff631d63eeeb628d286a3657c181f8435805c5a06a9d5
  integral.local_densities: 9796f5bf37f8d1fb98ba1cf80009406a24c99625a5e75a02f91469711c41c404
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 0, 0, 0, 1]
- [0, 0, 0, 1, 0]
signature: [4, 1]
determinant: -2
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 0, 0, 0, 1]
- [0, 0, 0, 1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: false
  discriminant_group: [2]
  overlattice_count: 1
  bad_reduction_primes: [2]
  genus_symbol: 'I_{4,1} (2: [1^4 2^1]_3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
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
    densities: [1, 9/8, 1, 9/8, 1, 15/16, 1, 57/64]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7]
indefinite:
  isotropic: true
morphisms:
- target: 3VDW
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3VDW
  name: O(L) generator 2
  matrix:
  - [0, 1, -2, 1, -1]
  - [1, 0, 2, -1, 1]
  - [-1, 1, -1, 1, -1]
  - [-1, 1, -2, 2, -1]
  - [1, -1, 2, -1, 2]
  scale: 1
- target: 3VDW
  name: O(L) generator 3
  matrix:
  - [-3, 0, -4, 4, -2]
  - [0, 1, 0, 0, 0]
  - [-2, 0, -1, 2, -1]
  - [-2, 0, -2, 3, -1]
  - [4, 0, 4, -4, 3]
  scale: 1
- target: 3VDW
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 3VDW
  name: O(L) generator 5
  matrix:
  - [0, -1, 0, 0, 0]
  - [-1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3VDW
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, 0, -2]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [-2, 0, 0, 1, -2]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3VDW
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0002, 0016.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0002, 0016.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0002, 0016.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 0002, 0016.
