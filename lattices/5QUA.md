---
tag: 5QUA
name: Constructed lattice 5QUA
latex: L_{\mathrm{5QUA}}
certifications:
  derive: ebe4c3af9865612187087d1ba752f9f878bb576b0faa5948f497c6f90a458985
  form.integer_valued: 3ac2e9360f72ffb950d3947ee8c816990d85c0d40ae2ec96f8d23e2763f0be34
  integral.elementary_primes: 698caa33a6d0270cab8e368333b935ae2c2a7b83276cceb509fae5cb4f4713b5
  integral.genus_symbol: b11f2667256772f24b57854b47fd6432b84cf743c21404e264a6b353f4b59d6f
  integral.genus_class_count: 68af539c7020084ba475aac375cd984b86fb0dae1bc7ea31c59f50d0c29262a6
  integral.overlattice_count: 6451569c213096afae974c5b9638369f525ff198160c1f7aeb6728372b71492d
  integral.spinor_genus_count: 5c0e108e9d02f36b0055419ac02ef1763789e3efd48cd08a3c3ee6e7f65ec187
  integral.spinor_genera: 1998c4c6ccd681ddde4c66c9c3c3bfd8ad992e220d5b15989d7025edf54d5f4a
  integral.hyperbolic_index: 8ad09e748d0bb73321e1d97d926d739f679afa37c587c6412cb39cc1476a2a3f
  automorphisms.automorphism_group_generator_morphisms: f8f8c7b89eae7d85382ca601e0747704b2dc293092650b12bfe505c64784e7d4
  integral.discriminant_form: 23c124f0a169c5ef7239c233bf6e0b3f13656032e5a3a6b1dfceed6c75970415
  automorphisms.automorphism_group_order: d08d7ba3c991a46bc425818c39412c2b13a1ca9adf203e650d10a50de768898c
  integral.discriminant_orbits: 4030d394fe9216d9e43453b86fcfab49f4b6897e8060a8da8e2c2eba942dcf77
  integral.modular_scale: 6af679f711e07d3526da42264e76094c2b51de3b051342425c32e2a5e3751883
  integral.anisotropic_primes: 90c7463c6be60facf34616142fbba4894e781d4ff1889351063fe66a0156d435
  integral.local_representations: f7cf46a537a5f393ae8d3cfe598cb561f318f48927258fd60679de4b1d4f9d45
  integral.local_densities: 7e7c9d150b919b7454dbece37cc3e1195aeee11fa6bdd73a398f1ff79994433d
rank: 4
gram_tensor:
- [2, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, 0, 1]
- [0, 0, 1, 0]
signature: [2, 2]
determinant: 4
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, 0, 1]
- [0, 0, 1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  modular_scale: false
  discriminant_group: [2, 2]
  overlattice_count: 2
  delta: 1
  bad_reduction_primes: [2]
  quadratic_character: 1
  genus_symbol: 'II_{2,2} (2: 1^2 [2^2]_0)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
  discriminant_form:
    orthogonal_group_order: 1
    isotropic_classes: 2
    isotropic_orbits: 2
  discriminant_orbits:
    Otilde:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    SOtilde:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    Otilde+:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    SOtilde+:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    O:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    SO:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    O+:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    SO+:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
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
    densities: [0, 2, 0, 3/2, 0, 2, 0, 9/4, 0, 2, 0, 3/2]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 5, O(L) generator 4, O(L) generator 6, 'O(L) generator 7 #2', 'O(L) generator 8 #2', O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12]
indefinite:
  isotropic: true
morphisms:
- target: 5QUA
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 5QUA
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 5QUA
  name: O(L) generator 3
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5QUA
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 1]
  - [0, 1, 0, 1]
  - [-2, 2, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5QUA
  name: O(L) generator 5
  matrix:
  - [1, 0, 1, 0]
  - [0, 1, 1, 0]
  - [0, 0, 1, 0]
  - [-2, 2, 0, 1]
  scale: 1
- target: 5QUA
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 0, -1]
  - [0, 0, -1, 0]
  scale: 1
- target: 5QUA
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 1]
  - [0, 1, 0, -1]
  - [-2, -2, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5QUA
  name: O(L) generator 8
  matrix:
  - [-1, 0, 1, 0]
  - [0, -1, -1, 0]
  - [0, 0, -1, 0]
  - [-2, -2, 0, -1]
  scale: 1
- target: 5QUA
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, -1]
  - [0, 2, 1, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 5QUA
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5QUA
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 5QUA
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5QUA
  name: 'O(L) generator 7 #2'
  matrix:
  - [1, 0, 1, 0]
  - [0, 1, -1, 0]
  - [0, 0, 1, 0]
  - [-2, -2, 0, 1]
  scale: 1
- target: 5QUA
  name: 'O(L) generator 8 #2'
  matrix:
  - [-1, 0, 0, 1]
  - [0, -1, 0, -1]
  - [-2, -2, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 0016.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 0016.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 0016.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ICX, 0016.
