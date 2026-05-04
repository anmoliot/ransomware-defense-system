def build_compliance_report(alert_count: int, audit_count: int):
    return {"alerts": alert_count, "audit_events": audit_count, "framework": "SOC2-ready baseline"}
