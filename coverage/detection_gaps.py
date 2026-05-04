def find_gaps(required_techniques, covered_techniques):
    return sorted(set(required_techniques) - set(covered_techniques))
