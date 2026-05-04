from collections import Counter
from typing import Iterable, List


def detect_dga_domains(domains: Iterable[str]) -> List[str]:
    suspicious = []
    for domain in domains:
        label = domain.split(".", 1)[0].lower()
        if len(label) < 12:
            continue
        counts = Counter(label)
        unique_ratio = len(counts) / max(len(label), 1)
        digit_ratio = sum(char.isdigit() for char in label) / max(len(label), 1)
        if unique_ratio > 0.65 or digit_ratio > 0.25:
            suspicious.append(domain)
    return suspicious
