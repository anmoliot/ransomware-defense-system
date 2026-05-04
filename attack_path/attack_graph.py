from backend.models.schema import GraphEdge, GraphNode, ThreatGraph


def build_path_graph(steps):
    nodes = [GraphNode(id=f"step:{index}", label=step, type="attack_step", risk=min(100, 20 + index * 15)) for index, step in enumerate(steps)]
    edges = [GraphEdge(source=nodes[index].id, target=nodes[index + 1].id, label="then") for index in range(len(nodes) - 1)]
    return ThreatGraph(nodes=nodes, edges=edges)
