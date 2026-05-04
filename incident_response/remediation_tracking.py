from dataclasses import dataclass
from typing import Dict


@dataclass
class RemediationTask:
    task_id: str
    incident_id: str
    action: str
    status: str = "open"


class RemediationTracker:
    def __init__(self):
        self.tasks: Dict[str, RemediationTask] = {}

    def create(self, task_id: str, incident_id: str, action: str) -> RemediationTask:
        task = RemediationTask(task_id=task_id, incident_id=incident_id, action=action)
        self.tasks[task_id] = task
        return task

    def complete(self, task_id: str) -> bool:
        task = self.tasks.get(task_id)
        if not task:
            return False
        task.status = "complete"
        return True


remediation_tracker = RemediationTracker()
