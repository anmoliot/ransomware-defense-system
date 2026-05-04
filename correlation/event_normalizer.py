from datetime import datetime
from typing import Any, Dict, Iterable, List

from backend.models.schema import Alert, DetectionPayload


def normalize_payload(payload: DetectionPayload) -> List[Dict[str, Any]]:
    events: List[Dict[str, Any]] = []
    base = {"agent_id": payload.agent_id, "timestamp": payload.timestamp.isoformat()}

    events.append({**base, "type": "file_metrics", "entropy": payload.entropy, "file_rate": payload.file_rate})
    if payload.canary_triggered:
        events.append({**base, "type": "canary", "name": "bait_file_touched"})

    for process in payload.processes:
        events.append({
            **base,
            "type": "process",
            "pid": process.pid,
            "ppid": process.ppid,
            "name": process.name,
            "command_line": process.command_line,
            "timestamp": process.timestamp.isoformat(),
        })

    for connection in payload.network_connections:
        events.append({
            **base,
            "type": "network",
            "process_name": connection.process_name,
            "remote_address": connection.remote_address,
            "remote_port": connection.remote_port,
            "timestamp": connection.timestamp.isoformat(),
        })

    for match in payload.yara_matches:
        events.append({**base, "type": "yara", "rule": match})
    for match in payload.ioc_matches:
        events.append({**base, "type": "ioc", "indicator": match})

    return sorted(events, key=lambda event: event.get("timestamp") or datetime.utcnow().isoformat())


def normalize_alerts(alerts: Iterable[Alert]) -> List[Dict[str, Any]]:
    normalized = []
    for alert in alerts:
        normalized.append({
            "type": "alert",
            "alert_id": alert.id,
            "agent_id": alert.agent_id,
            "risk_score": alert.verdict.risk_score,
            "state": alert.verdict.state,
            "timestamp": alert.timestamp.isoformat(),
        })
        if alert.payload_snapshot:
            normalized.extend(normalize_payload(alert.payload_snapshot))
    return normalized
