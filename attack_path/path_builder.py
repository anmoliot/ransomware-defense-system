def build_attack_path(events):
    path = []
    text = " ".join(str(event).lower() for event in events)
    if "powershell" in text:
        path.append("initial execution")
    if "smb" in text or "445" in text:
        path.append("lateral movement")
    if "credential" in text:
        path.append("credential access")
    if "entropy" in text or "canary" in text:
        path.append("ransomware impact")
    return path
