---
tag: 6ALE
name: Constructed lattice 6ALE
latex: L_{\mathrm{6ALE}}
certifications:
  derive: 56d23eb8c41d75434441d084b8e7d10514266ca386827982e5a21429040bb0e9
  form.integer_valued: dda9c42e018a676de95c9b1d8d4db9c5d119eb77d9a7fa37d23b4df193bb9ee8
  integral.elementary_primes: 3084717fc9d8a951c2dc42f4e1a896a1ec57cbbc4d96e942bf268d2430908cbf
  integral.genus_symbol: 51a18234b7638ad556a6bb25789e8e543f692f01243f3b902ddde7aecd8ee58d
  integral.genus_class_count: a65b751a6102ef4ffc3086adacc460ef916eeef261230b89843a0bf2d0870606
  integral.overlattice_count: cc991294c331ec0f673838c4d4c8f2538d5306606ab282f043f823711c6317e1
  integral.spinor_genus_count: 9969d14f1c9fe231724eea5992686c30098bace00367b6086a0484794f78986d
  integral.spinor_genera: d3749c36b52ce6e8a3a671782eacbd80b9929733969784a3a1b9b0dc80fc3ed9
  integral.hyperbolic_index: 806ec9baecaad55e76e4a6d7f9757b7a43852025c7babb3e997f02d0e3b14c2e
  automorphisms.automorphism_group_generator_morphisms: 6223b9f69e96250318bacc8a96479c3a9f4fa763277bf50704d898879ca9ea65
  integral.discriminant_form: ebec506f2452e9e513c2ebb0f66b9d51f8bd5dbde38a0b1bcfda2b500267fcd7
  automorphisms.automorphism_group_order: a084ecce85340628f951312cd0604e717f1f410eae237e48d4cec202534184c4
  integral.discriminant_orbits: 53afedd2a801d00d5581112582f785db3dffd8e87b046369c63d241354b8c987
  integral.modular_scale: 6a75a5e6a27229b3acdafcd196e20c7efd68e04a005b31eebee853e74bde7ca0
  integral.anisotropic_primes: c02bb9f46ec02d2e9153a1af6dcb71e02b5d1e57aa2f1cefb8316d566a1b2e6c
  integral.local_representations: aeedafdb331dcdb93456e2c7780dc30c6cf4372123ceeff19957f51965ba6a43
  integral.local_densities: 77671753912d1f40b35c7d22e30e9f3d69c2eacf6c61f3547eecce675b4469db
rank: 4
gram_tensor:
- [0, -1, 0, 0]
- [-1, 0, 0, 0]
- [0, 0, 0, -2]
- [0, 0, -2, 0]
signature: [2, 2]
determinant: 4
definiteness: indefinite
dual_gram_tensor:
- [0, -1, 0, 0]
- [-1, 0, 0, 0]
- [0, 0, 0, -1/2]
- [0, 0, -1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 2
  modular_scale: 2
  discriminant_group: [2, 2]
  overlattice_count: 4
  delta: 0
  bad_reduction_primes: [2]
  quadratic_character: 1
  genus_symbol: 'II_{2,2} (2: 1^2:2^2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
  discriminant_form:
    orthogonal_group_order: 2
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
    densities: [0, 1, 0, 5/2, 0, 1, 0, 13/4, 0, 1, 0, 5/2]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 4, 'O(L) generator 2 #2', O(L) generator 8, O(L) generator 6, O(L) generator 7, 'O(L) generator 6 #2', O(L) generator 3, 'O(L) generator 8 #2', 'O(L) generator 9 #2', 'O(L) generator 10 #2', 'O(L) generator 11 #2', 'O(L) generator 12 #2', O(L) generator 12]
indefinite:
  isotropic: true
morphisms:
- target: 6ALE
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6ALE
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, -2]
  - [-1, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6ALE
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 2, 0]
  - [0, 0, 1, 0]
  - [-1, 0, 0, 1]
  scale: 1
- target: 6ALE
  name: O(L) generator 4
  matrix:
  - [0, -1, 0, 0]
  - [-1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6ALE
  name: O(L) generator 5
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6ALE
  name: O(L) generator 6
  matrix:
  - [1, 0, 2, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, -1, 0, 1]
  scale: 1
- target: 6ALE
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 2]
  - [0, 1, 0, 0]
  - [0, -1, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6ALE
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6ALE
  name: O(L) generator 9
  matrix:
  - [0, -1, 0, 0]
  - [-1, 2, -2, -2]
  - [0, 1, 0, -1]
  - [0, 1, -1, 0]
  scale: 1
- target: 6ALE
  name: O(L) generator 10
  matrix:
  - [0, -1, -2, 0]
  - [-1, 0, -2, 0]
  - [0, 0, 1, 0]
  - [-1, -1, -2, 1]
  scale: 1
- target: 6ALE
  name: O(L) generator 11
  matrix:
  - [-1, 0, 0, -2]
  - [0, 1, -2, 0]
  - [1, 0, 0, 1]
  - [0, 1, -1, 0]
  scale: 1
- target: 6ALE
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6ALE
  name: 'O(L) generator 2 #2'
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6ALE
  name: 'O(L) generator 6 #2'
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 2]
  - [-1, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6ALE
  name: 'O(L) generator 8 #2'
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6ALE
  name: 'O(L) generator 9 #2'
  matrix:
  - [0, -1, 2, 0]
  - [-1, 0, 2, 0]
  - [0, 0, 1, 0]
  - [1, 1, -2, 1]
  scale: 1
- target: 6ALE
  name: 'O(L) generator 10 #2'
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, -1]
  - [0, 0, -1, 0]
  scale: 1
- target: 6ALE
  name: 'O(L) generator 11 #2'
  matrix:
  - [1, 0, 0, 2]
  - [0, 1, 0, 2]
  - [-1, -1, 1, -2]
  - [0, 0, 0, 1]
  scale: 1
- target: 6ALE
  name: 'O(L) generator 12 #2'
  matrix:
  - [0, -1, 0, 0]
  - [-1, 0, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ICZ.
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICY, 3ICZ.
