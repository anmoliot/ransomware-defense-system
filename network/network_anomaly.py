from typing import Iterable, List

from backend.models.schema import NetworkConnection


def detect_network_anomalies(connections: Iterable[NetworkConnection]) -> List[str]:
    signals = []
    for connection in connections:
        if connection.remote_port in {4444, 5555, 6667, 9001, 1337}:
            signals.append(f"suspicious_port:{connection.remote_port}")
        if connection.remote_port in {445, 139}:
            signals.append("smb_activity")
    return sorted(set(signals))
