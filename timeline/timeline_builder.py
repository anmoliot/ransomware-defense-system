from typing import List

from backend.models.schema import Alert, TimelineEvent
from timeline.event_timeline import alert_summary_event, make_event


def build_alert_timeline(alert: Alert) -> List[TimelineEvent]:
    events = [alert_summary_event(alert)]
    payload = alert.payload_snapshot
    if not payload:
        return events

    for process in payload.processes:
        events.append(
            make_event(
                "process",
                f"{process.name} launched",
                process.command_line or process.name,
                "warning" if process.name.lower() in {"powershell.exe", "cmd.exe"} else "info",
                timestamp=process.timestamp,
                mitre="T1059",
            )
        )

    if payload.canary_triggered:
        events.append(
            make_event(
                "deception",
                "Canary file touched",
                "A bait file was modified or deleted.",
                "critical",
                timestamp=alert.timestamp,
                mitre="T1486",
            )
        )

    for connection in payload.network_connections:
        if connection.remote_address:
            events.append(
                make_event(
                    "network",
                    f"Outbound connection to {connection.remote_address}",
                    f"Remote port {connection.remote_port} via {connection.process_name or 'unknown process'}",
                    "warning" if connection.remote_port in {4444, 5555, 6667, 9001, 1337, 445, 139} else "info",
                    timestamp=connection.timestamp,
                    mitre="T1071",
                )
            )

    return sorted(events, key=lambda event: event.timestamp)
