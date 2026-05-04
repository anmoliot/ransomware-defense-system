def detect_drift(current_mean: float, baseline_mean: float, tolerance: float = 0.25) -> bool:
    return abs(current_mean - baseline_mean) / max(abs(baseline_mean), 1) > tolerance
