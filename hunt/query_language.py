OPERATORS = {"AND", "OR", ">", "<", ">=", "<=", ":", "="}


def normalize_query(query: str) -> str:
    return " ".join(query.strip().split())
