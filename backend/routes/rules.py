from fastapi import APIRouter, Depends

from backend.models.schema import DetectionPayload
from backend.security.auth import User, require_role
from rules.custom_rules import evaluate_custom_rules
from rules.correlation_rules import CORRELATION_RULES


router = APIRouter()


@router.get("/correlation")
async def list_correlation_rules(user: User = Depends(require_role("admin", "analyst", "viewer"))):
    return {"rules": CORRELATION_RULES}


@router.post("/evaluate")
async def evaluate_rules(payload: DetectionPayload, user: User = Depends(require_role("admin", "analyst"))):
    return {"matches": evaluate_custom_rules(payload)}
