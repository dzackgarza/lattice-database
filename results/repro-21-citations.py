"""The #21 reproduction: each reported card value hashes to its shard entry, and the card cites nothing.

`checks.records.problems` cannot be imported where the preamble image is absent: `latticedb.records`
and `latticedb.corpus` import `sage_extensions` at module level, and this checkout's environment has
no `sage_extensions` installation. This script therefore runs the verifier's own deciding calls —
`certificates.certification_hash`, `genus.certified_value` and `certificates.is_certified` — on the
real cards and the real certificate shard, which is the whole of the per-field decision that
`checks.records.problems` makes:

    certificate = held.get(computation)
    expected_hash = certificates.certification_hash(computation, entry.lattice,
                        genus.certified_value(field, value, entry.lattice))
    if (cited.get(local_name) is not None or (certificate is not None and certificate.hash is not None))
        and not certificates.is_certified(held, computation, cited.get(local_name), expected_hash):
        found.append(f"{entry.path}: {block_name}.{field} contradicts its completed computation certificate")

Run it in the certification image (`.github/actions/sage/action.yml`): no database module here, so the
script is preamble-free and needs only pydantic, pyyaml and python-frontmatter.

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \\
      /sage/.venv/bin/python results/repro-21-citations.py
"""

import sys
from pathlib import Path

import frontmatter
import yaml
from pydantic import TypeAdapter

from latticedb import certificates
from latticedb.model import Lattice, Yaml

REPOSITORY = Path(__file__).resolve().parent.parent

# The fields `results/evidence-20-certificate-contradictions.md` classifies as `uncited`.
REPORTED: dict[str, tuple[str, ...]] = {
    "0021": ("root_span.norms", "root_span.roots"),
    "0024": ("hyperbolic.reflective", "root_span.norms", "root_span.roots"),
    "0026": ("hyperbolic.reflective", "root_span.norms", "root_span.roots"),
    "0268": ("hyperbolic.reflective", "root_span.norms", "root_span.roots"),
}
"""Each card of the report, and the block-qualified fields whose reference it lacks."""


def certified_value(field: str, value: Yaml) -> Yaml:
    """`genus.certified_value` for these fields: it commits to the stored value itself.

    `genus.certified_value` rewrites only `automorphism_group_generator_morphisms` (to the named
    morphisms' matrices) and the two orbit-series fields (to their projection); for every other
    field it returns the stored value unchanged.
    """
    assert field not in {"automorphism_group_generator_morphisms", "primitive_orbits", "discriminant_orbits"}
    return value


def front_matter(path: Path) -> dict[str, Yaml]:
    return TypeAdapter(dict[str, Yaml]).validate_python(frontmatter.load(str(path), encoding="utf-8").metadata)


def main() -> int:
    held = certificates.load(REPOSITORY)
    print(f"certificates.load: {len(held)} completed computations", file=sys.stderr)
    contradictions = 0
    for tag, fields in REPORTED.items():
        path = REPOSITORY / "lattices" / f"{tag}.md"
        metadata = front_matter(path)
        lattice = Lattice.model_validate(metadata)
        print(f"{tag}: certificate shard certificates/{certificates.group(tag)}.yaml")
        for qualified in fields:
            block_name, field = qualified.split(".", 1)
            block = metadata.get(block_name)
            value = block.get(field) if isinstance(block, dict) else None
            computation = f"{tag} {block_name}.{field}"
            certificate = held.get(computation)
            expected = certificates.certification_hash(computation, lattice, certified_value(field, value))
            cited = lattice.certifications.get(qualified)
            decided = (cited is not None or (certificate is not None and certificate.hash is not None)) and not certificates.is_certified(
                held, computation, cited, expected
            )
            contradictions += decided
            print(
                f"  {qualified}\n"
                f"    stored value   {yaml.safe_dump(value, default_flow_style=True, width=10_000).strip()}\n"
                f"    shard hash     {certificate.hash if certificate else 'absent'}\n"
                f"    hash of value  {expected}  {'== shard' if certificate and certificate.hash == expected else '!= shard'}\n"
                f"    card cites     {cited or 'nothing'}\n"
                f"    is_certified   {certificates.is_certified(held, computation, cited, expected)}\n"
                f"    contradiction  {decided}"
            )
    print(f"\n{contradictions} contradictions of {sum(len(fields) for fields in REPORTED.values())} reported fields")
    return 1 if contradictions == 0 else 0


if __name__ == "__main__":
    sys.exit(main())
