from mitre.tactic_engine import score_tactics


def contextual_score(alert, user_risk: int = 0, asset_criticality: int = 0):
    base = alert.verdict.risk_score
    mitre = score_tactics(alert.verdict.mitre_techniques)
    intel = 20 if "ioc_match" in alert.verdict.signals or "yara_match" in alert.verdict.signals else 0
    ancestry = 15 if any(signal.startswith("suspicious_process") for signal in alert.verdict.signals) else 0
    return min(100, int(base * 0.45 + mitre * 0.2 + intel + ancestry + user_risk * 0.1 + asset_criticality * 0.1))
