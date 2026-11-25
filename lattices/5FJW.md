---
tag: 5FJW
name: Constructed lattice 5FJW
latex: L_{\mathrm{5FJW}}
certifications:
  derive: 4841e979c8b1b1272bf93e2420a2c4a36d53bf18229d8e7b324ecdb7411c8f15
  form.integer_valued: 8847e2138bededadadc347f184dbb034d3356e3e221a3a1de8607e7bbfc92c1d
  integral.elementary_primes: 58f59f8cf2f91549d3e6dc4358f50d34a1423f8872133898206e04b54d9940a1
  integral.genus_symbol: 4ca4910787a77d412b00777f16b830871f86d3e34da50ae33070ed657a0e23e9
  integral.genus_class_count: 6eb0514bea55196578173d71e99158508d9ffda99114a85cdeb1c803c51cc209
  integral.overlattice_count: a3686e32a80172af9669dca7aa2b35d46a23a812c5d6d26c13505bd8363f5236
  integral.spinor_genus_count: e655b857b36b22154832d887a2977eb35a3baee3eb6dfa6fbb9a3a48f37a23ab
  integral.spinor_genera: 4be114bf8049b727b44efd6b9feac8df1d96154d01a8a0a5adc1782c032947cb
  integral.hyperbolic_index: 98d8b069f50069925e990aefc6d98293ef8d78b261af7c8919d47ee98ddd318b
  automorphisms.automorphism_group_order: 89994558c62d599153b6104d87aa7dba6926ea53320ad9d502fd0825e18d16d4
  automorphisms.automorphism_group_generator_morphisms: 3f4c874f1a31b83b3615ae0d879acf55b69a6e23e8462efe53a6f9b45deea333
  integral.primitive_orbits: 2f95fcfdb9b1bde5e04c33bdbaf12e4812a217aa015dcc90233fa3684f39316b
  integral.modular_scale: 0550cd2a1fe5435e61f98ec47aa61194bc9835117698993ab612742d5a8c1aa6
  integral.anisotropic_primes: 82c091dce728e61609a280f746dcacfd1df5745f3177763f5bc1b0b0b0f2ec06
  integral.local_representations: dfec1686a7575a12c97771e7ae279ffebd1163e309d76a5c7dec549575f34bc8
  integral.local_densities: a8bd035366fb15deb6b466220435b12fedd353e4f9946fdd9ef2b96c2972769d
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 0, -4, 2]
- [0, 0, 0, 2, -4]
signature: [1, 4]
determinant: 48
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 0, -1/3, -1/6]
- [0, 0, 0, -1/6, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [2, 2, 2, 6]
  overlattice_count: 31
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{1,4} (2: [1^-1]_3 2^4; 3: 1^-4 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
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
    SO+:
      constant: 1
      z: []
      w: []
    Otilde:
      constant: 15
      z: []
      w: []
    Otilde+:
      constant: 15
      z: []
      w: []
    SOtilde:
      constant: 15
      z: []
      w: []
    SOtilde+:
      constant: 15
      z: []
      w: []
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 3
      least_valuation: 0
    - representative: 5
      least_valuation: 2
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
  local_densities:
  - prime: 2
    densities: [0, 0, 5/2, 15/8, 0, 0, 3/2, 15/8]
  - prime: 3
    densities: [10/9, 10/9, 20/27, 10/9, 10/9, 22/27, 10/9, 10/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7]
indefinite:
  isotropic: true
morphisms:
- target: 5FJW
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5FJW
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FJW
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 1, 1, 1, 1]
  - [0, -1, 0, 0, -1]
  - [0, -1, 0, -1, 0]
  scale: 1
- target: 5FJW
  name: O(L) generator 4
  matrix:
  - [-1, -2, -2, -4, 2]
  - [1, 2, 1, 2, -1]
  - [1, 1, 2, 2, -1]
  - [-1, -1, -1, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FJW
  name: O(L) generator 5
  matrix:
  - [1, 2, 0, 0, 0]
  - [1, 1, 1, 0, 0]
  - [1, 2, 1, 1, 1]
  - [-1, -1, -1, 0, -1]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5FJW
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 5FJW
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0013, 3ID1.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0013, 3ID1.
- tag: 3ID1
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0013, 3ID1.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 0013, 3ID1.
