def format_wazuh_event(alert):
    return {"integration": "wazuh", "alert": alert.dict() if hasattr(alert, "dict") else alert}
