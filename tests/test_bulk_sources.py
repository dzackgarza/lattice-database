"""The published bulk tables present exact lattice forms in distinct conventions."""

from fractions import Fraction
from pathlib import Path

from latticedb import brandt_intrau, nebe_sloane, nipp, records, regular_ternaries, watson
from latticedb.model import Lattice

SOURCES = Path(__file__).resolve().parent.parent / "sources"


def _determinant(gram_tensor) -> int:
    """The exact determinant of a Gram tensor, by the flint build this process already has.

    `python-flint` and Sage each load their own `libflint` — 24.0.0 out of `python_flint.libs` and the
    system 19.0.0 — and the first build's `fmpz_set` binds to the second build's symbol, so
    `fmpz_mat(...).det()` in a process that has imported `sage.all` writes through a mismatched `fmpz`
    and the interpreter dies of SIGSEGV (#29). Sage's own matrix is the flint the process loaded, so it
    is used wherever Sage is importable; `python-flint` is imported only where Sage is not.
    """
    try:
        from sage.all import ZZ, matrix
    except ImportError:
        from flint import fmpz_mat

        return int(fmpz_mat(gram_tensor).det())
    return int(matrix(ZZ, [list(row) for row in gram_tensor]).det())


def test_nipp_tables_preserve_the_source_discriminants_and_group_orders() -> None:
    quaternary = nipp.quaternary(SOURCES / "nipp" / "d4to457.html")[0]
    quinary = nipp.quinary(SOURCES / "nipp" / "tbl.256.html")[0]
    assert (quaternary.discriminant, _determinant(quaternary.gram_tensor)) == (4, 4)
    assert (quaternary.automorphism_group_order, quaternary.mass) == (1152, Fraction(1, 1152))
    assert (quinary.discriminant, _determinant(quinary.gram_tensor)) == (2, 4)
    assert (quinary.automorphism_group_order, quinary.mass) == (3840, Fraction(1, 3840))


def test_brandt_intrau_tables_apply_their_distinct_parity_conventions() -> None:
    odd = brandt_intrau.odd_table(SOURCES / "brandt_intrau" / "Brandt_1.html")[0]
    even = brandt_intrau.even_table(SOURCES / "brandt_intrau" / "Brandt_2.html")[0]
    assert (odd.discriminant, odd.gram_tensor) == (-4, ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    assert (even.discriminant, even.gram_tensor) == (-2, ((2, 1, 1), (1, 2, 1), (1, 1, 2)))


def test_watson_table_reads_lower_triangular_gram_components() -> None:
    entries = watson.stored(SOURCES / "watson" / "watson.txt")
    assert (entries[0].dimension, entries[0].gram_tensor) == (1, ((1,),))
    assert (entries[1].dimension, entries[1].gram_tensor) == (2, ((5, 1), (1, 23)))


def test_union_archive_retains_repeated_names_at_distinct_positions() -> None:
    entries = nebe_sloane.archive_rows(SOURCES / "nebe_sloane" / "union.gz")
    assert len(entries) == 823
    assert [entry.ordinal for entry in entries] == list(range(1, 824))
    assert len({entry.name for entry in entries}) < len(entries)


def test_brandt_and_watson_source_forms_seed_valid_lattice_records() -> None:
    odd = brandt_intrau.odd_table(SOURCES / "brandt_intrau" / "Brandt_1.html")[0]
    even = brandt_intrau.even_table(SOURCES / "brandt_intrau" / "Brandt_2.html")[0]
    watson_entry = watson.stored(SOURCES / "watson" / "watson.txt")[0]
    for entry, declared in (
        (odd, brandt_intrau.record(odd)[0]),
        (even, brandt_intrau.record(even)[0]),
        (watson_entry, watson.record(watson_entry)[0]),
    ):
        lattice = Lattice.model_validate(records.derive({"tag": "ZZZZ", **declared}))
        assert lattice.gram_tensor == entry.gram_tensor


def test_regular_ternary_tables_seed_valid_lattice_records_with_their_proved_values() -> None:
    entries = regular_ternaries.entries()
    assert sum("regular" in entry.certified for entry in entries) == 913
    assert sum("spinor_regular" in entry.certified for entry in entries) == 913 + 29
    assert sum(entry.proved == "true under GRH" for entry in entries) == 14
    for entry in (entries[0], entries[225], entries[913]):
        declared = regular_ternaries.record(entry)[0]
        lattice = Lattice.model_validate(records.derive({"tag": "ZZZZ", **declared}))
        assert [list(row) for row in lattice.gram_tensor] == entry.gram_tensor
        assert declared["definite"] == {field: entry.proved for field in entry.certified}
