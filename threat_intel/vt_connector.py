class VirusTotalConnector:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key

    def lookup_hash(self, file_hash: str):
        return {"source": "virustotal", "hash": file_hash, "status": "not_configured" if not self.api_key else "planned"}
