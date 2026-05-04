from dataclasses import dataclass


@dataclass(frozen=True)
class ReputationResult:
    value: str
    score: int
    verdict: str


def score_indicator(value: str, matched_ioc: bool = False, signed: bool | None = None) -> ReputationResult:
    score = 0
    if matched_ioc:
        score += 80
    if signed is False:
        score += 20

    score = min(score, 100)
    if score >= 80:
        verdict = "malicious"
    elif score >= 40:
        verdict = "suspicious"
    else:
        verdict = "unknown"

    return ReputationResult(value=value, score=score, verdict=verdict)
