from backend.models.schema import Alert, GraphEdge, GraphNode, ThreatGraph
from forensics.process_tree import build_process_tree


def build_threat_graph(alert: Alert) -> ThreatGraph:
    payload = alert.payload_snapshot
    graph = build_process_tree(payload) if payload else ThreatGraph()
    nodes = {node.id: node for node in graph.nodes}
    edges = list(graph.edges)

    alert_node = GraphNode(id=f"alert:{alert.id}", label=alert.verdict.state, type="alert", risk=alert.verdict.risk_score)
    nodes[alert_node.id] = alert_node

    if payload:
        for process in payload.processes:
            process_id = f"process:{process.pid}" if process.pid is not None else f"process:{process.name.lower()}"
            edges.append(GraphEdge(source=process_id, target=alert_node.id, label="contributed_to"))

        for index, connection in enumerate(payload.network_connections):
            if not connection.remote_address:
                continue
            node_id = f"network:{connection.remote_address}:{connection.remote_port}:{index}"
            nodes[node_id] = GraphNode(
                id=node_id,
                label=f"{connection.remote_address}:{connection.remote_port}",
                type="network",
                risk=50 if connection.remote_port in {4444, 445, 139} else 20,
            )
            edges.append(GraphEdge(source=alert_node.id, target=node_id, label="observed"))

        for value in payload.ioc_matches + payload.yara_matches:
            node_id = f"ioc:{value}"
            nodes[node_id] = GraphNode(id=node_id, label=value, type="ioc", risk=90)
            edges.append(GraphEdge(source=node_id, target=alert_node.id, label="matched"))

    return ThreatGraph(nodes=list(nodes.values()), edges=edges)
