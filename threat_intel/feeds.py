from threat_intel.ioc_matcher import ioc_matcher


def load_local_demo_feeds() -> None:
    """Seeds the local matcher; external feed clients can extend this function later."""
    ioc_matcher.load_indicators(
        hashes=(),
        domains=("malicious.example", "ransomware-c2.example"),
        ips=("10.255.255.66", "203.0.113.99"),
        urls=(),
    )
