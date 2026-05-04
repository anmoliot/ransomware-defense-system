from backend.models.schema import ResponseActionResult


def isolate_host(agent_id: str, dry_run: bool = True) -> ResponseActionResult:
    return ResponseActionResult(
        action="isolate_host",
        target=agent_id,
        status="planned" if dry_run else "submitted",
        detail="Host isolation command queued." if not dry_run else "Dry run: host would be isolated.",
    )


def kill_process(process_name: str, dry_run: bool = True) -> ResponseActionResult:
    return ResponseActionResult(
        action="kill_process",
        target=process_name,
        status="planned" if dry_run else "submitted",
        detail="Process termination command queued." if not dry_run else "Dry run: process would be terminated.",
    )


def export_iocs(alert_id: str, dry_run: bool = True) -> ResponseActionResult:
    return ResponseActionResult(
        action="export_iocs",
        target=alert_id,
        status="completed",
        detail="IOCs exported to integration queue." if not dry_run else "Dry run: IOCs would be exported.",
    )


def backup_logs(alert_id: str, dry_run: bool = True) -> ResponseActionResult:
    return ResponseActionResult(
        action="backup_logs",
        target=alert_id,
        status="completed",
        detail="Relevant telemetry copied to evidence store." if not dry_run else "Dry run: logs would be preserved.",
    )
