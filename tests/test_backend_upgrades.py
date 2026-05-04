from tests.test_phase3 import make_attack_alert

from agents.enrollment import enroll_agent
from correlation.event_normalizer import normalize_alerts
from correlation.graph_builder import merge_alert_graphs
from incidents.incident_store import IncidentStore
from ml.inference import predict_risk
from pipeline.queue_manager import QueueManager
from sandbox.detonation import detonate
from security.telemetry_signing import sign_payload, verify_signature


def test_queue_manager_buffers_and_consumes_events():
    queue = QueueManager()
    event_id = queue.publish({"type": "telemetry", "agent_id": "endpoint-1"})

    assert queue.stats()["queued"] == 1
    assert queue.consume()[0]["id"] == event_id
    assert queue.stats()["queued"] == 0


def test_normalization_and_graph_merge():
    alert = make_attack_alert()
    events = normalize_alerts([alert])
    graph = merge_alert_graphs([alert])

    assert any(event["type"] == "process" for event in events)
    assert any(node.type == "endpoint" for node in graph.nodes)
    assert graph.edges


def test_incident_store_deduplicates_alert_ids():
    alert = make_attack_alert()
    incident = __import__("correlation.correlation_engine", fromlist=["CorrelationEngine"]).CorrelationEngine().correlate([alert])[0]
    store = IncidentStore()

    store.upsert(incident)
    store.upsert(incident)

    assert len(store.list()) == 1
    assert store.list()[0].alert_ids == ["phase3-alert"]


def test_signed_telemetry_round_trip():
    payload = {"agent_id": "endpoint-1", "risk": 90}
    signature = sign_payload(payload, "secret")

    assert verify_signature(payload, "secret", signature)
    assert not verify_signature(payload, "wrong", signature)


def test_ml_sandbox_and_agent_management_adapters():
    alert = make_attack_alert()
    agent = enroll_agent("endpoint-upgrade", "host-a", "Windows", "2.0.0")

    assert agent.agent_id == "endpoint-upgrade"
    assert predict_risk(alert.payload_snapshot)["risk_score"] > 80
    assert detonate("sample.exe", dry_run=True)["status"] == "planned"
