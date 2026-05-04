def validate_rule(rule):
    errors = []
    if "name" not in rule:
        errors.append("missing_name")
    if "when" not in rule:
        errors.append("missing_when")
    if "severity" not in rule:
        errors.append("missing_severity")
    return {"valid": not errors, "errors": errors}
