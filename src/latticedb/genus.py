"""CI serialization of lattice invariants computed by the research preamble.

`certify` sends each uncertified applicable computation to `sage_genus.py` under SageMath.
That module is a thin process/serialization boundary: every mathematical operation it
calls is owned by `dzack_research.preamble`.
A completed computation is authoritative for the part of the card that computation owns:
an authored value that disagrees is replaced by the computed value, and the resulting
card value is certified. A computation that does not finish remains uncertified.
"""

from __future__ import annotations

import json
import os
import selectors
import shutil
import signal
import subprocess
import sys
import time
from collections import deque
from collections.abc import Generator, Iterator
from contextlib import ExitStack, closing, suppress
from fractions import Fraction
from pathlib import Path
from tempfile import TemporaryFile
from typing import BinaryIO
from typing import NotRequired, TypedDict

import frontmatter
from pydantic import BaseModel, TypeAdapter

from latticedb import card_serialization, certificates, corpus, exceeded, failures, records, storage
from latticedb.catalogues import ArithmeticGroup
from latticedb.certificates import Certificate, Certificates
from latticedb.invariant_models import STANDARD_SUBGROUPS
from latticedb.model import (
    Automorphisms,
    DefiniteData,
    FormData,
    HyperbolicData,
    IntegralData,
    Lattice,
    RootSpan,
    Yaml,
    series_bound,
)

BLOCKS: dict[str, tuple[str, type[BaseModel]]] = {
    "integer_valued": ("form", FormData),
    "elementary_primes": ("integral", IntegralData),
    "genus_symbol": ("integral", IntegralData),
    "genus_class_count": ("integral", IntegralData),
    "overlattice_count": ("integral", IntegralData),
    "spinor_genus_count": ("integral", IntegralData),
    "spinor_genera": ("integral", IntegralData),
    "hyperbolic_index": ("integral", IntegralData),
    "automorphism_group_order": ("definite", DefiniteData),
    "automorphism_group_generator_morphisms": ("definite", DefiniteData),
    "discriminant_sequence": ("integral", IntegralData),
    "discriminant_form": ("integral", IntegralData),
    "primitive_orbits": ("integral", IntegralData),
    "cusp_chambers": ("integral", IntegralData),
    "cusp_root_orbits": ("integral", IntegralData),
    "discriminant_orbits": ("integral", IntegralData),
    "reflective": ("hyperbolic", HyperbolicData),
    "modular_scale": ("integral", IntegralData),
    "regular": ("definite", DefiniteData),
    "spinor_regular": ("definite", DefiniteData),
    "genus_theta_series": ("definite", DefiniteData),
    "theta_series_cuspidal_component": ("definite", DefiniteData),
    "cusp_form_coordinates": ("definite", DefiniteData),
    "siegel_eisenstein_coefficients": ("definite", DefiniteData),
    "anisotropic_primes": ("integral", IntegralData),
    "local_representations": ("integral", IntegralData),
    "local_densities": ("integral", IntegralData),
    "roots": ("root_span", RootSpan),
    "norms": ("root_span", RootSpan),
}
"""Each preamble-computed field, with the card block that stores it."""

AUTOMORPHISMS = "automorphisms"
"""The block of an indefinite card's automorphism data: the order of $O(L)$ and its generators.

An indefinite lattice's $O(L)$ may be finite or countably infinite, so the card states the order
here — an integer, or `aleph0` — and presents the group by its generators. A definite card states
the order with its generators in `definite` (#8).
"""

ORBIT_CERTIFIED_BOUND = card_serialization.ORBIT_CERTIFIED_BOUND
"""The z/w degree through which the preamble orbit computation certifies a series."""

ARITHMETIC_PREFIX = "arithmetic-group."
r"""The computation name of a field of an arithmetic-group card of this lattice.

An arithmetic-group card states a subgroup $\Gamma \leq O(L)$ and its relation to $O(L)$: its index
and the self-isometries of $L$ that generate it. Both are preamble results about this card's Gram
tensor, so both are certified here, and neither is a field of this card: the generator matrices are
`morphisms` entries of this card and the names are the group card's `data.generator_morphisms`.
"""

ARITHMETIC_FIELDS = ("index_in_orthogonal_group", "generator_morphisms")
"""The fields of an arithmetic-group card that a computation fills, in the order it fills them."""

ARITHMETIC_ORBIT_FIELDS = ("line_orbits", "plane_orbits", "flag_orbits")
"""The orbit counts of an arithmetic-group card, which a run asks for by name, in the order it stores them.

A group card may state how many orbits of primitive isotropic lines, of primitive isotropic planes
and of isotropic flags its subgroup has. The plane count repeats the lattice card's row, and the
flag count is the incidence of the two strata, which the owner decides by walking the plane cusps:
6132 s and 7973 s per $T_{\\mathrm{Co}}$-kernel row on a runner of its own (sage-extensions#286,
image run 44392429173), where the index of the same subgroup is read off its finite character image
in a second. So a run does not ask these of every group card: it names them, and it names all three,
because a flag count is stored with the two counts it joins.
"""


def certified_value(field: str, value: Yaml, lattice: Lattice | None = None) -> Yaml:
    """The stored value committed to by one completed preamble computation."""
    if field == "automorphism_group_generator_morphisms" or (field.startswith(ARITHMETIC_PREFIX) and field.endswith(".generator_morphisms")):
        # The names a card lists are its own choice; the commitment is to the matrices they name.
        if lattice is None or not isinstance(value, list):
            return value
        by_name = {morphism.name: morphism for morphism in lattice.morphisms if morphism.target == lattice.tag and morphism.scale == 1}
        names = TypeAdapter(list[str]).validate_python(value, strict=True)
        if any(name not in by_name for name in names):
            return value
        matrices = sorted(
            (by_name[name].matrix for name in names),
            key=lambda rows: tuple(entry for row in rows for entry in row),
        )
        return [[[entry for entry in row] for row in matrix] for matrix in matrices]
    if field in {"primitive_orbits", "discriminant_orbits"}:
        return card_serialization.orbit_projection(value) if isinstance(value, dict) else value
    return value


def applies(field: str, lattice: Lattice) -> bool:
    """Whether `certify` asks the preamble for `field` of this stored lattice.

    The database asks for a field when the card can store its value, and for no other reason.
    Where an operation is defined is the owner's to say: an operation that refuses this card
    raises, the raise is its refusal, `failures.record` quarantines that input
    (`failures.blocked`), and the run reports it once with `ChildProcessError` (#8). A
    database-side copy of the owner's domain withholds the call from a card the owner has since
    learned to answer — which is what this predicate did to `integral.primitive_orbits` and to
    the automorphism fields of an indefinite card — and the copy goes stale every time the owner
    extends an operation.

    The database's own facts, which are not the owner's domain:
    - `cusp_form_coordinates`: the owner does not present it.
    - The block a value is stored in names its hypothesis, so a field of `definite`,
      `indefinite`, `hyperbolic` or `integral` is asked only on a card that satisfies it; a
      value written into `definite` on an indefinite card would contradict the card's
      `definiteness`.
    - `roots` and `norms` are stored in `root_span`, which the schema refuses on a definite
      card, whose roots are `definite.roots`.
    - `polarization_counts`: no preamble operation presents a table of a source, and every
      count it holds is certified by the citation of that table.
    - `cusp_chambers`: a chamber is the source's walls, and the Gram matrix, diagram and wall
      count of them are what the card's form says; no preamble operation searches for one, and
      a Vinberg search is never run to fill a row.
    - `cusp_root_orbits`: the orbits are of the cusp stabilizer's action, and the owner's orbit
      call identifies two classes only through the generators it is given: it is not certified
      to generate that stabilizer at a primitive isotropic line
      (`generators_are_certified_complete` is `False`; sage-extensions#603 is the owner's issue for
      that family, #312 having supplied the image and its membership test), so a run of it
      counts identifications and not orbits, and no preamble operation states the count.

    Two rules below read the owner's domain off the card's own data, and they are exceptions because
    that refusal does not survive: a field whose computation raises ends its worker, and `certify`
    raises `ChildProcessError` once the queue is done, so a card asked for a field the owner does not
    define for it makes the run red. Every other field is still asked on every card that can store
    it, and an owner that refuses one of those is recorded by `failures.record` and reported once.
    """
    if field in {"cusp_form_coordinates", "polarization_counts", "cusp_chambers", "cusp_root_orbits"}:
        return False
    block_name, _model = stored_in(field, lattice.definiteness)
    match block_name:
        # The block gate only rejects: a field it admits is requested, whatever the operation's
        # own domain turns out to be, and the owner's raise is what answers for that domain.
        case "definite" if lattice.definite is None:
            return False
        case "indefinite" if lattice.indefinite is None:
            return False
        case "hyperbolic" if lattice.hyperbolic is None:
            return False
        case "integral" if lattice.integral is None:
            return False
    match field:
        case "roots" | "norms":
            return lattice.definite is None
        case "spinor_regular" | "spinor_genus_count" | "spinor_genera":
            # The owner defines the spinor fields in rank at least three and states the rank in its
            # own refusal: `spinor_genus_count` raises "the spinor-genus count of Genus of even
            # integral lattices of signature (2, 0) and determinant 3 is taken here in rank at least
            # three, and the rank is 2", and `spinor_genus_class_numbers` — which `spinor_genera`
            # and `is_spinor_regular` both reach — raises "spinor genera of Integral lattice of rank
            # 2 and signature (2, 0) require a nondegenerate lattice of finite rank at least three".
            # The rank is the card's own datum, so the threshold is read from the card and not
            # copied from the owner's code, and a card of rank three or more is asked as before.
            return lattice.rank is not None and lattice.rank >= 3
        case "discriminant_orbits":
            # `theory/orbits.md` gives the two orbit series to two kinds of card: $F_{L,\Gamma}$ is
            # enumerated from a definite card's vectors and stored in `integral.primitive_orbits`,
            # while $F_{A_L,\Gamma}$ is the series on the discriminant group of an even lattice whose
            # hyperbolic index is at least two, and it is stored in `integral.discriminant_orbits`.
            # No definite card carries the second series — the corpus's only two, 0040 and 0283, are
            # indefinite — and asking one leaves an uncertified `integral.discriminant_orbits` in the
            # queue of every run over A2.
            return lattice.integral is not None and lattice.definite is None
        case _:
            return True


