def predict_attack_probability(signals):
    weighted = 0
    for signal in signals:
        if signal in {"canary_triggered", "yara_match", "ioc_match"}:
            weighted += 30
        elif signal in {"high_entropy", "high_file_rate", "smb_activity"}:
            weighted += 18
        elif signal.startswith("suspicious_process"):
            weighted += 12
    return min(100, weighted)
