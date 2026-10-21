---
tag: 3IBE
name: Jagy–Kaplansky–Schiemann regular ternary form 878
latex: Jagy–Kaplansky–Schiemann regular ternary form 878
aliases: []
certifications:
  definite.regular: e0cc150d538efffeee1f6fc0a40d7ff136a51b3e84a04e857ca1108ca533ca44
  definite.spinor_regular: cae35d836c89c56b8ab05c625c2e37a13fcf51803676259b85e3171627216c81
  derive: d3be4054c63ac9dfdccbfad6508408a891803d1ea60c92c501e48ba8e502d50e
  form.integer_valued: ff9cb3ee420959c0724456d50458ff79a9a2c937b42a0b41a561580cd0bb352f
  integral.elementary_primes: 7f4b4c3ba81d097cafff09d508999aaa3043ab3a5948f369d10265b2605ebc1f
  integral.genus_symbol: 4f950a2b5dbde08cba93832d2742b86d184cb40f10989479907e358e318cdb64
  integral.genus_class_count: 12330cbff189255aeb3c7e54de2853a1641e757b1142d963087d24078af6106c
  integral.overlattice_count: 02bd44baecbecc58ae4920640618adc765540d9b7ac3d699ffe8afb622940058
  integral.spinor_genus_count: 4410c30fde8ff27cd4f4c390d284b5334ff17aa8548ef1576b0c846e8290194a
  integral.spinor_genera: bd923a04374e93ab7ed2c33806dd7a361700299a21564587d370e334fa36037a
  integral.hyperbolic_index: a6076da30d6719f77d1aa42d1a7e249a1449a5f7408f35a8e803fbad06699e2a
rank: 3
gram_tensor:
- [10, 3, 3]
- [3, 18, 9]
- [3, 9, 30]
signature: [3, 0]
determinant: 4320
definiteness: positive_definite
dual_gram_tensor:
- [17/160, -7/480, -1/160]
- [-7/480, 97/1440, -3/160]
- [-1/160, -3/160, 19/480]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 2880
  discriminant_group: [3, 1440]
  overlattice_count: 6
  bad_reduction_primes: [2, 3, 5]
  genus_symbol: 'II_{3,0} (2: 1^-2:[32^-1]_5; 3: 1^1 3^1 9^1; 5: 1^2 5^1)'
  genus_class_count: 3
  spinor_genus_count: 1
  spinor_genera: [3]
  hyperbolic_index: 0
definite:
  minimum: 10
  kissing_number: 2
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true under GRH
  spinor_regular: true under GRH
  theta_series: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0]
  root_system: []
  roots: []
root_sublattice:
  invariant_factors: []
morphisms: []
families: []
related: []
references:
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 878, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular under the generalized Riemann hypothesis by R. J. Lemke Oliver, Representations by ternary quadratic forms, Bull. London Math. Soc. 46 (2014), 1237-1247, Theorem 1.1.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 878, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular under the generalized Riemann hypothesis by R. J. Lemke Oliver, Representations by ternary quadratic forms, Bull. London Math. Soc. 46 (2014), 1237-1247, Theorem 1.1; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Row 878 of `sources/jagy_kaplansky_schiemann/regular_ternaries.txt` gives the coefficients $(a, b, c, d, e, f) = (5, 9, 15, 9, 3, 3)$ of $Q = ax^2 + by^2 + cz^2 + dyz + ezx + fxy$; the Gram tensor is that of $b(x, x) = 2Q(x)$.
