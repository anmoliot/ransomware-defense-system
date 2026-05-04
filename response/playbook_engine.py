import json
from pathlib import Path


class PlaybookEngine:
    def __init__(self, playbook_dir: str | Path | None = None):
        self.playbook_dir = Path(playbook_dir or Path(__file__).parent / "playbooks")

    def load(self, name: str):
        path = self.playbook_dir / f"{name}.json"
        return json.loads(path.read_text()) if path.exists() else None

    def list(self):
        return [path.stem for path in self.playbook_dir.glob("*.json")]


playbook_engine = PlaybookEngine()
