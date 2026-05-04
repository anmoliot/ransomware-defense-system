def detect_bruteforce(failed_logins: int, window_minutes: int = 10) -> bool:
    return failed_logins >= 5 and window_minutes <= 10
