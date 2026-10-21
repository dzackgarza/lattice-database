---
tag: 3HIW
name: BGF.2.416 (union:135)
latex: BGF.2.416
aliases: [BGF.2.416]
certifications:
  derive: 3fcf36dbd14959dec237e7538db83a3e2ce41f8b4767678fddd1185ab0004371
  form.integer_valued: cfd94babe1f4ac7dc2f3b21ea97aa1d35b0f1b6b11dfe6cf50ced35f681938ca
  integral.elementary_primes: 677e63182e7d9c3b630e8b64be5429460a28d2eeb7178cb6093199f82f741da9
  integral.genus_symbol: 99bdd1cdc50e015fd76f91e7043164d559a0141ea8c76369ac25ab83491d918b
  integral.genus_class_count: 0d3695e2fb2a6aee5aa5bf534137b8483d4370c9b9d58b7694a7ec1950f922e4
  integral.overlattice_count: 030ac5f20d76a9a6c27568a788c216fb1c729a7c1fba20a12b5952d0a8b92501
  integral.hyperbolic_index: c3a2a23715cc285d08638bc7d5d44716f8e07a0371acdd115c414f9947c91c40
  definite.automorphism_group_order: df069902da18a9dad1afce1dfdcc3b76a8f13e56a444f6893357a44b6c72f03b
  definite.automorphism_group_generator_morphisms: af92a693f026e8227f0e0cce2ec47e824c6d68f03bd3dad3bd3575cdd6c890ca
  integral.discriminant_sequence: 006c72290100f9d12dfb6daa4fd6e25500a6914e1d50364236d2b57fdd138604
  integral.primitive_orbits: 8462cc568a79cdc7ef584b422a002a7c2891b09db6f298a666a06a253b701f13
  integral.modular_scale: e19f70f1202f0ebdbe1ebc996cb9f0dc07146a34db366e6e2fbcfbb11beabb48
  definite.genus_theta_series: 01e689e333fd0895b71a18ba7e430cf302a7b0077039172680bbdc5d2d696d59
  definite.theta_series_cuspidal_component: 6a096659a364483fdc9f3128a92d3a8c46389571e449afcc6d992c9b91a2eaaf
  definite.siegel_eisenstein_coefficients: a0c6ae54b5590d7ddd090018308fcbf83198afb040731da457fdbbac59d3b8e5
  integral.anisotropic_primes: ab0f6133e105704c637e83eb312f804f13a27886e5962ad971df560242d58b02
  integral.local_representations: 8639053d031a66791d43ed0b75258e42ab106c691ddc4a7334a681cf339add31
  integral.local_densities: 9b794ba87487340c21f05f5c086c9306927fa651ff5d791cdf8331521be4c750
rank: 2
gram_tensor:
- [4, 1]
- [1, 6]
signature: [2, 0]
determinant: 23
definiteness: positive_definite
dual_gram_tensor:
- [6/23, -1/23]
- [-1/23, 4/23]
form:
  integer_valued: true
integral:
  elementary_primes: [23]
  parity: even
  level: 23
  modular_scale: 23
  discriminant_group: [23]
  discriminant_sequence:
    discriminant_factors: [23]
    discriminant_basis_lifts:
    - [-6/23, 1/23]
    discriminant_quadratic_gram:
    - [6/23]
    discriminant_group_order: 2
    discriminant_generators:
    - - [22]
    image_generators:
    - - [22]
    image_order: 2
    kernel_order: 1
    coset_representatives:
    - - [1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0]
    quotient_multiplication:
    - [0]
  overlattice_count: 1
  bad_reduction_primes: [2, 23]
  quadratic_character: -23
  genus_symbol: 'II_{2,0} (2: 1^2; 23: 1^1 23^1)'
  genus_class_count: 2
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 0, 1]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 0, 0, 1]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 0, 0, 2]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 0, 0, 2]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 0, 0, 1]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 0, 0, 1]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 0, 0, 2]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 0, 0, 2]
      w: [0, 0, 0, 0]
  anisotropic_primes: [23]
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
  - prime: 23
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 23
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2]
  - prime: 23
    densities: [2, 2, 2, 2, 0, 2, 0, 2, 2, 0, 0, 2]
definite:
  minimum: 4
  kissing_number: 2
  automorphism_group_order: 2
  automorphism_group_generator_morphisms: [O(L) generator 1]
  minimal_vectors:
  - [-1, 0]
  - [1, 0]
  perfect: false
  theta_series: [1, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2]
  genus_theta_series: [1, 0, 2/3, 0, 4/3, 0, 4/3, 0, 2, 0, 0, 0, 8/3]
  theta_series_cuspidal_component: [0, 0, -2/3, 0, 2/3, 0, 2/3, 0, 0, 0, 0, 0, -2/3]
  siegel_eisenstein_coefficients: [0, 2/3, 0, 4/3, 0, 4/3, 0, 2, 0, 0, 0, 8/3]
  root_system: []
  roots: []
root_sublattice:
  invariant_factors: []
morphisms:
- target: 3HIW
  name: O(L) generator 1
  matrix:
  - [-1, 0]
  - [0, -1]
  scale: 1
families: []
related: []
references:
- citation: G. Nebe and N. J. A. Sloane, Catalogue of Lattices, archive entry union:135.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/union.gz
---

Catalogue of Lattices archive entry `union:135` names `BGF.2.416`.
