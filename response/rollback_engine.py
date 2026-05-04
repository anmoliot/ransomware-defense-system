from backend.models.schema import ResponseActionResult


def plan_file_rollback(agent_id: str, snapshot_id: str, dry_run: bool = True) -> ResponseActionResult:
    return ResponseActionResult(
        action="rollback_files",
        target=f"{agent_id}:{snapshot_id}",
        status="planned" if dry_run else "submitted",
        detail="Dry run: files would be restored." if dry_run else "Rollback submitted to agent.",
    )
