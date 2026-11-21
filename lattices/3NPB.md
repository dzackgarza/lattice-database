---
tag: 3NPB
name: Constructed lattice 3NPB
latex: L_{\mathrm{3NPB}}
certifications:
  derive: 01628326d83be3d6cdde12b878963fc36e8cf549e95d299b33fae7a149d3ab4d
  form.integer_valued: 46a3ef2ed193d50472fdd0ccf442115ff06c8a5bd43515141ed7e6fdd35f35e8
  integral.elementary_primes: 5740a91140ebde7ac8a08c98532c72431e13d645902d147ff2290d0d65de5ebc
  integral.genus_symbol: 013e5e6d8eb9f80c1c15c29b7b39112cfeb60bf52cd60edb52c734df5605d427
  integral.genus_class_count: 1613e47b7c9b35ffb084ff229d0e0db00854c0c8bddd2316c782bf7f441e1431
  integral.overlattice_count: a8084fe664d969597491cba7137b3e71a2a6666496327be865dcf7001bdc54f7
  integral.spinor_genus_count: 0d7bd2dffac0c842ab1919bc35feb3301eab29389134d0865041f11ed78c7461
  integral.spinor_genera: 610f7dc5db85cc91da5afac79fa9dff92742e0c8f26f50cfcf2156442a8acaef
  automorphisms.automorphism_group_order: 9a801e9e79f663c2739e820f362bb08626fdfcdf7610f73efc706a8f4b595738
  automorphisms.automorphism_group_generator_morphisms: 2de089ae1225f0d340b5dcc903f31c19cf704bf98522d3c066003c8d9984b432
  integral.primitive_orbits: c2eeca745ba34d4bfe29f5103c58692e6328b43410cefaf6bc71d020a5aac657
  integral.modular_scale: de442b036244b98dec005db2cf73153e0051a2f490d80812bee7a43fb1bab459
  integral.anisotropic_primes: 6271a2dff5cbdb58aeb31e1c38bc96be0033ee4ef0bc45279adf36e2a4ff4f54
  integral.local_representations: b08e79df34df46b4b4591d209869cbb08c2807e79005552546d308a012685018
  integral.local_densities: bcfed207bbb61f5583d89e9c0122dac8dd31caccea73a72253c9cb9a5b4e1334
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, 1, 0, 0]
- [0, 0, 1, 0]
- [0, 0, 0, -2]
signature: [3, 1]
determinant: -2
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, 1, 0, 0]
- [0, 0, 1, 0]
- [0, 0, 0, -1/2]
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
  quadratic_character: -8
  genus_symbol: 'I_{3,1} (2: [1^3 2^1]_2)'
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
    densities: [5/4, 9/8, 5/4, 17/16, 3/4, 9/8, 3/4, 33/32, 5/4, 7/8, 5/4, 17/16]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7]
indefinite:
  isotropic: true
morphisms:
- target: 3NPB
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3NPB
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3NPB
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3NPB
  name: O(L) generator 4
  matrix:
  - [-8, 0, -3, -12]
  - [0, 1, 0, 0]
  - [-3, 0, 0, -4]
  - [6, 0, 2, 9]
  scale: 1
- target: 3NPB
  name: O(L) generator 5
  matrix:
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [-3, 0, 0, -4]
  - [2, 0, 0, 3]
  scale: 1
- target: 3NPB
  name: O(L) generator 6
  matrix:
  - [-10, 5, 2, -16]
  - [5, -2, -2, 8]
  - [2, -2, -1, 4]
  - [8, -4, -2, 13]
  scale: 1
- target: 3NPB
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0001, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0001, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 0001, 3ICX.
