---
tag: 4BAQ
name: Constructed lattice 4BAQ
latex: L_{\mathrm{4BAQ}}
certifications:
  derive: 933a455058e8c95d5b23a8f8a37714034e6b5de54f1207422234457f3b312daf
  form.integer_valued: 87258fb6faad4ecc713f27f5228ea29af398205a15514c51a022e78fb3a79ed7
  integral.elementary_primes: afe9347f440f090f2c6bbe2f17d6b7195929e94ffe1babc3eb81313dca69ad66
  integral.genus_symbol: c3a0a366a5b868e8afa003585a479385b52882ab2cc924b143a527edb46d3ba7
  integral.genus_class_count: c6d16cd5c9b15cefeb8208cb4ed8cc06e194144cf3b032510600a8a1a48ddfd6
  integral.overlattice_count: cd75d9a0e16d9c559d44897812a3b16999cf0112e53130e99cc0370e724a5b57
  integral.spinor_genus_count: d1ade9d1d4a0d75f3e15e252ca81132eb2cea3d9727bd750f6d5ef980ede4486
  integral.spinor_genera: 98a0ab6144f0961bae0fd91b030c26fa2b9d53aac9c06b415af338f0d32964ac
  automorphisms.automorphism_group_order: 2fbd540110ca1605e6d318ae1c35ab58454cdcc5d767ed2e66970fddb4c4a50b
  automorphisms.automorphism_group_generator_morphisms: 8209fe41a802079243d1c01fad903e48a414e48ee7ca2483d0796664e4c381d6
  integral.primitive_orbits: fefb875c2553bf6ee7936017ab8329223c296002877ad721df5eeb818c135b6a
  integral.modular_scale: 464cfa89be534aa42530a94f64dbf996f036011c86ecd3e9077a47579d9fa606
  integral.anisotropic_primes: e6e3d396eca9a13dde6dd609daab61890400384d801c3317392607276d3bb38f
  integral.local_representations: 8ed004549aca1a852eb395395a0f65f9be92e98df808e827548151bba92591d6
  integral.local_densities: 47e53c6211847b8d41d547880d4dd439bec9728fd1ad5774a6b6a1ba21a025de
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, -1, 0, 0]
- [0, 0, 2, -3]
- [0, 0, -3, 6]
signature: [3, 1]
determinant: -3
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, -1, 0, 0]
- [0, 0, 2, 1]
- [0, 0, 1, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [3]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'I_{3,1} (2: [1^-4]_0; 3: 1^3 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
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
    Otilde+:
      constant: 1
      z: []
      w: []
    SOtilde:
      constant: 1
      z: []
      w: []
    SOtilde+:
      constant: 1
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1, 3/2, 1, 1/4, 1, 3/2, 1, 7/8, 1, 3/2, 1, 1/4]
  - prime: 3
    densities: [2/3, 4/3, 8/9, 2/3, 4/3, 10/9, 2/3, 4/3, 26/27, 2/3, 4/3, 8/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 4BAQ
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4BAQ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, -1, 1]
  scale: 1
- target: 4BAQ
  name: O(L) generator 3
  matrix:
  - [0, -1, -1, 3]
  - [1, 2, 1, -3]
  - [1, 1, 2, -3]
  - [1, 1, 1, -2]
  scale: 1
- target: 4BAQ
  name: O(L) generator 4
  matrix:
  - [-2, 3, 3, -6]
  - [-3, 4, 3, -6]
  - [0, 0, 1, 0]
  - [-1, 1, 1, -1]
  scale: 1
- target: 4BAQ
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID4.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID4.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID4.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICW, 3ID4.
