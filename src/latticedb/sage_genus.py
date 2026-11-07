"""Thin Sage-process adapter for lattice invariants owned by the research preamble.

This module contains no lattice mathematics. It reads JSON requests from
``latticedb certify``, constructs the corresponding preamble lattice, invokes
preamble-owned operations, serializes their returned values, and writes each completed value as one
JSON line.
"""

import json
import sys
from collections.abc import Callable
from fractions import Fraction

from sage_extensions.categories.abstract_categories.mor_categories import CategoricalMor
from sage_extensions.categories.hyperbolic_lattices import HyperbolicLattices
from sage_extensions.categories.lattices import Lattices
from sage_extensions.categories.modules.framed.formed.form_modules import FormModules
from sage_extensions.categories.modules.pure.modules import Modules
from sage_extensions.categories.rings.commutative_algebra import FormalPowerSeriesRings
from sage_extensions.categories.rings.ring_foundation import LocalizationRings
from sage_extensions.categories.rings.ring_foundation import _OwnedRingElement
from sage_extensions.categories.rings.ring_foundation import OwnedRings
from sage_extensions.rings import session_ring_objects

from latticedb import records
from latticedb.genus import Request, applies
from latticedb.model import Lattice

_RINGS = session_ring_objects()
OWNED_ZZ = _RINGS["ZZ"]
OWNED_QQ = _RINGS["QQ"]


JsonValue = object


def _matrix_rows(morphism: CategoricalMor.ElementMethods) -> list[list[int]]:
    """Serialize a preamble morphism in the selected domain/codomain framings."""
    domain = morphism.domain()
    codomain = morphism.codomain()
    if not isinstance(domain, Modules.ParentMethods) or not isinstance(codomain, Modules.ParentMethods):
        raise TypeError("a generator morphism must have owned module endpoints")
    source_labels = tuple(domain.module_generating_set())
    target_labels = tuple(codomain.module_generating_set())
    return [
        [int(codomain.framing_morphism().lift(morphism(domain.module_generator(source_label)))(target_label)) for source_label in source_labels]
        for target_label in target_labels
    ]


def _integer_valued(lattice: Lattices.ParentMethods) -> bool:
    """Ask the integer module whether its scalar-valued form is integer-valued."""
    integer_ring = OWNED_ZZ
    assert isinstance(integer_ring, OwnedRings.ParentMethods)
    integer_domain = OWNED_ZZ
    assert isinstance(integer_domain, OwnedRings.NoZeroDivisors.Commutative.Nontrivial.ParentMethods)
    values = Modules(OWNED_QQ).restriction_of_scalars(integer_domain.fraction_field_map())(OWNED_QQ.regular_module())
    module = integer_ring.free_module(int(lattice.module_rank()))
    form = FormModules(OWNED_ZZ)(module.bilinear_hom_space(values)(lattice.gram_tensor()))
    return form.is_base_ring_valued()


def _elementary_primes(lattice: Lattices.ParentMethods) -> list[int]:
    """Serialize the preamble's prime-elementary predicates for a nontrivial discriminant group."""
    if lattice.discriminant_group().cardinality() == 1:
        return []
    return [int(prime) for prime in lattice.bad_reduction_primes() if lattice.is_p_elementary(prime)]


def _orthogonal_group_data(lattice: Lattices.ParentMethods) -> dict[str, JsonValue]:
    """Serialize the preamble-owned ``O(L)``, its order when it has one, and its selected generators.

    $O(L)$ of an indefinite lattice is infinite, so that card states the group by its
    generators and has no order to serialize (#8).
    """
    group = lattice.orthogonal_group()
    generators = [_matrix_rows(generator) for generator in group.group_generators()]
    match lattice.definiteness():
        case "positive_definite" | "negative_definite":
            return {"automorphism_group_order": int(group.cardinality()), "automorphism_group_generator_morphisms": generators}
        case _:
            return {"automorphism_group_generator_morphisms": generators}


def _root_span_data(lattice: Lattices.ParentMethods) -> dict[str, JsonValue]:
    """Serialize roots of ``L`` that generate ``L``, with their norms ``b(r, r)``.

    ``root_module_generating_set`` returns only when the roots generate ``L``,
    which proves ``L = ZPhi(L)``; otherwise it runs until the job ends.
    """
    labels = tuple(lattice.module_generating_set())
    framing = lattice.framing_morphism()
    roots = tuple(lattice.root_module_generating_set())
    return {
        "roots": [[int(framing.lift(root)(label)) for label in labels] for root in roots],
        "norms": [int(root.q()) for root in roots],
    }


def _reflective(lattice: Lattices.ParentMethods) -> bool | None:
    """Serialize the preamble's answer to whether ``W(L)`` has finite index in ``O(L)``.

    ``is_reflective`` answers ``True`` when Vinberg's algorithm completes and
    otherwise returns the undecided proposition, which certifies nothing.
    """
    match HyperbolicLattices(OWNED_ZZ)(lattice).is_reflective():
        case True:
            return True
        case _:
            return None


