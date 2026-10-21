---
tag: 3FID
name: watson 2:1017
latex: watson 2:1017
aliases: []
certifications:
  derive: 05586b1fdb7d15169c14075c8beed52ae1f94a2ddc5e3818f7e7daf02ae19429
  form.integer_valued: 3963fea00d851217068f3ac79c9ec1e01a8cb37186e1846e32b74775d3b62d20
  integral.elementary_primes: fca3c7ed93c52afbe5c373520f4f6dde8b99436740356fef8c658a06d1ee17f6
  integral.genus_symbol: 15f156f653c0b695e037dba63a5d2659032281f913d7e3068c487cd05ac874f3
  integral.genus_class_count: 34d6ff4bb8ae83698f512f178fc867b4259f4a39132be84a341f7b6f58cea189
  integral.overlattice_count: aedff4f39d503424cc5fecdfeae03de0b7eb3ca855f52e10b17dfb8abca2a6c0
  integral.hyperbolic_index: 8b865c89be011a3db5a22ac3fc3d87bb39258dd2d5ce0d358bb8323dde0a0bcd
  definite.automorphism_group_order: d2888373e1db64801313b53c72bd7d45f0d7a44ba14ce1f6d6655dfd7fb4a97a
  definite.automorphism_group_generator_morphisms: 7e1c5730675a151ae4e11b4c79fbd685aa7e5378bab15a82015746a64c756861
  integral.primitive_orbits: 5781817734d08da1b79e4f2a7786cefce9935053f6ea86c688125200e6a5262d
  integral.modular_scale: 01380ecb602d3aa25a7b20231adc4fe7e033e542def638db4a5e6f952c3de80c
  definite.genus_theta_series: 5852b30f861db31ab0dd9fea14ef0f5dc9c3d6b0691850d41fae95796f7d2b14
  definite.theta_series_cuspidal_component: f03ffc7a217e595f2cdc991a738e4c93d6ed878bdf23265ef8d47fd23737aca8
  definite.siegel_eisenstein_coefficients: 110a0b6ad4d98178182106620c0b36e7f35ecf6c724a094e68c58b7a3711a605
  integral.anisotropic_primes: 3324bfb04dd219149b5dd0474dfa61284917130a7d962c3e0ca52d29bf771bbb
  integral.local_representations: 11c7173df5a6e7088861d4874ed25bb2d74f09f12894b5cabab48b102334c0c8
  integral.local_densities: 961f876081257b3497b25bff5ebf1084c8914d084cecec8c6cc40e9332714a00
rank: 2
gram_tensor:
- [1, 0]
- [0, 16]
signature: [2, 0]
determinant: 16
definiteness: positive_definite
dual_gram_tensor:
- [1, 0]
- [0, 1/16]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 32
  modular_scale: 16
  discriminant_group: [16]
  overlattice_count: 3
  bad_reduction_primes: [2]
  quadratic_character: -4
  genus_symbol: 'I_{2,0} (2: [1^1]_1:[16^1]_1)'
  genus_class_count: 1
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [1, 0, 0, 0]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [1, 0, 0, 0]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [1, 0, 0, 0]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [2, 0, 0, 0]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [1, 0, 0, 0]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [1, 0, 0, 0]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [2, 0, 0, 0]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [2, 0, 0, 0]
      w: [0, 0, 0, 0]
  anisotropic_primes: [2]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 5
      least_valuation: 2
    - representative: 2
      least_valuation: 5
    - representative: 10
      least_valuation: 5
  local_densities:
  - prime: 2
    densities: [4, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0]
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0]
  - [1, 0]
  perfect: false
  theta_series: [1, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0]
  genus_theta_series: [1, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0]
  theta_series_cuspidal_component: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  siegel_eisenstein_coefficients: [2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0]
  root_system: []
  roots:
  - type: A1
    scale: 8
    simple_roots:
    - [0, 1]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0]
root_sublattice:
  invariant_factors: [1, 1]
  norms: [1, 16]
morphisms:
- target: 3FID
  name: O(L) generator 1
  matrix:
  - [-1, 0]
  - [0, -1]
  scale: 1
- target: 3FID
  name: O(L) generator 2
  matrix:
  - [1, 0]
  - [0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 2:1017.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:2:1017` gives this Gram tensor.
