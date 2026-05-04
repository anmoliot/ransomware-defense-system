from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class SearchClause:
    field: str
    operator: str
    value: str


def parse_search(query: str) -> List[SearchClause]:
    clauses = []
    for part in query.split(" and "):
        text = part.strip()
        for op in (">=", "<=", ">", "<", ":", "="):
            if op in text:
                field, value = [item.strip() for item in text.split(op, 1)]
                clauses.append(SearchClause(field=field, operator=op, value=value))
                break
    return clauses
