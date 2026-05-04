def scan_exposure(services):
    return [service for service in services if service.get("risky")]
