---
tag: 3IEJ
name: Constructed lattice 3IEJ
latex: L_{\mathrm{3IEJ}}
certifications:
  derive: 882d0bafe5f1b2dec0ab6c1795a79b5289e0957e5165366898792e34a1f0382f
  form.integer_valued: 573f6da10530c899bbb0d180d9f72daa89bbf6343a1b2c7dc5a3ac9fbcdf99fc
  integral.elementary_primes: 50b9b217f94a9e6780ff3632963528c7b0fbe7a7c8adbe34bd9bab4880fa42e8
  integral.genus_symbol: f420c194b78c1074cfba1f34d80655914396d4a93501f9c708200d8df4dc23a6
  integral.genus_class_count: 81b3eaaed3d346cd99a10f24a46e7b3fdbfc57850b72ed8cd755465196a33042
  integral.overlattice_count: da71d63b5eca9fae9114f2ca973a794e4d77a2807a617beee97c10e95ed70671
  integral.spinor_genus_count: 4037707fa6a85e033a3462c6b2c281d42e137c39072bcfa06896a174cf333d67
  integral.spinor_genera: ba103a0a74d7759f9ae7fd454dd9d1e329102f733068d980936d86fea9183bb1
  integral.hyperbolic_index: 6e1d18eec564990501e51c6ec400ee16304ea36d793de4d462697f21a43749b7
  automorphisms.automorphism_group_generator_morphisms: 5dbaf1330507003a18604e3474dfb6151d58715ac07aa576b2963ae106dc0c5f
  integral.discriminant_form: d016dc9ab51e5c0af7af5ce0dd242d6b2ad0d00013e0d6fd2d3e58fd88ebd5a4
  integral.primitive_orbits: b21a13db3b3e6c6529766a0911346ab4cdbf7cf7be563f18e48534cacee727e0
  integral.modular_scale: a5b592613ea803ffb388c58c7f42db09a48a804e93d921e375c566a4f7fbc2f3
  integral.anisotropic_primes: 697fe523381133bf5a9009cf7f8a74a273ff228fc6094e11bd091b060efb6abb
  integral.local_representations: 662467d38d97974cdab74a44e0cded27b955ee163c50b963a62c58c140837f3a
  integral.local_densities: 5c173fc11569d53f055909e7f560810d6f7baddc62638c0acda496b014f27281
rank: 3
gram_tensor:
- [2, 0, 0]
- [0, -2, 1]
- [0, 1, -2]
signature: [1, 2]
determinant: 6
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0]
- [0, -2/3, -1/3]
- [0, -1/3, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  modular_scale: false
  discriminant_group: [6]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'II_{1,2} (2: 1^-2 [2^1]_1; 3: 1^-2 3^1)'
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
      constant: 2
      z: []
      w: []
  discriminant_form:
    orthogonal_group_order: 2
    isotropic_classes: 1
    isotropic_orbits: 1
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
    densities: [0, 2, 0, 3/2, 0, 3/2, 0, 5/2, 0, 3, 0, 3/2]
  - prime: 3
    densities: [2/3, 2/3, 2, 2/3, 2/3, 4/3, 2/3, 2/3, 14/9, 2/3, 2/3, 2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
indefinite:
  isotropic: true
morphisms:
- target: 3IEJ
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, -1, 1]
  - [0, 0, 1]
  scale: 1
- target: 3IEJ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 1, -1]
  scale: 1
- target: 3IEJ
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3IEJ
  name: O(L) generator 4
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IEJ
  name: O(L) generator 5
  matrix:
  - [7, 6, 0]
  - [8, 7, 0]
  - [4, 3, 1]
  scale: 1
- target: 3IEJ
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID0.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID0.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ID0.
