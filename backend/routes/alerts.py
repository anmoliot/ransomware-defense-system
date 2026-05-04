from typing import List
from fastapi import APIRouter, Depends, Query
from ..core.audit_logger import audit_logger
from ..models.schema import Alert, SystemState
from ..core.state_manager import state_manager
from ..security.auth import User, require_role

router = APIRouter()

@router.get("/", response_model=List[Alert])
async def get_alerts(
    limit: int = Query(50, description="Max number of alerts to return"),
    user: User = Depends(require_role("admin", "analyst", "viewer")),
):
    """
    Returns the history of generated alerts.
    """
    audit_logger.log(user.username, "alerts.read", "alerts", "success", {"limit": limit})
    return state_manager.get_alerts(limit=limit)

@router.get("/status", response_model=dict)
async def get_system_status(user: User = Depends(require_role("admin", "analyst", "viewer"))):
    """
    Returns the current global system state.
    """
    audit_logger.log(user.username, "alerts.status", "system_state", "success")
    return {
        "state": state_manager.get_state()
    }
