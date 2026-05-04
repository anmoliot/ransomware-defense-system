from typing import Dict, List

from backend.models.schema import Incident


class IncidentStore:
    def __init__(self):
        self._incidents: Dict[str, Incident] = {}

    def upsert(self, incident: Incident) -> Incident:
        existing = self._incidents.get(incident.id)
        if existing:
            existing.risk_score = max(existing.risk_score, incident.risk_score)
            existing.severity = incident.severity
            existing.alert_ids = sorted(set(existing.alert_ids + incident.alert_ids))
            existing.timeline = sorted(existing.timeline + incident.timeline, key=lambda event: event.timestamp)
            existing.graph = incident.graph
            return existing
        self._incidents[incident.id] = incident
        return incident

    def list(self) -> List[Incident]:
        return list(self._incidents.values())


incident_store = IncidentStore()
