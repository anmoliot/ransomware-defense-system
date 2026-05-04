from threat_intel.ioc_matcher import ioc_matcher


def ingest_feed(items):
    hashes = [item["value"] for item in items if item.get("type") == "hash"]
    domains = [item["value"] for item in items if item.get("type") == "domain"]
    ips = [item["value"] for item in items if item.get("type") == "ip"]
    urls = [item["value"] for item in items if item.get("type") == "url"]
    ioc_matcher.load_indicators(hashes=hashes, domains=domains, ips=ips, urls=urls)
    return {"ingested": len(items)}
