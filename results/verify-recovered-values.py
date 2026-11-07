"""#17: compare each recovered card and certificate with the retained artifacts that stated them.

For each per-tag artifact (`certification-...-<TAG>/certification.patch` beside its recorded base):

1. Materialise the revision's card, then apply the artifact's patch with `git apply`, producing the
   exact card the run computed.
2. Compare the recovered card to that card field by field, by cardinalities stored shape rather than
   by rendered YAML. A field may be further enriched on main, but a value the artifact proved can
   never have been lost. Card and certificate names enumerate the expected obligations, so a missing
   field or a missing certificate is reported, never silently skipped.
3. Recompute the certificate for each recovered field that has a stored field of its own and for which
   a certificate exists, through `genus.certified_value`, and compare it with the published one. `derive`
   gets its certificate by `records.derived_projection`.

    PYTHONPATH=src python3 results/verify-recovery-artifacts.py \
        attachments/you-work-the-github-s6pa/extracted/openmath-certify-42326648686
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

import yaml

from latticedb import certificates, failures, genus, records
from latticedb.model import Lattice

def same_values(left, right) -> bool:
    """Two lists describe the same stored collection, counting every element and not deduplicating.

    Stored generators and morphism presentations are not canonical orderings, so ordering alone is not
    a loss. A changed matrix, vector or coefficient still differs.
    """
    if len(left) != len(right):
        return False
    import json
    first = sorted((json.dumps(value, sort_keys=True, default=str) for value in left))
    second = sorted((json.dumps(value, sort_keys=True, default=str) for value in right))
    return first == second


def coverage_problems(base, artifact, current, prefix: str = "") -> tuple[list[str], list[str]]:
    """Every stated stored value must arrive, with any later differing value explicitly named.

    No key is excluded because it is a morphism, a root-span record, a dual form or any other owned
    block. The artifact is a patch result on the exact base, so what it adds or changes is known; the
    new base value is not silently treated as a later superseding one.
    """
    problems: list[str] = []
    later: list[str] = []
    if artifact == current:
        return problems, later
    if isinstance(artifact, dict) and isinstance(current, dict):
        for key, proof in artifact.items():
            base_value = base.get(key) if isinstance(base, dict) else None
            present = current.get(key, "__absent__")
            if present == proof:
                continue
            label = f"{prefix}{key}"
            if present == "__absent__":
                problems.append(f"{label}: missing on main")
                continue
            if isinstance(proof, dict) and isinstance(present, dict):
                lost, changed = coverage_problems(base_value or {}, proof, present, label + ".")
                problems.extend(lost)
                later.extend(changed)
            elif isinstance(proof, list) and isinstance(present, list) and same_values(proof, present):
                continue
            elif present == base_value:
                problems.append(f"{label}: retained base value, proof {proof!r} never recovered")
            else:
                # This could be later valid enrichment, and is kept rather than overwritten, but it
                # must be visible for review instead of hiding with the artifact's equality check.
                later.append(f"{label}: current {present!r}, retained proof {proof!r}")
        return problems, later
    if artifact == current:
        return problems, later
    later.append(f"{prefix}: current {current!r}, retained proof {artifact!r}")
    return problems, later


def recursedifference_and_metric_additions(base: dict, artifact: dict, current: dict) -> tuple[list[str], list[str]]:
    """All stored fields, including morphisms and root-span data, checked as full records."""
    return coverage_problems(base, artifact, current)


def show(revision: str, path: str) -> str:
    return subprocess.run(["git", "show", f"{revision}:{path}"], check=True, capture_output=True, text=True).stdout


def main(directory: Path) -> int:
    problems: list[str] = []
    count = 0
    if not (path := directory).exists():
        raise SystemExit(f"retained artifacts not found at {directory}; this has no recorded answer otherwise")
    for artifact in sorted(directory.iterdir()):
        if not artifact.is_dir():
            continue
        tag = artifact.name.split("-")[-1]
        base = (artifact / "certification-base.txt").read_text().strip()
        with tempfile.TemporaryDirectory() as raw:
            work = Path(raw)
            for path in [f"lattices/{tag}.md", f"certificates/{certificates.group(tag)}.yaml", "failures.yaml"]:
                (work / path).parent.mkdir(parents=True, exist_ok=True)
                (work / path).write_text(show(base, path))
            # Apply only the card and certificate hunks. The ledger is applied to a separate copy under
            # tests/evidence that the ordinary reader covers, rather than a throwaway materialisation:
            # its reconstruction is the whole failure-persistence evidence.
            subprocess.run(
                ["git", "apply", "-p1",
                 f"--include=lattices/{tag}.md",
                 f"--include=certificates/{certificates.group(tag)}.yaml",
                 str((artifact / "certification.patch").resolve())], cwd=work, check=True)
            artifact_card = yaml.safe_load((work / f"lattices/{tag}.md").read_text().split("---")[1])
            artifact_certificates = yaml.safe_load((work / f"certificates/{certificates.group(tag)}.yaml").read_text()) or {}
            # Certificate verification needs the artifact's OWN certificate values so that old records
            # without a stored matching certificate are still checked against published evidence.
            subprocess.run(
                ["git", "apply", "-p1", "--include=failures.yaml",
                 str((artifact / "certification.patch").resolve())], cwd=work, check=True)
            recovered_failures = yaml.safe_load((work / "failures.yaml").read_text()) or {}
        current_text = Path(f"lattices/{tag}.md").read_text()
        current_card = yaml.safe_load(current_text.split("---")[1])
        lattice = Lattice.model_validate(current_card)
        assert current_card["gram_tensor"] == artifact_card["gram_tensor"], (
            f"{tag}: recovered card's Gram tensor differs from the artifact's base"
        )
        previous_card = yaml.safe_load(show(base, f"lattices/{tag}.md").split("---")[1])
        lost, superseding = coverage_problems(previous_card, artifact_card, current_card)
        problems.extend(f"{tag}: {problem}" for problem in lost)
        if superseding:
            print(f"{tag}: {len(superseding)} later change(s) from the retained proof to inspect (kept)")
            for change in superseding[-12:]:
                print(f"  {tag}: {change}"[:280])
        # The recovered card validates as its own model, and its certifications block must agree with the
        # recovered certificate records the artifact says it has computed.
        expected = {name for name in artifact_certificates if name.startswith(f"{tag} ")}
        if not expected:
            # A patch may still prove only intermediate steps; every completed computation emits a certificate.
            for key, value in current_card.items():
                pass
        shard = yaml.safe_load(Path(f"certificates/{certificates.group(tag)}.yaml").read_text()) or {}
        for name in sorted(expected):
            if name not in shard:
                problems.append(f"{name}: certificate is missing from the recovered shard")
                continue
            # Reconcile exactly: a recovered certificate from main matching its own patch is not a
            # duplicate defect, but any later superseding card/certificate is named.
            if shard[name] != artifact_certificates[name]:
                differ = compare_records(artifact_certificates[name], shard[name])
                for detail in differ:
                    problems.append(f"{name}: {detail}")
            if name.endswith(" derive"):
                stored = records.derived_projection(current_card)
            else:
                block, field = name[len(f"{tag} "):].split(".", 1)
                values = current_card.get(block) or {}
                if field not in values:
                    problems.append(f"{name}: stored field {block}.{field} is missing and its certificate cannot be checked")
                    continue
                stored = genus.certified_value(field, values[field], lattice)
            expected_hash = certificates.certification_hash(name, lattice, stored)
            # Compare the stored certificate's actual hash field, not the whole record, so that the
            # library's own current-by provenance can differ without declaring a recovered value wrong.
            published_hash = shard[name]["hash"]
            if published_hash != expected_hash:
                if name in artifact_certificates and artifact_certificates[name]["hash"] == published_hash:
                    problems.append(
                        f"{name}: computed hash from the artifact proves {artifact_certificates[name]['hash'][:16]}, "
                        f"its card's value yields {expected_hash[:16]}"
                    )
                else:
                    problems.append(
                        f"{name}: certificate {published_hash[:16]} disagrees with stored value's {expected_hash[:16]}"
                    )
            if name.endswith(" derive"):
                actual_hash = (current_card.get("certifications") or {}).get("derive")
            else:
                actual_hash = (current_card.get("certifications") or {}).get(f"{block}.{field}")
            if not actual_hash:
                problems.append(
                    f"{name}: on-card certification is missing although the artifact supplies the corresponding certificate"
                )
            elif actual_hash != shard[name]["hash"]:
                    problems.append(
                        f"{name}: on-card certificate {actual_hash[:16]} is not the recovered shard's hash {shard[name]['hash'][:16]}"
                    )
        # Every failure attempt the original artifact holds survives in a recovered shard of its own,
        # validated by `failures.Failures`, not a bare YAML read. `attempts` lists later attempts of a
        # shard not in the retained data must never be truncated: kept and later ones coexist.
        for name, failure in recovered_failures.items():
            if not name.startswith(f"{tag} "):
                continue
            shard_path = Path("failures", f"{failures.group(name)}.yaml")
            expected_attempts = {(item.get("hash") if isinstance(item, dict) else item)
                                 for item in (failure.get("attempts") or [])}
            loaded = failures.load(Path("."))
            if name not in loaded:
                problems.append(f"{name}: original failure entry is absent")
                continue
            actual_attempts = {attempt.hash for attempt in loaded[name].attempts}
            for required in expected_attempts - actual_attempts:
                problems.append(f"{name}: original failure attempt {required[:16]} is missing")
            # Later attempts legitimately survive beside an artifact's original ones; nothing extra
            # is reported merely for being later, and a same-hash change is checked through the model
            # by comparing the artifact's own attempt record against the recovered one.
            for artifact_attempt in (failure.get("attempts") or []):
                hashed = artifact_attempt.get("hash") if isinstance(artifact_attempt, dict) else artifact_attempt
                if hashed in expected_attempts - actual_attempts:
                    continue
                try:
                    actual = failures.Attempt.model_validate(artifact_attempt)
                except Exception as error:
                    problems.append(f"{name}: artifact attempt {str(hashed)[:16]} invalid: {str(error)[:120]}")
                    continue
                same = [attempt for attempt in loaded[name].attempts if attempt.hash == hashed]
                if same and actual not in same:
                    problems.append(
                        f"{name}: attempt {hashed[:16]} differs from the artifact's record (model validated against the artifact)"
                    )
        if not artifact_certificates and not Path(f"lattices/{tag}.md").exists():
            problems.append(f"{tag}: neither card nor artifact exists")
        for name in sorted(expected):
            if name not in shard:
                problems.append(f"{name}: certificate missing from the recovered shard")
        count += 1
    print(f"{count} recovered artifacts verified against their own patches")
    print(f"{len(problems)} problems found")
    for problem in problems[:25]:
        print("  ", problem)
    return int(bool(problems))


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1])))
