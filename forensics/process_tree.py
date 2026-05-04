from typing import Dict, List

from backend.models.schema import DetectionPayload, GraphEdge, GraphNode, ThreatGraph


def build_process_tree(payload: DetectionPayload) -> ThreatGraph:
    nodes: Dict[str, GraphNode] = {}
    edges: List[GraphEdge] = []

    for process in payload.processes:
        process_id = _process_id(process.pid, process.name)
        nodes[process_id] = GraphNode(
            id=process_id,
            label=process.name,
            type="process",
            risk=_process_risk(process.name, process.command_line),
        )

        if process.ppid or process.parent_name:
            parent_id = _process_id(process.ppid, process.parent_name or f"ppid:{process.ppid}")
            nodes.setdefault(
                parent_id,
                GraphNode(id=parent_id, label=process.parent_name or f"PID {process.ppid}", type="process"),
            )
            edges.append(GraphEdge(source=parent_id, target=process_id, label="spawned"))

    return ThreatGraph(nodes=list(nodes.values()), edges=edges)


def _process_id(pid: int | None, name: str | None) -> str:
    if pid is not None:
        return f"process:{pid}"
    return f"process:{(name or 'unknown').lower()}"


def _process_risk(name: str, command_line: str) -> int:
    lowered = f"{name} {command_line}".lower()
    score = 0
    if any(token in lowered for token in ("powershell", "cmd.exe", "wmic", "vssadmin", "certutil")):
        score += 45
    if any(token in lowered for token in ("encodedcommand", "-enc", "delete shadows", "downloadstring")):
        score += 45
    return min(score, 100)
