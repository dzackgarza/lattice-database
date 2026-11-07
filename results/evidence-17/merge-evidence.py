"""The unsafe recovery merge and the repaired one, on the same constructed conflict (issue #17).

The unsafe rule is what `results/recover-42326648686.py` did first: for each top-level key that the
recovered file changed from its base, take the recovered value whole. On a lattice card that replaces an
entire `integral` block, so a field current main has gained since the base — or a certificate written
after it — is lost.

    PYTHONPATH=src python3 results/evidence-17/merge-evidence.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from latticedb import merge  # noqa: E402

CARD_BASE = {
    "tag": "0001",
    "integral": {"parity": "even", "genus_symbol": "II_{1,1}"},
    "certifications": {"derive": "aaa"},
}
# Current main: a later run added a discriminant form to the same block and certified it.
CARD_CURRENT = {
    "tag": "0001",
    "integral": {
        "parity": "even",
        "genus_symbol": "II_{1,1}",
        "discriminant_form": {"orthogonal_group_order": 1, "isotropic_classes": 1, "isotropic_orbits": 1},
    },
    "certifications": {"derive": "aaa", "integral.discriminant_form": "bbb"},
}
# The artifact: the same run certified primitive orbits, on the same block.
CARD_RECOVERED = {
    "tag": "0001",
    "integral": {"parity": "even", "genus_symbol": "II_{1,1}", "primitive_orbits": {"O": {"constant": 2}}},
    "certifications": {"derive": "aaa", "integral.primitive_orbits": "ccc"},
}

FAILURE_BASE = {"0001 integral.primitive_orbits": {"disposition": "open", "attempts": [{"hash": "h1", "reason": "lost"}], "notes": []}}
FAILURE_CURRENT = {"0001 integral.primitive_orbits": {"disposition": "retry", "attempts": [{"hash": "h1", "reason": "lost"}, {"hash": "h2", "reason": "retry after repair"}], "notes": ["triaged"]}}
FAILURE_RECOVERED = {"0001 integral.primitive_orbits": {"disposition": "open", "attempts": [{"hash": "h1", "reason": "lost"}, {"hash": "h3", "reason": "exit status 1"}], "notes": []}}


def unsafe(base, current, recovered):
    """Take every top-level key the recovered file changed from base, whole."""
    merged = dict(current)
    for key, value in recovered.items():
        if base.get(key) != value:
            merged[key] = value
    return merged


def main() -> None:
    lost = unsafe(CARD_BASE, CARD_CURRENT, CARD_RECOVERED)
    print("unsafe card merge:")
    print("  integral keys:", sorted(lost["integral"]))
    print("  certifications:", sorted(lost["certifications"]))
    print("  lost from current:", sorted(set(CARD_CURRENT["integral"]) - set(lost["integral"])),
          sorted(set(CARD_CURRENT["certifications"]) - set(lost["certifications"])))

    merged, conflicts = merge.merge(CARD_BASE, CARD_CURRENT, CARD_RECOVERED)
    print("repaired card merge:")
    print("  integral keys:", sorted(merged["integral"]))
    print("  certifications:", sorted(merged["certifications"]))
    print("  conflicts:", conflicts)

    attempts_base = FAILURE_BASE["0001 integral.primitive_orbits"]["attempts"]
    attempts_current = FAILURE_CURRENT["0001 integral.primitive_orbits"]["attempts"]
    attempts_recovered = FAILURE_RECOVERED["0001 integral.primitive_orbits"]["attempts"]
    attempts, attempt_conflicts = merge.merge(attempts_base, attempts_current, attempts_recovered, key=lambda item: item["hash"])
    print("repaired failure attempts:", [item["hash"] for item in attempts], "conflicts:", attempt_conflicts)
    print("unsafe failure attempts:", [item["hash"] for item in FAILURE_RECOVERED["0001 integral.primitive_orbits"]["attempts"]],
          "— h2 lost")

    assert "discriminant_form" in merged["integral"], merged
    assert "primitive_orbits" in merged["integral"], merged
    assert {"h1", "h2", "h3"} == {item["hash"] for item in attempts}, attempts
    assert "integral.discriminant_form" not in lost["certifications"], "the unsafe rule lost a certificate"


if __name__ == "__main__":
    main()
