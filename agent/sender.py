import requests
from datetime import datetime

class Sender:
    def __init__(self, backend_url: str, agent_id: str):
        self.backend_url = backend_url
        self.agent_id = agent_id

    def send_payload(self, file_rate: float, entropy: float, canary_triggered: bool,
                     extension_changes: int, anomaly_score: float, processes=None,
                     network_connections=None, yara_matches=None, ioc_matches=None):
        payload = {
            "agent_id": self.agent_id,
            "timestamp": datetime.utcnow().isoformat(),
            "file_rate": file_rate,
            "entropy": entropy,
            "canary_triggered": canary_triggered,
            "extension_changes": extension_changes,
            "suspicious_patterns": [],
            "anomaly_score": anomaly_score,
            "processes": processes or [],
            "network_connections": network_connections or [],
            "yara_matches": yara_matches or [],
            "ioc_matches": ioc_matches or []
        }
        try:
            response = requests.post(f"{self.backend_url}/detect", json=payload, timeout=5)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Failed to send telemetry to backend: {e}")
            return False
