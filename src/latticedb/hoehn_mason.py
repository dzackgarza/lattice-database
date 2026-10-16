"""Stored transcription of the Höhn--Mason Leech-lattice ancillary file.

G. Höhn and G. Mason, "The 290 fixed-point sublattices of the Leech lattice",
arXiv:1505.06420.  This module is source intake.  It parses the archived source
and its card/tag locators, states each printed basis and generator matrix as a
module map between preamble modules with forms, and compares the results with
the lattice cards.  Containment, orthogonality, rank, form preservation,
bijectivity, factorization, composition and group orders are preamble
operations.

The source prints a coordinate space ``V = Z^24`` with a rational form, the
Leech lattice ``leech[1]`` by the rows of a basis in ``V``, the sublattices
``A`` and ``B`` of each entry by rows in ``V``, and the generators of ``C`` by
matrices acting on row vectors in the coordinates of that basis.  A card matrix
has the images of the source generators as its columns.
"""

from collections.abc import Mapping, Sequence
from pathlib import Path

from dzack_research.preamble.categories.abstract_categories.mor_categories import CategoricalMor
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    FormedModuleMor,
    FormModules,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import _OwnedRingElement, _OwnedRingParent
from dzack_research.preamble.rings import OwnedRings, session_ring_objects
from pydantic import BaseModel, ConfigDict, TypeAdapter

from latticedb import corpus, hashimoto
from latticedb.corpus import Matrix
from latticedb.model import GramTensor, Lattice, Tag, rational

_SESSION_RINGS = session_ring_objects()
_integers = _SESSION_RINGS["ZZ"]
assert isinstance(_integers, _OwnedRingParent)
ZZ: _OwnedRingParent = _integers
_ring = _SESSION_RINGS["ZZ"]
assert isinstance(_ring, OwnedRings.ParentMethods)
integer_ring: OwnedRings.ParentMethods = _ring
_domain = _SESSION_RINGS["ZZ"]
assert isinstance(_domain, OwnedRings.NoZeroDivisors.Commutative.Nontrivial.ParentMethods)
integer_domain: OwnedRings.NoZeroDivisors.Commutative.Nontrivial.ParentMethods = _domain
QQ = _SESSION_RINGS["QQ"]
_QQ_AS_ZZ_MODULE = Modules(QQ).restriction_of_scalars(integer_domain.fraction_field_map())(QQ)
LEECH_RANK = 24


class Leech(BaseModel):
    """The stored ``leech[1]`` source datum and its card locator."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    basis: Matrix
    inner_product: tuple[tuple[str, ...], ...]
    record: Tag
    record_basis: Matrix


class Entry(BaseModel):
    """One stored ``lattices[i,j]`` source datum and its card locator."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    i: int
    j: int
    coinvariant_basis: Matrix
    fixed_basis: Matrix
    stabilizer_generators: tuple[Matrix, ...]
    row: int
    record: Tag
    twist: int
    record_basis: Matrix


def stored(directory: Path) -> tuple[Leech, tuple[Entry, ...]]:
    """Return the archived Leech datum and all ancillary entries."""
    leech = Leech.model_validate_json((directory / "leech.json").read_text())
    entries = tuple(TypeAdapter(Entry).validate_json(path.read_text()) for path in sorted(directory.glob("lattices_*.json")))
    return leech, entries


def _formed_module(value: object) -> FormModules.ParentMethods:
    if not isinstance(value, FormModules.ParentMethods):
        raise TypeError("the owned form-module category must return a module with a form")
    return value


def _coordinate_vector(value: object) -> FramedFreeModules.ElementMethods:
    if not isinstance(value, FramedFreeModules.ElementMethods):
        raise TypeError("a stored coordinate image must belong to the owned framed free module")
    return value.to_vector()


def _integer_coefficient(value: object) -> int:
    if not isinstance(value, _OwnedRingElement):
        raise TypeError("a stored matrix coefficient must be an element of the owned scalar ring")
    return int(value)


def _formed(gram: GramTensor | None) -> FormModules.ParentMethods:
    """The free module ``Z^n`` with the rational bilinear form of Gram tensor ``gram``."""
    if gram is None:
        raise ValueError("a Gram tensor must be stated before constructing the source module")
    module = integer_ring.free_module(len(gram))
    return _formed_module(FormModules(ZZ)(module.bilinear_hom_space(_QQ_AS_ZZ_MODULE)(gram)))


