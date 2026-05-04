from typing import Dict, List


class TelemetryIndexer:
    def __init__(self):
        self.documents: List[Dict] = []

    def index(self, document: Dict) -> None:
        self.documents.append(document)

    def search(self, field: str, value) -> List[Dict]:
        return [doc for doc in self.documents if doc.get(field) == value]


telemetry_indexer = TelemetryIndexer()
