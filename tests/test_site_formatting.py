"""Publication of source-card coordinates through the schema boundary."""

from __future__ import annotations

import pytest

from latticedb.model import Lattice
from latticedb.site_formatting import summand_images


def test_root_span_images_require_the_source_card_to_state_its_rank() -> None:
    ambient = Lattice.model_validate(
        {
            "tag": "0001",
            "name": "Ambient card",
            "latex": "L",
            "root_span": {
                "roots": [[1]],
                "norms": [2],
                "embedding": [[1]],
                "summands": [{"tag": "0002", "scale": 1}],
            },
        }
    )
    source = Lattice.model_validate({"tag": "0002", "name": "Sparse source card", "latex": "M"})
    with pytest.raises(ValueError, match="summand 0002 images require a stated source rank"):
        summand_images(ambient, {"0002": source})


def test_collection_queries_preserve_all_row_constraints() -> None:
    from latticedb.collection_query import Collection, matches_collection

    query = Collection.model_validate({"title": "selected", "summary": "selected rows", "where": {"rank": 2, "even": True, "properties": ["integral", "definite"]}})
    assert matches_collection({"rank": 2, "even": True, "properties": ["definite", "integral", "unimodular"]}, query)
    assert not matches_collection({"rank": 3, "even": True, "properties": ["definite", "integral"]}, query)
    assert not matches_collection({"rank": 2, "even": False, "properties": ["definite", "integral"]}, query)
    assert not matches_collection({"rank": 2, "even": True, "properties": ["integral"]}, query)
    scalar_query = Collection.model_validate({"title": "integral", "summary": "integral rows", "where": {"properties": "integral"}})
    assert matches_collection({"properties": ["integral"]}, scalar_query)
    assert not matches_collection({"properties": ["definite"]}, scalar_query)
