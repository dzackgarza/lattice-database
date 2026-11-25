"""Evidence for lattice-database#13: the three orbit rows of each U ⊕ U ⊕ ⟨-2d⟩ card.

Run in the image with the card repository bound at the root it is given:

    repo=.scratch/sageext  # any checkout, this script reads only latticedb
    ~/sage-image/run.sh -b "$PWD:/repos/lattice-database" -w /repos/lattice-database -- \
        /sage/.venv/bin/python results/issue-13-the-three-orbit-rows-of-the-lambda-cards.py /repos/lattice-database

The script decides each acceptance item on the smallest input that can decide it:

1. `integral.primitive_orbits` on each card states a `constant` for `O`, `Otilde` and
   `Otilde+`, and nothing else on the card moved but the field and its stamp.  The
   comparison is against the card as `--base` has it (pass the commit before the rows
   landed), parsed, so a reformat is not a change; without `--base` the clause is
   reported as not exercised rather than passed.
2. Each row's certificate is one the recomputation agrees with, through the same
   `genus.certified_value` and `certificates.certification_hash` that `certify` used, and
   `checks.records.problems` finds nothing to say about the five cards.
3. The rows are certified by computation, not by a citation: the certificate's `by` names
   the preamble and no row carries a `reference`.
"""

import subprocess
import sys
from pathlib import Path

import yaml

from latticedb import certificates, checks, corpus, genus

arguments = [argument for argument in sys.argv[1:] if not argument.startswith("--base=")]
base = next((argument.partition("=")[2] for argument in sys.argv[1:] if argument.startswith("--base=")), None)
root = Path(arguments[0] if arguments else ".")
TAGS = ("6JRS", "6JRT", "6JRU", "6JRV", "6JRW")
ROWS = ("O", "Otilde", "Otilde+")
FIELD = "integral.primitive_orbits"


def front_matter(text: str) -> dict:
    """The YAML block of one card file, as a mapping."""
    _, _, rest = text.partition("---\n")
    body, _, _ = rest.partition("\n---\n")
    return yaml.safe_load(body)


def committed_card(tag: str, base: str | None) -> dict | None:
    """The card as `base` has it, so the diff a run made is the change and not a restyle."""
    if base is None:
        return None
    shown = subprocess.run(
        ["git", "show", f"{base}:lattices/{tag}.md"], cwd=root, capture_output=True, text=True, check=True
    )
    return front_matter(shown.stdout)


loaded = corpus.cards(root, TAGS)
held = certificates.load(root, TAGS)
problems = checks.records.problems(loaded, held, frozenset(TAGS))
print(f"item 2: checks.records.problems over the five cards: {len(problems)}")
for problem in problems:
    print("   ", problem)

failed = bool(problems)
for tag in TAGS:
    path = root / "lattices" / f"{tag}.md"
    before, after = committed_card(tag, base), front_matter(path.read_text())
    card = next(entry.lattice for entry in loaded.entries if entry.lattice.tag == tag)
    rows = after["integral"].get("primitive_orbits") or {}
    counts = {row: (rows.get(row) or {}).get("constant") for row in ROWS}

    # What moved, other than the field and the one stamp over it: the `integral` block is
    # expected to change, so what it may change by is the one key it gains.
    if before is None:
        moved, integral_moved, stamps = None, None, None
    else:
        moved = {key for key in after if key not in {"certifications", "integral"} and after[key] != before.get(key)}
        earlier = after["integral"]
        previous = before["integral"]
        integral_moved = {key for key in set(earlier) | set(previous) if earlier.get(key) != previous.get(key)}
        if integral_moved == {"primitive_orbits"}:
            integral_moved = set()
        stamps = {key for key in after["certifications"] if after["certifications"].get(key) != before["certifications"].get(key)}

    # The commitment and the certificate, through the code path `certify` wrote them with.
    computation = genus.name(tag, "primitive_orbits", card.definiteness)
    committed = genus.certified_value("primitive_orbits", rows or None, card)
    recomputed = certificates.certification_hash(computation, card, committed)
    stamp = card.certifications.get(FIELD)
    log = held.get(computation)
    cited_rows = [row for row in ROWS if "reference" in (rows.get(row) or {})]

    ok = (
        all(counts.get(row) is not None for row in ROWS)
        and (before is None or (not moved and not integral_moved and stamps == {FIELD}))
        and stamp is not None and log is not None and log.hash == recomputed == stamp
        and log.by == "research preamble"
        and not cited_rows
    )
    failed |= not ok
    print(
        f"{tag}: rows {counts} | "
        f"other blocks moved {sorted(moved) if moved is not None else 'not exercised (no --base)'} | "
        f"other integral keys moved {sorted(integral_moved) if integral_moved is not None else None} | "
        f"stamps moved {sorted(stamps) if stamps is not None else None} | recomputed {recomputed[:12]} "
        f"= card {str(stamp)[:12]} = certificate {log.hash[:12] if log else None} "
        f"by {log.by if log else None} | cited rows {cited_rows} | {'ok' if ok else 'FAILED'}"
    )

sys.exit(1 if failed else 0)
