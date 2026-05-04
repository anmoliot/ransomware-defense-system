def summarize_incident(incident):
    techniques = ", ".join(technique.technique_id for technique in incident.techniques) or "no mapped techniques"
    return f"{incident.title} is {incident.severity} with risk {incident.risk_score}. Techniques: {techniques}."
