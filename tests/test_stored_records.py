"""The shipped cards' certificate references, checked by the verifier that reports them (#21).

A card cites the certificate of every computation it stores, and `certificates/` holds that hash:
`checks.records.problems` compares each stored value's projection with the shard's entry and reports
a card that states a value the ledger disagrees with. `latticedb verify` runs exactly that check over
every card, one shard per process (the `verify` workflow, #6); this file runs it over the cards the
certificate-contradiction report names, against their own shards, so the suite that a dispatched
`tests` run carries reports a card that loses a reference (#5).

The cards are the reported four: 0268 is #21's own case, and the report adds 0021, 0024 and 0026.
"""

import re
from pathlib import Path

from latticedb import certificates, checks, corpus, genus
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


def test_the_regular_values_a_certificate_commits_to_are_on_their_cards() -> None:
    """#43: a certificate with no value on its card is a contradiction, and the value is not a guess.

    Eight definite cards carry a completed `definite.regular` or `definite.spinor_regular` certificate and state
    neither the value nor the citation, which `latticedb verify` reports as a contradiction -- the first problem the
    gate has been able to report on this corpus (#6). The field is a `bool | "true under GRH"`, so the certificate's
    hash commits to one of three values and the value is *read out of the certificate* rather than chosen: this test
    does that reading, and states that the card says what the certificate says.
    """
    root = REPOSITORY
    tags = ("02LP", "3ICA", "02BW", "02O9", "02YE", "0353", "03UB", "04R0")
    held = certificates.load(root, tags=tags)
    candidates = (True, False, "true under GRH")
    stated = 0
    for tag in tags:
        metadata = corpus.front_matter(corpus.read_card(root / "lattices" / f"{tag}.md"))
        lattice = Lattice.model_validate(metadata)
        for short in ("regular", "spinor_regular"):
            field = f"definite.{short}"
            certificate = held.get(f"{tag} {field}")
            if certificate is None or certificate.hash is None:
                continue
            matches = [
                value
                for value in candidates
                if certificates.certification_hash(f"{tag} {field}", lattice, value) == certificate.hash
            ]
            assert len(matches) == 1, f"{tag} {field}: the certificate commits to {matches}"
            value = matches[0]
            assert (metadata.get("definite") or {}).get(short) == value, (
                f"{tag}: the certificate commits to {value!r} and the card states "
                f"{(metadata.get('definite') or {}).get(short)!r}"
            )
            assert metadata.get("certifications", {}).get(field) == certificate.hash, (
                f"{tag}: the card does not cite the certificate of {field}"
            )
            stated += 1
    assert stated == 16, stated


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


SEARCH_CERTIFICATE = re.compile(r"^([0-9A-Za-z]{4}) (\S+):\n  hash: ([0-9a-f]{64})\n", re.MULTILINE)
"""A certificate of a search: `genus.SEMI_DECISIONS` names the fields a job may stop inside."""


def search_certificates() -> dict[str, dict[str, str]]:
    """Every certificate in `certificates/` of a field a job may stop inside, by card."""
    found: dict[str, dict[str, str]] = {}
    for path in sorted((REPOSITORY / "certificates").glob("*.yaml")):
        for matched in SEARCH_CERTIFICATE.finditer(path.read_text()):
            tag, field, digest = matched.groups()
            if field.rsplit(".", 1)[-1] in genus.SEMI_DECISIONS:
                found.setdefault(tag, {})[field] = digest
    return found


def test_a_search_certificate_is_stated_by_the_card_it_names() -> None:
    """#50: a search's certificate is evidence only while the card states the result it commits to.

    A derivation rebuilds the blocks it owns from the record a job read when it queued the card, and
    a search written during that job is not in the record; before #23 the derivation's write deleted
    the value and `certificates/`, which merges key by key, kept the entry. `genus.keep_other_computations`
    stops a later derivation doing it again, and this test holds the ledger itself: every certificate
    of a field a job may stop inside names a value its card states, at that card's Gram tensor.
    """
    found = search_certificates()
    assert len(found) > 1000, f"the scan found {len(found)} cards, not the corpus's search certificates"
    problems: list[str] = []
    for tag, fields in sorted(found.items()):
        path = REPOSITORY / "lattices" / f"{tag}.md"
        if not path.is_file():
            problems.append(f"{tag}: {len(fields)} search certificates and no card")
            continue
        metadata = corpus.front_matter(corpus.read_card(path))
        lattice = Lattice.model_validate(metadata)
        for field, digest in sorted(fields.items()):
            block_name, _, short = field.partition(".")
            block = metadata.get(block_name)
            value = block.get(short) if isinstance(block, dict) else None
            if value is None:
                problems.append(f"{tag} {field}: the shard holds {digest[:12]} and the card states no value")
            elif certificates.certification_hash(f"{tag} {field}", lattice, genus.certified_value(short, value, lattice)) != digest:
                problems.append(f"{tag} {field}: the card states {value!r}, which is not the certificate's value")
            elif lattice.certifications.get(field) != digest:
                problems.append(f"{tag} {field}: the card states the value and does not cite {digest[:12]}")
    assert problems == [], "\n".join(problems)
