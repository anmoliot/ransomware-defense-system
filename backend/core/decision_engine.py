from detection.risk_score import risk_scorer
from mitre.mapper import map_signals
from threat_intel.ioc_matcher import ioc_matcher
from ..models.schema import DetectionPayload, DecisionVerdict, SystemState

class DecisionEngine:
    def evaluate(self, payload: DetectionPayload) -> DecisionVerdict:
        """
        Takes the agent payload and produces a decision verdict.
        """
        intel_matches = ioc_matcher.match_payload(payload)
        if intel_matches:
            payload.ioc_matches.extend(match.value for match in intel_matches)

        risk = risk_scorer.score(payload)
        mitre_techniques = map_signals(risk.signals)

        # Critical priority: Canary triggered
        if payload.canary_triggered:
            return DecisionVerdict(
                state=SystemState.ATTACK,
                confidence=1.0,
                reason="Canary bait file was modified or deleted.",
                risk_score=max(risk.score, 95),
                mitre_techniques=mitre_techniques,
                signals=risk.signals,
            )

        if risk.score >= 80:
            return DecisionVerdict(
                state=SystemState.ATTACK,
                confidence=min(1.0, risk.score / 100.0),
                reason=f"High-confidence attack behavior detected with risk score {risk.score}.",
                risk_score=risk.score,
                mitre_techniques=mitre_techniques,
                signals=risk.signals,
            )

        if risk.score >= 40:
            return DecisionVerdict(
                state=SystemState.WARNING,
                confidence=min(0.95, max(0.4, risk.score / 100.0)),
                reason=f"Suspicious behavior detected with risk score {risk.score}.",
                risk_score=risk.score,
                mitre_techniques=mitre_techniques,
                signals=risk.signals,
            )

        # Fallback to backend heuristic rules
        if payload.entropy > 7.5 and payload.file_rate > 5.0:
            return DecisionVerdict(
                state=SystemState.ATTACK,
                confidence=0.9,
                reason="Simultaneous high entropy and rapid file modifications detected.",
                risk_score=max(risk.score, 80),
                mitre_techniques=mitre_techniques,
                signals=risk.signals,
            )
        elif payload.extension_changes > 0:
            return DecisionVerdict(
                state=SystemState.WARNING,
                confidence=0.7,
                reason=f"Suspicious file extension changes detected: {payload.extension_changes}",
                risk_score=max(risk.score, 40),
                mitre_techniques=mitre_techniques,
                signals=risk.signals,
            )
        
        return DecisionVerdict(
            state=SystemState.NORMAL,
            confidence=1.0,
            reason="Telemetry within normal operational parameters.",
            risk_score=risk.score,
            mitre_techniques=mitre_techniques,
            signals=risk.signals,
        )

# Singleton instance
decision_engine = DecisionEngine()
