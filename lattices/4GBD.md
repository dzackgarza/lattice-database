---
tag: 4GBD
name: Constructed lattice 4GBD
latex: L_{\mathrm{4GBD}}
certifications:
  derive: 3c226a0bf6e1333276360c078f6ae3dd6c8188889c670b69f567067a9139072e
  form.integer_valued: 61d2096a3262444755c8a01cf463f490befcb03f98ff9ef708a18362b81cbf17
  integral.elementary_primes: 1f151351efd09c19b3ab5c5c7ace3a8b83ee34e8868a7ca659e46b3cb9a6feac
  integral.genus_symbol: eed61f25dce8b7f73ef8741bd637cf2885a4e4030c2a1692009c82e2d668a116
  integral.genus_class_count: 4a86227838849553cd9e0134dd861bf3496c2e8f02898407f1a54212c20db3ef
  integral.overlattice_count: e8f750bf57db6a33087b6f356c7877ff71fde54c378bb4db1e1fb1f0fb5e9340
  integral.spinor_genus_count: 350850561b08a629c8a5264d7c9341ee6188bdb18559cf2e7ca1c46ac765d6c6
  integral.spinor_genera: 3d276896662f4c429e1cf4fada7203e4c9ed702795bec871016fa3be6f94169c
  integral.hyperbolic_index: 8d892060bba83129a5913b58942490b0d815eeffb2428133006e507d26786c1a
  automorphisms.automorphism_group_order: 1692b641f4ea01a62e7d114381bfcf4f2bfe946a4c9808180af6c925c13e4026
  automorphisms.automorphism_group_generator_morphisms: 214e850b39c23e6b6b880e04bab5df47d2f7358293d27afcb00f140760c2f38f
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, 2, 0, 0]
- [0, 0, 0, -1]
- [0, 0, -1, 0]
signature: [3, 1]
determinant: -2
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, 1/2, 0, 0]
- [0, 0, 0, -1]
- [0, 0, -1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  discriminant_group: [2]
  overlattice_count: 1
  bad_reduction_primes: [2]
  quadratic_character: -8
  genus_symbol: 'I_{3,1} (2: [1^3 2^1]_2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
indefinite:
  isotropic: true
morphisms:
- target: 4GBD
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 4GBD
  name: O(L) generator 2
  matrix:
  - [-1, -4, -2, -2]
  - [-2, -3, -2, -2]
  - [2, 4, 3, 2]
  - [2, 4, 2, 3]
  scale: 1
- target: 4GBD
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, -1]
  - [0, 2, 1, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 4GBD
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 2]
  - [0, 1, 0, 0]
  - [2, 0, 1, 2]
  - [0, 0, 0, 1]
  scale: 1
- target: 4GBD
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, -2]
  - [0, -1, 0, 0]
  - [2, 0, 1, 2]
  - [0, 0, 0, 1]
  scale: 1
- target: 4GBD
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ICY.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ICY.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ICY.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0002, 3ICY.
