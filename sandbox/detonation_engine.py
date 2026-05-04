from sandbox.detonation import detonate
from sandbox.malware_vm import plan_vm


def run_detonation(file_path: str, dry_run: bool = True):
    plan = plan_vm(file_path)
    result = detonate(file_path, dry_run=dry_run)
    return {"plan": plan, "result": result}