def _regular(lattice: Lattices.ParentMethods) -> bool | None:
    """Serialize the preamble's regularity answer when it is decided."""
    match lattice.is_regular():
        case True:
            return True
        case False:
            return False
        case _:
            return None


def _spinor_regular(lattice: Lattices.ParentMethods) -> bool | None:
    """Serialize the preamble's spinor-regularity answer when it is decided."""
    match lattice.is_spinor_regular():
        case True:
            return True
        case False:
            return False
        case _:
            return None


def _modular_scale(lattice: Lattices.ParentMethods) -> int | bool:
    """Serialize the preamble's \\(k\\) with \\(L\\cong L^*(k)\\), or ``False`` when there is none."""
    scale = lattice.modular_scale()
    return False if scale is None else int(scale)


def _rational(value: _OwnedRingElement | LocalizationRings.ElementMethods) -> int | str:
    """Serialize a preamble rational number, from its numerator and denominator, as an integer or a string `p/q` in lowest terms."""
    number = Fraction(int(value.numerator()), int(value.denominator()))
    return number.numerator if number.denominator == 1 else f"{number.numerator}/{number.denominator}"


def _coefficients(series: FormalPowerSeriesRings.ElementMethods, bound: int) -> list[int | str]:
    """Serialize the coefficients of `q^0, ..., q^bound` of a preamble power series."""
    return [_rational(series[exponent]) for exponent in range(bound + 1)]


def _local_densities(lattice: Lattices.ParentMethods, bound: int) -> list[dict[str, JsonValue]]:
    """Serialize the preamble's local densities `beta_p(L, m)`, `m = 1, ..., bound`, at each prime dividing `2 det L`."""
    genus = lattice.genus()
    return [{"prime": int(prime), "densities": [_rational(genus.local_density(prime, value)) for value in range(1, bound + 1)]} for prime in lattice.bad_reduction_primes()]


def _anisotropic_primes(lattice: Lattices.ParentMethods) -> list[int]:
    """Serialize the primes dividing `2 det L` at which the preamble's genus is anisotropic."""
    anisotropic = lattice.genus().anisotropic_primes()
    return [int(prime) for prime in lattice.bad_reduction_primes() if prime in anisotropic]


def _local_representations(lattice: Lattices.ParentMethods) -> list[dict[str, JsonValue]]:
    """Serialize the preamble's least represented valuation of each square class, at each prime dividing `2 det L` where it is not every class."""
    representations = lattice.genus().local_representations()
    exceptional = representations.index_set()
    return [
        {
            "prime": int(prime),
            "classes": [{"representative": int(representative), "least_valuation": int(valuation)} for representative, valuation in representations.value(prime).items()],
        }
        for prime in lattice.bad_reduction_primes()
        if prime in exceptional
    ]


SERIES = {
    "genus_theta_series": lambda lattice, bound: _coefficients(lattice.genus().theta_series(precision=bound + 1), bound),
    "theta_series_cuspidal_component": lambda lattice, bound: _coefficients(lattice.theta_series_cuspidal_component(precision=bound + 1), bound),
    "local_densities": _local_densities,
    "siegel_eisenstein_coefficients": lambda lattice, bound: _coefficients(lattice.genus().siegel_eisenstein_series(precision=bound + 1), bound)[1:],
}
"""Fields whose value is a prefix of a series, computed through the request's `series_bound`."""


JOINT = (
    (
        frozenset({"automorphism_group_order", "automorphism_group_generator_morphisms"}),
        _orthogonal_group_data,
    ),
    (frozenset({"roots", "norms"}), _root_span_data),
)
"""Fields that one preamble computation answers together, with that computation."""


VALUES = {
    "integer_valued": _integer_valued,
    "elementary_primes": _elementary_primes,
    "genus_symbol": lambda lattice: str(lattice.conway_sloane_genus_symbol()),
    "genus_class_count": lambda lattice: int(lattice.genus_class_number()),
    "overlattice_count": lambda lattice: int(lattice.integral_overlattice_inclusions().cardinality()),
    "spinor_genus_count": lambda lattice: int(lattice.spinor_genus_count()),
    "spinor_genera": lambda lattice: [int(value) for value in lattice.spinor_genus_class_numbers()],
    "hyperbolic_index": lambda lattice: int(lattice.integral_hyperbolic_index()),
    "discriminant_sequence": lambda lattice: lattice.discriminant_sequence_data(),
    "primitive_orbits": lambda lattice: _orbit_series(lattice.primitive_orbit_series()),
    "discriminant_form": lambda lattice: _discriminant_form(lattice),
    "discriminant_orbits": lambda lattice: _orbit_series(lattice.discriminant_orbit_series()),
    "reflective": _reflective,
    "modular_scale": _modular_scale,
    "regular": _regular,
    "spinor_regular": _spinor_regular,
    "anisotropic_primes": _anisotropic_primes,
    "local_representations": _local_representations,
}


