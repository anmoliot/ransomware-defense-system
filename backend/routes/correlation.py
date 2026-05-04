from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query

from backend.core.state_manager import state_manager
from backend.models.schema import Incident, ThreatGraph
from backend.security.auth import User, require_role
from correlation.correlation_engine import correlation_engine
from correlation.event_graph import build_threat_graph


router = APIRouter()


@router.get("/incidents", response_model=List[Incident])
async def get_correlated_incidents(
    limit: int = Query(50, ge=1, le=1000),
    user: User = Depends(require_role("admin", "analyst", "viewer")),
):
    return correlation_engine.correlate(state_manager.get_alerts(limit=limit))


@router.get("/graph/{alert_id}", response_model=ThreatGraph)
async def get_attack_graph(alert_id: str, user: User = Depends(require_role("admin", "analyst", "viewer"))):
    alert = state_manager.get_alert(alert_id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return build_threat_graph(alert)
