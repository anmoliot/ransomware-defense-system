PERSISTENCE_KEYS = ("run", "runonce", "services", "scheduled task", "startup")


def detect_persistence(entries):
    return [entry for entry in entries if any(key in str(entry).lower() for key in PERSISTENCE_KEYS)]
