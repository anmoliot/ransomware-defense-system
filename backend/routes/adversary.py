from fastapi import APIRouter, Depends

from adversary.attack_orchestrator import build_emulation_plan
from backend.security.auth import User, require_role


router = APIRouter()


@router.post("/plan")
async def plan(profile: dict, user: User = Depends(require_role("admin", "analyst"))):
    return build_emulation_plan(profile)
