---
tag: 3UNX
name: Constructed lattice 3UNX
latex: L_{\mathrm{3UNX}}
certifications:
  derive: 6aa3ffe887c916d4a2317631ccc97741939ddb1a376e4e53ee5e3df3b0862fa2
  form.integer_valued: b6be847a742a4ff453a52b1b2ecebde3a3420e2608a2d4556231f7c4aea61056
  integral.elementary_primes: 8b6366dca31364a72f1732dd8776d6f7e90b39887df71f4bba5914ff9a3fa244
  integral.genus_symbol: cddcfdc3e299c01952d9df5880ba25e3abee9d42a709f3744883596d7d53970f
  integral.genus_class_count: 7784785f34513984de70c275b5c078814d9d0a16266c798f62e28c4e892bc977
  integral.overlattice_count: 0fceb066f0785bb132da0a8da1656b471b29e6575d089a5370ba8102e021ccf7
  integral.spinor_genus_count: f30c932ea4b294c1a3127693c75baf34e945f9048f66d233fb8112fecbb70a8f
  integral.spinor_genera: ef16ef88e164fff683720958604a950348254480d521245e07bc62227605b1f9
  automorphisms.automorphism_group_order: ab26005c8d0039653db84ad2f0550d88950aca5adf74501c6438da4cb929a16a
  automorphisms.automorphism_group_generator_morphisms: c6e94387af108b6fc7dbb288aaa5ba6889be23be34311c14328959ad272c50a9
  integral.primitive_orbits: 5a4982718959dc26a5bd711bae424c49b569f8a690604f655f212847f2956d75
  integral.modular_scale: 2c69de9a54781e04100e1acfbbcea41ddbe2dd3d1aae42da120ae421cd477cae
  integral.anisotropic_primes: d0a763cef1e1f6ad8de8f1fc8b9815695a2c5efabce8473152c49002a96f77f7
  integral.local_representations: 28c416bad6d7f3e5db8c1001d827140d768a9023302b073e9f6fc7adc8096c7a
  integral.local_densities: 869731e8e4d04f59a64b3f0c1f9068d3be5c3d709a31038841bcf5e11c5fbf5c
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, 1, 0, 0]
- [0, 0, 2, 0]
- [0, 0, 0, -2]
signature: [3, 1]
determinant: -4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, 1, 0, 0]
- [0, 0, 1/2, 0]
- [0, 0, 0, -1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: 2
  discriminant_group: [2, 2]
  overlattice_count: 2
  bad_reduction_primes: [2]
  quadratic_character: -4
  genus_symbol: 'I_{3,1} (2: [1^2 2^2]_2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  primitive_orbits:
    O:
      constant: 2
      z: []
      w: []
    O+:
      constant: 2
      z: []
      w: []
    SO:
      constant: 2
      z: []
      w: []
    SO+:
      constant: 2
      z: []
      w: []
    Otilde+:
      constant: 2
      z: []
      w: []
    SOtilde:
      constant: 2
      z: []
      w: []
    SOtilde+:
      constant: 2
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1, 3/2, 1, 5/4, 1, 1/2, 1, 9/8, 1, 3/2, 1, 3/4]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 3UNX
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3UNX
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3UNX
  name: O(L) generator 3
  matrix:
  - [-8, -3, 0, -12]
  - [-3, 0, 0, -4]
  - [0, 0, 1, 0]
  - [6, 2, 0, 9]
  scale: 1
- target: 3UNX
  name: O(L) generator 4
  matrix:
  - [-7, 0, 2, -10]
  - [0, 1, 0, 0]
  - [5, 0, 0, 7]
  - [7, 0, -1, 10]
  scale: 1
- target: 3UNX
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0002, 3ICX.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0002, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0002, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 0002, 3ICX.
