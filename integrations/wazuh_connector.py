from integrations.wazuh import format_wazuh_event


class WazuhConnector:
    def send(self, alert):
        return {"connector": "wazuh", "status": "planned", "event": format_wazuh_event(alert)}
