def replay_telemetry(events, publisher):
    ids = []
    for event in events:
        ids.append(publisher(event))
    return ids
