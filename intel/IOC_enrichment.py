def enrich_ioc(value: str, indicator_type: str):
    return {"value": value, "type": indicator_type, "confidence": 50, "sources": ["local"]}
