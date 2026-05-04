from integrations.splunk import format_splunk_event


class SplunkConnector:
    def send(self, alert):
        return {"connector": "splunk", "status": "planned", "event": format_splunk_event(alert)}
