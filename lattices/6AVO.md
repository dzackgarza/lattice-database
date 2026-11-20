---
tag: 6AVO
name: Constructed lattice 6AVO
latex: L_{\mathrm{6AVO}}
certifications:
  derive: 8c8e57f0ce81c65590dbc8132becb835a8386803444854fb9a5516dd0f194d31
  form.integer_valued: 439b48779382433df2f1e92613544ca9c9102b95aea6ae981d96a8c636ba8e5d
  integral.elementary_primes: 410570e665297758cd8d38252998efa8bef671685a3558de8e8bf9b83e9f7c57
  integral.genus_symbol: 890fe847e89149e6bb3b487b70b8ac8ca46913f6393afad6e904e6393111d8c7
  integral.genus_class_count: 0e6a54d6cb6fc1bcff856f42422873241b2f728edd23747ca26d5a0056b7b0fd
  integral.overlattice_count: 6c633d667972d51200272ddb836cb7a6ffffa0d9144bc5e5d2c6b3538528757f
  integral.spinor_genus_count: b3880cc4c2eca30eae167b28040db22e9108bc25dfbf6e13f951053eee685f3a
  integral.spinor_genera: 41016160dedc7eab39502fb4d289b97b5acd991d4aa7d22d405c28fe6143ce83
  integral.hyperbolic_index: 7794b54ac57a8f7bd84f9272c3bc275ea3847b914f357a575d89e0f3faad3829
  automorphisms.automorphism_group_generator_morphisms: 9d3c4c738573924ae33288bcc9badf805d9615b55755e1a7db3cedeca434de9e
  integral.discriminant_form: 9ff747da6aac3195fb7de6932b132bd2115d15b80b20dc6d389442eb185bf9c2
  automorphisms.automorphism_group_order: 1f6352ab879da4875c8f9531878b98b582fdd8bb64e7d8eb829709369cb759d6
  integral.discriminant_orbits: e0f64b826cf979c8f669f3015bb3c39f64de1c087925fd58abbc95a3409264b4
  integral.modular_scale: 51f85c986b51dd2e88d87138a089fc0d685e4fb96be03e6e571b8f9c3603e291
  integral.anisotropic_primes: 510156fad36ac4a87d86665565b119bcad9c84a1f6d5d3b5452e89c1beab6d63
  integral.local_representations: 4c0b419a945ddfcaae3b311c123530fa0d4d7c4878edd7e234b4daa604f29e58
  integral.local_densities: 13992894e96631d951af2a35a8f114943527861770a84729680dded46ce1a018
rank: 4
gram_tensor:
- [0, -1, 0, 0]
- [-1, 0, 0, 0]
- [0, 0, -2, 1]
- [0, 0, 1, -2]
signature: [1, 3]
determinant: -3
definiteness: indefinite
dual_gram_tensor:
- [0, -1, 0, 0]
- [-1, 0, 0, 0]
- [0, 0, -2/3, -1/3]
- [0, 0, -1/3, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: even
  level: 3
  modular_scale: false
  discriminant_group: [3]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{1,3} (2: 1^-4; 3: 1^-3 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
  discriminant_form:
    orthogonal_group_order: 2
    isotropic_classes: 1
    isotropic_orbits: 1
  discriminant_orbits:
    Otilde:
      constant: 1
      z: [0, 1, 0, 1]
      w: [0, 1, 0, 1]
    SOtilde:
      constant: 1
      z: [0, 1, 0, 1]
      w: [0, 1, 0, 1]
    Otilde+:
      constant: 1
      z: [0, 1, 0, 1]
      w: [0, 1, 0, 1]
    SOtilde+:
      constant: 1
      z: [0, 1, 0, 1]
      w: [0, 1, 0, 1]
    O:
      constant: 1
      z: [0, 1, 0, 1]
      w: [0, 1, 0, 1]
    SO:
      constant: 1
      z: [0, 1, 0, 1]
      w: [0, 1, 0, 1]
    O+:
      constant: 1
      z: [0, 1, 0, 1]
      w: [0, 1, 0, 1]
    SO+:
      constant: 1
      z: [0, 1, 0, 1]
      w: [0, 1, 0, 1]
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 3
      least_valuation: 2
    - representative: 5
      least_valuation: 2
    - representative: 7
      least_valuation: 2
    - representative: 2
      least_valuation: 1
    - representative: 6
      least_valuation: 1
    - representative: 10
      least_valuation: 1
    - representative: 14
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [0, 5/2, 0, 5/4, 0, 5/2, 0, 15/8, 0, 5/2, 0, 5/4]
  - prime: 3
    densities: [4/3, 2/3, 10/9, 4/3, 2/3, 8/9, 4/3, 2/3, 28/27, 4/3, 2/3, 10/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 6AVO
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, -1]
  scale: 1
- target: 6AVO
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [-1, 1, 2, -1]
  - [1, 0, -1, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 6AVO
  name: O(L) generator 3
  matrix:
  - [1, -1, -2, 1]
  - [0, 1, 0, 0]
  - [0, -1, -1, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 6AVO
  name: O(L) generator 4
  matrix:
  - [0, -1, 0, 0]
  - [-1, 1, -1, 2]
  - [0, -1, 1, -1]
  - [0, -1, 0, -1]
  scale: 1
- target: 6AVO
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ID0.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ID0.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICY, 3ID0.
