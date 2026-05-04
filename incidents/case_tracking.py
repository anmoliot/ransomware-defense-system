from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class CaseNote:
    author: str
    body: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Case:
    incident_id: str
    owner: str
    notes: List[CaseNote] = field(default_factory=list)
