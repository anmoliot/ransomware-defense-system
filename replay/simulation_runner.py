def run_simulation(plan):
    return {"plan": plan.get("profile", "unknown"), "steps": len(plan.get("steps", [])), "status": "simulated"}
