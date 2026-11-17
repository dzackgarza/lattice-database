---
tag: 4IAH
name: Constructed lattice 4IAH
latex: L_{\mathrm{4IAH}}
certifications:
  derive: f3c72a96326206221fff948014df4bcc46395f4cf14526f07fb39067c190d1ab
  form.integer_valued: 22e7946dbfc01e71a78b874cbcab1ff2e590f219498b7cb9d5125731bedda18e
  integral.elementary_primes: 9d7f106c84978d97c67741bd8f5fc7c7c22753d80b266989983df98d533ea6e3
  integral.genus_symbol: 90843d45e7dc067e110f27c2bb7ff5c89ff1f8e750f78bb86ee46e1b39db437f
  integral.genus_class_count: 28c969b2322279755c3bb4adc3593cbe9985b3a8cd3532e26427e372eaa09381
  integral.overlattice_count: f8dbe3b36d2f03679c5e47adf52068f4a816bd2e6c713377416ca27704be71f1
  integral.spinor_genus_count: cb8ddf530885e52bcfdfcdec6f913d9c17fc5dac10ef3afefdcc43f440c53edd
  integral.spinor_genera: 58147a9efbbaa84af9c86f99b80762b84c28415c4887e0699bfa121a3115a0c9
  integral.hyperbolic_index: 24d22f54b087cb01f6b35ff550dfcf078331dfa1e338b3884e735072c61fbad0
  definite.automorphism_group_order: 93f53e25951411523bde37f74d33d208ee5915571cf1da4fe14f5e8cc69050ee
  definite.automorphism_group_generator_morphisms: b378540af9109ca808c9649f1a50f24cd319852fcbbe9d88f7689335140b8b98
  integral.primitive_orbits: 56b7d7831d2f95b91487d216c8f5132bd91b10dd013158b3de621d293d1e2896
  integral.modular_scale: 197fd75c7754a420906eecc2edf977ae03821b49b3972bca95469c8fc393aef0
  definite.genus_theta_series: 1eb87206462b952004f36a3edef668caaad56b3aa4854a3cea8332911940647a
  definite.theta_series_cuspidal_component: dfb675b355c3378b44e63637fb114de22164d2fab13a500012c994c404cab981
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, 2, 0, 0]
- [0, 0, 4, -6]
- [0, 0, -6, 12]
signature: [4, 0]
determinant: 24
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, 1/2, 0, 0]
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
  quadratic_character: 24
  genus_symbol: 'I_{4,0} (2: [1^-1 2^3]_6; 3: 1^-3 3^1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [1, 1, 1, 1]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [1, 1, 1, 1]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [1, 1, 1, 6]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [1, 1, 2, 6]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [1, 1, 1, 1]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [1, 1, 1, 1]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [1, 1, 2, 6]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [1, 1, 2, 6]
      w: [0, 0, 0, 0]
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 48
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 2, 4, 8, 12, 16, 24, 14, 6, 24, 4, 22]
  genus_theta_series: [1, 4/3, 10/3, 10/3, 28/3, 12, 40/3, 24, 34/3, 28/3, 24, 20/3, 70/3]
  theta_series_cuspidal_component: [0, 2/3, -4/3, 2/3, -4/3, 0, 8/3, 0, 8/3, -10/3, 0, -8/3, -4/3]
  root_system: [A1]
  roots:
  - type: G2
    scale: 2
    simple_roots:
    - [0, 0, 1, 0]
    - [0, 0, 0, 1]
  - type: A1
    scale: 1
    simple_roots:
    - [0, 1, 0, 0]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1]
  norms: [1, 2, 4]
morphisms:
- target: 4IAH
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4IAH
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4IAH
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 2, -3]
  - [0, 0, 1, -1]
  scale: 1
- target: 4IAH
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, -3]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ID6.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0002, 3ID6.
