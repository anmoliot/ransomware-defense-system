def normalize_event_sequence(events):
    return [str(event).lower().strip() for event in events if str(event).strip()]
