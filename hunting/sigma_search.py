from hunting.sigma_converter import sigma_to_hunt_query


def sigma_search(alerts, rule_text, query_engine):
    compiled = sigma_to_hunt_query(rule_text)
    return query_engine.search(alerts, compiled["query"])
