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
from contextlib import ExitStack, closing
from fractions import Fraction
from pathlib import Path
from tempfile import TemporaryFile
from typing import BinaryIO
from typing import NotRequired, TypedDict

import frontmatter
from pydantic import BaseModel, TypeAdapter

from latticedb import certificates, corpus, exceeded, failures, records, storage
from latticedb.certificates import Certificate, Certificates
from latticedb.model import (
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
    "primitive_orbits": ("integral", IntegralData),
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

ORBIT_CERTIFIED_BOUND = 4
"""The z/w degree through which the bounded preamble orbit computation certifies a series."""


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
        if not isinstance(value, dict):
            return value
        projected: dict[str, Yaml] = {}
        for group, series in value.items():
            if not isinstance(series, dict):
                projected[group] = series
                continue
            z = series.get("z")
            w = series.get("w")
            projected[group] = {
                "constant": series.get("constant"),
                "z": z[:ORBIT_CERTIFIED_BOUND] if isinstance(z, list) else z,
                "w": w[:ORBIT_CERTIFIED_BOUND] if isinstance(w, list) else w,
            }
        return projected
    return value


def applies(field: str, lattice: Lattice) -> bool:
    """Whether the preamble exposes `field` on this stored lattice."""
    match field:
        case "integer_valued":
            return True
        case "automorphism_group_order" | "automorphism_group_generator_morphisms":
            return lattice.definite is not None
        case _ if lattice.integral is None:
            return False
        case "reflective":
            if lattice.rank is None:
                raise ValueError(f"{field} requires a stored source rank")
            # Signature (1, 1) has a half-line as its domain, where no polyhedron criterion applies.
            return lattice.rank >= 3 and 1 in (lattice.signature or ())
        case "roots" | "norms":
            return lattice.definite is None
        case "cusp_form_coordinates":
            # The preamble does not present it yet: TODO node `theta-cusp-form-coordinates`.
            return False
        case "siegel_eisenstein_coefficients":
            if lattice.definite is None:
                return False
            if lattice.rank is None:
                raise ValueError(f"{field} requires a stored source rank")
            # Siegel's Hauptsatz requires more than one variable.
            return lattice.rank >= 2
        case "regular" | "genus_theta_series" | "theta_series_cuspidal_component":
            return lattice.definite is not None
        case "spinor_regular":
            if lattice.definite is None:
                return False
            if lattice.rank is None:
                raise ValueError(f"{field} requires a stored source rank")
            return lattice.rank >= 3
        case "discriminant_sequence":
            return lattice.definite is not None and lattice.integral.parity == "even"
        case "spinor_genus_count" | "spinor_genera":
            if lattice.rank is None:
                raise ValueError(f"{field} requires a stored source rank")
            return lattice.rank >= 3
        case "primitive_orbits":
            return lattice.definite is not None
        case "discriminant_orbits":
            index = lattice.integral.hyperbolic_index or 0
            return lattice.definite is None and lattice.integral.parity == "even" and index >= 2
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


def name(tag: str, field: str) -> str:
    """The name of the certificate of `field` of the record `tag`."""
    return f"{tag} derive" if field == "derive" else f"{tag} {BLOCKS[field][0]}.{field}"


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
            block_name = BLOCKS[field][0]
            block = metadata.get(block_name)
            stored_value = block.get(field) if isinstance(block, dict) else None
            computation = name(lattice.tag, field)
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
            lost_fields = [field for field in fields if exceeded.was_lost(log, name(lattice.tag, field), lattice)]
            fields = [field for field in fields if field not in lost_fields]
        gram = [[int(value) if value.denominator == 1 else str(value) for value in row] for row in lattice.gram_tensor]
        if lost_fields:
            lost.append({"tag": lattice.tag, "gram": gram, "integral": lattice.integral is not None, "fields": lost_fields, "series_bound": series_bound(len(gram))})
            if needs_derive:
                lost[-1]["record"] = metadata
            sizes[lattice.tag] = (len(gram), abs(lattice.determinant or Fraction(0)))
        if fields:
            interrupted = [field for field in fields if exceeded.seconds_run(log, name(lattice.tag, field), lattice) is not None]
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
                (resumed_searches if set(interrupted) & SEMI_DECISIONS else searches).append({**request, "fields": semi})
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
        # worker is kept from them, so every job certifies new values.
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
            assert process.stdin is not None
            request = next_request()
            holding[process] = request
            started[process] = set()
            process.stdin.write((json.dumps(request) + "\n").encode())
            process.stdin.flush()

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
                        assert process.stdin is not None and process.stdout is not None
                        process.stdin.close()
                        process.stdout.close()
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


def store(path: Path, values: dict[str, Yaml]) -> None:
    """Replace each computed scope on the card by the completed computation."""
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    morphisms = TypeAdapter(list[dict[str, Yaml]]).validate_python(metadata.get("morphisms", []), strict=True)
    if "roots" in values:
        # Computed roots generate L, so L = ZPhi(L) and the block has no summands or embedding.
        metadata["root_span"] = {}
    for field, (block_name, model) in BLOCKS.items():
        value = values.get(field)
        if value is None:
            continue
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


def certify(
    root: Path,
    loaded: corpus.Corpus,
    held: Certificates,
    tags: tuple[str, ...],
    deadline: float,
    workers: int = 1,
    shard: tuple[int, int] = (0, 1),
) -> None:
    """Compute every uncertified value on `workers` processes, replace its card scope, and certify the result.

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
            if short not in BLOCKS or name(tag, short) != computation:
                continue
            block = metadata.get(BLOCKS[short][0])
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
        with closing(computed(requests(loaded, held, log, tags, shard, failed=failed), deadline, workers)) as stream:
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
                            computation = name(entry.lattice.tag, str(field))
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
                        storage.write_text(entry.path, records.record_text(derived, entry.prose))
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
                        log.pop(name(entry.lattice.tag, field), None)
                        running.pop(name(entry.lattice.tag, field), None)
                exceeded.save(root, log)
                store(entry.path, values)
                stored = corpus.front_matter(corpus.read_card(entry.path))
                stored_lattice = Lattice.model_validate(stored)
                card_certifications = dict(stored_lattice.certifications)
                for field in BLOCKS:
                    if field not in values or values[field] is None:
                        continue
                    block_name = BLOCKS[field][0]
                    block = stored.get(block_name)
                    assert isinstance(block, dict)
                    computation = name(entry.lattice.tag, field)
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
    block_name = BLOCKS[field][0]
    block = TypeAdapter(dict[str, Yaml]).validate_python(metadata.get(block_name) or {}, strict=True)
    assert block.get(field) in (None, value), f"{path}: {block_name}.{field} is {block.get(field)}, the source proves {value}"
    block[field] = value
    metadata[block_name] = {key: block[key] for key in BLOCKS[field][1].model_fields if key in block}
    references = TypeAdapter(list[Yaml]).validate_python(metadata.get("references") or [], strict=True)
    if reference not in references:
        metadata["references"] = [*references, {key: value for key, value in reference.items()}]
    lattice = Lattice.model_validate(metadata)
    computation = name(lattice.tag, field)
    certificate_hash = certificates.certification_hash(computation, lattice, certified_value(field, value, lattice))
    metadata["certifications"] = {**lattice.certifications, f"{block_name}.{field}": certificate_hash}
    held[computation] = Certificate(hash=certificate_hash, by=reference["citation"])
    path.write_text(records.record_text(metadata, document.content))
