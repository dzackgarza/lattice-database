---
tag: 3FIM
name: watson 2:1026
latex: watson 2:1026
aliases: []
certifications:
  derive: 2eb22b00c5e82dfae1579e624c4c854aa48a4ee8cda04b9658492375bb2087ec
  form.integer_valued: ec51ba8f07232851a4de85381d31ba66e468a8abee804a3500a03b44edcaed67
  integral.elementary_primes: 4cbf6363dd41b110e434f10007cc8297ac20d5e11293021737239c9cccd7d8ce
  integral.genus_symbol: 5c9533dcfaf70d126502531c8caebd368eefef772ee293ee51a2c48fc562872e
  integral.genus_class_count: 1389d2118d8dd4c0ac0112aa97f169d2726a49c3810b5801525289c71e1fa8ed
  integral.overlattice_count: efdbbf1b06edf3175bac3f5f53dce4d156179f40a354adedcfa8822cb8c03681
  integral.hyperbolic_index: 5c4aa13995d613296cd9ae07deb81cb01c5c2fa94fa32f8adb1ea2424f112bfb
  definite.automorphism_group_order: 51eddf827c7038749f7f26d3258dced08734e4d3823e9dc66e7a3524a9ab9730
  definite.automorphism_group_generator_morphisms: cfc2720a3826522beb731449e167b6f33479c4a3211deb19becea287cbac1dc5
  integral.primitive_orbits: fed9d9bbb10972db07960921d7f676016f4bd31f477eb381c608e495a4a13c43
  integral.modular_scale: eb7151440f97cc39258a91327c8fe59df2ebdcc984edabe1aa62c1064b88bfa7
  definite.genus_theta_series: 82068c1ea33a243373ff020d5cb96be3da43c3999a6c15f4a9f38e3d23fc4709
  definite.theta_series_cuspidal_component: 6e885a1f4d1a6116a52771944afacc60f7d9e03dbeea213d0eadad155c0f2cbe
  definite.siegel_eisenstein_coefficients: c84f1ca3d05bad3b08891dc3fc71b721dff928c6f61244156a58482ea2d49e48
  integral.anisotropic_primes: 19db4b094517f9da963ed7e4a44dcfed3447ff7dde1ec2dbcaf7b5adccb06ade
  integral.local_representations: ed195a11222da6c78b794bbdf7adf28f985b72d6f0ad7306f84bbf7382ae79b9
  integral.local_densities: ca543b0c5e3347804ea46dff1523fc6e4f5dc6100f7b14a7ce96703b518bb2f3
rank: 2
gram_tensor:
- [3, -1]
- [-1, 3]
signature: [2, 0]
determinant: 8
definiteness: positive_definite
dual_gram_tensor:
- [3/8, 1/8]
- [1/8, 3/8]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 16
  modular_scale: 8
  discriminant_group: [8]
  overlattice_count: 2
  bad_reduction_primes: [2]
  quadratic_character: -8
  genus_symbol: 'I_{2,0} (2: [1^-1]_3:[8^-1]_3)'
  genus_class_count: 1
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 1, 1]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 0, 2, 1]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 0, 4, 2]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 0, 4, 2]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 0, 2, 1]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 0, 2, 1]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 0, 4, 2]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 0, 4, 2]
      w: [0, 0, 0, 0]
  anisotropic_primes: [2]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 3
      least_valuation: 0
    - representative: 2
      least_valuation: 3
    - representative: 6
      least_valuation: 3
  local_densities:
  - prime: 2
    densities: [0, 0, 4, 4, 0, 0, 0, 4, 0, 0, 4, 4]
definite:
  minimum: 3
  kissing_number: 4
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0]
  - [0, -1]
  - [0, 1]
  - [1, 0]
  perfect: false
  theta_series: [1, 0, 0, 4, 2, 0, 0, 0, 2, 0, 0, 4, 4]
  genus_theta_series: [1, 0, 0, 4, 2, 0, 0, 0, 2, 0, 0, 4, 4]
  theta_series_cuspidal_component: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  siegel_eisenstein_coefficients: [0, 0, 4, 2, 0, 0, 0, 2, 0, 0, 4, 4]
  root_system: []
  roots:
  - type: A1
    scale: 4
    simple_roots:
    - [1, -1]
  - type: A1
    scale: 2
    simple_roots:
    - [1, 1]
root_sublattice:
  invariant_factors: [1, 2]
morphisms:
- target: 3FIM
  name: O(L) generator 1
  matrix:
  - [-1, 0]
  - [0, -1]
  scale: 1
- target: 3FIM
  name: O(L) generator 2
  matrix:
  - [0, 1]
  - [1, 0]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 2:1026.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:2:1026` gives this Gram tensor.