def _rows(target: Modules.ParentMethods, rows: Matrix) -> CategoricalMor.ElementMethods:
    """The module map ``Z^k -> target`` taking the ``i``-th generator to the ``i``-th row."""
    source = integer_ring.free_module(len(rows))
    return hashimoto._module_map(source.module_category().Mor(source, target)(tuple(target(row) for row in rows)))


def _leech_lattice(leech: Leech) -> tuple[FormModules.ParentMethods, FormModules.ParentMethods, CategoricalMor.ElementMethods]:
    """``(V, leech[1], φ)``: the coordinate space, the lattice on the printed basis, and ``φ: Z^24 -> V``.

    ``φ`` takes the printed basis to its rows in ``V``; the form of
    ``leech[1]`` is the form of ``V`` pulled back along ``φ``.
    """
    space = _formed(tuple(tuple(rational(value) for value in row) for row in leech.inner_product))
    basis = _rows(space.unformed_module(), leech.basis)
    return space, _formed_module(FormModules(ZZ)(space.form().pullback(basis))), basis


def _sublattice(
    space: FormModules.ParentMethods, lattice: FormModules.ParentMethods, basis: CategoricalMor.ElementMethods, rows: Matrix
) -> tuple[FormModules.ParentMethods, CategoricalMor.ElementMethods] | None:
    """The printed rows as a sublattice ``S`` of ``leech[1]``, with the restricted form, and its inclusion.

    The map ``Z^k -> V`` given by the rows factors through ``φ`` exactly when
    every row is a vector of ``leech[1]``; otherwise the answer is ``None``.
    """
    inclusion = hashimoto._linear_map(_rows(space.unformed_module(), rows)).factor_through_or_none(basis)
    if inclusion is None:
        return None
    inclusion = hashimoto._module_map(inclusion)
    sublattice = FormModules(ZZ)(lattice.form().pullback(inclusion))
    generators = hashimoto._module_parent(inclusion.domain())
    return _formed_module(sublattice), hashimoto._module_map(
        sublattice.module_category().Mor(sublattice, lattice)(lambda label: lattice(inclusion(generators.module_generator(label))))
    )


def _complementary(
    space: FormModules.ParentMethods, coinvariant_inclusion: CategoricalMor.ElementMethods, fixed_inclusion: CategoricalMor.ElementMethods, entry: Entry
) -> bool:
    """Whether ``A`` and ``B`` are orthogonal in ``leech[1]`` and their ranks sum to 24."""
    ranks = int(hashimoto._linear_map(coinvariant_inclusion).image().module_rank()) + int(hashimoto._linear_map(fixed_inclusion).image().module_rank())
    return ranks == LEECH_RANK and all(space(left).is_orthogonal_to(space(right)) for left in entry.coinvariant_basis for right in entry.fixed_basis)


def _endomorphism(lattice: FormModules.ParentMethods, generator: Matrix) -> CategoricalMor.ElementMethods:
    """The stored generator as the endomorphism of ``leech[1]`` taking the ``i``-th basis vector to row ``i``."""
    return hashimoto._module_map(lattice.module_category().Mor(lattice, lattice)(tuple(lattice(row) for row in generator)))


def _fixes(endomorphism: CategoricalMor.ElementMethods, inclusion: CategoricalMor.ElementMethods) -> bool:
    """Whether ``g`` is the identity on the sublattice included by ``inclusion``, checked on its generators."""
    sublattice = hashimoto._module_parent(inclusion.domain())
    return all(endomorphism(inclusion(sublattice.module_generator(label))) == inclusion(sublattice.module_generator(label)) for label in sublattice.module_generating_set())


def _restriction(endomorphism: CategoricalMor.ElementMethods, inclusion: CategoricalMor.ElementMethods) -> CategoricalMor.ElementMethods | None:
    """``g|_A: A -> A``, the factor of ``g ∘ ι`` through ``ι``; ``None`` when ``g(A)`` is not contained in ``A``."""
    restricted = hashimoto._linear_map(hashimoto._module_map(endomorphism * inclusion)).factor_through_or_none(inclusion)
    return None if restricted is None else hashimoto._module_map(restricted)


