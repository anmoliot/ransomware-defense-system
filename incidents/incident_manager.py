from typing import Dict, List

from backend.models.schema import Incident


class IncidentManager:
    def __init__(self):
        self.incidents: Dict[str, Incident] = {}

    def upsert(self, incident: Incident) -> None:
        self.incidents[incident.id] = incident

    def list(self) -> List[Incident]:
        return list(self.incidents.values())

    def close(self, incident_id: str) -> bool:
        incident = self.incidents.get(incident_id)
        if not incident:
            return False
        incident.state = "closed"
        return True


incident_manager = IncidentManager()
