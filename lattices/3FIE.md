---
tag: 3FIE
name: watson 2:1018
latex: watson 2:1018
aliases: []
certifications:
  derive: 18867eb127c4c91a4b81ea82d0791f7c1ea213c54629890e9c9c570e84c2cd5d
  form.integer_valued: e822c67f72ee9a1ef65a62d81fb7042a46d99cb20a93d41096c99529ceabcddf
  integral.elementary_primes: 38f5fea42535800131a32b4f6293b07cc671217a4c9353f18dfd4a85ecb1fbb7
  integral.genus_symbol: d64b2aa7bff82c2a7daad5649cead5452cd2603cbb0d7a8cb534d6b48ef20742
  integral.genus_class_count: 66c088849e6e0dfe494955a345a3ae408c747c3c37f73c21fc5f06d765eecace
  integral.overlattice_count: d62023f5c9e23bba8bd424f8f4d7bce79bd54239b63b42fc43348c6cc62e074e
  integral.hyperbolic_index: 383d290298c13e365728486aad8734c355788ea4a27712bc5a38bdf27d6fa000
  definite.automorphism_group_order: 7454a01084f5eccdcb175b9e53c02fe70bb22e56dabbab6c0966fcbb0e7a56ec
  definite.automorphism_group_generator_morphisms: 7cc8ef1d60e60a3eb95f72a53a275e57fb93adc3a633cf6450aae55996881a5e
  integral.primitive_orbits: 69648b5fcbe7a0bc7a41b7b3f563c799a757cf140423419eb0049a3c50256b89
  integral.modular_scale: 69309a37c590e05ba75f6faebea2e5de6001c02a1ed52f688815901909d9930d
  definite.genus_theta_series: d3b9e20b486ca97a4caf8d2bea082e3f8b6867038eb16f80efe9143b1de8e7da
  definite.theta_series_cuspidal_component: ac2cf552c951a3b64311d4963e2eac29b2e82b256095dab828a3b183cf770d52
  definite.siegel_eisenstein_coefficients: 448b54e2e216971aaf9a500ec02c3805e8cccedc3b2d40fe817168c6d4a81ae4
  integral.anisotropic_primes: 4e1c988471062bb32db11e31d43b5aae7f2579a7024f00776be083900506e819
  integral.local_representations: a9ed671da42311c348f9e00eccd45f3a0aaa07acff52e5ba6b4cd663f9465ddf
  integral.local_densities: 6a3e6971bf980c53c018363eabc45884bb78e22e33ac18c3e9a0dfd401200d65
rank: 2
gram_tensor:
- [5, 2]
- [2, 4]
signature: [2, 0]
determinant: 16
definiteness: positive_definite
dual_gram_tensor:
- [1/4, -1/8]
- [-1/8, 5/16]
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
  genus_symbol: 'I_{2,0} (2: [1^-1]_5:[16^-1]_5)'
  genus_class_count: 1
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
  anisotropic_primes: [2]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 5
      least_valuation: 0
    - representative: 2
      least_valuation: 5
    - representative: 10
      least_valuation: 5
  local_densities:
  - prime: 2
    densities: [0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0]
definite:
  minimum: 4
  kissing_number: 2
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [0, -1]
  - [0, 1]
  perfect: false
  theta_series: [1, 0, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0]
  genus_theta_series: [1, 0, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0]
  theta_series_cuspidal_component: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  siegel_eisenstein_coefficients: [0, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0]
  root_system: []
  roots:
  - type: A1
    scale: 2
    simple_roots:
    - [0, 1]
  - type: A1
    scale: 8
    simple_roots:
    - [2, -1]
root_sublattice:
  invariant_factors: [1, 2]
morphisms:
- target: 3FIE
  name: O(L) generator 1
  matrix:
  - [-1, 0]
  - [0, -1]
  scale: 1
- target: 3FIE
  name: O(L) generator 2
  matrix:
  - [-1, 0]
  - [1, 1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 2:1018.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:2:1018` gives this Gram tensor.
