"""#4: the preamble prints a local density as `(3)/(2)`, and no `Fraction` reads that text.

Item 2 of #4 asks the regression test's path to receive an owner element whose printed form is
`(3)/(2)`. `tests/test_genus.py` states the value the card stores; this file states the premise on the
owner's own object and ties it to the serializer that reads it.

It is a module of its own because it loads the preamble into the test process, and a certify test that
runs in the same process has less memory and time for the worker it starts. Measured on the host this
was written on: with the same assertion placed inside `test_genus.py`, `genus.certify(...,
time.time() + 120)` ended with `Certification time budget exhausted` after 179.87 s, against 59.63 s
for the same tests without it, and as its own test in that file the worker was killed at `memory: 1.6
GiB available; 0022 holds 0.2 GiB`. As this module, the pair with that certify test passes in either
order (33.04 s and 40.50 s at load average 17.75); `justfile` and
`.github/workflows/certification-tests.yml` name it after `tests/test_genus.py` regardless, so the
worker never meets the process's high-water mark.
"""

from fractions import Fraction
from pathlib import Path

import frontmatter
import pytest

from latticedb import sage_genus

REPOSITORY = Path(__file__).resolve().parent.parent


def test_a_local_density_prints_the_text_a_fraction_rejects() -> None:
    """#4: 0022's density at 2 is `(3)/(2)` on the owner's object, and `_rational` stores `3/2`."""
    from sage_extensions.categories.lattices import Lattices
    from sage_extensions.rings import ZZ as owned_integers

    card = frontmatter.load(str(REPOSITORY / "lattices" / "0022.md")).metadata
    density = Lattices(owned_integers)(card["gram_tensor"]).genus().local_density(2, 1)
    assert str(density) == "(3)/(2)"
    with pytest.raises(ValueError):
        Fraction(str(density))
    assert sage_genus._rational(density) == "3/2"
