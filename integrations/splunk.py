def format_splunk_event(alert):
    return {"event": alert_to_dict(alert), "sourcetype": "ransomware-defense:alert"}


def alert_to_dict(alert):
    return alert.dict() if hasattr(alert, "dict") else alert
