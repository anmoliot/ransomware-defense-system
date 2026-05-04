from typing import List

from fastapi import APIRouter, Depends, HTTPException

from backend.core.state_manager import state_manager
from backend.models.schema import TimelineEvent
from backend.security.auth import User, require_role
from timeline.timeline_builder import build_alert_timeline


router = APIRouter()


@router.get("/alerts/{alert_id}", response_model=List[TimelineEvent])
async def get_alert_timeline(alert_id: str, user: User = Depends(require_role("admin", "analyst", "viewer"))):
    alert = state_manager.get_alert(alert_id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return build_alert_timeline(alert)
