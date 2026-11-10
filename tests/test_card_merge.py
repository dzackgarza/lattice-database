"""Two certification runs rewrite one card, and Git integrates both through its merge of that card.

The fields run and the searches run hold different fields of the same card, and each is a run of its
own: `certify.yml` takes the terminating fields and `certify-searches.yml` the semi-decisions, under
two concurrency groups. A run rewrites a card from the copy it checked out, so a card it does not
compute a field of still carries that field's lines as they were at its checkout. Both runs push by
cherry-picking their snapshot onto `main` (`.github/scripts/persist.sh`), so the card's citations are
merged, not replaced: a citation one run wrote is not the other run's to drop (#21).
"""

import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from latticedb import card_merge

REPOSITORY = Path(__file__).resolve().parent.parent

SEARCHES = ("hyperbolic.reflective", "root_span.norms", "root_span.roots")
"""The citations `certify-searches.yml` writes: the semi-decision fields of one card."""


def git(root: Path, *arguments: str) -> None:
    subprocess.run(["git", "-C", str(root), *arguments], check=True, capture_output=True)


def card(certifications: dict[str, str], integral: dict[str, object], definite: dict[str, object] | None) -> str:
    """A card with the blocks the defect involves, in the order a card lists them."""
    metadata: dict[str, object] = {
        "tag": "0268",
        "name": "<-1>^2 + <3>",
        "latex": "\\langle -1 \\rangle^{2} \\oplus \\langle 3 \\rangle",
        "aliases": [],
        "certifications": certifications,
        "rank": 3,
        "gram_tensor": [[-1, 0, 0], [0, -1, 0], [0, 0, 3]],
        "signature": [1, 2],
        "determinant": 3,
        "definiteness": "indefinite",
        "integral": integral,
        "root_span": {"roots": [[-1, 0, 0], [0, -1, 0], [0, 0, -1]], "norms": [-1, -1, 3]},
        "families": [],
        "related": [],
        "references": [],
        "hyperbolic": {"reflective": True},
    }
    if definite is not None:
        metadata["definite"] = definite
    return "---\n" + yaml.dump(metadata, sort_keys=False) + "---\n\nThe card's prose.\n"


FIELDS_RUN = {"derive": "11", "integral.genus_symbol": "22", "integral.genus_class_count": "33"}
"""What the fields run's copy of the card cites: its own computations, no semi-decision."""


def repository(tmp_path: Path) -> Path:
    """A repository whose cards merge through the driver `.gitattributes` declares, as main does."""
    (tmp_path / ".gitattributes").write_text((REPOSITORY / ".gitattributes").read_text())
    (tmp_path / "lattices").mkdir()
    # Git runs a driver in the worktree it merges, so the interpreter needs the source tree by
    # absolute path rather than the relative one this test session carries.
    driver = f"env PYTHONPATH={REPOSITORY / 'src'} {sys.executable} -m latticedb.card_merge %O %A %B"
    git(tmp_path, "init", "-q", "-b", "main")
    git(tmp_path, "config", "user.name", "test")
    git(tmp_path, "config", "user.email", "test@example.invalid")
    git(tmp_path, "config", "merge.card-map.driver", driver)
    return tmp_path


def test_a_card_keeps_the_citations_the_overlapping_run_wrote(tmp_path: Path) -> None:
    """The defect of #21: the searches run's three citations, dropped by the fields run's push."""
    root = repository(tmp_path)
    path = root / "lattices" / "0268.md"
    searches_only = {**FIELDS_RUN, **{field: f"aa{index}" for index, field in enumerate(SEARCHES)}}
    path.write_text(card(FIELDS_RUN, {"genus_symbol": "I_{1,2}"}, None))
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "the card both runs read")
    # The searches run certifies the three semi-decisions and pushes them.
    git(root, "checkout", "-q", "-b", "searches")
    path.write_text(card(searches_only, {"genus_symbol": "I_{1,2}"}, None))
    git(root, "commit", "-q", "-am", "searches")
    # The fields run, from the card as it was before that push, certifies a field of its own.
    git(root, "checkout", "-q", "main")
    git(root, "checkout", "-q", "-b", "fields")
    later = {**FIELDS_RUN, "integral.local_densities": "44"}
    path.write_text(card(later, {"genus_symbol": "I_{1,2}", "local_densities": [{"prime": 2, "densities": [1]}]}, None))
    git(root, "commit", "-q", "-am", "fields")
    git(root, "checkout", "-q", "searches")
    # What persist.sh does with one shard's snapshot.
    git(root, "cherry-pick", "fields")
    merged = yaml.safe_load(path.read_text().split("---")[1])["certifications"]
    assert merged == {**FIELDS_RUN, "integral.local_densities": "44", **{field: f"aa{index}" for index, field in enumerate(SEARCHES)}}


