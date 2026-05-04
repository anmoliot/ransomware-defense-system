from typing import List

from fastapi import APIRouter, Depends, Query

from backend.core.audit_logger import audit_logger
from backend.models.schema import AuditEvent
from backend.security.auth import User, require_role


router = APIRouter()


@router.get("/", response_model=List[AuditEvent])
async def get_audit_events(
    limit: int = Query(100, ge=1, le=1000),
    user: User = Depends(require_role("admin", "analyst")),
):
    audit_logger.log(user.username, "audit.read", "audit_events", "success", {"limit": limit})
    return audit_logger.list_events(limit)
