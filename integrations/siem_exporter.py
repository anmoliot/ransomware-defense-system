import json
from datetime import datetime
from typing import Dict

from backend.models.schema import Alert


def alert_to_json(alert: Alert) -> Dict[str, object]:
    return json.loads(alert.json())


def alert_to_cef(alert: Alert) -> str:
    verdict = alert.verdict
    severity = _cef_severity(verdict.risk_score)
    reason = verdict.reason.replace("|", "/")
    return (
        "CEF:0|RansomwareDefense|EDR|1.0|"
        f"{verdict.state}|{reason}|{severity}|"
        f"rt={_millis(alert.timestamp)} suser={alert.agent_id} "
        f"cs1Label=RiskScore cs1={verdict.risk_score} "
        f"cs2Label=Signals cs2={','.join(verdict.signals)}"
    )


def alert_to_syslog(alert: Alert) -> str:
    payload = alert_to_json(alert)
    return f"<134>{datetime.utcnow().isoformat()} ransomware-defense {json.dumps(payload, separators=(',', ':'))}"


def _cef_severity(score: int) -> int:
    if score >= 90:
        return 10
    if score >= 70:
        return 8
    if score >= 40:
        return 5
    return 2


def _millis(value: datetime) -> int:
    return int(value.timestamp() * 1000)
