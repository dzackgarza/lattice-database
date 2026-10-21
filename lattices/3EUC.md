---
tag: 3EUC
name: watson 2:152
latex: watson 2:152
aliases: []
certifications:
  derive: 732e617d7642967e743e55acb56c84d8d5b620a94f8c6174e5f8b80217a8a82a
  form.integer_valued: 6e21f3df22c646f1494310a08a9e370cf01c871db1a720c3d482e54eb2a2676c
  integral.elementary_primes: bb6d9fd2030521674bc509d32b8ee59924e81e2eba9ce1bd823f386587103055
  integral.genus_symbol: f924cc0f01fca0364bf89fd3a756f2a069d84741dc4b49b7e4e01c04e1955f8b
  integral.genus_class_count: d7998afe7423a7c1c25209a3cc9f04c3273b6a76b7bcb8b8828814a6a9359c30
  integral.overlattice_count: 38949bbfe233ca46f093bc58e5ad27ceab7b3496f19fb01531ed94f70cf13c47
  integral.hyperbolic_index: 5ce7f081b7d0ae973657e5057a19af96cd6c569a164545c27d25937d4c7bf990
  definite.automorphism_group_order: 5bb33727bea3f8daab57b29b3232dd589ff6c0873454ca97b78d899819f65ab9
  definite.automorphism_group_generator_morphisms: 890931a1fa4b34a717744deffa6d95ebb526d319645055c710b22edc6c62d136
  integral.discriminant_sequence: 3ae6e22ac054b6f1802122adb95db6ecd24787c7ceefa6dffaedbfaefd4ee431
  integral.primitive_orbits: cdb806255f0a447da9871b620ded00140b45de7d4d03bf79bb8f2e01ee3285ad
  integral.modular_scale: dbc5aa53c87fa4fa982eb44648d424ec511a37b6127974109a4f78fff72e8b35
  definite.genus_theta_series: 6b91ab2bbb6d08da431088de0f2f6d1eab058c3ec352271d7bcbac6af517cb99
  definite.theta_series_cuspidal_component: 277e3fdf66a4be68f3fa886cd63a5b0d7e77076c2955d49ca73790045014134f
  definite.siegel_eisenstein_coefficients: d83f10a8a1f81c9874cb4d547b67dcad39efd44b797e0314823b563f947992f3
  integral.anisotropic_primes: e8f0767c498e775eea4f7452bf7d5b90b3cd63d6fbfe5c55ed155ae301c52b48
  integral.local_representations: 4fe9d11be041e6060404a2c1a89f3df8d00d2c6c2e6acb2e23c1f5e6c5c2f34c
  integral.local_densities: c7f7086076528bae2289666759aef0c921664980af140e4dccd0d5a0454064ec
rank: 2
gram_tensor:
- [2, 1]
- [1, 2]
signature: [2, 0]
determinant: 3
definiteness: positive_definite
dual_gram_tensor:
- [2/3, -1/3]
- [-1/3, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: even
  level: 3
  modular_scale: 3
  discriminant_group: [3]
  discriminant_sequence:
    discriminant_factors: [3]
    discriminant_basis_lifts:
    - [-2/3, 1/3]
    discriminant_quadratic_gram:
    - [2/3]
    discriminant_group_order: 2
    discriminant_generators:
    - - [2]
    image_generators:
    - - [2]
    - - [2]
    image_order: 2
    kernel_order: 6
    coset_representatives:
    - - [1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0]
    quotient_multiplication:
    - [0]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{2,0} (2: 1^-2; 3: 1^-1 3^-1)'
  genus_class_count: 1
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 1, 0, 0]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 1, 0, 0]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 1, 0, 0]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 2, 0, 0]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 1, 0, 0]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 1, 0, 0]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 2, 0, 0]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 2, 0, 0]
      w: [0, 0, 0, 0]
  anisotropic_primes: [2, 3]
  local_representations:
  - prime: 2
    classes:
    - representative: 2
      least_valuation: 1
    - representative: 6
      least_valuation: 1
    - representative: 10
      least_valuation: 1
    - representative: 14
      least_valuation: 1
  - prime: 3
    classes:
    - representative: 2
      least_valuation: 0
    - representative: 6
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [0, 3, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0]
  - prime: 3
    densities: [0, 2, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0]
definite:
  minimum: 2
  kissing_number: 6
  automorphism_group_order: 12
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0]
  - [-1, 1]
  - [0, -1]
  - [0, 1]
  - [1, -1]
  - [1, 0]
  perfect: true
  theta_series: [1, 0, 6, 0, 0, 0, 6, 0, 6, 0, 0, 0, 0]
  genus_theta_series: [1, 0, 6, 0, 0, 0, 6, 0, 6, 0, 0, 0, 0]
  theta_series_cuspidal_component: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  siegel_eisenstein_coefficients: [0, 6, 0, 0, 0, 6, 0, 6, 0, 0, 0, 0]
  root_system: [A2]
  roots:
  - type: G2
    scale: 1
    simple_roots:
    - [0, 1]
    - [1, -2]
root_sublattice:
  invariant_factors: [1, 1]
  norms: [2]
morphisms:
- target: 3EUC
  name: O(L) generator 1
  matrix:
  - [0, -1]
  - [1, 1]
  scale: 1
- target: 3EUC
  name: O(L) generator 2
  matrix:
  - [1, 1]
  - [0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 2:152.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:2:152` gives this Gram tensor.
