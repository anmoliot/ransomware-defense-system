from fastapi import APIRouter, Depends

from backend.core.audit_logger import audit_logger
from backend.core.state_manager import state_manager
from backend.security.auth import User, require_role
from compliance.compliance_reports import build_compliance_report


router = APIRouter()


@router.get("/report")
async def report(user: User = Depends(require_role("admin", "analyst"))):
    return build_compliance_report(
        alert_count=len(state_manager.get_alerts(limit=1000)),
        audit_count=len(audit_logger.list_events(limit=5000)),
    )
