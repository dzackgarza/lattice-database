r"""
Sage session access to the lattice database by tag.

Load it into a Sage session started with ``~/research/src`` and ``src`` on ``PYTHONPATH``::

    sage: load("lookup.sage")
    sage: card("0094").name
    'E8'
    sage: lattice("0094").discriminant_module()

``card`` returns the validated record of ``lattices/<tag>.md``; ``lattice`` builds the
preamble lattice of that record's Gram tensor.
"""
from pathlib import Path

import frontmatter

import latticedb
from dzack_research.preamble.categories.lattices import Lattices
from latticedb.model import Lattice

LATTICES = Path(latticedb.__file__).resolve().parents[2] / "lattices"


def card(tag):
    r"""The validated record whose permanent identifier is ``tag``."""
    record = Lattice.model_validate(frontmatter.load(str(LATTICES / f"{tag}.md")).metadata)
    assert record.tag == tag, f"lattices/{tag}.md states tag {record.tag}"
    return record


def lattice(tag):
    r"""The preamble lattice over ``ZZ`` of the Gram tensor stored on card ``tag``."""
    record = card(tag)
    assert record.gram_tensor is not None, f"card {tag} stores no Gram tensor"
    return Lattices(ZZ)(record.gram_tensor)
