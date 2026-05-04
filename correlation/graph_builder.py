from typing import Iterable

from backend.models.schema import Alert, GraphEdge, GraphNode, ThreatGraph
from correlation.event_graph import build_threat_graph


def merge_alert_graphs(alerts: Iterable[Alert]) -> ThreatGraph:
    nodes = {}
    edges = []
    for alert in alerts:
        graph = build_threat_graph(alert)
        for node in graph.nodes:
            nodes[node.id] = node
        edges.extend(graph.edges)

    agents = {alert.agent_id for alert in alerts}
    for agent_id in agents:
        node_id = f"agent:{agent_id}"
        nodes[node_id] = GraphNode(id=node_id, label=agent_id, type="endpoint", risk=20)
        for alert in alerts:
            if alert.agent_id == agent_id:
                edges.append(GraphEdge(source=node_id, target=f"alert:{alert.id}", label="reported"))

    return ThreatGraph(nodes=list(nodes.values()), edges=edges)
