from typing import List

from backend.models.schema import Alert


def describe_attack_chain(alert: Alert) -> List[str]:
    chain = []
    payload = alert.payload_snapshot
    if not payload:
        return chain

    if payload.processes:
        chain.append("Execution")
    if payload.network_connections:
        chain.append("Command and Control or Lateral Movement")
    if payload.yara_matches or payload.ioc_matches:
        chain.append("Threat Intelligence Match")
    if payload.entropy >= 7.5 or payload.canary_triggered:
        chain.append("Impact")
    return chain
