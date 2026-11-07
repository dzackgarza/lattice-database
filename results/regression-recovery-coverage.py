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
    if len(sys.argv) > 1 and sys.argv[1] != "--report":
        verifier = ROOT / sys.argv[1]
    else:
        verifier = ROOT / "results/verify-recovered-values.py"
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
    outcome_file = ROOT / "attachments" / "outcome-recovery-coverage"
    outcome_file.mkdir(exist_ok=True)
    outcome_file = outcome_file / f"{verifier.stem}-{(__import__('os').getpid())}.log"
    outcomes_file = outcome_file
    cases = [
        ("stored-field-omission", mutate_omission),
        ("ordered-vector-reversal", mutate_ordered),
        ("certificate-record-conflict", mutate_certificate),
    ]
    outcomes = []
    for label, mutation in cases:
        (work / "lattices" / f"{tag}.md").write_text(original)
        mutation(work, tag, original)
        result = run(work, verifier)
        expected = expected_diagnostic(label, result.stdout, result.stderr)
        outcomes.append((label, result.returncode, expected))
        tofile(outcomes_file, f"CASE {label} exit={result.returncode} diagnostic={expected}\n{result.stdout[-5000:]}\n{result.stderr[-1500:]}\n")

    for label, code, expected in outcomes:
        print(f"RESULT {label}: exit={code}, expected={expected}")
    if "--report" in sys.argv:
        print("all cases completed; this report accepts no outcome")
    else:
        missing_cases = [name for name, code, expected in outcomes if code == 0 or not expected]
        assert not missing_cases, "these deliberate mutations did not produce the required type of rejection: " + ", ".join(missing_cases)
        print("PASS: the actual baseline passes and all three mutations are rejected")


def expected_diagnostic(label: str, stdout: str, stderr: str) -> bool:
    """Match the real comparison branch and its evidence, rather than any nonzero result."""
    combined = stdout + stderr
    if label == "stored-field-omission":
        return "root_span" in stdout + stderr and ("missing" in stdout + stderr or "requires stored" in stdout + stderr)
    if label == "ordered-vector-reversal":
        return "root_span.norms" in stdout and ("unresolved conflict" in stdout or "never recovered" in stdout)
    if label == "certificate-record-conflict":
        return "derive" in stdout and "conflict" in stdout and "NameError" not in combined
    return False


def mutate_omission(work: Path, tag: str, original: str) -> None:
    metadata = yaml.safe_load(original.split("---")[1])
    # A true coverage omission: drop the dependent derived blocks together, so `model_validate`
    # accepts this card. The formerly EXCLUDED-keyed verifier lets this real loss pass silently;
    # the correct verifier must name it. A root_sublattice-only validation error would prove neither.
    metadata.pop("root_span")
    metadata.pop("root_sublattice", None)
    write_record(work, tag, metadata)


def mutate_ordered(work: Path, tag: str, original: str) -> None:
    """Reverse a genuine ordered coefficients vector accepted through the actual owned schema."""
    metadata = yaml.safe_load(original.split("---")[1])
    metadata["root_span"]["norms"] = list(reversed(metadata["root_span"]["norms"]))
    write_record(work, tag, metadata)


def mutate_certificate(work: Path, tag: str, original: str) -> None:
    """Only a recovered certificate record changes, exercising its conflict branch at its own assertion."""
    from latticedb import certificates
    certificate_path = work / "certificates" / f"{certificates.group(tag)}.yaml"
    recovered = yaml.safe_load(certificate_path.read_text())
    name = f"{tag} derive"
    assert name in recovered
    recovered[name]["by"] += "; unresolved conflicting certificate provenance in this copy only"
    certificate_path.write_text(yaml.dump(recovered, Dumper=yaml.CSafeDumper, sort_keys=False, allow_unicode=True))


def tofile(destination: Path, text: str) -> None:
    from datetime import datetime, timezone
    with destination.open("a", encoding="utf-8") as evidence:
        evidence.write(datetime.now(timezone.utc).isoformat() + " " + text + "\n")


def write_record(work: Path, tag: str, metadata: dict) -> None:
    card = work / "lattices" / f"{tag}.md"
    body = card.read_text().split("---")[2]
    card.write_text("---\n" + yaml.dump(metadata, sort_keys=False, allow_unicode=True, width=100000) + "---" + body)

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


def run(work: Path, verifier: Path) -> subprocess.CompletedProcess:
    """Invoke the real verifier itself on this temporary recovery checkout."""
    import os
    process = subprocess.run(
        [os.environ.get("PYTHON", sys.executable), str(verifier), str(work / "artifacts")],
        cwd=work, capture_output=True, text=True, timeout=600,
    )
    print(f"$ {process.args}\n{process.stdout[-6000:]}{process.stderr[-1500:]}")
    return process



if __name__ == "__main__":
    main()
