"""Stored invariant blocks of lattice cards, without mathematical recomputation."""

from __future__ import annotations

from typing import Annotated, Literal, Self

from pydantic import Field, model_validator

from latticedb.record_types import (
    AdeType,
    Cardinality,
    IntegerVector,
    Rational,
    Record,
    Reference,
    RootType,
    Summand,
    VectorList,
)

OrbitGroup = Literal["O", "O+", "SO", "SO+", "Otilde", "Otilde+", "SOtilde", "SOtilde+"]
"""A subgroup $\\Gamma$ of $O(L)$: $S$ is the kernel of the determinant, `+` the kernel of the real spinor norm, and `tilde` the kernel of the action on $A_L$."""


OrbitCounts = Annotated[tuple[Annotated[int, Field(ge=0)] | None, ...], Field(strict=False)]


class PrimitiveOrbitSeries(Record):
    """The series $F_{L,\\Gamma}(z, w) = c_\\Gamma(0) + \\sum_{n \\geq 1} c_\\Gamma(n) z^n + \\sum_{n \\geq 1} c_\\Gamma(-n) w^n$ in $\\mathbb{Z}[[z, w]]$.

    $c_\\Gamma(n)$ is the number of $\\Gamma$-orbits on the primitive vectors $v$ with $b(v, v) = n$. A coefficient that is not known is null.
    """

    constant: Annotated[int, Field(ge=0)] | None = Field(
        default=None,
        description="$c_\\Gamma(0)$, the number of orbits of primitive isotropic vectors.",
    )
    z: OrbitCounts = Field(
        default=(),
        description="$c_\\Gamma(1), c_\\Gamma(2), \\dots$: the coefficients of $z, z^2, \\dots$",
    )
    w: OrbitCounts = Field(
        default=(),
        description="$c_\\Gamma(-1), c_\\Gamma(-2), \\dots$: the coefficients of $w, w^2, \\dots$",
    )
    reference: Reference | None = Field(
        default=None,
        description="The source of the coefficients; absent when `latticedb certify` computes them.",
    )

    def coefficient(self, n: int) -> int | None:
        """$c_\\Gamma(n)$, or None when it is not stated."""
        if n == 0:
            return self.constant
        counts, index = (self.z, n - 1) if n > 0 else (self.w, -n - 1)
        return counts[index] if index < len(counts) else None

    @property
    def degrees(self) -> range:
        """The $n$ for which the series can state $c_\\Gamma(n)$."""
        return range(-len(self.w), len(self.z) + 1)


class StabilizedObject(Record):
    """The object a subgroup of $O(L)$ fixes, named by a card's slug."""

    kind: Literal["vector_orbit", "chamber", "geometric_object", "geometric_family", "embedding"]
    identifier: str = Field(min_length=1)


class ChamberData(Record):
    """A chamber in the real hyperbolic lattice: a fundamental domain of a reflection subgroup."""

    interior_vector: IntegerVector = Field(description="An interior point of the chamber, in the record basis.")
    wall_normals: tuple[IntegerVector, ...] = Field(
        strict=False,
        description="One inward normal for each wall of the chamber, in the record basis.",
    )


class OrbitRepresentatives(Record):
    """Orbit representatives of the primitive vectors of one norm: one vector per $\\Gamma$-orbit, in the record basis."""

    square: int = Field(description="The norm $n = b(v, v)$ of each representative in this group.")
    representatives: VectorList = Field(
        strict=False,
        description="One primitive vector of norm $n$ for each $\\Gamma$-orbit, in the record basis.",
    )


