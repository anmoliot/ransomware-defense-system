def detect_shellcode(byte_markers):
    markers = set(byte_markers)
    suspicious = {"nop_sled", "private_rx", "api_hashing"}
    return sorted(markers & suspicious)
