"""Certificate-consistency checks for stored lattice cards."""

from __future__ import annotations

import frontmatter

from latticedb import certificates, corpus, genus, records
from latticedb.certificates import Certificates
from latticedb.corpus import Corpus


def shared_gram_problems(loaded: Corpus) -> list[str]:
    """One problem per Gram tensor stated by more than one card.

    A Gram tensor determines its lattice, so two cards stating one tensor
    record one lattice twice.
    """
    return [f"cards {', '.join(tags)} state one Gram tensor; a lattice has one card" for tags in corpus.duplicate_grams(loaded.entries).values()]


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
    return found
