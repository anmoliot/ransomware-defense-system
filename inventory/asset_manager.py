from typing import Dict, List

from inventory.endpoints import Endpoint


class AssetManager:
    def __init__(self):
        self.endpoints: Dict[str, Endpoint] = {}

    def upsert(self, endpoint: Endpoint) -> None:
        self.endpoints[endpoint.agent_id] = endpoint

    def list(self) -> List[Endpoint]:
        return list(self.endpoints.values())


asset_manager = AssetManager()
