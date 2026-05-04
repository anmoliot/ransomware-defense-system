from backend.core.decision_engine import DecisionEngine
from backend.models.schema import DetectionPayload, NetworkConnection, ProcessEvent, SystemState
from backend.security.auth import authenticate_user, issue_token
from backend.security.jwt import decode_access_token
from integrations.siem_exporter import alert_to_cef
from backend.models.schema import Alert
from datetime import datetime


def test_decision_engine_scores_process_and_network_attack():
    payload = DetectionPayload(
        agent_id="endpoint-1",
        file_rate=6.0,
        extension_changes=2,
        entropy=7.8,
        anomaly_score=0.7,
        canary_triggered=False,
        processes=[
            ProcessEvent(
                name="powershell.exe",
                command_line="powershell.exe -EncodedCommand AAAA",
            )
        ],
        network_connections=[
            NetworkConnection(remote_address="203.0.113.99", remote_port=4444)
        ],
    )

    verdict = DecisionEngine().evaluate(payload)

    assert verdict.state == SystemState.ATTACK
    assert verdict.risk_score >= 80
    assert "high_entropy" in verdict.signals
    assert "ioc_match" in verdict.signals
    assert any(item.technique_id == "T1059" for item in verdict.mitre_techniques)


def test_jwt_login_round_trip():
    user = authenticate_user("admin", "admin123")

    assert user is not None
    token = issue_token(user)
    payload = decode_access_token(token)

    assert payload["sub"] == "admin"
    assert payload["role"] == "admin"


def test_cef_export_contains_risk_score():
    payload = DetectionPayload(
        agent_id="endpoint-2",
        file_rate=10.0,
        extension_changes=1,
        entropy=8.0,
        canary_triggered=True,
    )
    verdict = DecisionEngine().evaluate(payload)
    alert = Alert(
        id="alert-1",
        timestamp=datetime.utcnow(),
        agent_id=payload.agent_id,
        verdict=verdict,
        payload_snapshot=payload,
    )

    cef = alert_to_cef(alert)

    assert cef.startswith("CEF:0|RansomwareDefense|EDR|1.0|")
    assert "cs1Label=RiskScore" in cef
