def replay_attack(events):
    return [{"sequence": index, "event": event} for index, event in enumerate(events)]
