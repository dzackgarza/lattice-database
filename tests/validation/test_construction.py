"""CI validation by constructing stored mathematical arrows in the preamble.

There are no lattice equations or independent algorithms here.  A stored map is
mathematically valid exactly when the corresponding preamble constructor accepts
it.  Algorithms and constructor contracts are tested at their preamble owners.

Each check reads the cards one file at a time: this corpus's 302,504 validated card models cost
about 7.5 GiB, and a check needs each card only for the length of its own morphisms, root span or
monodromy. The morphism check also runs in fresh processes, one chunk of cards each, because the
preamble keeps every structure it constructs for the life of the process: constructing the stored
morphisms of 302,504 cards in one process reaches about 19 GiB and the runner kills it, while a
chunk of 38,000 reaches about 3 GiB. `latticedb verify` splits the same way for the same reason
(`latticedb/checks/__init__.py`).

The assertions are the ones this file always made — every stored morphism states its scale, every
endpoint constructs, and every root-span embedding and monodromy generator constructs as the
preamble's morphism or automorphism — and a chunk that dies is a failure, never a pass: its exit
status is part of the verdict.
"""

import json
import subprocess
import sys
import traceback
from concurrent.futures import ThreadPoolExecutor
from collections.abc import Iterator
from pathlib import Path

import pytest
from sage_extensions.categories.lattices import Lattices
from sage_extensions.categories.modules.framed.formed.form_modules import FormModules
from sage_extensions.categories.modules.pure.modules import Modules
from sage_extensions.rings import session_ring_objects

from latticedb import corpus
from latticedb.catalogues import IntegralLocalSystem
from latticedb.model import Lattice, Yaml

REPOSITORY = Path(__file__).resolve().parent.parent.parent
_RINGS = session_ring_objects()
ZZ = _RINGS["ZZ"]
QQ = _RINGS["QQ"]
_QQ_AS_ZZ_MODULE = Modules(QQ).restriction_of_scalars(ZZ.fraction_field_map())(QQ)


@pytest.fixture(scope="module")
def paths() -> dict[str, Path]:
    """The card of each tag. A path costs tens of bytes; the card it names costs far more."""
    return {path.stem: path for path in sorted((REPOSITORY / "lattices").glob("*.md"))}


def _metadata(path: Path) -> dict[str, Yaml]:
    """A card's front matter, read and not validated."""
    return corpus.front_matter(corpus.read_card(path))


def _card(path: Path) -> Lattice:
    """A card's validated record."""
    return Lattice.model_validate(_metadata(path))


def _morphisms(metadata: dict[str, Yaml]) -> list[dict[str, Yaml]]:
    """The stored morphisms of a card's front matter."""
    stored = metadata.get("morphisms")
    return [morphism for morphism in stored if isinstance(morphism, dict)] if isinstance(stored, list) else []


def _owned(lattice: Lattice):
    """Construct the preamble object represented by a lattice card."""
    assert lattice.rank is not None and lattice.gram_tensor is not None
    if lattice.integral is not None:
        return Lattices(ZZ)(lattice.gram_tensor)
    module = ZZ.free_module(lattice.rank)
    return FormModules(ZZ)(module.bilinear_hom_space(_QQ_AS_ZZ_MODULE)(lattice.gram_tensor))


def _local_systems() -> Iterator[IntegralLocalSystem]:
    """Each stored integral local system, validated as the corpus reader validates one."""
    for path in sorted((REPOSITORY / "integral-local-systems").glob("*.md")):
        yield IntegralLocalSystem.model_validate(corpus.read_card(path).metadata)


WORKERS = 8
"""How many chunks the morphism check is split into, each in a process of its own."""

CONCURRENCY = 2
"""How many chunks run at once: a chunk of these cards peaks near 3 GiB, so two stay well inside a
runner's memory while halving the wall time of a check that constructs half a million morphisms."""

_WORKER = """
import json, runpy, sys
module = runpy.run_path(sys.argv[1])
print(json.dumps(module["_construct"](json.loads(sys.stdin.read()))))
"""
"""The worker that constructs one chunk: this file's own `_construct`, in a process of its own.

The chunk arrives on standard input: a chunk of this corpus is tens of thousands of tags, which is
more than one argument may carry.
"""


