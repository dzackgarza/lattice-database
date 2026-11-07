---
tag: 3IDE
name: Constructed lattice 3IDE
latex: L_{\mathrm{3IDE}}
certifications:
  derive: 628680186e97c44b13a9fb37c53d6095ea112d29aebdc580b9e1e258cb2717fa
  form.integer_valued: 91caa1f48bfa953d85ca47740a70f6cbbef3b423e2c9d10a70fc182ce8b31f82
  integral.elementary_primes: efa03e62221258b6a8e2ff3f6195190f6112786c612735e569767656319d8388
  integral.genus_symbol: 75b3521f207c9317feb2504232ea78fc4a996aac25de78af24fd1c7d1795ce27
  integral.genus_class_count: a2f843e64427125e64fdccc487876f002ca7c3d016b770e97de3b520c5f6b7d7
  integral.overlattice_count: 970b04cdd06e9cba60ecf59db236241ee53b0fd344c5786ff2e8114437009492
  integral.spinor_genus_count: 129fab5e3a8516a0f4cf8e6993ef4073c499cd528bb9903b1a387ea82b128de4
  integral.spinor_genera: abc36bde59a694d99db792e56bd1f76555597d7350f13be4ba5f092ff17454e2
  integral.hyperbolic_index: c7447e4afc38c4069e25b6c954771c0eb31f6f6d4fb9a8e11c04e23bc4efeba8
  automorphisms.automorphism_group_generator_morphisms: e0b21448a2a838461ad4f388940f5c8d02fc42b6954b93d0fcc3cf18defd8381
  integral.primitive_orbits: c741df13f4ca6d4ea56aaf0a66015af774c83541a50934b75b90ed65af9bcdb6
  integral.modular_scale: 62d630cdc9b894ab26b5adeec173c4ce7982efd9b77e87ca6239b81fde999867
  integral.anisotropic_primes: 491d09f650f853d52963d59aa0ee381a665ac77006800798cf251ff185c93c46
  integral.local_representations: 41ef6b905bf5038a5d5644809fb2e48b83cd050e7a1861cda6a5e1ee9d573cda
  integral.local_densities: 902fe242ad92db3728848d686ea669e98510fac6686ce99e5cff8e1c06ff3759
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, 2, 0]
- [0, 0, -2]
signature: [2, 1]
determinant: -4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, 1/2, 0]
- [0, 0, -1/2]
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
  genus_symbol: 'I_{2,1} (2: [1^1 2^2]_1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
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
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 0
    - representative: 5
      least_valuation: 2
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
  local_densities:
  - prime: 2
    densities: [2, 1, 1, 2, 0, 1, 1, 1/2, 2, 1, 1, 1/2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IDE
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IDE
  name: O(L) generator 2
  matrix:
  - [-17, 0, -24]
  - [0, 1, 0]
  - [12, 0, 17]
  scale: 1
- target: 3IDE
  name: O(L) generator 3
  matrix:
  - [-7, 2, -10]
  - [5, 0, 7]
  - [7, -1, 10]
  scale: 1
- target: 3IDE
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ICX.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0002, 3ICX.
