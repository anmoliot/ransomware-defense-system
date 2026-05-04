class Neo4jEngine:
    def __init__(self, uri: str = "bolt://localhost:7687"):
        self.uri = uri

    def upsert_graph(self, graph):
        return {"backend": "neo4j", "uri": self.uri, "nodes": len(graph.nodes), "edges": len(graph.edges), "status": "planned"}
