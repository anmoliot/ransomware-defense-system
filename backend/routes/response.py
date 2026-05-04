from fastapi import APIRouter, Depends, HTTPException, Query

from backend.core.audit_logger import audit_logger
from backend.core.state_manager import state_manager
from backend.models.schema import ResponseExecution
from backend.security.auth import User, require_role
from response.orchestrator import response_orchestrator


router = APIRouter()


@router.post("/playbooks/ransomware/{alert_id}", response_model=ResponseExecution)
async def execute_ransomware_playbook(
    alert_id: str,
    dry_run: bool = Query(True),
    user: User = Depends(require_role("admin", "analyst")),
):
    alert = state_manager.get_alert(alert_id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    execution = response_orchestrator.execute_ransomware_playbook(alert, dry_run=dry_run)
    audit_logger.log(
        user.username,
        "response.playbook",
        alert_id,
        "dry_run" if dry_run else "submitted",
        {"playbook": execution.playbook, "actions": [result.action for result in execution.results]},
    )
    return execution
