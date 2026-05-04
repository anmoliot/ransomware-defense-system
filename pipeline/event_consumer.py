from typing import Callable, Dict, List

from pipeline.queue_manager import queue_manager


def consume_events(handler: Callable[[Dict], None], limit: int = 100) -> List[str]:
    processed = []
    for event in queue_manager.consume(limit):
        handler(event)
        processed.append(event["id"])
    return processed
