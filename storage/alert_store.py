from typing import List

from backend.models.schema import Alert


class InMemoryAlertStore:
    def __init__(self, max_items: int = 1000):
        self.max_items = max_items
        self.alerts: List[Alert] = []

    def add(self, alert: Alert) -> None:
        self.alerts.append(alert)
        if len(self.alerts) > self.max_items:
            self.alerts = self.alerts[-self.max_items:]

    def list(self, limit: int = 50) -> List[Alert]:
        return self.alerts[-limit:]
