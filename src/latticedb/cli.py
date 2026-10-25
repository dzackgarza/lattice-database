"""Seed, author, enrich, verify, and publish lattice cards."""

import json
import os
import signal
import sys
import time
from pathlib import Path
from types import FrameType
from typing import Annotated
from urllib.request import Request, urlopen

import frontmatter
import yaml
from cyclopts import App, Parameter
from pydantic import TypeAdapter

from latticedb import (
    bulk_index,
    bulk_sources,
    certificates,
    checks,
    corpus,
    failures,
    genus,
    keyed_merge,
    records,
    regular_ternaries,
    seed,
    site,
    summands,
)
from latticedb.model import GramTensor, Lattice, Yaml

SERVED = Path("/var/www/static-sites/lattice-database")
ADDRESS = "http://127.0.0.1/"
HOST = "lattice-database.localhost"

app = App(name="latticedb", help=__doc__)

Root = Annotated[Path, Parameter(help="Directory that holds `lattices/` and `pages/`.")]
Aliases = Annotated[
    tuple[str, ...],
    Parameter(
        name="--alias",
        help="Another name of the lattice, as plain text; repeat for each one.",
    ),
]
Families = Annotated[
    tuple[str, ...],
    Parameter(name="--family", help="A family that contains the lattice; repeat for each one."),
]


def _refuse(found: list[str]) -> None:
    """Print the problems and exit with status 1 when there are any."""
    if found:
        print("\n".join(found), file=sys.stderr)
        sys.exit(1)


def _author(root: Root, declared: dict[str, Yaml], prose: str) -> Path:
    """Write a new card with a filename-only tag allocation."""
    tag = corpus.next_tag(root)
    path = root / "lattices" / f"{tag}.md"
    with path.open("x") as output:
        output.write(records.record_text({"tag": tag, **declared}, prose))
    return path


@app.command
def new(
    *,
    gram: Annotated[
        str,
        Parameter(help="The components b(e_i, e_j) as JSON rows of integers or strings `p/q`: `[[2, 1], [1, 2]]`."),
    ],
    name: Annotated[str, Parameter(help="Name as plain text.")],
    latex: Annotated[str, Parameter(help="Name as TeX, without math delimiters.")],
    alias: Aliases = (),
    family: Families = (),
    reference: Annotated[
        tuple[str, ...],
        Parameter(help="A bibliographic citation as plain text; repeat for each one."),
    ] = (),
    prose: Annotated[str, Parameter(help="The notes of the record, in Pandoc Markdown.")] = "",
    root: Root = Path(),
) -> None:
    """Write a lattice card from authored fields, without computation or verification.

    Refuses a Gram tensor that a card of the corpus already states: the
    corpus records a lattice once, so a second card with the same tensor is
    never written.
    """
    try:
        parsed = records.gram_tensor(json.loads(gram))
    except AssertionError as error:
        print(f"--gram: {error}", file=sys.stderr)
        sys.exit(1)
    key = corpus.gram_key(parsed)
    index = corpus.gram_index(root)
    if index.get(key):
        print(
            f"gram_tensor: the corpus already holds this tensor at {' '.join(index[key])}",
            file=sys.stderr,
        )
        sys.exit(1)
    declared: dict[str, Yaml] = {
        "name": name,
        "latex": latex,
        "aliases": list(alias),
        "gram_tensor": json.loads(gram),
        "families": list(family),
        "related": [],
        "references": [{"citation": citation} for citation in reference],
    }
    path = _author(root, declared, prose)
    corpus.append_index(root, path.stem, parsed)
    print(path)


@app.command(name="populate-standard-sums")
def populate_standard_sums(
    root: Root = Path(),
    max_rank: Annotated[int, Parameter(help="Largest rank of an authored construction (default: 10).")] = 10,
    max_content: Annotated[int, Parameter(help="Largest absolute form content after scaling (default: 2).")] = 2,
) -> None:
    """Author Gram presentations of all canonical sums of known untwisted indecomposables and their small twists."""
    from dzack_research.preamble.categories.lattices import Lattices
    from dzack_research.preamble.rings import session_ring_objects

    from latticedb import construction_corpus

    category = Lattices(session_ring_objects()["ZZ"])
    seeds = category.Untwisted().Indecomposable().known_objects(max_rank=max_rank)
    result = construction_corpus.populate_standard_sums(
        root, seeds, max_rank=max_rank, max_content=max_content
    )
    print(f"{result.new_cards} cards authored; {result.existing_cards} presentations already held")


