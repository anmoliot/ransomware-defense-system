class ModelRegistry:
    def __init__(self):
        self.models = {}

    def register(self, name: str, metadata: dict):
        self.models[name] = metadata
        return metadata


model_registry = ModelRegistry()
