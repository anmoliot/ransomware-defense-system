SYSMON_EVENT_MAP = {
    1: "Process Create",
    3: "Network Connection",
    7: "Image Loaded",
    11: "File Create",
    13: "Registry Value Set",
}


def map_sysmon_event(event_id: int) -> str:
    return SYSMON_EVENT_MAP.get(event_id, "Unknown")