@app.command(name="populate-construction-prefix")
def populate_construction_prefix(
    root: Root = Path(),
    max_expressions: Annotated[int, Parameter(help="Number of expressions to take from the unbounded preamble iterator.")] = 100,
    max_rank: Annotated[int, Parameter(help="Largest rank to store.")] = 10,
    max_content: Annotated[int, Parameter(help="Largest absolute form content to store.")] = 2,
) -> None:
    """Store a prefix of known lattice constructions, including tensors and gluings."""
    from dzack_research.preamble.categories.lattices import Lattices
    from dzack_research.preamble.rings import session_ring_objects

    from latticedb import construction_corpus

    category = Lattices(session_ring_objects()["ZZ"])
    seeds = category.Untwisted().Indecomposable().known_objects(max_rank=max_rank)
    result = construction_corpus.populate_construction_prefix(
        root, seeds, max_expressions=max_expressions, max_rank=max_rank, max_content=max_content
    )
    print(f"{result.new_cards} cards authored; {result.existing_cards} presentations already held")


@app.command(name="populate-standard-products")
def populate_standard_products(
    root: Root = Path(),
    max_rank: Annotated[int, Parameter(help="Largest rank to store.")] = 10,
    max_content: Annotated[int, Parameter(help="Largest absolute form content to store.")] = 2,
    max_inclusions_per_source: Annotated[int | None, Parameter(help="Optional count of gluing inclusions to visit per source.")] = None,
) -> None:
    """Author tensor products of all known small twists and their proper overlattices."""
    from dzack_research.preamble.categories.lattices import Lattices
    from dzack_research.preamble.rings import session_ring_objects

    from latticedb import construction_corpus

    category = Lattices(session_ring_objects()["ZZ"])
    seeds = category.Untwisted().Indecomposable().known_objects(max_rank=max_rank)
    result = construction_corpus.populate_standard_products(
        root, seeds, max_rank=max_rank, max_content=max_content,
        max_inclusions_per_source=max_inclusions_per_source,
    )
    print(f"{result.new_cards} cards authored; {result.existing_cards} presentations already held")


@app.command(name="populate-overlattices")
def populate_overlattices(
    root: Root = Path(),
    start_tag: Annotated[str, Parameter(help="First source-card tag to visit.")] = "0000",
    end_tag: Annotated[str | None, Parameter(help="Last source-card tag to visit, inclusive.")] = None,
    max_rank: Annotated[int, Parameter(help="Largest rank to store.")] = 10,
    max_content: Annotated[int, Parameter(help="Largest absolute form content to store.")] = 2,
    max_sources: Annotated[int | None, Parameter(help="Optional count of source cards to visit, in rank and tag order.")] = None,
    max_inclusions_per_source: Annotated[int | None, Parameter(help="Optional count of inclusions to visit per source.")] = None,
) -> None:
    """Author proper integral overlattices of selected existing cards."""
    from latticedb import construction_corpus

    radix = len(corpus.TAG_ALPHABET)
    start = int(start_tag, radix)
    end = None if end_tag is None else int(end_tag, radix)
    tags = (
        path.stem for path in (root / "lattices").glob("*.md")
        if int(path.stem, radix) >= start
        and (end is None or int(path.stem, radix) <= end)
    )
    result = construction_corpus.populate_overlattices_of_cards(
        root, tags, max_rank=max_rank, max_content=max_content,
        max_sources=max_sources, max_inclusions_per_source=max_inclusions_per_source,
    )
    print(f"{result.new_cards} cards authored; {result.existing_cards} presentations already held")


@app.command(name="merge-keyed-map")
def merge_keyed_map(base: Path, ours: Path, theirs: Path) -> None:
    """Git merge driver for the files of `certificates/` and `exceeded.yaml`: merge them key by key into OURS."""
    keyed_merge.merge_files(base, ours, theirs)


@app.command(name="bulk-source-fetch")
def bulk_source_fetch(root: Root = Path()) -> None:
    """Store the published Nipp, Brandt–Intrau, and Watson bulk source tables."""
    for path in bulk_sources.fetch(root):
        print(f"sources/{path}")


@app.command(name="bulk-index")
def bulk_index_write(root: Root = Path()) -> None:
    """Store parsed bulk source rows without deriving mathematical invariants."""
    for source, count in bulk_index.write(root).items():
        print(f"sources/normalized/{source}.jsonl.gz: {count} rows")


@app.command(name="seed")
def seed_cards(*, limit: int | None = None, root: Root = Path()) -> None:
    """Write permanent lattice cards from stored source rows without verification or enrichment."""
    seeded, attached, without_gram = seed.run(root, limit)
    print(f"{seeded} lattice cards written; {attached} source rows joined the card that states their Gram tensor; {len(without_gram)} source rows need a defining Gram tensor")


