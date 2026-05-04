def detect_sandbox_evasion(behaviors):
    markers = {"sleep_loop", "mouse_check", "process_count_check", "vm_artifact_check"}
    return sorted(set(behaviors) & markers)
