import subprocess
from datetime import datetime
from typing import List

from backend.models.schema import ProcessEvent


SUSPICIOUS_PROCESS_NAMES = {
    "powershell.exe",
    "pwsh.exe",
    "cmd.exe",
    "wmic.exe",
    "vssadmin.exe",
    "certutil.exe",
    "bitsadmin.exe",
    "rundll32.exe",
    "regsvr32.exe",
    "mshta.exe",
}


def collect_process_events() -> List[ProcessEvent]:
    """Collect process telemetry using psutil when available, with a Windows fallback."""
    try:
        import psutil  # type: ignore

        events = []
        for process in psutil.process_iter(["pid", "ppid", "name", "cmdline", "username"]):
            info = process.info
            name = info.get("name") or ""
            if name.lower() not in SUSPICIOUS_PROCESS_NAMES:
                continue
            cmdline = " ".join(info.get("cmdline") or [])
            parent_name = None
            try:
                parent = process.parent()
                parent_name = parent.name() if parent else None
            except Exception:
                parent_name = None
            events.append(
                ProcessEvent(
                    pid=info.get("pid"),
                    ppid=info.get("ppid"),
                    name=name,
                    command_line=cmdline,
                    parent_name=parent_name,
                    username=info.get("username"),
                    timestamp=datetime.utcnow(),
                )
            )
        return events
    except Exception:
        return _collect_with_tasklist()


def _collect_with_tasklist() -> List[ProcessEvent]:
    try:
        output = subprocess.check_output(
            ["tasklist", "/fo", "csv", "/nh"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        return []

    events = []
    for line in output.splitlines():
        parts = [part.strip('"') for part in line.split('","')]
        if not parts:
            continue
        name = parts[0]
        if name.lower() in SUSPICIOUS_PROCESS_NAMES:
            events.append(ProcessEvent(name=name, command_line=name, timestamp=datetime.utcnow()))
    return events
