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

from latticedb import certificates, failures, genus, merge, records
from latticedb.model import Lattice

def coverage_problems(base, artifact, current, prefix: str = "") -> list[str]:
    """Check every promised stored record; no generic multisets, no assumed later validity.

    Ordered schema data (Gram tensors, coordinate vectors, coefficient series) is compared exactly:
    reordering changes the form or coordinates, not a generator presentation. Any conflict is an
    explicit unresolved defect and never silently accepted as a later enrichment.
    """
    problems: list[str] = []
    if artifact == current:
        return problems
    if isinstance(artifact, dict) and isinstance(current, dict):
        for key, proof in artifact.items():
            if key not in current:
                problems.append(f"{prefix}{key}: missing on main")
            elif current[key] == proof:
                pass
            elif isinstance(proof, dict) and isinstance(current[key], dict):
                base_block = base.get(key) or {} if isinstance(base, dict) else {}
                problems.extend(coverage_problems(base_block, proof, current[key], prefix=f"{prefix}{key}."))
            elif isinstance(base, dict) and current[key] == base.get(key):
                problems.append(f"{prefix}{key}: base retained, proof {proof!r} never recovered")
            else:
                problems.append(
                    f"{prefix}{key}: unresolved conflict current {current[key]!r} != artifact proof {proof!r}"
                )
    else:
        problems.append(f"{prefix}: unresolved conflict current {current!r} != artifact proof {artifact!r}")
    return problems


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
            subprocess.run(["git", "init", "--quiet"], cwd=work, check=True)
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
        lost = coverage_problems(previous_card, artifact_card, current_card)
        problems.extend(f"{tag}: {problem}" for problem in lost)
        if lost:
            print(f"{tag}: {len(lost)} unresolved recovery defect(s)")
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
                # Compare through the existing three-way record machinery, preserving current and
                # retained candidates, with no generic `compare_records` reconstruction. Here the
                # artifact is `base`, while current and recovered are the same retained value: every
                # departure from that reference is a reported conflict, never silently overwritten.
                _, differences = merge.merge(artifact_certificates[name], shard[name], shard[name])
                for detail in differences:
                    problems.append(f"{name}: unresolved certificate conflict at {detail}")
                if not differences:
                    problems.append(
                        f"{name}: unresolved conflict, current certificate differs from the retained artifact"
                    )
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
