---
tag: 3GCF
name: watson 3:490
latex: watson 3:490
aliases: []
certifications:
  derive: 09b2faa8fffd6430c833f24da6d9b157c02d4140f8187bc8de9fc9754506ad27
  form.integer_valued: 25278de8a9e9cb04b6f2cf082cedadd34c35bee0a6876de2277e2a155767994c
  integral.elementary_primes: 782077c835ad2731c02c28a1790a9ea2827f25acc37b38f5366a225eb9ccf56b
  integral.genus_symbol: 6f03eea37c3424b1fc86cde503586892258b632cad0ed1f978dc47abf0f50575
  integral.genus_class_count: 929dd7f0d613c7de857dd1780b9cb54f0f099b8fc79988a5bec00823a12c1a67
  integral.overlattice_count: 187c867d40722f48a79ac2d6dc844b7b4986185930b82486de57681239fe5987
  integral.spinor_genus_count: bd8a400bbdea329a66e5e2613c5007d1e2c356f8248facbe2870b73f1d163f6f
  integral.spinor_genera: 085590adfdfa998c00c8fdd1451c54cbc4cf9babe419b7c20c2f6abde439331f
  integral.hyperbolic_index: 085f14c812ebd249fda91fe5ba87f3f3b62790fb55e675df2c5989f65d0d7609
  definite.automorphism_group_order: 91ab4f7d3e451ebf5d5fa637ed40a10467a8d1baf2d1755a2ef7dfb19f50c1d5
  definite.automorphism_group_generator_morphisms: 10b8a6f8f6f9534cc4813f72b9306060d8a0db1664152a4bf42027167cab7cfd
  integral.primitive_orbits: 6896a8d83eb12010a9b98d0ed839d029585cb6344eb6befac456bfffe7e17292
  integral.modular_scale: 4d5f94865c2e7426a7c58d68dc1a876bb2a105b42c6a01d973ffc399a43c9bb3
  definite.genus_theta_series: 78fb03f9a3604f6189b087d67eee73356790fd99c03dfbf498996997fd44a209
  definite.theta_series_cuspidal_component: d65726fe9c55d8e12fd691ee3e2e786fb8533c6989d4b1edb36cb8430c3a9927
  definite.siegel_eisenstein_coefficients: 4a765952625a9b30cc819b17d4701e04c35888d8ce1706894f3904e1ef306ac0
  integral.anisotropic_primes: bd5d122b6dd170a5a9bbd101373367bc6593f50fbce5246be31b3cab99f222fb
  integral.local_representations: 1fd69ee2e7fd382734644769b1a5086a74715bd5ef7e0a121de62c3df8476f9b
  integral.local_densities: 731d79c8da7e6b1a781d1c7591247bc44d65c8e96d81b072e82f33f1e3e18090
rank: 3
gram_tensor:
- [2, 1, -1]
- [1, 3, -1]
- [-1, -1, 3]
signature: [3, 0]
determinant: 12
definiteness: positive_definite
dual_gram_tensor:
- [2/3, -1/6, 1/6]
- [-1/6, 5/12, 1/12]
- [1/6, 1/12, 5/12]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 24
  modular_scale: false
  discriminant_group: [12]
  overlattice_count: 2
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{3,0} (2: [1^-2]_2 [4^1]_7; 3: 1^-2 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 1, 1, 1]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 1, 2, 1]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 1, 4, 2]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 2, 8, 2]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 1, 2, 1]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 1, 2, 1]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 2, 8, 2]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 2, 8, 2]
      w: [0, 0, 0, 0]
  anisotropic_primes: [2]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 3
      least_valuation: 0
    - representative: 7
      least_valuation: 0
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
    densities: [0, 1, 2, 1, 0, 1, 2, 3/2, 0, 1, 2, 3/2]
  - prime: 3
    densities: [2/3, 2/3, 4/3, 2/3, 2/3, 2, 2/3, 2/3, 14/9, 2/3, 2/3, 4/3]
definite:
  minimum: 2
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  theta_series: [1, 0, 2, 8, 2, 0, 6, 8, 6, 0, 4, 8, 12]
  genus_theta_series: [1, 0, 2, 8, 2, 0, 6, 8, 6, 0, 4, 8, 12]
  theta_series_cuspidal_component: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  siegel_eisenstein_coefficients: [0, 2, 8, 2, 0, 6, 8, 6, 0, 4, 8, 12]
  root_system: [A1]
  roots:
  - type: A1
    scale: 2
    simple_roots:
    - [0, 1, 1]
  - type: A1
    scale: 3
    simple_roots:
    - [1, -1, 1]
  - type: A1
    scale: 1
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 2]
morphisms:
- target: 3GCF
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GCF
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 0, -1]
  - [0, -1, 0]
  scale: 1
- target: 3GCF
  name: O(L) generator 3
  matrix:
  - [1, 1, -1]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:490.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:3:490` gives this Gram tensor.