class GroupData(Record):
    """A subgroup $\\Gamma \\leq O(L)$: its structure, its relation to $O(L)$, and the primitive-vector orbits it defines.
    $O$, $SO$, $O^+$, $SO^+$, $\\widetilde{O}$, $\\widetilde{SO}$, $\\widetilde{O}^+$ and $\\widetilde{SO}^+$ carry their series
    in `integral.primitive_orbits`; a key here names either one of those, extending it with generators, relators or representatives, or a further
    named subgroup such as $\\Gamma_{\\mathrm{En},2}$.
    """

    cardinality: Cardinality = Field(
        default=None,
        description=(
            "The cardinality $|\\Gamma|$ of $\\Gamma$: a positive integer $n$ when $\\Gamma$ is finite, or `aleph0` when it is "
            "countably infinite. A subgroup of $\\mathrm{GL}_n(\\mathbb{Z})$ is countable, so its cardinality is $n$ or $\\aleph_0$. "
            "A lattice of signature $(2, n)$ has a countably infinite $O(L)$, by the Eichler transvections "
            "$t(c, a) = v \\mapsto v - (a, v) c$ for a primitive isotropic $c$; its subgroups of finite index are infinite too."
        ),
    )

    index_in_orthogonal_group: Annotated[int, Field(gt=0)] | None = Field(default=None, description="The index $[O(L) : \\Gamma]$.")
    parent: str | None = Field(
        default=None,
        description="The key of a containing subgroup of the same lattice.",
    )
    generator_morphisms: Annotated[tuple[str, ...], Field(strict=False)] | None = Field(
        default=None,
        description="Names of self-isometries in this lattice card's `morphisms` field that generate $\\Gamma$.",
    )
    defining_relators: tuple[Annotated[tuple[int, ...], Field(strict=False)], ...] | None = Field(
        default=None,
        strict=False,
        description="Words in the signed generators above, one generator index per entry, that present $\\Gamma$.",
    )
    abstract_structure: str | None = Field(default=None, description="The abstract group $\\Gamma$, as plain text.")
    stabilized: StabilizedObject | None = Field(
        default=None,
        description="A vector orbit, chamber, geometric object, family or embedding that $\\Gamma$ fixes.",
    )
    chamber: ChamberData | None = Field(
        default=None,
        description="A chamber of the real hyperbolic lattice that $\\Gamma$ reflects in, when $\\Gamma$ is a reflection subgroup.",
    )
    orbits: tuple[OrbitRepresentatives, ...] | None = Field(
        default=None,
        strict=False,
        description=(
            "Orbit representatives of the primitive vectors, grouped by the norm $n$: one vector for each $\\Gamma$-orbit, "
            "in the record basis. A group states a set of representatives, not necessarily all of them."
        ),
    )
    reference: Reference | None = Field(default=None, description="The source of the structure and the representatives.")


class DiscriminantSequenceData(Record):
    """A finite discriminant action, its kernel order, and its pointed coset quotient."""

    discriminant_factors: list[int]
    discriminant_basis_lifts: list[list[str]]
    discriminant_quadratic_gram: list[list[str]]
    discriminant_group_order: int = Field(gt=0)
    discriminant_generators: list[list[list[int]]]
    image_generators: list[list[list[int]]]
    image_order: int = Field(gt=0)
    kernel_order: Annotated[int, Field(gt=0)] | None = None
    coset_representatives: list[list[list[int]]]
    mm_trivial: bool
    image_normal: bool
    quotient_generator_cosets: list[int] | None = None
    quotient_multiplication: list[list[int]] | None = None
    quotient_invariant_factors: list[Annotated[int, Field(gt=1)]] | None = None
    mm_f2_dimension: Annotated[int, Field(ge=0)] | None = None

    @model_validator(mode="after")
    def _sequence(self) -> Self:
        size = len(self.discriminant_factors)
        matrices = [
            *self.discriminant_generators,
            *self.image_generators,
            *self.coset_representatives,
        ]
        if any(len(rows) != size or any(len(row) != size for row in rows) for rows in matrices):
            raise ValueError("discriminant isometry matrices must be square in the stated basis")
        if len(self.discriminant_basis_lifts) != size or len(self.discriminant_quadratic_gram) != size:
            raise ValueError("the discriminant basis and quadratic Gram matrix must match the invariant factors")
        if self.image_normal != (self.quotient_multiplication is not None and self.quotient_generator_cosets is not None):
            raise ValueError("quotient group data are present exactly when the image is normal")
        if self.quotient_multiplication is not None:
            count = len(self.coset_representatives)
            if len(self.quotient_multiplication) != count or any(len(row) != count for row in self.quotient_multiplication):
                raise ValueError("the quotient multiplication table must index the cosets")
            if any(value < 0 or value >= count for row in self.quotient_multiplication for value in row):
                raise ValueError("quotient products must index the stated cosets")
        if self.quotient_invariant_factors is not None and self.quotient_multiplication is None:
            raise ValueError("quotient invariant factors require stored quotient-group data")
        if self.mm_f2_dimension is not None and self.quotient_multiplication is None:
            raise ValueError("the F2 dimension requires stored quotient-group data")
        return self


