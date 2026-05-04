def insider_risk(signals):
    weights = {"after_hours": 20, "bulk_download": 35, "privilege_escalation": 35, "disabled_mfa": 25}
    return min(100, sum(weights.get(signal, 0) for signal in signals))
