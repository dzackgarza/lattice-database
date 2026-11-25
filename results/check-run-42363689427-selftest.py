"""The comparison the #20 recovery uses is exact: it rejects reordering and lost multiplicity.

    python3 results/check-run-42363689427-selftest.py

A completeness check that accepts an old snapshot's values as "present" is only worth what its
equality is worth. This shows `recovery_comparison.same` and `changed_leaves` refusing exactly the
cases an unordered or recursive-subset comparison would have wrongly accepted: a permuted Gram
matrix, a permuted coordinate vector, a permuted morphism matrix, a lost duplicate coefficient, a
lost trailing entry, a cleared field, and `true` standing in for `1`.

Run it before believing a completeness result.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from recovery_comparison import MISSING, at, changed_leaves, same  # noqa: E402

GRAM = [[4, 2, 0], [2, 4, 2], [0, 2, 4]]
REVERSED = [[4, 2, 0], [2, 4, 2], [0, 2, 4]][::-1]
ROWS_PERMUTED = [GRAM[1], GRAM[0], GRAM[2]]

REJECTED = {
    "permuted Gram rows": (GRAM, ROWS_PERMUTED),
    "reversed Gram rows": (GRAM, REVERSED),
    "permuted coordinate vector": ([1, 2, 3], [3, 2, 1]),
    "permuted morphism matrix": ([[0, 1, 0], [1, 0, 0], [0, 0, 1]], [[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
    "lost duplicate coefficient": ([1, 1, 3], [1, 3]),
    "lost duplicate in a Gram row": ([[4, 2], [2, 4]], [[4, 2], [2, 4], [2, 4]]),
    "lost trailing coefficient": ([-1, 3], [-1]),
    "reordered norms": ([-1, 3], [3, -1]),
    "cleared to empty": ([[4]], []),
    "a list became a mapping": ([[4, 2], [2, 4]], {"0": [4, 2]}),
    "true standing in for 1": (1, True),
    "integer standing in for a string": ("4", 4),
    "a cipher standing in for nothing": (MISSING, None),
    "dropped key": ({"constant": 1, "planes": 4}, {"constant": 1}),
    "a citation that names another page": (
        {"citation": "Scattone, Section 6.2, p. 97"},
        {"citation": "Scattone, Section 6.2, p. 98"},
    ),
}

ACCEPTED = {
    "identical Gram": (GRAM, [list(row) for row in GRAM]),
    "identical nested record": (
        {"constant": 1, "planes": 4, "z": [], "w": []},
        {"constant": 1, "planes": 4, "z": [], "w": []},
    ),
    "identical mapped rows": (
        {"O": {"planes": 4}, "O+": {"constant": 1, "planes": 4}},
        {"O": {"planes": 4}, "O+": {"constant": 1, "planes": 4}},
    ),
}

failures: list[str] = []
for description, (left, right) in REJECTED.items():
    if same(left, right):
        failures.append(f"same() accepted {description}: {left!r} == {right!r}")
for description, (left, right) in ACCEPTED.items():
    if not same(left, right):
        failures.append(f"same() rejected {description}: {left!r} != {right!r}")

# A snapshot delta is reported, an untouched field is not, and a change is only "present" exactly.
base = {"rank": 3, "gram_tensor": GRAM, "integral": {"primitive_orbits": {"O": {"planes": 4}}}}
snapshot = {"rank": 3, "gram_tensor": GRAM, "integral": {"primitive_orbits": {"O": {"planes": 9}}}}
delta = changed_leaves(base, snapshot)
if delta != {"integral.primitive_orbits.O.planes": 9}:
    failures.append(f"changed_leaves reported {sorted(delta)}, not only the changed path")
if "rank" in delta or "gram_tensor" in delta:
    failures.append(f"changed_leaves reported an unchanged field: {sorted(delta)}")

current = {"rank": 3, "gram_tensor": GRAM, "integral": {"primitive_orbits": {"O": {"planes": 9}}}}
if not same(at(current, "integral.primitive_orbits.O.planes"), 9):
    failures.append("a value the snapshot states exactly was not found")
if same(at(current, "integral.primitive_orbits.O.planes"), 4):
    failures.append("a different value was accepted")
reordered = {"integral": {"primitive_orbits": {"O": {"planes": 9}}}, "gram_tensor": ROWS_PERMUTED}
if same(at(reordered, "gram_tensor"), GRAM) or at(current, "gram_tensor.inner") is not MISSING:
    failures.append("a permuted Gram passed, or a path through a list was read as a mapping")

for failure in failures:
    print("FAIL:", failure)
print(f"{len(REJECTED)} rejections, {len(ACCEPTED)} acceptances and 6 path cases checked; {len(failures)} failures")
raise SystemExit(1 if failures else 0)
