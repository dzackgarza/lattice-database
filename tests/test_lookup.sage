r"""``lookup.sage`` returns the stored card and its lattice for a tag."""
from pathlib import Path

load(str(Path(__file__).resolve().parents[1] / "lookup.sage"))


def test_card_and_lattice_of_e8():
    # E8 is the unique even unimodular positive definite lattice of rank 8
    # (Conway–Sloane, SPLAG, ch. 4, §8.1), with 240 vectors of norm 2.
    record = card("0094")
    assert record.name == "E8"
    E8 = IntegralLattice(matrix(QQ, record.gram_tensor).change_ring(ZZ))
    assert E8.rank() == 8
    assert E8.determinant() == 1
    assert E8.is_even()
    assert E8.gram_matrix().is_positive_definite()
    assert len(E8.short_vectors(3)[2]) == 240
    assert lattice("0094").rank() == 8
