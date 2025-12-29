import sys
from bdd_orchestrator.config import manual_mode_enabled


def _is_interactive():
    return sys.stdin.isatty()


def manual_recovery(step_name: str, exception: Exception):
    if not manual_mode_enabled() or not _is_interactive():
        raise exception

    print("\n" + "=" * 60)
    print(f"STEP FAILED: {step_name}")
    print(f"ERROR: {exception}")
    print("Manual recovery mode enabled.")
    print("Fix the issue manually in the application.")
    input("Press ENTER to continue execution...")
    print("Resuming execution...")
    print("=" * 60 + "\n")
