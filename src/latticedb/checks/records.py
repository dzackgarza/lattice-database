"""Certificate-consistency checks for stored lattice cards."""

from __future__ import annotations

from pathlib import Path

import frontmatter

from latticedb import certificates, corpus, genus, records
from latticedb.certificates import Certificates
from latticedb.corpus import Corpus


def duplicate_gram_messages(index: dict[str, list[str]], cards: frozenset[str] | None = None) -> list[str]:
    """One problem per group of tags stating one Gram tensor, for the groups a card of `cards` belongs to."""
    return [
        f"cards {', '.join(sorted(tags))} state one Gram tensor; a lattice has one card"
        for tags in index.values()
        if len(tags) > 1 and (cards is None or not cards.isdisjoint(tags))
    ]


def shared_gram_problems(loaded: Corpus, cards: frozenset[str] | None = None) -> list[str]:
    """One problem per Gram tensor stated by more than one card.

    A Gram tensor determines its lattice, so two cards stating one tensor
    record one lattice twice.
    """
    index = {corpus.gram_key(entry.lattice.gram_tensor): [] for entry in loaded.entries if entry.lattice.gram_tensor is not None}
    for entry in loaded.entries:
        if entry.lattice.gram_tensor is not None:
            index[corpus.gram_key(entry.lattice.gram_tensor)].append(entry.lattice.tag)
    return duplicate_gram_messages(index, cards)


def duplicate_gram_problems(root: Path, loaded: Corpus, cards: frozenset[str] | None = None) -> list[str]:
    """One problem per Gram tensor stated by more than one card, from the durable index when it covers the corpus.

    `corpus.stored_gram_index` states every card's tensor without loading the cards and without writing, so a shard of
    `latticedb verify` keeps the corpus-wide check its narrowed read would otherwise lose (#6). `cards` selects the
    duplicates that one of the shard's own cards belongs to, so the union over the shards reports every pair once. An
    index that no longer describes the cards on disk is not read, and the duplicates of the cards at hand are reported
    instead.
    """
    index = corpus.stored_gram_index(root)
    if index is not None:
        return duplicate_gram_messages(index, cards)
    return shared_gram_problems(loaded, cards)


def problems(loaded: Corpus, held: Certificates, cards: frozenset[str] | None = None) -> list[str]:
    """The stored claims of `cards` that contradict a certificate, and their local admission problems.

    `cards` selects the records whose claims are checked: `latticedb verify` checks
    the cards of one shard per run, because the preamble keeps every structure it
    constructs for the life of the process (#6).
    """
    found: list[str] = []
    for entry in loaded.entries:
        if cards is not None and entry.lattice.tag not in cards:
            continue
        cited = entry.lattice.certifications
        if entry.lattice.gram_tensor is None:
            if cited or any(name.startswith(f"{entry.lattice.tag} ") for name in held):
                found.append(f"{entry.path}: completed certificates require a stored defining Gram tensor")
            continue
        metadata = corpus.front_matter(corpus.read_card(entry.path))
        derive_name = f"{entry.lattice.tag} derive"
        derive_hash = certificates.certification_hash(derive_name, entry.lattice, records.derived_projection(metadata))
        derive_log = held.get(derive_name)
        if (cited.get("derive") is not None or (derive_log and derive_log.hash is not None)) and not certificates.is_certified(
            held, derive_name, cited.get("derive"), derive_hash
        ):
            found.append(f"{entry.path}: Gram-derived fields contradict their completed computation certificate")
        for field in genus.BLOCKS:
            block_name = genus.stored_in(field, entry.lattice.definiteness)[0]
            computation = genus.name(entry.lattice.tag, field, entry.lattice.definiteness)
            certificate = held.get(computation)
            block = metadata.get(block_name)
            value = block.get(field) if isinstance(block, dict) else None
            local_name = f"{block_name}.{field}"
            expected_hash = certificates.certification_hash(computation, entry.lattice, genus.certified_value(field, value, entry.lattice))
            if (cited.get(local_name) is not None or (certificate is not None and certificate.hash is not None)) and not certificates.is_certified(
                held, computation, cited.get(local_name), expected_hash
            ):
                found.append(f"{entry.path}: {block_name}.{field} contradicts its completed computation certificate")
        found.extend(f"{entry.path}: {problem}" for problem in records.local_admission_problems(entry.lattice))
        found.extend(arithmetic_problems(loaded, held, entry))
    return found


def arithmetic_problems(loaded: Corpus, held: Certificates, entry: corpus.Entry) -> list[str]:
    """The arithmetic-group fields of `entry` that no completed computation establishes.

    An arithmetic-group card states its index in $O(L)$, the names of the self-isometries that
    generate it, and — where a source or a run counted them — its orbit counts; all are computed from
    this lattice card's Gram tensor, so all are certified on this card under
    `arithmetic-group.<slug>.<field>`. A group card that states a value without that certificate, or
    that cites a certificate for a value it no longer states, contradicts its ledger.

    A count a card states beside its own `data.reference` is the exception, and it is the schema's
    own: a source-stated count is certified by that citation (`genus.cite`), never by a computation,
    which is how the 87 polarisation cards state `#I_1`, `#I_2` and `#I_12` from
    Dutour Sikirić–Hulek's tables and how the two Enriques groups state theirs from Sterk.
    """
    found: list[str] = []
    cards = {card.value.slug: card.value for card in loaded.arithmetic_groups if card.value.lattice == entry.lattice.tag}
    for slug in entry.lattice.arithmetic_groups:
        card = cards.get(slug)
        if card is None:
            continue
        for short in (*genus.ARITHMETIC_FIELDS, *genus.ARITHMETIC_ORBIT_FIELDS):
            field = f"{genus.ARITHMETIC_PREFIX}{slug}.{short}"
            stored = getattr(card.data, short)
            value = list(stored) if isinstance(stored, tuple) else stored
            computation = genus.name(entry.lattice.tag, field, entry.lattice.definiteness)
            cited = entry.lattice.certifications.get(field)
            if value is None and cited is None and held.get(computation) is None:
                continue
            if short in genus.ARITHMETIC_ORBIT_FIELDS and card.data.reference is not None:
                # A count the group card's own source states is certified by that citation.
                continue
            expected = certificates.certification_hash(computation, entry.lattice, genus.certified_value(field, value, entry.lattice))
            if not certificates.is_certified(held, computation, cited, expected):
                found.append(f"{entry.path}: arithmetic group {slug}: the stated {short} is not established by a completed computation certificate")
    return found