SAGE_MODULE = Path(__file__).with_name("sage_genus.py")
WORKER = [sys.executable, "-m", "latticedb.sage_genus"]
"""The command of one worker process, which reads requests and writes JSON lines."""

SEMI_DECISIONS = frozenset({"roots", "norms", "reflective", "regular", "spinor_regular"})
"""Fields whose procedure need not terminate, requested after a card's other fields."""


class Request(TypedDict):
    """One lattice and the preamble-owned fields CI asks it to compute."""

    tag: str
    gram: list[list[int | str]]
    integral: bool
    fields: list[str]
    series_bound: int
    record: NotRequired[dict[str, Yaml]]
    arithmetic_groups: NotRequired[list[dict[str, Yaml]]]
    """The arithmetic-group cards whose fields this request computes, each by `slug` and `standard_name`."""
    resumed: NotRequired[bool]
    """A computation of these fields was cut short by an earlier job."""


ORBIT_ROW_SEPARATORS = ("[", "]")

ORBIT_ROW_AXES = ("constant", "planes")
"""The parts of a row that a run can ask for on their own: its line count and its plane count.

A row states both, and the owner answers them from two operations with costs three orders of
magnitude apart — on $T_{\\mathrm{Co}}$'s kernel rows the line count is 122--172 s and the plane
count is 1813--2171 s (sage-extensions#286) — so a run names the part it is about rather than
paying for both, exactly as a run names a row rather than the whole field (#7).
"""


def orbit_row(field: str, row: str) -> str:
    """One subgroup's row of an orbit field, as a request names it: `primitive_orbits[Otilde]`.

    A card stores the row inside its field's block; a request names it alone so that the
    row is one computation, announced, stored and certified on its own. The eight rows of
    `integral.primitive_orbits` on an indefinite card are the eight standard subgroups,
    and one of them not returning then costs that row rather than the whole field (#7).
    """
    return f"{field}{ORBIT_ROW_SEPARATORS[0]}{row}{ORBIT_ROW_SEPARATORS[1]}"


def orbit_row_parts(field: str) -> tuple[str, str, str | None] | None:
    """The orbit field a request's row name belongs to, the row, and the part of it, if any.

    `primitive_orbits[Otilde]` is a row and `primitive_orbits[Otilde].planes` is its plane
    count alone. `None` for a request that names no row: a whole field, or any other computation.
    """
    base, opener, rest = field.partition(ORBIT_ROW_SEPARATORS[0])
    if not opener:
        return None
    row, closer, tail = rest.partition(ORBIT_ROW_SEPARATORS[1])
    if not closer or not base or not row:
        return None
    if not tail:
        return (base, row, None)
    axis = tail.removeprefix(".")
    return (base, row, axis) if tail != axis and axis in ORBIT_ROW_AXES else None


def orbit_row_of(field: str) -> tuple[str, str] | None:
    """The orbit field a request's row name belongs to and the row, or None for a whole field."""
    parts = orbit_row_parts(field)
    return None if parts is None else (parts[0], parts[1])


def stored_in(field: str, definiteness: str | None = None) -> tuple[str, type[BaseModel]]:
    """The block that stores `field` on a card of `definiteness`, and that block's model.

    A definite card states the order of $O(L)$ with its generators in `definite`, where
    `BLOCKS` keeps every field. An indefinite lattice's $O(L)$ may be finite or countably
    infinite, so its order and its generators both live in `automorphisms` (#8).

    A row of an orbit series — `primitive_orbits[Otilde]` — is stored in the block of the
    field it is a row of.
    """
    row = orbit_row_of(field)
    if row is not None:
        return stored_in(row[0], definiteness)
    match (field, definiteness):
        case ("automorphism_group_order" | "automorphism_group_generator_morphisms", "indefinite"):
            return AUTOMORPHISMS, Automorphisms
        case ("polarization_counts", _):
            # Outside BLOCKS: the preamble does not compute it, and a cited count is never requested.
            return "integral", IntegralData
        case _:
            return BLOCKS[field]


def name(tag: str, field: str, definiteness: str | None = None) -> str:
    """The name of the certificate of `field` of the record `tag`, in the block that stores it.

    An arithmetic-group field names the card the value is stored on, `<slug>`, because that value
    is not a field of the lattice card: `6JRR arithmetic-group.otilde-t-co.index_in_orthogonal_group`
    is the index of that subgroup, computed from this lattice's Gram tensor.
    """
    if field == "derive":
        return f"{tag} derive"
    if field.startswith(ARITHMETIC_PREFIX):
        return f"{tag} {field}"
    return f"{tag} {stored_in(field, definiteness)[0]}.{field}"


def in_shard(tag: str, shard: tuple[int, int]) -> bool:
    """Whether the card `tag` belongs to shard `i` of `n`, by a hash that every job computes alike."""
    index, count = shard
    return certificates.tag_hash(tag) % count == index


def arithmetic_orbit_dependencies(field: str) -> frozenset[str]:
    r"""The group-card orbit counts a run must ask for, given one that it named.

    The relation is the schema's and not a cost decision: a flag count is stored only beside the two
    counts it joins (`GroupData._orbit_counts`), so naming `flag_orbits` asks `line_orbits` and
    `plane_orbits` with it. The converse does not hold, and treating the three as one bundle did hold
    it: the counts are three computations of very different cost on $T_{\mathrm{Co}}$'s kernel
    groups — the line row is 31--52 s at 1.03 GiB, the plane row 1813--2171 s at 3.5 GiB, and the
    incidence 6132--7973 s (sage-extensions#286) — so a run that named the line count was paying for
    the other two and could lose all three to one kill.
    `frozenset()` for a field that is not one of the three.
    """
    slug, _, short = field.rpartition(".")
    if not slug.startswith(ARITHMETIC_PREFIX) or short not in ARITHMETIC_ORBIT_FIELDS:
        return frozenset()
    asked = {"line_orbits", "plane_orbits"} if short == "flag_orbits" else set()
    return frozenset(f"{slug}.{count}" for count in (asked or {short}))


