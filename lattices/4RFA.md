---
tag: 4RFA
name: Constructed lattice 4RFA
latex: L_{\mathrm{4RFA}}
certifications:
  derive: 2cd7159f0b177949774044a19e6727a0b059ca5993acd09009d463f47d7242df
  form.integer_valued: 0c6db3cae7febecc063699e49773caeca82a08a694cd3c10935041b99240c9b4
  integral.elementary_primes: fda1ae48ce670c924ab20527b152701d764eb4f71b25d80e099cc5bb971619a0
  integral.genus_symbol: 2dc12764f2a8a890f2b8e4ff990b6bd456582ff8e12b6b3fbd077304ca314cb4
  integral.genus_class_count: 5e0e113590eaaa95f762d5d60668939af7e79696679231fbf77696e9619b843c
  integral.overlattice_count: 5176263f5f273fc015d4e441e38d90d38f420c6a27b6665350310a11072a1763
  integral.spinor_genus_count: c75d9f3ff3ced30357af9553c148c0a15fd3a1f5b9baccf568f869834726bb9d
  integral.spinor_genera: dedf5f34a3b17262a7734ea063471838fa67b314839425072a1223753d7ce7c3
  integral.hyperbolic_index: 6b30ab6a3926fd25da78beadd4714e51ba5de03dc9105fee7746c947a192fa60
  definite.automorphism_group_order: 8faedb8c3f9ab8e257d275c831cf19908a1c47b106efc99de98edf06fd670fc8
  definite.automorphism_group_generator_morphisms: de6f1b4d8ad6304a458a1038a7596e0c7ec90eed8af0a5a78f83b812eb337721
  integral.discriminant_sequence: cbf3129800fef2698a29dd96a1874eb3c5e4b6e4f7fc74d88f3bbaee43794d2b
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, -1, 0]
- [0, 0, 0, 0, -1]
signature: [0, 5]
determinant: -1
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, -1, 0]
- [0, 0, 0, 0, -1]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 2
  discriminant_group: []
  discriminant_sequence:
    discriminant_factors: []
    discriminant_basis_lifts: []
    discriminant_quadratic_gram: []
    discriminant_group_order: 1
    discriminant_generators: []
    image_generators:
    - []
    - []
    - []
    - []
    - []
    image_order: 1
    kernel_order: 3840
    coset_representatives:
    - []
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: []
    quotient_multiplication:
    - [0]
  overlattice_count: 1
  bad_reduction_primes: [2]
  genus_symbol: I_{0,5}
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 10
  automorphism_group_order: 3840
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 10, 40, 80, 90, 112, 240, 320, 200]
  root_system: [D5]
  roots:
  - type: B5
    scale: -1/2
    simple_roots:
    - [1, -1, 0, 0, 0]
    - [0, 1, -1, 0, 0]
    - [0, 0, 1, -1, 0]
    - [0, 0, 0, 1, -1]
    - [0, 0, 0, 0, 1]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [-1]
morphisms:
- target: 4RFA
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4RFA
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 4RFA
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  - [0, 0, 1, 0, 0]
  scale: 1
- target: 4RFA
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 1, 0, 0, 0]
  scale: 1
- target: 4RFA
  name: O(L) generator 5
  matrix:
  - [0, 0, 0, 0, 1]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [1, 0, 0, 0, 0]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICW, 3ICW, 3ICW.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICW, 3ICW, 3ICW, 3ICW.
