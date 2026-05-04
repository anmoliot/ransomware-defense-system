DEFAULT_HUNT_RULES = [
    {
        "name": "Suspicious PowerShell",
        "query": "process_name:powershell.exe",
        "severity": "medium",
    },
    {
        "name": "High Entropy Activity",
        "query": "entropy > 7",
        "severity": "high",
    },
    {
        "name": "SMB Propagation",
        "query": "remote_port:445",
        "severity": "high",
    },
    {
        "name": "Known IOC Match",
        "query": "ioc_match=true",
        "severity": "critical",
    },
]
