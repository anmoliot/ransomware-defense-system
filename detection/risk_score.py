from dataclasses import dataclass, field
from typing import List

from backend.models.schema import DetectionPayload


SUSPICIOUS_PROCESS_NAMES = {
    "powershell.exe",
    "pwsh.exe",
    "cmd.exe",
    "wmic.exe",
    "vssadmin.exe",
    "certutil.exe",
    "bitsadmin.exe",
    "rundll32.exe",
    "regsvr32.exe",
    "mshta.exe",
}

SUSPICIOUS_COMMAND_TOKENS = {
    "-enc",
    "-encodedcommand",
    "delete shadows",
    "shadowcopy delete",
    "bypass",
    "downloadstring",
    "frombase64string",
    "invoke-expression",
}

SUSPICIOUS_PORTS = {4444, 5555, 6667, 9001, 1337}


@dataclass
class RiskResult:
    score: int
    signals: List[str] = field(default_factory=list)


class RiskScorer:
    """Combines endpoint, network, deception, and intel signals into a 0-100 score."""

    def score(self, payload: DetectionPayload) -> RiskResult:
        score = 0
        signals: List[str] = []

        if payload.canary_triggered:
            score += 45
            signals.append("canary_triggered")

        if payload.entropy >= 7.5:
            score += 20
            signals.append("high_entropy")
        elif payload.entropy >= 6.8:
            score += 10
            signals.append("elevated_entropy")

        if payload.file_rate >= 5.0:
            score += 20
            signals.append("high_file_rate")
        elif payload.file_rate >= 2.0:
            score += 10
            signals.append("elevated_file_rate")

        if payload.extension_changes:
            score += min(15, payload.extension_changes * 5)
            signals.append("suspicious_extension_change")

        if payload.anomaly_score is not None:
            anomaly_points = int(max(0.0, min(payload.anomaly_score, 1.0)) * 25)
            score += anomaly_points
            if payload.anomaly_score >= 0.4:
                signals.append("agent_anomaly_score")

        for process in payload.processes:
            name = process.name.lower()
            command_line = process.command_line.lower()
            if name in SUSPICIOUS_PROCESS_NAMES:
                score += 10
                signals.append(f"suspicious_process:{name}")
            if any(token in command_line for token in SUSPICIOUS_COMMAND_TOKENS):
                score += 15
                signals.append(f"suspicious_command:{name}")

        for connection in payload.network_connections:
            if connection.remote_port in SUSPICIOUS_PORTS:
                score += 10
                signals.append(f"suspicious_port:{connection.remote_port}")
            if connection.remote_port in {445, 139}:
                score += 8
                signals.append("smb_activity")

        if payload.yara_matches:
            score += min(35, 20 + (len(payload.yara_matches) * 5))
            signals.append("yara_match")

        if payload.ioc_matches:
            score += min(35, 20 + (len(payload.ioc_matches) * 5))
            signals.append("ioc_match")

        for pattern in payload.suspicious_patterns:
            signals.append(f"pattern:{pattern}")
            score += 5

        return RiskResult(score=min(score, 100), signals=sorted(set(signals)))


risk_scorer = RiskScorer()
