def vectorize_payload(payload):
    return [
        payload.file_rate,
        payload.entropy,
        payload.extension_changes,
        1 if payload.canary_triggered else 0,
        len(payload.processes),
        len(payload.network_connections),
        len(payload.yara_matches),
        len(payload.ioc_matches),
    ]
