def queue_automation(playbook: str, target: str):
    return {"playbook": playbook, "target": target, "status": "queued"}
