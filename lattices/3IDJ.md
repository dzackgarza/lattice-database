---
tag: 3IDJ
name: Constructed lattice 3IDJ
latex: L_{\mathrm{3IDJ}}
certifications:
  derive: 87005ea16908974c614293eeb4bdfbc80219701e3306a627d88b3eb44614965f
  form.integer_valued: ee2bd77585ec3c7fd178fce5ea67a7dbb1872286b19e75bb9f9a0204ade2110b
  integral.elementary_primes: d0a1e2416d884c55e7a8101cfe3c6c8c4478da5d5d668a40e5f7b5e51356856d
  integral.genus_symbol: 0b1611e49b4353825f3240925ee1b08458273f2418a79e04282066f886a274b4
  integral.genus_class_count: b12a5a5c145ac4a65bdb4fa032f14849334506b7041c551dd6cbbdf0ce6757b9
  integral.overlattice_count: 5b385452cd6b0d6a080df3098f64db5d25503a90b4b68af3d3b46adc191b93ba
  integral.spinor_genus_count: 32c8469069a8702c019e2186dae316186d60b0572bfa5421526555045ae9b3d0
  integral.spinor_genera: a7c1db50413784978347ce29b88535659d9292b2a6920423c80e8d598c4b072b
  integral.hyperbolic_index: d3d08bf9fedc5317ed06a08637faa9d3dc0dff2d69bde5f323758aa738e39b77
  automorphisms.automorphism_group_generator_morphisms: 6dad73ffc4a080e294e74d6638b993e03820c1f096e9b63b3e46aa9288c983d6
  integral.primitive_orbits: 6c4a5a8a113707cd15eebd74d7c4acbba42c66ffa6608b4c606a5f9398c2f537
  integral.modular_scale: 6d175807d7e3ecba8158b1fa64c5afabc66d04bce71c6fbdf87fe8f8cad6cb56
  integral.anisotropic_primes: 757db0af2c790e806bc865a558f6d19faa38a55b2f8bcd9795ac0da451377c3b
  integral.local_representations: fb65712eda2d80473dcbe03b8fe1dcc35f32bfc4bdfc9186c222a9457da56bb3
  integral.local_densities: 71a5768d6bdb5b4dbf812c0779bf8ae279d7c2e9b94ce6c558298c82287fd8a2
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, 0, -2]
- [0, -2, 0]
signature: [2, 1]
determinant: -4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, 0, -1/2]
- [0, -1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 2
  modular_scale: false
  discriminant_group: [2, 2]
  overlattice_count: 4
  bad_reduction_primes: [2]
  genus_symbol: 'I_{2,1} (2: [1^1]_1 2^2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 1
      z: []
      w: []
    SO:
      constant: 1
      z: []
      w: []
    Otilde:
      constant: 3
      z: []
      w: []
    SOtilde:
      constant: 3
      z: []
      w: []
    O+:
      constant: 1
      z: []
      w: []
    SO+:
      constant: 1
      z: []
      w: []
    Otilde+:
      constant: 3
      z: []
      w: []
    SOtilde+:
      constant: 3
      z: []
      w: []
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 2
    - representative: 5
      least_valuation: 0
    - representative: 7
      least_valuation: 2
    - representative: 2
      least_valuation: 3
    - representative: 6
      least_valuation: 3
    - representative: 10
      least_valuation: 3
    - representative: 14
      least_valuation: 3
  local_densities:
  - prime: 2
    densities: [3, 0, 0, 3, 1, 0, 0, 3/2, 3, 0, 0, 3/2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IDJ
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IDJ
  name: O(L) generator 2
  matrix:
  - [-1, 0, -2]
  - [1, 1, 1]
  - [0, 0, 1]
  scale: 1
- target: 3IDJ
  name: O(L) generator 3
  matrix:
  - [1, 2, 0]
  - [1, 1, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IDJ
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICZ.
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICZ.
