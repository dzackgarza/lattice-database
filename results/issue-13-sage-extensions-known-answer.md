# #13, item 2 — the known-answer test, prepared and unposted

Issue #13 has two acceptance items.

**Item 1 — the cards.** `lattices/6JRS.md` … `lattices/6JRW.md` carry
`integral.primitive_orbits` rows under `O`, `Otilde` and `Otilde+`, minted by
`latticedb certify` and certified by computation (`by: research preamble`, no
`reference` on a row). Landed in `18f55ce6fa`, merged forward and pushed as
`f9a1132aff2a379472206d080fae4bfa78a7ffee`. The evidence script is
`results/issue-13-the-three-orbit-rows-of-the-lambda-cards.py`:

```
run.sh -b "$PWD:/repos/lattice-database" -w /repos/lattice-database -- \
  /sage/.venv/bin/python results/issue-13-the-three-orbit-rows-of-the-lambda-cards.py \
  /repos/lattice-database --base=6bb85dd064
```

It reports `checks.records.problems` = 0 over the five cards, the recomputed
certificate equal to the card's stamp and to the held certificate on all five,
no row cited, and nothing else on a card moved.

**Item 2 — sage-extensions' known-answer test.** This file is that work, and it is
**unposted**: the platform's GitHub connection for this project is
`dzackgarza/lattice-database` alone, so the patch below cannot be pushed from
here. It is a checked patch against `dzackgarza/sage-extensions` at
`f2c519c` ("evidence: the kernel plane row gathers its split …"): apply it with

```
git apply results/issue-13-sage-extensions-known-answer.patch
```

in a sage-extensions checkout at that commit, then run
`python3 tests/cards/refresh_lattice_database_enriques.py --ref f9a1132aff…`
if the digest is to follow a later database commit.

## What the patch changes

| file | change |
| --- | --- |
| `tests/lattices/test_primitive_orbit_series_on_indefinite_lattices.sage` | the known-answer test: one test per card comparing the library's `isotropic_orbit_representatives(1).cardinality()` for `O`, `Otilde`, `Otilde+` with the card's row, plus the series-vs-orbit-call agreement on `6JRS`, the emptiness of `z`/`w`, the card's Gram/rank/signature/determinant, and the rows' certification |
| `tests/cards/refresh_lattice_database_enriques.py` | `LAMBDA_ORBIT_TAGS = ("6JRS", "6JRT", "6JRU", "6JRV", "6JRW")` added to `PRIMITIVE_ORBIT_TAGS`, so the digest carries the five cards; each row also records `cited` — whether the card states a `reference` — so the test can assert the row is a certificate's and not a citation's |
| `tests/cards/lattice-database-enriques.json` | regenerated at `f9a1132aff…`: the five cards' rows, `cited: false` on all eight cards in the section, and no other section moved |
| `tests/cards/README.md` | the read-rows table names the five cards and `cited`; `_provenance.ref` refreshed |

The test file's numbers are not typed: it reads the card by tag through the
conftest's `card` builtin and the library computes its side, so a library that
changes its count and a card that changes its number both fail. The file is split
one test per card because the count is a real computation (`L_36` is the slowest)
and the session's `--timeout=60` bounds one test.

## What was run

All inside the research image (`/sage/.venv/bin/python`, sage-extensions at
`f2c519c` bound at `/repos/sage-extensions`, this repository at
`f9a1132aff`):

* `python3 tests/cards/refresh_lattice_database_enriques.py --ref f9a1132aff…` —
  80 s, writes a 376-line diff: the five cards' rows and the `cited` flag, no
  other section changed.
* the known-answer test, all nine tests, in 52 s:
  `test_the_rows_of_l_1…` 7.4 s, `l_2` 8.6 s, `l_4` 5.4 s, `l_9` 6.6 s, `l_36`
  12.7 s, the series agreement 1.6 s, the `z`/`w` emptiness 0.9 s, the Gram test
  0.0 s, the certification test 0.0 s — 9 passed.
* `python -m sage_extensions.testing.test_lint tests/lattices/test_primitive_orbit_series_on_indefinite_lattices.sage`
  — 1 file, 0 findings. (The first draft used `isinstance` and `len` on the stamp
  and was rejected `TL03`/`TL10`; the stamp is now checked as a hexadecimal set.)
* `pytest tests/lattices/test_the_enriques_line_rows_by_card.py
  tests/lattices/test_coordinate_diagonal_embeddings.py -q --no-time-gates` — the
  four tests that read the regenerated digest, 4 passed.

The checkout's `.sage` collector is a CI-side plugin this image does not carry
(`pytest tests/lattices` collects only the `.py` files), so the `.sage` test was
executed by a driver that binds exactly the builtin `tests/lattices/conftest.py`
binds (`card`) and calls every `test_*` function. It is not a `pytest` run of the
collector; the assertions are the same assertions.

## Two things this patch does not fix

* `tests/lattices/test_primitive_orbit_series_on_the_catalogued_lattices.sage`
  fails on `0016` (`U`), before and after this patch and on the image's baked
  sage-extensions `cf656f8c` as well:
  `ArithmeticError: the stabilizer of Integral lattice of rank 1 and signature
  (0, 0) in Orthogonal group O(Integral lattice of rank 2 and signature (1, 1))
  has character image of order at least 1, and the stabilizer of its divided
  discriminant data has order 2; no exhibited stabilizer element closes the index
  2, so the exact image chi(Stab) is not certified`. It is a library defect on the
  rank-2 hyperbolic plane, not a digest or test problem, and it is not #13's.
* The database's five cards' `integral.primitive_orbits` certificate is over the
  three rows the card states. If the preamble later returns a count for another of
  the eight standard subgroups, `certify` mints that row and rewrites the field's
  one hash; the digest must then be refreshed (`cited` and the rows both come from
  the card), and this test will compare it without an edit.
