---
tag: 3IDM
name: Constructed lattice 3IDM
latex: L_{\mathrm{3IDM}}
certifications:
  derive: 96e704b26da7de6732a1f6cbd6d808eebe8e4b4bb83083d26d5d54084d3ed29d
  form.integer_valued: 58ecbc8f03046b57b7a2535497635cfa7f1fba3a54fbae0e977abce1ff900eb0
  integral.elementary_primes: 8b8d1288a0ba3a9daeb665b53ce26f5390d502e1fb06b1cc85d21d477f56907d
  integral.genus_symbol: 68d019b8281b338b6ca0846b5a515dbe22e968a6b03ad842a44c0107c720dca5
  integral.genus_class_count: e4f40f37f60b22e7a91e58e03986463afec7cb05c5e7ea031d836d6060aa8779
  integral.overlattice_count: f19e279fd26ba292341e6b7dd5b243e6a95b61bd326382af7f8b82c473c22499
  integral.spinor_genus_count: 3563789e7588966f948e19f0c842fa8efbb542a2a8d9627d7683cb3d2055914d
  integral.spinor_genera: 889d16596b1d1c896c9829330a596abf84bcd89f96a73d80309c20637a1650ea
  integral.hyperbolic_index: 0ffc8e78baad4781060894b1b5803a13c4a2ec63d6d59b52a75c622868f10fd9
  automorphisms.automorphism_group_generator_morphisms: bfbd68b36460ec0ffdd047ff07e232cc7c00d5fd91c925b0177a4f07bbc90040
  integral.primitive_orbits: 99dada91ed256f2df3c6bf91d10a37f200eb3762bae3f8411e83dcdb6361fab1
  integral.modular_scale: 2b7e34782855aac60bc06cd37a76566255b25369d4f5a3509941f1c49d660672
  integral.anisotropic_primes: 7e734b8ff5144fe900fca3517ca462d15fa2f318e05909fdbc5dbd314d5374b4
  integral.local_representations: 0d6a5abc3aaf11d8772a9581ed0428839ab30f568c72765e3bd921039e6eda1d
  integral.local_densities: 5027c0ab1c27f01c5fb87c23d8538b38271f51f765a80e3efd17a4088d561ea5
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, -4, 2]
- [0, 2, -4]
signature: [1, 2]
determinant: 12
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, -1/3, -1/6]
- [0, -1/6, -1/3]
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
  genus_symbol: 'I_{1,2} (2: [1^-1]_5 2^2; 3: 1^-2 3^-1)'
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
      constant: 3
      z: []
      w: []
    SOtilde:
      constant: 3
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
      constant: 3
      z: []
      w: []
    SOtilde+:
      constant: 6
      z: []
      w: []
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 2
    - representative: 5
      least_valuation: 0
    - representative: 7
      least_valuation: 2
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
    densities: [1, 0, 0, 2, 3, 0, 0, 3/2, 1, 0, 0, 3/2]
  - prime: 3
    densities: [2/3, 2/3, 4/3, 2/3, 2/3, 2, 2/3, 2/3, 14/9, 2/3, 2/3, 4/3]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IDM
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 1, -1]
  scale: 1
- target: 3IDM
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IDM
  name: O(L) generator 3
  matrix:
  - [7, 12, 0]
  - [-4, -7, 0]
  - [-2, -4, 1]
  scale: 1
- target: 3IDM
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID1.
- tag: 3ID1
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID1.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ID1.
