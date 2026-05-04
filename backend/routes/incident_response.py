from fastapi import APIRouter, Depends

from backend.security.auth import User, require_role
from incident_response.analyst_notes import analyst_notebook
from incident_response.case_management import case_manager
from incident_response.remediation_tracking import remediation_tracker


router = APIRouter()


@router.post("/cases/{incident_id}/assign")
async def assign_case(incident_id: str, owner: str, user: User = Depends(require_role("admin", "analyst"))):
    return case_manager.assign(incident_id, owner)


@router.post("/cases/{incident_id}/notes")
async def add_note(incident_id: str, body: str, user: User = Depends(require_role("admin", "analyst"))):
    return analyst_notebook.add(incident_id, user.username, body)


@router.post("/cases/{incident_id}/remediation")
async def add_remediation(incident_id: str, task_id: str, action: str, user: User = Depends(require_role("admin", "analyst"))):
    return remediation_tracker.create(task_id, incident_id, action)
