from bdd_orchestrator.config import manual_mode_enabled


def manual_recovery(step_name: str, exception: Exception):
    if not manual_mode_enabled():
        raise exception

    print("\n" + "=" * 60)
    print(f"STEP FAILED: {step_name}")
    print(f"ERROR: {exception}")
    print("Manual recovery mode enabled.")
    print("Fix the issue manually in the application.")
    input("Press ENTER to continue execution...")
    print("Resuming execution...")
    print("=" * 60 + "\n")
