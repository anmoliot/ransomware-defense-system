from fastapi import APIRouter, Depends

from backend.security.auth import User, require_role
from pipeline.queue_manager import queue_manager


router = APIRouter()


@router.post("/events")
async def publish_event(event: dict, user: User = Depends(require_role("admin", "analyst"))):
    return {"event_id": queue_manager.publish(event)}


@router.get("/stats")
async def queue_stats(user: User = Depends(require_role("admin", "analyst", "viewer"))):
    return queue_manager.stats()


@router.post("/consume")
async def consume(limit: int = 100, user: User = Depends(require_role("admin", "analyst"))):
    return {"events": queue_manager.consume(limit)}
