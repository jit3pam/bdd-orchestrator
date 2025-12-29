import sys
import builtins
from contextlib import contextmanager
from bdd_orchestrator.config import manual_mode_enabled

@contextmanager
def _block_input_when_non_interactive():
    if manual_mode_enabled() and sys.stdin.isatty():
        # interactive manual mode → allow input
        yield
        return

    original_input = builtins.input

    def blocked_input(*args, **kwargs):
        raise RuntimeError(
            "Blocking input() detected inside step execution. "
            "Manual interaction must be handled by the orchestrator, "
            "not inside step implementations."
        )

    builtins.input = blocked_input
    try:
        yield
    finally:
        builtins.input = original_input


def run_step(step_name, step_fn, retries=2):
    for attempt in range(1, retries + 1):
        try:
            with _block_input_when_non_interactive():
                step_fn()
            return  # success → exit
        except Exception as e:
            print(f"[Attempt {attempt}/{retries}] Step failed: {step_name}")

            if attempt == retries:
                from bdd_orchestrator.recovery import manual_recovery
                manual_recovery(step_name, e)
                raise  # ensure failure propagates if recovery doesn't resolve
            # else: silently retry

