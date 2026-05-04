from backend.models.schema import Alert, ResponseExecution
from response.remediation import backup_logs, export_iocs, isolate_host, kill_process


class ResponseOrchestrator:
    def execute_ransomware_playbook(self, alert: Alert, dry_run: bool = True) -> ResponseExecution:
        payload = alert.payload_snapshot
        results = [
            isolate_host(alert.agent_id, dry_run=dry_run),
            export_iocs(alert.id, dry_run=dry_run),
            backup_logs(alert.id, dry_run=dry_run),
        ]
        if payload:
            suspicious = [
                process.name
                for process in payload.processes
                if process.name.lower() in {"powershell.exe", "cmd.exe", "wmic.exe", "vssadmin.exe", "certutil.exe"}
            ]
            for process_name in sorted(set(suspicious)):
                results.append(kill_process(process_name, dry_run=dry_run))

        return ResponseExecution(
            playbook="ransomware_containment",
            alert_id=alert.id,
            dry_run=dry_run,
            results=results,
        )


response_orchestrator = ResponseOrchestrator()