QSeriesPrefix = Annotated[tuple[Rational, ...], Field(strict=False)]
"""Entry $k$ is the coefficient of $q^k$, for $k = 0, 1, 2, \\dots$ in order: the first terms of a power series in $q$."""


def series_bound(rank: int) -> int:
    """The exponent $N$ through which a card stores the series of a lattice of this rank.

    $N$ is 12, 8, 6 or 4 for rank at most 4, at most 8, at most 12, or greater: the number of
    vectors of norm at most $N$ grows like $N^{n/2}$ in rank $n$.
    """
    match rank:
        case _ if rank <= 4:
            return 12
        case _ if rank <= 8:
            return 8
        case _ if rank <= 12:
            return 6
        case _:
            return 4


class LocalDensities(Record):
    """The local densities $\\beta_p(L, m)$ of $L$ at one prime $p$."""

    prime: Annotated[int, Field(ge=2)] = Field(description="The prime $p$; it divides $2 \\det L$.")
    densities: QSeriesPrefix = Field(
        description=(
            "Entry $m - 1$ is $\\beta_p(L, m) = \\lim_{k \\to \\infty} p^{k(1-n)} \\#\\{x \\in L/p^k L : b(x, x) \\equiv m \\pmod{p^k}\\}$ "
            "for $m = 1, \\dots, N$ in order, where $n$ is the rank and $N$ is the bound of `theta_series`: "
            "12, 8, 6 or 4 for rank at most 4, at most 8, at most 12, or greater. "
            "Values are integers or strings `p/q`."
        )
    )


class SquareClassRepresentation(Record):
    """Which elements of one square class of $\\mathbb{Q}_p^\\times$ the local lattice $L \\otimes \\mathbb{Z}_p$ represents."""

    representative: Annotated[int, Field(gt=0)] = Field(
        description=(
            "The representative of the class: for $p = 2$ one of 1, 3, 5, 7, 2, 6, 10, 14; for odd $p$ one of $1$, $\\nu$, $p$, $p\\nu$, "
            "where $\\nu$ is the least positive quadratic nonresidue modulo $p$."
        )
    )
    least_valuation: Annotated[int, Field(ge=0)] = Field(
        description=(
            "The least $v$ such that $L \\otimes \\mathbb{Z}_p$ represents the elements of the class of valuation $v$. "
            "It then represents every element of the class of valuation $v + 2j$, $j \\geq 0$, and no other element of the class; "
            "$v$ has the parity of the valuation of the representative."
        )
    )


class LocalRepresentation(Record):
    """The nonzero $p$-adic integers that $L \\otimes \\mathbb{Z}_p$ represents, at a prime where it does not represent all of them."""

    prime: Annotated[int, Field(ge=2)] = Field(description="The prime $p$.")
    classes: Annotated[tuple[SquareClassRepresentation, ...], Field(strict=False)] = Field(
        description=(
            "One entry for each square class of $\\mathbb{Q}_p^\\times$ of which $L \\otimes \\mathbb{Z}_p$ represents some element, "
            "in the order the representatives are listed; it represents no element of a class that is not listed. "
            "There are eight square classes for $p = 2$ and four for odd $p$."
        )
    )


class FormData(Record):
    """Stored predicates of the lattice's bilinear form, including negative answers."""

    integer_valued: bool | None = Field(default=None, description="Whether the bilinear form takes values in the integers; null means unknown.")