def _construct(tags: list[str]) -> list[str]:
    """Construct every stored morphism of `tags` in this process, and report each failure as a line."""
    failures: list[str] = []
    for tag in tags:
        try:
            metadata = _metadata(REPOSITORY / "lattices" / f"{tag}.md")
            if not _morphisms(metadata):
                continue
            source_card = Lattice.model_validate(metadata)
            assert source_card.morphisms, f"{tag}: front matter states a morphism its card refuses"
            for stored in source_card.morphisms:
                assert stored.scale is not None, f"{tag} -> {stored.target}: source must state the morphism scale before verification"
                target_card = source_card if stored.target == source_card.tag else _card(REPOSITORY / "lattices" / f"{stored.target}.md")
                target = _owned(target_card)
                source = _owned(source_card).twist(stored.scale)
                category = Lattices(ZZ) if source_card.integral is not None and target_card.integral is not None else FormModules(ZZ)
                category.Mor(source, target)(tuple(target(image) for image in stored.images))
        except Exception:
            failures.append(f"{tag}: {traceback.format_exc()}")
    return failures


def test_stored_lattice_morphisms_construct_in_the_preamble(paths: dict[str, Path]) -> None:
    """Every card's morphisms state their scale, and their endpoints and images construct.

    The cards are constructed in `WORKERS` chunks, each in a process of its own, and the test fails
    on any assertion any chunk raises and on any chunk that ends without reporting its chunk.
    """
    tags = sorted(paths)
    size = -(-len(tags) // WORKERS)
    chunks = [tags[start : start + size] for start in range(0, len(tags), size)]

    def run(chunk: list[str]) -> list[str]:
        completed = subprocess.run(
            [sys.executable, "-c", _WORKER, str(Path(__file__).resolve())],
            input=json.dumps(chunk),
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode != 0 or not completed.stdout.strip():
            return [f"cards {chunk[0]}..{chunk[-1]}: the chunk ended with status {completed.returncode} and no result: {completed.stderr[-2000:]}"]
        return json.loads(completed.stdout)

    failures: list[str] = []
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as workers:
        for reported in workers.map(run, chunks):
            failures.extend(reported)
    assert failures == [], "\n".join(failures)


def test_integral_root_span_sum_embeddings_construct_in_the_preamble(paths: dict[str, Path]) -> None:
    """Every stored root-span embedding constructs as the preamble's morphism between its lattices."""
    category = Lattices(ZZ)
    for tag, path in paths.items():
        metadata = _metadata(path)
        span = metadata.get("root_span")
        if not isinstance(span, dict) or span.get("embedding") is None or metadata.get("integral") is None:
            continue
        target_card = _card(path)
        stored_span = target_card.root_span
        if stored_span is None or stored_span.summands is None or stored_span.embedding is None or not stored_span.summands:
            continue
        summand_cards = [_card(paths[summand.tag]) for summand in stored_span.summands]
        if any(summand_card.integral is None for summand_card in summand_cards):
            continue
        target = category(target_card.gram_tensor)
        # The owner's orthogonal sum retains the module biproduct; `biproduct` is the categorical
        # request that a form-preserving map does not supply, and is not what a card states here.
        source = category.orthogonal_sum(
            tuple(
                category(summand_card.gram_tensor).twist(summand.scale)
                for summand, summand_card in zip(stored_span.summands, summand_cards, strict=True)
            )
        )
        category.Mor(source, target)(tuple(target(row) for row in stored_span.embedding))


def test_local_system_monodromies_construct_as_preamble_automorphisms(paths: dict[str, Path]) -> None:
    """Every stored monodromy generator constructs as an automorphism of its fibre lattice."""
    for system in _local_systems():
        if system.fiber_lattice is None:
            continue
        fiber = _owned(_card(paths[system.fiber_lattice]))
        for generator in system.monodromy_generators:
            columns = tuple(tuple(row[index] for row in generator.matrix) for index in range(system.rank))
            fiber.Aut()(tuple(fiber(column) for column in columns))
