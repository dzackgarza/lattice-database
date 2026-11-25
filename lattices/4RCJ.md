---
tag: 4RCJ
name: Constructed lattice 4RCJ
latex: L_{\mathrm{4RCJ}}
certifications:
  derive: 1f33fda308e8affa9259fd748954ed21b00d98aa73c27725294912cc3101b789
  form.integer_valued: 19f2c7c552c8424e9b85d14e97d185ac3793af245a715b6e5cbeb9c5ff5df3eb
  integral.elementary_primes: 71b055905271fcffb377a935f972705cc0e66b4f113979a7b57ea379a85e32a2
  integral.genus_symbol: ab0637fd8200c28233b3d1088abf65e0116372926f298aa374eb39ce31e51da8
  integral.genus_class_count: 9c030f47815e8be499bee007f37a7b97a1330477bcbaa11055773cc1d831a19b
  integral.overlattice_count: e10ac7f93d670752a4b3a2175203f17aac6831d917d07a37ee9bfdde4086f890
  integral.spinor_genus_count: c902fbee387700371f16d54236e2a1c46d6485a8cb7d2e48c96122dda469bab1
  integral.spinor_genera: 0220e51e5c74827076e614dc5c7af9b1c71cd2004fdf9b3695a1b8c5e6b35663
  automorphisms.automorphism_group_order: 4fce296a7703b6df364c911b0772ceb8e25c47fb9b1c5619c3f68cda3b829c5f
  automorphisms.automorphism_group_generator_morphisms: a3832d266b8f5a2fd0563cc0efd6eae948daa8df04cdf4420134a281fe30d37d
  integral.primitive_orbits: e77d5e0c565cd3153166882e71a547f23742cfb3c80064e0ce543262a525a15f
  integral.modular_scale: 7b122c73ba347ebc082ba7ad8a6a57fd9512ca25a6cad2aa3ab770d8ccdfb25d
  integral.anisotropic_primes: ab4b568d9cf27ca270178646abf9c7f0a770e8ad5c0b6db9479cb290003bf120
  integral.local_representations: 53af52ba6f105cd0dd028cdafd48646af26eeaa79aa4a98dbcc889b7e2fa173d
  integral.local_densities: e745e8c85e3ff0e1a40aad200f831371b2089e2a2baa7f6218cd1eab8713d20d
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -2, 1, 0, 0]
- [0, 1, -2, 1, 1]
- [0, 0, 1, -2, 0]
- [0, 0, 1, 0, -2]
signature: [1, 4]
determinant: 4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -1, -1, -1/2, -1/2]
- [0, -1, -2, -1, -1]
- [0, -1/2, -1, -1, -1/2]
- [0, -1/2, -1, -1/2, -1]
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
  genus_symbol: 'I_{1,4} (2: [1^3]_5 2^2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  primitive_orbits:
    O:
      constant: 1
      z: []
      w: []
    O+:
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
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1/4, 3/2, 3/2, 13/32, 3/4, 3/2, 3/2, 9/16]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 4RCJ
  name: O(L) generator 1
  matrix:
  - [5, -2, 2, 2, -6]
  - [2, 0, 1, 1, -3]
  - [2, -1, 2, 1, -3]
  - [0, 0, 0, 1, 0]
  - [4, -2, 2, 2, -5]
  scale: 1
- target: 4RCJ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -1, 0, 1]
  - [0, 0, -1, 0, 2]
  - [0, 0, -1, 1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4RCJ
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 1, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4RCJ
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, -1, 0]
  - [0, 0, 1, -2, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, -1, 1]
  scale: 1
- target: 4RCJ
  name: O(L) generator 5
  matrix:
  - [3, 2, -2, 2, -2]
  - [0, 1, 0, 0, 0]
  - [2, 2, -1, 2, -2]
  - [0, 0, 0, 1, 0]
  - [2, 2, -2, 2, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3IF8.
- tag: 3IF8
  relation: This presentation is obtained by orthogonal sum of 0001, 3IF8.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3IF8.