def _discriminant_form(lattice) -> dict[str, JsonValue]:
    """The order of $O(A_L, q_L)$, the isotropic classes and their orbits, at the owner's form.

    The orbits are the owner's maintained partition of $A_L$; $q_L$ is constant on an orbit, so an
    orbit whose classes are isotropic is an orbit of isotropic classes.
    """
    form = lattice.discriminant_quadratic_form()
    isotropic = frozenset(form.isotropic_elements())
    inside = [orbit for orbit in form.orbits() if set(orbit) <= isotropic]
    return {
        "orthogonal_group_order": int(form.orthogonal_group().order()),
        "isotropic_classes": len(isotropic),
        "isotropic_orbits": len(inside),
    }


def _orbit_count(value: object) -> object:
    """One count of an orbit series, as a card states it.

    The owner answers the constant term of an orbit series with the cardinality of its set of orbits —
    an element of Sage's `Cardinalities` category, whose class is that category's `parent_class` — and
    not with an `int`, which `json` then refuses. The cardinality's own API is the conversion: `int` of a
    finite cardinality is its number, and an infinite one has none, so the coefficient is `None`, which
    `theory/orbits.md` states a coefficient that is not known to be. An infinite cardinality is the
    count `aleph0`, which the schema states, so the owner's answer is never dropped.
    """
    if value is None or isinstance(value, int):
        return value
    finite = getattr(value, "is_finite", None)
    if callable(finite) and not finite():
        return "aleph0"
    return int(value)


def _orbit_series(series: dict[str, object]) -> dict[str, object]:
    """An orbit series the owner returns, every count converted to what a card stores."""
    converted: dict[str, object] = {}
    for group, row in series.items():
        if not isinstance(row, dict):
            converted[group] = row
            continue
        entry = dict(row)
        if "constant" in entry:
            entry["constant"] = _orbit_count(entry["constant"])
        for key in ("z", "w"):
            values = entry.get(key)
            if isinstance(values, (list, tuple)):
                entry[key] = [_orbit_count(value) for value in values]
        converted[group] = entry
    return converted


def _start(tag: str, fields: list[str]) -> None:
    """Announce the computation of `fields`, so a run that ends during it can log it."""
    print(json.dumps({"tag": tag, "started": fields}), flush=True)


def _emit(tag: str, values: dict[str, JsonValue]) -> None:
    """Write one completed computation, so a run that ends early keeps every finished value."""
    print(json.dumps({"tag": tag, "by": "research preamble", **values}), flush=True)


def _run(tag: str, fields: list[str], compute: Callable[[], dict[str, JsonValue]]) -> dict[str, JsonValue]:
    """Announce one computation, then emit its values.

    A computation that raises ends this worker; the parent hands the card's
    computations that had not started to a new worker.
    """
    _start(tag, fields)
    values = compute()
    _emit(tag, values)
    return values


def _compute(request: Request) -> None:
    """Emit each requested value of one card as it completes, in the order requested."""
    tag = request["tag"]
    if "record" in request:
        if "derive" in request["fields"]:
            derived = _run(tag, ["derive"], lambda: {"derived": records.derive(request["record"])})["derived"]
        else:
            # The card's first request emitted this derivation; it is repeated only to select the fields.
            derived = records.derive(request["record"])
        stored = Lattice.model_validate(derived)
        if "integer_valued" in request["fields"]:
            assert stored.form is not None
            _start(tag, ["integer_valued"])
            _emit(tag, {"integer_valued": stored.form.integer_valued})
            request["fields"].remove("integer_valued")
        if stored.determinant == 0:
            return
        request["integral"] = stored.integral is not None
        request["fields"] = [field for field in request["fields"] if field != "derive" and applies(field, stored)]
    ring = OWNED_ZZ if request["integral"] else OWNED_QQ
    lattice = Lattices(ring)(request["gram"])
    joint = {field: (fields, compute) for fields, compute in JOINT for field in fields}
    done: set[str] = set()
    for field in request["fields"]:
        if field in done:
            continue
        if field in joint:
            # The answer is one computation, so every field of it that was asked for is
            # announced until it finishes and stored together. A field of the computation
            # this request did not ask for is not announced: it would be logged as an
            # interruption and never stored.
            fields, compute = joint[field]
            done |= fields
            _run(tag, [asked for asked in sorted(fields) if asked in request["fields"]], lambda: compute(lattice))
            continue
        done.add(field)
        _run(
            tag,
            [field],
            lambda: {field: SERIES[field](lattice, request["series_bound"]) if field in SERIES else VALUES[field](lattice)},
        )


def main() -> None:
    """Compute each request read from one stdin line, then report that card done.

    The parent hands a worker its next card only after ``done``, so a search
    that never returns holds this worker alone.
    """
    for line in sys.stdin:
        request: Request = json.loads(line)
        _compute(request)
        print(json.dumps({"tag": request["tag"], "done": True}), flush=True)


if __name__ == "__main__":
    main()