def arithmetic_requests(
    lattice: Lattice,
    loaded: corpus.Corpus,
    held: Certificates,
    wanted: tuple[str, ...] = (),
    *,
    named: bool = False,
) -> list[tuple[str, dict[str, Yaml]]]:
    r"""The uncertified fields of the arithmetic-group cards that this lattice states.

    An arithmetic-group card names one subgroup $\Gamma \leq O(L)$ and, when it has a
    `standard_name`, says which of the eight standard subgroups it is. Two of its fields are
    computations about this card's Gram tensor: `index_in_orthogonal_group`, asked as the index
    of the subgroup's finite character image `O(L)/Gamma` (its exact cardinality, not a coset
    enumeration), and `generator_morphisms`, asked as the isometries `g.group_generators()`
    returns. A card that states neither an index nor generators is asked for both; a value that a
    matching completed certificate already covers is not requested again. A card without a
    `standard_name`, such as a named subgroup defined by a source, has no owner operation that
    presents it, and is left alone.

    Its three orbit counts are asked where a run names one of them
    (`arithmetic-group.<slug>.flag_orbits`) and then all three together — a flag count is stored
    with the two counts it joins, and the three are one walk of the same subgroup, the plane row
    retained and the incidence reading it — or where a run names its cards (`certify --tag 6JRR`,
    a dispatch's own choice of cards) and asks no field at all. The sharded nightly does neither
    and pays nothing for them.
    """
    groups = {entry.value.slug: entry.value for entry in loaded.arithmetic_groups if entry.value.lattice == lattice.tag}
    chosen: list[tuple[str, dict[str, Yaml]]] = []
    for slug in lattice.arithmetic_groups:
        card = groups.get(slug)
        if card is None or card.standard_name is None:
            continue
        for short in ARITHMETIC_FIELDS:
            field = f"{ARITHMETIC_PREFIX}{slug}.{short}"
            computation = name(lattice.tag, field, lattice.definiteness)
            stored = getattr(card.data, short)
            # The group card states the generator names as a tuple; its commitment is the matrices.
            value = list(stored) if isinstance(stored, tuple) else stored
            expected_hash = certificates.certification_hash(computation, lattice, certified_value(field, value, lattice))
            if stored is None or certificates.is_pending(held, computation, lattice.certifications.get(field), expected_hash):
                chosen.append((field, {"slug": slug, "standard_name": card.standard_name}))
        # A named count takes the counts the schema makes it depend on, and no others; a run that
        # names its cards and no computation asks for all three, since nothing else ever asks.
        named_counts = {
            short
            for short in ARITHMETIC_ORBIT_FIELDS
            if short in wanted or f"{ARITHMETIC_PREFIX}{slug}.{short}" in wanted
        }
        if named and not wanted:
            named_counts = set(ARITHMETIC_ORBIT_FIELDS)
        joined = {"line_orbits", "plane_orbits"} if "flag_orbits" in named_counts else set()
        for short in ARITHMETIC_ORBIT_FIELDS:
            if short in named_counts | joined and getattr(card.data, short) is None:
                chosen.append((f"{ARITHMETIC_PREFIX}{slug}.{short}", {"slug": slug, "standard_name": card.standard_name}))
    return chosen


def orbit_rows_to_ask(
    lattice: Lattice,
    field: str,
    stored_value: Yaml,
    triage: failures.Failures,
    log: exceeded.Interruptions,
    *,
    only_missing: bool = True,
) -> list[str]:
    """The rows of an orbit field this run asks for, in the order the schema lists the subgroups.

    A row whose series the card already states is not asked again, and a row a failure quarantines
    — a subgroup that ran a whole job without returning — is not asked at all: it costs its own row
    and not the seven that return (#7). `only_missing=False` asks every unquarantined row, which
    re-mints the field's certificate over rows already stored.
    """
    stored = stored_value if isinstance(stored_value, dict) else {}
    rows: list[str] = []
    for row in STANDARD_SUBGROUPS:
        if only_missing:
            series = stored.get(row)
            if isinstance(series, dict) and series.get("constant") is not None:
                continue
        computation = name(lattice.tag, orbit_row(field, row), lattice.definiteness)
        if failures.blocked(triage, computation, lattice) or exceeded.is_exceeded(log, computation, lattice):
            continue
        rows.append(orbit_row(field, row))
    return rows


def orbit_plane_rows_to_ask(
    lattice: Lattice,
    field: str,
    stored_value: Yaml,
    triage: failures.Failures,
    log: exceeded.Interruptions,
    wanted: tuple[str, ...],
    *,
    named: bool,
) -> list[str]:
    r"""The plane parts of the orbit rows this run asks for, in the order the schema lists the subgroups.

    A row states two counts, and its plane count is the expensive one: it is the owner's orbit walk
    over the primitive isotropic planes, 1813--2171 s on $T_{\mathrm{Co}}$'s kernel rows, where the
    line count of the same row is 122--172 s (sage-extensions#286). The sharded nightly run must not
    pay that walk on every indefinite card that stores a row, so it asks this part only where a run
    names a part with `--field`. A run that names its cards — `certify --tag 6JRR`, which is what a
    dispatched run does — asks the parts of those cards and of no others: the cards are the run's own
    choice, and a part left unasked there is a value only another such run can produce.
    A part the card already states is not asked again, and a part a failure or an interrupted run
    quarantines is not asked at all.
    """
    stored = stored_value if isinstance(stored_value, dict) else {}
    parts: list[str] = []
    for row in STANDARD_SUBGROUPS:
        part = f"{orbit_row(field, row)}.planes"
        if not (part in wanted or (named and not wanted)):
            continue
        series = stored.get(row)
        if isinstance(series, dict) and series.get("planes") is not None:
            continue
        if failures.blocked(triage, name(lattice.tag, part, lattice.definiteness), lattice):
            continue
        if exceeded.is_exceeded(log, name(lattice.tag, part, lattice.definiteness), lattice):
            continue
        parts.append(part)
    return parts


def requests(
    loaded: corpus.Corpus,
    held: Certificates,
    log: exceeded.Interruptions,
    tags: tuple[str, ...],
    shard: tuple[int, int] = (0, 1),
    *,
    failed: failures.Failures | None = None,
    wanted: tuple[str, ...] = (),
) -> list[Request]:
    r"""For each nondegenerate record in `shard`, the uncertified applicable preamble computations.

    A computation that ran for a whole job without finishing is not requested. One
    that a job ended after a shorter time is requested first in its phase, so it runs
    for a whole job. The other cards follow by rank and then absolute determinant. The
    semi-decisions of every card are separate requests after all of them: every job
    ends inside a search, so a cut search resumed at the start of the next job would
    hold its workers through the fields that every procedure finishes. A computation
    that was running when a runner died comes after everything else, so a computation
    that ends its runner cannot end the next job early.

    `tags` is what the run names: the sharded nightly names no card, and a dispatched run names
    the cards it is about. The two costly parts of this queue — a row's plane count and a group
    card's three orbit counts, 1813--2171 s and 6132--7973 s a kernel row on
    $T_{\mathrm{Co}}$ (sage-extensions#286) — are asked where a run names one of them with
    `wanted`, and, when it names none, where it names its cards: a sharded nightly asks neither,
    and a `certify --tag` dispatch asks both of the cards it named.
    """
    resumed: list[Request] = []
    chosen: list[Request] = []
    resumed_searches: list[Request] = []
    searches: list[Request] = []
    lost: list[Request] = []
    sizes: dict[str, tuple[int, Fraction]] = {}
    triage = {} if failed is None else failed
    for entry in loaded.entries:
        lattice = entry.lattice
        if lattice.gram_tensor is None or (tags and lattice.tag not in tags) or not in_shard(lattice.tag, shard):
            continue
        if failures.blocked(triage, f"{lattice.tag} worker", lattice):
            continue
        metadata = corpus.front_matter(corpus.read_card(entry.path))
        cited = lattice.certifications
        derive_name = name(lattice.tag, "derive")
        derive_hash = certificates.certification_hash(derive_name, lattice, records.derived_projection(metadata))
        needs_derive = certificates.is_pending(held, derive_name, cited.get("derive"), derive_hash)
        needs_derive = needs_derive and not exceeded.is_exceeded(log, derive_name, lattice)
        if needs_derive and failures.blocked(triage, derive_name, lattice):
            continue
        if not needs_derive and lattice.rank is None:
            # A timed-out derivation cannot supply missing hypotheses for later operations.
            continue
        if lattice.determinant == 0:
            applicable = ["integer_valued"]
        else:
            # Before derivation the card lacks the hypotheses that select its fields, so all
            # are requested and the worker keeps those that apply to the derived card.
            applicable = list(BLOCKS) if lattice.rank is None or needs_derive else [field for field in BLOCKS if applies(field, lattice)]
        fields = []
        for field in applicable:
            block_name = stored_in(field, lattice.definiteness)[0]
            block = metadata.get(block_name)
            stored_value = block.get(field) if isinstance(block, dict) else None
            computation = name(lattice.tag, field, lattice.definiteness)
            if exceeded.is_exceeded(log, computation, lattice) or failures.blocked(triage, computation, lattice):
                continue
            expected_hash = certificates.certification_hash(computation, lattice, certified_value(field, stored_value, lattice))
            pending = stored_value is None or certificates.is_pending(held, computation, cited.get(f"{block_name}.{field}"), expected_hash)
            if field == "primitive_orbits" and lattice.definiteness == "indefinite":
                # The eight rows are eight computations: one subgroup that does not return costs its
                # own row, and the rows that do return are stored and certified without it (#7).
                rows = orbit_rows_to_ask(lattice, field, stored_value, triage, log)
                if not rows and pending:
                    # Every row is stored and the certificate is stale: one row re-mints it over the
                    # rows the card states, rather than the whole series being asked again.
                    rows = orbit_rows_to_ask(lattice, field, stored_value, triage, log, only_missing=False)[:1]
                fields.extend(rows)
                # The plane count of a row is its own computation: a run asks for it by name, or
                # for the cards it named rather than for a shard.
                fields.extend(orbit_plane_rows_to_ask(lattice, field, stored_value, triage, log, wanted, named=bool(tags)))
                continue
            if pending:
                fields.append(field)
        if needs_derive:
            fields.insert(0, "derive")
        # The arithmetic-group cards of this lattice state values computed from this card's Gram
        # tensor, so they are requested with it, after its own fields — unless an earlier run of that
        # computation is quarantined in triage, or outran a whole job.
        arithmetic = [
            (field, group)
            for field, group in arithmetic_requests(lattice, loaded, held, wanted, named=bool(tags))
            if not (
                exceeded.is_exceeded(log, name(lattice.tag, field, lattice.definiteness), lattice)
                or failures.blocked(triage, name(lattice.tag, field, lattice.definiteness), lattice)
            )
        ] if lattice.determinant else []
        fields = [*fields, *(field for field, _group in arithmetic)]
        if needs_derive and exceeded.was_lost(log, derive_name, lattice):
            # Without its derivation the card has no hypotheses for its other fields.
            lost_fields, fields = fields, []
        else:
            lost_fields = [field for field in fields if exceeded.was_lost(log, name(lattice.tag, field, lattice.definiteness), lattice)]
            fields = [field for field in fields if field not in lost_fields]
        gram = [[int(value) if value.denominator == 1 else str(value) for value in row] for row in lattice.gram_tensor]
        if lost_fields:
            lost.append({"tag": lattice.tag, "gram": gram, "integral": lattice.integral is not None, "fields": lost_fields, "series_bound": series_bound(len(gram))})
            if arithmetic:
                lost[-1]["arithmetic_groups"] = [group for field, group in arithmetic if field in lost_fields]
            if needs_derive:
                lost[-1]["record"] = metadata
            sizes[lattice.tag] = (len(gram), abs(lattice.determinant or Fraction(0)))
        if fields:
            interrupted = [field for field in fields if exceeded.seconds_run(log, name(lattice.tag, field, lattice.definiteness), lattice) is not None]
            rest = [field for field in fields if field not in interrupted]
            semi = [field for field in interrupted + rest if field in SEMI_DECISIONS]
            fields = [field for field in interrupted + rest if field not in SEMI_DECISIONS]
            request: Request = {
                "tag": lattice.tag,
                "gram": gram,
                "integral": lattice.integral is not None,
                "fields": fields,
                "series_bound": series_bound(len(lattice.gram_tensor)),
            }
            if arithmetic:
                request["arithmetic_groups"] = [group for field, group in arithmetic if field in fields]
            if needs_derive:
                request["record"] = metadata
                # Derivation supplies the hypotheses even when another field was interrupted.
                request["fields"] = ["derive", *[field for field in fields if field != "derive"]]
            if request["fields"]:
                if set(interrupted) - SEMI_DECISIONS:
                    resumed.append({**request, "resumed": True})
                else:
                    chosen.append(request)
            if semi:
                # A card that needs derivation carries its record, which selects the searches that apply.
                # The request is marked, so a run can take one phase or the other.
                (resumed_searches if set(interrupted) & SEMI_DECISIONS else searches).append({**request, "fields": semi, "searches": True})
            sizes[lattice.tag] = (len(gram), abs(lattice.determinant or Fraction(0)))

    # Smaller cards finish sooner, so each job certifies as many values as it can. A
    # semi-decision can hold its worker for the rest of the job, so the searches of
    # every card follow the fields that every procedure finishes.
    def by_size(request: Request) -> tuple[int, Fraction]:
        return sizes[request["tag"]]

    return resumed + sorted(chosen, key=by_size) + resumed_searches + sorted(searches, key=by_size) + sorted(lost, key=by_size)


