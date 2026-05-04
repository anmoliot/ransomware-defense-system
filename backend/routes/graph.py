from fastapi import APIRouter, Depends, Query

from backend.core.state_manager import state_manager
from backend.security.auth import User, require_role
from correlation.graph_builder import merge_alert_graphs
from graph.neo4j_engine import Neo4jEngine


router = APIRouter()


@router.get("/attack")
async def attack_graph(
    limit: int = Query(50, ge=1, le=1000),
    user: User = Depends(require_role("admin", "analyst", "viewer")),
):
    return merge_alert_graphs(state_manager.get_alerts(limit=limit))


@router.post("/neo4j/sync")
async def sync_neo4j(limit: int = 50, user: User = Depends(require_role("admin", "analyst"))):
    graph = merge_alert_graphs(state_manager.get_alerts(limit=limit))
    return Neo4jEngine().upsert_graph(graph)
