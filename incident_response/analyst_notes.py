from dataclasses import dataclass, field
from datetime import datetime
from typing import DefaultDict, List
from collections import defaultdict


@dataclass
class AnalystNote:
    incident_id: str
    author: str
    body: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


class AnalystNotebook:
    def __init__(self):
        self.notes: DefaultDict[str, List[AnalystNote]] = defaultdict(list)

    def add(self, incident_id: str, author: str, body: str) -> AnalystNote:
        note = AnalystNote(incident_id=incident_id, author=author, body=body)
        self.notes[incident_id].append(note)
        return note

    def list(self, incident_id: str) -> List[AnalystNote]:
        return self.notes[incident_id]


analyst_notebook = AnalystNotebook()
