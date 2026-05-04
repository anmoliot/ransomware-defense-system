from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass
class RegisteredAgent:
    agent_id: str
    hostname: str
    os_name: str
    version: str
    status: str = "online"
    last_seen: datetime = field(default_factory=datetime.utcnow)


class AgentRegistry:
    def __init__(self):
        self.agents: Dict[str, RegisteredAgent] = {}

    def register(self, agent: RegisteredAgent) -> RegisteredAgent:
        self.agents[agent.agent_id] = agent
        return agent

    def heartbeat(self, agent_id: str) -> bool:
        agent = self.agents.get(agent_id)
        if not agent:
            return False
        agent.last_seen = datetime.utcnow()
        agent.status = "online"
        return True

    def list(self) -> List[RegisteredAgent]:
        return list(self.agents.values())


agent_registry = AgentRegistry()
