import json
from pathlib import Path


def load_yaml_rules(path: str | Path):
    rules = []
    for file_path in Path(path).glob("*.yml"):
        rules.append({"name": file_path.stem, "text": file_path.read_text()})
    return rules


def load_json_rules(path: str | Path):
    return [json.loads(file_path.read_text()) for file_path in Path(path).glob("*.json")]
