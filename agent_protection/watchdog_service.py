def watchdog_status(last_heartbeat_seconds: int):
    return {"healthy": last_heartbeat_seconds < 60, "last_heartbeat_seconds": last_heartbeat_seconds}
