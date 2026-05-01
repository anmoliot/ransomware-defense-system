from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import detect, alerts, websocket

app = FastAPI(
    title="Ransomware Defense Backend",
    description="Backend API for ransomware detection and alerting",
    version="1.0.0"
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
app.include_router(detect.router, prefix="/detect", tags=["Detection"])
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])
app.include_router(websocket.router, tags=["Real-time"])

@app.get("/")
async def root():
    return {"status": "ok", "message": "Ransomware Defense Backend is running"}
