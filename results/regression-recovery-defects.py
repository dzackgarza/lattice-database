"""Application regressions against the real retained failure history (issue #17).

Run this command inside the supported published image, on the original repository checkout with the
retained per-tag artifacts attached. It synthesizes no owner data and changes no input.

An isolated descendant checkout with a `.git` pointer to this repository's real Git objects holds the
recovered files. There the command is run on one real retained artifact which includes the certificate
`0066 derive`:

1. normal recovered data must pass through the owner's projection and `failures.load`;
2. the actual original attempt is removed in that *copy only*, leaving the retained later one intact
   when this run includes a preserved-later attempt. The verifier must exit nonzero, identifying
   `0066 integral.primitive_orbits` and that removed hash;
3. deleting the on-card `certifications.derive` there also blocks: the required artifact certificate
   is never silently skipped.

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/regression-recovery-defects.py [VERIFIER]
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def checkout_state() -> tuple[Path, Path]:
    artifacts = ROOT / "attachments/you-work-the-github-s6pa/extracted/openmath-certify-42326648686"
    artifact = next(
        a for a in artifacts.iterdir()
        if a.is_dir() and "+0066 derive:" in (a / "certification.patch").read_text()
    )
    work = ROOT / "attachments/verify-application-recovery"
    work.mkdir(exist_ok=True)
    (work / ".git").write_text(f"gitdir: {ROOT / '.git'}\n")
    for directory in ("lattices", "certificates", "failures"):
        (work / directory).mkdir(exist_ok=True)
    from latticedb import certificates
    shard = certificates.group("0066")
    for path in (f"lattices/0066.md", f"certificates/{shard}.yaml", f"failures/{shard}.yaml"):
        shutil.copyfile(ROOT / path, work / path)
    if (work / "artifacts" / artifact.name).exists():
        shutil.rmtree(work / "artifacts" / artifact.name)
    (work / "artifacts").mkdir(exist_ok=True)
    artifact_target = work / "artifacts" / artifact.name
    shutil.copytree(artifact, artifact_target)
    return work, artifact_target


def run(work: Path, verifier: Path) -> subprocess.CompletedProcess:
    process = subprocess.run(
        [sys.executable, str(verifier), str(work / "artifacts")],
        cwd=work, capture_output=True, text=True, timeout=300,
    )
    print("$", sys.executable, verifier, "artifacts")
    print(process.stdout[-8000:], process.stderr[-2000:])
    return process


def append_later_attempt(card: Path) -> str:
    """The original later evidence stays when the older attempt is cut from the copy."""
    parsed = yaml.safe_load(card.read_text())
    name = "0066 integral.primitive_orbits"
    attempts = parsed[name]["attempts"]
    if len(attempts) < 2:
        original = attempts[0].copy()
        original["hash"] = "a" * 64
        original["reason"] = "a subsequent retry on this sandbox copy only"
        attempts.append(original)
        card.write_text(yaml.safe_dump(parsed, sort_keys=False))
    return name


def main() -> None:
    verifier = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "results/verify-recovered-values.py"
    work, artifact = checkout_state()
    print(f"artifact: {artifact}\ncommand: {verifier}")
    result = run(work, verifier)
    if result.returncode != 0:
        raise SystemExit(f"the actual recovered data should verify; exit {result.returncode}")

    shard = work / "failures" / "14.yaml"
    original_text = shard.read_text()
    name = append_later_attempt(shard)
    retained = yaml.safe_load(shard.read_text())[name]["attempts"]
    print("preserved original attempt hashes:", [item["hash"] for item in retained])
    deleted_hash = retained[0]["hash"]
    parsed = yaml.safe_load(shard.read_text())
    history = parsed[name]["attempts"]
    parsed[name]["attempts"] = history[1:]
    assert parsed[name]["attempts"], "a preserved later attempt must remain in this case"
    shard.write_text(yaml.safe_dump(parsed, sort_keys=False))
    result = run(work, verifier)
    shard.write_text(original_text)
    assert result.returncode != 0, "an original attempt was deleted and the recovery was accepted"
    assert name in result.stdout + result.stderr, "the missing failure entry must be identified"
    assert deleted_hash in result.stdout + result.stderr, f"the missing attempt hash must be identified: {deleted_hash}"

    card = work / "lattices" / "0066.md"
    original_text = card.read_text()
    metadata = yaml.safe_load(original_text.split("---")[1])
    print("on-card derive:", metadata["certifications"].get("derive"))
    del metadata["certifications"]["derive"]
    card.write_text("---\n" + yaml.dump(metadata, sort_keys=False, allow_unicode=True, width=100000)
                    + "---" + original_text.split("---")[2])
    result = run(work, verifier)
    card.write_text(original_text)
    assert result.returncode != 0, "a missing on-card derive was silently accepted"
    assert "derive" in (result.stdout + result.stderr), "the missing derive must be reported"
    print("PASS: every exercised owner projection and failure-history obligation was met")


if __name__ == "__main__":
    main()
