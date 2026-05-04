from tests.test_phase3 import make_attack_alert

from adversary.attack_orchestrator import build_emulation_plan
from ai_assistant.alert_explainer import explain_alert
from attack_path.path_builder import build_attack_path
from coverage.detection_gaps import find_gaps
from cyber_range.range_builder import build_range
from detection.threat_score_v2 import contextual_score
from detection_engineering.rule_tester import test_rule
from detection_engineering.rule_validator import validate_rule
from dfir.malware_artifact_extractor import extract_artifact_indicators
from dfir.persistence_analyzer import detect_persistence
from hunt.parser import parse
from incident_response.case_management import CaseManager
from incident_response.evidence_chain import EvidenceChain
from replay.attack_replay import replay_attack
from sandbox.detonation_engine import run_detonation
from ueba.insider_threat import insider_risk


def test_incident_response_case_and_evidence_chain():
    manager = CaseManager()
    evidence = EvidenceChain()

    case = manager.assign("inc-1", "analyst")
    item = evidence.add("process-list", "json", b"{}", "analyst")

    assert case.owner == "analyst"
    assert item.hash_sha256


def test_dfir_detection_engineering_and_ai_helpers():
    alert = make_attack_alert()
    rule = {"name": "ransomware-chain", "when": ["canary_triggered"], "severity": "critical", "mitre": ["T1486"]}

    assert "ransom_note" in extract_artifact_indicators("Your files are encrypted. Pay bitcoin to decrypt files.")
    assert detect_persistence(["HKCU Run key"])
    assert validate_rule(rule)["valid"]
    assert test_rule(rule, {"signals": alert.verdict.signals})["matched"]
    assert explain_alert(alert)["risk_score"] >= 80


def test_attack_path_hunt_dsl_scoring_and_replay():
    alert = make_attack_alert()
    events = [{"name": "powershell"}, {"port": 445, "label": "SMB"}, {"name": "canary"}]

    assert build_attack_path(events) == ["initial execution", "lateral movement", "ransomware impact"]
    assert "process:powershell.exe" in parse("process:powershell.exe AND entropy > 7")
    assert contextual_score(alert, user_risk=50, asset_criticality=80) >= 70
    assert replay_attack(events)[0]["sequence"] == 0


def test_adversary_sandbox_ueba_coverage_and_range():
    plan = build_emulation_plan({"name": "LockBit Safe", "family": "LockBit", "steps": ["execute", "encrypt"]})

    assert plan["destructive"] is False
    assert run_detonation("sample.exe", dry_run=True)["result"]["status"] == "planned"
    assert insider_risk(["bulk_download", "privilege_escalation"]) >= 70
    assert find_gaps(["T1059", "T1486"], ["T1059"]) == ["T1486"]
    assert build_range("training", 4)["hosts"] == 4
