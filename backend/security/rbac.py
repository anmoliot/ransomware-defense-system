ROLE_PERMISSIONS = {
    "admin": {"read", "write", "respond", "export"},
    "analyst": {"read", "write", "export"},
    "viewer": {"read"},
}


def has_permission(role: str, permission: str) -> bool:
    return permission in ROLE_PERMISSIONS.get(role, set())
