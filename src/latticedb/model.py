"""The schema of the record of one lattice.

A lattice here is a free module of finite rank over the integers with a
symmetric bilinear form `b` that takes rational values. The Gram tensor of
the lattice is `b`, a symmetric (0,2)-tensor; a record gives its components
`b(e_i, e_j)` in a basis. The form is not assumed positive definite,
integral, or nondegenerate.

A record is static. Enrichment may ask the research preamble for additional
mathematical values and serialize the returned results; reading a record checks
only schema shape and stored-field coherence. It does not infer whether a
mathematical hypothesis holds from other stored invariants.

Invariants that exist only under a hypothesis live in a block named for the
hypothesis (`integral`, `definite`, `indefinite`, `hyperbolic`).
"""

from collections.abc import Iterator
from typing import Annotated, Self

from pydantic import Field, ValidationError, model_validator
from pydantic_core import InitErrorDetails

from latticedb.invariant_models import (
    ChamberData as ChamberData,
)
from latticedb.invariant_models import (
    DefiniteData as DefiniteData,
)
from latticedb.invariant_models import (
    DiscriminantSequenceData as DiscriminantSequenceData,
)
from latticedb.invariant_models import (
    FormData as FormData,
)
from latticedb.invariant_models import (
    GroupData as GroupData,
)
from latticedb.invariant_models import (
    HyperbolicData as HyperbolicData,
)
from latticedb.invariant_models import (
    IndefiniteData as IndefiniteData,
)
from latticedb.invariant_models import (
    IntegralData as IntegralData,
)
from latticedb.invariant_models import (
    LocalDensities as LocalDensities,
)
from latticedb.invariant_models import (
    LocalRepresentation as LocalRepresentation,
)
from latticedb.invariant_models import (
    OrbitCounts as OrbitCounts,
)
from latticedb.invariant_models import (
    OrbitGroup as OrbitGroup,
)
from latticedb.invariant_models import (
    OrbitRepresentatives as OrbitRepresentatives,
)
from latticedb.invariant_models import (
    PrimitiveOrbitSeries as PrimitiveOrbitSeries,
)
from latticedb.invariant_models import (
    QSeriesPrefix as QSeriesPrefix,
)
from latticedb.invariant_models import (
    RootSpan as RootSpan,
)
from latticedb.invariant_models import (
    RootSublattice as RootSublattice,
)
from latticedb.invariant_models import (
    RootSystemComponent as RootSystemComponent,
)
from latticedb.invariant_models import (
    SquareClassRepresentation as SquareClassRepresentation,
)
from latticedb.invariant_models import (
    StabilizedObject as StabilizedObject,
)
from latticedb.invariant_models import (
    series_bound as series_bound,
)
from latticedb.record_types import (
    AdeType as AdeType,
)
from latticedb.record_types import (
    Cardinality as Cardinality,
)
from latticedb.record_types import (
    Definiteness as Definiteness,
)
from latticedb.record_types import (
    Family as Family,
)
from latticedb.record_types import (
    GramTensor as GramTensor,
)
from latticedb.record_types import (
    IntegerVector as IntegerVector,
)
from latticedb.record_types import (
    Morphism as Morphism,
)
from latticedb.record_types import (
    Rational as Rational,
)
from latticedb.record_types import (
    Record as Record,
)
from latticedb.record_types import (
    Reference as Reference,
)
from latticedb.record_types import (
    Related as Related,
)
from latticedb.record_types import (
    RootType as RootType,
)
from latticedb.record_types import (
    Slug as Slug,
)
from latticedb.record_types import (
    Summand as Summand,
)
from latticedb.record_types import (
    Tag as Tag,
)
from latticedb.record_types import (
    Vector as Vector,
)
from latticedb.record_types import (
    VectorList as VectorList,
)
from latticedb.record_types import (
    Yaml as Yaml,
)
from latticedb.record_types import _problem
from latticedb.record_types import (
    rational as rational,
)


