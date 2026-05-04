def build_emulation_plan(profile):
    return {
        "profile": profile.get("name", "unknown"),
        "family": profile.get("family", "generic"),
        "steps": profile.get("steps", []),
        "destructive": False,
    }
