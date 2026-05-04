from fastapi import APIRouter, Depends

from backend.security.auth import User, require_role
from sandbox.detonation import detonate
from sandbox.docker_sandbox import plan_container_detonation


router = APIRouter()


@router.post("/detonate")
async def detonate_file(file_path: str, dry_run: bool = True, user: User = Depends(require_role("admin", "analyst"))):
    if dry_run:
        return plan_container_detonation(file_path)
    return detonate(file_path, dry_run=False)
