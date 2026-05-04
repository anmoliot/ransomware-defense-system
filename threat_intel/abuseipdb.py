class AbuseIPDBConnector:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key

    def lookup_ip(self, ip: str):
        return {"source": "abuseipdb", "ip": ip, "status": "not_configured" if not self.api_key else "planned"}
