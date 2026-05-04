from backend.models.schema import ResponseActionResult


def quarantine_file(path: str, dry_run: bool = True) -> ResponseActionResult:
    return ResponseActionResult(
        action="quarantine_file",
        target=path,
        status="planned" if dry_run else "submitted",
        detail="Dry run: file would be moved to quarantine." if dry_run else "Quarantine command queued.",
    )
