import os

class AnomalyDetector:
    def __init__(self, entropy_threshold: float, file_rate_threshold: float):
        self.entropy_threshold = entropy_threshold
        self.file_rate_threshold = file_rate_threshold

    def evaluate(self, current_entropy: float, current_file_rate: float, canary_triggered: bool) -> float:
        """
        Evaluate anomaly score based on current metrics.
        Returns a score from 0.0 to 1.0.
        """
        score = 0.0

        if canary_triggered:
            return 1.0  # Absolute certainty of malicious activity

        # Weight factors
        entropy_weight = 0.6
        rate_weight = 0.4

        if current_entropy >= self.entropy_threshold:
            score += entropy_weight
        elif current_entropy > (self.entropy_threshold * 0.8):
            score += (entropy_weight * 0.5)

        if current_file_rate >= self.file_rate_threshold:
            score += rate_weight
        elif current_file_rate > (self.file_rate_threshold * 0.5):
            score += (rate_weight * 0.5)

        return min(score, 1.0)
