"""Match published catalogue rows against complete stored collection queries."""

from __future__ import annotations

from pydantic import Field

from latticedb.model import Record

type Cell = str | int | float | bool | None | list[str]
type Row = dict[str, Cell]


class Collection(Record):
    """A page that lists the lattices whose database row satisfies `where`."""

    title: str = Field(description="Title of the page. Dollar signs mark TeX.")
    summary: str = Field(description="One sentence that says which lattices the page lists. Dollar signs mark TeX.")
    where: dict[str, int | str | bool | list[str]] = Field(
        description=(
            "Key of a row of `lattices.json` -> required value. A lattice is listed when every condition holds. "
            "For a key whose value is a list, such as `properties`, the list must contain the required value, or each of the required values."
        )
    )


def matches_collection(record: Row, collection: Collection) -> bool:
    """Apply every stored collection constraint to one published row."""
    for key, required in collection.where.items():
        match record[key], required:
            case list() as values, list() as wanted:
                if not all(item in values for item in wanted):
                    return False
            case list() as values, _:
                if required not in values:
                    return False
            case value, _:
                if value != required:
                    return False
    return True
