def threat_surface_score(exposures, coverage_count: int):
    return max(0, min(100, len(exposures) * 15 - coverage_count * 5))
