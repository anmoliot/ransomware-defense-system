from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import (
    alerts,
    agents,
    adversary,
    analytics,
    ai_assistant,
    asm,
    attack_path,
    audit,
    auth,
    compliance,
    correlation,
    detect,
    detection_engineering,
    dfir,
    forensics,
    graph,
    hunt_dsl,
    hunting,
    incident_response,
    incidents,
    integrations,
    pipeline,
    range,
    response,
    rules,
    sandbox,
    timeline,
    websocket,
)

app = FastAPI(
    title="Ransomware Defense Backend",
    description="Backend API for ransomware detection, alerting, auth, audit, and SIEM export",
    version="2.0.0"
)

# Allow CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(agents.router, prefix="/agents", tags=["Agents"])
app.include_router(adversary.router, prefix="/adversary", tags=["Adversary Emulation"])
app.include_router(ai_assistant.router, prefix="/ai-assistant", tags=["AI Analyst"])
app.include_router(asm.router, prefix="/asm", tags=["Attack Surface"])
app.include_router(attack_path.router, prefix="/attack-path", tags=["Attack Path"])
app.include_router(detect.router, prefix="/detect", tags=["Detection"])
app.include_router(detection_engineering.router, prefix="/detection-engineering", tags=["Detection Engineering"])
app.include_router(dfir.router, prefix="/dfir", tags=["DFIR"])
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])
app.include_router(audit.router, prefix="/audit", tags=["Audit"])
app.include_router(compliance.router, prefix="/compliance", tags=["Compliance"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
app.include_router(forensics.router, prefix="/forensics", tags=["Forensics"])
app.include_router(correlation.router, prefix="/correlation", tags=["Correlation"])
app.include_router(graph.router, prefix="/graph", tags=["Graph"])
app.include_router(hunting.router, prefix="/hunting", tags=["Threat Hunting"])
app.include_router(hunt_dsl.router, prefix="/hunt", tags=["Hunting DSL"])
app.include_router(incident_response.router, prefix="/incident-response", tags=["Incident Response"])
app.include_router(pipeline.router, prefix="/pipeline", tags=["Pipeline"])
app.include_router(range.router, prefix="/range", tags=["Cyber Range"])
app.include_router(response.router, prefix="/response", tags=["Response"])
app.include_router(sandbox.router, prefix="/sandbox", tags=["Sandbox"])
app.include_router(timeline.router, prefix="/timeline", tags=["Timeline"])
app.include_router(incidents.router, prefix="/incidents", tags=["Incidents"])
app.include_router(rules.router, prefix="/rules", tags=["Rules"])
app.include_router(integrations.router, prefix="/integrations", tags=["Integrations"])
app.include_router(websocket.router, tags=["Real-time"])

@app.get("/")
async def root():
    return {"status": "ok", "message": "Ransomware Defense Backend is running"}
