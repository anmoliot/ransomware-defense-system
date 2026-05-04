def collect_artifact_manifest(agent_id: str):
    return {
        "agent_id": agent_id,
        "artifacts": ["process_list", "network_connections", "recent_file_events", "autoruns"],
    }
