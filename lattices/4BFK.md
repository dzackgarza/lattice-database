---
tag: 4BFK
name: Constructed lattice 4BFK
latex: L_{\mathrm{4BFK}}
certifications:
  derive: dbd441cc7cae807d58660f828227a69f16b4f03f6117bc9bb35d1b0235b9a362
  form.integer_valued: 8e33afe5f3121a16fb73775c6bab8e19244a772db00f81a5f8aa5857ab24a37a
  integral.elementary_primes: e35e303c5f34ffa0b606e89b410d6fb281b82dc99afbe0c645012bc298b086f5
  integral.genus_symbol: 9a4c28ecfb1810109e4ae1c6f77820cedcfb9a9e868a52a503ebe4e47d518d34
  integral.genus_class_count: 144b2c183c5ab02e0a87b174c059272a534754f0a84c65025dabc4d1637c4228
  integral.overlattice_count: 678045221f86aae7354e2ff03ed13bf73735c1dce08631a2219f7f6ac79f2a69
  integral.spinor_genus_count: 453144783d5b2011b386ccc13ed088951b2a1abdd17f8aa3e42e85d7ef06510b
  integral.spinor_genera: bc66cdfb90681440e31fc477a1696589099f9614e3e524efe1920239e656a774
  automorphisms.automorphism_group_order: c8c59e5c81f2d91f80d9137894ee4facd806ffb1b21c2902a35b1b9b17754b77
  automorphisms.automorphism_group_generator_morphisms: ea609d2ecc639dcbaacaf51c9c1b5cb0f8653d07d20330b6adc916d0dd69514f
  integral.primitive_orbits: 0fe64b0b455b0e50dee348656e7363aebb34c2dcacdf80fb972b9acdb0a93dd3
  integral.modular_scale: 9060975e786a4b0c36163b69fe9d0e895e408142d66d0bd5003265f6fbb622ae
  integral.anisotropic_primes: 7fa3b99fd544aa8a46e0dd178518ed500538f557ab2f8d504edb2ebbde8ea5e1
  integral.local_representations: ddd7a645e5ecb713a0d61af776c82eed011cd55c59c0a46488cc93abfd0f5465
  integral.local_densities: fc058e810ec3ca2cb681f330cc9f185df75e0adcb2506514716f9fac60294f04
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, -1, 0, 0]
- [0, 0, 4, -6]
- [0, 0, -6, 12]
signature: [3, 1]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, -1, 0, 0]
- [0, 0, 1, 1/2]
- [0, 0, 1/2, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'I_{3,1} (2: [1^-2]_4 2^2; 3: 1^-3 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  primitive_orbits:
    O:
      constant: 2
      z: []
      w: []
    O+:
      constant: 2
      z: []
      w: []
    SO:
      constant: 2
      z: []
      w: []
    SO+:
      constant: 2
      z: []
      w: []
    Otilde+:
      constant: 4
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
      least_valuation: 0
    - representative: 7
      least_valuation: 0
    - representative: 2
      least_valuation: 3
    - representative: 6
      least_valuation: 3
    - representative: 10
      least_valuation: 3
    - representative: 14
      least_valuation: 3
  local_densities:
  - prime: 2
    densities: [1, 0, 1, 5/2, 1, 0, 1, 5/4, 1, 0, 1, 5/2]
  - prime: 3
    densities: [4/3, 2/3, 10/9, 4/3, 2/3, 8/9, 4/3, 2/3, 28/27, 4/3, 2/3, 10/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8]
indefinite:
  isotropic: true
morphisms:
- target: 4BFK
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4BFK
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 2, -3]
  - [0, 0, 1, -2]
  scale: 1
- target: 4BFK
  name: O(L) generator 3
  matrix:
  - [-1, 2, -2, 0]
  - [-2, 3, -2, 0]
  - [-2, 2, -1, 0]
  - [-1, 1, -1, 1]
  scale: 1
- target: 4BFK
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4BFK
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 2, -3]
  - [0, 0, 1, -1]
  scale: 1
- target: 4BFK
  name: O(L) generator 6
  matrix:
  - [-1, 2, -4, 6]
  - [-2, 3, -4, 6]
  - [-2, 2, -2, 3]
  - [-1, 1, -1, 1]
  scale: 1
- target: 4BFK
  name: O(L) generator 7
  matrix:
  - [-1, 2, -2, 0]
  - [-2, 9, -14, 12]
  - [-2, 8, -13, 12]
  - [-1, 3, -5, 5]
  scale: 1
- target: 4BFK
  name: O(L) generator 8
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID6.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICW, 3ID6.