MEMORY_RESERVE = 0.1
"""The fraction of the machine's memory that the workers leave available.

Below it the worker holding the most memory is killed, so a computation that
outgrows the runner costs its own card rather than the runner and the whole job.
"""


def _meminfo(key: str) -> int:
    """One `/proc/meminfo` entry, in bytes."""
    for line in Path("/proc/meminfo").read_text().splitlines():
        label, _, value = line.partition(":")
        if label == key:
            return int(value.split()[0]) * 1024
    raise KeyError(key)


def _resident_bytes(group: int) -> int:
    """The resident memory of every process in the process group `group`."""
    total = 0
    for stat in Path("/proc").glob("[0-9]*/stat"):
        try:
            fields = stat.read_text().rsplit(")", 1)[1].split()
        except OSError:
            continue  # The process exited after the listing.
        if int(fields[2]) == group:
            total += int(fields[21]) * os.sysconf("SC_PAGE_SIZE")
    return total


def computed(chosen: list[Request], deadline: float, workers: int) -> Generator[dict[str, Yaml]]:
    """Stream results from `workers` Sage processes, with checkpoints, until the job deadline.

    A worker holds one card and receives the next only after reporting it done, so a
    search that never returns holds back only its own worker. A worker that exits while
    holding a card yields `{"tag": tag, "failed": reason}`; another takes the remaining
    cards, beginning with the computations of that card that had not started.

    The two ways a worker ends are told apart by what its exit reports, which is all the
    parent can observe of it. A worker that returned has a non-negative `returncode` and
    `exit status N`; one that raised has a positive one and its traceback on stderr. A
    worker that was killed has a negative one, the negated signal, and no traceback: the
    run's own memory kill is known from the reserve check that sent its SIGKILL, and
    `killed` then carries the memory the worker held and the floor the run was keeping,
    both measured at the kill. Any other signal is reported by its number, so a container
    out-of-memory kill — which arrives as signal 9 — is recorded as one.
    """
    queue = deque(chosen)
    if not queue:
        return
    reserve = int(MEMORY_RESERVE * _meminfo("MemTotal"))
    holding: dict[subprocess.Popen[bytes], Request] = {}

    def next_request() -> Request:
        # Resumed computations may outrun the job again; while other requests wait, one
        # worker is kept available for the other requests.
        if workers > 1 and sum(1 for request in holding.values() if request.get("resumed")) >= workers - 1:
            for index, request in enumerate(queue):
                if not request.get("resumed"):
                    del queue[index]
                    return request
        return queue.popleft()

    started: dict[subprocess.Popen[bytes], set[str]] = {}
    pending: dict[subprocess.Popen[bytes], bytes] = {}
    exhausted: set[subprocess.Popen[bytes]] = set()
    peaks: dict[subprocess.Popen[bytes], int] = {}
    errors: dict[subprocess.Popen[bytes], BinaryIO] = {}
    with ExitStack() as resources, selectors.DefaultSelector() as selector:

        def stderr(process: subprocess.Popen[bytes]) -> str:
            output = errors[process]
            output.seek(0)
            text = output.read().decode("utf-8", errors="replace")
            output.seek(0)
            output.truncate()
            if text:
                print(text, file=sys.stderr, end="", flush=True)
            return text

        def assign(process: subprocess.Popen[bytes]) -> None:
            """Hand the next request to `process`.

            A worker that ended before it read the request — a startup failure such as a
            missing module — leaves the write to raise `BrokenPipeError`. The request stays
            the process's holding, so the read loop reports the failure with the worker's
            stderr and the card is queued for triage instead of the run ending here.
            """
            assert process.stdin is not None
            request = next_request()
            holding[process] = request
            started[process] = set()
            try:
                process.stdin.write((json.dumps(request) + "\n").encode())
                process.stdin.flush()
            except BrokenPipeError:
                pass

        def release(process: subprocess.Popen[bytes]) -> None:
            """Close a worker's pipes; one that ended before its request was written raises nothing."""
            assert process.stdin is not None and process.stdout is not None
            with suppress(BrokenPipeError):
                process.stdin.close()
            process.stdout.close()

        def spawn() -> None:
            output = resources.enter_context(TemporaryFile())
            process = subprocess.Popen(WORKER, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=output, start_new_session=True)
            errors[process] = output
            assert process.stdout is not None
            selector.register(process.stdout, selectors.EVENT_READ, process)
            pending[process] = b""
            assign(process)

        try:
            for _ in range(min(workers, len(queue))):
                spawn()
            checkpointed = time.monotonic()
            while pending:
                remaining = deadline - time.time()
                if remaining <= 0:
                    yield {"deadline": True}
                    return
                if time.monotonic() - checkpointed >= 30:
                    checkpointed = time.monotonic()
                    # The job log records memory and disk, so a runner lost to either is diagnosed from CI.
                    if holding:
                        largest = max(holding, key=lambda process: _resident_bytes(process.pid))
                        print(
                            f"memory: {_meminfo('MemAvailable') / 2**30:.1f} GiB available; {holding[largest]['tag']} holds {_resident_bytes(largest.pid) / 2**30:.1f} GiB; "
                            f"disk: {shutil.disk_usage('.').free / 2**30:.1f} GiB free",
                            flush=True,
                        )
                    yield {"checkpoint": True}
                candidates = [process for process in holding if started[process] and process not in exhausted]
                if candidates and _meminfo("MemAvailable") < reserve:
                    # The kill costs that card and not the runner, so its cost is measured here:
                    # this is the only moment the memory the worker holds can be observed (#46).
                    resident = {process: _resident_bytes(process.pid) for process in candidates}
                    largest = max(candidates, key=resident.__getitem__)
                    exhausted.add(largest)
                    peaks[largest] = resident[largest]
                    os.killpg(largest.pid, signal.SIGKILL)
                for key, _ in selector.select(min(5, remaining)):
                    process = key.data
                    chunk = os.read(key.fd, 65536)
                    if not chunk:
                        selector.unregister(key.fileobj)
                        release(process)
                        process.wait()
                        del pending[process]
                        request = holding.pop(process, None)
                        begun = started.pop(process, set())
                        if request is not None:
                            unstarted = [field for field in request["fields"] if field not in begun]
                            if begun and unstarted and "derive" not in request["fields"]:
                                queue.appendleft({**request, "fields": unstarted})
                            signal_number = -process.returncode if process.returncode is not None and process.returncode < 0 else None
                            kill: dict[str, Yaml] = {}
                            if process in exhausted:
                                reason = "memory exhausted"
                                kill = {"by": "memory", "peak": peaks[process], "limit": reserve}
                            elif signal_number is not None:
                                # No traceback to read: the signal is all that ended it, and a
                                # container out-of-memory kill arrives here as signal 9.
                                reason = f"killed by signal {signal_number}"
                                kill = {"by": f"signal {signal_number}"}
                            else:
                                reason = f"exit status {process.returncode}"
                            error = stderr(process)
                            yield {"tag": request["tag"], "failed": reason, **({"killed": kill} if kill else {}), **({"stderr": error} if error else {})}
                        errors.pop(process).close()
                        exhausted.discard(process)
                        peaks.pop(process, None)
                        # A worker that ends before starting a computation would end its successor alike.
                        if queue and (request is None or begun):
                            spawn()
                        continue
                    pending[process] += chunk
                    while b"\n" in pending[process]:
                        line, pending[process] = pending[process].split(b"\n", 1)
                        if not line.strip():
                            continue
                        values = json.loads(line)
                        if "done" not in values:
                            if "started" in values:
                                started[process] |= set(values["started"])
                            yield values
                            continue
                        stderr(process)
                        del holding[process]
                        if queue:
                            assign(process)
                        else:
                            assert process.stdin is not None
                            with suppress(BrokenPipeError):
                                process.stdin.close()
        finally:
            for process in pending:
                if process.poll() is None:
                    try:
                        os.killpg(process.pid, signal.SIGTERM)
                    except ProcessLookupError:
                        if process.poll() is None:
                            raise


