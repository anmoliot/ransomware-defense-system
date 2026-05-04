def build_killchain(techniques):
    return [f"{technique.tactic}:{technique.technique_id}" for technique in techniques]