class Lattice(Record):
    tag: Tag = Field(description="Permanent identifier: at least four characters from 0-9 and A-Z. The file name is the tag.")
    name: str = Field(description="Name as plain text, for search.")
    latex: str = Field(description="Name as TeX, without math delimiters.")
    aliases: Annotated[tuple[str, ...], Field(strict=False)] = Field(default=(), description="Other names, as plain text.")
    certifications: dict[str, str] = Field(
        default_factory=dict,
        description=(
            "Completed computations cited by computation name. Each value is the SHA-256 certificate hash of that computation on this card's Gram tensor and stored result."
        ),
    )
    rank: int | None = Field(
        default=None,
        ge=1,
        description="Rank of the underlying free module, when the source states it.",
    )
    gram_tensor: (
        Annotated[
            tuple[Annotated[tuple[Rational, ...], Field(strict=False)], ...],
            Field(strict=False),
        ]
        | None
    ) = Field(
        default=None,
        description=(
            "Components of the Gram tensor, the symmetric (0,2)-tensor $b$, in a basis $e_1, \\dots, e_n$: "
            "row $i$ lists $b(e_i, e_1), \\dots, b(e_i, e_n)$. Values are integers or strings `p/q`."
        ),
    )
    signature: Annotated[tuple[int, int], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "`[n_plus, n_minus]`: the numbers of $v$ with $b(v, v) > 0$ and with $b(v, v) < 0$ in a $b$-orthogonal basis of $L \\otimes \\mathbb{Q}$. "
            "They do not depend on the basis (Sylvester's law of inertia)."
        ),
    )
    determinant: Rational | None = Field(
        default=None,
        description="$\\det(b(e_i, e_j))$. It is the same for every basis of $L$.",
    )
    definiteness: Definiteness | None = Field(
        default=None,
        description=(
            "`positive_definite` or `negative_definite` when $b(x, x)$ has one sign on nonzero $x$; `indefinite` when it takes both signs; "
            "`positive_semidefinite` when $b(x, x) \\geq 0$ for all $x$, $b \\neq 0$ and the determinant is zero, "
            "and `negative_semidefinite` with $\\leq$; `zero` when $b = 0$."
        ),
    )
    dual_gram_tensor: (
        Annotated[
            tuple[Annotated[tuple[Rational, ...], Field(strict=False)], ...],
            Field(strict=False),
        ]
        | None
    ) = Field(
        default=None,
        description=(
            "Components of the inverse Gram tensor, the Gram tensor $b^*$ of the dual lattice $L^*$ in the basis dual to $e_1, \\dots, e_n$: "
            "row $i$ lists $b^*(e^i, e^1), \\dots, b^*(e^i, e^n)$. Values are integers or strings `p/q`. "
            "Computed by `latticedb enrich` from the Gram tensor; it requires a nonzero determinant."
        ),
    )
    families: Annotated[tuple[Family, ...], Field(strict=False)] = Field(default=(), description="Named families that contain the lattice.")
    related: Annotated[tuple[Related, ...], Field(strict=False)] = Field(default=(), description="Related lattices in the catalogue.")
    references: Annotated[tuple[Reference, ...], Field(strict=False)] = Field(default=(), description="Literature for the lattice.")
    form: FormData | None = Field(default=None, description=FormData.__doc__)
    integral: IntegralData | None = Field(default=None, description=IntegralData.__doc__)
    definite: DefiniteData | None = Field(default=None, description=DefiniteData.__doc__)
    indefinite: IndefiniteData | None = Field(default=None, description=IndefiniteData.__doc__)
    hyperbolic: HyperbolicData | None = Field(default=None, description=HyperbolicData.__doc__)
    root_span: RootSpan | None = Field(default=None, description=RootSpan.__doc__)
    root_sublattice: RootSublattice | None = Field(default=None, description=RootSublattice.__doc__)
    morphisms: Annotated[tuple[Morphism, ...], Field(strict=False)] = Field(
        default=(),
        description="Stored morphisms whose domain is this lattice card; each morphism names its codomain lattice by tag.",
    )
    orthogonal_group: Slug | None = Field(
        default=None,
        description="Arithmetic-group card for the canonical integral orthogonal group O(L), when that group has a stored card.",
    )
    arithmetic_groups: Annotated[tuple[Slug, ...], Field(strict=False)] = Field(
        default=(),
        description="Arithmetic-group cards attached to this lattice, including `orthogonal_group` when it is stored.",
    )

    @property
    def nullity(self) -> int | None:
        return None if self.rank is None or self.signature is None else self.rank - self.signature[0] - self.signature[1]

    @model_validator(mode="after")
    def _well_defined(self) -> Self:
        """Verify only structural and cross-field coherence of a parsed card."""
        problems = list(self._shape_problems())
        if not problems:
            problems = [
                *self._integral_problems(),
                *self._definite_problems(),
                *self._root_problems(),
                *self._dual_problems(),
            ]
        if problems:
            raise ValidationError.from_exception_data(type(self).__name__, problems)
        return self

    def _shape_problems(self) -> Iterator[InitErrorDetails]:
        if self.form is not None and self.form.integer_valued is False and self.integral is not None:
            yield _problem("integrality_conflict", "a non-integer-valued form cannot carry the integral hypothesis", ("integral",))
        rank = self.rank
        if rank is not None and self.gram_tensor is not None and (len(self.gram_tensor) != rank or any(len(row) != rank for row in self.gram_tensor)):
            yield _problem(
                "gram_tensor_shape",
                "a (0,2)-tensor on a module of rank {rank} has {rank} rows of {rank} components",
                ("gram_tensor",),
                {"rank": rank},
            )
        if self.signature is not None and (min(self.signature) < 0 or (rank is not None and sum(self.signature) > rank)):
            yield _problem(
                "signature_shape",
                "n_plus and n_minus are nonnegative and their sum does not exceed the rank when stated",
                ("signature",),
            )

    def _integral_problems(self) -> Iterator[InitErrorDetails]:
        if self.integral is None:
            return
        if self.integral.discriminant_sequence is not None:
            if tuple(self.integral.discriminant_sequence.discriminant_factors) != self.integral.discriminant_group:
                yield _problem(
                    "discriminant_sequence_factors",
                    "the discriminant sequence must use the stated invariant factors",
                    ("integral", "discriminant_sequence", "discriminant_factors"),
                )
        yield from self._spinor_problems()
        yield from self._local_problems()

    def _local_problems(self) -> Iterator[InitErrorDetails]:
        """Structural conditions on stored local data: primes dividing `2 det L` in increasing order, and one entry per square class."""
        assert self.integral is not None
        data = self.integral
        for field, primes in (
            ("anisotropic_primes", data.anisotropic_primes),
            ("local_representations", None if data.local_representations is None else tuple(entry.prime for entry in data.local_representations)),
            ("local_densities", None if data.local_densities is None else tuple(entry.prime for entry in data.local_densities)),
        ):
            if primes is not None and (any(prime < 2 for prime in primes) or any(first >= second for first, second in zip(primes, primes[1:], strict=False))):
                yield _problem(
                    "local_primes_order",
                    "the primes increase strictly",
                    ("integral", field),
                )
            if primes is not None and self.determinant is not None and self.determinant != 0 and any((2 * self.determinant) % prime != 0 for prime in primes):
                yield _problem(
                    "local_primes_divide_2_det",
                    "every listed prime divides 2 det L",
                    ("integral", field),
                )
        for position, entry in enumerate(data.local_representations or ()):
            representatives = tuple(found.representative for found in entry.classes)
            expected = 8 if entry.prime == 2 else 4
            if (
                len(set(representatives)) != len(representatives)
                or len(representatives) > expected
                or (entry.prime == 2 and not set(representatives) <= {1, 3, 5, 7, 2, 6, 10, 14})
            ):
                yield _problem(
                    "square_classes_shape",
                    "the prime {prime} has {expected} square classes, and each listed class is listed once by its representative",
                    ("integral", "local_representations", str(position)),
                    {"prime": entry.prime, "expected": expected},
                )
            for found in entry.classes:
                odd_valuation = found.representative % entry.prime == 0
                if found.least_valuation % 2 != int(odd_valuation):
                    yield _problem(
                        "square_class_valuation_parity",
                        "the least valuation of the class of {representative} has the parity of the valuation of {representative}",
                        ("integral", "local_representations", str(position)),
                        {"representative": found.representative},
                    )

    def _dual_problems(self) -> Iterator[InitErrorDetails]:
        """Structural conditions on a stored dual Gram tensor."""
        if self.dual_gram_tensor is None:
            return
        if self.gram_tensor is None or self.rank is None:
            yield _problem(
                "dual_gram_requires_gram",
                "the dual Gram tensor requires the Gram tensor",
                ("dual_gram_tensor",),
            )
            return
        dual = self.dual_gram_tensor
        if len(dual) != self.rank or any(len(row) != self.rank for row in dual):
            yield _problem(
                "dual_gram_shape",
                "a (0,2)-tensor on a module of rank {rank} has {rank} rows of {rank} components",
                ("dual_gram_tensor",),
                {"rank": self.rank},
            )
            return

    def _spinor_problems(self) -> Iterator[InitErrorDetails]:
        """Structural conditions on stored spinor-genus data."""
        assert self.integral is not None
        count, genera = self.integral.spinor_genus_count, self.integral.spinor_genera
        if count is None and genera is None:
            return
        if genera is None:
            return
        location = ("integral", "spinor_genera")
        if count is not None and len(genera) != count:
            yield _problem(
                "spinor_genera_count",
                "{listed} spinor genera are listed, and there are {count}",
                location,
                {"listed": len(genera), "count": count},
            )

    def _definite_problems(self) -> Iterator[InitErrorDetails]:
        if self.definite is None:
            return
        data = self.definite
        generator_names = data.automorphism_group_generator_morphisms
        if generator_names is not None:
            self_isometry_names = [morphism.name for morphism in self.morphisms if morphism.target == self.tag and morphism.scale == 1]
            if len(set(generator_names)) != len(generator_names) or any(self_isometry_names.count(name) != 1 for name in generator_names):
                yield _problem(
                    "automorphism_group_generators",
                    "each generator name occurs once in the generator list and names exactly one isometry L -> L (a morphism entry with scale 1) on this lattice card",
                    ("definite", "automorphism_group_generator_morphisms"),
                )
        yield from self._theta_problems()
        if data.roots is not None and any(
            len(component.simple_roots) != component.rank or (self.rank is not None and any(len(row) != self.rank for row in component.simple_roots))
            for component in data.roots
        ):
            yield _problem(
                "roots_shape",
                "a component of rank m has m simple roots, each with the stated lattice rank of coordinates when known",
                ("definite", "roots"),
            )
        if data.minimal_vectors is not None:
            vectors = data.minimal_vectors
            if (
                data.kissing_number is None
                or data.minimum is None
                or len(vectors) != data.kissing_number
                or len({tuple(v) for v in vectors}) != len(vectors)
                or (self.rank is not None and any(len(v) != self.rank for v in vectors))
            ):
                yield _problem(
                    "minimal_shell_shape",
                    "the complete minimal shell has distinct vectors of the lattice rank and the kissing number",
                    ("definite", "minimal_vectors"),
                )

    def _theta_problems(self) -> Iterator[InitErrorDetails]:
        """Structural conditions on the stored theta data: constant terms, and the cuspidal component as the stated difference."""
        assert self.definite is not None
        data = self.definite
        if data.genus_theta_series is not None and data.genus_theta_series[:1] != (1,):
            yield _problem(
                "genus_theta_constant",
                "the genus theta series has constant term 1, the weighted average of the constant terms 1",
                ("definite", "genus_theta_series"),
            )
        cuspidal = data.theta_series_cuspidal_component
        if cuspidal is None:
            return
        if cuspidal[:1] != (0,):
            yield _problem(
                "cuspidal_constant",
                "the cuspidal component has constant term 0",
                ("definite", "theta_series_cuspidal_component"),
            )
        if (
            data.theta_series is not None
            and data.genus_theta_series is not None
            and any(difference != own - average for difference, own, average in zip(cuspidal, data.theta_series, data.genus_theta_series, strict=False))
        ):
            yield _problem(
                "cuspidal_difference",
                "each entry of the cuspidal component is the entry of `theta_series` minus the entry of `genus_theta_series`",
                ("definite", "theta_series_cuspidal_component"),
            )

    def _root_problems(self) -> Iterator[InitErrorDetails]:
        span = self.root_span
        if span is not None:
            if self.definite is not None:
                yield _problem(
                    "root_span_on_definite",
                    "`definite.roots` states the roots of a definite lattice, so the `root_span` block is an error there",
                    ("root_span",),
                )
            if self.rank is not None and any(len(row) != self.rank for row in (*span.roots, *(span.embedding or ()))):
                yield _problem(
                    "root_span_shape",
                    "each row lists {rank} coordinates",
                    ("root_span",),
                    {"rank": self.rank},
                )
            if len(span.norms) != len(span.roots):
                yield _problem(
                    "root_span_norms_shape",
                    "`norms` has one entry for each row of `roots`",
                    ("root_span", "norms"),
                )
            if (span.summands is None) != (span.embedding is None):
                yield _problem(
                    "root_span_representative_incomplete",
                    "`summands` and `embedding` are stated together",
                    ("root_span",),
                )
        sublattice = self.root_sublattice
        decided = (self.definite is not None and self.definite.roots is not None) or span is not None
        if sublattice is None:
            return
        if not decided:
            yield _problem(
                "root_sublattice_not_decided",
                "the `root_sublattice` block requires stored `definite.roots` or `root_span` data",
                ("root_sublattice",),
            )
            return
        factors = sublattice.invariant_factors
        if (
            (self.rank is not None and len(factors) > self.rank)
            or any(d < 1 for d in factors)
            or any(second % first != 0 for first, second in zip(factors, factors[1:], strict=False))
        ):
            message = "positive invariant factors, each dividing the next, numbering at most the lattice rank when stated"
            yield _problem(
                "root_sublattice_factors_shape",
                message,
                ("root_sublattice", "invariant_factors"),
            )
