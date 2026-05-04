def normalize_auth_event(username: str, source_ip: str, success: bool):
    return {"username": username, "source_ip": source_ip, "success": success}
