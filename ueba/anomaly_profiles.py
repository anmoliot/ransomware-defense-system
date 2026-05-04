def profile_anomaly(current: float, baseline: float, tolerance: float = 2.0):
    return current > baseline * tolerance
