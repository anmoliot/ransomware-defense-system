from hunting.search_parser import parse_search


def search_documents(documents, query: str):
    clauses = parse_search(query)
    matches = []
    for document in documents:
        if all(str(document.get(clause.field, "")).lower() == clause.value.lower() for clause in clauses if clause.operator in {":", "="}):
            matches.append(document)
    return matches
