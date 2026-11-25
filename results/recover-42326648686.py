"""Recover the completed results of run 42326648686 from its per-tag artifacts (issue #17).

Each artifact is a patch against the revision the run read, with that revision recorded beside it. For
one artifact this script:

1. materialises the revision's own copy of the files the patch touches — the card, its certificate
   shard, `exceeded.yaml`, the ledger — and applies the patch there with `git apply`, so every context
   and every deleted line is verified by Git and there is no second patch reader here;
2. reads back only the entries of the ledger the patch touches, streaming the patched ledger from disk,
   so the hundred-megabyte file is never held in memory;
3. reconciles each file three ways — the revision's version, the current tree, the recovered version —
   at the level of stored fields with `latticedb.merge`: a value current main gained since the revision
   is kept, the artifact's value is taken, and a field both changed differently is left on the current
   side and reported, with the recovered candidate written beside it.

A reported conflict is a delivery blocker: this exits non-zero and the recovery is not finished.

    PYTHONPATH=src python3 results/recover-42326648686.py ATTACHMENTS/openmath-certify-42326648686
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from pydantic import TypeAdapter

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from latticedb import certificates, failures, merge  # noqa: E402

LEDGER = "failures.yaml"
EVIDENCE = Path("results") / "evidence-17" / "conflicts"


def show(revision: str, path: str) -> str:
    return subprocess.run(["git", "show", f"{revision}:{path}"], check=True, capture_output=True, text=True).stdout


def patch_files(text: str) -> set[str]:
    """The a/ path of each file a patch touches."""
    return {
        line[len("diff --git a/"):].rsplit(" b/", 1)[0]
        for line in text.splitlines()
        if line.startswith("diff --git a/") and " b/" in line
    }


def ledger_keys(text: str) -> set[str]:
    """The ledger entries a patch touches: every top-level entry its hunks mention."""
    keys: set[str] = set()
    inside = False
    for line in text.splitlines():
        if line.startswith("diff --git a/"):
            inside = line[len("diff --git a/"):].rsplit(" b/", 1)[0] == LEDGER
            continue
        if not inside or not line or line[0] not in " +-":
            continue
        body = line[1:]
        if body[:1] not in (" ", "\t") and body.endswith(":"):
            keys.add(body[:-1])
    return keys


def ledger_values(path: Path, keys: set[str]) -> dict:
    """The wanted entries of a ledger, read by streaming it from disk."""
    values: dict = {}
    key = None
    keep = False
    block: list[str] = []
    with path.open() as ledger:
        for line in ledger:
            if line[:1] not in (" ", "\t", "-") and line.rstrip("\n").endswith(":"):
                if keep and key is not None:
                    values[key] = next(iter((yaml.safe_load("".join(block)) or {}).values()), {})
                key = line.rstrip("\n")[:-1]
                keep = key in keys
                block = []
            if keep:
                block.append(line)
    if keep and key is not None:
        values[key] = next(iter((yaml.safe_load("".join(block)) or {}).values()), {})
    return values


def load_shard(path: Path) -> dict:
    return (yaml.load(path.read_text(), Loader=yaml.CSafeLoader) or {}) if path.exists() else {}


def dump_shard(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.dump(data, Dumper=yaml.CSafeDumper, sort_keys=False, allow_unicode=True))


def verify_ledger_entrys(path: Path, members: set[str]) -> None:
    """Each entry is in the shard of its own key and reads back through the ledger's own model."""
    shard = TypeAdapter(failures.Failures).validate_python(yaml.load(path.read_text(), Loader=yaml.CSafeLoader) or {})
    for name in members:
        if failures.group(name) != path.stem:
            raise SystemExit(f"{name} belongs to failures/{failures.group(name)}.yaml, not {path.name}")
        if name in shard and shard[name].disposition not in ("open", "retry", "resolved"):
            raise SystemExit(f"{name}: {shard[name].disposition} is not a disposition")


def keyed(item):
    """The identity of a list item, so a list both sides extended keeps both.

    A failure attempt is its input hash, a stored morphism its target and name, and anything else its
    own text.
    """
    if isinstance(item, dict):
        if "hash" in item:
            return item["hash"]
        if "name" in item:
            return (str(item.get("target")), str(item["name"]))
        return json.dumps(item, sort_keys=True, default=str)
    return item


