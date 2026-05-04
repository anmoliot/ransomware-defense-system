def parse_protocol(packet):
    port = packet.get("dst_port")
    if port == 53:
        return "dns"
    if port in {80, 8080}:
        return "http"
    if port == 443:
        return "tls"
    if port in {445, 139}:
        return "smb"
    return packet.get("protocol", "unknown")
