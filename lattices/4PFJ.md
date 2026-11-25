---
tag: 4PFJ
name: Constructed lattice 4PFJ
latex: L_{\mathrm{4PFJ}}
certifications:
  derive: 0337a986f4b98948a85c540ac44816ce80a242f6692f4f9bdee77050f61ef6a0
  form.integer_valued: 7100a555b0de0783474aa45fe8c285789e80871760ec3c4919a0f3e14d0076f2
  integral.elementary_primes: f3cbdc38f7333a31beedeea5d198780e752af51c3c96c40337ae660c4db3b5af
  integral.genus_symbol: 66a9233019604d3a193a0124e56d02d7f6347f1fb67a0a4cc64087b9afd8ebe7
  integral.genus_class_count: 8b8ce7a0209d92d4fadbab3c6052c0d60d0d0367a442fa78d410f06a238e475a
  integral.overlattice_count: 7589fbfafa7050b77f41fe348d7060ff9c02ed4da63d04f1cdbe18e82fe38dfc
  integral.spinor_genus_count: 6602f6a7768e5b63a3724d90c996d1fdf9b8f4f63a9f7a39b6f4c132cfa2dadc
  integral.spinor_genera: 31da5fa9e6f2335ff01a1a690f98825dc0e2140e39b16e3e90760caccb22c42c
  automorphisms.automorphism_group_order: c9c8bac902377c337f2c99fcaf3e02cc82bb626f4634d1e5e8cdb876c68dff71
  automorphisms.automorphism_group_generator_morphisms: d76c59efbf7568ad96be4dc2c9f33e82a36b19632edca084203e3d4be7f35139
  integral.modular_scale: 352f5ef02a70d951c75213cb4cb311aefba1aa6e472d09ca08b367a15985854e
  integral.anisotropic_primes: 54e6ae4481f5332a50230a4230063010a19a4c76b9063c2421e33ff04c8f8a5f
  integral.local_representations: e2667c7746c6e9fad38d68dc870f501befb86475f7dcf252c7fc5bf24a811476
  integral.local_densities: c2583a5c7f3c8f822d4f898e96dedf8a0536ea5176506a24e0ff839b25651f6e
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -2, 1, 0, 0]
- [0, 1, -2, 0, 0]
- [0, 0, 0, 2, -1]
- [0, 0, 0, -1, 2]
signature: [3, 2]
determinant: 9
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -2/3, -1/3, 0, 0]
- [0, -1/3, -2/3, 0, 0]
- [0, 0, 0, 2/3, 1/3]
- [0, 0, 0, 1/3, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [3, 3]
  overlattice_count: 3
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{3,2} (2: [1^5]_1; 3: 1^-3 3^-2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [11/8, 3/4, 3/4, 83/64, 9/8, 3/4, 3/4, 39/32]
  - prime: 3
    densities: [4/3, 2/3, 26/27, 4/3, 2/3, 26/27, 4/3, 2/3]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17, O(L) generator 18, O(L) generator 19, O(L) generator 20, O(L) generator 21, O(L) generator 22, O(L) generator 23, O(L) generator 24, O(L) generator 25, O(L) generator 26, O(L) generator 27, O(L) generator 28, O(L) generator 29, O(L) generator 30, O(L) generator 31, O(L) generator 32, O(L) generator 33, O(L) generator 34]
indefinite:
  isotropic: true
morphisms:
- target: 4PFJ
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 3
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 2, 2, -1]
  - [0, 2, 0, 1, -2]
  - [0, -2, 1, 0, 2]
  - [0, -1, 2, 2, 0]
  scale: 1
- target: 4PFJ
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 6
  matrix:
  - [1, -2, -2, 2, 2]
  - [-2, 3, 2, -2, -2]
  - [0, 1, -1, 0, 0]
  - [0, 0, 0, -1, 1]
  - [-2, 2, 2, -2, -1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 2, 1, -2]
  - [0, 2, 0, -1, -1]
  - [0, -1, -1, 0, 2]
  - [0, -2, 1, 2, 0]
  scale: 1
- target: 4PFJ
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 2, 0, -1, -1]
  - [0, 0, 2, -2, 1]
  - [0, -1, -1, 2, 0]
  - [0, -2, 1, 0, 2]
  scale: 1
