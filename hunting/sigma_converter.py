from typing import Dict


def sigma_to_hunt_query(rule_text: str) -> Dict[str, str]:
    """Convert a small useful subset of Sigma YAML into this project's hunt query language."""
    title = "Sigma Rule"
    query_parts = []

    for raw_line in rule_text.splitlines():
        line = raw_line.strip()
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip()
        elif "Image|" in line or line.startswith("Image:"):
            value = line.split(":", 1)[1].strip().strip("'\"")
            image_name = value.replace("/", "\\").split("\\")[-1]
            query_parts.append(f"process_name:{image_name}")
        elif "CommandLine|contains:" in line:
            value = line.split(":", 1)[1].strip().strip("'\"")
            query_parts.append(value)

    return {"title": title, "query": " and ".join(query_parts) if query_parts else rule_text}
