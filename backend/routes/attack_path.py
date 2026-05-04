from fastapi import APIRouter, Depends

from attack_path.attack_graph import build_path_graph
from attack_path.path_builder import build_attack_path
from backend.security.auth import User, require_role


router = APIRouter()


@router.post("/reconstruct")
async def reconstruct(events: list[dict], user: User = Depends(require_role("admin", "analyst", "viewer"))):
    path = build_attack_path(events)
    return {"path": path, "graph": build_path_graph(path)}
