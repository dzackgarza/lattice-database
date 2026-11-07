---
tag: 3IET
name: Constructed lattice 3IET
latex: L_{\mathrm{3IET}}
certifications:
  derive: 71e3d78ac4f63467a04efcdb1d32be7e492017cf7d77787a97cab6259115d4c7
  form.integer_valued: f39be68ccc55cad88905438083c5801ac6c8e5bb43490dfc82721a64428e3850
  integral.elementary_primes: 2f3cbab421a1eac239c8ad383af3df3981627028fbb498c29d723a6ca8e822cd
  integral.genus_symbol: 26b3809dc577ab6b65ef33a6401374594f692b9fe98d72ac18422436789bdea1
  integral.genus_class_count: 70ab50c47aeb761eff80c65c62b692fbdead7ad9b8ef337e183164dc52cfaace
  integral.overlattice_count: 5ff97c10b641090337f4ec1c0f9d3d1581631c85def35a28ffb98b0f01ddad78
  integral.spinor_genus_count: f2c80cd3822cf0fc2bbc3e875ee33945685738f643bf5e44e20fed2164f6ddf5
  integral.spinor_genera: 79c902dacb5fbd2b95291c07a3431e5c3a03eb2babd5a6c9e2f80a772f74453b
  integral.hyperbolic_index: 1b399bc909f096dc9f7ec898fd6cfe67e7670deec68176d9146b5141f7f61889
  automorphisms.automorphism_group_generator_morphisms: 67d67b75c76b2a4e4d3267800828f43e795276f3ad32adfe2eb6df7a34be265f
  integral.discriminant_form: 22b721771d2ffde42d2d67160de9447e733f0e43d6c6dd437bb6be9583fa8eec
  integral.primitive_orbits: 3fbef2930991a0c6140804233d079868a493d291f75bfb9e7c43d0abea8518e1
  integral.modular_scale: b5d8a4dbf4466da43afbc5b6c34a043b8f01cfb21a3be08b1654c553808f0b89
  integral.anisotropic_primes: 5c425b272494ac60f50fbb18682a4175b68f8e50beaf8177ec8f2bac18c6f8f1
  integral.local_representations: 676f92e7d1eb75d895c6d0934a5cfbced848bf6df8321731a09e970c62d90436
  integral.local_densities: 44812c1cd6c99e2214516ae6dc00b8f911158dd2ff1c9f7edebfdf6e012d884c
rank: 3
gram_tensor:
- [-2, 0, 0]
- [0, 0, 1]
- [0, 1, 0]
signature: [1, 2]
determinant: 2
definiteness: indefinite
dual_gram_tensor:
- [-1/2, 0, 0]
- [0, 0, 1]
- [0, 1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  modular_scale: false
  discriminant_group: [2]
  overlattice_count: 1
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{1,2} (2: 1^2 [2^1]_7)'
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
  discriminant_form:
    orthogonal_group_order: 1
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
    densities: [0, 3/2, 0, 3/2, 0, 2, 0, 9/4, 0, 3/2, 0, 3/2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IET
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IET
  name: O(L) generator 2
  matrix:
  - [-1, 0, -1]
  - [2, 1, 1]
  - [0, 0, 1]
  scale: 1
- target: 3IET
  name: O(L) generator 3
  matrix:
  - [1, 0, 1]
  - [2, 1, 1]
  - [0, 0, 1]
  scale: 1
- target: 3IET
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICX, 0016.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 3ICX, 0016.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICX, 0016.
