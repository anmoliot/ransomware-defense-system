def mitre_coverage(rules):
    techniques = set()
    for rule in rules:
        techniques.update(rule.get("mitre", []))
    return {"techniques": sorted(techniques), "count": len(techniques)}
