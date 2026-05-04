from typing import List

from backend.models.schema import AuditEvent


class InMemoryAuditStore:
    def __init__(self, max_items: int = 5000):
        self.max_items = max_items
        self.events: List[AuditEvent] = []

    def add(self, event: AuditEvent) -> None:
        self.events.append(event)
        if len(self.events) > self.max_items:
            self.events = self.events[-self.max_items:]

    def list(self, limit: int = 100) -> List[AuditEvent]:
        return self.events[-limit:]
