from collections import defaultdict
from typing import DefaultDict, List

from incidents.case_tracking import Case, CaseNote


class CaseTracker:
    def __init__(self):
        self.cases: DefaultDict[str, Case] = defaultdict(lambda: Case(incident_id="", owner="unassigned"))

    def assign(self, incident_id: str, owner: str) -> Case:
        case = self.cases[incident_id]
        case.incident_id = incident_id
        case.owner = owner
        return case

    def add_note(self, incident_id: str, author: str, body: str) -> CaseNote:
        case = self.cases[incident_id]
        case.incident_id = incident_id
        note = CaseNote(author=author, body=body)
        case.notes.append(note)
        return note

    def notes(self, incident_id: str) -> List[CaseNote]:
        return self.cases[incident_id].notes


case_tracker = CaseTracker()
