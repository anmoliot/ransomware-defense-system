TENANT_ROLES = {
    "owner": {"admin", "analyst", "viewer"},
    "analyst": {"analyst", "viewer"},
    "viewer": {"viewer"},
}


def allowed_roles(role: str):
    return TENANT_ROLES.get(role, set())
