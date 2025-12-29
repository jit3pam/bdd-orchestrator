from typing import Callable
from bdd_orchestrator.config import max_retries
from bdd_orchestrator.recovery import manual_recovery


def run_step(step_name: str, step_fn: Callable):
    retries = max_retries()
    last_exception = None

    for attempt in range(1, retries + 1):
        try:
            return step_fn()
        except Exception as e:
            last_exception = e
            print(f"[Attempt {attempt}/{retries}] Step failed: {step_name}")

    manual_recovery(step_name, last_exception)
    return step_fn()
