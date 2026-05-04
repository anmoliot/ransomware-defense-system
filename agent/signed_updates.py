def verify_update_signature(package_hash: str, trusted_hashes) -> bool:
    return package_hash in set(trusted_hashes)
