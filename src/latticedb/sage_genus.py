"""Thin Sage-process adapter for lattice invariants owned by the research preamble.

This module contains no lattice mathematics. It reads JSON requests from
``latticedb certify``, constructs the corresponding preamble lattice, invokes
preamble-owned operations, serializes their returned values, and writes each completed value as one
JSON line.
"""

import json
import sys
from fractions import Fraction

from dzack_research.preamble.categories.abstract_categories.mor_categories import CategoricalMor
from dzack_research.preamble.categories.hyperbolic_lattices import HyperbolicLattices
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModules
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.commutative_algebra import FormalPowerSeriesRings
from dzack_research.preamble.categories.rings.ring_foundation import _OwnedRingElement
from dzack_research.preamble.rings import session_ring_objects

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
    values = Modules(OWNED_QQ).restriction_of_scalars(OWNED_ZZ.fraction_field_map())(OWNED_QQ)
    module = OWNED_ZZ.free_module(int(lattice.module_rank()))
    form = FormModules(OWNED_ZZ)(module.bilinear_hom_space(values)(lattice.gram_tensor()))
    return form.is_base_ring_valued()


def _elementary_primes(lattice: Lattices.ParentMethods) -> list[int]:
    """Serialize the preamble's prime-elementary predicates for a nontrivial discriminant group."""
    if lattice.discriminant_group().cardinality() == 1:
        return []
    return [int(prime) for prime in lattice.bad_reduction_primes() if lattice.is_p_elementary(prime)]


def _orthogonal_group_data(lattice: Lattices.ParentMethods) -> dict[str, JsonValue]:
    """Serialize the preamble-owned ``O(L)`` and its selected generators."""
    group = lattice.orthogonal_group()
    return {
        "automorphism_group_order": int(group.cardinality()),
        "automorphism_group_generator_morphisms": [_matrix_rows(generator) for generator in group.group_generators()],
    }


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


def _rational(value: int | Fraction | _OwnedRingElement) -> int | str:
    """Serialize a preamble rational number as an integer or a string `p/q`."""
    number = Fraction(str(value))
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
    "primitive_orbits": lambda lattice: lattice.primitive_orbit_series(),
    "discriminant_orbits": lambda lattice: lattice.discriminant_orbit_series(),
    "reflective": _reflective,
    "modular_scale": _modular_scale,
    "regular": _regular,
    "spinor_regular": _spinor_regular,
    "anisotropic_primes": _anisotropic_primes,
    "local_representations": _local_representations,
}


def _start(tag: str, fields: list[str]) -> None:
    """Announce the computation of `fields`, so a run that ends during it can log it."""
    print(json.dumps({"tag": tag, "started": fields}), flush=True)


def _emit(tag: str, values: dict[str, JsonValue]) -> None:
    """Write one completed computation, so a run that ends early keeps every finished value."""
    print(json.dumps({"tag": tag, "by": "research preamble", **values}), flush=True)


def main() -> None:
    task = json.load(sys.stdin)
    lattices: list[Request] = task["lattices"]
    for request in lattices:
        if "derive" in request["fields"]:
            _start(request["tag"], ["derive"])
            derived = records.derive(request["record"])
            _emit(request["tag"], {"derived": derived})
            stored = Lattice.model_validate(derived)
            if "integer_valued" in request["fields"]:
                assert stored.form is not None
                _start(request["tag"], ["integer_valued"])
                _emit(request["tag"], {"integer_valued": stored.form.integer_valued})
                request["fields"].remove("integer_valued")
            if stored.determinant == 0:
                continue
            request["integral"] = stored.integral is not None
            request["fields"] = [field for field in request["fields"] if field != "derive" and applies(field, stored)]
        ring = OWNED_ZZ if request["integral"] else OWNED_QQ
        lattice = Lattices(ring)(request["gram"])
        joint_fields: set[str] = set()
        for fields, compute in JOINT:
            chosen = fields & set(request["fields"])
            if not chosen:
                continue
            _start(request["tag"], sorted(fields))
            # The answer is one computation, so every field of it is stored together.
            _emit(request["tag"], compute(lattice))
            joint_fields |= fields
        for field in request["fields"]:
            if field in joint_fields:
                continue
            _start(request["tag"], [field])
            value = SERIES[field](lattice, request["series_bound"]) if field in SERIES else VALUES[field](lattice)
            _emit(request["tag"], {field: value})


if __name__ == "__main__":
    main()
