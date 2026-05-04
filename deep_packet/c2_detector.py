def detect_c2(flow):
    return bool(flow.get("beaconing") or flow.get("tor") or flow.get("rare_domain"))
