from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass
class IncidentCase:
    incident_id: str
    owner: str = "unassigned"
    status: str = "new"
    priority: str = "medium"
    created_at: datetime = field(default_factory=datetime.utcnow)
    tags: List[str] = field(default_factory=list)


class CaseManager:
    def __init__(self):
        self.cases: Dict[str, IncidentCase] = {}

    def open_case(self, incident_id: str, priority: str = "medium") -> IncidentCase:
        case = self.cases.get(incident_id) or IncidentCase(incident_id=incident_id, priority=priority)
        self.cases[incident_id] = case
        return case

    def assign(self, incident_id: str, owner: str) -> IncidentCase:
        case = self.open_case(incident_id)
        case.owner = owner
        case.status = "assigned"
        return case

    def update_status(self, incident_id: str, status: str) -> IncidentCase:
        case = self.open_case(incident_id)
        case.status = status
        return case


case_manager = CaseManager()
