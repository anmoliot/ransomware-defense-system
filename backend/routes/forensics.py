from fastapi import APIRouter, Depends, HTTPException

from backend.core.state_manager import state_manager
from backend.models.schema import ThreatGraph
from backend.security.auth import User, require_role
from forensics.lineage_builder import summarize_lineage
from forensics.process_tree import build_process_tree


router = APIRouter()


@router.get("/process-tree/{alert_id}", response_model=ThreatGraph)
async def get_process_tree(alert_id: str, user: User = Depends(require_role("admin", "analyst", "viewer"))):
    alert = state_manager.get_alert(alert_id)
    if not alert or not alert.payload_snapshot:
        raise HTTPException(status_code=404, detail="Alert or payload not found")
    return build_process_tree(alert.payload_snapshot)


@router.get("/lineage/{alert_id}")
async def get_lineage(alert_id: str, user: User = Depends(require_role("admin", "analyst", "viewer"))):
    alert = state_manager.get_alert(alert_id)
    if not alert or not alert.payload_snapshot:
        raise HTTPException(status_code=404, detail="Alert or payload not found")
    return {"alert_id": alert_id, "lineage": summarize_lineage(alert.payload_snapshot)}
