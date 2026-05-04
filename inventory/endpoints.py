from dataclasses import dataclass


@dataclass
class Endpoint:
    agent_id: str
    hostname: str
    os_name: str
    status: str = "active"