@app.command(name="regular-ternaries")
def regular_ternaries_seed(root: Root = Path()) -> None:
    """Write a card for each form of the stored regular and spinor regular ternary tables, its value certified by the table's citation.

    A form whose exact Gram tensor a card already states gets the value and the
    citation on that card, so the corpus still records each tensor once.
    """
    index = corpus.gram_index(root)
    held = certificates.load(root)
    written = 0
    for entry in regular_ternaries.entries():
        gram = TypeAdapter(GramTensor).validate_python(entry.gram_tensor)
        key = corpus.gram_key(gram)
        if key not in index:
            path = _author(root, *regular_ternaries.record(entry))
            corpus.append_index(root, path.stem, gram)
            index[key] = [path.stem]
            written += 1
        for tag in index[key]:
            for field, reference in entry.certified.items():
                genus.cite(root / "lattices" / f"{tag}.md", field, entry.proved, reference, held)
    certificates.save(root, held)
    print(f"{written} lattice cards written; {len(regular_ternaries.entries())} table rows certified by citation")


@app.command
def morphism(
    source: Annotated[str, Parameter(help="Tag of the source lattice.")],
    target: Annotated[str, Parameter(help="Tag of the target lattice.")],
    *,
    name: Annotated[str, Parameter(help="Name as plain text; TeX between `$` signs is rendered.")],
    matrix: Annotated[
        str,
        Parameter(help="JSON rows of integers, rank(target) rows by rank(source) columns: column j is the image of e_j."),
    ],
    description: Annotated[str | None, Parameter(help="One or two sentences on the morphism.")] = None,
    scale: Annotated[
        int | None,
        Parameter(help="The integer c with b_T(phi x, phi y) = c b_S(x, y): a morphism S(c) -> T."),
    ] = None,
    row_subdivisions: Annotated[
        str,
        Parameter(help="JSON list of the lines between rows, as SageMath's `M.subdivisions()[0]`."),
    ] = "[]",
    column_subdivisions: Annotated[
        str,
        Parameter(help="JSON list of the lines between columns, as SageMath's `M.subdivisions()[1]`."),
    ] = "[]",
    root: Root = Path(),
) -> None:
    """Author a morphism on the source lattice card."""
    path = root / "lattices" / f"{source}.md"
    document = corpus.read_card(path)
    added: dict[str, Yaml] = {
        "target": target,
        "name": name,
        "matrix": json.loads(matrix),
        "row_subdivisions": json.loads(row_subdivisions),
        "column_subdivisions": json.loads(column_subdivisions),
    }
    if description is not None:
        added["description"] = description
    if scale is not None:
        added["scale"] = scale
    metadata = corpus.front_matter(document)
    existing = TypeAdapter(list[dict[str, Yaml]]).validate_python(metadata.get("morphisms", []))
    metadata["morphisms"] = [*existing, added]
    path.write_text(records.record_text(metadata, document.content))
    print(path)


@app.command
def verify(root: Root = Path()) -> None:
    """Report stored-card inconsistencies without changing cards; mathematics is delegated to the preamble."""
    try:
        count, problems = checks.run(root)
    except corpus.CorpusInvalid as invalid:
        print("\n".join(invalid.problems), file=sys.stderr)
        print(f"{len(invalid.problems)} problems", file=sys.stderr)
        sys.exit(1)
    _refuse(problems)
    print(f"{count} lattice cards structurally verified")


@app.command
def duplicates(root: Root = Path()) -> None:
    """List the tags that share a Gram tensor, without changing lattice cards."""
    index = corpus.gram_index(root)
    found = {gram: tags for gram, tags in index.items() if len(tags) > 1}
    for tags in found.values():
        print(f"{' '.join(tags)}")
    if found:
        print(
            f"{sum(len(tags) for tags in found.values())} cards share a Gram tensor",
            file=sys.stderr,
        )
        sys.exit(1)
    print(f"{sum(len(tags) for tags in index.values())} lattice cards have distinct Gram tensors")


@app.command
def deduplicate(root: Root = Path()) -> None:
    """Merge every card into the earliest card that states its Gram tensor, and retire its tag.

    The merged card's references, families, related lattices and prose join the
    earliest card, whose stated values they must agree with. Its certificates
    leave `certificates/`: a value it certified is already on the earliest
    card under that card's own certificate.
    """
    loaded = corpus.load(root)
    held = certificates.load(root)
    retired: corpus.Retired = {}
    for tags in corpus.duplicate_grams(loaded.entries).values():
        earliest, *later = sorted(tags)
        survivor = root / "lattices" / f"{earliest}.md"
        kept = corpus.front_matter(corpus.read_card(survivor))
        for tag in later:
            path = root / "lattices" / f"{tag}.md"
            document = corpus.read_card(path)
            fields = corpus.front_matter(document)
            cited = fields.get("certifications")
            for certified in cited if isinstance(cited, dict) else {}:
                block, _, field = certified.partition(".")
                stated = kept.get(block)
                assert certified == "derive" or (isinstance(stated, dict) and stated.get(field) is not None), (
                    f"{tag}: {certified} is certified and {earliest} does not state it"
                )
            seed.attach(survivor, fields, document.content.strip())
            path.unlink()
            for name in [name for name in held if name.startswith(f"{tag} ")]:
                del held[name]
            retired[tag] = f"{fields['name']}; its Gram tensor is stated by lattice card {earliest}"
    certificates.save(root, held)
    with (root / corpus.RETIRED_FILE).open("a") as output:
        output.write(yaml.safe_dump(retired, sort_keys=False, allow_unicode=True, width=100000) if retired else "")
    corpus.gram_index(root)
    print(f"{len(retired)} cards merged into the earliest card that states their Gram tensor")