def _record_isometry(record: Lattice, twist: int, sublattice: FormModules.ParentMethods, record_basis: Matrix) -> CategoricalMor.ElementMethods | None:
    """The isometry ``R(t) -> S`` whose matrix is the stored record basis, or ``None``."""
    return hashimoto.basis_isometry(_formed(record.gram_tensor).twist(twist), sublattice, record_basis)


def _matrix(morphism: CategoricalMor.ElementMethods) -> Matrix:
    """The card matrix of ``morphism``: the images of the source generators as columns."""
    source = hashimoto._module_parent(morphism.domain())
    target = hashimoto._module_parent(morphism.codomain())
    images = tuple(_coordinate_vector(morphism(source.module_generator(label))) for label in source.module_generating_set())
    return tuple(tuple(_integer_coefficient(image(label)) for image in images) for label in target.module_generating_set())


def _record_matrices(isometry: CategoricalMor.ElementMethods, restrictions: Sequence[CategoricalMor.ElementMethods | None]) -> tuple[Matrix, ...]:
    """The matrices of ``ψ^{-1} ∘ g|_A ∘ ψ`` for the record isometry ``ψ: R(t) -> A``."""
    inverse = hashimoto._linear_map(isometry).inverse()
    if any(restriction is None for restriction in restrictions):
        raise ValueError("every restriction must be defined before serializing its matrix")
    return tuple(_matrix(hashimoto._module_map(inverse * restriction * isometry)) for restriction in restrictions if restriction is not None)


def automorphisms(leech: Leech, entry: Entry, record: Lattice) -> tuple[Matrix, ...]:
    """The generators of ``C`` restricted to ``A``, as self-isometries of the record ``R`` of the entry."""
    space, lattice, basis = _leech_lattice(leech)
    coinvariant = _sublattice(space, lattice, basis, entry.coinvariant_basis)
    assert coinvariant is not None, f"lattices[{entry.i},{entry.j}]: a row of A is not a vector of leech[1]"
    sublattice, inclusion = coinvariant
    isometry = _record_isometry(record, entry.twist, sublattice, entry.record_basis)
    assert isometry is not None, f"lattices[{entry.i},{entry.j}]: the stored basis is not an isometry from {entry.record}({entry.twist}) to A"
    restrictions = tuple(_restriction(_endomorphism(lattice, generator), inclusion) for generator in entry.stabilizer_generators)
    assert all(restriction is not None for restriction in restrictions), f"lattices[{entry.i},{entry.j}]: a generator of C does not map A to itself"
    return _record_matrices(isometry, restrictions)


def embedding(leech: Leech, entry: Entry, leech_record: Lattice, record: Lattice) -> Matrix:
    """The inclusion of ``A`` into ``leech[1]`` as a map of the records ``R(t) -> L``."""
    space, lattice, basis = _leech_lattice(leech)
    leech_isometry = hashimoto.basis_isometry(_formed(leech_record.gram_tensor), lattice, leech.record_basis)
    assert leech_isometry is not None, f"leech[1]: the stored basis is not an isometry from {leech.record} to leech[1]"
    coinvariant = _sublattice(space, lattice, basis, entry.coinvariant_basis)
    assert coinvariant is not None, f"lattices[{entry.i},{entry.j}]: a row of A is not a vector of leech[1]"
    sublattice, inclusion = coinvariant
    isometry = _record_isometry(record, entry.twist, sublattice, entry.record_basis)
    assert isometry is not None, f"lattices[{entry.i},{entry.j}]: the stored basis is not an isometry from {entry.record}({entry.twist}) to A"
    return _matrix(hashimoto._module_map(hashimoto._linear_map(leech_isometry).inverse() * inclusion * isometry))


def group_order(record: Lattice, generators: tuple[Matrix, ...]) -> int:
    """The order of the subgroup of ``O(R)`` generated by the card matrices ``generators``."""
    lattice = Lattices(ZZ)(record.gram_tensor)
    group = lattice.orthogonal_group()
    subgroup = group.subgroup(tuple(tuple(lattice(column) for column in zip(*generator, strict=True)) for generator in generators))
    return int(subgroup.order())


