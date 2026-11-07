---
tag: 3IDG
name: Constructed lattice 3IDG
latex: L_{\mathrm{3IDG}}
certifications:
  derive: 6914b8c9d001a316c0021f6ca6449f40134151c5db53a95789aedfeb50dc9f49
  form.integer_valued: d46d63f9ce6d9915fda1fe44497ef3bae941bd2961cf5b995040373a48456cc8
  integral.elementary_primes: 7743df9a671857e36d2f186c3f669a086a2ce85319a10c603104187bcbefeaac
  integral.genus_symbol: 8f333d312f5539e1cf09e7f9bf6514a6b6f91cd2e5c4eba4dab0b94e8d23bea1
  integral.genus_class_count: 69dea83ce0b31442ddec5209f46b41f164b5545e23cc086727ef65e5f1014a2f
  integral.overlattice_count: 377141f6d62dc60f84b37930a3fe16b76491f17eeb6a69d25af23729e57bba7c
  integral.spinor_genus_count: 598dc92c2acc3416aecfe43cccc6c8803c55352dbe4964f3037bf8b7bed3257b
  integral.spinor_genera: 2d7171210fd812f2e78899931f5d87d4d53c18d4f58a957be27e446246e03a66
  integral.hyperbolic_index: 2025ba40cf673fbd974165f702cb8ddfb4f4ea0ce048687344026c095a9369dd
  automorphisms.automorphism_group_generator_morphisms: 34c9daf96ddef576badadd8acb25052591da88a13a06956ab6dfed3f04dd2f22
  integral.primitive_orbits: 3c7f4a590e26d31b0ee4910b973d5f7adeacfaa188aa49a41c251dc5c9f05335
  integral.modular_scale: e15601dcef48b84f123dd30c8747f008a3e7eb1f33cb479eec74780b6320cbc6
  integral.anisotropic_primes: d997de22acbd782a95f22e982939e02fbc75c3057f99bdc9406096c35bae86cd
  integral.local_representations: d47f369ae2419424e0e8d8737aaab054f7e1c6d4cea513b68e7ceac55961dea3
  integral.local_densities: 483155ae6eb436759fe251a63438a607b98bfc3abb3553689d72d216deb1de14
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, 0, 1]
- [0, 1, 0]
signature: [2, 1]
determinant: -1
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, 0, 1]
- [0, 1, 0]
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
  genus_symbol: I_{2,1}
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
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
      constant: 1
      z: []
      w: []
    SOtilde:
      constant: 1
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
    densities: [2, 1/2, 1/2, 2, 1, 1/2, 1/2, 5/4, 2, 1/2, 1/2, 5/4]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IDG
  name: O(L) generator 1
  matrix:
  - [-1, 2, 0]
  - [0, 1, 0]
  - [2, -2, 1]
  scale: 1
- target: 3IDG
  name: O(L) generator 2
  matrix:
  - [-3, 2, -2]
  - [-2, 2, -1]
  - [2, -1, 2]
  scale: 1
- target: 3IDG
  name: O(L) generator 3
  matrix:
  - [1, 0, 2]
  - [-2, 1, -2]
  - [0, 0, 1]
  scale: 1
- target: 3IDG
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0016.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0001, 0016.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0016.
