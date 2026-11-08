---
tag: 3IDC
name: Constructed lattice 3IDC
latex: L_{\mathrm{3IDC}}
certifications:
  derive: 814ad7312fce7fe79c256ab8aec843cded1d778dd3058d4f97b3a9a3f6ee81b4
  form.integer_valued: 25c1396b745d8c6dbbfd93d11763e8aaea334d1e8c2d08f2b7b592c55e485182
  integral.elementary_primes: f332aed431480d83fa39b17a133a361d9010ddff0331c2e41d9d76b302652c5e
  integral.genus_symbol: d2e37376f6ad223134e0d3fafbc1bbf30d57ef740d2f61296b269190db3df599
  integral.genus_class_count: 78ae542206bc79d8c2dbd3beae60b14f7986d580f8ae470fb5db8eec75d50123
  integral.overlattice_count: bae6731d44046c494950b073ff3c087c0020a8f2887bfc614b5cc1f9e7b27ab5
  integral.spinor_genus_count: 8e388d58992cefbb764442aedef4c42aa577506d6a9f673217fe6b51c26c8f3b
  integral.spinor_genera: 1817c03c3ca61604f037d55e833a1b0818699dad4d9ba81d7c31a2e17a86aeb3
  automorphisms.automorphism_group_generator_morphisms: 401e5ea3a3ed8b4b24d718d91cc6ecfa01a607d2c9bb3a7af78ea29e665dfb1b
  integral.primitive_orbits: fdcd5e4c4813df4fc63b84c9e440e3853fc5537d1486dfc2d63304b0632bd00f
  integral.modular_scale: 3488813a1da19595b2f652bc1fc90cba55bb9560dd9ba1be919ebe012d4f5ba6
  integral.anisotropic_primes: 19bd49be17c901046bfc98ff682af88c4b820bb338af9d7e6d7dc863c542493c
  integral.local_representations: 7b94b33a417f38b09fd8aadb3f7187150bfec53c0ae21614866f75a3d09e253a
  integral.local_densities: d3e0dbd9f27f3792a081f926c875d60101aeb145d8fa72886317adef2a027dba
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, -1, 0]
- [0, 0, 2]
signature: [2, 1]
determinant: -2
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, -1, 0]
- [0, 0, 1/2]
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
  genus_symbol: 'I_{2,1} (2: [1^2 2^1]_1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
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
    densities: [1, 2, 1, 1/2, 1, 1/2, 1, 2, 1, 1, 1, 1/2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IDC
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, 1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IDC
  name: O(L) generator 2
  matrix:
  - [0, 1, 2]
  - [-1, 2, 2]
  - [1, -1, -1]
  scale: 1
- target: 3IDC
  name: O(L) generator 3
  matrix:
  - [-3, 4, 4]
  - [-4, 5, 4]
  - [2, -2, -1]
  scale: 1
- target: 3IDC
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 0002.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 0002.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 0002.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICW, 0002.
