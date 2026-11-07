"""Scattone's polarized K3 lattices: the stored Gram is the source's lattice, and its cited rows certify it.

Scattone, *On the compactification of moduli spaces for algebraic K3 surfaces* (Mem. Amer. Math. Soc.
374, 1987), §1.1 equation (1.1.1), p. 3, states L_k = U + U + E8(-1) + E8(-1) + <-2k>. The E8 summand is
the standard E8 lattice from Sage's `CartanMatrix(['E', 8])`, negated; it is unimodular.
"""

from pathlib import Path

import frontmatter
import yaml
from sage.all import CartanMatrix, block_diagonal_matrix, matrix, ZZ
from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import session_ring_objects

from latticedb import certificates, genus
from latticedb.model import Lattice

REPOSITORY = Path(__file__).resolve().parent.parent
RING = session_ring_objects()["ZZ"]
EXPECTED_ROWS = {
    "6JRX": {"O": {"planes": 4}, "O+": {"constant": 1, "planes": 4}, "Otilde+": {"constant": 1}},
    "6JRY": {"O": {"planes": 9}, "O+": {"constant": 1, "planes": 9}, "Otilde+": {"constant": 1}},
}
EXPECTED_COUNTS = {
    "6JRX": {
        "O": {"constant": None, "z": None, "w": None, "planes": 4},
        "O+": {"constant": 1, "z": None, "w": None, "planes": 4},
        "Otilde+": {"constant": 1, "z": None, "w": None},
    },
    "6JRY": {
        "O": {"constant": None, "z": None, "w": None, "planes": 9},
        "O+": {"constant": 1, "z": None, "w": None, "planes": 9},
        "Otilde+": {"constant": 1, "z": None, "w": None},
    },
}
"""The counts a certificate commits to: the terms and a stated plane count, never a citation."""


def expected_gram(k: int):
    """The exact sum U + U + E8(-1) + E8(-1) + <-2k> of Scattone (1.1.1), from the source E8 Cartan."""
    e8 = matrix(ZZ, -CartanMatrix(["E", 8]))
    u = matrix(ZZ, [[0, 1], [1, 0]])
    return block_diagonal_matrix(u, u, e8, e8, matrix(ZZ, [[-2 * k]]))


def stored(tag: str) -> Lattice:
    return Lattice.model_validate(front_matter(tag))


def front_matter(tag: str) -> dict:
    """The card as written, whose `primitive_orbits` rows are the raw series the certificate covers."""
    return frontmatter.load(REPOSITORY / "lattices" / f"{tag}.md").metadata


def test_the_two_scattone_cards_are_the_lattices_of_equation_1_1_1() -> None:
    for tag, k in (("6JRX", 1), ("6JRY", 2)):
        card = stored(tag)
        assert card.gram_tensor is not None and card.integral is not None
        expected = expected_gram(k)
        rows = [[int(value) for value in row] for row in card.gram_tensor]
        assert rows == [[int(value) for value in row] for row in expected.rows()], (
            f"{tag}: stored Gram differs from Scattone (1.1.1)"
        )
        owned = Lattices(RING)(rows)
        source = Lattices(RING)([[int(value) for value in row] for row in expected.rows()])
        assert int(owned.determinant()) == int(source.determinant()) == -2 * k
        assert tuple(int(value) for value in owned.signature_pair()) == (2, 19)
        assert int(owned.discriminant_group().cardinality()) == 2 * k
        assert card.determinant == -2 * k
        factors = [2] if k == 1 else [4]
        assert list(card.integral.discriminant_group or ()) == factors


def test_the_cited_scattone_rows_are_retained_and_certified_against_the_corrected_gram() -> None:
    for tag, wanted in EXPECTED_ROWS.items():
        card = stored(tag)
        assert card.integral is not None and card.integral.primitive_orbits is not None
        assert set(card.integral.primitive_orbits) == {"O", "O+", "Otilde+"}
        for group, fields in wanted.items():
            row = card.integral.primitive_orbits[group]
            for field, value in fields.items():
                assert getattr(row, field) == value, f"{tag} {group}.{field}"
            assert row.reference is not None and "Scattone" in row.reference.citation
        # The commitment is over the stored counts and the corrected Gram, and it is what
        # `latticedb verify` recomputes: the projection takes the front matter's raw rows, not
        # the validated series, and it drops each row's citation.
        counts = genus.certified_value("primitive_orbits", front_matter(tag)["integral"]["primitive_orbits"], card)
        assert counts == EXPECTED_COUNTS[tag]
        name = f"{tag} integral.primitive_orbits"
        assert card.certifications.get("integral.primitive_orbits") == certificates.certification_hash(
            name, card, counts
        )
        shard = yaml.safe_load((REPOSITORY / "certificates" / f"{certificates.group(tag)}.yaml").read_text()) or {}
        assert shard[name]["hash"] == card.certifications["integral.primitive_orbits"]
