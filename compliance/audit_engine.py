def summarize_audit(events):
    return {"count": len(events), "actions": sorted({event.action for event in events})}
