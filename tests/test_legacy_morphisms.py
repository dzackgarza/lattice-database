"""Preserve the declarations of the imported card format across schema changes."""

import subprocess
from pathlib import Path

import frontmatter

from latticedb import legacy_morphisms

REPOSITORY = Path(__file__).resolve().parent.parent


def test_imported_implicit_scales_become_explicit_without_changing_scaled_maps(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    path = tmp_path / "lattices" / "0001.md"
    path.write_text(subprocess.check_output(["git", "-C", str(REPOSITORY), "show", "287b70c9791a898e35a9400fd57b276ef599812d:lattices/0001.md"], text=True))
    original = frontmatter.load(str(path)).metadata["morphisms"]
    assert "scale" not in original[0]
    scaled = [morphism for morphism in original if morphism.get("scale") == 2]
    assert scaled
    document = frontmatter.load(str(path))
    document.metadata["morphisms"].append({"target": "0011", "name": "Authored after import", "matrix": [[1], [0]]})
    path.write_text(frontmatter.dumps(document))
    legacy_morphisms.restore(tmp_path, REPOSITORY)
    migrated = frontmatter.load(str(path)).metadata["morphisms"]
    assert migrated[0]["scale"] == 1
    assert [morphism for morphism in migrated if morphism.get("scale") == 2] == scaled
    assert "scale" not in migrated[-1]
    assert legacy_morphisms.restore(tmp_path, REPOSITORY) == ()
