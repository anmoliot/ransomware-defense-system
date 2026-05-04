def explain_alert(alert):
    return {
        "state": alert.verdict.state,
        "risk_score": alert.verdict.risk_score,
        "reason": alert.verdict.reason,
        "signals": alert.verdict.signals,
    }
