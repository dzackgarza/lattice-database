"""Derived indices of stored relations, with all lattice mathematics delegated to preamble."""

from __future__ import annotations

from collections.abc import Sequence

from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import session_ring_objects
from pydantic import TypeAdapter

from latticedb.corpus import Entry
from latticedb.model import Lattice

ZZ = session_ring_objects()["ZZ"]


def hyperbolic_planes(lattice: Lattice) -> int | None:
    """Return ``n`` when the card represents ``U^n``; recognition is preamble-owned."""
    if lattice.integral is None or lattice.gram_tensor is None:
        return None
    result = Lattices(ZZ)(lattice.gram_tensor).hyperbolic_plane_power_if_even_unimodular()
    return TypeAdapter(int | None).validate_python(result, strict=True)


def hyperbolic_index_bounds(entries: Sequence[Entry]) -> dict[str, int]:
    """Index stored embeddings ``U^n -> T`` as lower bounds for the targets."""
    by_tag = {entry.lattice.tag: entry.lattice for entry in entries}
    bounds: dict[str, int] = {}
    for entry in entries:
        source = entry.lattice
        if not source.morphisms:
            continue
        planes = hyperbolic_planes(source)
        if planes is None:
            continue
        for morphism in source.morphisms:
            if morphism.target in by_tag and morphism.scale is None:
                raise ValueError("morphism scale must be stated before deriving hyperbolic index bounds")
            if morphism.scale == 1 and morphism.target in by_tag:
                bounds[morphism.target] = max(planes, bounds.get(morphism.target, 0))
    return bounds
