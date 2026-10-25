---
tag: 3EUT
name: watson 2:169
latex: watson 2:169
aliases: []
certifications:
  derive: ca6a488c1af0602b8e85d7ade0f5f3d943ddecd3fc394501697dcc1eea162f69
  form.integer_valued: e47f7c2760d3d811358f9f4395120c3754aae5c09c3d9e991cba9536d0cfefdd
  integral.elementary_primes: 6ebb764f9c73500d950abf4a97483e5993ec6811274b9f2c140d00df230d0c98
  integral.genus_symbol: 81b227742d942e95e20c8ca1bc51f546710585e3bf4c27b502387523fbea3f4d
  integral.genus_class_count: 71b81fb714eee438c434f0f4960c5d9cd9a1784df3accbe01cb950cc524d1c8d
  integral.overlattice_count: b6205c4bdffbe4ad5420cbcb2a0d4107113736dd65e27a4413715f480b9e7534
  integral.hyperbolic_index: 734952be9a6fe47a68692a6a51234a705ba3b64af0c3762f6c75bc2e4c89a972
  definite.automorphism_group_order: 7e057236e4a94c7439caf6cf75a1fbd3e04486e529105e0a553698ed20f29e97
  definite.automorphism_group_generator_morphisms: 224f579ca40e4a2883a765b43d58ee15d52900586f063ff2dd0965d25969e455
  integral.primitive_orbits: 2737e86cf818e6c35854d9cfb23eace31d5359fa66e03aac4a35b11ed8eab4bc
  integral.modular_scale: 07341ad5db3ae44bbee7087a3f122f5ad1b3635866f857c3434a038853cf6a77
  definite.genus_theta_series: ca7c25424fab8b263f694bdba773b7199bfee374db1874ffd793ed9c0ae95c8f
  definite.theta_series_cuspidal_component: 21b83c670cac4e2a51581c4a964d848e33529cc65e1a470c87eaa8e3ed2588f5
  definite.siegel_eisenstein_coefficients: 3280a22ebda77ce94b52e22313c74388680da3809ae1892a322d2c51c65c80c1
  integral.anisotropic_primes: 366f2c2a719396058420034fef424a19fda36abc797119cbbe1e6de07000f1e4
  integral.local_representations: 0c892647b247aafdb604f7d8ff87698398202aa829c94dc6fff60698c35e9bd4
  integral.local_densities: f3bc410dbbb71c0b2a903f0b5f6e4c1e67a16a9a6e88d7ac56c4854a7a715aac
rank: 2
gram_tensor:
- [1, 0]
- [0, 2]
signature: [2, 0]
determinant: 2
definiteness: positive_definite
dual_gram_tensor:
- [1, 0]
- [0, 1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: 2
  discriminant_group: [2]
  overlattice_count: 1
  bad_reduction_primes: [2]
  quadratic_character: -8
  genus_symbol: 'I_{2,0} (2: [1^1 2^1]_2)'
  genus_class_count: 1
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [1, 1, 1, 0]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [1, 1, 2, 0]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [1, 1, 1, 0]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [1, 1, 2, 0]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [1, 1, 2, 0]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [1, 1, 2, 0]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [1, 1, 2, 0]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [1, 1, 2, 0]
      w: [0, 0, 0, 0]
  anisotropic_primes: [2]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 0
    - representative: 2
      least_valuation: 1
    - representative: 6
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [2, 2, 2, 2, 0, 2, 0, 2, 2, 0, 2, 2]
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0]
  - [1, 0]
  perfect: false
  theta_series: [1, 2, 2, 4, 2, 0, 4, 0, 2, 6, 0, 4, 4]
  genus_theta_series: [1, 2, 2, 4, 2, 0, 4, 0, 2, 6, 0, 4, 4]
  theta_series_cuspidal_component: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  siegel_eisenstein_coefficients: [2, 2, 4, 2, 0, 4, 0, 2, 6, 0, 4, 4]
  root_system: [A1]
  roots:
  - type: A1
    scale: 1
    simple_roots:
    - [0, 1]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0]
root_sublattice:
  invariant_factors: [1, 1]
  norms: [1, 2]
morphisms:
- target: 3EUT
  name: O(L) generator 1
  matrix:
  - [-1, 0]
  - [0, -1]
  scale: 1
- target: 3EUT
  name: O(L) generator 2
  matrix:
  - [1, 0]
  - [0, -1]
  scale: 1
families: []
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002.
references:
- citation: Watson, primitive lattices of class number one, 2:169.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: G. Nebe and N. J. A. Sloane, Catalogue of Lattices, archive entry union:141.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/union.gz
---

Source entry `watson:2:169` gives this Gram tensor.

Catalogue of Lattices archive entry `union:141` names `C2`.
