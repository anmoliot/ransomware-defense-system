from fastapi import APIRouter, Depends

from agents.agent_registry import agent_registry
from agents.enrollment import enroll_agent
from agents.heartbeat_manager import mark_offline_stale
from agents.update_manager import plan_update
from backend.security.auth import User, require_role


router = APIRouter()


@router.post("/enroll")
async def enroll(payload: dict, user: User = Depends(require_role("admin", "analyst"))):
    agent = enroll_agent(
        agent_id=payload["agent_id"],
        hostname=payload.get("hostname", payload["agent_id"]),
        os_name=payload.get("os_name", "unknown"),
        version=payload.get("version", "1.0.0"),
    )
    return agent


@router.post("/{agent_id}/heartbeat")
async def heartbeat(agent_id: str):
    return {"agent_id": agent_id, "known": agent_registry.heartbeat(agent_id)}


@router.get("/")
async def list_agents(user: User = Depends(require_role("admin", "analyst", "viewer"))):
    return {"agents": mark_offline_stale(agent_registry.list())}


@router.post("/{agent_id}/updates")
async def update_agent(agent_id: str, version: str, user: User = Depends(require_role("admin"))):
    return plan_update(agent_id, version)
