---
tag: 6CUG
name: Constructed lattice 6CUG
latex: L_{\mathrm{6CUG}}
certifications:
  derive: 450be3c9a4361f984f3ad3eafb9d440d5ee6272e098945ade368741ee5630258
  form.integer_valued: 3df99316843e091a46d24b90d7c798b14cf62d0cd3b2361aa53010eeeb93e79b
  integral.elementary_primes: 788b2b4ee3f08c84b18785dad2e387f0fb41c513af855a035485b0aa8f9ce8bd
  integral.genus_symbol: d769d0fa38f5f8a7c0743a7189d79a14ec8caf81442543fea8bc68ab8491ee35
  integral.genus_class_count: c778451bf97fb4fd43dc14eca21971d3685473f8e863d47e7c0e6fef051dc7f7
  integral.overlattice_count: 1da212f2baab48ad4531c0596d6f5f3b8cbc175162c9a91e1bf9fba47841d867
  integral.spinor_genus_count: f03d9a3b7dac77c834c2f4700180fe9afb740e439ae5155bd47d0b7983114c11
  integral.spinor_genera: 62f79f57e78b9fd6cfa5565f6719748d821aa1234e3ffe0a7277d3185967be16
  integral.hyperbolic_index: 83454338d34d01a6f7e17931b9193aad8fa89b6850095a15f3f3b9677fa4fe3e
  automorphisms.automorphism_group_generator_morphisms: 042a787abcc7076db0508885744c81b9c9cc40d7a8c1a629f10479da6ce1b5e4
  integral.discriminant_form: 5aab418195f15f905dc3cdec4f14f83c0d90a155b273d1398713bc7bd8587fe0
rank: 4
gram_tensor:
- [0, 2, 0, 0]
- [2, 0, 0, 0]
- [0, 0, 2, -1]
- [0, 0, -1, 2]
signature: [3, 1]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [0, 1/2, 0, 0]
- [1/2, 0, 0, 0]
- [0, 0, 2/3, 1/3]
- [0, 0, 1/3, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 6
  discriminant_group: [2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{3,1} (2: 1^-2:2^2; 3: 1^3 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  discriminant_form:
    orthogonal_group_order: 4
    isotropic_classes: 3
    isotropic_orbits: 2
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 6CUG
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, -1]
  scale: 1
- target: 6CUG
  name: O(L) generator 2
  matrix:
  - [2, -1, -2, 1]
  - [-1, 2, 2, -1]
  - [2, -2, -3, 2]
  - [0, 0, 0, 1]
  scale: 1
- target: 6CUG
  name: O(L) generator 3
  matrix:
  - [1, -2, -1, -1]
  - [0, 1, 0, 0]
  - [0, -2, 0, -1]
  - [0, -2, -1, 0]
  scale: 1
- target: 6CUG
  name: O(L) generator 4
  matrix:
  - [1, -2, -1, -1]
  - [-2, 7, 4, 1]
  - [2, -6, -3, -2]
  - [0, -2, 0, -1]
  scale: 1
- target: 6CUG
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0013, 0012.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0013, 0012.
---

The selected Gram tensor is obtained by orthogonal sum of 0013, 0012.
