import uuid
from datetime import datetime

from backend.models.schema import Alert, TimelineEvent


def make_event(event_type: str, title: str, description: str, severity: str, timestamp: datetime | None = None, mitre=None):
    return TimelineEvent(
        id=str(uuid.uuid4()),
        timestamp=timestamp or datetime.utcnow(),
        event_type=event_type,
        title=title,
        description=description,
        severity=severity,
        mitre_technique=mitre,
    )


def alert_summary_event(alert: Alert) -> TimelineEvent:
    return make_event(
        "alert",
        f"{alert.verdict.state} alert",
        alert.verdict.reason,
        _severity(alert.verdict.risk_score),
        timestamp=alert.timestamp,
    )


def _severity(score: int) -> str:
    if score >= 80:
        return "critical"
    if score >= 40:
        return "warning"
    return "info"