def main(directory: Path) -> int:
    artifacts = sorted(
        (
            (
                artifact.name.split("-")[-1],
                (artifact / "certification-base.txt").read_text().strip(),
                artifact,
            )
            for artifact in directory.iterdir()
            if artifact.is_dir()
        ),
        key=lambda entry: entry[0],
    )
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    report: list[str] = []
    conflicts: list[str] = []
    diverged: list[str] = []
    bases: dict[str, Path] = {}

    with tempfile.TemporaryDirectory() as scratch:
        scratch_path = Path(scratch)
        for tag, base, artifact in artifacts:
            patch_path = (artifact / "certification.patch").resolve()
            patch = patch_path.read_text()
            touched = patch_files(patch)
            shard = certificates.group(tag)

            with tempfile.TemporaryDirectory(dir=scratch_path) as raw:
                work = Path(raw)
                for path in touched:
                    target = work / path
                    target.parent.mkdir(parents=True, exist_ok=True)
                    if path == LEDGER:
                        if base not in bases:
                            bases[base] = scratch_path / f"base-{base}.yaml"
                            bases[base].write_text(show(base, LEDGER))
                        shutil.copyfile(bases[base], target)
                    else:
                        target.write_text(show(base, path))
                subprocess.run(["git", "apply", "-p1", str(patch_path)], cwd=work, check=True)

                card_path = work / "lattices" / f"{tag}.md"
                if card_path.exists():
                    current = Path("lattices") / f"{tag}.md"
                    current_text = current.read_text()
                    base_text = show(base, f"lattices/{tag}.md")
                    recovered_text = card_path.read_text()
                    if current_text == base_text:
                        current.write_text(recovered_text)
                        report.append(f"{tag}: card written from the artifact")
                    else:
                        merged, found = merge.merge(
                            yaml.safe_load(base_text.split("---")[1]),
                            yaml.safe_load(current_text.split("---")[1]),
                            yaml.safe_load(recovered_text.split("---")[1]),
                            key=keyed,
                        )
                        body = "---".join(current_text.split("---")[2:])
                        current.write_text(
                            "---\n" + yaml.dump(merged, sort_keys=False, allow_unicode=True, width=100000) + "---" + body
                        )
                        report.append(f"{tag}: card reconciled with {len(found)} conflict(s)")
                        conflicts.extend(f"{tag} lattices/{tag}.md {path}" for path in found)
                        if found:
                            (EVIDENCE / f"{tag}-card-recovered.md").write_text(recovered_text)

                certificate_path = work / "certificates" / f"{shard}.yaml"
                if certificate_path.exists():
                    target = Path("certificates") / f"{shard}.yaml"
                    merged, found = merge.merge(
                        yaml.safe_load(show(base, f"certificates/{shard}.yaml")) or {},
                        load_shard(target),
                        yaml.safe_load(certificate_path.read_text()) or {},
                    )
                    dump_shard(target, {name: merged[name] for name in sorted(merged)})
                    report.append(f"{tag}: certificate shard {shard} reconciled with {len(found)} conflict(s)")
                    conflicts.extend(f"{tag} certificates/{shard}.yaml {path}" for path in found)
                    if found:
                        shutil.copyfile(certificate_path, EVIDENCE / f"{tag}-certificates-{shard}-recovered.yaml")

                exceeded_path = work / "exceeded.yaml"
                if exceeded_path.exists():
                    # `exceeded.yaml` is the interruption log, not a published value: an entry the
                    # current tree already has is the later run's and is kept as it is, and only the
                    # entries it lacks are added. A divergence is reported, never blocking, because the
                    # artifact that recorded it is retained and the ledger carries the durable evidence.
                    target = Path("exceeded.yaml")
                    current = load_shard(target)
                    recovered = yaml.safe_load(exceeded_path.read_text()) or {}
                    added = [name for name in recovered if name not in current]
                    dump_shard(target, {**current, **{name: recovered[name] for name in added}})
                    kept = sorted(set(recovered) - set(added))
                    report.append(
                        f"{tag}: exceeded.yaml, {len(added)} entr(y/ies) added, {len(kept)} kept as current"
                    )
                    if kept:
                        diverged.extend(f"{tag} exceeded.yaml {name}" for name in kept)

                if LEDGER in touched:
                    keys = ledger_keys(patch)
                    base_values = ledger_values(bases[base], keys)
                    recovered_values = ledger_values(work / LEDGER, keys)
                    if not keys <= set(recovered_values):
                        raise SystemExit(f"{tag}: the patched ledger lost {sorted(keys - set(recovered_values))}")
                    # Each entry goes to the shard of its own key: a patch's diff context reaches into
                    # the neighbouring entries, which can belong to other cards.
                    shards: dict[str, set[str]] = {}
                    for key in keys:
                        shards.setdefault(failures.group(key), set()).add(key)
                    for shard_of, members in sorted(shards.items()):
                        target = Path(failures.DIRECTORY) / f"{shard_of}.yaml"
                        current = load_shard(target)
                        merged, found = merge.merge(
                            {key: base_values[key] for key in members if key in base_values},
                            {key: current[key] for key in members if key in current},
                            {key: recovered_values[key] for key in members if key in recovered_values},
                            key=keyed,
                        )
                        dump_shard(target, {**current, **{name: merged[name] for name in sorted(merged)}})
                        report.append(
                            f"{tag}: {len(members)} failure entr(y/ies) merged into failures/{shard_of}.yaml "
                            f"with {len(found)} conflict(s)"
                        )
                        conflicts.extend(f"{tag} failures/{shard_of}.yaml {path}" for path in found)
                        if found:
                            (EVIDENCE / f"{tag}-failures-{shard_of}-recovered.yaml").write_text(
                                yaml.dump(
                                    {key: recovered_values[key] for key in sorted(members) if key in recovered_values},
                                    Dumper=yaml.CSafeDumper,
                                    sort_keys=False,
                                    allow_unicode=True,
                                )
                            )
                        verify_ledger_entrys(target, members)

    print("\n".join(report))
    if diverged:
        print(f"\n{len(diverged)} interruption entr(y/ies) the current tree had already moved on from:")
        print("\n".join(diverged))
    if conflicts:
        print(f"\n{len(conflicts)} conflict(s), kept on the current side; the recovered values are in {EVIDENCE}:")
        print("\n".join(conflicts))
        return 1
    print("\nno conflict: every field the artifacts carry is on the cards, in the shards and in the ledger")
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1])))
