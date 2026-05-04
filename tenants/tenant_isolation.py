def tenant_filter(records, tenant_id: str):
    return [record for record in records if record.get("tenant_id") == tenant_id]
