from datetime import datetime
from typing import List

from backend.models.schema import NetworkConnection


def collect_network_connections() -> List[NetworkConnection]:
    """Collect endpoint network connections with psutil if it is installed."""
    try:
        import psutil  # type: ignore
    except Exception:
        return []

    connections: List[NetworkConnection] = []
    process_names = {}

    for conn in psutil.net_connections(kind="inet"):
        remote = conn.raddr if conn.raddr else None
        local = conn.laddr if conn.laddr else None
        if not remote:
            continue

        process_name = process_names.get(conn.pid)
        if process_name is None and conn.pid:
            try:
                process_name = psutil.Process(conn.pid).name()
            except Exception:
                process_name = ""
            process_names[conn.pid] = process_name

        connections.append(
            NetworkConnection(
                process_name=process_name or None,
                local_address=getattr(local, "ip", None),
                local_port=getattr(local, "port", None),
                remote_address=getattr(remote, "ip", None),
                remote_port=getattr(remote, "port", None),
                protocol="tcp",
                state=conn.status,
                timestamp=datetime.utcnow(),
            )
        )

    return connections
