# `Lattices(QQ)` refuses a Python `Fraction` entry: `unable to coerce <class 'fractions.Fraction'> to an integer`

Filed against `dzackgarza/sage-extensions` from `dzackgarza/lattice-database#37`. The GitHub App
this connection holds has no write access to this repository's issues, so the text is here and was
not posted; open it with this body.

## What fails

The owned `QQ` element constructor does not accept a Python `fractions.Fraction`. It reads the value
as a numerator of the `ZZ`-localization that presents `QQ`, so `Fraction(2, 3)` reaches
`ZZ.__init__` and raises `TypeError: unable to coerce <class 'fractions.Fraction'> to an integer`.

Observed at `dbe90c02ae` (the revision the failing `tests` run used) as
`sage_extensions/categories/rings/ring_foundation.py:1658` in `source_element`, reached from
`Lattices.__call__` through `_lattice._nested_gram_tensor`; the same failure is present at `441519c`
as `ring_foundation.py:1535`/`1538` in the `source_element`/`fraction` pair.

## Reproducer, through the public call only

```python
from fractions import Fraction

from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import session_ring_objects

rings = session_ring_objects()
ZZ, QQ = rings["ZZ"], rings["QQ"]

QQ(Fraction(2, 3))                                      # TypeError: unable to coerce <class 'fractions.Fraction'> to an integer
QQ(2) / QQ(3)                                           # (2)/(3)                      ok
Lattices(QQ)([[2, 1], [1, 2]])                          # Lattice of rank 2 and signature (2, 0)   ok
Lattices(QQ)([[QQ(2)/QQ(3), QQ(1)/QQ(3)],               # Lattice of rank 2 and signature (2, 0)   ok
              [QQ(1)/QQ(3), QQ(2)/QQ(3)]])
Lattices(ZZ)([[2, 1], [1, 2]])                          # Integral lattice of rank 2 and signature (2, 0)   ok
Lattices(QQ)([[Fraction(2, 3), Fraction(1, 3)],         # TypeError, as above
              [Fraction(1, 3), Fraction(2, 3)]])
```

Run inside the pinned image (`ghcr.io/dzackgarza/sage:develop`) with
`PYTHONPATH=<sage-extensions>/src`, Sage 11.0.beta5, Python 3.14.10. Command that produced it:

```sh
/sage/.venv/bin/python - <<'PY'
from fractions import Fraction
from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import session_ring_objects
ZZ, QQ = session_ring_objects()["ZZ"], session_ring_objects()["QQ"]
print(QQ(Fraction(2, 3)))
PY
```

## Expected

`A nested list of rational values constructs a lattice over `QQ``: an owned `QQ` element for a
Python `Fraction` (`QQ(Fraction(2, 3)) == QQ(2) / QQ(3)`), and therefore
`Lattices(QQ)(<nested list of Fraction>)` for the same list of `QQ` elements. Either that, or a
refusal that names the accepted input — the current message reports a coercion to an integer,
which is not the ring the caller asked for.

## Where lattice-database stops

`latticedb.records.derive` builds the rational model of a card with rational Gram entries from the
values the card stores, which are `fractions.Fraction`:

```python
rational_lattice = Lattices(QQ)(gram)          # src/latticedb/records.py:320
```

so `tests/test_records.py::test_derive_computes_rational_definite_invariants_through_the_integral_twist`
fails for the card `A2 dual`, gram tensor `[["2/3", "1/3"], ["1/3", "2/3"]]`, at the line above. The
one-line reproduction through the database is:

```sh
PYTHONPATH=$HOME/research/src:src /sage/.venv/bin/python - <<'PY'
from latticedb import records
records.derive({"tag": "0001", "name": "A2 dual", "latex": "A2 dual", "aliases": [],
                "gram_tensor": [["2/3", "1/3"], ["1/3", "2/3"]],
                "families": [], "related": [], "references": []})
PY
```

The database does not convert those values itself: `records.rational_gram` presents the same card
entries as elements of the restricted regular module for the formed module, and a bare `Fraction`
is the stored form the card holds.

## Provenance

* `dzackgarza/lattice-database` `tests` run `43007340416`, lattice-database `1224b1b184`,
  sage-extensions `dbe90c02ae`, test
  `tests/test_records.py::test_derive_computes_rational_definite_invariants_through_the_integral_twist`,
  first assertion line: `ring_foundation.py:1658 source_element: unable to coerce <class 'fractions.Fraction'> to an integer`,
  reached from `Lattices.__call__` through `_nested_gram_tensor`.
* Reproduced at `dbe90c02ae` and at `441519c` in the image above, in both cases from the public calls
  quoted here.
