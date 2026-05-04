from hunting.sigma_converter import sigma_to_hunt_query


def compile_sigma_rules(rule_texts):
    return [sigma_to_hunt_query(rule_text) for rule_text in rule_texts]
