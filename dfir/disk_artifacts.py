SUSPICIOUS_PATH_MARKERS = ("startup", "temp", "appdata", "programdata", "tasks")


def analyze_disk_artifacts(paths):
    return [{"path": path, "suspicious": any(marker in path.lower() for marker in SUSPICIOUS_PATH_MARKERS)} for path in paths]
