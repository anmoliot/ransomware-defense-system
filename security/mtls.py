def mtls_configured(cert_path: str | None, key_path: str | None, ca_path: str | None) -> bool:
    return bool(cert_path and key_path and ca_path)
