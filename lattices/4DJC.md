---
tag: 4DJC
name: Constructed lattice 4DJC
latex: L_{\mathrm{4DJC}}
certifications:
  derive: 253691cc2145111540ee2907683091885b0df84d94cf19f822a8d8fdad5b7a6f
  form.integer_valued: 956ff244ce7349d17cd2c97266b416ca0bdf1ea83420b12eb00753692b1f5009
  integral.elementary_primes: f1752819c954c3f9a1a5826950dd7b5d37a9a59b1a22a85ed76475ae62b7ed51
  integral.genus_symbol: 5083807b678f13153eb364c62602de93392f21cedc0400166b1dd49cae956feb
  integral.genus_class_count: d059dd7699931986ec0c3ac5a96754622a7694033f93058f711a8f9a23c734d5
  integral.overlattice_count: 63e76c6f61653a5ba632d90f9d44747fb4767835615ae23bac3c5f65e1860893
  integral.spinor_genus_count: e054475e7cfad62af1fcd7604dbb331a78682cfa9193084b740db159da4d7704
  integral.spinor_genera: 733e3d46f645085f8f25570824482209674c540ddd475c78f62619dc56ad455f
  integral.hyperbolic_index: 3133403825e4a704433cde47879af8062fc93595d1aa4670fee65571f81666b5
  automorphisms.automorphism_group_order: d928300645249bbdde8ae5064f9f653a3ee4f172fd00a6849c56d0b17c71d48a
  automorphisms.automorphism_group_generator_morphisms: fccbb1ec17dbf1edcbef7fed5abae14e4c4f76051002c55947b2d45f74c863ac
  integral.primitive_orbits: 691c86c0d4c922c177ef5205f6c9acc35e3c156708bd199da5bc2eb303f8acbc
  integral.modular_scale: 5f6e00c802d18377b2caf21102a7ac7fa85544dfd6641ed0e7153b4764aa27de
  integral.anisotropic_primes: 4798e1033dbaf73c0c37216b5054f922dcafc905845d4fb0579b409baf6713cf
  integral.local_representations: 507a77fc6b8e7b62ae596ddc953536ffcddb9f1dca99d4071d35dc747ca2da93
  integral.local_densities: a1ee93151bdd30354e3c7e0571356f55fbe342e0128222a914f027f21fba66cd
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 0, 0, 0, -1]
- [0, 0, 0, -1, 0]
signature: [4, 1]
determinant: -4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 0, 0, 0, -1]
- [0, 0, 0, -1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: false
  discriminant_group: [2, 2]
  overlattice_count: 2
  bad_reduction_primes: [2]
  genus_symbol: 'I_{4,1} (2: [1^3 2^2]_3)'
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
    Otilde:
      constant: 2
      z: []
      w: []
    Otilde+:
      constant: 2
      z: []
      w: []
    SOtilde:
      constant: 2
      z: []
      w: []
    SOtilde+:
      constant: 2
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1, 1, 5/4, 17/16, 1, 1, 3/4, 17/16]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
indefinite:
  isotropic: true
morphisms:
- target: 4DJC
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-2, 0, 0, 1, 2]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DJC
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 1]
  - [0, 0, 1, 0, 0]
  - [0, -2, 0, 1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DJC
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 4DJC
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DJC
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DJC
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 3ICY.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 3ICY.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 3ICY.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0002, 0002, 3ICY.
