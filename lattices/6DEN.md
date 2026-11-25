---
tag: 6DEN
name: Constructed lattice 6DEN
latex: L_{\mathrm{6DEN}}
certifications:
  derive: 138b22e04e69d2c5d107a492fc294f476ad4b10b8a7bfeb902c90f694ede0555
  form.integer_valued: f0728bc3643b773bbc2eddae56327b8e257bf7c06d9363c83ceb10870ff0d228
  integral.elementary_primes: 307fd46bd101f1c7c95714da5719ca53c8fb3b2f82b90d812d9b80d84111d939
  integral.genus_symbol: 65075a31357922a734f5473fd36f69ddcda47f5e7fd1ad44e018af80237719c6
  integral.genus_class_count: 5ad4aed5ea206e477ccf67a322d869be5881fedd98174d6da25c54c2a99bdbda
  integral.overlattice_count: 65f625b62bcec6d44ec5b291773cbefa07c5beac408438d9e1b990e9fd2b3524
  integral.spinor_genus_count: 252aec05e0618e1e49a163ed287d3c5bb580faf3846e0b725f5bc20411a6ec86
  integral.spinor_genera: 8616132430980c82f472fa12fee92ced06be1b9a4cb44df95f4e9b4f448f0693
  integral.hyperbolic_index: a0385ace2ec53eec80515143f1a21ef67efe5bb834d7838d42e0386f4ef9d7cb
  automorphisms.automorphism_group_generator_morphisms: bcdcfc45b7946388ca5a898f4b0561ac7a66f52287820db05ea69ce3636b01e0
  integral.discriminant_form: f18e32fff2843cb788a3febe7f80e74233f5b82b8a13a3f4e47e065a3f8de4f7
  automorphisms.automorphism_group_order: 0de17ea504e84d45c5b612bc9b8330c72c5c7e981a27c16d67354f88aa613c2d
  integral.discriminant_orbits: 0227485e2a5c80996d26ade9e11b4d29ac5cc2c104e940631ba6e681e5cea030
  integral.modular_scale: db520500fca344b17978acd6f41747089d134007264977f3a0a56a11327668be
  integral.anisotropic_primes: 4ecde2c9ec3741ad0b65678ce2a65230d7b338d315a68d0b79468375094d3c42
  integral.local_representations: 03f710da47f79d00673570dbbd8440f24598738e1c2654b10e5ac2ca911537be
  integral.local_densities: 50c1989abcdd99511a5056c0720e9b718b5092a2912b2303fbb97f10f3892e7f
rank: 4
gram_tensor:
- [0, 2, 0, 0]
- [2, 0, 0, 0]
- [0, 0, 2, -3]
- [0, 0, -3, 6]
signature: [3, 1]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [0, 1/2, 0, 0]
- [1/2, 0, 0, 0]
- [0, 0, 2, 1]
- [0, 0, 1, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 6
  modular_scale: false
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
  discriminant_orbits:
    Otilde:
      constant: 3
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    SOtilde:
      constant: 3
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    Otilde+:
      constant: 3
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    SOtilde+:
      constant: 3
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    O:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    SO:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    O+:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    SO+:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
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
    densities: [0, 3, 0, 1/2, 0, 3, 0, 7/4, 0, 3, 0, 1/2]
  - prime: 3
    densities: [2/3, 4/3, 8/9, 2/3, 4/3, 10/9, 2/3, 4/3, 26/27, 2/3, 4/3, 8/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, 'O(L) generator 2 #2', 'O(L) generator 3 #2', 'O(L) generator 4 #2', O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 6DEN
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, -1, 1]
  scale: 1
- target: 6DEN
  name: O(L) generator 2
  matrix:
  - [2, -1, -1, 3]
  - [-1, 2, 1, -3]
  - [-2, 2, 3, -6]
  - [-2, 2, 2, -5]
  scale: 1
- target: 6DEN
  name: O(L) generator 3
  matrix:
  - [1, -2, -2, 3]
  - [0, 1, 0, 0]
  - [0, -2, -1, 3]
  - [0, 0, 0, 1]
  scale: 1
- target: 6DEN
  name: O(L) generator 4
  matrix:
  - [1, -2, -1, 3]
  - [-6, 7, 6, -15]
  - [0, 2, 2, -3]
  - [-2, 4, 3, -7]
  scale: 1
- target: 6DEN
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6DEN
  name: 'O(L) generator 2 #2'
  matrix:
  - [2, -1, 2, -3]
  - [-1, 2, -2, 3]
  - [-2, 2, -3, 6]
  - [0, 0, 0, 1]
  scale: 1
- target: 6DEN
  name: 'O(L) generator 3 #2'
  matrix:
  - [1, -2, 1, -3]
  - [0, 1, 0, 0]
  - [0, -2, 2, -3]
  - [0, -2, 1, -2]
  scale: 1
- target: 6DEN
  name: 'O(L) generator 4 #2'
  matrix:
  - [1, -2, 2, -3]
  - [-6, 7, -9, 15]
  - [0, 2, -1, 3]
  - [2, -2, 3, -4]
  scale: 1
related:
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0013, 3ID4.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 0013, 3ID4.
---

The selected Gram tensor is obtained by orthogonal sum of 0013, 3ID4.
