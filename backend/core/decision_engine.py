from ..models.schema import DetectionPayload, DecisionVerdict, SystemState

class DecisionEngine:
    def evaluate(self, payload: DetectionPayload) -> DecisionVerdict:
        """
        Takes the agent payload and produces a decision verdict.
        """
        # Critical priority: Canary triggered
        if payload.canary_triggered:
            return DecisionVerdict(
                state=SystemState.ATTACK,
                confidence=1.0,
                reason="Canary bait file was modified or deleted."
            )
            
        # Agent provided an explicit anomaly score
        if payload.anomaly_score is not None:
            if payload.anomaly_score >= 0.8:
                return DecisionVerdict(
                    state=SystemState.ATTACK,
                    confidence=payload.anomaly_score,
                    reason=f"Agent reported critical anomaly score: {payload.anomaly_score:.2f}"
                )
            elif payload.anomaly_score >= 0.4:
                return DecisionVerdict(
                    state=SystemState.WARNING,
                    confidence=payload.anomaly_score,
                    reason=f"Agent reported warning anomaly score: {payload.anomaly_score:.2f}"
                )

        # Fallback to backend heuristic rules
        if payload.entropy > 7.5 and payload.file_rate > 5.0:
            return DecisionVerdict(
                state=SystemState.ATTACK,
                confidence=0.9,
                reason="Simultaneous high entropy and rapid file modifications detected."
            )
        elif payload.extension_changes > 0:
            return DecisionVerdict(
                state=SystemState.WARNING,
                confidence=0.7,
                reason=f"Suspicious file extension changes detected: {payload.extension_changes}"
            )
        
        return DecisionVerdict(
            state=SystemState.NORMAL,
            confidence=1.0,
            reason="Telemetry within normal operational parameters."
        )

# Singleton instance
decision_engine = DecisionEngine()
