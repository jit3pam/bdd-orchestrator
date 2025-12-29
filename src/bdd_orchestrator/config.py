import os


def manual_mode_enabled() -> bool:
    return os.getenv("BDD_MANUAL_MODE", "false").lower() == "true"


def max_retries() -> int:
    return int(os.getenv("BDD_STEP_RETRIES", "1"))
