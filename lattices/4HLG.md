---
tag: 4HLG
name: Constructed lattice 4HLG
latex: L_{\mathrm{4HLG}}
certifications:
  derive: 8afcbda129bd9dff0fdae631682299780536f4ac7729b11d97718eff50d7948d
  form.integer_valued: 12d5435c516606485e4c2d95185e8d4a9e96657c576503671a6894ab7d88f2b7
  integral.elementary_primes: 98d369edc38cc027bcca9b85d33677eeec2f221c948e54448c65b657a71d43ec
  integral.genus_symbol: 00d01f244d8e6afbf64c5a84c4c64290618cc818d8ad0dcd449ad3206487504a
  integral.genus_class_count: 5ac84b658c675a0a4b478b78ee9fb883363b64d103f69cb0dbdcbb76b7fd0881
  integral.overlattice_count: a338fb90da6629314055c618130d3df30d6db33a686739b703dbc6afcc100af3
  integral.spinor_genus_count: f58050334f0fba11f003516bbf2e5d3697a84d9d7b5d87eb611210265ade3103
  integral.spinor_genera: bf09e0d040c5446cdd67b26ca83c72f1dd9c479f7fba58edeb21016fdab22eb8
  integral.hyperbolic_index: 1189deec9397b661b4560e616133060a7bbf2fc4e900cfe70969fe339442d5aa
  definite.automorphism_group_order: 1a480610102521564d38cc7366b6d4de070380f7f826a720f4b3113cbe24051a
  definite.automorphism_group_generator_morphisms: cc73267301c955d1f0733063811b95c426f7a88863c04376b65d26837f69042f
  integral.primitive_orbits: 2d1b6d0815acf1609080e0873cab4e2bf0e42fac8e3135fe11c0829491df9dd4
  integral.modular_scale: 2fcc5d1708a86ad2dffa67dd5a97f2e146bbc97ce753a7c5a466e87809cd2f60
  definite.genus_theta_series: aebb852b65a9358b09e31545b986005d571cada5a6603107d4b4a6c267542b49
  definite.theta_series_cuspidal_component: ab4cc57a7a26c4cb3cc305dbd743a67ea926bb466af26f8be959d7f9a6b2379d
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, 2, 0, 0]
- [0, 0, 2, -1]
- [0, 0, -1, 2]
signature: [4, 0]
determinant: 6
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, 1/2, 0, 0]
- [0, 0, 2/3, 1/3]
- [0, 0, 1/3, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  modular_scale: false
  discriminant_group: [6]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  quadratic_character: 24
  genus_symbol: 'I_{4,0} (2: [1^-3 2^1]_2; 3: 1^3 3^-1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [1, 2, 2, 1]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [1, 2, 2, 1]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [1, 2, 2, 1]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [1, 2, 2, 1]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [1, 2, 2, 1]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [1, 2, 2, 1]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [1, 2, 2, 1]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [1, 2, 2, 1]
      w: [0, 0, 0, 0]
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 48
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 8, 16, 14, 24, 22, 12, 44, 42, 36, 64, 40]
  genus_theta_series: [1, 10/3, 28/3, 40/3, 34/3, 24, 70/3, 12, 124/3, 130/3, 36, 200/3, 136/3]
  theta_series_cuspidal_component: [0, -4/3, -4/3, 8/3, 8/3, 0, -4/3, 0, 8/3, -4/3, 0, -8/3, -16/3]
  root_system: [A2, A1]
  roots:
  - type: G2
    scale: 1
    simple_roots:
    - [0, 0, 0, 1]
    - [0, 0, 1, -1]
  - type: A1
    scale: 1
    simple_roots:
    - [0, 1, 0, 0]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1]
  norms: [1, 2]
morphisms:
- target: 4HLG
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4HLG
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, -1]
  - [0, 0, 1, 0]
  scale: 1
- target: 4HLG
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, -1]
  - [0, 0, 0, -1]
  scale: 1
- target: 4HLG
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0012.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0012.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0012.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0002, 0012.