def _generator_morphisms(tag: str, morphisms: list[dict[str, Yaml]], matrices: list[Yaml], prefix: str = "O(L)") -> tuple[list[str], list[dict[str, Yaml]]]:
    """Place computed generators of O(L) on the lattice card and return their names."""
    names: list[str] = []
    used_self_names = {morphism["name"] for morphism in morphisms if isinstance(morphism.get("name"), str)}
    for index, matrix in enumerate(matrices, start=1):
        assert isinstance(matrix, list)
        existing = next(
            (morphism for morphism in morphisms if morphism.get("target") == tag and morphism["matrix"] == matrix and morphism.get("scale") == 1),
            None,
        )
        if existing is None:
            base = f"{prefix} generator {index}"
            name = base
            suffix = 2
            while name in used_self_names:
                name = f"{base} #{suffix}"
                suffix += 1
            morphisms.append({"target": tag, "name": name, "matrix": matrix, "scale": 1})
            used_self_names.add(name)
        else:
            assert isinstance(existing["name"], str)
            name = existing["name"]
        names.append(name)
    return names, morphisms


DERIVED_BLOCKS = ("integral", "definite", "indefinite", "root_span", "root_sublattice")
"""The blocks `records.derive` pops and rebuilds, and so the blocks a derivation can otherwise thin out."""


def keep_other_computations(path: Path, derived: dict[str, Yaml]) -> dict[str, Yaml]:
    """The derived card, carrying every stored field of `path` that the derivation does not state.

    `records.derive` rebuilds the blocks it owns from the record it is given, and that record is the
    run's read of the card from when the card was queued — up to a job's 350 minutes earlier. A field
    another computation wrote in between, such as the semi-decision `definite.regular`, is in neither,
    so writing the derivation alone deletes the value while `certificates/` keeps its certificate, and
    the card and the ledger disagree (#23). Such a field belongs to a computation of its own, with its
    own certificate, so the derivation does not decide it: a field the stored card states and the
    derived card does not is carried over, the citation included. A derivation whose Gram tensor
    differs from the stored card is another lattice and carries nothing over.
    """
    current = corpus.front_matter(corpus.read_card(path))
    if current.get("gram_tensor") != derived.get("gram_tensor"):
        return derived
    kept = dict(derived)
    carried: set[str] = set()
    for block_name in DERIVED_BLOCKS:
        stored = current.get(block_name)
        if not isinstance(stored, dict):
            continue
        produced = kept.get(block_name)
        produced = dict(produced) if isinstance(produced, dict) else {}
        carried_fields = {field: value for field, value in stored.items() if value is not None and field not in produced}
        carried |= {f"{block_name}.{field}" for field in carried_fields}
        if carried_fields or produced:
            kept[block_name] = {**carried_fields, **produced}
    if carried:
        citations = dict(kept.get("certifications") or {})
        stored_citations = current.get("certifications") or {}
        for local_name in sorted(carried):
            if local_name in stored_citations:
                citations[local_name] = stored_citations[local_name]
        kept["certifications"] = citations
    return kept


def store(path: Path, values: dict[str, Yaml]) -> None:
    """Replace each computed scope on the card by the completed computation.

    A value keyed by a row of an orbit series — `primitive_orbits[Otilde]` — is stored as that
    row of its field's block, beside the rows stored before it, so a row computed alone lands
    without the rows that did not return (#7).
    """
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    morphisms = TypeAdapter(list[dict[str, Yaml]]).validate_python(metadata.get("morphisms", []), strict=True)
    computed: dict[str, Yaml] = {}
    for key, value in values.items():
        if value is None:
            continue
        row = orbit_row_of(key)
        field = row[0] if row is not None else key
        if field not in BLOCKS:
            continue
        if row is None:
            computed[field] = value
        elif isinstance(value, dict):
            earlier = computed.get(field)
            computed[field] = {**(earlier if isinstance(earlier, dict) else {}), **value}
        elif field not in computed:
            computed[field] = value
    if "roots" in computed:
        # Computed roots generate L, so L = ZPhi(L) and the block has no summands or embedding.
        metadata["root_span"] = {}
    for field, value in computed.items():
        block_name, model = stored_in(field, metadata.get("definiteness"))
        if field == "automorphism_group_generator_morphisms":
            assert isinstance(value, list)
            generator_names, morphisms = _generator_morphisms(path.stem, morphisms, value)
            value = [name for name in generator_names]
        # The hyperbolic block holds only computed fields, so the first computed value creates it.
        match metadata.setdefault(block_name, {}):
            case dict() as block:
                if field in {"primitive_orbits", "discriminant_orbits"} and isinstance(value, dict):
                    present = block.get(field)
                    replacement = dict(present) if isinstance(present, dict) else {}
                    for group, computed_series in value.items():
                        if not isinstance(computed_series, dict):
                            replacement[group] = computed_series
                            continue
                        old_series = replacement.get(group)
                        updated_series = dict(old_series) if isinstance(old_series, dict) else {}
                        for key, computed_part in computed_series.items():
                            if key in {"z", "w"} and isinstance(computed_part, list):
                                old_part = updated_series.get(key)
                                tail = old_part[len(computed_part) :] if isinstance(old_part, list) else []
                                updated_series[key] = [*computed_part, *tail]
                            else:
                                updated_series[key] = computed_part
                        replacement[group] = updated_series
                    block[field] = replacement
                else:
                    block[field] = value
                metadata[block_name] = {key: block[key] for key in model.model_fields if key in block}
    metadata["morphisms"] = [morphism for morphism in morphisms]
    text = records.record_text(metadata, document.content)
    if text != path.read_text():
        storage.write_text(path, text)


def in_phase(requests: list[Request], searches: bool | None) -> list[Request]:
    """The requests of one phase: the terminating fields, or the semi-decision searches.

    `None` is both phases, in the order the queue gives them, which is everything else first.
    """
    if searches is None:
        return requests
    return [request for request in requests if bool(request.get("searches")) == searches]