class IntegralData(Record):
    """Stored invariants of an integer-valued lattice, when available."""

    elementary_primes: Annotated[tuple[Annotated[int, Field(ge=2)], ...], Field(strict=False, max_length=1)] | None = Field(
        default=None,
        description="The singleton [p] when the nontrivial discriminant group is elementary abelian of prime exponent p; [] when it is not; null means unknown.",
    )
    parity: Literal["even", "odd"] = Field(description="`even` when $b(x, x)$ is even for every $x$, `odd` otherwise.")
    level: Annotated[int, Field(gt=0)] | None = Field(
        default=None,
        description="Least positive $k$ for which $k b(x,x)$ is even for every $x$ in the dual lattice. Requires nonzero determinant.",
    )
    modular_scale: Literal[False] | Annotated[int, Field(gt=0)] | None = Field(
        default=None,
        description=(
            "The $k > 0$ with $L\\cong L^*(k)$, or `false` when there is no such $k$; "
            "an explicit chosen isometry, when stored, belongs to this card's morphisms rather than a separate object."
        ),
    )
    discriminant_group: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Invariant factors $d_1 \\mid d_2 \\mid \\dots$, each greater than 1, of the cokernel of the correlation $L \\to \\operatorname{Hom}(L, \\mathbb{Z})$. "
            "The empty list is the trivial group."
        ),
    )
    discriminant_sequence: DiscriminantSequenceData | None = Field(
        default=None,
        description=(
            "For a nondegenerate even lattice, generators of $O(A_L,q_L)$, the image of the discriminant action in the stated basis, "
            "and representatives of the pointed coset set; full generators of $O(L)$ are named self-isometry morphisms when available. "
            "$MM(L)=O(A_L,q_L)/\\operatorname{im}\\rho_L$. A multiplication table and generator cosets are present when the image is normal."
        ),
    )
    overlattice_count: int | None = Field(
        default=None,
        description=(
            "The number of integral lattices $M$ with $L \\subseteq M \\subseteq L^*$, with $M = L$ counted: the number of subgroups $H$ of the discriminant group "
            "$A_L = L^*/L$ with $b_{A_L}(H, H) = 0$, for the form $b_{A_L}(x + L, y + L) = b(x, y) + \\mathbb{Z}$ with values in $\\mathbb{Q}/\\mathbb{Z}$. "
            "Subgroups are counted, not their orbits under the isometries of $L$. An even $L$ can have odd lattices among the $M$. "
            "When certified, this exact invariant was computed by the certification phase."
        ),
    )
    delta: Literal[0, 1] | None = Field(
        default=None,
        description=(
            "Nikulin's invariant $\\delta$ of an even lattice with $2 A_L = 0$: "
            "0 when $b(x, x)$ is an integer for every $x$ in the dual lattice $L^*$, and 1 otherwise. "
            "With the rank $r$ and $A_L \\cong (\\mathbb{Z}/2)^a$ it gives $(r, a, \\delta)$. "
            "This field is meaningful for an even nondegenerate 2-elementary lattice."
        ),
    )
    bad_reduction_primes: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "The primes that divide $2 \\det L$, in increasing order: the primes $p$ at which $Q(x) = b(x, x)$ is degenerate modulo $p$. "
            "Outside them and the primes that divide $n$, the scheme $Q(x) = n$ over $\\mathbb{Z}$ has good reduction."
        ),
    )
    quadratic_character: int | None = Field(
        default=None,
        description=(
            "For rank $2m$: the discriminant $d$ of the field $\\mathbb{Q}(\\sqrt{D})$ with $D = (-1)^m \\det L$, and 1 when $D$ is a square. "
            "For $p \\nmid 2 \\det L$ the Kronecker symbol $\\chi_D(p) = (d / p)$ is 1 exactly when $Q$ modulo $p$ is a sum of $m$ hyperbolic planes, "
            "and it determines the number of points of $Q(x) = n$ over $\\mathbb{F}_{p^k}$. "
            "This field is meaningful for even rank and nonzero determinant."
        ),
    )
    genus_symbol: str | None = Field(
        default=None,
        description=(
            "`I` (odd) or `II` (even) with the signature, such as `II_{1,9}`. When the determinant is not 1 or -1, the local symbol at each prime "
            "that divides twice the determinant follows in parentheses, in the notation that SageMath prints. Requires a nonzero determinant."
        ),
    )
    genus_class_count: int | None = Field(
        default=None,
        gt=0,
        description=(
            "The class number of the genus of $L$: the number of isometry classes of lattices in the genus, $L$ counted. "
            "Computed by CI from the preamble operation `L.genus_class_number()`. "
            "Requires a nonzero determinant; absent when it is not computed."
        ),
    )
    spinor_genus_count: int | None = Field(
        default=None,
        gt=0,
        description=(
            "The number of spinor genera in the genus of $L$, a power of 2 (Conway and Sloane, SPLAG, Chapter 15, Section 9.1): "
            "the order of the quotient of the spinor operators by the spinor kernel of Theorems 16 and 17 there, enlarged by the spinor operator of one improper "
            "isometry, so that a spinor genus is a union of isometry classes. "
            "Computed by CI from the preamble operation `L.spinor_genus_count()`. Requires a nonzero determinant and rank at least 3."
        ),
    )
    spinor_genera: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "The number of isometry classes in each spinor genus of the genus of $L$: first in the spinor genus of $L$, then in the others in decreasing order. "
            "The first entry is the class number of the spinor genus of $L$, and the sum is the class number of the genus. "
            "Computed by CI from the preamble operation `L.spinor_genus_class_numbers()`. Requires a nonzero determinant and rank at least 3."
        ),
    )
    hyperbolic_index: int | None = Field(
        default=None,
        ge=0,
        description=(
            "The largest $n$ with $L \\cong U^n \\oplus L'$ for a lattice $L'$, where $U$ is the hyperbolic plane. "
            "For an integral $L$ this is the largest $n$ with an embedding $U^n \\hookrightarrow L$, because a unimodular sublattice $M$ of $L$ "
            "satisfies $L = M \\oplus M^{\\perp}$. "
            "Computed by `latticedb certify`: $L \\cong U^n \\oplus L'$ holds exactly when the genus of $L$ is the sum of the genus of $U^n$ and a genus of "
            "signature $(n_+ - n, n_- - n)$, since a lattice $U \\oplus L'$ of rank at least 3 is alone in its genus "
            "(Nikulin 1980, Theorem 1.13.1*). Requires a nonzero determinant; absent when it is not computed."
        ),
    )
    primitive_orbits: dict[OrbitGroup, PrimitiveOrbitSeries] | None = Field(
        default=None,
        description=(
            "For a group $\\Gamma \\subseteq O(L)$, the series $F_{L,\\Gamma}(z, w)$ whose coefficient $c_\\Gamma(n)$ is the number of $\\Gamma$-orbits of primitive "
            "vectors $v$ with $b(v, v) = n$. The keys are `O`, `SO`, `O+`, `SO+`, `Otilde`, `SOtilde`, `Otilde+` and `SOtilde+`: $S$ is the kernel of the determinant, "
            "$+$ the kernel of the real spinor norm, and $\\widetilde{O}(L)$ the kernel of $O(L) \\to O(A_L)$. "
            "Computed by `latticedb certify` through $z^4$ and $w^4$ for a definite lattice; stated with a reference otherwise. Requires a nonzero determinant."
        ),
    )
    discriminant_orbits: dict[OrbitGroup, PrimitiveOrbitSeries] | None = Field(
        default=None,
        description=(
            "For a group $\\Gamma \\subseteq O(L)$, the series whose coefficient $c_\\Gamma(n)$ is the number of $\\Gamma$-orbits on the elements $\\alpha \\in A_L$ with "
            "$q_L(\\alpha) = n / \\operatorname{ord}(\\alpha)^2$, keyed by the same eight groups. This is a function of the discriminant form $(A_L, q_L)$, not of $L$: it is "
            "computed by `latticedb certify` from $(A_L, q_L)$ for an even lattice of hyperbolic index at least 2. It equals $F_{L,\\Gamma}$ for an even "
            "$L$ containing two orthogonal hyperbolic planes (Eichler; theory/orbits.md), and it is defined for every nondegenerate $L$."
        ),
    )
    anisotropic_primes: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "The primes $p$ dividing $2 \\det L$, in increasing order, at which $L \\otimes \\mathbb{Q}_p$ is anisotropic: $b(x, x) \\neq 0$ for every nonzero $x$. "
            "The real place is not listed; the signature decides it. "
            "At a prime $p$ not dividing $2 \\det L$ the rank and the determinant decide it: a form of rank 1 is anisotropic, "
            "one of rank 2 is anisotropic exactly when $-\\det L$ is not a square modulo $p$, and one of rank at least 3 is isotropic. "
            "Requires a nonzero determinant."
        ),
    )
    local_representations: Annotated[tuple[LocalRepresentation, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "The values $b(x, x)$ of the localizations of $L$, as conditions on square classes: "
            "for each prime $p$ dividing $2 \\det L$ at which $L \\otimes \\mathbb{Z}_p$ does not represent every nonzero $p$-adic integer, in increasing order, "
            "the least valuation at which it represents each square class of $\\mathbb{Q}_p^\\times$. "
            "At a prime $p$ not dividing $2 \\det L$ the rank and the determinant decide the conditions: "
            "a form $\\langle d \\rangle$ of rank 1 represents exactly the class of $d$, from valuation 0; "
            "a form of rank 2 represents every nonzero $p$-adic integer when $-\\det L$ is a square modulo $p$, "
            "and otherwise exactly the elements of even valuation, the classes $1$ and $\\nu$ from valuation 0; "
            "a form of rank at least 3 represents every nonzero $p$-adic integer. "
            "A nonzero integer $m$ is represented by $L \\otimes \\mathbb{Z}_p$ for every prime $p$ exactly when, at each prime, "
            "the valuation of $m$ is at least the least valuation of its class, and the signature decides the real place. "
            "Requires a nonzero determinant."
        ),
    )
    local_densities: Annotated[tuple[LocalDensities, ...], Field(strict=False)] | None = Field(
        default=None,
        description=("The local densities $\\beta_p(L, m)$ at each prime $p$ that divides $2 \\det L$, in increasing order of $p$. Requires a nonzero determinant."),
    )


