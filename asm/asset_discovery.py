def discover_assets(seed_hosts):
    return [{"host": host, "status": "known"} for host in seed_hosts]
