from typing import List
from fastapi import APIRouter, Query
from ..models.schema import Alert, SystemState
from ..core.state_manager import state_manager

router = APIRouter()

@router.get("/", response_model=List[Alert])
async def get_alerts(limit: int = Query(50, description="Max number of alerts to return")):
    """
    Returns the history of generated alerts.
    """
    return state_manager.get_alerts(limit=limit)

@router.get("/status", response_model=dict)
async def get_system_status():
    """
    Returns the current global system state.
    """
    return {
        "state": state_manager.get_state()
    }
