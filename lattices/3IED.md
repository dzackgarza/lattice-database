---
tag: 3IED
name: Constructed lattice 3IED
latex: L_{\mathrm{3IED}}
certifications:
  derive: fbfbcb973f1d653bef018a75c2e3f9489018b67d6d76b1964323829adb14eb2e
  form.integer_valued: 168c50fdca4412df263590749b62c62d4ebae8a30c95e37bbc1b7df6788ac1da
  integral.elementary_primes: 77f9173a17a51cb016b14403dbb5071c6f6677b1cb9082bd2dcd49ace0ddfba0
  integral.genus_symbol: 773a26b9120885c5efda48f246c8ea18db59e474866a30acdd1c44e1c4e6133a
  integral.genus_class_count: f4d693946180da94f189b71724e2265dabbb1de6400141b7694de914a660eda9
  integral.overlattice_count: 612c8c4f821cbe88fda0a9458b07942dc41ccb0142d62cfd33b5b031aa880eca
  integral.spinor_genus_count: f187b059dc3f543b423ceb82618ef4b7a0cf9557d257776bdba0f8c5a3b2fc3b
  integral.spinor_genera: 9e3f7091f1c9100e02337503723468880fb4f1e3720e88875b6b9bbcaa6100bf
  integral.hyperbolic_index: 11a7f03525a057d21beaeeb5e8b3f7cbc9e491ddf6172ca0e19626c53962613b
  automorphisms.automorphism_group_generator_morphisms: 0ba70993409672786fb1bc7da6897e51b3f2d4b903fc60ff71d54e328454e32f
  integral.discriminant_form: 7a1a7b49badef4a9de1fcd84e5c92ab3e614e40a8ff07d689532ad76b05ca0c7
  integral.primitive_orbits: e24daabecde03a7c57fad10660a00b1304cee1b30b69ced7c8b1cc30555bbc47
  integral.modular_scale: 782bdddc725ffe9cd121481a858e3a4eb92fa583854531067062c8c8dfee8638
  integral.anisotropic_primes: 7d22eee1c277b60c59823bfafb78b0da0ffd9245dea428dfe63813ea151456d4
  integral.local_representations: ce3b3ddcb4a3c5ea85d7002411d2ace7d9182addae7cc7e4df16ca54b82c6a6a
  integral.local_densities: 3660f407f314f4f86a9cd9e4cbe81cc59b6e34d80e081f5b294575c94b8f1c46
rank: 3
gram_tensor:
- [2, 0, 0]
- [0, 2, 0]
- [0, 0, -2]
signature: [2, 1]
determinant: -8
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0]
- [0, 1/2, 0]
- [0, 0, -1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  modular_scale: 4
  discriminant_group: [2, 2, 2]
  overlattice_count: 4
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{2,1} (2: [2^3]_1)'
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
      constant: 2
      z: []
      w: []
    SOtilde:
      constant: 2
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
      constant: 2
      z: []
      w: []
    SOtilde+:
      constant: 2
      z: []
      w: []
  discriminant_form:
    orthogonal_group_order: 2
    isotropic_classes: 3
    isotropic_orbits: 2
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
    densities: [0, 4, 0, 1, 0, 1, 0, 4, 0, 2, 0, 1]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 3IED
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, 1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IED
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IED
  name: O(L) generator 3
  matrix:
  - [0, 1, 0]
  - [1, 0, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IED
  name: O(L) generator 4
  matrix:
  - [-2, 1, 2]
  - [-1, 2, 2]
  - [-2, 2, 3]
  scale: 1
- target: 3IED
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0002, 3ICX.
