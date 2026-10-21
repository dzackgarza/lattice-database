---
tag: 3HVF
name: O(15) (union:586)
latex: O(15)
aliases: [O(15)]
certifications:
  derive: a2e8554cc368688df60371e353de3fde199b293fb026ffd1bfc7eb142ce85496
  form.integer_valued: 2f319813d9ee308c352beb267c5493f4d5fad770594c2850f613403d6faf09ac
  integral.elementary_primes: cd0c6886afa3f1b1ae64b44cf905b9285a8dadb83b0eb64a6ef8451c2e5910d5
  integral.genus_symbol: 31c473cb67de0506d85fa062ab6495ddffb1b7c4ee04446890437e6aad45d004
  integral.genus_class_count: d89c2987fb82eb76831b839a53878147b4916df23ddc30abce83cca45ece1f10
  integral.overlattice_count: 3351715a69a2acc76a4787418b32bbebabd5700148f09a03a6a90aefa44f79a7
  integral.spinor_genus_count: 8a8b04d4f46dcfe650e12f0f4ad8752188a95d2d7369d8982f126b6683e11a88
  integral.spinor_genera: 1ad92a871daf0f8d6e8bd1e2a586a73253b85c3e24a5a09b55d4d1ae6d414b99
  integral.hyperbolic_index: d4ee38afae556d5162f778a473f64738eff3a7c7e51917ba7ddd91ee7a272ecb
  definite.automorphism_group_order: 2d5fe25ba4680242d226aafc64c230fb6040190a2390f369322c85a4b6caa34c
  definite.automorphism_group_generator_morphisms: 096833de871d8efb4766b408e80d04f7e421609ddbedc0bd579f19f085785b62
  integral.primitive_orbits: 472db103142072da4d806ef4a9ca5b88c93c1886aba518521e97cc9e9e2f3e18
  integral.modular_scale: e5c99899943ce05c19e07cc090581d7eb4b678d3d912e4c62c55c0c53f177bf9
  definite.genus_theta_series: b96f19218378382f03fb935a827c196eb27e3c4ee0dae4ca49711169e14afe6b
  definite.theta_series_cuspidal_component: 0748800c0f01015418640b6cc450d9d77eade415bf2c52626b0ebd84e8e852e8
  definite.siegel_eisenstein_coefficients: f2af63135bf3efbfdd562d9f50dc17bbdfc90f25eefc89f7770aa0a8acafa050
  integral.anisotropic_primes: 94797bcc1afc560aa6447e9414b13b1f4c95a03614d5f89b2fced3ef0875d70c
  integral.local_representations: 869fa0fb8784074566230da846034cb415e97a3e63763fd2ffa1d637af09b7e6
  integral.local_densities: 443e6d62d2f1f928bcf45404d6cb033c7cc2fafc78655153e8bfac70cdeae06d
rank: 4
gram_tensor:
- [3, 1, 0, -1]
- [1, 3, 1, 0]
- [0, 1, 6, 2]
- [-1, 0, 2, 6]
signature: [4, 0]
determinant: 225
definiteness: positive_definite
dual_gram_tensor:
- [2/5, -2/15, 0, 1/15]
- [-2/15, 2/5, -1/15, 0]
- [0, -1/15, 1/5, -1/15]
- [1/15, 0, -1/15, 1/5]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 30
  modular_scale: 15
  discriminant_group: [15, 15]
  overlattice_count: 3
  bad_reduction_primes: [2, 3, 5]
  quadratic_character: 1
  genus_symbol: 'I_{4,0} (2: [1^4]_0; 3: 1^-2 3^-2; 5: 1^-2 5^-2)'
  genus_class_count: 5
  spinor_genus_count: 1
  spinor_genera: [5]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 1, 1]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 0, 1, 1]
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
      z: [0, 0, 1, 1]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 0, 1, 1]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 0, 4, 2]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 0, 4, 2]
      w: [0, 0, 0, 0]
  anisotropic_primes: [5]
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1, 1/2, 1, 5/4, 1, 1/2, 1, 13/8, 1, 1/2, 1, 5/4]
  - prime: 3
    densities: [2/3, 2/3, 14/9, 2/3, 2/3, 14/9, 2/3, 2/3, 50/27, 2/3, 2/3, 14/9]
  - prime: 5
    densities: [6/5, 6/5, 6/5, 6/5, 6/25, 6/5, 6/5, 6/5, 6/5, 6/25, 6/5, 6/5]
definite:
  minimum: 3
  kissing_number: 4
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 0, 4, 2, 0, 4, 4, 8, 12, 0, 8, 18]
  genus_theta_series: [1, 1/2, 1/2, 7/2, 5/2, 1/2, 7/2, 4, 13/2, 25/2, 1/2, 6, 35/2]
  theta_series_cuspidal_component: [0, -1/2, -1/2, 1/2, -1/2, -1/2, 1/2, 0, 3/2, -1/2, -1/2, 2, 1/2]
  siegel_eisenstein_coefficients: [1/2, 1/2, 7/2, 5/2, 1/2, 7/2, 4, 13/2, 25/2, 1/2, 6, 35/2]
  root_system: []
  roots: []
root_sublattice:
  invariant_factors: []
morphisms:
- target: 3HVF
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 3HVF
  name: O(L) generator 2
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 0, -1]
  - [0, 0, -1, 0]
  scale: 1
families: []
related: []
references:
- citation: G. Nebe and N. J. A. Sloane, Catalogue of Lattices, archive entry union:586.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/union.gz
---

Catalogue of Lattices archive entry `union:586` names `O(15)`.

Strongly 15-modular The odd associate of the extremal strongly 15-modular even lattice E(15).
