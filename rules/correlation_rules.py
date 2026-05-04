CORRELATION_RULES = [
    {
        "name": "Ransomware Incident",
        "when": ["suspicious_process", "high_entropy", "high_file_rate"],
        "severity": "critical",
    },
    {
        "name": "Lateral Ransomware Behavior",
        "when": ["suspicious_process", "smb_activity", "yara_match"],
        "severity": "critical",
    },
]
