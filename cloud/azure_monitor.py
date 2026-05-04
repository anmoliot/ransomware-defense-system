def detect_azure_privilege_abuse(event):
    return "Add member to role" in event.get("operationName", "")
