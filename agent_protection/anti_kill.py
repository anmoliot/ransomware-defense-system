def anti_kill_policy():
    return {"restart_on_exit": True, "protected_process": "planned", "requires_admin": True}
