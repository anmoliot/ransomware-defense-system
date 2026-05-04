import uuid
from typing import Iterable, List

from backend.models.schema import Alert, Incident
from correlation.attack_chain import describe_attack_chain
from correlation.event_graph import build_threat_graph
from timeline.timeline_builder import build_alert_timeline


class CorrelationEngine:
    def correlate(self, alerts: Iterable[Alert]) -> List[Incident]:
        incidents = []
        for alert in alerts:
            if alert.verdict.risk_score < 40:
                continue
            chain = describe_attack_chain(alert)
            severity = self._severity(alert.verdict.risk_score)
            title = "Ransomware Incident" if "Impact" in chain else "Suspicious Endpoint Activity"
            incidents.append(
                Incident(
                    id=f"inc-{uuid.uuid5(uuid.NAMESPACE_URL, alert.id)}",
                    title=title,
                    severity=severity,
                    risk_score=alert.verdict.risk_score,
                    alert_ids=[alert.id],
                    techniques=alert.verdict.mitre_techniques,
                    timeline=build_alert_timeline(alert),
                    graph=build_threat_graph(alert),
                )
            )
        return incidents

    def _severity(self, score: int) -> str:
        if score >= 80:
            return "critical"
        if score >= 60:
            return "high"
        if score >= 40:
            return "medium"
        return "low"


correlation_engine = CorrelationEngine()