def store_arithmetic_group(
    root: Path,
    tag: str,
    slug: str,
    values: dict[str, Yaml],
) -> list[tuple[str, Yaml]]:
    """Store the computed fields of one arithmetic-group card, its generators as self-isometries of `tag`.

    A generator is one isometry $L \to L$, so it is a `morphisms` entry of the lattice card with
    `scale: 1`, and the group card lists the names of those entries: the matrices are stored once.
    The values are certified on the lattice card, whose Gram tensor is the input of every one of
    them, under the names `arithmetic-group.<slug>.<field>`; the group card states the values. The
    three orbit counts of a subgroup are stored together, because a flag count is schema-checked
    against the two counts it joins.
    Returns each stored field with the value its certificate commits to.
    """
    lattice_path = root / "lattices" / f"{tag}.md"
    document = corpus.read_card(lattice_path)
    metadata = corpus.front_matter(document)
    morphisms = TypeAdapter(list[dict[str, Yaml]]).validate_python(metadata.get("morphisms", []), strict=True)
    group_path = root / "arithmetic-groups" / f"{slug}.md"
    group_document = corpus.read_card(group_path)
    group_metadata = corpus.front_matter(group_document)
    data = TypeAdapter(dict[str, Yaml]).validate_python(group_metadata.get("data") or {}, strict=True)
    stored: list[tuple[str, Yaml]] = []
    matrices = values.get("generator_morphisms")
    if isinstance(matrices, list):
        names, morphisms = _generator_morphisms(tag, morphisms, matrices, prefix=str(group_metadata.get("name") or slug))
        data["generator_morphisms"] = list(names)
        stored.append(("generator_morphisms", [[[int(entry) for entry in row] for row in matrix] for matrix in sorted(matrices, key=_matrix_order)]))
    index = values.get("index_in_orthogonal_group")
    if isinstance(index, int) and not isinstance(index, bool):
        data["index_in_orthogonal_group"] = index
        stored.append(("index_in_orthogonal_group", index))
    for short in ARITHMETIC_ORBIT_FIELDS:
        count = values.get(short)
        if isinstance(count, int) and not isinstance(count, bool):
            data[short] = count
            stored.append((short, count))
    if not stored:
        return stored
    model = ArithmeticGroup.model_validate({**group_metadata, "data": data})
    computed_data = model.data.model_dump(exclude_none=True, mode="json")
    # The card keeps the order it states its fields in; a computed field it did not state is appended.
    written = {**group_metadata, "data": {**{key: computed_data[key] for key in data if key in computed_data}, **{key: value for key, value in computed_data.items() if key not in data}}}
    text = card_serialization.catalogue_text(written, group_document.content)
    if text != group_path.read_text():
        storage.write_text(group_path, text)
    if morphisms:
        metadata["morphisms"] = [morphism for morphism in morphisms]
        storage.write_text(lattice_path, records.record_text(metadata, document.content))
    return stored


def _matrix_order(matrix: object) -> tuple[int, ...]:
    """The order of the matrices a certificate commits to: entrywise, so the choice of names is not part of it."""
    assert isinstance(matrix, list)
    return tuple(int(entry) for row in matrix for entry in row)


