def detonate(file_path: str, dry_run: bool = True):
    return {"file": file_path, "dry_run": dry_run, "status": "planned" if dry_run else "submitted"}
