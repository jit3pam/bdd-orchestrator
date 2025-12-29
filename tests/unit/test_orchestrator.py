import os
from bdd_orchestrator.orchestrator import run_step


def test_run_step_success():
    assert run_step("ok", lambda: 1) == 1


def test_run_step_retry_then_success():
    calls = {"count": 0}

    def flaky():
        calls["count"] += 1
        if calls["count"] < 2:
            raise ValueError("fail")
        return "ok"

    os.environ["BDD_STEP_RETRIES"] = "2"
    assert run_step("flaky", flaky) == "ok"
