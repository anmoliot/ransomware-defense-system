from collections import deque
from typing import Deque, Dict, List


class TelemetryBuffer:
    def __init__(self, max_size: int = 10000):
        self.max_size = max_size
        self.events: Deque[Dict] = deque(maxlen=max_size)

    def append(self, event: Dict) -> None:
        self.events.append(event)

    def drain(self, limit: int = 100) -> List[Dict]:
        drained = []
        while self.events and len(drained) < limit:
            drained.append(self.events.popleft())
        return drained

    def size(self) -> int:
        return len(self.events)
