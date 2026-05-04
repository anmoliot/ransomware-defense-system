def tenant_scope(organization_id: str, resource: str) -> str:
    return f"{organization_id}:{resource}"
