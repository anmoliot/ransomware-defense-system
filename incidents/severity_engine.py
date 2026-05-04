def severity_from_score(score: int) -> str:
    if score >= 90:
        return "critical"
    if score >= 70:
        return "high"
    if score >= 40:
        return "medium"
    return "low"


def should_escalate(score: int, repeated_alerts: int = 1) -> bool:
    return score >= 80 or repeated_alerts >= 3
