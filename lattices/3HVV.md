---
tag: 3HVV
name: BGF.3.xxx (union:602)
latex: BGF.3.xxx
aliases: [BGF.3.xxx]
certifications:
  derive: 27d7ab05e2049f5df18bd92575a17e973367e07233337e2bde5b21726f20b25d
  form.integer_valued: c01ab3472db133732903b9989e77ee7462de4fbac34636867956b03fb2c96c88
  integral.elementary_primes: 5cfbc19a34c3b2841b69b76b121193c5ad071e17297f83a5ef72c4fc3b0818f6
  integral.genus_symbol: 89faf1643bda3317512b466293420043b7a4f21e8fe71d5a5030a1e8d77a36e2
  integral.genus_class_count: 18a7621147631875dd3ee0511d8e6e00d3bf7aebac2b42bfed4f776d1b6ac0bd
  integral.overlattice_count: 0bd3abdb8ae54e8e5ac4be484be74f29993dea2fca9b2b492c5a5ec4fd047665
  integral.spinor_genus_count: 097d56cedab63032374d1e2e22d6b2008319fce0c0179ce34edd10377a5008bb
  integral.spinor_genera: 248057e2797d722d72778accd72909a916aebc1687663a8b8fe75f7d229a6b06
  integral.hyperbolic_index: c5509f99ee19de42a546cbab67e8ed410975d1d9327115d6833cb8780150468c
  definite.automorphism_group_order: 8a1f186019be0d83c14ca5b9eb321fce8173ed3cfa0a5c563f503eb724ce3b2e
  definite.automorphism_group_generator_morphisms: 4bfec30b82e8da66edc9ad8a1cd1c0b6276a43fe2907ab065753360418a81c93
  integral.primitive_orbits: 5c6cc2e4787b144fcdada934c3e29021d4af93a1de3b130b4f77a8ad31a86978
  integral.modular_scale: a5cba68f9852abff8f447945bb3afb2eb9964da4cf7e8c7a66db0d64c9363e2e
  definite.genus_theta_series: debc3ff88faab079a99b2ad5ba3c3ea68c08fb24756fd808631ed54df536c027
  definite.theta_series_cuspidal_component: a4599cd8f93ce7d9986af8abee56d2e58c980e5e6dca193737f483509d9bda0a
  definite.siegel_eisenstein_coefficients: cb835264f4215d56b36b1574ae00e0e2a39e788277788e5180db7d19525caa6f
  integral.anisotropic_primes: 998f0c57cc56e722428a0f73365aaacf879a2e113a5ba4bef61c014ef7bb294e
  integral.local_representations: a06849f95e2d2c987f42f260537a2d5b70dd7624a257d3f1210578790ae7d32a
  integral.local_densities: 6f01959c79197d139cac7b0bf9ba9cac8d241762c49a365dc9f5513a99bc8ef9
rank: 3
gram_tensor:
- [3, 1, 0]
- [1, 3, 1]
- [0, 1, 3]
signature: [3, 0]
determinant: 21
definiteness: positive_definite
dual_gram_tensor:
- [8/21, -1/7, 1/21]
- [-1/7, 3/7, -1/7]
- [1/21, -1/7, 8/21]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 42
  modular_scale: false
  discriminant_group: [21]
  overlattice_count: 1
  bad_reduction_primes: [2, 3, 7]
  genus_symbol: 'I_{3,0} (2: [1^-3]_3; 3: 1^-2 3^-1; 7: 1^2 7^-1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 2, 1]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 0, 3, 2]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 0, 6, 4]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 0, 6, 4]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 0, 3, 2]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 0, 3, 2]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 0, 6, 4]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 0, 6, 4]
      w: [0, 0, 0, 0]
  anisotropic_primes: [7]
  local_representations:
  - prime: 7
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 0
    - representative: 21
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [1/2, 1/2, 2, 5/4, 1/2, 1/2, 1, 5/4, 1/2, 1/2, 2, 2]
  - prime: 3
    densities: [2/3, 2/3, 4/3, 2/3, 2/3, 2, 2/3, 2/3, 14/9, 2/3, 2/3, 4/3]
  - prime: 7
    densities: [8/7, 8/7, 8/7, 8/7, 8/7, 8/7, 0, 8/7, 8/7, 8/7, 8/7, 8/7]
definite:
  minimum: 3
  kissing_number: 6
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  - [0, 0, 1]
  - [0, 1, 0]
  - [1, 0, 0]
  perfect: false
  theta_series: [1, 0, 0, 6, 4, 2, 4, 0, 4, 4, 2, 8, 10]
  genus_theta_series: [1, 2/3, 2/3, 16/3, 10/3, 4/3, 4, 0, 10/3, 14/3, 4/3, 8, 32/3]
  theta_series_cuspidal_component: [0, -2/3, -2/3, 2/3, 2/3, 2/3, 0, 0, 2/3, -2/3, 2/3, 0, -2/3]
  siegel_eisenstein_coefficients: [2/3, 2/3, 16/3, 10/3, 4/3, 4, 0, 10/3, 14/3, 4/3, 8, 32/3]
  root_system: []
  roots:
  - type: A1
    scale: 3
    simple_roots:
    - [1, 0, -1]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3HVV
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3HVV
  name: O(L) generator 2
  matrix:
  - [0, 0, 1]
  - [0, 1, 0]
  - [1, 0, 0]
  scale: 1
families: []
related: []
references:
- citation: G. Nebe and N. J. A. Sloane, Catalogue of Lattices, archive entry union:602.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/union.gz
---

Catalogue of Lattices archive entry `union:602` names `BGF.3.xxx`.
