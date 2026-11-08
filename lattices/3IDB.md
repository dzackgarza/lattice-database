---
tag: 3IDB
name: Constructed lattice 3IDB
latex: L_{\mathrm{3IDB}}
certifications:
  derive: ab9abb1f599938ba04742f705ba02be0e57aae0f13dcedc9780f12c85a5d4000
  form.integer_valued: 4b2484f760945a857e30ff15f7ac29fc3ffe628de8fd00e3de4c099b0bb7650e
  integral.elementary_primes: ea5c0c8e8110b94d6ab0ec81df8e95676306dc0d32d49d7a482dea08a7a05a75
  integral.genus_symbol: 926aae2c1b16004a5c0ee1e59065bb3dfbfb001a4f8415861cd1087641108c4a
  integral.genus_class_count: cd10e1b27228c5a3334153e9e0a67020fbdf3d0d8245ed02b0b95d84051596d6
  integral.overlattice_count: cf394e00ed51bc61db5fceef3784b570a78e11c7387710320da6239be288f9d8
  integral.spinor_genus_count: 114afba7a378129f846735b3199ec3d3d5fcc2f9daf387b537bf4afc87c83c17
  integral.spinor_genera: 5dd8ea7041ed39d211f1ad48cee46071c562ee6d74a6db8e4b313fa1f6078de8
  automorphisms.automorphism_group_generator_morphisms: 246cceb34800e5caa048e182967e9c720afbe56c0ec93afcd9c37e9e8d794e68
  integral.primitive_orbits: 1b828319a6e748256523e565f3a0b3354105b3bc10f1fb7bd0d0a8239141dc3d
  integral.modular_scale: d9795a08156d39373ca376eb3a4c16c8843f19732acd8dfdc4a41ef178389a6c
  integral.anisotropic_primes: 9270bd18e5a489f4a0f161031ec5119ad36554589f8b9144923d60df1d1703bb
  integral.local_representations: 1caec72832667ba0682838c52577405c4ae662410c39e0777aac00c389640c78
  integral.local_densities: eeafaa42bce6e3023a6e33e6bdc6a6c15380f58be48fa285b1369b43494309e9
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, 1, 0]
- [0, 0, -2]
signature: [2, 1]
determinant: -2
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, 1, 0]
- [0, 0, -1/2]
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
- target: 3IDB
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IDB
  name: O(L) generator 2
  matrix:
  - [-8, -3, -12]
  - [-3, 0, -4]
  - [6, 2, 9]
  scale: 1
- target: 3IDB
  name: O(L) generator 3
  matrix:
  - [0, 1, 0]
  - [-3, 0, -4]
  - [2, 0, 3]
  scale: 1
- target: 3IDB
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 3ICX.
