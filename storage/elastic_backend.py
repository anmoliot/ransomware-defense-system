class ElasticBackend:
    def __init__(self, url: str = "http://localhost:9200"):
        self.url = url

    def index_alert(self, alert):
        return {"backend": "elastic", "url": self.url, "status": "planned", "id": getattr(alert, "id", None)}
