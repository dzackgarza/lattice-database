"""The recovery merge keeps both sides of a field neither of them conflicts on (issue #17)."""

from __future__ import annotations

from latticedb import merge

CARD_BASE = {"tag": "0001", "integral": {"parity": "even"}, "certifications": {"derive": "a"}}
# Current main: a later run added a field to the same block and certified it.
CARD_CURRENT = {
    "tag": "0001",
    "integral": {"parity": "even", "discriminant_form": {"isotropic_classes": 1}},
    "certifications": {"derive": "a", "integral.discriminant_form": "b"},
}
# The artifact: its own run added another field to that same block.
CARD_RECOVERED = {
    "tag": "0001",
    "integral": {"parity": "even", "primitive_orbits": {"O": {"constant": 2}}},
    "certifications": {"derive": "a", "integral.primitive_orbits": "c"},
}


def test_two_runs_that_extend_one_block_keep_both_extensions() -> None:
    """A field only one side has is taken; only a field both changed differently is a conflict."""
    merged, conflicts = merge.merge(CARD_BASE, CARD_CURRENT, CARD_RECOVERED)
    assert isinstance(merged, dict)
    assert set(merged["integral"]) == {"parity", "discriminant_form", "primitive_orbits"}
    assert set(merged["certifications"]) == {"derive", "integral.discriminant_form", "integral.primitive_orbits"}
    assert conflicts == []


def test_two_attempts_of_one_failure_are_both_kept() -> None:
    """A failure's attempts are merged by hash, so neither run's evidence is dropped."""
    base = {"attempts": [{"hash": "h1"}]}
    current = {"attempts": [{"hash": "h1"}, {"hash": "h2"}]}
    recovered = {"attempts": [{"hash": "h1"}, {"hash": "h3"}]}
    merged, conflicts = merge.merge(base, current, recovered, key=lambda item: item.get("hash"))
    assert [item["hash"] for item in merged["attempts"]] == ["h1", "h2", "h3"]
    assert conflicts == []


def test_a_field_both_sides_changed_differently_is_reported_and_kept() -> None:
    """A real disagreement is neither resolved nor lost: the current value stays and the path is named."""
    merged, conflicts = merge.merge({"seconds": 1}, {"seconds": 2}, {"seconds": 3})
    assert merged == {"seconds": 2}
    assert conflicts == ["seconds"]
