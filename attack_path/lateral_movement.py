def detect_lateral_path(connections):
    hosts = [connection.remote_address for connection in connections if connection.remote_port in {445, 139}]
    return {"lateral_movement": len(set(hosts)) >= 2, "hosts": sorted(set(hosts))}
