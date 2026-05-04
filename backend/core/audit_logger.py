import uuid
from datetime import datetime
from typing import List

from backend.models.schema import AuditEvent


class AuditLogger:
    def __init__(self):
        self.events: List[AuditEvent] = []

    def log(self, actor: str, action: str, target: str, outcome: str, details=None) -> AuditEvent:
        event = AuditEvent(
            id=str(uuid.uuid4()),
            timestamp=datetime.utcnow(),
            actor=actor,
            action=action,
            target=target,
            outcome=outcome,
            details=details or {},
        )
        self.events.append(event)
        if len(self.events) > 5000:
            self.events = self.events[-5000:]
        return event

    def list_events(self, limit: int = 100) -> List[AuditEvent]:
        return self.events[-limit:]


audit_logger = AuditLogger()
