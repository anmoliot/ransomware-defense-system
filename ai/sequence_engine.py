ATTACK_SEQUENCE = ["powershell", "persistence", "smb", "encryption"]


def score_sequence(events):
    joined = " ".join(events).lower()
    hits = sum(1 for item in ATTACK_SEQUENCE if item in joined)
    return int((hits / len(ATTACK_SEQUENCE)) * 100)
