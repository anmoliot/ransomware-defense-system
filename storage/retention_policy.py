def should_retain(age_days: int, severity: str) -> bool:
    if severity in {"critical", "high"}:
        return age_days <= 365
    return age_days <= 90
