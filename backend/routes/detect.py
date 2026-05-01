import uuid
from datetime import datetime
from fastapi import APIRouter, BackgroundTasks
from ..models.schema import DetectionPayload, Alert, SystemState
from ..core.decision_engine import decision_engine
from ..core.state_manager import state_manager
from ..core.websocket_manager import ws_manager

router = APIRouter()

async def process_and_broadcast(alert: Alert):
    # This runs as a background task
    await ws_manager.broadcast_alert(alert.dict())

@router.post("/", response_model=dict)
async def handle_detection(payload: DetectionPayload, background_tasks: BackgroundTasks):
    # 1. Evaluate payload
    verdict = decision_engine.evaluate(payload)
    
    # 2. If it's a WARNING or ATTACK, register an alert
    if verdict.state in [SystemState.WARNING, SystemState.ATTACK]:
        # Update system state
        if verdict.state == SystemState.ATTACK or state_manager.get_state() != SystemState.ATTACK:
            state_manager.set_state(verdict.state)
            
        alert = Alert(
            id=str(uuid.uuid4()),
            timestamp=datetime.utcnow(),
            agent_id=payload.agent_id,
            verdict=verdict,
            payload_snapshot=payload
        )
        state_manager.add_alert(alert)
        
        # 3. Broadcast asynchronously
        background_tasks.add_task(process_and_broadcast, alert)

    return {
        "status": "success",
        "verdict": verdict
    }