def test_a_card_keeps_a_value_the_overlapping_run_stored(tmp_path: Path) -> None:
    """The same integration, one block down: a value the fields run states is not the searches' to drop.

    `definite.regular` is a semi-decision field, so the searches run stores it; the fields run's copy
    of the card predates it and rewrites the block for a field of its own.
    """
    root = repository(tmp_path)
    path = root / "lattices" / "0268.md"
    path.write_text(card(FIELDS_RUN, {"genus_symbol": "I_{1,2}"}, {"minimum": 2}))
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "the card both runs read")
    git(root, "checkout", "-q", "-b", "searches")
    path.write_text(card({**FIELDS_RUN, "definite.regular": "aa0"}, {"genus_symbol": "I_{1,2}"}, {"minimum": 2, "regular": False}))
    git(root, "commit", "-q", "-am", "searches")
    git(root, "checkout", "-q", "main")
    git(root, "checkout", "-q", "-b", "fields")
    path.write_text(card(FIELDS_RUN, {"genus_symbol": "I_{1,2}", "genus_class_count": 1}, {"minimum": 2, "kissing_number": 6}))
    git(root, "commit", "-q", "-am", "fields")
    git(root, "checkout", "-q", "searches")
    git(root, "cherry-pick", "fields")
    metadata = yaml.safe_load(path.read_text().split("---")[1])
    assert metadata["definite"] == {"minimum": 2, "kissing_number": 6, "regular": False}
    assert metadata["certifications"]["definite.regular"] == "aa0"


def test_a_one_sided_change_is_taken_and_a_disagreement_is_the_incoming_run() -> None:
    """Each key's change comes from the side that made one; a key both changed takes the incoming run.

    A citation the incoming run no longer states is a disagreement, and it is taken: a run that
    retracts a value it certified is the newer record of that key. This is not the defect — the
    defect is a run that never had the key, which states nothing to disagree with.
    """
    base = {"certifications": {"derive": "1", "root_span.roots": "2"}, "root_span": {"roots": [[1]], "norms": [1]}}
    ours = {"certifications": {"derive": "1", "root_span.roots": "9"}, "root_span": {"roots": [[1]], "norms": [1]}}
    theirs = {"certifications": {"derive": "1"}, "root_span": {"roots": [[2]], "norms": [2]}}
    assert card_merge.merge(base, ours, theirs) == {
        "certifications": {"derive": "1"},
        "root_span": {"roots": [[2]], "norms": [2]},
    }


def test_the_driver_writes_the_merged_card_into_ours(tmp_path: Path) -> None:
    """Git's driver protocol: the result belongs in `ours`, and it reads as a card."""
    base = tmp_path / "base.md"
    ours = tmp_path / "ours.md"
    theirs = tmp_path / "theirs.md"
    base.write_text(card(FIELDS_RUN, {"genus_symbol": "I_{1,2}"}, None))
    ours.write_text(card({**FIELDS_RUN, **{field: f"aa{index}" for index, field in enumerate(SEARCHES)}}, {"genus_symbol": "I_{1,2}"}, None))
    theirs.write_text(card({**FIELDS_RUN, "integral.local_densities": "44"}, {"genus_symbol": "I_{1,2}", "local_densities": [{"prime": 2}]}, None))
    card_merge.merge_files(base, ours, theirs)
    merged = yaml.safe_load(ours.read_text().split("---")[1])
    assert set(merged["certifications"]) == {*FIELDS_RUN, "integral.local_densities", *SEARCHES}
    assert merged["integral"]["local_densities"] == [{"prime": 2}]
    assert ours.read_text().endswith("The card's prose.\n")


def test_a_card_the_driver_cannot_read_stops_the_merge(tmp_path: Path) -> None:
    """A side that is not a card is a defect to report, never a card half written."""
    base = tmp_path / "base.md"
    ours = tmp_path / "ours.md"
    theirs = tmp_path / "theirs.md"
    base.write_text(card(FIELDS_RUN, {"genus_symbol": "I_{1,2}"}, None))
    ours.write_text(card(FIELDS_RUN, {"genus_symbol": "I_{1,2}"}, None))
    theirs.write_text("<<<<<<< HEAD\nnot a card\n")
    before = ours.read_text()
    with pytest.raises(card_merge.Unreadable):
        card_merge.merge_files(base, ours, theirs)
    assert ours.read_text() == before
