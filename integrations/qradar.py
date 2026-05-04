def format_qradar_event(alert):
    return {"qid": 500001, "payload": alert.dict() if hasattr(alert, "dict") else alert}
