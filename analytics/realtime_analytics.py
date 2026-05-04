from collections import Counter


def summarize_alert_stream(alerts):
    states = Counter(str(alert.verdict.state) for alert in alerts)
    avg_risk = 0 if not alerts else sum(alert.verdict.risk_score for alert in alerts) / len(alerts)
    return {"count": len(alerts), "states": dict(states), "average_risk": round(avg_risk, 2)}
