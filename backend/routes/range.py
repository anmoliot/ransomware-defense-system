from fastapi import APIRouter, Depends

from backend.security.auth import User, require_role
from cyber_range.blue_team_scenario import blue_team_objectives
from cyber_range.range_builder import build_range
from cyber_range.red_team_scenario import red_team_plan
from replay.attack_replay import replay_attack


router = APIRouter()


@router.post("/build")
async def build(name: str, hosts: int = 3, user: User = Depends(require_role("admin", "analyst"))):
    return {**build_range(name, hosts), "blue_team": blue_team_objectives(), "red_team": red_team_plan()}


@router.post("/replay")
async def replay(events: list[dict], user: User = Depends(require_role("admin", "analyst"))):
    return {"events": replay_attack(events)}
