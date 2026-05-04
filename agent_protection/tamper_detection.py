def detect_tampering(events):
    markers = ("service stop", "delete logs", "disable", "uninstall", "kill agent")
    return [event for event in events if any(marker in str(event).lower() for marker in markers)]