class RootSystemComponent(Record):
    """An irreducible component of the root system $\\Phi(L)$ of a definite lattice, with a base."""

    type: RootType = Field(
        description=(
            "Type of the component: `A1`, `B2`, `C3`, `D4`, `E6`, `E7`, `E8`, `F4`, `G2`, and the higher ranks of `A` to `D`. "
            "`B_n` has $2n$ short roots, and `C_n` has $2n$ long roots."
        )
    )
    scale: Rational = Field(
        description=(
            "The $k \\neq 0$ with $b(r, r) = 2k$ for each short root $r$ of the component. "
            "The simple roots have $b(\\alpha_i, \\alpha_j) = k\\,(\\alpha_i, \\alpha_j)$, "
            "where $(\\alpha_i, \\alpha_j)$ is the entry of the symmetrized Cartan matrix of the type, normalized so that $(r, r) = 2$ for a short root $r$. "
            "$k$ is negative on a negative definite lattice."
        )
    )
    simple_roots: Annotated[tuple[IntegerVector, ...], Field(strict=False)] = Field(
        description=(
            "Row $i$ lists the coordinates of the simple root $\\alpha_i$ in the chosen basis $e_1, \\dots, e_n$. "
            "The simple roots are numbered as SageMath's `CartanMatrix` numbers them. "
            "The rows of all components are a basis of $\\mathbb{Z}\\Phi(L)$: "
            "they are the matrix of the embedding into $L$ of the orthogonal sum of the root lattices of the components."
        )
    )

    @property
    def rank(self) -> int:
        return int(self.type[1:])


