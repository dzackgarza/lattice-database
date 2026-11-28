---
tag: 5IAQ
name: Constructed lattice 5IAQ
latex: L_{\mathrm{5IAQ}}
certifications:
  derive: 4ba61d2b1473a9c4c1d17e8b0a6cd82e41d8aa9e1088114887bd7bb4d823dd68
  form.integer_valued: 296bd15493e8118e03cc6342ea668ffddb5dce97d9a236a358f78d6a60a55f51
  integral.elementary_primes: 92c5aa67012626f5618b90d821155e380e1b36493d5a6303495ba860c4a63a6e
  integral.genus_symbol: a0c5ad190777bdacaf1b62465f70c2d1423c57eccd33b8e6d7dc46e7088260b7
  integral.genus_class_count: ae6f6bd2030a29632bc1f820d89a887fe242105b37de1f89bc3ec37d3f511d28
  integral.overlattice_count: c10204df3bb007f554cf536325fe3ff9cb7ee8cad1edfb787d532ff58b9dc98e
  integral.spinor_genus_count: 068ba905f299d7bcb12e3002c2ef0cb07709edc1d385d47546383a18d90b20c5
  integral.spinor_genera: fe1ab1da7c8a95d04fa8bb4136e1cb4400aa0fa8bcf97c242abcfd18a63ca045
  integral.hyperbolic_index: 3e43cafbb2daf82bb40767084cf569025a9d6c8e5833826495d4b526b5dbaa9c
  definite.automorphism_group_order: f5951da7e19b90b12a432f07ad96c21a3f4a2fd1dc96abec5516a504425fb16f
  definite.automorphism_group_generator_morphisms: e35bea2639244ce6bef7f4cf26f57b8cc20d0d75c6c628d170f73ada3beb84ed
  integral.discriminant_sequence: fea38426ba4d2577393fb3b41f2c564d72db17854bf3f3b649620c165c8c4632
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -2, 1, 0, 0]
- [0, 1, -2, 1, 0]
- [0, 0, 1, -2, 1]
- [0, 0, 0, 1, -2]
signature: [0, 5]
determinant: -5
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -4/5, -3/5, -2/5, -1/5]
- [0, -3/5, -6/5, -4/5, -2/5]
- [0, -2/5, -4/5, -6/5, -3/5]
- [0, -1/5, -2/5, -3/5, -4/5]
form:
  integer_valued: true
integral:
  elementary_primes: [5]
  parity: odd
  level: 10
  discriminant_group: [5]
  discriminant_sequence:
    discriminant_factors: [5]
    discriminant_basis_lifts:
    - ['0', -1/5, -2/5, -3/5, 1/5]
    discriminant_quadratic_gram:
    - [1/5]
    discriminant_group_order: 2
    discriminant_generators:
    - - [4]
    image_generators:
    - - [1]
    - - [1]
    - - [1]
    - - [4]
    image_order: 2
    kernel_order: 240
    coset_representatives:
    - - [1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0]
    quotient_multiplication:
    - [0]
  overlattice_count: 1
  bad_reduction_primes: [2, 5]
  genus_symbol: 'I_{0,5} (2: [1^-5]_7; 5: 1^4 5^1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 480
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 20, 40, 32, 60, 100, 120, 120]
  root_system: [A4]
  roots:
  - type: A4
    scale: -1
    simple_roots:
    - [0, 0, 0, 0, 1]
    - [0, 0, 0, 1, 0]
    - [0, 0, 1, 0, 0]
    - [0, 1, 0, 0, 0]
  - type: A1
    scale: -1/2
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [-1, -2]
morphisms:
- target: 5IAQ
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5IAQ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 1, 0, 0, -1]
  - [0, 1, -1, 1, -1]
  - [0, 1, -1, 0, 0]
  scale: 1
- target: 5IAQ
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, -1, 1, -1]
  - [0, 1, -1, 1, -1]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5IAQ
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, -1, 1, -1]
  - [0, 0, -1, 1, 0]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3IF5.
- tag: 3IF5
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3IF5.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3IF5.
