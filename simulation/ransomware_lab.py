def ransomware_scenario():
    return {
        "name": "safe_ransomware_emulation",
        "steps": ["spawn powershell", "touch canary", "rename files", "simulate high entropy writes"],
        "destructive": False,
    }
