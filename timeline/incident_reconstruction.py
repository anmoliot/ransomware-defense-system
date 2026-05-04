from timeline.event_ordering import order_events


def reconstruct_incident(incident):
    return {
        "incident_id": incident.id,
        "title": incident.title,
        "events": order_events(incident.timeline),
        "techniques": [technique.technique_id for technique in incident.techniques],
    }
