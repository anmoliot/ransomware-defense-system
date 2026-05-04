from agents.agent_registry import RegisteredAgent, agent_registry


def enroll_agent(agent_id: str, hostname: str, os_name: str, version: str = "1.0.0"):
    return agent_registry.register(RegisteredAgent(agent_id=agent_id, hostname=hostname, os_name=os_name, version=version))
