from typing import List, Optional
from ..models.schema import SystemState, Alert

class StateManager:
    def __init__(self):
        self.current_state: SystemState = SystemState.NORMAL
        self.alert_history: List[Alert] = []

    def set_state(self, new_state: SystemState):
        self.current_state = new_state

    def get_state(self) -> SystemState:
        return self.current_state

    def add_alert(self, alert: Alert):
        self.alert_history.append(alert)
        # Optional: trim history if too large
        if len(self.alert_history) > 1000:
            self.alert_history = self.alert_history[-1000:]

    def get_alerts(self, limit: int = 50) -> List[Alert]:
        return self.alert_history[-limit:]

    def get_alert(self, alert_id: str) -> Optional[Alert]:
        for alert in self.alert_history:
            if alert.id == alert_id:
                return alert
        return None

# Singleton instance
state_manager = StateManager()