def check(
    leech: Leech,
    entries: tuple[Entry, ...],
    groups: tuple[hashimoto.GroupRow, ...],
    lattices: Mapping[str, Lattice],
    morphisms: corpus.Held,
) -> list[str]:
    """Compare the archived ancillary data to card data through preamble computations."""
    found: list[str] = []
    space, lattice, basis = _leech_lattice(leech)
    leech_isometry = hashimoto.basis_isometry(_formed(lattices[leech.record].gram_tensor), lattice, leech.record_basis)
    leech_inverse = None if leech_isometry is None else hashimoto._linear_map(leech_isometry).inverse()
    if leech_isometry is None:
        found.append(f"leech[1]: the stored basis is not an isometry from {leech.record} to leech[1]")
    by_n = {row.n: row for row in groups}
    rows = sorted(entry.row for entry in entries)
    owners = sorted(row.n for row in groups if row.shares is None)
    if rows != owners:
        found.append(f"lattices.txt: the entries name the rows {rows} of Table 10.2, the rows without a sharp sign are {owners}")
    for entry in entries:
        name = f"lattices[{entry.i},{entry.j}]"
        coinvariant = _sublattice(space, lattice, basis, entry.coinvariant_basis)
        fixed = _sublattice(space, lattice, basis, entry.fixed_basis)
        if coinvariant is None or fixed is None or not _complementary(space, coinvariant[1], fixed[1], entry):
            found.append(f"{name}: A and B are not orthogonal sublattices of leech[1] of complementary rank")
            continue
        sublattice, inclusion = coinvariant
        endomorphisms = tuple(_endomorphism(lattice, generator) for generator in entry.stabilizer_generators)
        form_morphisms = FormModules(lattice.base_ring()).Mor(lattice, lattice)
        if not isinstance(form_morphisms, FormedModuleMor):
            raise TypeError("the public form-module Mor must implement the owned form-preservation query")
        if not all(form_morphisms.preserves_forms(endomorphism) and _fixes(endomorphism, fixed[1]) for endomorphism in endomorphisms):
            found.append(f"{name}: a generator of C is not an isometry of leech[1] that fixes B")
            continue
        restrictions = tuple(_restriction(endomorphism, inclusion) for endomorphism in endomorphisms)
        if any(restriction is None for restriction in restrictions):
            found.append(f"{name}: a generator of C does not map A to itself")
            continue
        record = lattices[entry.record]
        isometry = _record_isometry(record, entry.twist, sublattice, entry.record_basis)
        if isometry is None:
            found.append(f"{name}: the stored basis is not an isometry from {entry.record}({entry.twist}) to A")
            continue
        row = by_n[entry.row]
        stated = (row.coinvariant.record, -row.coinvariant.twist) if row.coinvariant else None
        if stated != (entry.record, entry.twist):
            found.append(f"{name}: Table 10.2 row {entry.row} gives Lambda_G(-1) = {stated}, the entry gives {(entry.record, entry.twist)}")
        generated = _record_matrices(isometry, restrictions)
        order = group_order(record, generated)
        if order != row.order:
            found.append(f"{name}: C acts on A with a group of order {order}, Table 10.2 row {entry.row} states |G| = {row.order}")
        if leech_inverse is not None and (
            _matrix(leech_inverse * inclusion * isometry),
            entry.twist,
        ) not in morphisms.get((entry.record, leech.record), ()):
            found.append(f"lattice card {entry.record} does not hold the inclusion of {name} into {leech.record}")
        held = morphisms.get((entry.record, entry.record), ())
        if any((generator, 1) not in held for generator in generated):
            found.append(f"lattice card {entry.record} does not hold the self-isometry generators of C of {name}")
    return found


def stored_problems(root: Path, loaded: corpus.Corpus) -> list[str]:
    """Run the source comparison against the current lattice cards."""
    groups, _ = hashimoto.stored(root / "sources" / "hashimoto")
    lattices = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    return check(
        *stored(root / "sources" / "hoehn_mason"),
        groups,
        lattices,
        corpus.held(loaded),
    )
