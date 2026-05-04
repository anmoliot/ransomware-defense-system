from fastapi import APIRouter, Depends

from backend.core.state_manager import state_manager
from backend.security.auth import User, require_role
from hunt.execution_engine import execute
from hunt.parser import parse


router = APIRouter()


@router.post("/parse")
async def parse_query(query: str, user: User = Depends(require_role("admin", "analyst", "viewer"))):
    return {"tokens": parse(query)}


@router.post("/execute")
async def execute_query(query: str, user: User = Depends(require_role("admin", "analyst"))):
    return {"alerts": execute(query, state_manager.get_alerts(limit=1000))}
