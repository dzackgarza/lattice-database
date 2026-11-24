---
tag: 5EPT
name: Constructed lattice 5EPT
latex: L_{\mathrm{5EPT}}
certifications:
  derive: 193111f346debd5da229dfe27d5f8d237cecc5f17149e60724e2bfeb17ca4045
  form.integer_valued: 14da272555ff9305a92fe08ab09a6761057e60f1005735468e6f2e33005d7384
  integral.elementary_primes: 478f8a370515b55d8ee7ba456a589831fa60e8f37d4785553cde0e19c6668311
  integral.genus_symbol: 0ae66b4baafe208fd38485445ca6ce4c285d4b0c83a1860956f7a0f34c9dc5f9
  integral.genus_class_count: 6af9e7a327888e7102bca47b3d0710a3126d48dcda604d5ab4b60bc55b8e773e
  integral.overlattice_count: a9de5a49c02befacf13366652b7bee7510869642965c158908c5a7ee8e23ea03
  integral.spinor_genus_count: b370b56259ed4cd305fde5096c544c258529a17edca7ecde2eec5567d81074d2
  integral.spinor_genera: 5297a3322ec0528877e70d8a6ed68ecdccbae0dfe4fad00a70d331263cd77aef
  integral.hyperbolic_index: 4e1fa6bf9861397d44bdbc6bd57d2941619a31de5b3e8090af961d242e976419
  automorphisms.automorphism_group_order: 8554f41da6e9cc3f939439b19b8ae5f6684664683257400502696a3da0ef03b8
  automorphisms.automorphism_group_generator_morphisms: 2211ad90106b63c3d88011d7b3b63182bdbd594329899e74cd83a6bbaa64fd2b
  integral.primitive_orbits: 642bdc86958d10619e980e7a025a014ff5c77fdc2f5a1f2c04e2dd3fc9b2a572
  integral.modular_scale: bf150521d1e7470e8a5a66c93091db452e80b7f163934e52f30ef1f9e3dd4400
  integral.anisotropic_primes: 38598dc5c430aea1c70ad28b469f1d3bd13b0ecb7958081f723a4a5ac73b154b
  integral.local_representations: 7c330f61741fddd4ff4dffbb7dc3fd2da5c596a4ecce92e435622ac002cb3431
  integral.local_densities: 974b60894fdafc09300f1545ae275e51adc89b9e5ebc240fb5d1564a151d9bcd
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 0, 0, -2]
- [0, 0, 0, -2, 0]
signature: [2, 3]
determinant: -4
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 0, 0, -1/2]
- [0, 0, 0, -1/2, 0]
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
  genus_symbol: 'I_{2,3} (2: [1^3]_7 2^2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
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
    Otilde:
      constant: 4
      z: []
      w: []
    Otilde+:
      constant: 4
      z: []
      w: []
    SOtilde:
      constant: 4
      z: []
      w: []
    SOtilde+:
      constant: 4
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1/2, 1/2, 5/4, 23/16, 1/2, 1/2, 7/4, 23/16]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17]
indefinite:
  isotropic: true
morphisms:
- target: 5EPT
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5EPT
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 2, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, -1, 0, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 2]
  - [0, 0, 1, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 7
  matrix:
  - [1, 0, 2, 0, 0]
  - [-2, 1, -2, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 2]
  - [0, -1, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 9
  matrix:
  - [1, 2, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [-2, -2, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 2, 0]
  - [0, 0, 0, 1, 0]
  - [0, -1, 0, 0, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 2, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 0, 0, -1, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0, 4]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-2, 0, 0, 1, -4]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 13
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5EPT
  name: O(L) generator 14
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 5EPT
  name: O(L) generator 15
  matrix:
  - [-1, 2, 0, 0, 0]
  - [-2, 2, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 16
  matrix:
  - [1, 0, 0, 2, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, -2, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 0, -1, -1, 1]
  scale: 1
- target: 5EPT
  name: O(L) generator 17
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICY, 3ICZ.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICY, 3ICZ.
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICY, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICY, 3ICZ.