@app.command
def enrich(
    *,
    tag: Annotated[
        tuple[str, ...],
        Parameter(help="Tag of a card to compute; repeat for each one. All cards when absent."),
    ] = (),
    root: Root = Path(),
) -> None:
    """Compute ordinary derived card fields without certifying them."""
    loaded = corpus.load(root)
    selected = set(tag)
    for entry in loaded.entries:
        lattice = entry.lattice
        if lattice.gram_tensor is None or (selected and lattice.tag not in selected):
            continue
        text = entry.path.read_text()
        document = frontmatter.loads(text)
        metadata = corpus.front_matter(document)
        derived = records.derive(metadata)
        updated = records.record_text(derived, document.content)
        if updated != text:
            entry.path.write_text(updated)
            print(f"{entry.path}: derived values written")


@app.command
def enrich_summand_maps(*, root: Root = Path()) -> None:
    """Write preamble-computed orthogonal summand maps over the corpus."""
    _refuse(summands.store(root, corpus.load(root)))


@app.command
def certification_failures(root: Root = Path()) -> None:
    """Show the durable triage ledger, including error evidence and retry history."""
    print(json.dumps({key: value.model_dump(mode="json") for key, value in failures.load(root).items()}, indent=2))


@app.command
def retry_computation(tag: str, computation: str, *, note: str, root: Root = Path()) -> None:
    """Release one failed computation after recording its repair or triage decision."""
    failures.retry(root, f"{tag} {computation}", note)


@app.command
def certify(
    *,
    tag: Annotated[
        tuple[str, ...],
        Parameter(help="Tag of a card to certify; repeat for each one. All cards when absent."),
    ] = (),
    minutes: Annotated[
        int,
        Parameter(help="Minutes until the job's timeout ends this run; a computation still running then stays in `exceeded.yaml`."),
    ],
    workers: Annotated[
        int,
        Parameter(help="Sage processes computing at once; a search that never returns holds only one. Defaults to the CPU count."),
    ] = os.cpu_count() or 1,
    shard: Annotated[
        str,
        Parameter(help="`i/n`: certify only the cards whose tag falls in shard `i` of `n`, so `n` jobs share the corpus."),
    ] = "0/1",
    root: Root = Path(),
) -> None:
    """Compute uncertified card values, replace disagreements, and certify the computed results."""
    deadline = time.time() + 60 * minutes
    index, count = (int(part) for part in shard.split("/"))
    if not 0 <= index < count:
        raise ValueError(f"shard {shard} names no shard of {count}")
    loaded = corpus.load(root)
    held = certificates.load(root)
    genus.certify(root, loaded, held, tag, deadline, workers, (index, count))


@app.command
def build(
    root: Root = Path(),
    target: Annotated[Path, Parameter(help="Directory for the site. The command replaces it.")] = Path("_site"),
) -> None:
    """Build the site from the corpus."""
    count = site.build(root, target)
    print(f"{count} lattices -> {target}")


@app.command
def deploy(root: Root = Path()) -> None:
    """Build the site, link it into the directory that nginx serves, and check that nginx serves it."""
    target = (root / "_site").resolve()
    site.build(root, target)
    if not SERVED.is_symlink():
        SERVED.symlink_to(target)
    assert SERVED.resolve() == target, f"{SERVED} links to {SERVED.resolve()}, not to {target}"
    with urlopen(Request(ADDRESS, headers={"Host": HOST})) as response:
        assert response.status == 200, f"{ADDRESS} with host {HOST} returned {response.status}"
    print(f"http://{HOST}/")


@app.command
def next_tag(root: Root = Path()) -> None:
    """Print the tag for the next new record."""
    print(corpus.next_tag(root))


def main() -> None:
    """Run the CLI, unwinding workers and persistence on CI termination."""

    def terminate(signum: int, frame: FrameType | None) -> None:
        raise SystemExit(128 + signum)

    signal.signal(signal.SIGTERM, terminate)
    app()
