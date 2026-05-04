def triage_incident(incident):
    score = incident.risk_score
    if score >= 90:
        return {"priority": "p1", "sla_minutes": 15, "recommended_status": "active_investigation"}
    if score >= 70:
        return {"priority": "p2", "sla_minutes": 60, "recommended_status": "assigned"}
    return {"priority": "p3", "sla_minutes": 240, "recommended_status": "queued"}
