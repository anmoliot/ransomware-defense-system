from pathlib import Path


def plan_memory_dump(pid: int, output_dir: str | Path = "evidence"):
    return {"pid": pid, "output": str(Path(output_dir) / f"pid-{pid}.dmp"), "status": "planned"}
