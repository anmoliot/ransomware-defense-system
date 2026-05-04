RISKY_PORTS = {3389: "RDP", 445: "SMB", 22: "SSH", 5900: "VNC"}


def map_services(open_ports):
    return [{"port": port, "service": RISKY_PORTS.get(port, "unknown"), "risky": port in RISKY_PORTS} for port in open_ports]
