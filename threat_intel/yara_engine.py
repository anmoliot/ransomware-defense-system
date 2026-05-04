from pathlib import Path
from typing import List


class YaraEngine:
    """YARA scanner with a safe keyword fallback when yara-python is unavailable."""

    def __init__(self, rules_dir: str | Path | None = None):
        self.rules_dir = Path(rules_dir or Path(__file__).parent / "rules")
        self._compiled = None
        try:
            import yara  # type: ignore

            rule_files = {
                path.stem: str(path)
                for path in self.rules_dir.glob("*.yar")
            }
            self._compiled = yara.compile(filepaths=rule_files) if rule_files else None
        except Exception:
            self._compiled = None

    def scan_file(self, path: str | Path) -> List[str]:
        target = Path(path)
        if not target.exists() or not target.is_file():
            return []

        if self._compiled is not None:
            return [match.rule for match in self._compiled.match(str(target))]

        try:
            data = target.read_bytes()[:1024 * 1024].lower()
        except OSError:
            return []

        fallback_hits = []
        fallback_keywords = {
            "Ransomware_Note_Keyword": [b"your files are encrypted", b"decrypt", b"bitcoin"],
            "Shadow_Copy_Delete": [b"vssadmin", b"delete shadows"],
            "Suspicious_PowerShell": [b"powershell", b"encodedcommand"],
        }
        for rule_name, keywords in fallback_keywords.items():
            if all(keyword in data for keyword in keywords):
                fallback_hits.append(rule_name)

        return fallback_hits


yara_engine = YaraEngine()
