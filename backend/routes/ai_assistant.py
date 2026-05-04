from fastapi import APIRouter, Depends

from ai_assistant.alert_explainer import explain_alert
from ai_assistant.remediation_suggestions import suggest_remediation
from backend.core.state_manager import state_manager
from backend.security.auth import User, require_role


router = APIRouter()


@router.get("/alerts/{alert_id}/explain")
async def explain(alert_id: str, user: User = Depends(require_role("admin", "analyst", "viewer"))):
    alert = state_manager.get_alert(alert_id)
    if not alert:
        return {"error": "alert_not_found"}
    return {**explain_alert(alert), "remediation": suggest_remediation(alert)}
