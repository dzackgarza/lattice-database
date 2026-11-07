---
tag: 3IDQ
name: Constructed lattice 3IDQ
latex: L_{\mathrm{3IDQ}}
certifications:
  derive: ffff7330b50ea056c4541ccb6ef691a613608d7a6a8c5292cde409d22025c07f
  form.integer_valued: a561b0aaf8c7ad384d083ae36da7b0c49e8cd1dbb45ef494fd91a9315f5f6277
  integral.elementary_primes: 8489cab695ecc70002e1dd2b5c92219c0b3ec3d2aba916731319d6400fa83ece
  integral.genus_symbol: 421bc33759e34d536b1c2dea76ebf33a9b76ddf43738082944c2abb563888b1f
  integral.genus_class_count: e6e17b6053f7acb773fd75ab87fea4e9781cd1b251787aa581317d85714e2fd0
  integral.overlattice_count: 6a1648068b7be1a95ddb850701b0479951f642a4fa78853c545581770a243d9d
  integral.spinor_genus_count: 7f996c9da6bb99946f2fa0143406bab08ebd2d5e9227f0c25b6914ad784c2c5d
  integral.spinor_genera: b76f532d73c0628902aade1814c6652a9941a8d384126b25e82adeed716b48a6
  integral.hyperbolic_index: 1d44c98878dfc83e099c4c4fd2a1119b9191a8520cac592e7f819d7c11fa84f5
  automorphisms.automorphism_group_generator_morphisms: 9a490ac97fc507c6536c42391621b3e26bb4e99d6e26d6e65ff27cedd176a0f3
  integral.primitive_orbits: 6300a72c22eec6ec9cef8d71fe88fb7149fe523d4a402ab2940e42b66579eff7
  integral.modular_scale: ed75e561a2e56a81b9d12f23b189cbe515019c133958ce92e621d859757f28a5
  integral.anisotropic_primes: 72c828ddac3d98c5b22d7882973a668e1170e9e63b26e7a9ea63c0f7301a6d89
  integral.local_representations: 8a2926609f6e0b9af4b6a345c944837d6cfb01ba87cad5661e1d6a5755c06ae6
  integral.local_densities: 1e535f915c4a766ad0f1d576fdcdcb00eba125916493b69d29af9df284d8624a
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, -4, 6]
- [0, 6, -12]
signature: [1, 2]
determinant: 12
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, -1, -1/2]
- [0, -1/2, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{1,2} (2: [1^-1]_5 2^2; 3: 1^-2 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  primitive_orbits:
    O:
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
    O+:
      constant: 1
      z: []
      w: []
    SO+:
      constant: 1
      z: []
      w: []
    Otilde+:
      constant: 3
      z: []
      w: []
    SOtilde+:
      constant: 6
      z: []
      w: []
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 2
    - representative: 5
      least_valuation: 0
    - representative: 7
      least_valuation: 2
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
    densities: [1, 0, 0, 2, 3, 0, 0, 3/2, 1, 0, 0, 3/2]
  - prime: 3
    densities: [2/3, 2/3, 4/3, 2/3, 2/3, 2, 2/3, 2/3, 14/9, 2/3, 2/3, 4/3]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IDQ
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 2, -3]
  - [0, 1, -2]
  scale: 1
- target: 3IDQ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 3]
  - [0, -1, 2]
  scale: 1
- target: 3IDQ
  name: O(L) generator 3
  matrix:
  - [7, 12, -12]
  - [-6, -11, 12]
  - [-2, -4, 5]
  scale: 1
- target: 3IDQ
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID5.
- tag: 3ID5
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID5.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ID5.