def certify(
    root: Path,
    loaded: corpus.Corpus,
    held: Certificates,
    tags: tuple[str, ...],
    deadline: float,
    workers: int = 1,
    shard: tuple[int, int] = (0, 1),
    searches: bool | None = None,
    fields: tuple[str, ...] = (),
) -> None:
    """Compute every uncertified value on `workers` processes, replace its card scope, and certify the result.

    `searches` takes one phase of the queue: `False` the terminating fields alone, `True` the
    semi-decision searches alone. A search can hold a worker for a whole job, so a dispatched run
    that only wants the fields does not wait for one, and the searches are a job of their own.
    `fields` narrows the queue to the named computations, a field (`primitive_orbits`) taking the
    rows of that field with it: a card whose other fields are expensive can be asked for the one
    value a run is about, without a ledger entry standing in for the reason. A row's plane count
    is the one value a row does not carry by naming the row, because it costs the owner's plane
    walk rather than its line walk: a run asks for it as `primitive_orbits[Otilde].planes`.
    `deadline` is the time, in seconds since the epoch, at which the job's timeout
    ends this run. A computation in progress is logged in `exceeded.yaml` until it
    finishes, checkpointing the seconds actually spent in this run. A worker that
    fails on a card ends no other card's computations; the run raises after the
    queue is done, so the failure is reported with every completed value stored.
    A worker the run ends rather than the card — killed because the machine ran out
    of memory, or by a signal — costs only its own card: its computation is logged
    in `exceeded.yaml` with what the run observed of the kill, and the card is left
    as it was, so the run reports the cost and still exits 0 (#46).
    """
    by_tag = {entry.lattice.tag: entry for entry in loaded.entries}
    log = exceeded.load(root)
    failed = failures.recover(root, {tag: entry.lattice for tag, entry in by_tag.items() if (not tags or tag in tags) and in_shard(tag, shard)}, log)
    reconciled = False
    for computation, failure in failed.items():
        tag, field = computation.split(" ", 1)
        entry = by_tag.get(tag)
        if entry is None or (tags and tag not in tags) or not in_shard(tag, shard) or failure.disposition == "resolved":
            continue
        lattice = entry.lattice
        if lattice.gram_tensor is None or failure.attempts[-1].hash != exceeded.input_hash(computation, lattice):
            continue
        metadata = corpus.front_matter(corpus.read_card(entry.path))
        if field == "derive":
            value = records.derived_projection(metadata)
        else:
            short = field.rsplit(".", 1)[-1]
            if short not in BLOCKS or name(tag, short, lattice.definiteness) != computation:
                continue
            block = metadata.get(stored_in(short, lattice.definiteness)[0])
            if not isinstance(block, dict) or block.get(short) is None:
                continue
            value = certified_value(short, block[short], lattice)
        expected = certificates.certification_hash(computation, lattice, value)
        if certificates.is_certified(held, computation, lattice.certifications.get(field), expected):
            failed[computation] = failure.model_copy(update={"disposition": "resolved"})
            log.pop(computation, None)
            reconciled = True
    if reconciled:
        failures.save(root, failed)
        exceeded.save(root, log)
    running: dict[str, float] = {}
    worker_failures: list[str] = []
    # Certificates are saved at each checkpoint, in the groups of the cards that changed,
    # rather than with each value. A card whose certificate a hard kill lost cites a hash
    # that `certificates/` lacks, so it is recomputed.
    unsaved: set[str] = set()

    def checkpoint(final: bool = False) -> None:
        if unsaved:
            certificates.save(root, held, unsaved)
            unsaved.clear()
        if running:
            for computation, started_at in running.items():
                # Until the final checkpoint, a pushed entry is lost if the runner dies.
                log[computation] = exceeded.Interruption(hash=log[computation].hash, seconds=int(time.monotonic() - started_at), lost=not final)
                if final and log[computation].seconds >= exceeded.WINDOW_SECONDS:
                    tag = computation.split(" ", 1)[0]
                    failed[computation] = failures.record(root, computation, by_tag[tag].lattice, "certification budget exhausted", "", log[computation].seconds)
            exceeded.save(root, log)

    try:
        chosen = requests(loaded, held, log, tags, shard, failed=failed, wanted=fields)
        if fields:
            # A filter names a computation, and a field's name takes its rows with it. A row's
            # plane count is asked for only by its own name, so it is named and not inherited. An
            # arithmetic-group orbit count is one of three the run asks together, so naming one
            # keeps the three.
            wanted = set(fields)
            narrowed: list[Request] = []
            for request in chosen:
                kept = [
                    field
                    for field in request["fields"]
                    if field in wanted
                    or (orbit_row_of(field) or (field,))[0] in wanted
                    or (field.startswith(ARITHMETIC_PREFIX) and bool(arithmetic_orbit_dependencies(field) & wanted))
                ]
                if kept:
                    narrowed.append({**request, "fields": kept})
            chosen = narrowed
        with closing(computed(in_phase(chosen, searches), deadline, workers)) as stream:
            for values in stream:
                if "checkpoint" in values:
                    checkpoint()
                    continue
                if "deadline" in values:
                    print("Certification time budget exhausted", flush=True)
                    break
                if "failed" in values:
                    tag = str(values["tag"])
                    lattice = by_tag[tag].lattice
                    killed = values.get("killed")
                    kill = killed if isinstance(killed, dict) else None
                    active = [computation for computation in running if computation.startswith(f"{tag} ")]
                    for computation in active or [f"{tag} worker"]:
                        started_at = running.pop(computation, None)
                        elapsed = time.monotonic() - started_at if started_at is not None else 0.0
                        failed[computation] = failures.record(root, computation, lattice, str(values["failed"]), str(values.get("stderr", "")), elapsed)
                        if kill is None:
                            # A failure is a defect to repair, not a computation that outran its job.
                            log.pop(computation, None)
                            continue
                        # The run ended this worker, so what it cost is recorded, not raised: the
                        # entry's key names the card and the stage, and the values are what the
                        # run observed of the kill (#46).
                        peak, limit = kill.get("peak"), kill.get("limit")
                        log[computation] = exceeded.Interruption(
                            hash=exceeded.input_hash(computation, lattice),
                            seconds=int(elapsed),
                            lost=True,
                            killed_by=str(kill["by"]),
                            peak_bytes=peak if isinstance(peak, int) else None,
                            limit_bytes=limit if isinstance(limit, int) else None,
                        )
                    exceeded.save(root, log)
                    if kill is None:
                        worker_failures.append(f"{tag} ({values['failed']})")
                    continue
                entry = by_tag[str(values["tag"])]
                worker_name = f"{entry.lattice.tag} worker"
                if "started" not in values and worker_name in failed and failed[worker_name].disposition == "retry":
                    failures.resolve(root, worker_name, entry.lattice)
                    failed[worker_name] = failures.load(root)[worker_name]
                match values:
                    case {"started": list() as started}:
                        for field in started:
                            computation = name(entry.lattice.tag, str(field), entry.lattice.definiteness)
                            log[computation] = exceeded.Interruption(
                                hash=exceeded.input_hash(computation, entry.lattice),
                                seconds=0,
                                lost=True,
                            )
                            running[computation] = time.monotonic()
                        exceeded.save(root, log)
                        continue
                    case {"derived": dict() as derived}:
                        stored_lattice = Lattice.model_validate(derived)
                        computation = name(stored_lattice.tag, "derive")
                        certificate_hash = certificates.certification_hash(computation, stored_lattice, records.derived_projection(derived))
                        derived["certifications"] = {**stored_lattice.certifications, "derive": certificate_hash}
                        storage.write_text(entry.path, records.record_text(keep_other_computations(entry.path, derived), entry.prose))
                        held[computation] = Certificate(hash=certificate_hash, by=str(values["by"]))
                        if computation in failed:
                            failures.resolve(root, computation, stored_lattice)
                        unsaved.add(stored_lattice.tag)
                        log.pop(computation, None)
                        running.pop(computation, None)
                        exceeded.save(root, log)
                        print(stored_lattice.tag, "derive", flush=True)
                        continue
                arithmetic_fields = [field for field in values if isinstance(field, str) and field.startswith(ARITHMETIC_PREFIX)]
                row_fields = [field for field in values if isinstance(field, str) and orbit_row_of(field) is not None]
                for field in (*BLOCKS, *row_fields, *arithmetic_fields):
                    if field in values:
                        log.pop(name(entry.lattice.tag, field, entry.lattice.definiteness), None)
                        running.pop(name(entry.lattice.tag, field, entry.lattice.definiteness), None)
                exceeded.save(root, log)
                store(entry.path, values)
                computed_groups: dict[str, dict[str, Yaml]] = {}
                for field in arithmetic_fields:
                    slug, short = str(field)[len(ARITHMETIC_PREFIX) :].rsplit(".", 1)
                    computed_groups.setdefault(slug, {})[short] = values[field]
                committed_by_group: dict[str, Yaml] = {}
                for slug, group_values in computed_groups.items():
                    for short, committed in store_arithmetic_group(root, entry.lattice.tag, slug, group_values):
                        committed_by_group[f"{ARITHMETIC_PREFIX}{slug}.{short}"] = committed
                stored = corpus.front_matter(corpus.read_card(entry.path))
                stored_lattice = Lattice.model_validate(stored)
                card_certifications = dict(stored_lattice.certifications)
                for field, committed in committed_by_group.items():
                    computation = name(entry.lattice.tag, field, stored_lattice.definiteness)
                    certificate_hash = certificates.certification_hash(computation, stored_lattice, committed)
                    card_certifications[field] = certificate_hash
                    held[computation] = Certificate(hash=certificate_hash, by=str(values["by"]))
                    if computation in failed:
                        failures.resolve(root, computation, stored_lattice)
                # A row of an orbit series certifies the field it belongs to, over the rows the card
                # now stores: the certificate commits to what the card states, and a row that did
                # not return is not part of it (#7).
                certified_fields = [*BLOCKS, *(base for base in dict.fromkeys(orbit_row_of(row)[0] for row in row_fields) if base not in BLOCKS)]
                for field in certified_fields:
                    block_name = stored_in(field, stored_lattice.definiteness)[0]
                    block = stored.get(block_name)
                    if not isinstance(block, dict) or block.get(field) is None:
                        continue
                    computation = name(entry.lattice.tag, field, stored_lattice.definiteness)
                    certificate_hash = certificates.certification_hash(
                        computation,
                        stored_lattice,
                        certified_value(field, block.get(field), stored_lattice),
                    )
                    card_certifications[f"{block_name}.{field}"] = certificate_hash
                    held[computation] = Certificate(hash=certificate_hash, by=str(values["by"]))
                    if computation in failed:
                        failures.resolve(root, computation, stored_lattice)
                # A row that returned resolves the failure its own earlier attempt recorded.
                for row_field in row_fields:
                    row_computation = name(entry.lattice.tag, row_field, stored_lattice.definiteness)
                    if row_computation in failed:
                        failures.resolve(root, row_computation, stored_lattice)
                stored["certifications"] = {name: certificate_hash for name, certificate_hash in card_certifications.items()}
                document = corpus.read_card(entry.path)
                storage.write_text(entry.path, records.record_text(stored, document.content))
                unsaved.add(entry.lattice.tag)
                print(
                    entry.lattice.tag,
                    {field: values[field] for field in (*BLOCKS, *row_fields, *arithmetic_fields) if field in values},
                    flush=True,
                )
    finally:
        checkpoint(final=True)
    if worker_failures:
        raise ChildProcessError(f"{SAGE_MODULE} failed on " + ", ".join(worker_failures))


def cite(path: Path, field: str, value: Yaml, reference: dict[str, str], held: Certificates) -> None:
    """Store `value` of `field` on the card at `path` and certify it by the source that proves it.

    The certificate's provenance is the citation, so certification never
    recomputes the value. A different value already on the card contradicts
    the source and stops the run.
    """
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    block_name, model = stored_in(field, metadata.get("definiteness"))
    block = TypeAdapter(dict[str, Yaml]).validate_python(metadata.get(block_name) or {}, strict=True)
    assert block.get(field) in (None, value), f"{path}: {block_name}.{field} is {block.get(field)}, the source proves {value}"
    block[field] = value
    metadata[block_name] = {key: block[key] for key in model.model_fields if key in block}
    references = TypeAdapter(list[Yaml]).validate_python(metadata.get("references") or [], strict=True)
    if reference not in references:
        metadata["references"] = [*references, {key: value for key, value in reference.items()}]
    lattice = Lattice.model_validate(metadata)
    computation = name(lattice.tag, field, lattice.definiteness)
    certificate_hash = certificates.certification_hash(computation, lattice, certified_value(field, value, lattice))
    metadata["certifications"] = {**lattice.certifications, f"{block_name}.{field}": certificate_hash}
    held[computation] = Certificate(hash=certificate_hash, by=reference["citation"])
    path.write_text(records.record_text(metadata, document.content))


def cite_orbit_row(
    path: Path,
    group: str,
    series: dict[str, Yaml],
    reference: dict[str, str],
    held: Certificates,
) -> None:
    """Store one row of `integral.primitive_orbits` and certify the field by the row's citation.

    A row is the series of one subgroup, keyed by its group: the citation that proves it names
    the paper and the locator, and it joins the card's references. The certificate is one per
    field, so its hash commits to the projected row set and its provenance names the citation of
    every row that carries one, this row's first; certification therefore never recomputes a
    cited row, and a different value already on the card contradicts the source.
    """
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    block_name, model = stored_in("primitive_orbits", metadata.get("definiteness"))
    block = TypeAdapter(dict[str, Yaml]).validate_python(metadata.get(block_name) or {}, strict=True)
    rows = block.get("primitive_orbits")
    series_of_group = dict(TypeAdapter(dict[str, Yaml]).validate_python(rows or {}, strict=True))
    assert series_of_group.get(group) in (None, series), (
        f"{path}: {block_name}.primitive_orbits.{group} is {series_of_group.get(group)}, the source proves {series}"
    )
    series_of_group[group] = series
    block["primitive_orbits"] = {key: series_of_group[key] for key in sorted(series_of_group)}
    metadata[block_name] = {key: block[key] for key in model.model_fields if key in block}
    references = TypeAdapter(list[Yaml]).validate_python(metadata.get("references") or [], strict=True)
    if reference not in references:
        metadata["references"] = [*references, {key: value for key, value in reference.items()}]
    lattice = Lattice.model_validate(metadata)
    computation = name(lattice.tag, "primitive_orbits", lattice.definiteness)
    certificate_hash = certificates.certification_hash(computation, lattice, certified_value("primitive_orbits", block["primitive_orbits"], lattice))
    metadata["certifications"] = {**lattice.certifications, f"{block_name}.primitive_orbits": certificate_hash}
    held[computation] = Certificate(hash=certificate_hash, by=_orbit_provenance(block["primitive_orbits"], reference))
    path.write_text(records.record_text(metadata, document.content))


