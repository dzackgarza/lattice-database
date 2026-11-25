---
tag: 6GRC
name: Constructed lattice 6GRC
latex: L_{\mathrm{6GRC}}
certifications:
  derive: 51779ddb52c4332929a8899f437869839950441ff8f796b65ab7d6ec14ed110c
  form.integer_valued: f3d85cb8d874f0c3e59be354b856014291132000d91ca56a81914819dd8e4404
  integral.elementary_primes: 436de79cb1db148f25aa9e059617ba445b7ace11c1c18b89b798442f34e08a34
  integral.genus_symbol: a92e6be4d215886c83a3416c98cfa07b295d94c32778cd090591639e375c0289
  integral.genus_class_count: e4041c0141f85d48aef3e1887a2c2f7af75228cf0559e7d19ad5e5452b618b5e
  integral.overlattice_count: 47eb618c7473f28ca2678cf2fa9b7a55ebef7bc508ee51fdcfe1cb034510296b
  integral.spinor_genus_count: 47b5e855e7a94fce6ebdb847590eceba705bab1b32887127fd1dcdf564dc40ab
  integral.spinor_genera: 1801b4c08524c153f236b4265eb8684a3feabd3c904db04f76dbef34d22f38aa
  integral.hyperbolic_index: f201dd899c7cba7076709bb78a60bbc360f8ee6a91cda15c0b1839f3ab0d8a6b
  definite.automorphism_group_order: fc3b9236f46e03d5a8516e3b7f4f804d21892c2a990f6fff7bcbbc52482ea209
  definite.automorphism_group_generator_morphisms: 4d0c94bc0dbcea46a371c51c4ccb8d1bf2122363f088ad6cb3228a6889be7b08
  integral.discriminant_sequence: 216ae73a1ee6aa7ced1cb5b816315d180788e633734caf23e09ce50cc45e8d0d
  integral.discriminant_form: 4b47a991c677937c282d340f2da946ab15411d21140ffc6688db667821cb7f10
  integral.primitive_orbits: 8e8dc43d590fd38b1952ffcb0fddc8a9b8a19d54d37ef46c9cab004c75a87c21
  integral.modular_scale: eb2237a3cec8d3b74c92754c6656fd662014e41594a15fbe94ed58a9676f2668
  definite.genus_theta_series: 225e9cc6923693ca237dd2ebbdc9b760043817906cc555552442f23a4a485fc4
  definite.theta_series_cuspidal_component: ce8894ebd93ce144eb1c90d012041d0767bf53d196405eb6718c21d18af33d7f
  definite.siegel_eisenstein_coefficients: 05793f95be525478b1d8e591aaac864ff46f461f31e13f57cf11475d92d494d3
  integral.anisotropic_primes: 231724ef6e7f494cb345875b3e48411a9aef66e7b5abd7a0ff3764400da2cdd3
  integral.local_representations: bb386c5b3e6c9ade27c9c42ff48a142c98254b80dab1fae37733555fdd126d80
  integral.local_densities: 69927c7a832b09d8aced5a92e1ea276c54cad22f46673402cf16246b23b5219e
rank: 4
gram_tensor:
- [2, -1, 0, 0]
- [-1, 2, 0, 0]
- [0, 0, 2, -3]
- [0, 0, -3, 6]
signature: [4, 0]
determinant: 9
definiteness: positive_definite
dual_gram_tensor:
- [2/3, 1/3, 0, 0]
- [1/3, 2/3, 0, 0]
- [0, 0, 2, 1]
- [0, 0, 1, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: even
  level: 3
  modular_scale: 3
  discriminant_group: [3, 3]
  discriminant_sequence:
    discriminant_factors: [3, 3]
    discriminant_basis_lifts:
    - [1/3, -1/3, '0', '0']
    - ['0', '0', '0', 1/3]
    discriminant_quadratic_gram:
    - [2/3, '0']
    - ['0', 2/3]
    discriminant_group_order: 8
    discriminant_generators:
    - - [0, 1]
      - [2, 0]
    - - [2, 0]
      - [0, 1]
    image_generators:
    - - [1, 0]
      - [0, 2]
    - - [1, 0]
      - [0, 2]
    - - [0, 1]
      - [1, 0]
    image_order: 8
    kernel_order: 36
    coset_representatives:
    - - [1, 0]
      - [0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0, 0]
    quotient_multiplication:
    - [0]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  quadratic_character: 1
  genus_symbol: 'II_{4,0} (2: 1^4; 3: 1^2 3^2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 1, 0, 1]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 1, 0, 1]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 2, 0, 1]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 2, 0, 2]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 1, 0, 1]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 1, 0, 1]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 2, 0, 2]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 2, 0, 2]
      w: [0, 0, 0, 0]
  discriminant_form:
    orthogonal_group_order: 8
    isotropic_classes: 1
    isotropic_orbits: 1
  anisotropic_primes: [3]
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
    densities: [0, 3/2, 0, 9/4, 0, 3/2, 0, 21/8, 0, 3/2, 0, 9/4]
  - prime: 3
    densities: [4/3, 4/3, 4/9, 4/3, 4/3, 4/9, 4/3, 4/3, 4/27, 4/3, 4/3, 4/9]
definite:
  minimum: 2
  kissing_number: 12
  automorphism_group_order: 288
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, -1, 0, 0]
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -2, -1]
  - [0, 0, -1, -1]
  - [0, 0, -1, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, 1]
  - [0, 0, 2, 1]
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [1, 1, 0, 0]
  perfect: false
  theta_series: [1, 0, 12, 0, 36, 0, 12, 0, 84, 0, 72, 0, 36]
  genus_theta_series: [1, 0, 12, 0, 36, 0, 12, 0, 84, 0, 72, 0, 36]
  theta_series_cuspidal_component: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  siegel_eisenstein_coefficients: [0, 12, 0, 36, 0, 12, 0, 84, 0, 72, 0, 36]
  root_system: [A2, A2]
  roots:
  - type: G2
    scale: 1
    simple_roots:
    - [0, 0, 1, 0]
    - [0, 0, 0, 1]
  - type: G2
    scale: 1
    simple_roots:
    - [0, 1, 0, 0]
    - [1, -1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1]
  norms: [2]
morphisms:
- target: 6GRC
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 2, -3]
  - [0, 0, 1, -1]
  scale: 1
- target: 6GRC
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, -3]
  - [0, 0, 0, -1]
  scale: 1
- target: 6GRC
  name: O(L) generator 3
  matrix:
  - [0, 0, 0, 1]
  - [0, 0, -1, 2]
  - [2, -1, 0, 0]
  - [1, 0, 0, 0]
  scale: 1
related:
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0012, 3ID4.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 0012, 3ID4.
---

The selected Gram tensor is obtained by orthogonal sum of 0012, 3ID4.
