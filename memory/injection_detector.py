from typing import Dict, List


def detect_injection_indicators(process_metadata: Dict[str, object]) -> List[str]:
    indicators = []
    if process_metadata.get("unsigned_module"):
        indicators.append("unsigned_module")
    if process_metadata.get("rx_private_memory"):
        indicators.append("rx_private_memory")
    if process_metadata.get("remote_thread"):
        indicators.append("remote_thread")
    return indicators
