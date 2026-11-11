"""Migrate the imported card format's declared implicit morphism scales.

At revision 287b70c9791a898e35a9400fd57b276ef599812d, Morphism.scale was
an integer with default 1 (src/latticedb/model.py). The subsequent schema
split made an omitted scale unknown without migrating the stored cards.
This reader restores only declarations matched in that immutable source;
it neither infers a scale from a matrix nor assigns one to a new morphism.

The immutable source is the pinned revision, read from a checkout that holds it
or from a snapshot directory that holds that revision's cards at the same
relative paths.  A checkout is read through `git`, so a card the working tree
has since changed still reads as the revision stored it; the snapshot is how a
checkout without the history, such as the shallow one CI makes, reads it.

Run from the repository's Sage Python with:
    from pathlib import Path
    from latticedb.legacy_morphisms import restore
    restore(Path(), Path())
"""

import json
import subprocess
from pathlib import Path

import frontmatter
from pydantic import TypeAdapter

from latticedb import corpus, records
from latticedb.model import Yaml

REVISION = "287b70c9791a898e35a9400fd57b276ef599812d"
MORPHISMS = TypeAdapter(list[dict[str, Yaml]])


def _key(morphism: dict[str, Yaml]) -> str:
    return json.dumps([morphism["target"], morphism["name"], morphism["matrix"]])


def _archive_from_git(archive: Path) -> dict[str, str]:
    """The revision's cards that declare morphisms, read out of the checkout `archive` through `git`."""
    listed = subprocess.check_output(["git", "-C", str(archive), "grep", "-l", "^morphisms:", REVISION, "--", "lattices"], text=True).splitlines()
    paths = [source_path.split(":", 1)[1] for source_path in listed]
    return {relative: subprocess.check_output(["git", "-C", str(archive), "show", f"{REVISION}:{relative}"], text=True) for relative in paths}


def _archive_from_directory(archive: Path) -> dict[str, str]:
    """The cards that declare morphisms of the snapshot `archive`, under the revision's own relative paths."""
    found: dict[str, str] = {}
    for path in sorted((archive / "lattices").glob("*.md")):
        text = path.read_text()
        if "\nmorphisms:\n" in text:
            found[f"lattices/{path.name}"] = text
    return found


def archived_cards(archive: Path) -> dict[str, str]:
    """The cards of the pinned revision that declare morphisms, relative path -> text.

    `archive` is a checkout that holds the revision, which `git` identifies by the
    revision and not by its working tree, or a snapshot directory holding that
    revision's `lattices/` as the revision stored them.
    """
    if (archive / ".git").exists():
        return _archive_from_git(archive)
    return _archive_from_directory(archive)


def restore(root: Path, archive: Path) -> tuple[Path, ...]:
    """Make the historical declarations explicit on matching current cards."""
    changed: list[Path] = []
    for relative, archived_text in archived_cards(archive).items():
        path = root / relative
        if not path.is_file():
            continue
        text = path.read_text()
        if "\nmorphisms:\n" not in text:
            continue
        document = frontmatter.loads(text)
        metadata = corpus.front_matter(document)
        morphisms = MORPHISMS.validate_python(metadata["morphisms"], strict=True)
        if all(morphism.get("scale") is not None for morphism in morphisms):
            continue
        original = frontmatter.loads(archived_text)
        source = {_key(morphism): morphism for morphism in MORPHISMS.validate_python(original.metadata.get("morphisms", []), strict=True)}
        edited = False
        for morphism in morphisms:
            if morphism.get("scale") is None and _key(morphism) in source:
                declared = source[_key(morphism)]
                # Absence is exactly 1 in this pinned source format's schema.
                morphism["scale"] = declared["scale"] if "scale" in declared else 1
                edited = True
        if edited:
            metadata["morphisms"] = [morphism for morphism in morphisms]
            path.write_text(records.record_text(metadata, document.content))
            changed.append(path)
    return tuple(changed)
