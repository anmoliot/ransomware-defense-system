from fastapi import APIRouter, Depends, Query

from backend.core.audit_logger import audit_logger
from backend.core.state_manager import state_manager
from backend.security.auth import User, require_role
from integrations.siem_exporter import alert_to_cef, alert_to_json, alert_to_syslog


router = APIRouter()


@router.get("/siem")
async def export_siem(
    format: str = Query("json", pattern="^(json|cef|syslog)$"),
    limit: int = Query(50, ge=1, le=1000),
    user: User = Depends(require_role("admin", "analyst")),
):
    alerts = state_manager.get_alerts(limit=limit)
    audit_logger.log(user.username, "siem.export", "alerts", "success", {"format": format, "limit": limit})
    if format == "cef":
        return {"format": format, "events": [alert_to_cef(alert) for alert in alerts]}
    if format == "syslog":
        return {"format": format, "events": [alert_to_syslog(alert) for alert in alerts]}
    return {"format": format, "events": [alert_to_json(alert) for alert in alerts]}
