def extract_behavior(observations):
    behavior = []
    text = " ".join(map(str, observations)).lower()
    if "file write" in text:
        behavior.append("file_modification")
    if "network" in text:
        behavior.append("network_activity")
    if "registry" in text:
        behavior.append("persistence_attempt")
    return behavior