class DefiniteData(Record):
    """Invariants of a definite lattice. They are stated for a positive definite form; on a negative definite lattice they are the invariants of $-b$."""

    minimum: Rational | None = Field(
        default=None,
        description="Optional cached least value of $b(x,x)$ over nonzero $x$.",
    )
    kissing_number: int | None = Field(
        default=None,
        description="Optional cached number of vectors attaining the minimum.",
    )
    automorphism_group_order: int | None = Field(
        default=None,
        description="Order of $O(L)$, computed by CI from the preamble operation `L.orthogonal_group()`.",
    )
    automorphism_group_generator_morphisms: Annotated[tuple[str, ...], Field(strict=False)] | None = Field(
        default=None,
        description="Names of self-isometries in this card's `morphisms` field that generate $O(L)$, computed by CI from the preamble operation `L.orthogonal_group()`.",
    )
    minimal_vectors: list[list[int]] | None = Field(
        default=None,
        description="A complete minimal shell in the record basis; its size equals `kissing_number`.",
    )
    perfect: bool | None = Field(
        default=None,
        description="Whether the rank-one tensors $v v^T$ of minimal vectors span $\\operatorname{Sym}^2(\\mathbb Q^n)$.",
    )
    regular: bool | Literal["true under GRH"] | None = Field(
        default=None,
        description=(
            "For a definite integral lattice: every value $b(x, x)$ represented by some lattice of its genus is represented by this lattice. "
            "`true under GRH` when it is proved under the generalized Riemann hypothesis; `references` names the proof."
        ),
    )
    spinor_regular: bool | Literal["true under GRH"] | None = Field(
        default=None,
        description=(
            "For a definite integral lattice of rank at least 3: every value $b(x, x)$ represented by some lattice of its spinor genus is represented by this lattice. "
            "`true under GRH` when it is proved under the generalized Riemann hypothesis; `references` names the proof."
        ),
    )
    theta_series: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Entry $k$ is the number of $x$ with $b(x, x) = k$, for $k = 0, 1, 2, \\dots$. "
            "The entries run through $k = \\max(\\mu, N)$ at least, "
            "where $\\mu$ is the minimum and $N$ is 12, 8, 6 or 4 for rank at most 4, at most 8, at most 12, or greater."
        ),
    )
    genus_theta_series: QSeriesPrefix | None = Field(
        default=None,
        description=(
            "The theta series of the genus of an integral $L$: $\\theta_{\\operatorname{gen}(L)} = \\sum_i \\theta_{L_i} / |O(L_i)| \\big/ \\sum_i 1 / |O(L_i)|$, "
            "over representatives $L_i$ of the isometry classes of the genus, with the exponent $b(x, x)$ of `theta_series`. "
            "Entry $k$ is the coefficient of $q^k$, for $k = 0, \\dots, N$ with $N$ as for `theta_series`: "
            "12, 8, 6 or 4 for rank at most 4, at most 8, at most 12, or greater. "
            "Values are integers or strings `p/q`, and entry 0 is 1. "
            "By the Siegel–Weil formula it is the Eisenstein component of $\\theta_L$."
        ),
    )
    theta_series_cuspidal_component: QSeriesPrefix | None = Field(
        default=None,
        description=(
            "$\\theta_L - \\theta_{\\operatorname{gen}(L)}$ for an integral $L$, the cuspidal component of $\\theta_L$: "
            "entry $k$ is the coefficient of $q^k$ for $k = 0, \\dots, N$ as in `genus_theta_series`, "
            "values are integers or strings `p/q`, and entry 0 is 0. It is zero when the genus has one class."
        ),
    )
    cusp_form_coordinates: QSeriesPrefix | None = Field(
        default=None,
        description=(
            "For an integral $L$ of even rank $n$: the coordinates of `theta_series_cuspidal_component` in the basis of "
            "$S_{n/2}(\\Gamma_0(N), \\chi)$ whose $q$-expansions are in reduced row echelon form, in the order of that basis. "
            "With the exponent $b(x, x)$, $\\theta_L$ is the theta series of $L(2)$ in the usual normalization, so $N = 2\\,\\ell$ for the level $\\ell$ of $L$, "
            "and $\\chi$ is the Kronecker character of `quadratic_character`. The space has a basis of forms with rational $q$-expansions, "
            "and the reduced echelon basis of their span is unique, so the coordinates do not depend on a choice."
        ),
    )
    siegel_eisenstein_coefficients: QSeriesPrefix | None = Field(
        default=None,
        description=(
            "For an integral $L$: entry $m - 1$ is the coefficient of $q^m$, $m = 1, 2, \\dots$, of the Eisenstein series of the Siegel–Weil formula, "
            "computed as the Siegel product of the real density and the local densities $\\beta_p(L, m)$ over every prime. "
            "By the Siegel–Weil formula it equals entry $m$ of `genus_theta_series`; the two are independent computations of one number."
        ),
    )
    root_system: Annotated[tuple[AdeType, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "ADE type of $\\Phi_{\\{2\\}}(L) = \\{r \\in L : b(r, r) = 2\\}$, as irreducible components in any order: `[E8]`, `[A1, A1]`, or `[]` "
            "when it is empty. "
            "By Witt's theorem (Conway and Sloane, *Sphere Packings, Lattices and Groups*, 3rd edition, Chapter 4, §3), "
            "$\\mathbb{Z}\\Phi_{\\{2\\}}(L)$ is the orthogonal sum of the root lattices of the components. "
            "Optional cached root-system data; when present it is a preamble-computed or source-stated value."
        ),
    )
    roots: Annotated[tuple[RootSystemComponent, ...], Field(strict=False)] | None = Field(
        default=None,
        description="Optional cached root system $\\Phi(L)$ as irreducible components, each with a base; `[]` when it is known to have no roots.",
    )


