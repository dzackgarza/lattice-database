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
    work = Path(tempfile.mkdtemp(prefix="artifact-value-", dir=ROOT / "attachments"))
    source = work / filename
    source.write_text(subprocess.run(["git", "show", f"{base}:{filename}"], check=True, capture_output=True, text=True).stdout)
    subprocess.run(["git", "apply", "-p1", str(artifact.resolve())], cwd=work, check=True)
    return yaml.safe_load(source.read_text().split("---")[1])


def main() -> None:
    verifier = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "results/verify-recovered-values.py"
    target = None
    for artifact in sorted(BUNDLE.iterdir()):
        if not artifact.is_dir():
            continue
        tag = artifact.name.split("-")[-1]
        base = (artifact / "certification-base.txt").read_text().strip()
        patched = apply(Path("lattices") / f"{tag}.md", base, artifact / "certification.patch")
        for field in FIELDS:
            if patched.get(field):
                target = (tag, base, artifact, field)
                break
        if target:
            break
    if target is None:
        raise SystemExit(f"no retained artifact besides {FIELDS}")
    tag, base, artifact, field = target
    print(f"reproduces a genuine retained stored field: {tag} {field}")

    work = Path(tempfile.mkdtemp(prefix=f"recovery-{tag}-{field}-", dir=ROOT / "attachments"))
    (work / ".git").write_text(f"gitdir: {ROOT / '.git'}\n")
    for directory in ("lattices", "certificates", "failures", "artifacts"):
        (work / directory).mkdir(exist_ok=True)
    for directory in ("lattices", "certificates", "failures"):
        where = work / directory
        for source in (ROOT / directory).iterdir():
            if source.is_file() and (
                (directory == "lattices" and source.name == f"{tag}.md") or
                (directory == "certificates" and source.name == "14.yaml")
            ):
                shutil.copyfile(source, where / source.name)
    from latticedb import certificates
    certificate_shard = certificates.group(tag)
    current_certificate = ROOT / "certificates" / f"{certificate_shard}.yaml"
    shutil.copy(current_certificate, Path(work, "certificates") / current_certificate.name)
    shutil.copytree(artifact, work / "artifacts" / artifact.name)

    original = (work / "lattices" / f"{tag}.md").read_text()
    metadata = yaml.safe_load(original.split("---")[1])
    missing = metadata.pop(field)
    print("omitted from this copy only:", field, "containing", len(missing) if hasattr(missing, "__len__") else 1)
    before = root_card = (work / "lattices" / f"{tag}.md").read_text()
    (work / "lattices" / f"{tag}.md").write_text(
        "---\n" + yaml.dump(metadata, sort_keys=False, allow_unicode=True, width=100000)
        + "---" + original.split("---")[2]
    )
    process = subprocess.run(
        [sys.executable, str(verifier), str(work / "artifacts")],
        cwd=work, capture_output=True, text=True, timeout=600,
    )
    print(process.stdout[-8000:], process.stderr[-2000:])
    assert process.returncode, "the omitted stored field must not pass"
    assert field in process.stdout, f"the omitted field must be reported: {field}"
    print("PASS: the omitted promised value is an explicit failure, not silently ignored")


if __name__ == "__main__":
    main()
