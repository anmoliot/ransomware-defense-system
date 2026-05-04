from typing import List


def scan_memory_with_yara(pid: int, rule_names=None) -> List[str]:
    rule_names = rule_names or []
    if pid <= 0:
        return ["invalid_pid"]
    return []
