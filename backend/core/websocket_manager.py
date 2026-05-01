from fastapi import WebSocket
from typing import List

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast_alert(self, alert_data: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json({
                    "type": "alert",
                    "data": alert_data
                })
            except Exception:
                # Connection might have dropped
                pass

# Singleton instance
ws_manager = ConnectionManager()