class IndefiniteData(Record):
    """Invariants of a lattice on which $b(x, x)$ takes both signs."""

    isotropic: bool = Field(description="Whether $b(x, x) = 0$ for some nonzero $x$.")


class HyperbolicData(Record):
    """Invariants of a nondegenerate lattice of rank at least 2 whose signature is $(1, n)$ or $(n, 1)$."""

    reflective: bool = Field(description="Whether the subgroup generated by reflections has finite index in the isometry group.")


class RootSpan(Record):
    """$\\mathbb{Z}\\Phi(L)$ for a lattice that is not definite. Present only when $b$ is not definite."""

    roots: Annotated[tuple[IntegerVector, ...], Field(strict=False)] = Field(
        description=(
            "Roots of $L$ that generate $\\mathbb{Z}\\Phi(L)$: each row lists the coordinates of one root in the chosen basis $e_1, \\dots, e_n$. "
            "`[]` when $L$ has no roots. "
            "When the rows generate $L$, that proves $L = \\mathbb{Z}\\Phi(L)$. "
            "When they do not, the notes of the record prove that each root of $L$ is in the sublattice that the rows generate."
        )
    )
    norms: Annotated[tuple[Rational, ...], Field(strict=False)] = Field(description="Entry $i$ is $b(r_i, r_i)$ for the root $r_i$ in row $i$ of `roots`.")
    summands: Annotated[tuple[Summand, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Lattices $M_1(k_1), M_2(k_2), \\dots$, each a record with a scale, "
            "with $\\mathbb{Z}\\Phi(L) \\cong M_1(k_1) \\oplus M_2(k_2) \\oplus \\cdots$, an orthogonal sum. "
            "Present exactly when `embedding` is present. Absent when $L = \\mathbb{Z}\\Phi(L)$."
        ),
    )
    embedding: Annotated[tuple[IntegerVector, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Matrix of an isometric embedding $M_1 \\oplus M_2 \\oplus \\cdots \\to L$ with image $\\mathbb{Z}\\Phi(L)$: "
            "the rows list the coordinates of the images of the chosen basis vectors of $M_1$, then of $M_2$, and so on."
        ),
    )


class RootSublattice(Record):
    """The root sublattice $R(L) = \\mathbb{Z}\\Phi(L)$ as a sublattice of $L$. Present when $L$ is definite or has a `root_span` block."""

    invariant_factors: Annotated[tuple[int, ...], Field(strict=False)] = Field(
        description=(
            "The invariant factors $d_1 \\mid d_2 \\mid \\dots$ of $R(L)$ in $L$. Their number is the rank of $R(L)$. "
            "With $M'$ the primitive sublattice $L \\cap (R(L) \\otimes \\mathbb{Q})$, "
            "$M' / R(L) \\cong \\mathbb{Z}/d_1 \\oplus \\mathbb{Z}/d_2 \\oplus \\cdots$."
        )
    )
    norms: Annotated[tuple[Rational, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "For a root lattice, a set $S$ with $L = \\mathbb{Z}\\Phi_S(L)$: among the sets of values $b(r, r)$ of generating roots, "
            "one with the fewest elements, and then the least absolute values. Present exactly when $L = R(L)$."
        ),
    )
