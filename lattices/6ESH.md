---
tag: 6ESH
name: Constructed lattice 6ESH
latex: L_{\mathrm{6ESH}}
certifications:
  derive: ec73133cff7193c590bc7a6816efa3c8a8df2c6776ef88b87bd034f26edc5a72
  form.integer_valued: 2c58cb1ea0669e0f3dd81c57749b8e9d7ec09799f8b1e873c250bdc8793eb4af
  integral.elementary_primes: 2315d6c9011646d9726464bc11f920435109377c5cf087b2f78a6ad803f10c65
  integral.genus_symbol: d42cb2280ffa78f703543da7c528a7bffe49cc140911fe89432d7293bdd88b9f
  integral.genus_class_count: 5ce7d4623c74112cb1589914e1ea7b5f31152fc28f7add74f83db421b11eb1ed
  integral.overlattice_count: f535fb3358380ed338a08fc51172d643c57730d065a8fffc40152e6409c0d231
  integral.spinor_genus_count: 13d9c4444022a5c30b11bed7ec5cfdb486a07d62306ad651158aff5899df0363
  integral.spinor_genera: 10858d9ef5b7b30d4585da1e395dac3ef517b66dc0f39a0a7cc928718862d372
  integral.hyperbolic_index: 94bd5cf8ac37997a4e46c08091723a4fe7ee0cbf5b0ccd8a186960f72fa2331e
  automorphisms.automorphism_group_order: e3b3e932f65acea2d75abab6ed709020aceb452eed2467897996540f5d1147bf
  automorphisms.automorphism_group_generator_morphisms: 3b538b2871f998f138e6173467c696c207fa96c042d237754b5e6c41a55bfc71
rank: 4
gram_tensor:
- [0, -2, 0, 0]
- [-2, 0, 0, 0]
- [0, 0, 2, -3]
- [0, 0, -3, 6]
signature: [3, 1]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [0, -1/2, 0, 0]
- [-1/2, 0, 0, 0]
- [0, 0, 2, 1]
- [0, 0, 1, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 6
  discriminant_group: [2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{3,1} (2: 1^-2:2^2; 3: 1^3 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
indefinite:
  isotropic: true
morphisms:
- target: 6ESH
  name: O(L) generator 1
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6ESH
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 2, -3]
  - [0, 0, 1, -2]
  scale: 1
- target: 6ESH
  name: O(L) generator 3
  matrix:
  - [2, 1, 1, 0]
  - [1, 2, 1, 0]
  - [-4, -4, -3, 0]
  - [-2, -2, -2, 1]
  scale: 1
- target: 6ESH
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [2, 1, 1, 0]
  - [-4, 0, -1, 0]
  - [-2, 0, -1, 1]
  scale: 1
- target: 6ESH
  name: O(L) generator 5
  matrix:
  - [0, 1, 0, 0]
  - [1, 2, 1, 0]
  - [0, 2, 2, -3]
  - [0, 2, 1, -1]
  scale: 1
- target: 6ESH
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 3ICZ, 3ID4.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 3ICZ, 3ID4.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICZ, 3ID4.
