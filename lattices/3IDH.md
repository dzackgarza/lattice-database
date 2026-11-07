---
tag: 3IDH
name: Constructed lattice 3IDH
latex: L_{\mathrm{3IDH}}
certifications:
  derive: d77b2e017ea7ef5e1f47993a77b27fb86a4fff4c3df3be475339e82741e26b42
  form.integer_valued: 3027e539a001ae99ab9204c46f92987397215b9d1bbc6330427d310037f1e502
  integral.elementary_primes: 7cbebc62199d09ceaad245c7788b52874b5bbb161613c955345b366090b1e3d2
  integral.genus_symbol: fe1990a7896f62ae69de88af23b827e9cfb3e0dec6e651184a4c3bbfbe727439
  integral.genus_class_count: 452de551088fccd4541d2b675e84350e6769f8df161768e1419eec8be156416d
  integral.overlattice_count: 8aa133abc2d27670358bed1be4be1056f51998e46568be88ef76231d8712817e
  integral.spinor_genus_count: b11ebe4db24b5a685b528fdffdf9057972dd4baccd0ace591fcde2451849b2f6
  integral.spinor_genera: 6c2cfefa739474af41eb32026fb6dd09a17517745d87ca7154702706cf50f342
  integral.hyperbolic_index: 13cc61f589cbd613fc23779fa77ac38b933d6818a849f3cfb3f82941b2c9edd4
  automorphisms.automorphism_group_generator_morphisms: 8d3ba56631ec061146e69870e37454355e46ce4ba25d21de9cf3b1d40c11ab60
  integral.primitive_orbits: b964fd1ee708e0eebc6ef179ac494b38109e8cbb5955db3f70abe829c8d9c543
  integral.modular_scale: dbdafeb770c7138c6afd08df9e013bd08264e947efe2dde25fd33900661ce8cf
  integral.anisotropic_primes: 8b8dfa84fb0fd62ed053ccc326be119b7eba7e0bf70fe39b2a6a92cee2f63ac5
  integral.local_representations: 155613ceaf9c294210e58a2007f2bb274b8ecab96b9462b3c35720b15fc3405f
  integral.local_densities: d86d1a7b79bcf913536ef16cdfe425266a35dbd2f425bd590ec17eb52eb6c061
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, 0, -1]
- [0, -1, 0]
signature: [2, 1]
determinant: -1
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, 0, -1]
- [0, -1, 0]
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
- target: 3IDH
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IDH
  name: O(L) generator 2
  matrix:
  - [-1, -2, 0]
  - [0, 1, 0]
  - [2, 2, 1]
  scale: 1
- target: 3IDH
  name: O(L) generator 3
  matrix:
  - [1, 0, 2]
  - [2, 1, 2]
  - [0, 0, 1]
  scale: 1
- target: 3IDH
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICY.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICY.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICY.
