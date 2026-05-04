def detect_impossible_travel(km_distance: float, hours_elapsed: float) -> bool:
    if hours_elapsed <= 0:
        return True
    return (km_distance / hours_elapsed) > 900
