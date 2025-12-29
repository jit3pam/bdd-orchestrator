import os
from bdd_orchestrator.orchestrator import run_step


def test_run_step_success(monkeypatch):
    monkeypatch.setenv("BDD_MANUAL_MODE", "false")
    monkeypatch.setattr("sys.stdin.isatty", lambda: False)

    called = []

    def step():
        called.append(True)

    run_step("ok", step)

    assert called == [True]



def test_run_step_retry_then_success(monkeypatch):
    monkeypatch.setenv("BDD_MANUAL_MODE", "false")
    monkeypatch.setattr("sys.stdin.isatty", lambda: False)

    calls = {"count": 0}

    def flaky():
        calls["count"] += 1
        if calls["count"] < 2:
            raise Exception("fail")

    run_step("retry", flaky, retries=2)

    assert calls["count"] == 2

