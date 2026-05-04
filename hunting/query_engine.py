import operator
from typing import Iterable, List

from backend.models.schema import Alert


OPS = {
    ">": operator.gt,
    ">=": operator.ge,
    "<": operator.lt,
    "<=": operator.le,
    "=": operator.eq,
    ":": operator.eq,
}


class HuntQueryEngine:
    def search(self, alerts: Iterable[Alert], query: str, limit: int = 50) -> List[Alert]:
        clauses = [part.strip() for part in query.split(" and ") if part.strip()]
        results = []
        for alert in alerts:
            if all(self._matches(alert, clause) for clause in clauses):
                results.append(alert)
            if len(results) >= limit:
                break
        return results

    def _matches(self, alert: Alert, clause: str) -> bool:
        for op_text in (">=", "<=", ">", "<", ":", "="):
            if op_text in clause:
                field, expected = [part.strip() for part in clause.split(op_text, 1)]
                return self._compare(alert, field, op_text, expected)
        return clause.lower() in alert.json().lower()

    def _compare(self, alert: Alert, field: str, op_text: str, expected: str) -> bool:
        payload = alert.payload_snapshot
        if field == "risk_score":
            return OPS[op_text](alert.verdict.risk_score, int(expected))
        if field == "entropy" and payload:
            return OPS[op_text](payload.entropy, float(expected))
        if field == "file_rate" and payload:
            return OPS[op_text](payload.file_rate, float(expected))
        if field == "process_name" and payload:
            return any(process.name.lower() == expected.lower() for process in payload.processes)
        if field == "remote_port" and payload:
            return any(connection.remote_port == int(expected) for connection in payload.network_connections)
        if field == "network_beaconing":
            return expected.lower() == "true" and "suspicious_port" in " ".join(alert.verdict.signals)
        if field == "ioc_match":
            return expected.lower() == "true" and "ioc_match" in alert.verdict.signals
        if field == "state":
            return alert.verdict.state.lower() == expected.lower()
        return False


hunt_query_engine = HuntQueryEngine()
