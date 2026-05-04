TACTIC_WEIGHTS = {
    "Execution": 20,
    "Defense Evasion": 15,
    "Lateral Movement": 25,
    "Command and Control": 20,
    "Impact": 30,
}


def score_tactics(techniques):
    return min(100, sum(TACTIC_WEIGHTS.get(technique.tactic, 5) for technique in techniques))
