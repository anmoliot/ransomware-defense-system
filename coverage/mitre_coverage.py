def coverage_by_tactic(rules):
    tactics = {}
    for rule in rules:
        for tactic in rule.get("tactics", []):
            tactics[tactic] = tactics.get(tactic, 0) + 1
    return tactics
