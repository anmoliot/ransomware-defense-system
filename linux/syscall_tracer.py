SUSPICIOUS_SYSCALLS = {"ptrace", "chmod", "setuid", "mount", "init_module"}


def score_syscalls(syscalls):
    return min(100, sum(20 for syscall in syscalls if syscall in SUSPICIOUS_SYSCALLS))
