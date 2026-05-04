import hashlib
from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class EvidenceItem:
    name: str
    artifact_type: str
    hash_sha256: str
    collected_by: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


def hash_evidence(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class EvidenceChain:
    def __init__(self):
        self.items: List[EvidenceItem] = []

    def add(self, name: str, artifact_type: str, data: bytes, collected_by: str) -> EvidenceItem:
        item = EvidenceItem(name=name, artifact_type=artifact_type, hash_sha256=hash_evidence(data), collected_by=collected_by)
        self.items.append(item)
        return item


evidence_chain = EvidenceChain()
