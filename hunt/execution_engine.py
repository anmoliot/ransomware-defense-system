from hunting.query_engine import HuntQueryEngine


def execute(query: str, alerts):
    converted = query.replace("process:", "process_name:").replace("AND", "and")
    return HuntQueryEngine().search(alerts, converted)
