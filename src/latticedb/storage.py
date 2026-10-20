"""Atomic replacement of persisted database text."""

import os
import stat
import tempfile
from pathlib import Path


def write_text(path: Path, text: str) -> None:
    """Keep the previous complete file if writing its replacement is interrupted."""
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    descriptor, temporary = tempfile.mkstemp(prefix=f".latticedb-write-{path.name}.", dir=path.parent)
    staging = Path(temporary)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            os.fchmod(stream.fileno(), mode)
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(staging, path)
    finally:
        staging.unlink(missing_ok=True)
