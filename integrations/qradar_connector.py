from integrations.qradar import format_qradar_event


class QRadarConnector:
    def send(self, alert):
        return {"connector": "qradar", "status": "planned", "event": format_qradar_event(alert)}
