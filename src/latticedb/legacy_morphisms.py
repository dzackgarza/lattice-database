"""Migrate the imported card format's declared implicit morphism scales.

At revision 287b70c9791a898e35a9400fd57b276ef599812d, Morphism.scale was
an integer with default 1 (src/latticedb/model.py). The subsequent schema
split made an omitted scale unknown without migrating the stored cards.
This reader restores only declarations matched in that immutable source;
it neither infers a scale from a matrix nor assigns one to a new morphism.

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


def restore(root: Path, archive: Path) -> tuple[Path, ...]:
    """Make the historical declarations explicit on matching current cards."""
    archived = subprocess.check_output(["git", "-C", str(archive), "grep", "-l", "^morphisms:", REVISION, "--", "lattices"], text=True).splitlines()
    changed: list[Path] = []
    for source_path in archived:
        relative = source_path.split(":", 1)[1]
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
        original = frontmatter.loads(subprocess.check_output(["git", "-C", str(archive), "show", f"{REVISION}:{relative}"], text=True))
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
