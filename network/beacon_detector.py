def detect_beaconing(intervals, tolerance: float = 0.15):
    if len(intervals) < 4:
        return False
    avg = sum(intervals) / len(intervals)
    return all(abs(interval - avg) / max(avg, 1) <= tolerance for interval in intervals)
