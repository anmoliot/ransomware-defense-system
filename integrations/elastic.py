def format_elastic_document(alert):
    data = alert.dict() if hasattr(alert, "dict") else alert
    data["_index"] = "ransomware-defense-alerts"
    return data
