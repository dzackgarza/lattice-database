"""Compute `integral.discriminant_form` on a card through the field owner, and certify it (#12).

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \\
      /sage/.venv/bin/python results/compute-discriminant-forms.py 6JRX 6JRY [029J 6JRR ...]

The value is $O(A_L, q_L)$, its isotropic elements and the number of its orbits on them, and the owner
computes it: `discriminant_quadratic_form()`, `orthogonal_group().order()`, `isotropic_elements()` and
`orbits()`, as `sage_genus._discriminant_form` asks it.

Only that field is requested. `latticedb certify` selects every field a card lacks, and on these
cards that meant the integral invariants too: the four-card run in this checkout died with
"memory exhausted" on 029J, 6JRR, 6JRX and 6JRY before writing anything, so selecting the field
explicitly is what lets the finite discriminant computation finish.

The request and the declaration of the computed value are the worker's own: `sage_genus._compute`
is what `certify` starts in a subprocess, and the certificate is then made exactly as
`genus.certify` makes it -- `genus.store` for the value, `certificates.certification_hash` over the
stored value and Gram tensor for the hash, and `certificates.save` for the shard.
"""
from __future__ import annotations

import contextlib
import io
import json
import sys
from pathlib import Path

import yaml

from latticedb import certificates, corpus, genus, records, sage_genus
from latticedb.certificates import Certificate
from latticedb.model import Lattice

ROOT = Path(__file__).resolve().parent.parent
FIELD = "discriminant_form"


def request_for(tag: str) -> dict:
    metadata = corpus.front_matter(corpus.read_card(ROOT / "lattices" / f"{tag}.md"))
    lattice = Lattice.model_validate(metadata)
    gram = [[int(value) if value.denominator == 1 else str(value) for value in row] for row in lattice.gram_tensor]
    return {"tag": tag, "gram": gram, "integral": lattice.integral is not None,
            "fields": [FIELD], "series_bound": genus.series_bound(len(gram))}


def computed(request: dict) -> dict:
    """The worker's own answer for this request: `sage_genus._compute` emits it as JSON."""
    emitted = io.StringIO()
    with contextlib.redirect_stdout(emitted):
        sage_genus._compute(dict(request))
    for line in emitted.getvalue().splitlines():
        data = json.loads(line)
        if data.get("tag") == request["tag"] and FIELD in data:
            return data
    raise RuntimeError(f"{request['tag']}: the worker emitted no {FIELD}: {emitted.getvalue()!r}")


def main(tags: list[str]) -> int:
    held = certificates.load(ROOT)
    for tag in tags:
        path = ROOT / "lattices" / f"{tag}.md"
        values = computed(request_for(tag))
        genus.store(path, {FIELD: values[FIELD]})
        stored = corpus.front_matter(corpus.read_card(path))
        lattice = Lattice.model_validate(stored)
        block_name, _ = genus.stored_in(FIELD, lattice.definiteness)
        block = stored[block_name]
        computation = genus.name(tag, FIELD, lattice.definiteness)
        certificate_hash = certificates.certification_hash(
            computation, lattice, genus.certified_value(FIELD, block[FIELD], lattice)
        )
        certifications = dict(lattice.certifications)
        certifications[f"{block_name}.{FIELD}"] = certificate_hash
        stored["certifications"] = certifications
        document = corpus.read_card(path)
        path.write_text(records.record_text(stored, document.content))
        held[computation] = Certificate(hash=certificate_hash, by=str(values["by"]))
        certificates.save(ROOT, held, tags={tag})
        print(f"{tag}: {block[FIELD]}  certificate {certificate_hash[:16]}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
