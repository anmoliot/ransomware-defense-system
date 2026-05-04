from backend.models.schema import Alert, DetectionPayload, NetworkConnection, ProcessEvent, SystemState
from backend.core.decision_engine import DecisionEngine
from correlation.correlation_engine import CorrelationEngine
from forensics.process_tree import build_process_tree
from hunting.query_engine import HuntQueryEngine
from response.orchestrator import ResponseOrchestrator
from rules.custom_rules import evaluate_custom_rules
from timeline.timeline_builder import build_alert_timeline
from datetime import datetime


def make_attack_alert():
    payload = DetectionPayload(
        agent_id="endpoint-phase3",
        file_rate=8.0,
        extension_changes=3,
        entropy=7.9,
        anomaly_score=0.8,
        canary_triggered=True,
        processes=[
            ProcessEvent(pid=100, ppid=50, name="powershell.exe", command_line="powershell -EncodedCommand AAA"),
            ProcessEvent(pid=101, ppid=100, parent_name="powershell.exe", name="cmd.exe", command_line="cmd /c encryptor.exe"),
        ],
        network_connections=[
            NetworkConnection(process_name="cmd.exe", remote_address="203.0.113.99", remote_port=445)
        ],
        yara_matches=["Shadow_Copy_Delete"],
    )
    verdict = DecisionEngine().evaluate(payload)
    return Alert(
        id="phase3-alert",
        timestamp=datetime.utcnow(),
        agent_id=payload.agent_id,
        verdict=verdict,
        payload_snapshot=payload,
    )


def test_process_tree_builds_parent_child_edges():
    alert = make_attack_alert()
    graph = build_process_tree(alert.payload_snapshot)

    assert any(node.label == "powershell.exe" for node in graph.nodes)
    assert any(edge.label == "spawned" for edge in graph.edges)


def test_correlation_creates_incident_with_graph_and_timeline():
    alert = make_attack_alert()
    incidents = CorrelationEngine().correlate([alert])

    assert len(incidents) == 1
    assert incidents[0].severity == "critical"
    assert incidents[0].graph.nodes
    assert incidents[0].timeline


def test_hunting_query_matches_process_and_entropy():
    alert = make_attack_alert()
    matches = HuntQueryEngine().search([alert], "process_name:powershell.exe and entropy > 7", 10)

    assert matches == [alert]


def test_response_playbook_is_safe_dry_run():
    alert = make_attack_alert()
    execution = ResponseOrchestrator().execute_ransomware_playbook(alert, dry_run=True)

    assert execution.dry_run is True
    assert any(result.action == "isolate_host" for result in execution.results)
    assert all(result.status in {"planned", "completed"} for result in execution.results)


def test_rules_and_timeline_capture_ransomware_chain():
    alert = make_attack_alert()
    matches = evaluate_custom_rules(alert.payload_snapshot)
    timeline = build_alert_timeline(alert)

    assert alert.verdict.state == SystemState.ATTACK
    assert matches
    assert any(event.event_type == "deception" for event in timeline)
