class AnomalyStream:
    def __init__(self, threshold: int = 80):
        self.threshold = threshold
        self.latest = []

    def observe(self, risk_score: int):
        self.latest.append(risk_score)
        self.latest = self.latest[-100:]
        return risk_score >= self.threshold


anomaly_stream = AnomalyStream()
