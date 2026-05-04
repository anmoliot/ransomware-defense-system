from fastapi import APIRouter, Depends, Query

from analytics.attack_predictor import predict_attack_probability
from analytics.realtime_analytics import summarize_alert_stream
from backend.core.state_manager import state_manager
from backend.security.auth import User, require_role


router = APIRouter()


@router.get("/stream-summary")
async def stream_summary(
    limit: int = Query(100, ge=1, le=1000),
    user: User = Depends(require_role("admin", "analyst", "viewer")),
):
    return summarize_alert_stream(state_manager.get_alerts(limit=limit))


@router.get("/predict/{alert_id}")
async def predict(alert_id: str, user: User = Depends(require_role("admin", "analyst", "viewer"))):
    alert = state_manager.get_alert(alert_id)
    if not alert:
        return {"error": "alert_not_found"}
    return {"alert_id": alert_id, "probability": predict_attack_probability(alert.verdict.signals)}
