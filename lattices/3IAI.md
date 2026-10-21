---
tag: 3IAI
name: Jagy–Kaplansky–Schiemann regular ternary form 653
latex: Jagy–Kaplansky–Schiemann regular ternary form 653
aliases: []
certifications:
  definite.regular: 8fa7cdb8beb96e1316854933254981dc93ddfa65864097680d03918cb433f378
  definite.spinor_regular: 18fd630a90bac508edf5713520571566591f62961c051221d0ca0c58e385f16a
  derive: 2f1397f5171ee97544754998ce56622dd3dffdd534241d5208dc4bd1059ccb49
  form.integer_valued: 75e16afab54038e54fe0cb28e14f52a5569a244030441ca1b6f0c06f1f4a78ef
  integral.elementary_primes: ac95c6ad73e617705cb133dc521108dafc2e482a64eb6007194fbfab4fc2a97d
  integral.genus_symbol: 0af2d8f5c041533c5faccef4316361668b89bcd391e4f6a1bb4b40ce9b8be600
  integral.genus_class_count: 84cac8125a52b424a8389d545310a8e255ce9873b63dc7fde161fb74e0b5df86
rank: 3
gram_tensor:
- [33, 12, 6]
- [12, 48, 24]
- [6, 24, 52]
signature: [3, 0]
determinant: 57600
definiteness: positive_definite
dual_gram_tensor:
- [1/30, -1/120, 0]
- [-1/120, 7/240, -1/80]
- [0, -1/80, 1/40]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 480
  discriminant_group: [240, 240]
  bad_reduction_primes: [2, 3, 5]
  genus_symbol: 'I_{3,0} (2: [1^1]_1:[16^2]_2; 3: 1^1 3^2; 5: 1^-1 5^-2)'
  genus_class_count: 1
definite:
  minimum: 33
  kissing_number: 2
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
  root_system: []
  roots:
  - type: A1
    scale: 80
    simple_roots:
    - [0, 1, -2]
root_sublattice:
  invariant_factors: [1]
morphisms: []
families: []
related: []
references:
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 653, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 653, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Row 653 of `sources/jagy_kaplansky_schiemann/regular_ternaries.txt` gives the coefficients $(a, b, c, d, e, f) = (33, 48, 52, 48, 12, 24)$ of $Q = ax^2 + by^2 + cz^2 + dyz + ezx + fxy$; the Gram tensor is that of $b(x, x) = Q(x)$.
