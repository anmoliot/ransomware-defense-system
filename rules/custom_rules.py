from dataclasses import dataclass
from typing import List

from backend.models.schema import DetectionPayload


@dataclass(frozen=True)
class RuleMatch:
    name: str
    severity: str
    reason: str


def evaluate_custom_rules(payload: DetectionPayload) -> List[RuleMatch]:
    matches: List[RuleMatch] = []
    has_shell = any(process.name.lower() in {"powershell.exe", "cmd.exe"} for process in payload.processes)
    has_smb = any(connection.remote_port in {445, 139} for connection in payload.network_connections)
    if has_shell and has_smb and payload.entropy >= 7.0:
        matches.append(
            RuleMatch(
                name="PowerShell SMB Entropy Ransomware Chain",
                severity="critical",
                reason="PowerShell/cmd activity, SMB traffic, and entropy spike appeared together.",
            )
        )
    if payload.canary_triggered and payload.file_rate >= 2.0:
        matches.append(
            RuleMatch(
                name="Canary Trigger With File Burst",
                severity="critical",
                reason="Canary touched during elevated file activity.",
            )
        )
    return matches
