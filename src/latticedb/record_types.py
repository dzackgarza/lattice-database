"""Scalar, reference and morphism record types shared by lattice cards."""

from __future__ import annotations

import re
from collections.abc import Iterator
from datetime import date
from fractions import Fraction
from typing import Annotated, Literal, Self

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    ValidationError,
    model_validator,
)
from pydantic_core import InitErrorDetails, PydanticCustomError

type Yaml = None | bool | int | float | str | date | list[Yaml] | dict[str, Yaml]
"""A value that a YAML document can hold."""

type Vector = tuple[int, ...]
"""Coordinates of a lattice element in the chosen basis."""

type GramTensor = tuple[tuple[Fraction, ...], ...]
"""Components ``b(e_i,e_j)`` of the selected rational-valued bilinear form."""

_RATIONAL = re.compile(r"-?\d+(/[1-9]\d*)?")


def rational(value: Yaml | Fraction) -> Fraction:
    """Read an integer, or a string `p/q`, as an exact rational. Floats are refused."""
    match value:
        case Fraction():
            return value
        case bool():
            raise PydanticCustomError(
                "rational_type",
                "a rational is an integer or a string 'p/q', not a boolean",
            )
        case int():
            return Fraction(value)
        case str() if _RATIONAL.fullmatch(value):
            return Fraction(value)
        case str():
            raise PydanticCustomError(
                "rational_parsing",
                "'{value}' is not of the form 'p/q'",
                {"value": value},
            )
        case _:
            raise PydanticCustomError("rational_type", "a rational is an integer or a string 'p/q'")


Rational = Annotated[Fraction, BeforeValidator(rational)]
Tag = Annotated[str, Field(pattern=r"^[0-9A-Z]{4,}$")]
Slug = Annotated[str, Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")]
Family = Annotated[str, Field(pattern=r"^[a-z0-9]+(-[a-z0-9]+)*$")]
AdeType = Annotated[str, Field(pattern=r"^(A[1-9]\d*|D[4-9]|D[1-9]\d+|E[678])$")]
RootType = Annotated[str, Field(pattern=r"^(A[1-9]\d*|B[2-9]|B[1-9]\d+|C[3-9]|C[1-9]\d+|D[4-9]|D[1-9]\d+|E[678]|F4|G2)$")]
IntegerVector = Annotated[tuple[int, ...], Field(strict=False)]
VectorList = Annotated[tuple[IntegerVector, ...], Field(strict=False)]
Cardinality = Annotated[int, Field(gt=0)] | Literal["aleph0"] | None
Definiteness = Literal[
    "positive_definite",
    "negative_definite",
    "indefinite",
    "positive_semidefinite",
    "negative_semidefinite",
    "zero",
]


def _problem(
    kind: str,
    message: str,
    location: tuple[str, ...],
    context: dict[str, str | int] | None = None,
) -> InitErrorDetails:
    return InitErrorDetails(type=PydanticCustomError(kind, message, context), loc=location, input=None)


class Record(BaseModel):
    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        frozen=True,
        arbitrary_types_allowed=True,
    )


class Related(Record):
    tag: Tag = Field(description="Tag of another lattice in the catalogue.")
    relation: str = Field(description="One sentence that states how that lattice is related to this one.")


class Summand(Record):
    """A lattice $M(k)$: a record $M$ of the catalogue with its form scaled by a nonzero integer $k$.

    The summand names a lattice card and an additional scale used by this construction.
    The catalogue does not identify a lattice with its twists globally: $M$ and $M(k)$
    may both have cards.
    """

    tag: Tag = Field(description="Tag of the lattice $M$ in the catalogue.")
    scale: int = Field(description="The nonzero integer $k$: the summand is $M$ with the form $k b_M$.")

    @model_validator(mode="after")
    def _nonzero_scale(self) -> Self:
        if self.scale == 0:
            problem = _problem(
                "summand_scale_zero",
                "M(0) has the zero form and is not a summand of a root sublattice",
                ("scale",),
            )
            raise ValidationError.from_exception_data(type(self).__name__, [problem])
        return self


class Reference(Record):
    citation: str = Field(description="Bibliographic citation as plain text.")
    url: str | None = Field(default=None, description="Address of the source, when it has one.")


class Morphism(Record):
    """A stored morphism whose domain is the lattice card that contains it."""

    target: Tag = Field(description="Tag of the codomain lattice $T$.")
    name: str = Field(description="Name as plain text; TeX between `$` signs is rendered.")
    description: str | None = Field(
        default=None,
        description="One or two sentences on the morphism, as plain text with TeX between `$` signs.",
    )
    matrix: Annotated[tuple[IntegerVector, ...], Field(strict=False, min_length=1)] = Field(
        description=(
            "Matrix with $\\operatorname{rank} T$ rows and $\\operatorname{rank} S$ columns: column $j$ lists the coordinates of $\\varphi(e_j)$ in the chosen basis of $T$."
        )
    )
    scale: int | None = Field(
        default=None,
        description="When stated by the source, the nonzero integer $c$ with $b_T(\\varphi x, \\varphi y) = c b_S(x, y)$.",
    )
    row_subdivisions: IntegerVector = Field(default=())
    column_subdivisions: IntegerVector = Field(default=())

    @model_validator(mode="after")
    def _well_defined(self) -> Self:
        columns = len(self.matrix[0])
        problems: list[InitErrorDetails] = []
        if columns == 0 or any(len(row) != columns for row in self.matrix):
            problems.append(
                _problem(
                    "matrix_shape",
                    "the rows of the matrix are nonempty and have one length",
                    ("matrix",),
                )
            )
        if self.scale == 0:
            problems.append(
                _problem(
                    "scale_nonzero",
                    "the scale c of a morphism S(c) -> T is not zero",
                    ("scale",),
                )
            )
        problems.extend(_subdivision_problems(self.row_subdivisions, len(self.matrix), ("row_subdivisions",)))
        problems.extend(_subdivision_problems(self.column_subdivisions, columns, ("column_subdivisions",)))
        if problems:
            raise ValidationError.from_exception_data(type(self).__name__, problems)
        return self

    @property
    def images(self) -> tuple[Vector, ...]:
        """The columns of the matrix: the coordinates of the images of the source basis."""
        return tuple(zip(*self.matrix, strict=True))


def _subdivision_problems(lines: Vector, size: int, location: tuple[str, ...]) -> Iterator[InitErrorDetails]:
    if any(not 0 < line < size for line in lines) or any(first >= second for first, second in zip(lines, lines[1:], strict=False)):
        yield _problem(
            "subdivision_range",
            "the lines increase strictly and each lies strictly between 0 and {size}",
            location,
            {"size": size},
        )
