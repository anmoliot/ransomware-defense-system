from integrations.elastic import format_elastic_document


class ElasticConnector:
    def send(self, alert):
        return {"connector": "elastic", "status": "planned", "event": format_elastic_document(alert)}
