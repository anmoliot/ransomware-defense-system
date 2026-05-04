def detect_smb_lateral_movement(connections):
    smb_hosts = {connection.remote_address for connection in connections if connection.remote_port in {445, 139}}
    return len(smb_hosts) >= 3
