"""The shipped cards' certificate references, checked by the verifier that reports them (#21).

A card cites the certificate of every computation it stores, and `certificates/` holds that hash:
`checks.records.problems` compares each stored value's projection with the shard's entry and reports
a card that states a value the ledger disagrees with. `latticedb verify` runs exactly that check over
every card, one shard per process (the `verify` workflow, #6); this file runs it over the cards the
certificate-contradiction report names, against their own shards, so the suite that a dispatched
`tests` run carries reports a card that loses a reference (#5).

The cards are the reported four: 0268 is #21's own case, and the report adds 0021, 0024 and 0026.
"""

from pathlib import Path

from latticedb import certificates, checks, corpus
from latticedb.model import Lattice

REPOSITORY = Path(__file__).resolve().parent.parent

REPORTED = ("0021", "0024", "0026", "0268")
"""The cards whose computed values had a certificate in their shard and no reference on the card."""

CONTRADICTION = "contradicts its completed computation certificate"


def entry(tag: str) -> corpus.Entry:
    """The stored card, as every workflow reads it."""
    path = REPOSITORY / "lattices" / f"{tag}.md"
    document = corpus.read_card(path)
    return corpus.Entry(Lattice.model_validate(corpus.front_matter(document)), document.content, path)


def these_cards() -> corpus.Corpus:
    """A corpus of the reported cards: the check reads the whole corpus, and only these are asked for."""
    return corpus.Corpus(
        entries=tuple(entry(tag) for tag in REPORTED),
        families={},
        retired={},
        geometric=(),
        geometric_families=(),
        graphs=(),
        genera=(),
        polytopes=(),
        toric_varieties=(),
        geometric_maps=(),
        local_systems=(),
        operators=(),
        moduli_problems=(),
        lattice_families=(),
        lie_groups=(),
        arithmetic_groups=(),
    )


def test_the_reported_cards_cite_the_certificates_their_shards_hold() -> None:
    """Each stored value hashes to the certificate its shard holds, and the card cites that hash."""
    loaded = these_cards()
    held = certificates.load(REPOSITORY)
    problems = checks.records.problems(loaded, held, frozenset(REPORTED))
    contradictions = [problem for problem in problems if CONTRADICTION in problem]
    assert contradictions == [], "\n".join(problems)


def test_the_cards_state_the_fields_the_report_names() -> None:
    """The check above is not vacuous: each card states the fields, and its shard certifies them."""
    held = certificates.load(REPOSITORY)
    stated = {
        "0021": ("root_span.roots", "root_span.norms"),
        "0024": ("hyperbolic.reflective", "root_span.roots", "root_span.norms"),
        "0026": ("hyperbolic.reflective", "root_span.roots", "root_span.norms"),
        "0268": ("hyperbolic.reflective", "root_span.roots", "root_span.norms"),
    }
    for tag, fields in stated.items():
        lattice = entry(tag).lattice
        metadata = corpus.front_matter(corpus.read_card(REPOSITORY / "lattices" / f"{tag}.md"))
        for qualified in fields:
            block_name = qualified.split(".", 1)[0]
            block = metadata.get(block_name)
            assert isinstance(block, dict) and block.get(qualified.split(".", 1)[1]) is not None, f"{tag} {qualified} is not stated"
            assert held.get(f"{tag} {qualified}") is not None, f"{tag} {qualified} has no certificate"
            assert lattice.certifications.get(qualified) is not None, f"{tag} {qualified} is not cited"
