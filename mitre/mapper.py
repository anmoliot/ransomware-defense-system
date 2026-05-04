from typing import Iterable, List

from backend.models.schema import MitreTechnique


SIGNAL_TO_MITRE = {
    "canary_triggered": MitreTechnique(
        tactic="Impact",
        technique_id="T1486",
        technique="Data Encrypted for Impact",
    ),
    "high_entropy": MitreTechnique(
        tactic="Impact",
        technique_id="T1486",
        technique="Data Encrypted for Impact",
    ),
    "high_file_rate": MitreTechnique(
        tactic="Impact",
        technique_id="T1486",
        technique="Data Encrypted for Impact",
    ),
    "suspicious_extension_change": MitreTechnique(
        tactic="Impact",
        technique_id="T1486",
        technique="Data Encrypted for Impact",
    ),
    "agent_anomaly_score": MitreTechnique(
        tactic="Defense Evasion",
        technique_id="T1027",
        technique="Obfuscated Files or Information",
    ),
    "yara_match": MitreTechnique(
        tactic="Execution",
        technique_id="T1204",
        technique="User Execution",
    ),
    "ioc_match": MitreTechnique(
        tactic="Command and Control",
        technique_id="T1071",
        technique="Application Layer Protocol",
    ),
    "smb_activity": MitreTechnique(
        tactic="Lateral Movement",
        technique_id="T1021.002",
        technique="SMB/Windows Admin Shares",
    ),
}


def map_signals(signals: Iterable[str]) -> List[MitreTechnique]:
    mapped = {}
    for signal in signals:
        base_signal = signal.split(":", 1)[0]
        if base_signal == "suspicious_process" or base_signal == "suspicious_command":
            technique = MitreTechnique(
                tactic="Execution",
                technique_id="T1059",
                technique="Command and Scripting Interpreter",
            )
        elif base_signal == "suspicious_port":
            technique = MitreTechnique(
                tactic="Command and Control",
                technique_id="T1071",
                technique="Application Layer Protocol",
            )
        else:
            technique = SIGNAL_TO_MITRE.get(signal)

        if technique:
            mapped[technique.technique_id] = technique

    return list(mapped.values())
