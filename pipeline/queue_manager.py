import uuid
from datetime import datetime
from typing import Dict

from pipeline.telemetry_buffer import TelemetryBuffer


class QueueManager:
    def __init__(self):
        self.buffer = TelemetryBuffer()

    def publish(self, event: Dict) -> str:
        event_id = event.get("id") or str(uuid.uuid4())
        self.buffer.append({**event, "id": event_id, "queued_at": datetime.utcnow().isoformat()})
        return event_id

    def consume(self, limit: int = 100):
        return self.buffer.drain(limit)

    def stats(self):
        return {"backend": "in_memory", "queued": self.buffer.size()}


queue_manager = QueueManager()
