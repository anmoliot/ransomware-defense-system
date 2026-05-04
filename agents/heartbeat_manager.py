from datetime import datetime, timedelta


def mark_offline_stale(agents, stale_minutes: int = 5):
    cutoff = datetime.utcnow() - timedelta(minutes=stale_minutes)
    for agent in agents:
        if agent.last_seen < cutoff:
            agent.status = "offline"
    return agents
