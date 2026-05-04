from typing import List

from fastapi import APIRouter, Depends, Query

from backend.core.state_manager import state_manager
from backend.models.schema import Incident
from backend.security.auth import User, require_role
from correlation.correlation_engine import correlation_engine


router = APIRouter()


@router.get("/", response_model=List[Incident])
async def list_incidents(
    limit: int = Query(50, ge=1, le=1000),
    user: User = Depends(require_role("admin", "analyst", "viewer")),
):
    return correlation_engine.correlate(state_manager.get_alerts(limit=limit))
