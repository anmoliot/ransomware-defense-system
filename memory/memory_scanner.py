from typing import List


def scan_process_memory(pid: int) -> List[str]:
    """Placeholder adapter for Volatility/YARA memory scanning integrations."""
    if pid <= 0:
        return ["invalid_pid"]
    return []