- target: 4PFJ
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, -1, 1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 4PFJ
  name: O(L) generator 11
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 12
  matrix:
  - [-3, 2, 2, 0, 0]
  - [-2, 1, 2, 0, 0]
  - [0, -1, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 13
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 14
  matrix:
  - [3, 2, 2, 0, 0]
  - [0, 1, -1, 0, 0]
  - [2, 2, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 15
  matrix:
  - [-1, 2, 2, -2, -2]
  - [-2, 3, -2, 0, 0]
  - [0, 1, 3, -2, -2]
  - [0, 0, 0, 1, -1]
  - [-2, 2, -4, 2, 1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 16
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 4PFJ
  name: O(L) generator 17
  matrix:
  - [1, 2, 2, -2, -2]
  - [0, -1, 1, 0, 0]
  - [-2, -3, -2, 2, 2]
  - [0, 0, 0, -1, 1]
  - [2, 2, 2, -2, -1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 18
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 4PFJ
  name: O(L) generator 19
  matrix:
  - [1, -2, -2, -2, -2]
  - [2, 0, -4, -3, 0]
  - [0, 2, 0, 1, 1]
  - [0, -1, -1, -2, 0]
  - [-2, 0, 3, 2, 0]
  scale: 1
- target: 4PFJ
  name: O(L) generator 20
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 2, 0, -1, 2]
  - [0, 0, 2, -2, 1]
  - [0, -2, 1, 0, -2]
  - [0, -1, 2, -2, 0]
  scale: 1
- target: 4PFJ
  name: O(L) generator 21
  matrix:
  - [-1, -2, -2, -2, -2]
  - [0, 1, -1, 0, 0]
  - [2, 3, 2, 2, 2]
  - [2, 2, 2, 1, 2]
  - [0, 0, 0, -1, 1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 22
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -2, 1, -2]
  - [0, -2, 0, -1, -1]
  - [0, -1, -1, 0, -2]
  - [0, -2, 1, -2, 0]
  scale: 1
- target: 4PFJ
  name: O(L) generator 23
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 4PFJ
  name: O(L) generator 24
  matrix:
  - [1, -2, -2, -2, -2]
  - [0, 0, -2, -1, -1]
  - [-2, 4, 0, 0, 3]
  - [2, -3, 0, 0, -2]
  - [0, 1, 1, 0, 2]
  scale: 1
- target: 4PFJ
  name: O(L) generator 25
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -2, 0, -1, 2]
  - [0, 0, -2, 1, 1]
  - [0, -1, 2, -2, 0]
  - [0, 1, 1, 0, -2]
  scale: 1
- target: 4PFJ
  name: O(L) generator 26
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 7, -3, 0, -6]
  - [0, 0, 1, 0, 0]
  - [0, 4, -2, -1, -3]
  - [0, 8, -4, 0, -7]
  scale: 1
- target: 4PFJ
  name: O(L) generator 27
  matrix:
  - [3, 4, 4, -6, 0]
  - [0, 1, -4, 4, -2]
  - [4, 8, 1, -4, -4]
  - [2, 4, -2, 1, -3]
  - [-2, -4, -4, 6, 1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 28
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 29
  matrix:
  - [-3, -2, -2, 0, 0]
  - [0, 1, -1, 0, 0]
  - [-2, -1, -2, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 30
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, -3, -4, 6, 0]
  - [0, -2, -2, 3, 1]
  - [0, 2, 2, -4, 1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 31
  matrix:
  - [-1, -4, 2, 2, 2]
  - [0, 4, -1, -2, -2]
  - [2, 1, -3, 0, 0]
  - [0, 0, 0, -1, 1]
  - [-2, 2, 2, -2, -1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 32
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PFJ
  name: O(L) generator 33
  matrix:
  - [105, 214, -218, 72, -198]
  - [-146, -298, 304, -99, 276]
  - [-30, -62, 62, -21, 57]
  - [-70, -144, 147, -48, 134]
  - [-128, -261, 267, -86, 242]
  scale: 1
- target: 4PFJ
  name: O(L) generator 34
  matrix:
  - [1, 4, -2, -2, -2]
  - [2, 5, -3, -2, -2]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 1]
  - [2, 4, -2, -2, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID0, 0012.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID0, 0012.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID0, 0012.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ID0, 0012.
