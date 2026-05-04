def detect_privilege_escalation(old_roles, new_roles) -> bool:
    return bool(set(new_roles) - set(old_roles))
