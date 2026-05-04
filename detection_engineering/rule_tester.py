def test_rule(rule, fixture):
    required = set(rule.get("when", []))
    signals = set(fixture.get("signals", []))
    return {"rule": rule.get("name", "unnamed"), "matched": required.issubset(signals)}
