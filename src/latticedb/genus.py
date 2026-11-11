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
from latticedb.certificates import Certificate, Certificates
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
"""The block of an indefinite card's automorphism data: the generators of $O(L)$, no order.

$O(L)$ of an indefinite lattice is infinite, so the card states the group by its
generators; the order is a field of `definite` alone (#8).
"""

ORBIT_CERTIFIED_BOUND = card_serialization.ORBIT_CERTIFIED_BOUND
"""The z/w degree through which the preamble orbit computation certifies a series."""


def certified_value(field: str, value: Yaml, lattice: Lattice | None = None) -> Yaml:
    """The stored value committed to by one completed preamble computation."""
    if field == "automorphism_group_generator_morphisms":
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

    The database asks for a field when two things hold: the card can store the value,
    and the card lies in the domain the owner states for the operation. Neither is a
    guess at what the owner can compute — the owner says where it is defined, in its
    own errors ("spinor genera of Integral lattice of rank 2 and signature (2, 0)
    require a nondegenerate lattice of finite rank at least three") and in the schema,
    and a card outside a domain gets no field rather than a failure queued every run.

    The database's own facts:
    - `cusp_form_coordinates`: the owner does not present it.
    - The block a value is stored in names its hypothesis, so a field of `definite`,
      `indefinite`, `hyperbolic` or `integral` is asked only on a card that satisfies
      it; a value written into `definite` on an indefinite card would contradict the
      card's `definiteness`.
    - `roots` and `norms` are stored in `root_span`, which the schema refuses on a
      definite card, whose roots are `definite.roots`.

    The owner's stated domain:
    - `spinor_regular`, `spinor_genus_count` and `spinor_genera`: rank at least 3, as
      the owner's error states.
    - `siegel_eisenstein_coefficients`: rank at least 2, Siegel's Hauptsatz requiring
      more than one variable.
    - `reflective`: rank at least 3, signature (1, 1) being a half-line where no
      polyhedron criterion applies.
    - `discriminant_sequence`: a definite even card, its discriminant form being the
      quadratic form of an even lattice.
    - `discriminant_orbits`: the Eichler hypothesis of `theory/orbits.md`, an even
      lattice of hyperbolic index at least 2.
    - `polarization_counts`: no preamble operation presents a table of a source, and
      every count it holds is certified by the citation of that table.
    - `cusp_chambers`: a chamber is the source's walls, and the Gram matrix, diagram
      and wall count of them are what the card's form says; no preamble operation
      searches for a chamber, and a Vinberg search is never run to fill a row.
    - `discriminant_form`: $q_L$ is a quadratic form only on an even lattice, and the owner
      partitions $A_L$, so the request is made on an even card whose classes of $A_L$ are few,
      $|A_L| = |\\det L| \\leq 4096$.

    Everything else — including `integral.primitive_orbits` and the automorphism
    generators on an indefinite card — is asked on every card that can store it (#8).
    """
    if field in {"cusp_form_coordinates", "polarization_counts", "cusp_chambers"}:
        return False
    block_name, _model = stored_in(field, lattice.definiteness)
    match block_name:
        # The block gate only rejects: a field it admits still has to pass the
        # operation's own domain below, which is how a definite card of rank 2 is
        # refused for spinor regularity.
        case "definite" if lattice.definite is None:
            return False
        case "indefinite" if lattice.indefinite is None:
            return False
        case "hyperbolic" if lattice.hyperbolic is None:
            return False
        case "integral" if lattice.integral is None:
            return False
    rank = lattice.rank
    match field:
        case "roots" | "norms":
            return lattice.definite is None
        case "discriminant_form":
            # q_L is a quadratic form only on an even lattice, and the orbit partition is of the
            # classes of A_L, so the request is made on an even card with |A_L| = |det L| small.
            return (
                lattice.integral is not None
                and lattice.integral.parity == "even"
                and lattice.determinant is not None
                and abs(lattice.determinant) <= 4096
            )
        case "reflective" | "spinor_regular" | "spinor_genus_count" | "spinor_genera":
            if rank is None:
                raise ValueError(f"{field} requires a stored source rank")
            return rank >= 3
        case "siegel_eisenstein_coefficients":
            if rank is None:
                raise ValueError(f"{field} requires a stored source rank")
            return rank >= 2
        case "discriminant_sequence":
            return lattice.definite is not None and lattice.integral.parity == "even"
        case "discriminant_orbits":
            return lattice.definite is None and lattice.integral.parity == "even" and (lattice.integral.hyperbolic_index or 0) >= 2
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
    resumed: NotRequired[bool]
    """A computation of these fields was cut short by an earlier job."""


def stored_in(field: str, definiteness: str | None = None) -> tuple[str, type[BaseModel]]:
    """The block that stores `field` on a card of `definiteness`, and that block's model.

    A definite card states the order of $O(L)$ with its generators in `definite`, where
    `BLOCKS` keeps every field. An indefinite lattice's $O(L)$ is infinite, so its data
    is the generators alone and lives in `automorphisms` (#8).
    """
    match (field, definiteness):
        case ("automorphism_group_generator_morphisms", "indefinite"):
            return AUTOMORPHISMS, Automorphisms
        case ("polarization_counts", _):
            # Outside BLOCKS: the preamble does not compute it, and a cited count is never requested.
            return "integral", IntegralData
        case _:
            return BLOCKS[field]


def name(tag: str, field: str, definiteness: str | None = None) -> str:
    """The name of the certificate of `field` of the record `tag`, in the block that stores it."""
    return f"{tag} derive" if field == "derive" else f"{tag} {stored_in(field, definiteness)[0]}.{field}"


def in_shard(tag: str, shard: tuple[int, int]) -> bool:
    """Whether the card `tag` belongs to shard `i` of `n`, by a hash that every job computes alike."""
    index, count = shard
    return certificates.tag_hash(tag) % count == index


def requests(
    loaded: corpus.Corpus,
    held: Certificates,
    log: exceeded.Interruptions,
    tags: tuple[str, ...],
    shard: tuple[int, int] = (0, 1),
    *,
    failed: failures.Failures | None = None,
) -> list[Request]:
    """For each nondegenerate record in `shard`, the uncertified applicable preamble computations.

    A computation that ran for a whole job without finishing is not requested. One
    that a job ended after a shorter time is requested first in its phase, so it runs
    for a whole job. The other cards follow by rank and then absolute determinant. The
    semi-decisions of every card are separate requests after all of them: every job
    ends inside a search, so a cut search resumed at the start of the next job would
    hold its workers through the fields that every procedure finishes. A computation
    that was running when a runner died comes after everything else, so a computation
    that ends its runner cannot end the next job early.
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
            if stored_value is None or certificates.is_pending(held, computation, cited.get(f"{block_name}.{field}"), expected_hash):
                fields.append(field)
        if needs_derive:
            fields.insert(0, "derive")
        if needs_derive and exceeded.was_lost(log, derive_name, lattice):
            # Without its derivation the card has no hypotheses for its other fields.
            lost_fields, fields = fields, []
        else:
            lost_fields = [field for field in fields if exceeded.was_lost(log, name(lattice.tag, field, lattice.definiteness), lattice)]
            fields = [field for field in fields if field not in lost_fields]
        gram = [[int(value) if value.denominator == 1 else str(value) for value in row] for row in lattice.gram_tensor]
        if lost_fields:
            lost.append({"tag": lattice.tag, "gram": gram, "integral": lattice.integral is not None, "fields": lost_fields, "series_bound": series_bound(len(gram))})
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
    """
    queue = deque(chosen)
    if not queue:
        return
    reserve = MEMORY_RESERVE * _meminfo("MemTotal")
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
                    largest = max(candidates, key=lambda process: _resident_bytes(process.pid))
                    exhausted.add(largest)
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
                            reason = "memory exhausted" if process in exhausted else f"exit status {process.returncode}"
                            error = stderr(process)
                            yield {"tag": request["tag"], "failed": reason, **({"stderr": error} if error else {})}
                        errors.pop(process).close()
                        exhausted.discard(process)
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


def _generator_morphisms(tag: str, morphisms: list[dict[str, Yaml]], matrices: list[Yaml]) -> tuple[list[str], list[dict[str, Yaml]]]:
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
            base = f"O(L) generator {index}"
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
    """Replace each computed scope on the card by the completed computation."""
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    morphisms = TypeAdapter(list[dict[str, Yaml]]).validate_python(metadata.get("morphisms", []), strict=True)
    if "roots" in values:
        # Computed roots generate L, so L = ZPhi(L) and the block has no summands or embedding.
        metadata["root_span"] = {}
    for field in BLOCKS:
        value = values.get(field)
        if value is None:
            continue
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


def certify(
    root: Path,
    loaded: corpus.Corpus,
    held: Certificates,
    tags: tuple[str, ...],
    deadline: float,
    workers: int = 1,
    shard: tuple[int, int] = (0, 1),
    searches: bool | None = None,
) -> None:
    """Compute every uncertified value on `workers` processes, replace its card scope, and certify the result.

    `searches` takes one phase of the queue: `False` the terminating fields alone, `True` the
    semi-decision searches alone. A search can hold a worker for a whole job, so a dispatched run
    that only wants the fields does not wait for one, and the searches are a job of their own.
    `deadline` is the time, in seconds since the epoch, at which the job's timeout
    ends this run. A computation in progress is logged in `exceeded.yaml` until it
    finishes, checkpointing the seconds actually spent in this run. A worker that
    fails on a card ends no other card's computations; the run raises after the
    queue is done, so the failure is reported with every completed value stored.
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
        with closing(computed(in_phase(requests(loaded, held, log, tags, shard, failed=failed), searches), deadline, workers)) as stream:
            for values in stream:
                if "checkpoint" in values:
                    checkpoint()
                    continue
                if "deadline" in values:
                    print("Certification time budget exhausted", flush=True)
                    break
                if "failed" in values:
                    tag = str(values["tag"])
                    active = [computation for computation in running if computation.startswith(f"{tag} ")]
                    for computation in active or [f"{tag} worker"]:
                        elapsed = time.monotonic() - running[computation] if computation in running else 0
                        failed[computation] = failures.record(root, computation, by_tag[tag].lattice, str(values["failed"]), str(values.get("stderr", "")), elapsed)
                    for computation in active:
                        started_at = running.pop(computation)
                        if values["failed"] == "memory exhausted":
                            # Preserve its interruption evidence; triage quarantines the retry.
                            log[computation] = exceeded.Interruption(hash=log[computation].hash, seconds=int(time.monotonic() - started_at), lost=True)
                        else:
                            # A failure is a defect to repair, not a computation that outran its job.
                            log.pop(computation, None)
                    exceeded.save(root, log)
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
                for field in BLOCKS:
                    if field in values:
                        log.pop(name(entry.lattice.tag, field, entry.lattice.definiteness), None)
                        running.pop(name(entry.lattice.tag, field, entry.lattice.definiteness), None)
                exceeded.save(root, log)
                store(entry.path, values)
                stored = corpus.front_matter(corpus.read_card(entry.path))
                stored_lattice = Lattice.model_validate(stored)
                card_certifications = dict(stored_lattice.certifications)
                for field in BLOCKS:
                    if field not in values or values[field] is None:
                        continue
                    block_name = stored_in(field, stored_lattice.definiteness)[0]
                    block = stored.get(block_name)
                    assert isinstance(block, dict)
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
                stored["certifications"] = {name: certificate_hash for name, certificate_hash in card_certifications.items()}
                document = corpus.read_card(entry.path)
                storage.write_text(entry.path, records.record_text(stored, document.content))
                unsaved.add(entry.lattice.tag)
                print(
                    entry.lattice.tag,
                    {field: values[field] for field in BLOCKS if field in values},
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


def cite_cusp_chambers(
    path: Path,
    group: str,
    rows: list[dict[str, Yaml]],
    reference: dict[str, str],
    by: str,
    held: Certificates,
) -> None:
    """Store the chambers at the cusps of one subgroup and certify them.

    A row is the chamber at one cusp: its walls are the source's vectors, and its Gram matrix,
    Coxeter diagram and wall count are computed from the card's Gram tensor. The certificate is
    one per field, so its hash commits to every row of every subgroup and its provenance names
    the citation that prints the walls and the program that computed the invariants of them.
    A stored row is neither dropped nor contradicted: the rows already on the card must be among
    the rows the source proves, so a further statement of the same source adds its cusp's row to
    the ones already stored and stops the writer only where the two disagree.
    """
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    block_name, model = stored_in("cusp_chambers", metadata.get("definiteness"))
    block = TypeAdapter(dict[str, Yaml]).validate_python(metadata.get(block_name) or {}, strict=True)
    chambers = block.get("cusp_chambers")
    rows_of_group = dict(TypeAdapter(dict[str, Yaml]).validate_python(chambers or {}, strict=True))
    stored = TypeAdapter(list[Yaml]).validate_python(rows_of_group.get(group) or [], strict=True)
    for row in stored:
        assert row in rows, (
            f"{path}: {block_name}.cusp_chambers.{group} holds the row {row}, which is not among the rows the source proves {rows}"
        )
    rows_of_group[group] = rows
    block["cusp_chambers"] = {key: rows_of_group[key] for key in sorted(rows_of_group)}
    metadata[block_name] = {key: block[key] for key in model.model_fields if key in block}
    references = TypeAdapter(list[Yaml]).validate_python(metadata.get("references") or [], strict=True)
    if reference not in references:
        metadata["references"] = [*references, {key: value for key, value in reference.items()}]
    lattice = Lattice.model_validate(metadata)
    computation = name(lattice.tag, "cusp_chambers", lattice.definiteness)
    certificate_hash = certificates.certification_hash(computation, lattice, certified_value("cusp_chambers", block["cusp_chambers"], lattice))
    metadata["certifications"] = {**lattice.certifications, f"{block_name}.cusp_chambers": certificate_hash}
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
