"""Parallel certification shards integrate their certificate logs through Git."""

import subprocess
import sys
from pathlib import Path

import yaml

REPOSITORY = Path(__file__).resolve().parent.parent


def git(root: Path, *arguments: str) -> None:
    subprocess.run(["git", "-C", str(root), *arguments], check=True, capture_output=True)


def write(root: Path, data: dict[str, object]) -> None:
    (root / "certificates").mkdir(exist_ok=True)
    (root / "certificates" / "shared.yaml").write_text(yaml.safe_dump(data, sort_keys=False))


def test_two_shards_rebase_adjacent_certificates_without_conflict(tmp_path: Path) -> None:
    (tmp_path / ".gitattributes").write_text((REPOSITORY / ".gitattributes").read_text())
    write(tmp_path, {"0001 derive": {"hash": "a"}, "0004 derive": {"hash": "d"}})
    git(tmp_path, "init", "-q", "-b", "main")
    git(tmp_path, "config", "user.name", "test")
    git(tmp_path, "config", "user.email", "test@example.invalid")
    driver = f"{sys.executable} -m latticedb merge-keyed-map %O %A %B"
    git(tmp_path, "config", "merge.keyed-map.driver", driver)
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-q", "-m", "base")
    git(tmp_path, "checkout", "-q", "-b", "shard")
    write(tmp_path, {"0001 derive": {"hash": "a"}, "0003 derive": {"hash": "c"}, "0004 derive": {"hash": "d"}})
    git(tmp_path, "commit", "-q", "-am", "shard 1")
    git(tmp_path, "checkout", "-q", "main")
    write(tmp_path, {"0001 derive": {"hash": "a"}, "0002 derive": {"hash": "b"}, "0004 derive": {"hash": "d"}})
    git(tmp_path, "commit", "-q", "-am", "shard 0")
    git(tmp_path, "checkout", "-q", "shard")
    git(tmp_path, "rebase", "-q", "main")
    assert list(yaml.safe_load((tmp_path / "certificates" / "shared.yaml").read_text())) == [
        "0001 derive",
        "0002 derive",
        "0003 derive",
        "0004 derive",
    ]
