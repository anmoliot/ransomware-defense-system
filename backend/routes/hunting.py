from fastapi import APIRouter, Depends

from backend.core.state_manager import state_manager
from backend.models.schema import HuntQuery
from backend.security.auth import User, require_role
from hunting.hunt_rules import DEFAULT_HUNT_RULES
from hunting.query_engine import hunt_query_engine
from hunting.sigma_converter import sigma_to_hunt_query


router = APIRouter()


@router.get("/rules")
async def list_hunt_rules(user: User = Depends(require_role("admin", "analyst", "viewer"))):
    return {"rules": DEFAULT_HUNT_RULES}


@router.post("/query")
async def run_hunt(request: HuntQuery, user: User = Depends(require_role("admin", "analyst"))):
    alerts = reversed(state_manager.get_alerts(limit=1000))
    matches = hunt_query_engine.search(alerts, request.query, request.limit)
    return {"query": request.query, "count": len(matches), "alerts": matches}


@router.post("/sigma/convert")
async def convert_sigma(rule_text: str, user: User = Depends(require_role("admin", "analyst"))):
    return sigma_to_hunt_query(rule_text)