STATED_IN_A_CHAMBER_ROW = ("cusp", "statement", "printed_page", "figure")
"""The fields of a chamber row that a re-reading of the same statement may not change."""


def _chamber_read_further(row: dict[str, Yaml], rows: list[dict[str, Yaml]]) -> str | None:
    """Why a stored chamber row is not kept by the rows now proved, or `None` when it is.

    A figure of a source is read again, not replaced: the row on the card keeps its cusp, its statement,
    its page and its figure, and every wall it states is still a wall of the row proved now. What a fuller
    reading adds is further walls of the same chamber; a moved wall, a lost wall, or a changed cusp,
    statement, page or figure contradicts the card and is reported instead.
    """
    same = [new for new in rows if new.get("cusp") == row.get("cusp")] if row.get("cusp") is not None else [new for new in rows if new.get("statement") == row.get("statement")]
    if not same:
        return f"the row at the cusp {row.get('cusp')} is not among the rows proved now"
    read = same[0]
    for key in STATED_IN_A_CHAMBER_ROW:
        if read.get(key) != row.get(key):
            return f"the row at the cusp {row.get('cusp')} changes its {key} from {row.get(key)} to {read.get(key)}"
    walls = {(wall.get("name"), tuple(wall.get("vector") or ())) for wall in read.get("walls") or []}
    for wall in row.get("walls") or []:
        if (wall.get("name"), tuple(wall.get("vector") or ())) not in walls:
            return f"the wall {wall.get('name')} of the row at the cusp {row.get('cusp')} is dropped or moved"
    return None


def cite_cusp_chambers(
    path: Path,
    group: str,
    rows: list[dict[str, Yaml]],
    reference: dict[str, str],
    by: str,
    held: Certificates,
) -> None:
    """Store the chambers at the cusps of one subgroup that a source prints, and certify them.

    A row is the chamber at one cusp: its walls are the source's vectors, and its Gram matrix,
    Coxeter diagram and wall count are computed from the card's Gram tensor. The certificate is
    one per field, so its hash commits to every row of every subgroup and its provenance names
    the citation that prints the walls and the program that computed the invariants of them.
    A stored row is neither dropped nor contradicted: the cusp, statement, page and figure of a row
    already on the card stay, and every wall it states is still a wall of the row proved now, so a
    fuller reading of the same statement adds walls and a further statement of the same source adds
    its cusp's row. Anything else stops the writer, with the field that moved.
    """
    _write_cusp_chambers(path, group, rows, reference, by, held)


def store_cusp_chambers(
    path: Path,
    group: str,
    rows: list[dict[str, Yaml]],
    by: str,
    held: Certificates,
) -> None:
    """Store the chambers of one subgroup that a computation produced, and certify them by it.

    No source prints these rows, so none cites one: `by` names the operation and its revision, and
    the row states no statement, page or figure. The Gram matrix, the diagram, the wall count and the
    ideal-vertex count are what the operation returned and what the card's Gram tensor says about it —
    `latticedb certify` never requests this field, so a computation that fills it is the caller's, and
    its provenance is what keeps it checkable.
    """
    _write_cusp_chambers(path, group, rows, None, by, held)


def _write_cusp_chambers(
    path: Path,
    group: str,
    rows: list[dict[str, Yaml]],
    reference: dict[str, str] | None,
    by: str,
    held: Certificates,
) -> None:
    """Store the rows of one subgroup on the loaded block and write the field's one certificate."""
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    block_name, model = stored_in("cusp_chambers", metadata.get("definiteness"))
    block = TypeAdapter(dict[str, Yaml]).validate_python(metadata.get(block_name) or {}, strict=True)
    chambers = block.get("cusp_chambers")
    rows_of_group = dict(TypeAdapter(dict[str, Yaml]).validate_python(chambers or {}, strict=True))
    stored = TypeAdapter(list[Yaml]).validate_python(rows_of_group.get(group) or [], strict=True)
    for row in stored:
        problem = _chamber_read_further(dict(TypeAdapter(dict[str, Yaml]).validate_python(row, strict=True)), rows)
        assert problem is None, f"{path}: {block_name}.cusp_chambers.{group}: {problem}"
    rows_of_group[group] = rows
    block["cusp_chambers"] = {key: rows_of_group[key] for key in sorted(rows_of_group)}
    metadata[block_name] = {key: block[key] for key in model.model_fields if key in block}
    if reference is not None:
        references = TypeAdapter(list[Yaml]).validate_python(metadata.get("references") or [], strict=True)
        if reference not in references:
            metadata["references"] = [*references, {key: value for key, value in reference.items()}]
    lattice = Lattice.model_validate(metadata)
    computation = name(lattice.tag, "cusp_chambers", lattice.definiteness)
    certificate_hash = certificates.certification_hash(computation, lattice, certified_value("cusp_chambers", block["cusp_chambers"], lattice))
    metadata["certifications"] = {**lattice.certifications, f"{block_name}.cusp_chambers": certificate_hash}
    held[computation] = Certificate(hash=certificate_hash, by=by)
    path.write_text(records.record_text(metadata, document.content))


def store_cusp_root_orbits(
    path: Path,
    group: str,
    rows: list[dict[str, Yaml]],
    by: str,
    held: Certificates,
) -> None:
    """Store the orbits of the root classes at the cusps of one subgroup that a computation decided, and certify them.

    No source prints these rows: the count is the computation's own, and where the cusp's root family has one class
    the count is one orbit whatever the group is, which is the case a computation can decide without a generating
    family of the cusp stabilizer (`genus.applies` refuses the field for the general case, sage-extensions#603).
    `by` names the program and the revision that returned the rows, and the certificate's hash commits to every row
    of every subgroup of the card, in the manner of `store_cusp_chambers`.

    A row already stored at one of these cusps is neither dropped nor changed: a second computation that states that
    cusp differently stops the writer, and one that states a further cusp adds that row and keeps the rest.
    """
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    block_name, model = stored_in("cusp_root_orbits", metadata.get("definiteness"))
    block = TypeAdapter(dict[str, Yaml]).validate_python(metadata.get(block_name) or {}, strict=True)
    stated = block.get("cusp_root_orbits")
    rows_of_group = dict(TypeAdapter(dict[str, Yaml]).validate_python(stated or {}, strict=True))
    stored = TypeAdapter(list[Yaml]).validate_python(rows_of_group.get(group) or [], strict=True)
    cusps: dict[tuple[int, ...], dict[str, Yaml]] = {}
    for row in stored:
        cusp = tuple(TypeAdapter(list[int]).validate_python(row.get("cusp") or [], strict=True))
        cusps[cusp] = dict(TypeAdapter(dict[str, Yaml]).validate_python(row, strict=True))
    for row in rows:
        cusp = tuple(TypeAdapter(list[int]).validate_python(row.get("cusp") or [], strict=True))
        if cusp in cusps:
            assert cusps[cusp] == row, f"{path}: {block_name}.cusp_root_orbits.{group}: the row at the cusp {list(cusp)} is stated twice, differently"
        else:
            cusps[cusp] = row
    rows_of_group[group] = [cusp for _, cusp in sorted(cusps.items())]
    block["cusp_root_orbits"] = {key: rows_of_group[key] for key in sorted(rows_of_group)}
    metadata[block_name] = {key: block[key] for key in model.model_fields if key in block}
    lattice = Lattice.model_validate(metadata)
    computation = name(lattice.tag, "cusp_root_orbits", lattice.definiteness)
    certificate_hash = certificates.certification_hash(computation, lattice, certified_value("cusp_root_orbits", block["cusp_root_orbits"], lattice))
    metadata["certifications"] = {**lattice.certifications, f"{block_name}.cusp_root_orbits": certificate_hash}
    held[computation] = Certificate(hash=certificate_hash, by=by)
    path.write_text(records.record_text(metadata, document.content))


def _orbit_provenance(series_of_group: dict[str, Yaml], reference: dict[str, str]) -> str:
    """The citations of the rows a certificate commits to, this row's own first."""
    citations = [reference["citation"]]
    for key in sorted(series_of_group):
        row = series_of_group[key]
        cited = row.get("reference") if isinstance(row, dict) else None
        citation = cited.get("citation") if isinstance(cited, dict) else None
        if citation and citation not in citations:
            citations.append(citation)
    return "; ".join(citations)
