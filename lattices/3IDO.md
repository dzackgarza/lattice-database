---
tag: 3IDO
name: Constructed lattice 3IDO
latex: L_{\mathrm{3IDO}}
certifications:
  derive: 7419042717ce2a51b67fdff2e91dedd4b3735b27074f143ff78a6256fb377502
  form.integer_valued: b3c34f4d12f5f8ffda9d64a94c44f55180b67102a440983fc0152a3ff79b6f35
  integral.elementary_primes: eb11adf60ebe15a7c774ef00e3cb9f8d1dc133d8f8832bb4a9102c7a5f17de30
  integral.genus_symbol: 78e587045e331cd7944c3040a68effa55c26641c2b5fa01e0b20e951c52d602c
  integral.genus_class_count: 4c736c1732df45ad9577ffbad223d4af5bf9cee4718e8aa969f3801d1b7ac184
  integral.overlattice_count: 1e44dacdeba4c9e27287f87d06a6d9df830d56b16a9b521e4f390fbce5661dd3
  integral.spinor_genus_count: 8d30c7f1053e0ec993e6c6bcb1d8d3c1787a535c6c8c7bb8b963d1ac2a5b1058
  integral.spinor_genera: 1930fbb85075088483c1ca796cbdcfda2d8af97eb863fa0ca234bf741f778fdc
  automorphisms.automorphism_group_generator_morphisms: e336f4d8e6e50e05d9c5f9fb1223a8c4c11997c0c7ea51e65d5215d202a7bdb2
  integral.primitive_orbits: d0c7ae8dd5893975b5789dbac1d98177156018b0dd1eca1a345088dc6b2c6fc5
  integral.modular_scale: 2c46b4e37cdd3e8e4fc591647c446dfcf1233320ad5efaa73ca084e7c2688285
  integral.anisotropic_primes: 0e6887093adae4c14e2d60f4b0c53e7d876fdec711a093754d35a6ae1b453341
  integral.local_representations: 538acb2ba35aee716126297e531f712d0f5c3c153d01ccfbed15c9b0e3a56ebe
  integral.local_densities: 68d382433e65fd2e72f8fd23edc43a87a0821691c5b5bccf489fd83fe35b3bf9
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, -2, 3]
- [0, 3, -6]
signature: [1, 2]
determinant: 3
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, -2, -1]
- [0, -1, -2/3]
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
  genus_symbol: 'I_{1,2} (2: [1^-3]_1; 3: 1^2 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  primitive_orbits:
    O:
      constant: 0
      z: []
      w: []
    SO:
      constant: 0
      z: []
      w: []
    Otilde:
      constant: 0
      z: []
      w: []
    SOtilde:
      constant: 0
      z: []
      w: []
    O+:
      constant: 0
      z: []
      w: []
    SO+:
      constant: 0
      z: []
      w: []
    Otilde+:
      constant: 0
      z: []
      w: []
    SOtilde+:
      constant: 0
      z: []
      w: []
  anisotropic_primes: [2, 3]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 0
    - representative: 7
      least_valuation: 0
    - representative: 2
      least_valuation: 1
    - representative: 6
      least_valuation: 1
    - representative: 10
      least_valuation: 1
    - representative: 14
      least_valuation: 1
  - prime: 3
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 2
      least_valuation: 0
    - representative: 3
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [1, 3/2, 3/2, 1/2, 0, 3/2, 3/2, 3/4, 1, 3/2, 3/2, 3/4]
  - prime: 3
    densities: [4/3, 4/3, 2/3, 4/3, 4/3, 0, 4/3, 4/3, 4/9, 4/3, 4/3, 2/3]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: false
morphisms:
- target: 3IDO
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, -1, 1]
  scale: 1
- target: 3IDO
  name: O(L) generator 2
  matrix:
  - [5, -6, 12]
  - [0, 1, 0]
  - [-2, 3, -5]
  scale: 1
- target: 3IDO
  name: O(L) generator 3
  matrix:
  - [3, -4, 6]
  - [2, -3, 6]
  - [0, 0, 1]
  scale: 1
- target: 3IDO
  name: O(L) generator 4
  matrix:
  - [5, -6, 12]
  - [6, -7, 15]
  - [2, -2, 5]
  scale: 1
- target: 3IDO
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID3.
- tag: 3ID3
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID3.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ID3.
