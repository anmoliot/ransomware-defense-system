from typing import List

from backend.models.schema import DetectionPayload


def summarize_lineage(payload: DetectionPayload) -> List[str]:
    summaries = []
    for process in payload.processes:
        parent = process.parent_name or (f"PID {process.ppid}" if process.ppid else "unknown parent")
        summaries.append(f"{parent} -> {process.name}")
    return summaries
