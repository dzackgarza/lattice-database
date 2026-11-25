---
tag: 4MHX
name: Constructed lattice 4MHX
latex: L_{\mathrm{4MHX}}
certifications:
  derive: eb71fdb97a8ef17036f8f45f6da360d1cc041604c5ef484e52fda8e691aff81f
  form.integer_valued: 4051369f96552620f733d7422aab03af347e28de585cd37a0587fa291adc4099
  integral.elementary_primes: 2e51ac95e40ff2cbdb2c62d6744b5512e2249f86809c68ab0a7a5636ec9153e5
  integral.genus_symbol: b67d90c7297f27c3f4e68f6c5551fe9d25dddd204a2dcf7c28cacbec1323d89b
  integral.genus_class_count: d6c0deae0522ee7b09cba07fcc480dce039c0eb395ba23f5e31d8225bd4ce682
  integral.overlattice_count: 88b82f322ce6c66849c8ea06958460b28eb68fd064cea0d72d305f7e42ea7447
  integral.spinor_genus_count: 5ab3ce83bd1bcbd2c3335e92408476fdfb9a78f1ec1be9eb773327dfaf307e01
  integral.spinor_genera: e68362c5f55351e3cc7338be4584d9c3903364f5fa9b97128742f697302c2d05
  integral.hyperbolic_index: d48b69defff8da8caec9ea117da3e37e871e1527999237801946ee718c0f5f71
  automorphisms.automorphism_group_generator_morphisms: d4195f1fd5bf1daf80618ed8438f0c63d17bd1c847af4bc5d849027f1ccfe4b1
  automorphisms.automorphism_group_order: 09247a339a9419596b640d720a691e02a3e4a9db6bbfcadd83b8724e3c9fc26f
  integral.modular_scale: 4579f026ad39d0a6a88052d599c51f7cd5ef63f234b19f595a08008b144be8bd
  integral.anisotropic_primes: de3f12c020373b949b5f9fbc837068209bbd12ecc5de49cfdb4ff1f2f2ef5fec
  integral.local_representations: 4d23416bea5c91d8a71462dee65205f0c4baa9c4ca0c20d30c1a8853752a8d71
  integral.local_densities: 694b08317f61b7f32dfc3092dd33ca0da9c61b27757c4ba0a59c05b6cee673c8
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, 4, -6]
- [0, 0, -6, 12]
signature: [3, 1]
determinant: -24
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, 1, 1/2]
- [0, 0, 1/2, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  modular_scale: false
  discriminant_group: [2, 2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  quadratic_character: -24
  genus_symbol: 'I_{3,1} (2: [1^-1 2^3]_4; 3: 1^3 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1/2, 5/4, 3/2, 7/8, 3/2, 3/4, 1/2, 17/16, 1/2, 3/4, 3/2, 9/8]
  - prime: 3
    densities: [2/3, 4/3, 10/9, 2/3, 4/3, 8/9, 2/3, 4/3, 26/27, 2/3, 4/3, 10/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: ['O(L) generator 1 #2', 'O(L) generator 2 #2', 'O(L) generator 3 #2', O(L) generator 4, O(L) generator 5, 'O(L) generator 6 #2', 'O(L) generator 7 #2', O(L) generator 8]
indefinite:
  isotropic: true
morphisms:
- target: 4MHX
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, -1, 1]
  scale: 1
- target: 4MHX
  name: O(L) generator 2
  matrix:
  - [-31, -48, 24, -48]
  - [24, 37, -18, 36]
  - [0, 0, 1, 0]
  - [-4, -6, 3, -5]
  scale: 1
- target: 4MHX
  name: O(L) generator 3
  matrix:
  - [-15, -24, 8, -24]
  - [12, 19, -6, 18]
  - [-4, -6, 3, -6]
  - [-4, -6, 2, -5]
  scale: 1
- target: 4MHX
  name: O(L) generator 4
  matrix:
  - [-17, -24, 0, 0]
  - [12, 17, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4MHX
  name: O(L) generator 5
  matrix:
  - [-3, -4, 0, 0]
  - [2, 3, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4MHX
  name: O(L) generator 6
  matrix:
  - [-31, -48, 24, -48]
  - [24, 37, -18, 36]
  - [-12, -18, 8, -15]
  - [-8, -12, 5, -10]
  scale: 1
- target: 4MHX
  name: O(L) generator 7
  matrix:
  - [-21, -36, 28, -48]
  - [18, 31, -24, 42]
  - [-4, -6, 3, -6]
  - [-6, -10, 7, -13]
  scale: 1
- target: 4MHX
  name: O(L) generator 8
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 4MHX
  name: 'O(L) generator 1 #2'
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 3]
  - [0, 0, 0, 1]
  scale: 1
- target: 4MHX
  name: 'O(L) generator 2 #2'
  matrix:
  - [-31, -48, 0, 24]
  - [24, 37, 0, -18]
  - [12, 18, 1, -9]
  - [8, 12, 0, -5]
  scale: 1
- target: 4MHX
  name: 'O(L) generator 3 #2'
  matrix:
  - [-15, -24, 8, 0]
  - [12, 19, -6, 0]
  - [8, 12, -3, 0]
  - [4, 6, -2, 1]
  scale: 1
- target: 4MHX
  name: 'O(L) generator 6 #2'
  matrix:
  - [-31, -48, 0, 24]
  - [24, 37, 0, -18]
  - [12, 18, -1, -6]
  - [4, 6, -1, -1]
  scale: 1
- target: 4MHX
  name: 'O(L) generator 7 #2'
  matrix:
  - [-21, -36, -8, 36]
  - [18, 31, 6, -30]
  - [14, 24, 3, -21]
  - [8, 14, 2, -13]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ID6.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICX, 3ID6.
