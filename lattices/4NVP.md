---
tag: 4NVP
name: Constructed lattice 4NVP
latex: L_{\mathrm{4NVP}}
certifications:
  derive: 964d4433188002d9fa37aec290a908804fe7d3d1971aaace3aaacc9b3ebb1bac
  form.integer_valued: e8bf26194904ebaaa2de7127882eaaecf705537a9f80b8312e3cddec0b6ff5f9
  integral.elementary_primes: e0acb9ab94a5d1e862de956d9a5f4ad7616b5e4a31518daa3b3bcefec09aede5
  integral.genus_symbol: 33506fb94e3b633f031032b9c61280b16477456c06323fb8ff7b274600ede591
  integral.genus_class_count: 0cf3be44dd24f962bad0546c01126c1f2271c1f55e34ce3ba732fd49d43e6260
  integral.overlattice_count: 5fd50685c5dd9b085170dc0b1046114f85c6e0402f392bae0476a4c18d4df927
  integral.spinor_genus_count: 96d7ace3c69a5f8a8597c856fcd078ef0ced8227c41cb1ca29f02a0314503160
  integral.spinor_genera: 61585d22b570a998587a490fde334067a4b03112a070485f7d74da40619e7e00
  integral.hyperbolic_index: 3b303afd65f033269fc49af6726739900bee25c7d824f0d73561d8663852ec9f
  automorphisms.automorphism_group_order: dbac3c82f9d49ea4c01ce52f3fa5e1ab6be675956c0309c0f6c86ce0d373e68c
  automorphisms.automorphism_group_generator_morphisms: 2fa80bbf89f47be9b4825a2e2d6f7a3704bfe32e2f233adace47bf84ec656572
  integral.primitive_orbits: 3f3ec13bb38ad91ba8b6fb61792a6aea1026fe7fa31087b67ea66295a0a1bf52
  integral.modular_scale: a0a7aa9cc970a109a9796889d299d3b327e2fe36d3ef0717508784cde0957b7e
  integral.anisotropic_primes: d4d9979caa2130300e1a5c60509cba0dc4b32329d3f929ee23a677da8d085c90
  integral.local_representations: 226a74011896dfed340adb7325045bb4ba1bd26229c7f0da97ed84d4f58d4e9b
  integral.local_densities: e87fa540abba39f53ad97600b794c353d3564b4bb4f2b51cd27ef99a3ee262e3
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 0, 2, -1]
- [0, 0, 0, -1, 2]
signature: [4, 1]
determinant: -3
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 0, 2/3, 1/3]
- [0, 0, 0, 1/3, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [3]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{4,1} (2: [1^-5]_1; 3: 1^4 3^-1)'
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
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [7/8, 5/4, 5/4, 47/64, 5/8, 5/4, 5/4, 25/32]
  - prime: 3
    densities: [8/9, 8/9, 32/27, 8/9, 8/9, 34/27, 8/9, 8/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7]
indefinite:
  isotropic: true
morphisms:
- target: 4NVP
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4NVP
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NVP
  name: O(L) generator 3
  matrix:
  - [-1, -2, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [2, 2, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NVP
  name: O(L) generator 4
  matrix:
  - [-3, -2, -4, -2, -2]
  - [4, 3, 4, 2, 2]
  - [2, 1, 3, 1, 1]
  - [-2, -1, -2, 0, -1]
  - [-2, -1, -2, -1, 0]
  scale: 1
- target: 4NVP
  name: O(L) generator 5
  matrix:
  - [1, 2, 2, 4, -2]
  - [2, 3, 2, 4, -2]
  - [2, 2, 3, 4, -2]
  - [-2, -2, -2, -3, 2]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NVP
  name: O(L) generator 6
  matrix:
  - [-1, 0, -2, 0, 0]
  - [2, 1, 2, 0, 0]
  - [2, 1, 3, 2, -1]
  - [-2, -1, -2, -1, 0]
  - [-2, -1, -2, -1, 1]
  scale: 1
- target: 4NVP
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
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICY, 0012.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICY, 0012.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICY, 0012.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICY, 0012.
