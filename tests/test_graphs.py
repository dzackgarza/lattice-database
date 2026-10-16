"""Graph-card scalar parsing preserves declared integer data."""

from __future__ import annotations

from pathlib import Path

import frontmatter
import pytest

from latticedb.graphs import WeightedGraph

ROOT = Path(__file__).resolve().parents[1]


def test_cartan_matrix_refuses_fraction_strings_instead_of_truncating_them() -> None:
    metadata = frontmatter.load(ROOT / "graphs" / "b2-root-diagram.md").metadata
    metadata["edges"][0]["weight"]["cartan"][0] = "1/2"
    graph = WeightedGraph.model_validate(metadata)
    with pytest.raises(ValueError, match="invalid literal for int"):
        graph.cartan_matrix()


def test_root_gram_refuses_string_cartan_entries_at_the_integer_boundary() -> None:
    metadata = frontmatter.load(ROOT / "graphs" / "b2-root-diagram.md").metadata
    metadata["edges"][0]["weight"]["cartan"] = [str(entry) for entry in metadata["edges"][0]["weight"]["cartan"]]
    graph = WeightedGraph.model_validate(metadata)
    with pytest.raises(TypeError, match="Cartan entries must be integers"):
        graph.vinberg_invariant_matrix()
