"""Presentation of stored lattice values in the generated site."""

from __future__ import annotations

import json
import re
from fractions import Fraction

from sage_extensions.categories.lattice_zeta_invariants import PartialLFactor, QuadraticCharacterDiscriminant, QuadraticHypersurfaceZetaFactorization

from latticedb.model import (
    Lattice,
    Morphism,
    OrbitGroup,
    PrimitiveOrbitSeries,
    RootSystemComponent,
    Vector,
)


def rational_tex(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{'-' if value < 0 else ''}\\tfrac{{{abs(value.numerator)}}}{{{value.denominator}}}"


def group_text(factors: tuple[int, ...]) -> str:
    """`Z/2^3 + Z/4` for the invariant factors (2, 2, 2, 4); `0` for the trivial group."""
    runs = [(factor, factors.count(factor)) for factor in dict.fromkeys(factors)]
    return " + ".join(f"(Z/{factor})^{count}" if count > 1 else f"Z/{factor}" for factor, count in runs) or "0"


def group_tex(factors: tuple[int, ...]) -> str:
    runs = [(factor, factors.count(factor)) for factor in dict.fromkeys(factors)]
    return " \\oplus ".join(f"(\\mathbb{{Z}}/{factor})^{{{count}}}" if count > 1 else f"\\mathbb{{Z}}/{factor}" for factor, count in runs) or "0"


def orbit_group_tex(group: OrbitGroup) -> str:
    """TeX for a key of `integral.primitive_orbits`, such as `\\widetilde{SO}^+(L)` for `SOtilde+`."""
    name, plus = group.removesuffix("+"), "^+" if group.endswith("+") else ""
    letters = name.removesuffix("tilde")
    return f"\\widetilde{{{letters}}}{plus}(L)" if name.endswith("tilde") else f"\\mathrm{{{letters}}}{plus}(L)"


ORBIT_GROUP_KEYS: tuple[OrbitGroup, ...] = ("O", "SO", "O+", "SO+", "Otilde", "SOtilde", "Otilde+", "SOtilde+")
"""The eight standard subgroup keys of $O(L)$: the keys of `integral.primitive_orbits`."""


def subgroup_tex(key: str) -> str:
    """TeX for a standard arithmetic-subgroup name or a named subgroup such as `Gamma_En_2`."""
    return next((orbit_group_tex(group) for group in ORBIT_GROUP_KEYS if group == key), key.replace("_", "\\_"))


def cardinality_tex(cardinality: int | str) -> str:
    """TeX for a stored finite or countably infinite group cardinality."""
    if cardinality == "aleph0":
        return "\\aleph_0"
    return str(cardinality)


def orbit_series_tex(series: PrimitiveOrbitSeries) -> str:
    """TeX for $F_{L,\\Gamma}(z, w)$: the stated nonzero terms, `?` for each coefficient that is not stated, and the order to which the series is stated."""
    terms = []
    for n in sorted(series.degrees, key=lambda n: (abs(n), -n)):
        count = series.coefficient(n)
        if count == 0:
            continue
        variable = "" if n == 0 else ("z" if n > 0 else "w") + (f"^{{{abs(n)}}}" if abs(n) > 1 else "")
        coefficient = "?" if count is None else str(count)
        terms.append(coefficient if not variable else (variable if coefficient == "1" else f"{coefficient}\\,{variable}"))
    order = f"O(z^{{{len(series.z) + 1}}}, w^{{{len(series.w) + 1}}})"
    return " + ".join([*terms, order])


def _argument(shift: int) -> str:
    return "s" if shift == 0 else f"s - {shift}" if shift > 0 else f"s + {-shift}"


def _character_tex(character: QuadraticCharacterDiscriminant) -> str:
    coefficient = int(character.coefficient)
    if not character.times_norm_parameter:
        return str(coefficient)
    return "n" if coefficient == 1 else "-n" if coefficient == -1 else f"{coefficient}n"


def _l_factor_tex(factor: PartialLFactor) -> str:
    argument = _argument(int(factor.shift))
    character = factor.character
    if int(character.coefficient) == 1 and not character.times_norm_parameter:
        return f"\\zeta^\\Sigma({argument})"
    return f"L^\\Sigma({argument}, \\chi_{{{_character_tex(character)}}})"


def cone_zeta_tex(lattice: Lattice) -> str:
    """Render the preamble-owned zeta factorization of the zero level."""
    from sage_extensions.categories.lattices import Lattices
    from sage_extensions.rings import session_ring_objects

    owned = Lattices(session_ring_objects()["ZZ"])(lattice.gram_tensor)
    return _zeta_factorization_tex(owned.quadratic_hypersurface_zeta_factorization(cone=True))


def nonzero_zeta_tex(lattice: Lattice) -> str:
    """Render the preamble-owned zeta factorization of a nonzero level."""
    from sage_extensions.categories.lattices import Lattices
    from sage_extensions.rings import session_ring_objects

    owned = Lattices(session_ring_objects()["ZZ"])(lattice.gram_tensor)
    return _zeta_factorization_tex(owned.quadratic_hypersurface_zeta_factorization(cone=False))


def _zeta_factorization_tex(factorization: QuadraticHypersurfaceZetaFactorization) -> str:
    numerator = "\\, ".join(_l_factor_tex(factor) for factor in factorization.numerator)
    if not factorization.denominator:
        return numerator
    denominator = "\\, ".join(_l_factor_tex(factor) for factor in factorization.denominator)
    return f"\\frac{{{numerator}}}{{{denominator}}}"


def genus_tex(symbol: str) -> str:
    """TeX for a stored genus symbol such as `II_{1,9} (2: 2^10)`."""
    head, _, local = symbol.partition(" (")
    letters, _, signature = head.partition("_")
    tex = f"\\mathrm{{{letters}}}_{signature}"
    if not local:
        return tex
    parts = []
    for part in local.removesuffix(")").split("; "):
        prime, _, body = part.partition(": ")
        body = re.sub(r"\^(-?\d+)", r"^{\1}", body)
        body = re.sub(r"\]_(\d+)", r"]_{\1}", body)
        parts.append(f"{prime}\\colon {body.replace(' ', '\\,')}")
    return f"{tex}\\ \\bigl({';\\ '.join(parts)}\\bigr)"


def root_system_tex(components: tuple[str, ...]) -> str:
    """`D_{4} \\oplus A_{1}^{3}` for the irreducible components (D4, A1, A1, A1)."""
    runs = [(component, components.count(component)) for component in dict.fromkeys(components)]
    return " \\oplus ".join(f"{component[0]}_{{{component[1:]}}}" + (f"^{{{count}}}" if count > 1 else "") for component, count in runs)


def set_tex(values: tuple[Fraction, ...]) -> str:
    """`\\{-2, \\tfrac{2}{3}\\}` for the set of the values."""
    return f"\\{{{', '.join(rational_tex(value) for value in sorted(set(values)))}\\}}"


def combination_tex(coordinates: Vector, symbol: str = "e") -> str:
    """`e_{1} - 2e_{3}` for the coordinates (1, 0, -2); `0` for the zero vector."""
    terms = []
    for index, coefficient in enumerate(coordinates, start=1):
        if coefficient == 0:
            continue
        sign = "-" if coefficient < 0 else "+"
        size = "" if abs(coefficient) == 1 else str(abs(coefficient))
        terms.append((sign, f"{size}{symbol}_{{{index}}}"))
    if not terms:
        return "0"
    first_sign, first = terms[0]
    return ("-" if first_sign == "-" else "") + first + "".join(f" {sign} {term}" for sign, term in terms[1:])


def _runs(names: list[str]) -> list[tuple[str, int]]:
    return [(name, names.count(name)) for name in dict.fromkeys(names)]


def root_span_tex(components: tuple[RootSystemComponent, ...]) -> str:
    """Render the stored component types and scales, without deriving another lattice identification."""
    names = [component.type if component.scale == 1 else f"{component.type}({rational_tex(component.scale)})" for component in components]
    runs = _runs(names)
    return " \\oplus ".join(f"{name}^{{{count}}}" if count > 1 else name for name, count in runs) or "0"


def root_span_text(components: tuple[RootSystemComponent, ...]) -> str:
    names = [component.type if component.scale == 1 else f"{component.type}({component.scale})" for component in components]
    runs = _runs(names)
    return " + ".join(f"{name}^{count}" if count > 1 else name for name, count in runs) or "0"


def block_tex(block: list[int], symbol: str = "e") -> str:
    """`e_{3}, \\dots, e_{10}` for the indices 3 to 10; each vector for fewer than four indices or a block with a gap."""
    if len(block) > 3 and block[-1] - block[0] == len(block) - 1:
        return f"{symbol}_{{{block[0]}}}, \\dots, {symbol}_{{{block[-1]}}}"
    return ", ".join(f"{symbol}_{{{index}}}" for index in block)


def matrix_tex(morphism: Morphism) -> str:
    """The matrix as a TeX `array`, with a vertical line at each column subdivision and `\\hline` at each row subdivision."""
    columns = len(morphism.matrix[0])
    bounds = (0, *morphism.column_subdivisions, columns)
    alignment = "|".join("r" * (high - low) for low, high in zip(bounds, bounds[1:], strict=False))
    lines = []
    for index, matrix_row in enumerate(morphism.matrix):
        if index in morphism.row_subdivisions:
            lines.append("\\hline")
        lines.append(" & ".join(str(value) for value in matrix_row) + " \\\\")
    return f"\\left(\\begin{{array}}{{{alignment}}}\n" + "\n".join(lines) + "\n\\end{array}\\right)"


def matrix_text(morphism: Morphism) -> str:
    """The matrix and its subdivisions as JSON, one row per line, in the form that `latticedb morphism` reads."""
    rows = ",\n  ".join(json.dumps(list(matrix_row)) for matrix_row in morphism.matrix)
    row_lines = json.dumps(list(morphism.row_subdivisions))
    column_lines = json.dumps(list(morphism.column_subdivisions))
    return f'{{"matrix": [\n  {rows}\n],\n "row_subdivisions": {row_lines},\n "column_subdivisions": {column_lines}}}'


def summand_name(record: Lattice, scale: int) -> tuple[str, str]:
    """The stored card name for $M$, with ``(k)`` appended for a nontrivial twist."""
    if scale == 1:
        return record.name, record.latex
    return f"{record.name}({scale})", f"{record.latex}({scale})"


def span_summands(lattice: Lattice, lattices: dict[str, Lattice]) -> list[tuple[Lattice, str]]:
    """`(M, name of M(k) as TeX)` for each summand $M(k)$ of `root_span.summands`."""
    span = lattice.root_span
    if span is None or span.summands is None:
        return []
    return [(lattices[summand.tag], summand_name(lattices[summand.tag], summand.scale)[1]) for summand in span.summands]


def summand_images(lattice: Lattice, lattices: dict[str, Lattice]) -> list[tuple[Lattice, str, int, Vector]]:
    """`(M, name of M(k) as TeX, j, x)` for each row `x` of `root_span.embedding`: the embedding sends the basis vector $e_j$ of the summand $M(k)$ to `x`."""
    span = lattice.root_span
    if span is None or span.summands is None or span.embedding is None:
        return []
    sources: list[tuple[Lattice, str, int]] = []
    for record, name in span_summands(lattice, lattices):
        if record.rank is None:
            raise ValueError(f"root-span summand {record.tag} images require a stated source rank")
        sources.extend((record, name, j) for j in range(1, record.rank + 1))
    return [(record, name, j, image) for (record, name, j), image in zip(sources, span.embedding, strict=True)]


def theta_tex(theta: tuple[int, ...]) -> str:
    terms = [
        "1",
        *(f"{count}q^{{{power}}}" if power > 1 else f"{count}q" for power, count in enumerate(theta) if power > 0 and count > 0),
    ]
    return " + ".join([*terms, f"O(q^{{{len(theta)}}})"])
