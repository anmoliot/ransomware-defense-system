from collections import Counter


def summarize_flows(connections):
    ports = Counter(connection.remote_port for connection in connections if connection.remote_port)
    return {"remote_ports": dict(ports), "total": sum(ports.values())}
