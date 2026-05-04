def suggest_remediation(alert):
    suggestions = ["Preserve evidence", "Run threat hunt for shared IOCs"]
    if alert.verdict.risk_score >= 80:
        suggestions.insert(0, "Isolate endpoint in dry-run playbook review")
    return suggestions
