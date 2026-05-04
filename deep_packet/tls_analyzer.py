def analyze_tls(handshake):
    return {
        "sni": handshake.get("sni"),
        "ja3": handshake.get("ja3"),
        "suspicious": handshake.get("ja3") in {"bad-ja3-demo"},
    }
