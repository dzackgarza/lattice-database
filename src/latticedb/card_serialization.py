"""Read and serialize lattice-card metadata without changing its stored values."""

from __future__ import annotations

from fractions import Fraction

import yaml

from latticedb import model
from latticedb.model import GramTensor, Yaml

KEYS = (
    "tag",
    "name",
    "latex",
    "aliases",
    "certifications",
    "rank",
    "gram_tensor",
    "signature",
    "determinant",
    "definiteness",
    "dual_gram_tensor",
    "form",
    "integral",
    "definite",
    "indefinite",
    "root_span",
    "root_sublattice",
    "morphisms",
    "orthogonal_group",
    "arithmetic_groups",
    "families",
    "related",
    "references",
    "hyperbolic",
)
"""The keys of a record, in the order in which a record lists them."""


class Flow(list[Yaml]):
    """A list that YAML writes on one line."""


yaml.add_representer(
    Flow,
    lambda dumper, data: dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=True),
)


def _is_scalar(value: Yaml) -> bool:
    match value:
        case list() | dict():
            return False
        case _:
            return True


def _styled(value: Yaml) -> Yaml:
    """Return the value with each list of scalars as a `Flow`: the layout of a record."""
    match value:
        case dict():
            return {key: _styled(item) for key, item in value.items()}
        case list() if all(_is_scalar(item) for item in value):
            return Flow(value)
        case list():
            return [_styled(item) for item in value]
        case _:
            return value


def record_text(record: dict[str, Yaml], prose: str) -> str:
    """Return the text of the file of a record."""
    assert set(record) <= set(KEYS), set(record) - set(KEYS)
    ordered = {key: _styled(record[key]) for key in KEYS if key in record}
    return "---\n" + yaml.dump(ordered, sort_keys=False, allow_unicode=True, width=100000) + "---\n" + _body(prose)


def _body(prose: str) -> str:
    """The prose after the front matter, in the form the Markdown formatter flowmark keeps.

    That is two blank lines when there is no prose, else a blank line and the prose.
    """
    return "\n" + prose + "\n" if prose else "\n\n"


MORPHISM_KEYS = (
    "target",
    "name",
    "description",
    "matrix",
    "scale",
    "row_subdivisions",
    "column_subdivisions",
)
"""The keys of a morphism, in the order in which a lattice card lists them."""


def rational(value: Fraction) -> int | str:
    """Return the value as a record writes it: an integer, or a string `p/q`."""
    return int(value) if value.denominator == 1 else str(value)


def gram_tensor(rows: Yaml) -> GramTensor:
    """Read the `gram_tensor` field of a record: rows of integers or strings `p/q`."""
    match rows:
        case list():
            return tuple(_row(row) for row in rows)
        case _:
            raise AssertionError("gram_tensor is a list of rows")


def _row(row: Yaml) -> tuple[Fraction, ...]:
    match row:
        case list():
            return tuple(model.rational(value) for value in row)
        case _:
            raise AssertionError("each row of gram_tensor is a list")


def _block(record: dict[str, Yaml], key: str) -> dict[str, Yaml]:
    match record.get(key):
        case dict() as block:
            return block
        case _:
            return {}


def _ordered(block: dict[str, Yaml], fields: tuple[str, ...]) -> dict[str, Yaml]:
    assert set(block) <= set(fields), set(block) - set(fields)
    return {field: block[field] for field in fields if field in block}
