from hunt.query_language import normalize_query


def parse(query: str):
    normalized = normalize_query(query)
    return [token for token in normalized.replace("(", " ").replace(")", " ").split(" ") if token]
