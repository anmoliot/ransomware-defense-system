def normalize_packet(packet):
    return {
        "src": packet.get("src"),
        "dst": packet.get("dst"),
        "dst_port": packet.get("dst_port"),
        "protocol": packet.get("protocol", "tcp"),
    }
