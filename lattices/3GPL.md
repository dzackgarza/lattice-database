---
tag: 3GPL
name: watson 4:170
latex: watson 4:170
aliases: []
certifications:
  derive: 32ffbfa23bf218c592ef6a33ba8aa5e0be8bf150807d6d07dae915da4ef60bb5
  form.integer_valued: a16d0632eeebd1aaaa7f6207170d50e02f4f270fad2e81725fb1b3e4d2288e26
  integral.elementary_primes: 5aa1bc6d2e9ae43add7a68a1b8ae8194a7bb7d1d4736b6dd443ae6e88789b2b2
  integral.genus_symbol: 0a28be464587f4eec10c7eb08c4d5c3b5ade7009ef8637eedabb37576625d28c
  integral.genus_class_count: f3e8b9ce4aad7b2dc25962d3d55df6cc05990d91e29e4766a0fd8e1e1cd203be
  integral.overlattice_count: 10f0e66bb05c14cfea8b57bc6388b0b98fc5bdf37d86bfa9b12d377b0c03848d
  integral.spinor_genus_count: 9206e84c054e55382700ffe3c13ddd1c173382747bb3ec215af4a54e478beb85
  integral.spinor_genera: ca8c7f89d8ccf4d17cbd5de480b0a979a9e94de84083abc9e8c248ae1c44ebcd
  integral.hyperbolic_index: 2ab4100d3bf06bc098775d83afc94bf7068436297c716d722e0bc5f68ac6f937
  definite.automorphism_group_order: 5923f8f0c54849678d3675f177fc85210fcdb77f2fc47cb53450e9bd7556112e
  definite.automorphism_group_generator_morphisms: 86a9cb702961abe29328db863aa15bbcd29666ff886dde0227d766be50f09604
rank: 4
gram_tensor:
- [2, -1, 0, -1]
- [-1, 8, -3, 2]
- [0, -3, 12, -6]
- [-1, 2, -6, 26]
signature: [4, 0]
determinant: 3645
definiteness: positive_definite
dual_gram_tensor:
- [74/135, 2/27, 4/135, 1/45]
- [2/27, 4/27, 1/27, 0]
- [4/135, 1/27, 14/135, 1/45]
- [1/45, 0, 1/45, 2/45]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 135
  discriminant_group: [3, 9, 135]
  overlattice_count: 6
  bad_reduction_primes: [2, 3, 5]
  quadratic_character: 5
  genus_symbol: 'II_{4,0} (2: 1^-4; 3: 1^-1 3^1 9^1 27^1; 5: 1^-3 5^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
definite:
  minimum: 2
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 2, 0, 0, 0, 0, 0, 6, 0, 0, 0, 6]
  root_system: [A1]
  roots:
  - type: A1
    scale: 1
    simple_roots:
    - [1, 0, 0, 0]
  - type: A1
    scale: 45
    simple_roots:
    - [1, 0, 1, 2]
root_sublattice:
  invariant_factors: [1, 1]
morphisms:
- target: 3GPL
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 3GPL
  name: O(L) generator 2
  matrix:
  - [1, -1, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 3GPL
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, -1]
  - [0, 1, 0, 0]
  - [0, 0, 1, -1]
  - [0, 0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 4:170.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:4:170` gives this Gram tensor.
