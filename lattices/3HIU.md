---
tag: 3HIU
name: BGF.2.318 (union:133)
latex: BGF.2.318
aliases: [BGF.2.318]
certifications:
  derive: f463c1f84146ba745841e2e9529a755d5c8863c601b5912d4163e4a2afe40311
  form.integer_valued: 9ef34aec09d0140d8c32197d5cef4d281beecd07df7e1e196171caf72a4b8e85
  integral.elementary_primes: 97981a30bd4099bcd126fa650656529b4da20529fa7d0135dae15bde0e09bc2d
  integral.genus_symbol: 95a20e009d8b61911d10b1b3c42f984837863dd20913eed3fa2a46d8007820ee
  integral.genus_class_count: 8583d0afe4516ff112947f7fb5e6eda2587a30b241606637368745e345dfa049
  integral.overlattice_count: 5031bbfd594ef02248affd33a8483e80bf34eb26255f0aad5bdb1c1547bd8c1c
  integral.hyperbolic_index: 5ab955352db6ce8a59670bc710eaaf10db9990060d503399255d7458913800d5
  definite.automorphism_group_order: fe343e5155ddf726285b4f3b0f22b6a04c525a01b86a20c5cc658f4d5df107ef
  definite.automorphism_group_generator_morphisms: 56137163d63f9b0a40fee85485ad00719108c0a0cf3761a086def9d11a552946
  integral.primitive_orbits: 0fbc9b6be035ae845610f638dd7e75c42e928cff128c136058e6d2d54188ea6f
  integral.modular_scale: 45dcd5fb4fed6d0c6149c6eaf006c7becaf7e6e6f6755195dfb41c103cd8e732
  definite.genus_theta_series: 00ffbbd78e7fb609205dcbc03f653ec60a4ea211f2b998a014b82ec3afc6e843
  definite.theta_series_cuspidal_component: 76f8841d12b73a034c948217095e58fbc05264e2b8384002eb6000cfa9f4aa89
  definite.siegel_eisenstein_coefficients: a4ac3d673e01dec792ad03ae00d4b96e2aca62ea57cfe093f40057222926104a
  integral.anisotropic_primes: 42454877c2da6f91411830eb6011ef3c7e6027531e23d7bf0a4c630004182423
  integral.local_representations: b10acece2e8322d3c09d229c6c2fc2a687e4122add2bf411e62d49e42f514a91
  integral.local_densities: 4368199b843db36d6047f67b923457e428b7c47c83567f3ee5dc96388d3239ca
rank: 2
gram_tensor:
- [3, 1]
- [1, 8]
signature: [2, 0]
determinant: 23
definiteness: positive_definite
dual_gram_tensor:
- [8/23, -1/23]
- [-1/23, 3/23]
form:
  integer_valued: true
integral:
  elementary_primes: [23]
  parity: odd
  level: 46
  modular_scale: 23
  discriminant_group: [23]
  overlattice_count: 1
  bad_reduction_primes: [2, 23]
  quadratic_character: -23
  genus_symbol: 'I_{2,0} (2: [1^2]_0; 23: 1^1 23^1)'
  genus_class_count: 2
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 1, 0]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 0, 1, 0]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 0, 2, 0]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 0, 2, 0]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 0, 1, 0]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 0, 1, 0]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 0, 2, 0]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 0, 2, 0]
      w: [0, 0, 0, 0]
  anisotropic_primes: [23]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 0
    - representative: 5
      least_valuation: 0
    - representative: 7
      least_valuation: 0
    - representative: 2
      least_valuation: 3
    - representative: 6
      least_valuation: 3
    - representative: 10
      least_valuation: 3
    - representative: 14
      least_valuation: 3
  - prime: 23
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 23
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [1, 0, 1, 1, 1, 0, 1, 2, 1, 0, 1, 1]
  - prime: 23
    densities: [2, 2, 2, 2, 0, 2, 0, 2, 2, 0, 0, 2]
definite:
  minimum: 3
  kissing_number: 2
  automorphism_group_order: 2
  automorphism_group_generator_morphisms: [O(L) generator 1]
  minimal_vectors:
  - [-1, 0]
  - [1, 0]
  perfect: false
  theta_series: [1, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 0, 2]
  genus_theta_series: [1, 2/3, 0, 4/3, 2/3, 0, 0, 0, 4/3, 2, 0, 0, 4/3]
  theta_series_cuspidal_component: [0, -2/3, 0, 2/3, -2/3, 0, 0, 0, 2/3, 0, 0, 0, 2/3]
  siegel_eisenstein_coefficients: [2/3, 0, 4/3, 2/3, 0, 0, 0, 4/3, 2, 0, 0, 4/3]
  root_system: []
  roots: []
root_sublattice:
  invariant_factors: []
morphisms:
- target: 3HIU
  name: O(L) generator 1
  matrix:
  - [-1, 0]
  - [0, -1]
  scale: 1
families: []
related: []
references:
- citation: G. Nebe and N. J. A. Sloane, Catalogue of Lattices, archive entry union:133.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/union.gz
---

Catalogue of Lattices archive entry `union:133` names `BGF.2.318`.
