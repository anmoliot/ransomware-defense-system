def build_behavior_report(file_path: str, observations):
    return {"file": file_path, "observations": observations, "verdict": "suspicious" if observations else "unknown"}
