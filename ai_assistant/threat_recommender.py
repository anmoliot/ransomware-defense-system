def recommend_next_steps(signals):
    steps = []
    if "ioc_match" in signals:
        steps.append("Enrich matched IOC and search across endpoints.")
    if "smb_activity" in signals:
        steps.append("Check lateral movement and isolate affected subnet if confirmed.")
    if "canary_triggered" in signals:
        steps.append("Prioritize containment and preserve evidence.")
    return steps or ["Continue monitoring and collect more telemetry."]
