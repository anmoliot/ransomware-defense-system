from pathlib import Path
from typing import Iterable, List

from threat_intel.yara_engine import yara_engine


def scan_files(paths: Iterable[str | Path]) -> List[dict]:
    results = []
    for path in paths:
        matches = yara_engine.scan_file(path)
        if matches:
            results.append({"path": str(path), "matches": matches})
    return results
