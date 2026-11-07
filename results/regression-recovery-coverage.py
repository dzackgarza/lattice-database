"""Reproduce the verifier's omission of an owned stored field (issue #17).

The verifier used to skip `morphisms`, `root_span`, and `root_sublattice` unconditionally, even when
`git apply` on the retained base shows that computation produced exactly those values. For a real artifact
carrying one of those fields this runner:

1. applies that artifact's original patch to its exact base using `git`;
2. makes a fresh copy of the recovered checkout under `attachments/`;
3. removes one such field from that copy, with the owner project and card model left intact;
4. expects the supplied verifier to exit nonzero and name the field rather than accept its omission.

Changing values here affects only the copy, not the retained artifacts and not main.

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/regression-recovery-coverage.py [VERIFIER]
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "attachments/you-work-the-github-s6pa/extracted/openmath-certify-42326648686"
FIELDS = ("root_span", "root_sublattice", "morphisms", "dual_gram_tensor")


def apply(filename: Path, base: str, artifact: Path) -> dict:
    """Reconstruct every file the real patch needs, before running `git apply` against it."""
    patch_path = artifact / "certification.patch"
    work = Path(tempfile.mkdtemp(prefix="artifact-value-", dir=ROOT / "attachments"))
    for path in patch_files(patch_path):
        source = work / path
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text(subprocess.run(["git", "show", f"{base}:{path}"], check=True, capture_output=True, text=True).stdout)
    subprocess.run(["git", "init", "--quiet"], cwd=work, check=True)
    subprocess.run(["git", "apply", "-p1", str(patch_path.resolve())], cwd=work, check=True)
    return yaml.safe_load((work / filename).read_text().split("---")[1])


def patch_files(patch_path: Path) -> set[str]:
    return {
        line[len("diff --git a/"):].rsplit(" b/", 1)[0]
        for line in patch_path.read_text().splitlines()
        if line.startswith("diff --git a/") and " b/" in line
    }


def main() -> None:
    verifier = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "results/verify-recovered-values.py"
    target = None
    for artifact in sorted(BUNDLE.iterdir()):
        if not artifact.is_dir():
            continue
        tag = artifact.name.split("-")[-1]
        base = (artifact / "certification-base.txt").read_text().strip()
        patched = apply(Path("lattices") / f"{tag}.md", base, artifact)
        for field in FIELDS:
            if patched.get(field):
                target = (tag, base, artifact, field)
                break
        if target and patched.get('integral', {}).get('discriminant_form'):
            break
        target = None
    if target is None:
        raise SystemExit(f"no retained artifact besides {FIELDS}")
    tag, base, artifact, field = target
    print(f"reproduces a genuine retained stored field: {tag} {field}")

    work = Path(tempfile.mkdtemp(prefix=f"recovery-{tag}-{field}-", dir=ROOT / "attachments"))
    (work / ".git").write_text(f"gitdir: {ROOT / '.git'}\n")
    for directory in ("lattices", "certificates", "failures", "artifacts"):
        (work / directory).mkdir(exist_ok=True)
    (work / "lattices").mkdir(exist_ok=True)
    shutil.copy(ROOT / "lattices" / f"{tag}.md", work / "lattices" / f"{tag}.md")
    (work / "certificates").mkdir(exist_ok=True)
    from latticedb import certificates, failures
    certificate_shard = certificates.group(tag)
    current_certificate = ROOT / "certificates" / f"{certificate_shard}.yaml"
    shutil.copy(current_certificate, Path(work, "certificates") / current_certificate.name)
    # The other shards must match the actual tag and the entries really mentioned by this artifact,
    # including entries named only by its diff's context lines; a hardcoded tests/14.yaml is wrong.
    (work / "failures").mkdir(exist_ok=True)
    for key in ledger_keys(artifact / "certification.patch"):
        shard = failures.group(key)
        shutil.copy(ROOT / "failures" / f"{shard}.yaml", work / "failures" / f"{shard}.yaml")
    shutil.copytree(artifact, work / "artifacts" / artifact.name)

    initial = run(work, verifier)
    if initial.returncode:
        raise SystemExit(f"baseline does not verify ({initial.returncode}), so this runner proves nothing yet")

    original = (work / "lattices" / f"{tag}.md").read_text()
    metadata = yaml.safe_load(original.split("---")[1])
    missing = metadata.pop(field)
    print("omitted from this copy only:", field, "containing", len(missing) if hasattr(missing, "__len__") else 1)
    write_record(work, tag, metadata)
    report = run(work, verifier)
    assert report.returncode, "the omitted stored field must not pass"
    assert field in report.stdout, f"the omitted field must be reported: {field}"
    print("PASS: a missing promised value is a reported defect")

    # The ordered tensors/vectors are not unordered generator shorthand. Swap the first two rows of
    # the retained card's Gram tensor in this copy only. A verifier that normalizes lists into sets
    # might consider these identical, but its definition and its certificate cannot.
    metadata = yaml.safe_load(original.split("---")[1])
    metadata["gram_tensor"] = [row[:] for row in metadata["gram_tensor"]]
    assert len(metadata["gram_tensor"]) > 1
    metadata["gram_tensor"][0], metadata["gram_tensor"][1] = metadata["gram_tensor"][1], metadata["gram_tensor"][0]
    write_record(work, tag, metadata)
    report = run(work, verifier)
    assert report.returncode, "a swapped pair of Gram rows must be refused as ordered data"
    assert "Gram tensor" in report.stdout or "gram_tensor" in (report.stdout + report.stderr), (
        "must explain that the actual ordered tensor is inconsistent with its artifact"
    )
    print("PASS: an ordered tensor's reordering is rejected")

    # A real conflict is not presumed to be a valid superseding value. Keep `Lattice.model_validate`
    # valid but alter an actually computed discriminant-form count in this copy, so full comparison
    # must reach the retained base/proof/current conflict check.
    metadata = yaml.safe_load(original.split("---")[1])
    form = metadata["integral"]["discriminant_form"]
    form["isotropic_classes"] = form["isotropic_classes"] + 1
    write_record(work, tag, metadata)
    report = run(work, verifier)
    assert report.returncode, "the current/proof mismatch must not pass because it might be newer"
    assert "conflict" in (report.stdout + report.stderr).lower(), (
        "must report the unresolved current/proof conflict explicitly"
    )
    print("PASS: an unresolved current/artifact mismatch prevents acceptance")


def ledger_keys(patch_path: Path) -> set[str]:
    """Top-level computation entries in a real artifact's failure-ledger patch, including context."""
    found: set[str] = set()
    inside = False
    for line in patch_path.read_text().splitlines():
        if line.startswith("diff --git a/"):
            inside = line[len("diff --git a/"):].rsplit(" b/", 1)[0] == "failures.yaml"
        elif inside and line[:1] in ("+", "-", " "):
            body = line[1:]
            if body[:1] not in (" ", "	", "-") and body.rstrip().endswith(":"):
                found.add(body.rstrip()[:-1])
    return found


def write_record(work: Path, tag: str, metadata: dict) -> None:
    """Write this copy's front matter, leaving the corpus serializer's stored card types unchanged."""
    card = work / "lattices" / f"{tag}.md"
    body = card.read_text().split("---")[2]
    card.write_text(
        "---\n" + yaml.dump(metadata, sort_keys=False, allow_unicode=True, width=100000) + "---" + body
    )


if __name__ == "__main__":
    main()
